"""Tests for compute_effective_stirring_C_e in src/simulation/run_simulation.py."""

import os
import sys

import numpy as np
import pytest
import rebound

_SRC = os.path.join(os.path.dirname(__file__), "..", "src")
for _sub in ("simulation", "config_io", "plotting", "diagnostics", "utilities",
             "mass_models"):
    sys.path.insert(0, os.path.join(_SRC, _sub))

from run_simulation import compute_effective_stirring_C_e  # noqa: E402

CONFIG = {
    "massive_planetesimals": {"N": 400},
    "star": {"mass": 1.0},
    "disk": {"amin": 95.0, "amax": 105.0, "emin": 0.0, "emax": 3.2e-5},
}


def _sim(eccentricities, masses):
    sim = rebound.Simulation()
    sim.units = ("yr", "AU", "Msun")
    sim.add(m=1.0, name="star")
    rng = np.random.default_rng(1)
    for k, (e, m) in enumerate(zip(eccentricities, masses)):
        sim.add(m=m, a=rng.uniform(95.0, 105.0), e=e, f=rng.uniform(0, 2 * np.pi),
                name=f"MP_{k}")
    sim.t = 1.0e5
    return sim


def _rayleigh_e(n, sigma=0.01):
    return np.random.default_rng(0).rayleigh(sigma, n)


def test_clean_rayleigh_sample_keeps_every_body():
    e = _rayleigh_e(400)
    r = compute_effective_stirring_C_e(_sim(e, np.full(400, 1e-8)), CONFIG)
    assert r["cut_applied"]
    assert r["excluded"] == []
    assert r["n_used"] == 400
    assert r["C_e"] == pytest.approx(r["C_e_all"])


def test_scattered_body_is_excluded_from_rms_but_not_masses():
    e = _rayleigh_e(400)
    e[7] = 0.4  # one body flung out by a strong encounter
    masses = np.full(400, 1e-8)
    masses[3] = 5e-8
    r = compute_effective_stirring_C_e(_sim(e, masses), CONFIG)

    assert r["cut_applied"]
    assert [name for name, _ in r["excluded"]] == ["MP_7"]
    assert r["n_used"] == 399
    assert r["rms_e"] < r["rms_e_all"]
    assert r["C_e"] < r["C_e_all"]
    # M and Mdisc still come from every massive planetesimal.
    assert r["m_max"] == pytest.approx(5e-8)
    assert r["m_disc"] == pytest.approx(masses.sum())
    # C_e scales as RMS(e)^4 at fixed masses / geometry / t.
    assert r["C_e"] / r["C_e_all"] == pytest.approx((r["rms_e"] / r["rms_e_all"]) ** 4)


def test_cut_not_applied_when_disk_is_not_stirred():
    # Unstirred disk: e still near its initial uniform [0, emax] draw plus a
    # few larger values. The median-based cut would trim the larger ones, but
    # median(e) < 30 * emax, so the cut must be skipped and every body used.
    e = np.concatenate([np.linspace(1e-5, 2e-5, 390), np.full(10, 1e-3)])
    r = compute_effective_stirring_C_e(_sim(e, np.full(400, 1e-8)), CONFIG)
    assert not r["cut_applied"]
    assert r["excluded"] == []
    assert r["C_e"] == pytest.approx(r["C_e_all"])


def test_config_nsigma_sets_the_cut_factor():
    e = _rayleigh_e(400)
    e[7] = 0.4
    e[8] = 0.042  # ~5 sigma: kept at the default factor, cut at 3
    default = compute_effective_stirring_C_e(_sim(e, np.full(400, 1e-8)), CONFIG)
    tighter = compute_effective_stirring_C_e(
        _sim(e, np.full(400, 1e-8)), {**CONFIG, "rayleigh_cut": {"nsigma": 3}})
    assert default["cut_nsigma"] == 5 and tighter["cut_nsigma"] == 3
    assert "MP_8" not in [n for n, _ in default["excluded"]]
    assert "MP_8" in [n for n, _ in tighter["excluded"]]
    assert tighter["C_e"] < default["C_e"]


def test_ks_warning_does_not_switch_the_cut_off():
    # Stirred but clearly non-Rayleigh bulk (uniform e): the KS test warns,
    # yet the scattered body is still excluded.
    e = np.linspace(0.002, 0.02, 400)
    e[7] = 0.4
    r = compute_effective_stirring_C_e(_sim(e, np.full(400, 1e-8)), CONFIG)
    assert r["ks_warning"]
    assert r["cut_applied"]
    assert [name for name, _ in r["excluded"]] == ["MP_7"]
