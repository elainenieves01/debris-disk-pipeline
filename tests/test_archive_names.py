"""Tests for src/utilities/archive_names.py and its use in build_snapshot_table.

Snapshots are lightweight stand-ins with known names/masses: real REBOUND
archives built by hand in a test are exactly what cannot be trusted here.
"""

import os
import sys
from types import SimpleNamespace

import pytest

_SRC = os.path.join(os.path.dirname(__file__), "..", "src")
for _sub in ("plotting", "utilities"):
    sys.path.insert(0, os.path.join(_SRC, _sub))

import summary_figures as sf  # noqa: E402
from archive_names import ArchiveNameChecker, ArchiveNameError, main  # noqa: E402

GOOD = ["star", "GP", "MP_0", "MP_1", "MP_2", "TP_0", "TP_1"]
MASSES = [1.0, 1e-3, 3e-8, 1e-8, 2e-8, 0.0, 0.0]


def _sim(names, masses=None, t=0.0, collision="none"):
    masses = MASSES[: len(names)] if masses is None else masses
    particles = [SimpleNamespace(name=n, m=m) for n, m in zip(names, masses)]
    return SimpleNamespace(N=len(particles), particles=particles, t=t, collision=collision)


def _check(*snapshots):
    checker = ArchiveNameChecker("test.bin")
    for index, sim in enumerate(snapshots):
        checker.check(sim, index)


def test_consistent_snapshots_pass():
    _check(_sim(GOOD), _sim(GOOD, t=1.0))


def test_removed_particles_are_allowed():
    kept = [0, 1, 2, 4, 6]  # MP_1 and TP_0 escaped
    _check(_sim(GOOD), _sim([GOOD[i] for i in kept], [MASSES[i] for i in kept], t=1.0))


@pytest.mark.parametrize("names, message", [
    (["MP_0", "star", "GP", "MP_1", "MP_2", "TP_0", "TP_1"], "not 'star'"),
    (["star", "GP", None, "MP_1", "MP_2", "TP_0", "TP_1"], "no name"),
    (["star", "GP", "MP_0", "MP_0", "MP_2", "TP_0", "TP_1"], "duplicate"),
    (["star", "GP", "MP_0", "MP_1", "junk", "TP_0", "TP_1"], "unexpected name"),
    (["star", "GP", "MP_0", "MP_2", "MP_1", "TP_0", "TP_1"], "numbered"),
])
def test_bad_first_snapshot_is_rejected(names, message):
    with pytest.raises(ArchiveNameError, match=message):
        _check(_sim(names))


def test_reordered_names_are_rejected():
    swapped = ["star", "GP", "MP_1", "MP_0", "MP_2", "TP_0", "TP_1"]
    with pytest.raises(ArchiveNameError, match="same order"):
        _check(_sim(GOOD), _sim(swapped, t=1.0))


def test_name_moved_to_another_body_is_rejected():
    # Same names in the same order, but MP_0 now sits on a body of another mass.
    masses = list(MASSES)
    masses[2], masses[3] = masses[3], masses[2]
    with pytest.raises(ArchiveNameError, match="changed mass"):
        _check(_sim(GOOD), _sim(GOOD, masses, t=1.0))


def test_mass_check_skipped_when_collisions_merge_bodies():
    masses = list(MASSES)
    masses[2] += masses[3]
    _check(_sim(GOOD, collision="direct"), _sim(GOOD, masses, t=1.0, collision="direct"))


def test_error_names_archive_and_snapshot():
    with pytest.raises(ArchiveNameError, match=r"test\.bin: snapshot 1 \(t = 5"):
        _check(_sim(GOOD), _sim(GOOD[:2] + [None] + GOOD[3:], t=5.0))


def test_build_snapshot_table_refuses_bad_names(monkeypatch):
    # Checked before any row is built, so the bad first snapshot never reaches
    # the orbit/position code.
    bad = [_sim(GOOD[:2] + ["MP_0"] + GOOD[2:-1])]
    monkeypatch.setattr(sf.rebound, "Simulationarchive", lambda path: bad)
    with pytest.raises(ArchiveNameError, match="duplicate"):
        sf.build_snapshot_table("fake.bin")


def test_cli_reports_and_sets_exit_status(monkeypatch, capsys):
    import archive_names

    archives = {"good.bin": [_sim(GOOD)], "bad.bin": [_sim(GOOD), _sim(GOOD[::-1])]}

    def fake_check(path):
        checker = ArchiveNameChecker(path)
        for index, sim in enumerate(archives[path]):
            checker.check(sim, index)
        return len(archives[path])

    monkeypatch.setattr(archive_names, "check_archive_names", fake_check)
    assert main(["good.bin"]) == 0
    assert main(["good.bin", "bad.bin"]) == 1
    out = capsys.readouterr().out
    assert "OK   good.bin" in out and "FAIL bad.bin" in out
