"""Tests for src/launch/remote_cluster.py: pure argv builders and the
sync -> bootstrap -> launch step sequencing (subprocess mocked throughout)."""

import copy
import os
import sys
from unittest.mock import patch, MagicMock

import pytest

_SRC = os.path.join(os.path.dirname(__file__), "..", "src")
for _sub in ("config_io", "launch"):
    sys.path.insert(0, os.path.join(_SRC, _sub))

import remote_cluster  # noqa: E402


CLUSTER_CFG = {
    "host": "login.cluster.university.edu",
    "username": "myusername",
    "remote_dir": "~/debris-disk-pipeline",
    "conda_env": "debris_pipeline",
}

CONFIG = {
    "simulation": {"name": "pytest_remote"},
    "compute": {"target": "cluster", "cluster": dict(CLUSTER_CFG)},
}


def _cluster_cfg():
    return remote_cluster._cluster_cfg(CONFIG)


def test_cluster_cfg_applies_defaults():
    cfg = _cluster_cfg()
    assert cfg["environment_file"] == "environment.yml"
    assert cfg["ssh_opts"] == []
    assert cfg["rsync_excludes"] == []


def test_build_mkdir_cmd():
    cmd = remote_cluster.build_mkdir_cmd(_cluster_cfg())
    assert cmd == [
        "ssh",
        "myusername@login.cluster.university.edu",
        "mkdir -p ~/debris-disk-pipeline",
    ]


def test_build_rsync_cmd_includes_default_excludes():
    cmd = remote_cluster.build_rsync_cmd(_cluster_cfg(), repo_root="/repo")
    assert cmd[0] == "rsync"
    for pattern in remote_cluster.DEFAULT_RSYNC_EXCLUDES:
        assert "--exclude" in cmd
        assert pattern in cmd
    assert cmd[-2] == "/repo/"
    assert cmd[-1] == "myusername@login.cluster.university.edu:~/debris-disk-pipeline/"


def test_build_rsync_cmd_appends_custom_excludes():
    cfg = _cluster_cfg()
    cfg["rsync_excludes"] = ["*.h5"]
    cmd = remote_cluster.build_rsync_cmd(cfg, repo_root="/repo")
    assert "*.h5" in cmd


def test_build_bootstrap_cmd():
    cmd = remote_cluster.build_bootstrap_cmd(_cluster_cfg())
    assert cmd[:2] == ["ssh", "myusername@login.cluster.university.edu"]
    assert cmd[2:4] == ["bash", "-lc"]
    assert "bootstrap_env.sh debris_pipeline environment.yml" in cmd[4]


def test_build_launch_cmd():
    cmd = remote_cluster.build_launch_cmd(_cluster_cfg(), "sess1", "config/run.yaml")
    assert "launch_tmux.sh debris_pipeline sess1 ~/debris-disk-pipeline 'config/run.yaml'" in cmd[4]


def test_ssh_opts_extend_ssh_base():
    cfg = _cluster_cfg()
    cfg["ssh_opts"] = ["-p", "2222"]
    cmd = remote_cluster.build_mkdir_cmd(cfg)
    assert cmd[:4] == ["ssh", "-p", "2222", "myusername@login.cluster.university.edu"]


def _mock_success():
    result = MagicMock()
    result.returncode = 0
    return result


def test_remote_launch_runs_steps_in_order():
    config = copy.deepcopy(CONFIG)
    with patch("remote_cluster.subprocess.run", return_value=_mock_success()) as mock_run:
        remote_cluster.remote_launch(config, "/repo/config/run.yaml")

    assert mock_run.call_count == 4  # mkdir, rsync, bootstrap, tmux-launch
    step_cmds = [call.args[0] for call in mock_run.call_args_list]
    assert step_cmds[0][2] == "mkdir -p ~/debris-disk-pipeline"
    assert step_cmds[1][0] == "rsync"
    assert "bootstrap_env.sh" in step_cmds[2][4]
    assert "launch_tmux.sh" in step_cmds[3][4]


def test_remote_launch_aborts_on_first_failure():
    config = copy.deepcopy(CONFIG)
    failing = MagicMock()
    failing.returncode = 1

    with patch(
        "remote_cluster.subprocess.run", side_effect=[_mock_success(), failing]
    ) as mock_run:
        with pytest.raises(remote_cluster.RemoteLaunchError):
            remote_cluster.remote_launch(config, "/repo/config/run.yaml")

    assert mock_run.call_count == 2  # mkdir succeeded, rsync failed -> stop


def test_remote_launch_raises_on_oserror():
    config = copy.deepcopy(CONFIG)
    with patch("remote_cluster.subprocess.run", side_effect=OSError("no ssh binary")):
        with pytest.raises(remote_cluster.RemoteLaunchError):
            remote_cluster.remote_launch(config, "/repo/config/run.yaml")
