"""Tests for the optional `compute:` block in config_utils.validate_config."""

import copy
import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src", "config_io"))

from config_utils import validate_config  # noqa: E402


BASE_CONFIG = {
    "simulation": {"name": "pytest_compute"},
    "units": {},
    "integration": {},
    "star": {},
    "disk": {},
    "massive_planetesimals": {},
    "test_particles": {},
}

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


def _config(compute=None):
    config = copy.deepcopy(BASE_CONFIG)
    if compute is not None:
        config["compute"] = compute
    return config


def test_missing_compute_defaults_to_local():
    validate_config(_config())  # no error


def test_target_local_explicit():
    validate_config(_config({"target": "local"}))


def test_target_cluster_with_valid_remotes_block():
    validate_config(
        _config({"target": "cluster", "remotes": {"cluster": dict(CLUSTER_CFG)}})
    )


def test_two_named_remotes_either_validates():
    remotes = {"cluster": dict(CLUSTER_CFG), "work_computer": dict(WORK_COMPUTER_CFG)}
    validate_config(_config({"target": "cluster", "remotes": remotes}))
    validate_config(_config({"target": "work_computer", "remotes": remotes}))


def test_compute_not_a_mapping_raises():
    with pytest.raises(TypeError):
        validate_config(_config("cluster"))


def test_target_naming_undefined_remote_raises():
    with pytest.raises(KeyError):
        validate_config(_config({"target": "quantum"}))


def test_target_not_local_without_remotes_block_raises():
    with pytest.raises(KeyError):
        validate_config(_config({"target": "cluster"}))


@pytest.mark.parametrize("missing_key", ["host", "username", "remote_dir", "conda_env"])
def test_remote_block_missing_required_key_raises(missing_key):
    cluster = dict(CLUSTER_CFG)
    del cluster[missing_key]
    with pytest.raises(KeyError):
        validate_config(_config({"target": "cluster", "remotes": {"cluster": cluster}}))
