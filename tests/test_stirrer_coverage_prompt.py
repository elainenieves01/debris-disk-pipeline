"""Tests for check_stirrer_disk_coverage's continue/abort prompt in
src/simulation/run_simulation.py."""

import os
import sys

import pytest
import rebound

_SRC = os.path.join(os.path.dirname(__file__), "..", "src")
for _sub in ("simulation", "config_io", "plotting", "diagnostics", "utilities",
             "mass_models"):
    sys.path.insert(0, os.path.join(_SRC, _sub))

import run_simulation  # noqa: E402
from run_simulation import UNATTENDED_ENV, check_stirrer_disk_coverage  # noqa: E402

CONFIG = {
    "massive_planetesimals": {"N": 2},
    "star": {"mass": 1.0},
    "disk": {"amin": 95.0, "amax": 105.0, "emin": 0.0, "emax": 3.2e-5},
}


def _uncovered_sim():
    """Two tiny stirrers: their feeding zones fall far short of the belt."""
    sim = rebound.Simulation()
    sim.units = ("yr", "AU", "Msun")
    sim.add(m=1.0, name="star")
    sim.add(m=1e-12, a=98.0, name="MP_0")
    sim.add(m=1e-12, a=102.0, name="MP_1")
    return sim


class _TTY:
    def isatty(self):
        return True


@pytest.fixture
def tty_stdin(monkeypatch):
    monkeypatch.setattr(run_simulation.sys, "stdin", _TTY())


def test_unattended_launch_continues_without_prompting(tty_stdin, monkeypatch, capsys):
    monkeypatch.setenv(UNATTENDED_ENV, "1")

    def no_prompt(_):
        raise AssertionError("an unattended run must never prompt")

    monkeypatch.setattr("builtins.input", no_prompt)
    check_stirrer_disk_coverage(_uncovered_sim(), CONFIG)
    out = capsys.readouterr().out
    assert "WARNING: stirrer feeding zones do NOT span the belt" in out
    assert "Unattended launch" in out


def test_interactive_run_still_prompts_and_aborts_on_no(tty_stdin, monkeypatch):
    monkeypatch.delenv(UNATTENDED_ENV, raising=False)
    monkeypatch.setattr("builtins.input", lambda _: "n")
    with pytest.raises(SystemExit, match="Aborted before integration"):
        check_stirrer_disk_coverage(_uncovered_sim(), CONFIG)


def test_interactive_run_continues_on_yes(tty_stdin, monkeypatch, capsys):
    monkeypatch.delenv(UNATTENDED_ENV, raising=False)
    monkeypatch.setattr("builtins.input", lambda _: "y")
    check_stirrer_disk_coverage(_uncovered_sim(), CONFIG)
    assert "Continuing at user request." in capsys.readouterr().out


def test_remote_tmux_script_marks_runs_unattended():
    script = os.path.join(os.path.dirname(__file__), "..", "scripts", "remote",
                          "launch_tmux.sh")
    with open(script, encoding="utf-8") as f:
        assert f"{UNATTENDED_ENV}=1 python -u src/simulation/run_simulation.py" in f.read()
