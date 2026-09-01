"""The massive_planetesimals `distribution` mass mode in build_simulation."""

import copy
import os
import sys

import numpy as np
import pytest

_SRC = os.path.join(os.path.dirname(__file__), "..", "src")
for _sub in ("config_io", "plotting", "diagnostics", "utilities", "mass_models", "simulation"):
    sys.path.insert(0, os.path.join(_SRC, _sub))

from run_simulation import build_simulation, EARTH_MASS_TO_SOLAR_MASS  # noqa: E402
from mass_models import masses_to_radii, M_SUN_KG  # noqa: E402


BASE_CONFIG = {
    "simulation": {"name": "pytest_dohnanyi", "random_seed": 0,
                   "output_dir": "outputs", "dump": False},
    "units": {"time": "yr", "length": "AU", "mass": "Msun"},
    "integration": {"integrator": "mercurius",
                    "timestep_fraction_of_planet_period": 0.1,
                    "maxtime": 100.0, "time_step": 50, "exit_max_distance": 100.0},
    "star": {"mass": 1.0},
    "giant_planet": None,
    "disk": {"amin": 95, "amax": 105, "emin": 0.0, "emax": 3.2e-5,
             "imin_deg": 0.0, "imax_deg": 3.2e-5},
    "massive_planetesimals": {
        "N": 60,
        "total_disk_mass_earth": 0.5,
        "distribution": {"type": "power_law", "mode": "total_mass",
                         "variable": "radius", "min": 1, "max": 100,
                         "unit": "km", "slope": 3.5, "seed": 42},
    },
    "test_particles": {"N": 0, "distribution": "uniform"},
    "plots": {"enabled": False, "dpi": 200},
}


def _config(**overrides):
    cfg = copy.deepcopy(BASE_CONFIG)
    cfg["massive_planetesimals"].update(overrides)
    return cfg


def _mp_masses(sim):
    return np.array(
        [p.m for p in sim.particles if (p.name or "").startswith("MP_")]
    )


def _is_uniform(masses):
    # relative check: MP masses can be ~1e-17 Msun, so allclose's default
    # atol=1e-8 would call any spectrum uniform
    return bool(np.allclose(masses, masses[0], rtol=1e-9, atol=0.0))


def test_distribution_mode_sets_nonuniform_masses_summing_to_total():
    sim = build_simulation(_config())
    masses = _mp_masses(sim)

    assert masses.size == 60
    assert not _is_uniform(masses)                          # a real spectrum
    total_earth = masses.sum() / EARTH_MASS_TO_SOLAR_MASS
    assert total_earth == pytest.approx(0.5, rel=1e-6)     # rescaled to the total


def test_distribution_seed_is_reproducible():
    a = _mp_masses(build_simulation(_config()))
    b = _mp_masses(build_simulation(_config()))
    assert np.array_equal(a, b)

    c = _mp_masses(build_simulation(_config(
        distribution={"type": "power_law", "variable": "radius", "min": 1,
                      "max": 100, "unit": "km", "slope": 3.5, "seed": 7})))
    assert not np.array_equal(a, c)


def test_even_split_unchanged_without_distribution_block():
    sim = build_simulation(_config(distribution=None))
    masses = _mp_masses(sim)
    assert _is_uniform(masses)
    assert masses.sum() / EARTH_MASS_TO_SOLAR_MASS == pytest.approx(0.5, rel=1e-9)


def test_distribution_requires_total_disk_mass_earth():
    cfg = _config()
    del cfg["massive_planetesimals"]["total_disk_mass_earth"]
    cfg["massive_planetesimals"]["individual_MP_mass_plutos"] = 1e-4
    with pytest.raises(ValueError):
        build_simulation(cfg)


def test_distribution_rejects_mismatched_unit():
    with pytest.raises(ValueError):
        build_simulation(_config(
            distribution={"type": "power_law", "variable": "mass", "min": 1e-6,
                          "max": 1e-2, "unit": "km", "slope": 1.8333}))


def _size_range_config():
    cfg = copy.deepcopy(BASE_CONFIG)
    cfg["massive_planetesimals"] = {
        "N": 60,
        "distribution": {"type": "power_law", "mode": "size_range",
                         "variable": "radius", "min": 1, "max": 100,
                         "unit": "km", "slope": 3.5, "seed": 42},
    }
    return cfg


def test_size_range_mode_uses_literal_km_and_computes_disk_mass():
    sim = build_simulation(_size_range_config())
    masses_msun = _mp_masses(sim)
    assert masses_msun.size == 60
    assert not _is_uniform(masses_msun)

    radii_km = masses_to_radii(masses_msun * M_SUN_KG, density_g_cm3=1.0)
    assert radii_km.min() >= 1.0 - 1e-6
    assert radii_km.max() <= 100.0 + 1e-6

    # disk mass is whatever the bodies sum to (not anchored), and small
    total_earth = masses_msun.sum() / EARTH_MASS_TO_SOLAR_MASS
    assert 0 < total_earth < 1e-3


def test_size_range_mode_rejects_a_mass_key():
    cfg = _size_range_config()
    cfg["massive_planetesimals"]["total_disk_mass_earth"] = 0.5
    with pytest.raises(ValueError):
        build_simulation(cfg)


def test_distribution_rejects_unknown_mode():
    with pytest.raises(ValueError):
        build_simulation(_config(
            distribution={"type": "power_law", "mode": "bogus", "variable": "radius",
                          "min": 1, "max": 100, "unit": "km", "slope": 3.5}))
