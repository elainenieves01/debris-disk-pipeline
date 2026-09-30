"""The simulation log (src/launch/run_log.py) and its launcher hook."""

import copy
import os
import sys
from unittest.mock import patch

import yaml

_SRC = os.path.join(os.path.dirname(__file__), "..", "src")
for _sub in ("config_io", "launch"):
    sys.path.insert(0, os.path.join(_SRC, _sub))

import launch_simulation  # noqa: E402
import run_log  # noqa: E402

REPO = os.path.join(os.path.dirname(__file__), "..")

UNIFORM_CONFIG = {
    "simulation": {"name": "pytest_log_uniform", "random_seed": 0,
                   "output_dir": "outputs", "dump": False},
    "units": {"time": "yr", "length": "AU", "mass": "Msun"},
    "integration": {"integrator": "mercurius", "timestep_fraction_of_planet_period": 0.1,
                    "maxtime": 1000, "time_step": 100, "exit_max_distance": 1000.0},
    "star": {"mass": 1.0},
    "giant_planet": None,
    "disk": {"amin": 95, "amax": 105, "emin": 0.0, "emax": 3.2e-5,
             "imin_deg": 0.0, "imax_deg": 3.2e-5},
    "massive_planetesimals": {"N": 20, "total_disk_mass_earth": 0.28},
    "test_particles": {"N": 0},
    "compute": {"target": "local"},
}


def _csv_config():
    config = copy.deepcopy(UNIFORM_CONFIG)
    config["simulation"]["name"] = "pytest_log_csv"
    config["massive_planetesimals"] = {
        "N": 800,
        "distribution": {
            "type": "power_law", "mode": "csv", "variable": "radius", "unit": "km",
            "path": "src/mass_models/cascade_selection_200km_800keep/slope_q3/selected.csv",
            "slope": 3.0,
        },
    }
    return config


def test_uniform_config_summary():
    row, notes = run_log.summarize_config(UNIFORM_CONFIG)

    assert notes == []
    assert row["mass_model"] == "uniform"
    assert float(row["disk_mass_earth"]) == pytest_approx(0.28)
    assert row["mp_mass_min_earth"] == row["mp_mass_max_earth"]
    # 0.1 x circular period at 95 AU around 1 Msun
    assert float(row["dt_yr"]) == pytest_approx(0.1 * 95 ** 1.5, rel=1e-3)
    assert (row["amin_AU"], row["amax_AU"], row["maxtime_yr"]) == ("95", "105", "1000")


def test_csv_distribution_summary_sums_the_file():
    import pandas as pd

    row, notes = run_log.summarize_config(_csv_config())
    selected = pd.read_csv(os.path.join(
        REPO, "src/mass_models/cascade_selection_200km_800keep/slope_q3/selected.csv"))

    assert notes == []
    assert row["mass_model"] == "power law in radius (csv)"
    assert row["mass_slope"] == "3"
    assert float(row["disk_mass_earth"]) == pytest_approx(selected["mass_earth"].sum(), rel=1e-5)


def test_broken_config_still_logs_with_a_note():
    config = copy.deepcopy(UNIFORM_CONFIG)
    del config["star"]
    row, notes = run_log.summarize_config(config)

    assert row["run_name"] == "pytest_log_uniform"
    assert notes and "could not build initial conditions" in notes[0]


def test_dispatch_logs_a_successful_launch():
    with patch("launch_simulation.launch_local"):
        launch_simulation.dispatch(UNIFORM_CONFIG, "config/pytest_log.yaml")

    rows = run_log.read_log()
    assert len(rows) == 1
    assert rows[0]["run_name"] == "pytest_log_uniform"
    assert rows[0]["target"] == "local"
    assert rows[0]["status"] == "launched"


def test_refresh_fills_outcome_for_the_matching_launch(tmp_path):
    run_log.append_row(run_log.make_row(UNIFORM_CONFIG, "", target="local",
                                        sent_at="2026-09-01T10:00:00-03:00"))
    run_log.append_row(run_log.make_row(UNIFORM_CONFIG, "", target="local",
                                        sent_at="2026-09-10T10:00:00-03:00"))
    run_dir = tmp_path / "outputs" / "pytest_log_uniform"
    run_dir.mkdir(parents=True)
    (run_dir / "run_metadata.yaml").write_text(yaml.safe_dump({
        "run_uuid": "abc", "created": "2026-09-10T10:00:05-03:00",
        "finished": "2026-09-10T12:00:05-03:00", "wall_runtime_seconds": 7200,
        "outcome": "completed", "final_particle_count": 21,
    }))

    assert run_log.refresh(tmp_path / "outputs") == 1
    first, second = run_log.read_log()
    assert first["status"] == "launched"
    assert (second["status"], second["runtime_hr"], second["run_uuid"]) == ("completed", "2", "abc")


def test_backfill_skips_runs_already_logged(tmp_path):
    run_dir = tmp_path / "outputs" / "pytest_log_uniform"
    run_dir.mkdir(parents=True)
    (run_dir / "config.yaml").write_text(yaml.safe_dump(UNIFORM_CONFIG))
    (run_dir / "run_metadata.yaml").write_text(yaml.safe_dump({
        "run_uuid": "xyz", "created": "2026-09-02T09:00:00-03:00",
        "host": {"hostname": "somewhere"}, "outcome": "completed",
    }))

    assert run_log.backfill(tmp_path / "outputs") == ["pytest_log_uniform"]
    assert run_log.backfill(tmp_path / "outputs") == []
    (row,) = run_log.read_log()
    assert (row["target"], row["status"]) == ("somewhere", "completed")


def pytest_approx(value, rel=1e-6):
    import pytest
    return pytest.approx(value, rel=rel)


def test_summarizing_writes_nothing_to_the_run_output_dir(tmp_path):
    config = _csv_config()
    config["simulation"]["output_dir"] = str(tmp_path)
    run_log.summarize_config(config)

    assert list(tmp_path.iterdir()) == []


def test_legacy_config_summary():
    legacy = {
        "simulation": {"name": "legacy_run"},
        "integration": {"integrator": "whfast", "timestep_fraction_of_planet_period": 0.1,
                        "maxtime": 1.0e6, "Noutputs": 50, "exit_max_distance": 1000.0},
        "star": {"mass": 1.28},
        "giant_planet": {"mass_jupiter": 1.26, "a": 2.56},
        "disk": {"amin": 30.0, "amax": 50.0},
        "dwarf_planets": {"N": 500, "total_mass_earth": 1.0},
        "test_particles": {"N": 1000},
    }
    row, notes = run_log.summarize_legacy_config(legacy)

    assert (row["n_massive"], row["n_test"], row["output_every_yr"]) == (500, 1000, "20000")
    assert (row["mass_model"], row["disk_mass_earth"]) == ("uniform", "1")
    period = (2.56 ** 3 / (1.28 + 1.26 * 9.5479e-4)) ** 0.5
    assert float(row["dt_yr"]) == pytest_approx(0.1 * period, rel=1e-5)
    assert notes == []


# ---- keeping the log current -------------------------------------------------

def _write_metadata(run_dir, **fields):
    run_dir.mkdir(parents=True, exist_ok=True)
    (run_dir / "run_metadata.yaml").write_text(yaml.safe_dump(fields))


def test_run_updates_its_own_row_on_start_and_finish(tmp_path):
    run_log.append_row(run_log.make_row(UNIFORM_CONFIG, "", target="local",
                                        sent_at="2026-09-10T10:00:00-03:00"))
    run_dir = tmp_path / "outputs" / "pytest_log_uniform"

    _write_metadata(run_dir, run_uuid="u1", created="2026-09-10T10:00:01-03:00")
    run_log.note_run_event(UNIFORM_CONFIG, "", run_dir)
    (row,) = run_log.read_log()
    assert (row["status"], row["run_uuid"]) == ("running", "u1")

    _write_metadata(run_dir, run_uuid="u1", created="2026-09-10T10:00:01-03:00",
                    outcome="completed", finished="2026-09-10T11:00:01-03:00",
                    wall_runtime_seconds=3600, final_particle_count=21)
    run_log.note_run_event(UNIFORM_CONFIG, "", run_dir)
    (row,) = run_log.read_log()
    assert (row["status"], row["runtime_hr"]) == ("completed", "1")


def test_run_started_without_the_launcher_gets_a_row(tmp_path):
    run_log.write_log([])
    run_dir = tmp_path / "outputs" / "pytest_log_uniform"
    _write_metadata(run_dir, run_uuid="u2", created="2026-09-11T09:00:00-03:00")

    run_log.note_run_event(UNIFORM_CONFIG, "config/x.yaml", run_dir)

    (row,) = run_log.read_log()
    assert row["status"] == "running"
    assert "started without launch_simulation.py" in row["notes"]


def test_run_event_is_a_no_op_without_a_log(tmp_path):
    run_dir = tmp_path / "outputs" / "pytest_log_uniform"
    _write_metadata(run_dir, run_uuid="u3", created="2026-09-11T09:00:00-03:00")

    run_log.note_run_event(UNIFORM_CONFIG, "", run_dir)  # e.g. on a remote copy

    assert not run_log.LOG_PATH.exists()


def test_launch_row_matches_a_run_that_started_slightly_before_sent_at():
    row = run_log.make_row(UNIFORM_CONFIG, "", target="barbieri",
                           sent_at="2026-09-10T10:00:30+00:00")
    metadata = {"created": "2026-09-10T10:00:05+00:00"}  # remote clock a bit behind
    assert run_log.row_for_metadata([row], "pytest_log_uniform", metadata) is row


def _sync_with_probe(monkeypatch, probe_text, statuses):
    names = [f"pytest_sync_{i}" for i in range(len(statuses))]
    rows = []
    for name, status in zip(names, statuses):
        config = copy.deepcopy(UNIFORM_CONFIG)
        config["simulation"]["name"] = name
        row = run_log.make_row(config, "", target="barbieri",
                               sent_at="2026-09-20T10:00:00+00:00")
        row["status"] = status
        rows.append(row)
    run_log.write_log(rows)
    monkeypatch.setattr(run_log, "known_remotes", lambda: {"barbieri": {
        "host": "h", "username": "u", "remote_dir": "/r", "ssh_opts": []}})

    class Result:
        returncode, stdout, stderr = 0, probe_text, ""
    calls = []
    monkeypatch.setattr(run_log.subprocess, "run",
                        lambda cmd, **kw: calls.append((cmd, kw)) or Result())
    changes = run_log.sync_remote()
    return {r["run_name"]: r for r in run_log.read_log()}, changes, calls


def test_sync_classifies_remote_runs(monkeypatch):
    now = 1_790_000_000
    started = "created: '2026-09-20T10:00:10+00:00'\nrun_uuid: x"
    probe = "\n".join([
        "=== pytest_sync_0", started, "--- tmux", "alive", "--- archive", str(now - 600),
        "=== pytest_sync_1", started, "--- tmux", "alive", "--- archive", str(now - 12 * 3600),
        "=== pytest_sync_2", started, "outcome: completed", "wall_runtime_seconds: 7200",
        "--- tmux", "gone", "--- archive", str(now - 60),
        "=== pytest_sync_3", started, "--- tmux", "gone", "--- archive", str(now - 60),
        "=== pytest_sync_4", "--- tmux", "alive", "--- archive", "none",
        "=== __now__", str(now),
    ])
    rows, changes, calls = _sync_with_probe(
        monkeypatch, probe, ["running", "running", "running", "running", "launched"])

    assert [rows[f"pytest_sync_{i}"]["status"] for i in range(5)] == [
        "running", "possibly stalled", "completed", "stopped (no outcome)", "starting"]
    assert rows["pytest_sync_2"]["runtime_hr"] == "2"
    assert "archive last written 12.0 h ago" in rows["pytest_sync_1"]["last_checked"]
    cmd, kw = calls[0]
    assert "BatchMode=yes" in cmd and "tmux has-session -t =pytest_sync_0" in kw["input"]
    assert len(changes) == 5


def test_sync_leaves_finished_runs_alone(monkeypatch):
    rows, changes, calls = _sync_with_probe(monkeypatch, "", ["completed"])
    assert changes == [] and calls == []


def test_sync_explains_how_to_connect_when_ssh_needs_a_password(monkeypatch):
    import pytest

    run_log.write_log([dict(run_log.make_row(UNIFORM_CONFIG, "", target="barbieri"),
                            status="running")])
    monkeypatch.setattr(run_log, "known_remotes", lambda: {"barbieri": {
        "host": "h", "username": "u", "remote_dir": "/r", "ssh_opts": []}})

    class Result:
        returncode, stdout, stderr = 255, "", "Permission denied"
    monkeypatch.setattr(run_log.subprocess, "run", lambda cmd, **kw: Result())

    with pytest.raises(SystemExit, match="ssh -fN u@h"):
        run_log.sync_remote()


def test_autocommit_only_touches_the_repo_log(monkeypatch):
    monkeypatch.setenv(run_log.AUTOCOMMIT_ENV, "1")
    run_log.write_log([])
    # LOG_PATH points at a temp file here, so nothing may be committed
    assert run_log.commit_and_push("test") is False


def test_dispatch_stamps_sent_at_before_launching():
    stamps = []
    with patch("launch_simulation.launch_local",
               side_effect=lambda *a: stamps.append(run_log.now_iso())), \
         patch("run_log.record_launch") as record:
        launch_simulation.dispatch(UNIFORM_CONFIG, "config/pytest_log.yaml")

    sent_at = record.call_args.kwargs["sent_at"]
    assert run_log._ts(sent_at) <= run_log._ts(stamps[0])
