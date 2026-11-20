"""
push_outputs.py

Copy this machine's finished runs (outputs/<name>/ -- the .bin, checkpoint,
figures, everything) to the cluster (barbieri), which is the home of the full
outputs, and CHECK that every file arrived. Run it on any machine that holds
runs: the work computer after its runs finish (hourly timer in systemd/), or
this Mac to back up the runs it already has.

    python src/launch/push_outputs.py --dry-run     # list what it would do
    python src/launch/push_outputs.py               # copy + verify
    python src/launch/push_outputs.py --target barbieri

Per run folder:
  * still running (run_metadata.yaml present, no outcome)   -> skipped
  * not on the cluster yet                                  -> copied
  * on the cluster with the same run_uuid                   -> brought up to date
  * on the cluster as a different run of the same name, or
    a folder without run_metadata.yaml on either side that
    already exists there                                    -> NOT touched; reported
After every copy the folder is compared with the cluster's (file by file, by
size); a run is reported "verified" only when nothing differs. Nothing is
ever deleted on either side -- deleting local files is a separate, manual
step, done only after a run shows "verified".

Uses SSH BatchMode, so it never prompts: this machine needs an SSH key
registered on barbieri once (ssh-copy-id). It never touches git or
simulation_log.csv.
"""

import argparse
import fcntl
import os
import re
import shlex
import subprocess
import sys
from pathlib import Path

_SRC_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _SRC_DIR)

import run_log  # noqa: E402  (also puts src/utilities on sys.path)
from provenance import RUN_METADATA_FILENAME  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parents[2]
OUTPUTS_DIR = REPO_ROOT / "outputs"
LOCK_NAME = ".push_outputs.lock"
SAFE_NAME = re.compile(r"^[A-Za-z0-9._+-]+$")


def _ssh_opts(remote_cfg):
    return ["-o", "BatchMode=yes", "-o", "ConnectTimeout=15", *remote_cfg["ssh_opts"]]


def _remote_outputs(remote_cfg):
    return remote_cfg["remote_dir"].rstrip("/") + "/outputs"


def remote_listing(remote_cfg):
    """{run name: run_uuid or None} for every folder in the remote's outputs/."""
    user_host = f"{remote_cfg['username']}@{remote_cfg['host']}"
    path = _remote_outputs(remote_cfg)
    outputs = ('"$HOME"/' + shlex.quote(path[2:])) if path.startswith("~/") \
        else shlex.quote(path)
    script = (
        f"cd {outputs} 2>/dev/null || exit 0\n"
        f"for d in */; do n=${{d%/}}; "
        f"u=$(grep -m1 '^run_uuid:' \"$n/{RUN_METADATA_FILENAME}\" 2>/dev/null "
        f"| sed \"s/^run_uuid: *//; s/[\\\"']//g\"); echo \"$n|$u\"; done\n"
    )
    result = subprocess.run(
        ["ssh", *_ssh_opts(remote_cfg), user_host, "bash", "-s"],
        input=script, capture_output=True, text=True, timeout=120,
    )
    if result.returncode != 0:
        raise SystemExit(
            f"could not reach {user_host} without a password: {result.stderr.strip()}\n"
            "Register this machine's SSH key there once (it asks for the password):\n"
            f"  ssh-copy-id {user_host}"
        )
    listing = {}
    for line in result.stdout.splitlines():
        name, _, uuid = line.partition("|")
        if name:
            listing[name] = uuid or None
    return listing


def plan(local_runs, remote):
    """
    local_runs: {name: {"run_uuid": str|None, "outcome": str|None,
                        "has_metadata": bool}}
    remote:     {name: run_uuid or None} (names present on the cluster)

    Returns {name: (action, reason)}, action one of
    "copy", "update", "running", "conflict", "exists", "skip".
    """
    decisions = {}
    for name, info in sorted(local_runs.items()):
        if not SAFE_NAME.match(name):
            decisions[name] = ("skip", "unusual characters in the run name")
        elif info["has_metadata"] and not info["outcome"]:
            decisions[name] = ("running", "no outcome recorded yet")
        elif name not in remote:
            decisions[name] = ("copy", "not on the cluster yet")
        elif info["run_uuid"] and remote[name]:
            if info["run_uuid"] == remote[name]:
                decisions[name] = ("update", "same run already on the cluster")
            else:
                decisions[name] = (
                    "conflict",
                    f"the cluster has a different run named {name} "
                    f"(run_uuid {remote[name]}) -- not touched",
                )
        else:
            decisions[name] = (
                "exists",
                "a folder of this name is on the cluster and one side has no "
                "run_uuid to compare -- not touched",
            )
    return decisions


def local_runs(outputs_dir):
    runs = {}
    for d in sorted(Path(outputs_dir).iterdir()):
        if not d.is_dir():
            continue
        meta = run_log._load_yaml(d / RUN_METADATA_FILENAME) or {}
        runs[d.name] = {
            "run_uuid": meta.get("run_uuid"),
            "outcome": meta.get("outcome"),
            "has_metadata": (d / RUN_METADATA_FILENAME).exists(),
        }
    return runs


def _dest(remote_cfg, name):
    user_host = f"{remote_cfg['username']}@{remote_cfg['host']}"
    return f"{user_host}:{_remote_outputs(remote_cfg)}/{name}/"


def build_copy_cmd(remote_cfg, name, outputs_dir):
    """rsync one run folder to the cluster. Never deletes anything."""
    ssh = " ".join(["ssh", *_ssh_opts(remote_cfg)])
    return ["rsync", "-a", "--partial", "-e", ssh,
            f"{Path(outputs_dir) / name}/", _dest(remote_cfg, name)]


def build_verify_cmd(remote_cfg, name, outputs_dir):
    """Dry run listing every file whose size differs or is missing on the cluster."""
    ssh = " ".join(["ssh", *_ssh_opts(remote_cfg)])
    return ["rsync", "-rn", "--size-only", "--itemize-changes", "-e", ssh,
            f"{Path(outputs_dir) / name}/", _dest(remote_cfg, name)]


def verify(remote_cfg, name, outputs_dir):
    """(ok, differing lines). ok only when the dry run reports no file to send."""
    result = subprocess.run(build_verify_cmd(remote_cfg, name, outputs_dir),
                            capture_output=True, text=True)
    if result.returncode != 0:
        return False, [f"verify failed: {result.stderr.strip()}"]
    differing = [ln for ln in result.stdout.splitlines() if ln.startswith(">f")]
    return not differing, differing


def push(target="barbieri", outputs_dir=OUTPUTS_DIR, dry_run=False):
    """Copy + verify every finished local run. Returns {name: status}."""
    remotes = run_log.known_remotes()
    if target not in remotes:
        raise SystemExit(f"no compute.remotes entry named {target!r} in config/*.yaml")
    remote_cfg = remotes[target]
    decisions = plan(local_runs(outputs_dir), remote_listing(remote_cfg))
    status = {}
    for name, (action, reason) in decisions.items():
        if action in ("copy", "update"):
            print(f"  {name}: {reason}")
            if dry_run:
                status[name] = "would copy"
                continue
            if subprocess.run(build_copy_cmd(remote_cfg, name, outputs_dir)).returncode != 0:
                print(f"  {name}: copy failed, will retry next time", file=sys.stderr)
                status[name] = "copy failed"
                continue
            ok, differing = verify(remote_cfg, name, outputs_dir)
            status[name] = "verified" if ok else "MISMATCH"
            print(f"  {name}: {'verified on ' + target if ok else 'MISMATCH'}")
            for line in differing[:5]:
                print(f"      {line}", file=sys.stderr)
        elif action in ("conflict", "exists"):
            print(f"  {name}: {reason}", file=sys.stderr)
            status[name] = action
        else:
            status[name] = action
    counts = {}
    for s in status.values():
        counts[s] = counts.get(s, 0) + 1
    print(f"{target}: " + ", ".join(f"{n} {s}" for s, n in sorted(counts.items())))
    return status


def main(argv=None):
    p = argparse.ArgumentParser(description="Copy finished runs to the cluster and verify.")
    p.add_argument("--target", default="barbieri")
    p.add_argument("--outputs", default=str(OUTPUTS_DIR))
    p.add_argument("--dry-run", action="store_true", help="list what would be copied")
    args = p.parse_args(argv)

    Path(args.outputs).mkdir(parents=True, exist_ok=True)
    with open(Path(args.outputs) / LOCK_NAME, "w") as lock:
        try:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            print("another push_outputs.py is still copying; skipping this round")
            return
        print(f"--- push_outputs {run_log.now_iso()}")
        push(args.target, args.outputs, args.dry_run)


if __name__ == "__main__":
    main()
