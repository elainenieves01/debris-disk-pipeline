"""Tests for src/launch/launch_simulation.py and tmux_utils.py."""

import copy
import os
import sys
from unittest.mock import patch, MagicMock

import pytest

_SRC = os.path.join(os.path.dirname(__file__), "..", "src")
for _sub in ("config_io", "launch"):
    sys.path.insert(0, os.path.join(_SRC, _sub))

import launch_simulation  # noqa: E402
import remote_cluster  # noqa: E402
from tmux_utils import sanitize_session_name, session_name_for  # noqa: E402


def test_sanitize_session_name_replaces_bad_chars():
    assert sanitize_session_name("SS 800MP: 100Myr!") == "SS_800MP__100Myr_"


def test_sanitize_session_name_leaves_safe_chars():
    assert sanitize_session_name("run-1.0_ok") == "run-1.0_ok"


def test_session_name_for_defaults_to_simulation_name():
    config = {"simulation": {"name": "SS 100"}}
    assert session_name_for(config) == "SS_100"


def test_session_name_for_uses_override():
    config = {"simulation": {"name": "ignored"}, "compute": {"tmux_session": "custom!"}}
    assert session_name_for(config) == "custom_"


LOCAL_CONFIG = {
    "simulation": {"name": "pytest_local"},
    "compute": {"target": "local"},
}

CLUSTER_CONFIG = {
    "simulation": {"name": "pytest_cluster"},
    "compute": {
        "target": "cluster",
        "cluster": {
            "host": "h",
            "username": "u",
            "remote_dir": "~/r",
            "conda_env": "e",
        },
    },
}


def test_dispatch_local_calls_launch_local():
    with patch("launch_simulation.launch_local") as mock_local:
        launch_simulation.dispatch(LOCAL_CONFIG, "config/pytest_local.yaml")
    mock_local.assert_called_once_with(LOCAL_CONFIG, "config/pytest_local.yaml")


def test_dispatch_no_compute_block_defaults_local():
    config = {"simulation": {"name": "no_compute"}}
    with patch("launch_simulation.launch_local") as mock_local:
        launch_simulation.dispatch(config, "config/no_compute.yaml")
    mock_local.assert_called_once()


def test_dispatch_cluster_calls_remote_launch():
    with patch("remote_cluster.remote_launch") as mock_remote:
        launch_simulation.dispatch(CLUSTER_CONFIG, "config/pytest_cluster.yaml")
    mock_remote.assert_called_once_with(CLUSTER_CONFIG, "config/pytest_cluster.yaml")


def test_dispatch_cluster_launch_error_exits_nonzero(capsys):
    with patch(
        "remote_cluster.remote_launch",
        side_effect=remote_cluster.RemoteLaunchError("rsync failed"),
    ):
        with pytest.raises(SystemExit) as exc_info:
            launch_simulation.dispatch(CLUSTER_CONFIG, "config/pytest_cluster.yaml")
    assert exc_info.value.code == 1
    assert "LAUNCH FAILED" in capsys.readouterr().err


def test_dispatch_unknown_target_raises():
    config = {"simulation": {"name": "x"}, "compute": {"target": "quantum"}}
    with pytest.raises(ValueError):
        launch_simulation.dispatch(config, "config/x.yaml")


def _mock_success():
    result = MagicMock()
    result.returncode = 0
    return result


def test_launch_local_starts_new_tmux_session_when_none_running():
    with patch(
        "launch_simulation._tmux_has_session", return_value=False
    ), patch(
        "launch_simulation.subprocess.run", return_value=_mock_success()
    ) as mock_run:
        launch_simulation.launch_local(LOCAL_CONFIG, "config/pytest_local.yaml")

    cmd = mock_run.call_args.args[0]
    assert cmd[:5] == ["tmux", "new-session", "-d", "-s", "pytest_local"]


def test_launch_local_refuses_duplicate_session():
    with patch("launch_simulation._tmux_has_session", return_value=True):
        with pytest.raises(SystemExit) as exc_info:
            launch_simulation.launch_local(LOCAL_CONFIG, "config/pytest_local.yaml")
    assert exc_info.value.code == 1
