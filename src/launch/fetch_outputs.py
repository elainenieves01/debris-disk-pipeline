"""
fetch_outputs.py

Copy finished remote runs' output folders (outputs/<name>/ on barbieri or any
other compute.remotes host) into this checkout's outputs/, so every machine
that runs this keeps its own copy of the results.

    python src/launch/fetch_outputs.py              # copy anything new
    python src/launch/fetch_outputs.py --dry-run    # only list what it would copy
    python src/launch/fetch_outputs.py --target barbieri

A run is "finished" when its remote run_metadata.yaml records an outcome
(completed or failed); runs still going, or killed before recording one, are
left alone. A run is skipped when this machine already has it -- a local
run_metadata.yaml with the same run_uuid and an outcome, plus a local .bin the
same size as the remote one (git tracks a run's metadata and reports but not
its .bin, so a checkout can have the first without the second). A local
folder that belongs to a *different* run of the same name is never
overwritten; it's reported instead.

Files already here are never replaced, except the .bin itself: a run's
reports and figures often get revised (and committed) after it finishes, and
the remote's originals mustn't overwrite them. run_metadata.yaml is copied
last, and an interrupted copy is simply picked up again next time.

Uses SSH BatchMode, so it never prompts -- it needs a key (or an open shared
connection) for each remote. It never touches git or simulation_log.csv, which
is what lets it run unattended on several machines at once (launchd/ and
systemd/ hold the hourly schedules); run `run_log.py sync` to update the log.
"""

import argparse
import fcntl
import os
import re
import shlex
import subprocess
import sys
from pathlib import Path

import yaml

_SRC_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _SRC_DIR)

import run_log  # noqa: E402  (also puts src/utilities on sys.path)
from provenance import RUN_METADATA_FILENAME  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parents[2]
OUTPUTS_DIR = REPO_ROOT / "outputs"
LOCK_NAME = ".fetch_outputs.lock"

# rsync's remote path goes through the remote shell, so only plain run names.
SAFE_NAME = re.compile(r"^[A-Za-z0-9._+-]+$")


def _ssh_opts(remote_cfg):
    return ["-o", "BatchMode=yes", "-o", "ConnectTimeout=15", *remote_cfg["ssh_opts"]]


def _list_script(remote_dir):
    """Shell script printing, per remote run, its run_metadata.yaml and .bin size."""
    outputs = shlex.quote(remote_dir.rstrip("/") + "/outputs")
    return (
        f"cd {outputs} 2>/dev/null || exit 0\n"
        f"for d in */; do n=${{d%/}}; "
        f"[ -f \"$n/{RUN_METADATA_FILENAME}\" ] || continue; "
        f"echo \"=== $n\"; cat \"$n/{RUN_METADATA_FILENAME}\"; "
        # GNU stat on the cluster, BSD stat as a fallback
        f"echo '--- binsize'; stat -c %s \"$n/$n.bin\" 2>/dev/null "
        f"|| stat -f %z \"$n/$n.bin\" 2>/dev/null || echo none; done\n"
    )


def _parse_listing(text):
    """{name: {"metadata": dict|None, "bin_size": int|None}} from _list_script output."""
    runs, name, section, buf = {}, None, None, []

    def flush():
        if name is None:
            return
        entry = runs.setdefault(name, {"metadata": None, "bin_size": None})
        body = "\n".join(buf).strip()
        if section is None and body:
            try:
                data = yaml.safe_load(body)
                entry["metadata"] = data if isinstance(data, dict) else None
            except yaml.YAMLError:
                pass
        elif section == "binsize" and body.isdigit():
            entry["bin_size"] = int(body)

    for line in text.splitlines():
        if line.startswith("=== "):
            flush()
            name, section, buf = line[4:].strip(), None, []
        elif line.startswith("--- "):
            flush()
            section, buf = line[4:].strip(), []
        else:
            buf.append(line)
    flush()
    return {n: r for n, r in runs.items() if r["metadata"]}


def remote_runs(remote_cfg):
    """{run name: {"metadata", "bin_size"}} for every run folder on the remote."""
    user_host = f"{remote_cfg['username']}@{remote_cfg['host']}"
    result = subprocess.run(
        ["ssh", *_ssh_opts(remote_cfg), user_host, "bash", "-s"],
        input=_list_script(remote_cfg["remote_dir"]),
        capture_output=True, text=True, timeout=120,
    )
    if result.returncode != 0:
        raise SystemExit(
            f"could not reach {user_host} without a password: {result.stderr.strip()}\n"
            "Register this machine's SSH key there once (it asks for the password):\n"
            f"  ssh-copy-id {user_host}"
        )
    return _parse_listing(result.stdout)


def plan(runs, outputs_dir):
    """
    Decide what to do with each remote run. Returns {name: (action, reason)},
    action one of "fetch", "have", "running", "conflict", "skip".

    "have" needs the same run_uuid with an outcome AND, when the remote run
    has an archive, a local <name>.bin of the same size -- the repo tracks
    run_metadata.yaml and reports but not .bin files, so a checkout can hold
    a run's metadata without its archive.
    """
    decisions = {}
    for name, remote in sorted(runs.items()):
        remote_meta = remote["metadata"]
        if not SAFE_NAME.match(name):
            decisions[name] = ("skip", "unusual characters in the run name")
            continue
        if not remote_meta.get("outcome"):
            decisions[name] = ("running", "no outcome recorded yet")
            continue
        run_dir = Path(outputs_dir) / name
        local_meta = run_log._load_yaml(run_dir / RUN_METADATA_FILENAME)
        local_bin = run_dir / f"{name}.bin"
        local_size = local_bin.stat().st_size if local_bin.exists() else None
        if not local_meta:
            decisions[name] = ("fetch", f"finished ({remote_meta['outcome']}), not here yet")
        elif local_meta.get("run_uuid") != remote_meta.get("run_uuid"):
            decisions[name] = (
                "conflict",
                f"local outputs/{name}/ is a different run "
                f"(run_uuid {local_meta.get('run_uuid') or 'missing'}) -- not overwritten",
            )
        elif not local_meta.get("outcome"):
            decisions[name] = ("fetch", "local copy predates the run finishing")
        elif remote["bin_size"] is not None and local_size != remote["bin_size"]:
            decisions[name] = ("fetch", "archive missing here" if local_size is None
                               else "local archive incomplete")
        else:
            decisions[name] = ("have", "already here")
    return decisions


def build_rsync_cmds(remote_cfg, name, outputs_dir, has_archive=True):
    """
    The rsyncs that copy one run, in order:
      1. everything but the archive and run_metadata.yaml, never replacing a
         file already here -- reports and figures get revised locally after a
         run (and committed), and the remote's originals mustn't clobber them;
      2. <name>.bin, which is never edited locally, so it's always brought
         up to date (resuming a partial copy);
      3. run_metadata.yaml, last, once the rest is in place.
    """
    user_host = f"{remote_cfg['username']}@{remote_cfg['host']}"
    src = f"{user_host}:{remote_cfg['remote_dir'].rstrip('/')}/outputs/{name}/"
    dest = f"{Path(outputs_dir) / name}/"
    base = ["rsync", "-a", "--partial", "-e", " ".join(["ssh", *_ssh_opts(remote_cfg)])]
    archive = f"{name}.bin"
    cmds = [[*base, "--ignore-existing", "--exclude", RUN_METADATA_FILENAME,
             "--exclude", archive, src, dest]]
    if has_archive:
        cmds.append([*base, src + archive, dest])
    cmds.append([*base, src + RUN_METADATA_FILENAME, dest])
    return cmds


def fetch(target=None, outputs_dir=OUTPUTS_DIR, dry_run=False):
    """Copy every finished, not-yet-here run from each remote. Returns the copied names."""
    remotes = run_log.known_remotes()
    if target is not None:
        if target not in remotes:
            raise SystemExit(f"no compute.remotes entry named {target!r} in config/*.yaml")
        remotes = {target: remotes[target]}
    copied = []
    for remote_name, remote_cfg in sorted(remotes.items()):
        runs = remote_runs(remote_cfg)
        decisions = plan(runs, outputs_dir)
        for name, (action, reason) in decisions.items():
            if action in ("fetch", "conflict"):
                print(f"  [{remote_name}] {name}: {reason}")
            if action != "fetch" or dry_run:
                continue
            Path(outputs_dir, name).mkdir(parents=True, exist_ok=True)
            for cmd in build_rsync_cmds(remote_cfg, name, outputs_dir,
                                        has_archive=runs[name]["bin_size"] is not None):
                if subprocess.run(cmd).returncode != 0:
                    print(f"  [{remote_name}] {name}: copy failed, will retry next time",
                          file=sys.stderr)
                    break
            else:
                copied.append(name)
                print(f"  [{remote_name}] {name}: copied")
        held = sum(a == "have" for a, _ in decisions.values())
        going = sum(a == "running" for a, _ in decisions.values())
        print(f"{remote_name}: {held} already here, {going} still running")
    return copied


def main(argv=None):
    p = argparse.ArgumentParser(description="Copy finished remote runs into outputs/.")
    p.add_argument("--target", default=None, help="only this remote (default: all)")
    p.add_argument("--outputs", default=str(OUTPUTS_DIR))
    p.add_argument("--dry-run", action="store_true", help="list what would be copied")
    args = p.parse_args(argv)

    Path(args.outputs).mkdir(parents=True, exist_ok=True)
    with open(Path(args.outputs) / LOCK_NAME, "w") as lock:
        try:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            print("another fetch_outputs.py is still copying; skipping this round")
            return
        print(f"--- fetch_outputs {run_log.now_iso()}")
        copied = fetch(args.target, args.outputs, args.dry_run)
        if not args.dry_run:
            print(f"Copied {len(copied)} run(s): {', '.join(copied) or 'none'}")


if __name__ == "__main__":
    main()
