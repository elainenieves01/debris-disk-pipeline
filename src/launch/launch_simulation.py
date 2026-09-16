"""Launch a simulation locally or on a named remote machine (a university
cluster, a work computer, ...), per the config's `compute:` block. Either
way, the run starts inside a detached tmux session so it survives the
launching terminal (or a Claude Code session) closing.

    python src/launch/launch_simulation.py config/<file>.yaml

`run_simulation.py` itself is untouched -- calling it directly still works
exactly as before for a plain foreground local run.
"""

import os
import subprocess
import sys
from pathlib import Path

_SRC_DIR = os.path.dirname(os.path.abspath(__file__))
for _subdir in ("config_io", "launch"):
    sys.path.insert(0, os.path.join(_SRC_DIR, "..", _subdir))

from config_utils import read_config  # noqa: E402
from tmux_utils import session_name_for  # noqa: E402
import remote  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parents[2]
RUN_SIMULATION_SCRIPT = REPO_ROOT / "src" / "simulation" / "run_simulation.py"


def _tmux_has_session(session):
    result = subprocess.run(
        ["tmux", "has-session", "-t", session],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    return result.returncode == 0


def launch_local(config, config_path):
    """Run the simulation locally, inside a detached tmux session."""
    session = session_name_for(config)

    if _tmux_has_session(session):
        print(
            f"LAUNCH FAILED: tmux session '{session}' is already running "
            f"-- not starting a duplicate.",
            file=sys.stderr,
        )
        print(f"Attach with: tmux attach -t {session}", file=sys.stderr)
        sys.exit(1)

    config_abs_path = str(Path(config_path).resolve())
    inner_command = (
        f"{sys.executable} -u {RUN_SIMULATION_SCRIPT} '{config_abs_path}'; "
        f'ec=$?; echo; echo "[finished, exit $ec]"; exit $ec'
    )
    result = subprocess.run(
        ["tmux", "new-session", "-d", "-s", session, "bash", "-lc", inner_command],
        cwd=REPO_ROOT,
    )
    if result.returncode != 0:
        print(f"LAUNCH FAILED: could not start tmux session '{session}'.", file=sys.stderr)
        sys.exit(1)

    print(f"Launched tmux session '{session}' locally.")
    print()
    print("Reattach any time:")
    print(f"  tmux attach -t {session}")
    print("Detach again with Ctrl-b d -- the run keeps going after you detach.")


def dispatch(config, config_path):
    target = (config.get("compute") or {}).get("target", "local")

    if target == "local":
        launch_local(config, config_path)
    else:
        try:
            remote.remote_launch(config, config_path, target)
        except remote.RemoteLaunchError as error:
            print(f"LAUNCH FAILED: {error}", file=sys.stderr)
            sys.exit(1)


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage:")
        print("python src/launch/launch_simulation.py config/config.yaml")
        sys.exit(1)

    config_path = sys.argv[1]

    print(f"Reading configuration from: {config_path}")

    config = read_config(config_path)

    dispatch(config, config_path)
