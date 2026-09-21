"""Tests for src/launch/remote.py: pure argv builders and the
sync -> bootstrap -> launch step sequencing (subprocess mocked throughout).
Covers both a 'cluster' and a 'work_computer' named remote to confirm
nothing cluster-specific leaked into the generic implementation."""

import copy
import os
import shlex
import sys
from unittest.mock import patch, MagicMock

import pytest

_SRC = os.path.join(os.path.dirname(__file__), "..", "src")
for _sub in ("config_io", "launch"):
    sys.path.insert(0, os.path.join(_SRC, _sub))

import remote  # noqa: E402


CLUSTER_CFG = {
    "host": "login.cluster.university.edu",
    "username": "myusername",
    "remote_dir": "~/debris-disk-pipeline",
    "conda_env": "debris_pipeline",
}

WORK_COMPUTER_CFG = {
    "host": "work-pc.tailnet.ts.net",
    "username": "myusername",
    "remote_dir": "~/debris-disk-pipeline",
    "conda_env": "debris_pipeline",
}

CONFIG = {
    "simulation": {"name": "pytest_remote"},
    "compute": {
        "target": "cluster",
        "remotes": {
            "cluster": dict(CLUSTER_CFG),
            "work_computer": dict(WORK_COMPUTER_CFG),
        },
    },
}


def _remote_cfg(target="cluster"):
    return remote._remote_cfg(CONFIG, target)


def test_remote_cfg_applies_defaults():
    cfg = _remote_cfg()
    assert cfg["environment_file"] == "environment.yml"
    assert cfg["ssh_opts"] == []
    assert cfg["rsync_excludes"] == []


def test_remote_cfg_unknown_target_raises():
    with pytest.raises(remote.RemoteLaunchError):
        remote._remote_cfg(CONFIG, "nonexistent")


def test_build_mkdir_cmd():
    cmd = remote.build_mkdir_cmd(_remote_cfg("cluster"))
    assert cmd == [
        "ssh",
        "myusername@login.cluster.university.edu",
        "mkdir -p ~/debris-disk-pipeline",
    ]


def test_build_mkdir_cmd_for_work_computer():
    cmd = remote.build_mkdir_cmd(_remote_cfg("work_computer"))
    assert cmd == [
        "ssh",
        "myusername@work-pc.tailnet.ts.net",
        "mkdir -p ~/debris-disk-pipeline",
    ]


def test_build_rsync_cmd_includes_default_excludes():
    cmd = remote.build_rsync_cmd(_remote_cfg("cluster"), repo_root="/repo")
    assert cmd[0] == "rsync"
    for pattern in remote.DEFAULT_RSYNC_EXCLUDES:
        assert "--exclude" in cmd
        assert pattern in cmd
    assert cmd[-2] == "/repo/"
    assert cmd[-1] == "myusername@login.cluster.university.edu:~/debris-disk-pipeline/"


def test_build_rsync_cmd_appends_custom_excludes():
    cfg = _remote_cfg("cluster")
    cfg["rsync_excludes"] = ["*.h5"]
    cmd = remote.build_rsync_cmd(cfg, repo_root="/repo")
    assert "*.h5" in cmd


def _reparsed_by_remote_shell(cmd):
    """Simulate what actually happens to an argv list on the wire: ssh joins
    every element after the host with a single space and hands that one
    string to the remote's shell, which re-splits it from scratch (this is
    what let the original $1-unbound bug through -- asserting on the local
    argv list alone never exercises this round trip). Returns the argv the
    remote command ultimately sees, via the same word-splitting rules
    (shlex, POSIX mode) the remote shell applies."""
    host_idx = 1  # cmd[0] == "ssh"; cmd[1] == user@host (ssh_opts, if any, sit
    # between them, but tests here don't use ssh_opts)
    joined = " ".join(cmd[host_idx + 1:])
    return shlex.split(joined)


def test_build_bootstrap_cmd():
    cmd = remote.build_bootstrap_cmd(_remote_cfg("cluster"))
    assert cmd[:2] == ["ssh", "myusername@login.cluster.university.edu"]
    assert cmd[2:4] == ["bash", "-lc"]
    assert (
        "bootstrap_env.sh debris_pipeline environment.yml ~/debris-disk-pipeline"
        in cmd[4]
    )

    # Regression test for the real bug: after ssh's space-join + the remote
    # shell's re-split, bootstrap_env.sh must still receive exactly its three
    # positional arguments -- not zero (which is what "bash", "-lc",
    # unquoted_remote_command produced: bootstrap_env.sh ran with $1 unbound).
    # The third argument (remote_dir) matters in its own right too: without
    # it bootstrap_env.sh has no way to cd into the repo before resolving
    # environment.yml, which is relative to the repo, not to wherever the
    # SSH login happens to start (see the "EnvironmentFileNotFound" bug this
    # covers -- bootstrap_env.sh looking for environment.yml in $HOME).
    remote_argv = _reparsed_by_remote_shell(cmd)
    assert remote_argv[:2] == ["bash", "-lc"]
    script_and_args = shlex.split(remote_argv[2])
    assert script_and_args[-3:] == [
        "debris_pipeline", "environment.yml", "~/debris-disk-pipeline",
    ]
    assert script_and_args[0].endswith("bootstrap_env.sh")


def test_build_launch_cmd():
    cmd = remote.build_launch_cmd(_remote_cfg("cluster"), "sess1", "config/run.yaml")
    assert cmd[2:4] == ["bash", "-lc"]
    # cmd[4] is shlex-quoted as one token (see build_launch_cmd's comment);
    # undoing just that one layer should hand back the original, unquoted
    # remote_command string verbatim.
    assert shlex.split(cmd[4]) == [
        "~/debris-disk-pipeline/scripts/remote/launch_tmux.sh debris_pipeline "
        "sess1 ~/debris-disk-pipeline 'config/run.yaml'"
    ]

    # The real regression check: launch_tmux.sh must actually receive its
    # four positional arguments after ssh's join + the remote shell's parse.
    remote_argv = _reparsed_by_remote_shell(cmd)
    script_and_args = shlex.split(remote_argv[2])
    assert script_and_args[0].endswith("launch_tmux.sh")
    assert script_and_args[1:] == [
        "debris_pipeline", "sess1", "~/debris-disk-pipeline", "config/run.yaml",
    ]


def test_ssh_opts_extend_ssh_base():
    cfg = _remote_cfg("cluster")
    cfg["ssh_opts"] = ["-p", "2222"]
    cmd = remote.build_mkdir_cmd(cfg)
    assert cmd[:4] == ["ssh", "-p", "2222", "myusername@login.cluster.university.edu"]


def _mock_success():
    result = MagicMock()
    result.returncode = 0
    return result


def test_remote_launch_runs_steps_in_order():
    config = copy.deepcopy(CONFIG)
    with patch("remote.subprocess.run", return_value=_mock_success()) as mock_run:
        remote.remote_launch(config, "/repo/config/run.yaml", "cluster")

    assert mock_run.call_count == 4  # mkdir, rsync, bootstrap, tmux-launch
    step_cmds = [call.args[0] for call in mock_run.call_args_list]
    assert step_cmds[0][2] == "mkdir -p ~/debris-disk-pipeline"
    assert step_cmds[1][0] == "rsync"
    assert "bootstrap_env.sh" in step_cmds[2][4]
    assert "launch_tmux.sh" in step_cmds[3][4]


def test_remote_launch_works_for_work_computer_target():
    config = copy.deepcopy(CONFIG)
    with patch("remote.subprocess.run", return_value=_mock_success()) as mock_run:
        remote.remote_launch(config, "/repo/config/run.yaml", "work_computer")

    step_cmds = [call.args[0] for call in mock_run.call_args_list]
    assert "work-pc.tailnet.ts.net" in step_cmds[0][1]


def test_remote_launch_aborts_on_first_failure():
    config = copy.deepcopy(CONFIG)
    failing = MagicMock()
    failing.returncode = 1

    with patch(
        "remote.subprocess.run", side_effect=[_mock_success(), failing]
    ) as mock_run:
        with pytest.raises(remote.RemoteLaunchError):
            remote.remote_launch(config, "/repo/config/run.yaml", "cluster")

    assert mock_run.call_count == 2  # mkdir succeeded, rsync failed -> stop


def test_remote_launch_raises_on_oserror():
    config = copy.deepcopy(CONFIG)
    with patch("remote.subprocess.run", side_effect=OSError("no ssh binary")):
        with pytest.raises(remote.RemoteLaunchError):
            remote.remote_launch(config, "/repo/config/run.yaml", "cluster")


def test_remote_launch_unknown_target_raises_before_any_subprocess():
    config = copy.deepcopy(CONFIG)
    with patch("remote.subprocess.run") as mock_run:
        with pytest.raises(remote.RemoteLaunchError):
            remote.remote_launch(config, "/repo/config/run.yaml", "nonexistent")
    mock_run.assert_not_called()
