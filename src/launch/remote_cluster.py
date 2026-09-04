"""Sync + bootstrap + launch a simulation on a remote cluster over SSH.

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


def _cluster_cfg(config):
    """Pull compute.cluster with defaults applied. Assumes validate_config()
    already confirmed the required keys are present."""
    compute = config.get("compute") or {}
    cluster = dict(compute.get("cluster") or {})
    cluster.setdefault("environment_file", "environment.yml")
    cluster.setdefault("ssh_opts", [])
    cluster.setdefault("rsync_excludes", [])
    return cluster


def _ssh_base(cluster_cfg):
    return ["ssh", *cluster_cfg["ssh_opts"], f"{cluster_cfg['username']}@{cluster_cfg['host']}"]


def build_mkdir_cmd(cluster_cfg):
    return [*_ssh_base(cluster_cfg), f"mkdir -p {cluster_cfg['remote_dir']}"]


def build_rsync_cmd(cluster_cfg, repo_root=REPO_ROOT):
    excludes = DEFAULT_RSYNC_EXCLUDES + list(cluster_cfg["rsync_excludes"])
    cmd = ["rsync", "-avz", "--delete"]
    for pattern in excludes:
        cmd += ["--exclude", pattern]
    ssh_opts = cluster_cfg["ssh_opts"]
    if ssh_opts:
        cmd += ["-e", "ssh " + " ".join(ssh_opts)]
    remote_dir = cluster_cfg["remote_dir"].rstrip("/")
    cmd += [
        f"{repo_root}/",
        f"{cluster_cfg['username']}@{cluster_cfg['host']}:{remote_dir}/",
    ]
    return cmd


def build_bootstrap_cmd(cluster_cfg):
    remote_dir = cluster_cfg["remote_dir"].rstrip("/")
    remote_command = (
        f"{remote_dir}/scripts/remote/bootstrap_env.sh "
        f"{cluster_cfg['conda_env']} {cluster_cfg['environment_file']}"
    )
    return [*_ssh_base(cluster_cfg), "bash", "-lc", remote_command]


def build_launch_cmd(cluster_cfg, session, config_rel_path):
    remote_dir = cluster_cfg["remote_dir"].rstrip("/")
    remote_command = (
        f"{remote_dir}/scripts/remote/launch_tmux.sh "
        f"{cluster_cfg['conda_env']} {session} {remote_dir} '{config_rel_path}'"
    )
    return [*_ssh_base(cluster_cfg), "bash", "-lc", remote_command]


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


def remote_launch(config, config_path):
    """Sync code, bootstrap the remote conda env, and launch the run inside
    a detached tmux session on the cluster. Raises RemoteLaunchError on any
    step failure."""
    cluster_cfg = _cluster_cfg(config)
    session = session_name_for(config)
    try:
        config_rel_path = Path(config_path).resolve().relative_to(REPO_ROOT)
    except ValueError:
        config_rel_path = Path("config") / Path(config_path).name

    _run_inherited(build_mkdir_cmd(cluster_cfg), "remote mkdir")
    _run_inherited(build_rsync_cmd(cluster_cfg), "rsync")
    print(
        f"Synced code to {cluster_cfg['username']}@{cluster_cfg['host']}:"
        f"{cluster_cfg['remote_dir']}"
    )

    _run_inherited(build_bootstrap_cmd(cluster_cfg), "remote conda bootstrap")
    print(f"Remote conda env '{cluster_cfg['conda_env']}' ready.")

    _run_inherited(
        build_launch_cmd(cluster_cfg, session, config_rel_path), "remote tmux launch"
    )
    print(f"Launched tmux session '{session}' on the cluster.")
    print()
    print("Reattach any time:")
    print(
        f'  ssh {cluster_cfg["username"]}@{cluster_cfg["host"]} '
        f'-t "tmux attach -t {session}"'
    )
    print("Detach again with Ctrl-b d -- the run keeps going after you disconnect.")
