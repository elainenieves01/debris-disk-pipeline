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


def _config(compute=None):
    config = copy.deepcopy(BASE_CONFIG)
    if compute is not None:
        config["compute"] = compute
    return config


def test_missing_compute_defaults_to_local():
    validate_config(_config())  # no error


def test_target_local_explicit():
    validate_config(_config({"target": "local"}))


def test_target_cluster_with_valid_block():
    validate_config(_config({"target": "cluster", "cluster": dict(CLUSTER_CFG)}))


def test_compute_not_a_mapping_raises():
    with pytest.raises(TypeError):
        validate_config(_config("cluster"))


def test_unknown_target_raises():
    with pytest.raises(ValueError):
        validate_config(_config({"target": "quantum"}))


def test_cluster_target_without_cluster_block_raises():
    with pytest.raises(KeyError):
        validate_config(_config({"target": "cluster"}))


@pytest.mark.parametrize("missing_key", ["host", "username", "remote_dir", "conda_env"])
def test_cluster_block_missing_required_key_raises(missing_key):
    cluster = dict(CLUSTER_CFG)
    del cluster[missing_key]
    with pytest.raises(KeyError):
        validate_config(_config({"target": "cluster", "cluster": cluster}))
