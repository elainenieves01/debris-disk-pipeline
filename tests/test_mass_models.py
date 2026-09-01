"""Tests for src/mass_models/mass_models.py."""

import os
import sys

import numpy as np
import pytest

sys.path.insert(
    0, os.path.join(os.path.dirname(__file__), "..", "src", "mass_models")
)

from mass_models import (  # noqa: E402
    M_EARTH_KG,
    DOHNANYI_MASS_SLOPE,
    radii_to_masses,
    masses_to_radii,
    sample_powerlaw,
    generate_distribution,
)


def test_radius_mass_roundtrip():
    radii = np.array([1.0, 10.0, 123.4, 800.0])
    back = masses_to_radii(radii_to_masses(radii, density_g_cm3=1.5), density_g_cm3=1.5)
    assert np.allclose(back, radii, rtol=1e-12)


def test_sample_powerlaw_bounds():
    x = sample_powerlaw(50_000, 1.0, 1000.0, slope=1.8333, seed=1)
    assert x.min() >= 1.0
    assert x.max() <= 1000.0
    assert x.shape == (50_000,)


def test_sample_powerlaw_slope_recovery():
    # MLE for a truncated power law is dominated by the lower cutoff; with a
    # wide dynamic range the simple Hill estimator recovers the input slope.
    xmin, xmax, q = 1.0, 1.0e5, 1.9
    x = sample_powerlaw(400_000, xmin, xmax, slope=q, seed=7)
    q_hat = 1.0 + x.size / np.sum(np.log(x / xmin))
    assert q_hat == pytest.approx(q, abs=0.05)


def test_sample_powerlaw_slope_one():
    x = sample_powerlaw(10_000, 2.0, 20.0, slope=1.0, seed=3)
    assert x.min() >= 2.0
    assert x.max() <= 20.0


def test_sample_powerlaw_validation():
    with pytest.raises(ValueError):
        sample_powerlaw(0, 1.0, 2.0, slope=2.0)
    with pytest.raises(ValueError):
        sample_powerlaw(10, -1.0, 2.0, slope=2.0)
    with pytest.raises(ValueError):
        sample_powerlaw(10, 5.0, 2.0, slope=2.0)


def test_generate_distribution_columns_and_attrs():
    df = generate_distribution(100, seed=0)
    assert list(df.columns) == [
        "particle_id", "radius_km", "mass_kg", "mass_earth", "mass_solar",
    ]
    assert len(df) == 100
    assert df.attrs["slope"] == pytest.approx(DOHNANYI_MASS_SLOPE)
    assert df.attrs["n_particles"] == 100
    assert df.attrs["seed"] == 0


def test_generate_distribution_total_mass_rescaling():
    target = 2.8
    df = generate_distribution(
        500, value_min=1e-6, value_max=1e-2, slope=1.8333,
        total_disk_mass_earth=target, seed=42,
    )
    assert df["mass_earth"].sum() == pytest.approx(target, rel=1e-9)
    # radii stay consistent with the rescaled masses
    assert np.allclose(
        df["radius_km"], masses_to_radii(df["mass_kg"]), rtol=1e-9
    )


def test_generate_distribution_reproducible():
    a = generate_distribution(200, seed=99)
    b = generate_distribution(200, seed=99)
    assert np.array_equal(a["mass_kg"].to_numpy(), b["mass_kg"].to_numpy())


def test_generate_distribution_radius_mode():
    df = generate_distribution(
        300, distribution_variable="radius",
        value_min=1.0, value_max=500.0, slope=3.5, seed=5,
    )
    assert df["radius_km"].min() >= 1.0
    assert df["radius_km"].max() <= 500.0
    assert np.allclose(df["mass_kg"], radii_to_masses(df["radius_km"]), rtol=1e-9)
