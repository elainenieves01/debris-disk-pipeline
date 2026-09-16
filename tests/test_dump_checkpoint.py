"""get_particles() writes the resume checkpoint (dump_data.json) atomically:
a crash mid-write must never leave a truncated/corrupt file behind."""

import json
import os
import sys

import pytest
import rebound

_SRC = os.path.join(os.path.dirname(__file__), "..", "src")
for _sub in ("config_io", "plotting", "diagnostics", "utilities", "mass_models", "simulation"):
    sys.path.insert(0, os.path.join(_SRC, _sub))

from run_simulation import get_particles  # noqa: E402


def _sim():
    sim = rebound.Simulation()
    sim.add(m=1.0, x=0, y=0, z=0, vx=0, vy=0, vz=0, name="star")
    sim.add(m=1e-6, x=1.0, y=0, z=0, vx=0, vy=1.0, vz=0, name="MP_0")
    sim.t = 12.5
    return sim


def test_get_particles_writes_valid_json(tmp_path):
    dump_path = tmp_path / "dump_data.json"
    get_particles(0, _sim(), dump_path)

    with open(dump_path) as f:
        data = json.load(f)
    assert set(data) == {"star", "MP_0"}
    assert data["star"]["time"] == 12.5


def test_get_particles_leaves_no_tmp_file_behind(tmp_path):
    dump_path = tmp_path / "dump_data.json"
    get_particles(0, _sim(), dump_path)
    assert list(tmp_path.iterdir()) == [dump_path]


def test_get_particles_failed_write_does_not_corrupt_existing_checkpoint(
    tmp_path, monkeypatch
):
    dump_path = tmp_path / "dump_data.json"
    get_particles(0, _sim(), dump_path)
    with open(dump_path) as f:
        good_snapshot = json.load(f)

    def _boom(*args, **kwargs):
        raise OSError("simulated crash mid-write")

    monkeypatch.setattr("run_simulation.json.dump", _boom)
    with pytest.raises(OSError):
        get_particles(1, _sim(), dump_path)

    # The original checkpoint must be untouched -- still valid JSON, still
    # the last successful snapshot -- not a half-written file.
    with open(dump_path) as f:
        assert json.load(f) == good_snapshot
