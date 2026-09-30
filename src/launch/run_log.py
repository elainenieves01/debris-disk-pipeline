"""
run_log.py

A running log of every simulation sent out, one row per launch, in
simulation_log.csv at the repo root.

launch_simulation.py appends a row automatically each time it launches a run
(locally or on a remote). Each row records the disk limits, run length, output
interval, the integration timestep and total disk mass (both computed by
building the run's initial conditions exactly as run_simulation.py does, not
just read off the config), the mass model, where it was sent and when, and the
git commit it was launched from.

Commands, for runs that didn't go through the launcher:

    # a run started some other way (systemd, scripts/run_*.sh, run_simulation.py)
    python src/launch/run_log.py add config/<file>.yaml --target barbieri \\
        --sent 2026-09-01T10:00 --note "started by hand"

    # one row for every outputs/<name>/run_metadata.yaml not already logged
    python src/launch/run_log.py backfill

    # fill in finish time / outcome / runtime from outputs/<name>/run_metadata.yaml
    # (run after copying a remote run's outputs back)
    python src/launch/run_log.py refresh

    # configs from the old debris-disk-pipeline-legacy repo, as unconfirmed runs
    python src/launch/run_log.py legacy ~/debris-disk-pipeline-legacy

    # print the log
    python src/launch/run_log.py show --last 10

    # check barbieri's runs over SSH and update their rows (open a shared
    # login first with `ssh -fN <user>@<host>` if it asks for a password)
    python src/launch/run_log.py sync

Keeping the log current:
  * launch_simulation.py adds a row on every successful launch;
  * run_simulation.py updates its row when the run starts, finishes or fails
    (runs on this machine only -- a remote copy of the repo has no log), and
    adds a row if the run was started without the launcher;
  * `sync` does the same for remote runs, reading their run_metadata.yaml,
    tmux session and archive timestamp over SSH;
  * every automatic or command-line change is committed (simulation_log.csv
    only) and pushed. Set DEBRIS_RUN_LOG_AUTOCOMMIT=0, or pass --no-commit, to
    skip that.

Logging never stops a launch or a run: if anything fails, a warning is printed
and the run carries on.
"""

import argparse
import contextlib
import copy
import csv
import fcntl
import io
import os
import platform
import shlex
import subprocess
import sys
import tempfile
from datetime import datetime
from pathlib import Path

import yaml

_SRC_DIR = os.path.dirname(os.path.abspath(__file__))
for _subdir in ("config_io", "plotting", "diagnostics", "utilities", "mass_models",
                "simulation", "launch"):
    sys.path.insert(0, os.path.join(_SRC_DIR, "..", _subdir))

from provenance import (  # noqa: E402
    FROZEN_CONFIG_FILENAME,
    RUN_METADATA_FILENAME,
    collect_git_info,
)
from tmux_utils import sanitize_session_name, session_name_for  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parents[2]
REPO_LOG_PATH = REPO_ROOT / "simulation_log.csv"
LOG_PATH = REPO_LOG_PATH
LOCK_NAME = ".simulation_log.lock"

AUTOCOMMIT_ENV = "DEBRIS_RUN_LOG_AUTOCOMMIT"

# Clocks on different machines disagree a little, and the launcher stamps
# sent_at just before handing off, so a run's own start time can land slightly
# before or after it. Anything this close counts as the same launch.
LAUNCH_MATCH_TOLERANCE_S = 600

# A remote run whose archive hasn't been written for this long is flagged.
STALL_HOURS = 6

# Statuses sync keeps checking; anything else (completed, failed, ...) is final.
ACTIVE_STATUSES = ("launched", "starting", "running", "possibly stalled")

EARTH_MASS_TO_SOLAR_MASS = 3.0034896149156e-6  # as in run_simulation.py

COLUMNS = [
    "sent_at", "run_name", "target", "launched_from", "config",
    "git_commit", "git_dirty",
    "maxtime_yr", "output_every_yr", "dt_yr", "dt_basis", "integrator",
    "amin_AU", "amax_AU", "emin", "emax", "imin_deg", "imax_deg",
    "n_massive", "n_test", "disk_mass_earth", "mass_model", "mass_slope",
    "mp_mass_min_earth", "mp_mass_max_earth", "mass_source",
    "giant_planet", "exit_max_distance_AU",
    "status", "finished_at", "runtime_hr", "final_particle_count", "run_uuid",
    "last_checked", "notes",
]


# ============================================================
# Summarizing a config
# ============================================================

def now_iso():
    return datetime.now().astimezone().isoformat(timespec="seconds")


_now = now_iso


def _ts(value):
    """Parse an ISO timestamp for comparisons (naive ones taken as local time)."""
    try:
        return datetime.fromisoformat(str(value)).astimezone()
    except ValueError:
        return datetime.min.replace(tzinfo=datetime.now().astimezone().tzinfo)


def _g(value, digits=6):
    """Compact number formatting for the CSV."""
    if value is None or value == "":
        return ""
    try:
        return f"{float(value):.{digits}g}"
    except (TypeError, ValueError):
        return str(value)


def _mass_model(config):
    """(mass_model, mass_slope, mass_source) as described by the config."""
    mp = config.get("massive_planetesimals") or {}
    dist = mp.get("distribution")
    if dist is not None:
        mode = str(dist.get("mode", "total_mass")).lower()
        variable = dist.get("variable", "")
        source = dist.get("path", "") if mode == "csv" else (
            f"[{dist.get('min')}, {dist.get('max')}] {dist.get('unit', '')}".strip()
        )
        return f"power law in {variable} ({mode})", _g(dist.get("slope")), source

    for key, source in (
        ("total_disk_mass_earth", "total_disk_mass_earth"),
        ("total_mass_earth", "total_mass_earth"),
        ("individual_MP_mass_plutos", "individual_MP_mass_plutos"),
        ("mass_fraction_of_giant_planet", "mass_fraction_of_giant_planet"),
    ):
        if mp.get(key) is not None:
            return "uniform", "", f"{source} = {mp[key]}"
    return "", "", ""


def _giant_planet(config):
    gp = config.get("giant_planet")
    if not gp:
        return "none"
    return (f"{gp.get('mass_jupiter')} M_J, a = {gp.get('a')} AU, "
            f"e = {gp.get('e')}, i = {gp.get('inc_deg')} deg")


def _build_initial_conditions(config):
    """
    Build the run's t = 0 simulation exactly as run_simulation.py would (resume
    dumps ignored), with its chatter suppressed. Returns (sim, dt_basis).

    build_simulation writes distribution diagnostics (distribution.csv and
    figures) into the run's output directory, so it's pointed at a throwaway
    directory here to leave outputs/ untouched.
    """
    from run_simulation import build_simulation  # heavy import; only when needed

    cfg = copy.deepcopy(config)
    cfg.setdefault("simulation", {})["dump"] = False

    captured = io.StringIO()
    cwd = os.getcwd()
    with tempfile.TemporaryDirectory() as scratch:
        cfg["simulation"]["output_dir"] = scratch
        try:
            os.chdir(REPO_ROOT)  # distribution CSV paths are repo-relative
            with contextlib.redirect_stdout(captured):
                sim = build_simulation(cfg)
        finally:
            os.chdir(cwd)

    basis = ""
    for line in captured.getvalue().splitlines():
        if line.strip().startswith("Timestep:") and "(" in line:
            basis = line.split("(", 1)[1].rsplit("=", 1)[0].strip()
    return sim, basis


def summarize_config(config):
    """One log row's worth of run parameters (no launch / outcome fields)."""
    sim_cfg = config.get("simulation") or {}
    integ = config.get("integration") or {}
    disk = config.get("disk") or {}
    mp = config.get("massive_planetesimals") or {}
    tp = config.get("test_particles") or {}
    mass_model, mass_slope, mass_source = _mass_model(config)

    row = {
        "run_name": sim_cfg.get("name", ""),
        "maxtime_yr": _g(integ.get("maxtime")),
        "output_every_yr": _g(integ.get("time_step")),
        "integrator": integ.get("integrator", ""),
        "exit_max_distance_AU": _g(integ.get("exit_max_distance")),
        "amin_AU": _g(disk.get("amin")),
        "amax_AU": _g(disk.get("amax")),
        "emin": _g(disk.get("emin")),
        "emax": _g(disk.get("emax")),
        "imin_deg": _g(disk.get("imin_deg")),
        "imax_deg": _g(disk.get("imax_deg")),
        "n_massive": mp.get("N", ""),
        "n_test": tp.get("N", ""),
        "mass_model": mass_model,
        "mass_slope": mass_slope,
        "mass_source": mass_source,
        "giant_planet": _giant_planet(config),
    }

    notes = []
    try:
        sim, basis = _build_initial_conditions(config)
        masses = [p.m / EARTH_MASS_TO_SOLAR_MASS for p in sim.particles
                  if (p.name or "").startswith("MP_")]
        row["dt_yr"] = _g(sim.dt)
        row["dt_basis"] = basis
        if masses:
            row["disk_mass_earth"] = _g(sum(masses))
            row["mp_mass_min_earth"] = _g(min(masses))
            row["mp_mass_max_earth"] = _g(max(masses))
            if mass_model == "uniform" and max(masses) - min(masses) > 1e-9 * max(masses):
                row["mass_model"] = "uniform (config) but masses differ"
    except Exception as error:  # never block a launch over the log
        notes.append(f"could not build initial conditions: {type(error).__name__}: {error}")

    return row, notes


# ============================================================
# Reading and writing the log
# ============================================================

def read_log(path=None):
    path = Path(path or LOG_PATH)
    if not path.exists():
        return []
    with open(path, newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_log(rows, path=None):
    path = Path(path or LOG_PATH)
    with open(path, "w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=COLUMNS, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow({c: row.get(c, "") for c in COLUMNS})


@contextlib.contextmanager
def _lock(path):
    """Exclusive lock beside the log, so concurrent runs don't clobber it."""
    with open(Path(path).parent / LOCK_NAME, "w") as handle:
        fcntl.flock(handle, fcntl.LOCK_EX)
        yield


@contextlib.contextmanager
def edit_log(path=None):
    """Yield the log's rows for editing under the lock, then write them back sorted."""
    path = Path(path or LOG_PATH)
    with _lock(path):
        rows = read_log(path)
        yield rows
        rows.sort(key=lambda r: _ts(r.get("sent_at", "")))
        write_log(rows, path)


def append_row(row, path=None):
    with edit_log(path) as rows:
        rows.append(row)


def _git(*args, timeout=60):
    env = dict(os.environ, GIT_TERMINAL_PROMPT="0")  # never hang on a password prompt
    return subprocess.run(["git", "-C", str(REPO_ROOT), *args], capture_output=True,
                          text=True, timeout=timeout, env=env)


def commit_and_push(message, path=None):
    """
    Commit simulation_log.csv (and nothing else) and push it. Only touches the
    repo's own log, skipped when DEBRIS_RUN_LOG_AUTOCOMMIT=0 or outside a git
    checkout, and never raises. Returns True if a commit was made.
    """
    path = Path(path or LOG_PATH)
    if (os.environ.get(AUTOCOMMIT_ENV, "1") == "0"
            or path.resolve() != REPO_LOG_PATH.resolve()
            or not (REPO_ROOT / ".git").exists()):
        return False
    rel = REPO_LOG_PATH.name
    try:
        with _lock(path):
            if _git("diff", "--quiet", "HEAD", "--", rel).returncode == 0:
                return False
            commit = _git("commit", "--only", "-m", message, "--", rel)
            if commit.returncode != 0:
                print(f"(run log not committed: {commit.stderr.strip() or commit.stdout.strip()})",
                      file=sys.stderr)
                return False
        push = _git("push", timeout=120)
        if push.returncode != 0:
            print("(run log committed but not pushed -- run `git push` later: "
                  f"{push.stderr.strip().splitlines()[-1] if push.stderr.strip() else 'push failed'})",
                  file=sys.stderr)
        return True
    except Exception as error:
        print(f"(run log not committed: {type(error).__name__}: {error})", file=sys.stderr)
        return False


def make_row(config, config_path, *, target, sent_at=None, launched_from=None,
             git=None, status="launched", note=""):
    row, notes = summarize_config(config)
    if note:
        notes.insert(0, note)
    git = git if git is not None else collect_git_info(REPO_ROOT)
    row.update(
        sent_at=sent_at or _now(),
        target=target,
        launched_from=launched_from or platform.node(),
        config=_repo_relative(config_path),
        git_commit=git.get("short", "") if git.get("available") else "",
        git_dirty=("yes" if git.get("dirty") else "no") if git.get("available") else "",
        status=status,
        notes="; ".join(notes),
    )
    return row


def _repo_relative(path):
    if not path:
        return ""
    try:
        return str(Path(path).resolve().relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def record_launch(config, config_path, target, sent_at=None, path=None):
    """Append (and commit) a row for a launch that just succeeded. Never raises."""
    try:
        row = make_row(config, config_path, target=target, sent_at=sent_at)
        append_row(row, path)
        print(f"Logged launch in {_repo_relative(path or LOG_PATH)}")
        commit_and_push(f"Run log: launched {row['run_name']} on {target}", path)
    except Exception as error:
        print(f"(run log not updated: {type(error).__name__}: {error})", file=sys.stderr)


# ============================================================
# Outcomes from run_metadata.yaml
# ============================================================

def _load_yaml(path):
    try:
        with open(path, encoding="utf-8") as handle:
            data = yaml.safe_load(handle)
        return data if isinstance(data, dict) else None
    except (OSError, yaml.YAMLError):
        return None


def _outcome_fields(metadata):
    fields = {"run_uuid": metadata.get("run_uuid", "")}
    if metadata.get("outcome"):
        fields["status"] = metadata["outcome"]
    if metadata.get("finished"):
        fields["finished_at"] = str(metadata["finished"])
    if metadata.get("wall_runtime_seconds") is not None:
        fields["runtime_hr"] = _g(float(metadata["wall_runtime_seconds"]) / 3600, 4)
    if metadata.get("final_particle_count") is not None:
        fields["final_particle_count"] = metadata["final_particle_count"]
    return fields


def row_for_metadata(rows, name, metadata):
    """
    The launch row a run_metadata.yaml belongs to: the latest row for that
    run name sent no later than the run started (give or take clock skew).
    """
    if not metadata or not metadata.get("created"):
        return None
    created = _ts(metadata["created"]).timestamp()
    candidates = [r for r in rows if r["run_name"] == name
                  and _ts(r.get("sent_at", "")).timestamp()
                  <= created + LAUNCH_MATCH_TOLERANCE_S]
    return max(candidates, key=lambda r: _ts(r["sent_at"])) if candidates else None


def refresh(outputs_dir, path=None):
    """Fill outcome fields for logged runs whose outputs/<name>/ is here."""
    updated = 0
    with edit_log(path) as rows:
        for name in {r["run_name"] for r in rows}:
            metadata = _load_yaml(Path(outputs_dir) / name / RUN_METADATA_FILENAME)
            row = row_for_metadata(rows, name, metadata)
            if row is None:
                continue
            before = dict(row)
            row.update(_outcome_fields(metadata))
            updated += row != before
    return updated


def note_run_event(config, config_path, run_output_dir, path=None):
    """
    Called by run_simulation.py when a run starts, finishes or fails: update
    its row from run_metadata.yaml (adding one if it was started without the
    launcher) and commit it. Only acts where the log exists in a git checkout
    -- i.e. not in a remote copy of the repo. Never raises.
    """
    path = Path(path or LOG_PATH)
    try:
        if not path.exists() or not (REPO_ROOT / ".git").exists():
            return
        metadata = _load_yaml(Path(run_output_dir) / RUN_METADATA_FILENAME)
        if not metadata:
            return
        name = config["simulation"]["name"]
        with edit_log(path) as rows:
            row = row_for_metadata(rows, name, metadata)
            if row is None:
                row = make_row(config, config_path, target=f"local ({platform.node()})",
                               sent_at=str(metadata.get("created", "")),
                               note="started without launch_simulation.py")
                rows.append(row)
            row.update(_outcome_fields(metadata))
            if not metadata.get("outcome"):
                row["status"] = "running"
            row["last_checked"] = f"{_now()}: run reported {row['status']}"
            status = row["status"]
        commit_and_push(f"Run log: {name} {status}", path)
    except Exception as error:
        print(f"(run log not updated: {type(error).__name__}: {error})", file=sys.stderr)


def backfill(outputs_dir, path=None):
    """Add a row for every outputs/<name>/run_metadata.yaml not yet logged."""
    with edit_log(path) as rows:
        return _backfill_rows(rows, outputs_dir)


def _backfill_rows(rows, outputs_dir):
    logged = {r.get("run_uuid") for r in rows if r.get("run_uuid")}
    added = []
    for meta_path in sorted(Path(outputs_dir).glob(f"*/{RUN_METADATA_FILENAME}")):
        metadata = _load_yaml(meta_path)
        if not metadata or metadata.get("run_uuid") in logged:
            continue
        config = _load_yaml(meta_path.parent / FROZEN_CONFIG_FILENAME)
        if config is None:
            continue
        row = make_row(
            config,
            (metadata.get("config") or {}).get("source_path", ""),
            target=(metadata.get("host") or {}).get("hostname", ""),
            sent_at=str(metadata.get("created", "")),
            launched_from=(metadata.get("host") or {}).get("hostname", ""),
            git=metadata.get("git") or {},
            note="backfilled from run_metadata.yaml",
        )
        row.update(_outcome_fields(metadata))
        rows.append(row)
        added.append(row["run_name"])
    return added


# ============================================================
# Legacy pipeline (debris-disk-pipeline-legacy) configs
# ============================================================
#
# The legacy repo kept no run records (outputs/ was gitignored), so its configs
# are logged as "unconfirmed", dated by when each config was last committed.
# Its config layout predates this one -- dwarf_planets instead of
# massive_planetesimals, Noutputs instead of time_step, and always a giant
# planet -- so it's summarized here following the legacy run_simulation.py.

LEGACY_JUPITER_MASS_TO_SOLAR_MASS = 9.5479e-4  # legacy run_simulation.py


def summarize_legacy_config(config):
    """Log fields for a legacy-layout config (no simulation is built)."""
    sim_cfg = config.get("simulation") or {}
    integ = config.get("integration") or {}
    disk = config.get("disk") or {}
    dp = config.get("dwarf_planets") or {}
    tp = config.get("test_particles") or {}
    gp = config.get("giant_planet")
    notes = []

    maxtime = float(integ.get("maxtime", 0) or 0)
    n_out = integ.get("Noutputs")
    row = {
        "run_name": sim_cfg.get("name", ""),
        "maxtime_yr": _g(maxtime),
        "output_every_yr": _g(maxtime / float(n_out)) if n_out else _g(integ.get("time_step")),
        "integrator": integ.get("integrator", ""),
        "exit_max_distance_AU": _g(integ.get("exit_max_distance")),
        "amin_AU": _g(disk.get("amin")),
        "amax_AU": _g(disk.get("amax")),
        "emin": _g(disk.get("emin")),
        "emax": _g(disk.get("emax")),
        "imin_deg": _g(disk.get("imin_deg")),
        "imax_deg": _g(disk.get("imax_deg")),
        "n_massive": dp.get("N", ""),
        "n_test": tp.get("N", ""),
        "giant_planet": _giant_planet(config),
    }

    m_star = float((config.get("star") or {}).get("mass", 1.0))
    m_planet = float(gp["mass_jupiter"]) * LEGACY_JUPITER_MASS_TO_SOLAR_MASS if gp else 0.0
    if gp:
        # legacy: sim.dt = fraction * sim.particles[1].P (units yr, AU, Msun: G = 4 pi^2)
        period = (float(gp["a"]) ** 3 / (m_star + m_planet)) ** 0.5
        fraction = float(integ.get("timestep_fraction_of_planet_period", 0.1))
        row["dt_yr"] = _g(fraction * period)
        row["dt_basis"] = f"{fraction:g} x giant planet orbital period"
        if str(integ.get("integrator", "")).lower() == "ias15":
            notes.append("IAS15 is adaptive: dt_yr is only the initial timestep")

    n = int(dp.get("N", 0) or 0)
    per_body = None
    if dp.get("total_mass_earth") is not None:
        row["mass_source"] = f"dwarf_planets.total_mass_earth = {dp['total_mass_earth']}"
        per_body = float(dp["total_mass_earth"]) / n if n else None
    elif dp.get("mass_fraction_of_giant_planet") is not None:
        row["mass_source"] = (f"dwarf_planets.mass_fraction_of_giant_planet = "
                              f"{dp['mass_fraction_of_giant_planet']}")
        per_body = (float(dp["mass_fraction_of_giant_planet"]) * m_planet
                    / EARTH_MASS_TO_SOLAR_MASS)
    if n and per_body is not None:
        row.update(mass_model="uniform", disk_mass_earth=_g(per_body * n),
                   mp_mass_min_earth=_g(per_body), mp_mass_max_earth=_g(per_body))
    elif n == 0:
        row.update(mass_model="none (no massive bodies)", disk_mass_earth="0")

    return row, notes


def _git_out(repo, *args):
    import subprocess
    return subprocess.run(["git", "-C", str(repo), *args], capture_output=True,
                          text=True, check=True).stdout.strip()


def log_legacy_repo(repo, ref="origin/main", path=None):
    """Log every config/*.yaml at `ref` of the legacy repo as unconfirmed."""
    repo = Path(repo).expanduser()
    with edit_log(path) as rows:
        return _legacy_rows(rows, repo, ref)


def _legacy_rows(rows, repo, ref):
    logged = {r.get("config") for r in rows}
    added = []
    names = _git_out(repo, "ls-tree", "--name-only", ref, "config/").splitlines()
    for rel in sorted(n for n in names if n.endswith((".yaml", ".yml"))):
        label = f"debris-disk-pipeline-legacy:{rel}"
        if label in logged:
            continue
        config = yaml.safe_load(_git_out(repo, "show", f"{ref}:{rel}")) or {}
        date, commit = _git_out(repo, "log", "-1", "--format=%aI %h", ref, "--", rel).split()
        row, notes = summarize_legacy_config(config)
        notes = [f"legacy pipeline config ({ref}); NOT confirmed it was ever run -- "
                 "sent_at is when the config was last committed"] + notes
        row.update(sent_at=date, target="unknown (legacy)", config=label,
                   git_commit=f"legacy {commit}", status="unconfirmed",
                   notes="; ".join(notes))
        rows.append(row)
        added.append(row["run_name"])
    return added


# ============================================================
# Remote runs
# ============================================================

def known_remotes():
    """compute.remotes entries found across config/*.yaml, by name."""
    import remote  # launcher module; imported here to keep run_log light

    found = {}
    for config_path in sorted((REPO_ROOT / "config").glob("*.yaml")):
        config = _load_yaml(config_path) or {}
        for name in ((config.get("compute") or {}).get("remotes") or {}):
            if name not in found:
                found[name] = remote._remote_cfg(config, name)
    return found


def _session_for_row(row):
    config = _load_yaml(REPO_ROOT / row["config"]) if row.get("config") else None
    if config and (config.get("simulation") or {}).get("name") == row["run_name"]:
        return session_name_for(config)
    return sanitize_session_name(row["run_name"])


def _probe_script(remote_dir, runs):
    """Shell script printing each run's metadata, tmux state and archive mtime."""
    outputs = shlex.quote(remote_dir.rstrip("/") + "/outputs")
    lines = [f"cd {outputs} 2>/dev/null || {{ echo '=== __no_outputs__'; exit 0; }}"]
    for name, session in runs:
        q = shlex.quote(name)
        lines.append(
            f"echo '=== '{q}; cat {q}/{RUN_METADATA_FILENAME} 2>/dev/null; "
            f"echo '--- tmux'; tmux has-session -t ={shlex.quote(session)} 2>/dev/null "
            f"&& echo alive || echo gone; "
            f"echo '--- archive'; stat -c %Y {q}/{q}.bin 2>/dev/null || echo none"
        )
    lines.append("echo '=== __now__'; date +%s")
    return "\n".join(lines)


def _parse_probe(text):
    """{name: {"metadata": dict|None, "tmux": str, "archive": int|None}}, remote now."""
    runs, now, name, section, buf = {}, None, None, None, []

    def flush():
        if name is None or name.startswith("__"):
            return
        entry = runs.setdefault(name, {"metadata": None, "tmux": "gone", "archive": None})
        body = "\n".join(buf).strip()
        if section is None and body:
            try:
                data = yaml.safe_load(body)
                entry["metadata"] = data if isinstance(data, dict) else None
            except yaml.YAMLError:
                pass
        elif section == "tmux":
            entry["tmux"] = body or "gone"
        elif section == "archive":
            entry["archive"] = int(body) if body.isdigit() else None

    for line in text.splitlines():
        if line.startswith("=== "):
            flush()
            name, section, buf = line[4:].strip(), None, []
        elif line.startswith("--- "):
            flush()
            section, buf = line[4:].strip(), []
        else:
            if name == "__now__" and line.strip().isdigit():
                now = int(line.strip())
            buf.append(line)
    flush()
    return runs, now


def _remote_status(row, probe, remote_now):
    """(fields to set, human-readable check) for one row from its probe result."""
    metadata = probe.get("metadata")
    alive = probe.get("tmux") == "alive"
    started = (metadata and metadata.get("created")
               and row_for_metadata([row], row["run_name"], metadata) is row)
    if started:
        fields = _outcome_fields(metadata)
        if metadata.get("outcome"):
            return fields, f"finished ({metadata['outcome']})"
        if alive:
            if probe.get("archive") and remote_now:
                age_h = (remote_now - probe["archive"]) / 3600
                fields["status"] = "possibly stalled" if age_h > STALL_HOURS else "running"
                return fields, f"tmux alive, archive last written {age_h:.1f} h ago"
            fields["status"] = "running"
            return fields, "tmux alive, no archive written yet"
        fields["status"] = "stopped (no outcome)"
        return fields, "tmux session gone and no outcome recorded -- killed or crashed?"
    if alive:
        return {"status": "starting"}, "tmux alive, run_metadata.yaml not written yet"
    return {}, "no run_metadata.yaml for this launch and no tmux session"


def _clean_manual_notes(notes):
    """Drop the one-off status notes written before sync existed."""
    parts = [p for p in notes.split("; ") if p and "tmux session alive" not in p]
    return "; ".join(parts)


def sync_remote(target=None, path=None):
    """
    Check every active remote row over SSH and update its status. Uses SSH
    BatchMode, so it relies on an existing shared connection or key -- it never
    prompts. Returns a list of (run_name, old_status, new_status, check).
    """
    remotes = known_remotes()
    rows = read_log(path)
    active = [r for r in rows if r.get("status") in ACTIVE_STATUSES
              and r.get("target") in remotes and (target is None or r["target"] == target)]
    changes = []
    for name in sorted({r["target"] for r in active}):
        remote_cfg = remotes[name]
        runs = sorted({(r["run_name"], _session_for_row(r)) for r in active
                       if r["target"] == name})
        user_host = f"{remote_cfg['username']}@{remote_cfg['host']}"
        cmd = ["ssh", "-o", "BatchMode=yes", "-o", "ConnectTimeout=15",
               *remote_cfg["ssh_opts"], user_host, "bash", "-s"]
        result = subprocess.run(cmd, input=_probe_script(remote_cfg["remote_dir"], runs),
                                capture_output=True, text=True, timeout=120)
        if result.returncode != 0:
            raise SystemExit(
                f"could not reach {name} ({user_host}) without a password: "
                f"{result.stderr.strip()}\nOpen a shared login first, then rerun sync:\n"
                f"  ssh -fN {user_host}"
            )
        probes, remote_now = _parse_probe(result.stdout)
        checked_at = _now()
        with edit_log(path) as live_rows:
            for row in live_rows:
                if row.get("target") != name or row.get("status") not in ACTIVE_STATUSES:
                    continue
                if (row["run_name"], _session_for_row(row)) not in runs:
                    continue
                fields, check = _remote_status(row, probes.get(row["run_name"], {}),
                                               remote_now)
                old = row.get("status", "")
                row.update(fields)
                row["last_checked"] = f"{checked_at} ({name}): {check}"
                row["notes"] = _clean_manual_notes(row.get("notes", ""))
                changes.append((row["run_name"], old, row.get("status", ""), check))
    return changes


# ============================================================
# CLI
# ============================================================

SHOW_COLUMNS = [
    ("sent_at", 16), ("run_name", 34), ("target", 10), ("maxtime_yr", 9),
    ("dt_yr", 9), ("amin_AU", 6), ("amax_AU", 6), ("n_massive", 5),
    ("disk_mass_earth", 10), ("mass_model", 26), ("status", 10),
]


def show(path=None, last=None):
    rows = read_log(path)
    if last:
        rows = rows[-last:]
    header = "  ".join(name[:width].ljust(width) for name, width in SHOW_COLUMNS)
    print(header)
    print("-" * len(header))
    for row in rows:
        print("  ".join(str(row.get(name, ""))[:width].ljust(width)
                        for name, width in SHOW_COLUMNS))


def parse_args(argv=None):
    p = argparse.ArgumentParser(description="Log of every simulation sent out.")
    p.add_argument("--log", default=None,
                   help=f"log file (default: {LOG_PATH.relative_to(REPO_ROOT)})")
    p.add_argument("--no-commit", action="store_true",
                   help="don't commit and push the log after changing it")
    sub = p.add_subparsers(dest="command", required=True)

    add = sub.add_parser("add", help="log a run that didn't go through the launcher")
    add.add_argument("config")
    add.add_argument("--target", default=None,
                     help="where it ran (default: the config's compute.target, else local)")
    add.add_argument("--sent", default=None,
                     help="when it was sent, ISO date/time (default: now)")
    add.add_argument("--note", default="")

    sub.add_parser("backfill", help="log every run in outputs/ not already logged")
    sub.add_parser("refresh", help="fill outcomes from outputs/<name>/run_metadata.yaml")

    leg = sub.add_parser("legacy", help="log a debris-disk-pipeline-legacy checkout's "
                                        "configs as unconfirmed runs")
    leg.add_argument("repo", help="path to the legacy repo checkout")
    leg.add_argument("--ref", default="origin/main")

    sy = sub.add_parser("sync", help="check remote runs over SSH and update their rows")
    sy.add_argument("--target", default=None, help="only this remote (default: all)")

    sh = sub.add_parser("show", help="print the log")
    sh.add_argument("--last", type=int, default=None)

    for sp in (sub.choices["backfill"], sub.choices["refresh"]):
        sp.add_argument("--outputs", default=str(REPO_ROOT / "outputs"))
    return p.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)
    message = _run_command(args)
    if message and not args.no_commit:
        commit_and_push(message, args.log)


def _run_command(args):
    """Run one CLI command; returns a commit message if the log changed."""
    if args.command == "add":
        config = _load_yaml(args.config)
        if config is None:
            raise SystemExit(f"could not read config {args.config}")
        target = args.target or (config.get("compute") or {}).get("target", "local")
        sent = args.sent
        if sent:
            sent = datetime.fromisoformat(sent).astimezone().isoformat(timespec="seconds")
        row = make_row(config, args.config, target=target, sent_at=sent,
                       note=args.note or "logged by hand")
        append_row(row, args.log)
        print(f"Logged {row['run_name']} ({target}, sent {row['sent_at']})")
        return f"Run log: add {row['run_name']}"
    if args.command == "backfill":
        added = backfill(args.outputs, args.log)
        print(f"Backfilled {len(added)} run(s): {', '.join(added) or 'none'}")
        return f"Run log: backfill {len(added)} run(s)" if added else None
    if args.command == "refresh":
        updated = refresh(args.outputs, args.log)
        print(f"Updated {updated} run(s)")
        return f"Run log: refresh {updated} run(s)" if updated else None
    if args.command == "legacy":
        added = log_legacy_repo(args.repo, args.ref, args.log)
        print(f"Logged {len(added)} legacy config(s): {', '.join(added) or 'none'}")
        return f"Run log: {len(added)} legacy config(s)" if added else None
    if args.command == "sync":
        changes = sync_remote(args.target, args.log)
        for name, old, new, check in changes:
            arrow = f"{old} -> {new}" if old != new else new
            print(f"  {name:40s} {arrow:32s} {check}")
        moved = sum(old != new for _, old, new, _ in changes)
        print(f"Checked {len(changes)} run(s); {moved} changed status")
        return f"Run log: sync ({moved} status change(s))" if changes else None
    if args.command == "show":
        show(args.log, args.last)
    return None


if __name__ == "__main__":
    main()
