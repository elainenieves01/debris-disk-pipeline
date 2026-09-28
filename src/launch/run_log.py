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

Logging never stops a launch: if anything about summarizing the run fails, the
row is written with what could be read and the error goes in the notes column.
"""

import argparse
import contextlib
import copy
import csv
import io
import os
import platform
import sys
import tempfile
from datetime import datetime
from pathlib import Path

import yaml

_SRC_DIR = os.path.dirname(os.path.abspath(__file__))
for _subdir in ("config_io", "plotting", "diagnostics", "utilities", "mass_models",
                "simulation"):
    sys.path.insert(0, os.path.join(_SRC_DIR, "..", _subdir))

from provenance import (  # noqa: E402
    FROZEN_CONFIG_FILENAME,
    RUN_METADATA_FILENAME,
    collect_git_info,
)

REPO_ROOT = Path(__file__).resolve().parents[2]
LOG_PATH = REPO_ROOT / "simulation_log.csv"

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
    "notes",
]


# ============================================================
# Summarizing a config
# ============================================================

def _now():
    return datetime.now().astimezone().isoformat(timespec="seconds")


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


def append_row(row, path=None):
    path = Path(path or LOG_PATH)
    rows = read_log(path)
    rows.append(row)
    rows.sort(key=lambda r: _ts(r.get("sent_at", "")))
    write_log(rows, path)


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


def record_launch(config, config_path, target, path=None):
    """Append a row for a launch that just succeeded. Never raises."""
    try:
        row = make_row(config, config_path, target=target)
        append_row(row, path)
        print(f"Logged launch in {_repo_relative(path or LOG_PATH)}")
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


def refresh(outputs_dir, path=None):
    """Fill outcome fields for logged runs whose outputs/<name>/ is here."""
    rows = read_log(path)
    updated = 0
    for name in {r["run_name"] for r in rows}:
        metadata = _load_yaml(Path(outputs_dir) / name / RUN_METADATA_FILENAME)
        if not metadata or not metadata.get("created"):
            continue
        created = _ts(metadata["created"])
        # the launch that produced this metadata: latest one sent before it started
        candidates = [r for r in rows if r["run_name"] == name
                      and _ts(r.get("sent_at", "")) <= created]
        if not candidates:
            continue
        row = max(candidates, key=lambda r: _ts(r["sent_at"]))
        before = dict(row)
        row.update(_outcome_fields(metadata))
        updated += row != before
    write_log(rows, path)
    return updated


def backfill(outputs_dir, path=None):
    """Add a row for every outputs/<name>/run_metadata.yaml not yet logged."""
    rows = read_log(path)
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
    rows.sort(key=lambda r: _ts(r.get("sent_at", "")))
    write_log(rows, path)
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
    rows = read_log(path)
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
    rows.sort(key=lambda r: _ts(r.get("sent_at", "")))
    write_log(rows, path)
    return added


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

    sh = sub.add_parser("show", help="print the log")
    sh.add_argument("--last", type=int, default=None)

    for sp in (sub.choices["backfill"], sub.choices["refresh"]):
        sp.add_argument("--outputs", default=str(REPO_ROOT / "outputs"))
    return p.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)

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
    elif args.command == "backfill":
        added = backfill(args.outputs, args.log)
        print(f"Backfilled {len(added)} run(s): {', '.join(added) or 'none'}")
    elif args.command == "refresh":
        print(f"Updated {refresh(args.outputs, args.log)} run(s)")
    elif args.command == "legacy":
        added = log_legacy_repo(args.repo, args.ref, args.log)
        print(f"Logged {len(added)} legacy config(s): {', '.join(added) or 'none'}")
    elif args.command == "show":
        show(args.log, args.last)


if __name__ == "__main__":
    main()
