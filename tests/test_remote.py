"""Tests for src/launch/remote.py: pure argv builders and the
sync -> bootstrap -> launch step sequencing (subprocess mocked throughout).
Covers both a 'cluster' and a 'work_computer' named remote to confirm
nothing cluster-specific leaked into the generic implementation."""

import copy
import os
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


def test_build_bootstrap_cmd():
    cmd = remote.build_bootstrap_cmd(_remote_cfg("cluster"))
    assert cmd[:2] == ["ssh", "myusername@login.cluster.university.edu"]
    assert cmd[2:4] == ["bash", "-lc"]
    assert "bootstrap_env.sh debris_pipeline environment.yml" in cmd[4]


def test_build_launch_cmd():
    cmd = remote.build_launch_cmd(_remote_cfg("cluster"), "sess1", "config/run.yaml")
    assert "launch_tmux.sh debris_pipeline sess1 ~/debris-disk-pipeline 'config/run.yaml'" in cmd[4]


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
