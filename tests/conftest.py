"""Shared fixtures."""

import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src", "launch"))

import run_log  # noqa: E402


@pytest.fixture(autouse=True)
def _isolated_run_log(tmp_path, monkeypatch):
    """Keep tests (e.g. launch_simulation.dispatch) out of the real simulation_log.csv."""
    monkeypatch.setattr(run_log, "LOG_PATH", tmp_path / "simulation_log.csv")
    monkeypatch.setenv(run_log.AUTOCOMMIT_ENV, "0")
