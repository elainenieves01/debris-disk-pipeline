"""Sync + bootstrap + launch a simulation on a named remote machine over SSH
(a university cluster, a work computer, or any other host defined under a
config's `compute.remotes` block).

SSH access is assumed to be password/interactive (no keys, possibly 2FA), so
every subprocess here inherits the caller's stdio rather than capturing it --
prompts show up in the user's real terminal exactly as they would running
`ssh`/`rsync` by hand. Nothing here stores or types a password on the user's
behalf.

A failed step raises RemoteLaunchError and aborts the remaining steps -- a
failed launch means nothing is running yet, so (unlike send_ntfy) this must
never degrade silently.
"""

import subprocess
from pathlib import Path

from tmux_utils import session_name_for

REPO_ROOT = Path(__file__).resolve().parents[2]

DEFAULT_RSYNC_EXCLUDES = [
    ".git/",
    "outputs/",
    "logs/",
    "__pycache__/",
    "*.pyc",
    ".ipynb_checkpoints/",
]


class RemoteLaunchError(RuntimeError):
    """Raised when any remote-launch step fails. Never swallowed silently."""


def _remote_cfg(config, target):
    """Pull compute.remotes.<target> with defaults applied. Assumes
    validate_config() already confirmed the required keys are present --
    still raises a clear RemoteLaunchError if that was somehow skipped."""
    compute = config.get("compute") or {}
    remotes = compute.get("remotes") or {}
    if target not in remotes:
        available = ", ".join(sorted(remotes)) or "(none defined)"
        raise RemoteLaunchError(
            f"compute.target={target!r} has no matching entry under "
            f"compute.remotes. Available remotes: {available}."
        )
    remote = dict(remotes[target])
    remote.setdefault("environment_file", "environment.yml")
    remote.setdefault("ssh_opts", [])
    remote.setdefault("rsync_excludes", [])
    return remote


def _ssh_base(remote_cfg):
    return ["ssh", *remote_cfg["ssh_opts"], f"{remote_cfg['username']}@{remote_cfg['host']}"]


def build_mkdir_cmd(remote_cfg):
    return [*_ssh_base(remote_cfg), f"mkdir -p {remote_cfg['remote_dir']}"]


def build_rsync_cmd(remote_cfg, repo_root=REPO_ROOT):
    excludes = DEFAULT_RSYNC_EXCLUDES + list(remote_cfg["rsync_excludes"])
    cmd = ["rsync", "-avz", "--delete"]
    for pattern in excludes:
        cmd += ["--exclude", pattern]
    ssh_opts = remote_cfg["ssh_opts"]
    if ssh_opts:
        cmd += ["-e", "ssh " + " ".join(ssh_opts)]
    remote_dir = remote_cfg["remote_dir"].rstrip("/")
    cmd += [
        f"{repo_root}/",
        f"{remote_cfg['username']}@{remote_cfg['host']}:{remote_dir}/",
    ]
    return cmd


def build_bootstrap_cmd(remote_cfg):
    remote_dir = remote_cfg["remote_dir"].rstrip("/")
    remote_command = (
        f"{remote_dir}/scripts/remote/bootstrap_env.sh "
        f"{remote_cfg['conda_env']} {remote_cfg['environment_file']}"
    )
    return [*_ssh_base(remote_cfg), "bash", "-lc", remote_command]


def build_launch_cmd(remote_cfg, session, config_rel_path):
    remote_dir = remote_cfg["remote_dir"].rstrip("/")
    remote_command = (
        f"{remote_dir}/scripts/remote/launch_tmux.sh "
        f"{remote_cfg['conda_env']} {session} {remote_dir} '{config_rel_path}'"
    )
    return [*_ssh_base(remote_cfg), "bash", "-lc", remote_command]


def _run_inherited(cmd, step_name):
    """Run cmd with inherited stdio (password/2FA prompts show normally).
    Raises RemoteLaunchError on nonzero exit or launch failure."""
    try:
        result = subprocess.run(cmd)
    except OSError as error:
        raise RemoteLaunchError(f"{step_name} failed to start: {error}") from error

    if result.returncode != 0:
        raise RemoteLaunchError(
            f"{step_name} failed (exit {result.returncode}): {' '.join(cmd)}"
        )


def remote_launch(config, config_path, target):
    """Sync code, bootstrap the remote conda env, and launch the run inside
    a detached tmux session on compute.remotes[target]. Raises
    RemoteLaunchError on any step failure."""
    remote_cfg = _remote_cfg(config, target)
    session = session_name_for(config)
    try:
        config_rel_path = Path(config_path).resolve().relative_to(REPO_ROOT)
    except ValueError:
        config_rel_path = Path("config") / Path(config_path).name

    _run_inherited(build_mkdir_cmd(remote_cfg), "remote mkdir")
    _run_inherited(build_rsync_cmd(remote_cfg), "rsync")
    print(
        f"Synced code to {remote_cfg['username']}@{remote_cfg['host']}:"
        f"{remote_cfg['remote_dir']}"
    )

    _run_inherited(build_bootstrap_cmd(remote_cfg), "remote conda bootstrap")
    print(f"Remote conda env '{remote_cfg['conda_env']}' ready.")

    _run_inherited(
        build_launch_cmd(remote_cfg, session, config_rel_path), "remote tmux launch"
    )
    print(f"Launched tmux session '{session}' on {target}.")
    print()
    print("Reattach any time:")
    print(
        f'  ssh {remote_cfg["username"]}@{remote_cfg["host"]} '
        f'-t "tmux attach -t {session}"'
    )
    print("Detach again with Ctrl-b d -- the run keeps going after you disconnect.")
