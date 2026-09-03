"""
Planetesimal size / mass distribution models.

Standalone helpers for building a population of planetesimals whose masses
follow a truncated power law (a Dohnanyi collisional-cascade spectrum by
default).  Nothing here is wired into ``run_simulation.py`` yet -- see
``make_distribution.py`` for the command-line entry point.
"""

import numpy as np
import pandas as pd


# ============================================================
# Constants
# ============================================================
#
# Kept consistent with src/simulation/run_simulation.py, which uses
#   EARTH_MASS_TO_SOLAR_MASS = 3.0034896149156e-6
#   SOLAR_MASS_G             = 1.98892e33   (i.e. M_sun = 1.98892e30 kg)

M_SUN_KG = 1.98892e30
M_EARTH_KG = M_SUN_KG * 3.0034896149156e-6

# Canonical Dohnanyi (1969) collisional-cascade slopes.
#   differential mass spectrum   dN/dm ~ m^-(11/6)
#   differential size spectrum   dN/da ~ a^-3.5
DOHNANYI_MASS_SLOPE = 11.0 / 6.0
DOHNANYI_SIZE_SLOPE = 3.5


# ============================================================
# Unit conversions
# ============================================================

def radii_to_masses(radii_km, density_g_cm3=1.0):
    """
    Convert spherical particle radii to masses.

    m = (4/3) * pi * rho * R^3

    Parameters
    ----------
    radii_km : array-like
        Particle radii in km.

    density_g_cm3 : float
        Bulk density in g/cm^3.

    Returns
    -------
    masses_kg : numpy.ndarray
        Particle masses in kg.
    """

    radii_km = np.asarray(radii_km, dtype=float)

    radii_m = radii_km * 1000.0
    density_kg_m3 = density_g_cm3 * 1000.0

    masses_kg = (
        (4.0 / 3.0)
        * np.pi
        * density_kg_m3
        * radii_m**3
    )

    return masses_kg


def masses_to_radii(masses_kg, density_g_cm3=1.0):
    """
    Convert spherical particle masses to radii.

    R = [3m / (4*pi*rho)]^(1/3)

    Parameters
    ----------
    masses_kg : array-like
        Particle masses in kg.

    density_g_cm3 : float
        Bulk density in g/cm^3.

    Returns
    -------
    radii_km : numpy.ndarray
        Particle radii in km.
    """

    masses_kg = np.asarray(masses_kg, dtype=float)

    density_kg_m3 = density_g_cm3 * 1000.0

    radii_m = (
        (3.0 * masses_kg)
        / (4.0 * np.pi * density_kg_m3)
    ) ** (1.0 / 3.0)

    radii_km = radii_m / 1000.0

    return radii_km


# ============================================================
# Power-law sampler
# ============================================================

def sample_powerlaw(
    n_particles,
    value_min,
    value_max,
    slope,
    seed=None
):
    """
    Sample from a truncated power law:

        dN/dx proportional to x^(-slope)

    where x can represent radius or mass.  Uses the analytic inverse-CDF
    transform, with a log-uniform special case for ``slope == 1``.

    Parameters
    ----------
    n_particles : int
        Number of samples to draw.
    value_min, value_max : float
        Truncation limits (same units); both must be > 0 and
        value_max > value_min.
    slope : float
        Power-law exponent (the ``q`` in ``dN/dx ~ x^-q``).
    seed : int or numpy.random.Generator or None
        Seed or generator for reproducibility.

    Returns
    -------
    numpy.ndarray
        ``n_particles`` samples in ``[value_min, value_max]``.
    """

    if n_particles <= 0:
        raise ValueError("n_particles must be > 0")

    if value_min <= 0:
        raise ValueError("value_min must be > 0")

    if value_max <= value_min:
        raise ValueError(
            "value_max must be greater than value_min"
        )

    if not np.isfinite(slope):
        raise ValueError("slope must be finite")

    rng = seed if isinstance(seed, np.random.Generator) else np.random.default_rng(seed)

    u = rng.uniform(0.0, 1.0, n_particles)

    # Special case slope = 1
    if np.isclose(slope, 1.0):

        values = value_min * (
            value_max / value_min
        ) ** u

    else:

        exponent = 1.0 - slope

        values = (
            u * (
                value_max**exponent
                - value_min**exponent
            )
            + value_min**exponent
        ) ** (1.0 / exponent)

    return values


# ============================================================
# Main distribution generator
# ============================================================

def generate_distribution(
    n_particles,
    distribution_variable="mass",
    value_min=1.0e-6,
    value_max=1.0e-2,
    slope=DOHNANYI_MASS_SLOPE,
    density_g_cm3=1.0,
    mass_unit="earth",
    total_disk_mass_earth=None,
    seed=None,
):
    """
    Generate a planetesimal size/mass distribution.

    Parameters
    ----------
    n_particles : int
        Number of particles.

    distribution_variable : str
        Either "radius" or "mass" -- which quantity the power law is drawn in.
        Defaults to "mass" (Dohnanyi mass spectrum).

    value_min, value_max : float
        Lower/upper truncation limits for the sampled variable.

        distribution_variable="radius": units are km.
        distribution_variable="mass":   units are set by ``mass_unit``.

    slope : float
        Power-law slope for the selected variable.
            radius:  dN/dR proportional to R^(-slope)
            mass:    dN/dm proportional to m^(-slope)
        Defaults to the Dohnanyi mass slope 11/6.

    density_g_cm3 : float
        Bulk density, used for every radius<->mass conversion.

    mass_unit : str
        Unit of ``value_min`` / ``value_max`` when
        distribution_variable="mass".  One of "kg", "earth", "solar".

    total_disk_mass_earth : float or None
        If given, every sampled mass is rescaled by a single constant factor
        so that the masses sum to this value (in Earth masses), and radii are
        recomputed from the rescaled masses.  This preserves the power-law
        slope but shifts the realized min/max away from ``value_min`` /
        ``value_max``.

    seed : int or numpy.random.Generator or None
        Random seed / generator.

    Returns
    -------
    pandas.DataFrame
        Columns: particle_id, radius_km, mass_kg, mass_earth, mass_solar.
        Sampling parameters are recorded in ``df.attrs``.
    """

    distribution_variable = distribution_variable.lower()

    # --------------------------------------------------------
    # Radius distribution
    # --------------------------------------------------------

    if distribution_variable == "radius":

        radii_km = sample_powerlaw(
            n_particles=n_particles,
            value_min=value_min,
            value_max=value_max,
            slope=slope,
            seed=seed,
        )

        masses_kg = radii_to_masses(radii_km, density_g_cm3=density_g_cm3)

    # --------------------------------------------------------
    # Mass distribution
    # --------------------------------------------------------

    elif distribution_variable == "mass":

        if mass_unit == "kg":
            to_kg = 1.0
        elif mass_unit == "earth":
            to_kg = M_EARTH_KG
        elif mass_unit == "solar":
            to_kg = M_SUN_KG
        else:
            raise ValueError("mass_unit must be 'kg', 'earth', or 'solar'")

        masses_kg = sample_powerlaw(
            n_particles=n_particles,
            value_min=value_min * to_kg,
            value_max=value_max * to_kg,
            slope=slope,
            seed=seed,
        )

        radii_km = masses_to_radii(masses_kg, density_g_cm3=density_g_cm3)

    else:

        raise ValueError(
            "distribution_variable must be 'radius' or 'mass'"
        )

    # --------------------------------------------------------
    # Optional rescaling to a target total disk mass
    # --------------------------------------------------------

    if total_disk_mass_earth is not None:
        target_kg = float(total_disk_mass_earth) * M_EARTH_KG
        current_kg = float(np.sum(masses_kg))
        if current_kg <= 0:
            raise ValueError("sampled masses sum to zero; cannot rescale")
        masses_kg = masses_kg * (target_kg / current_kg)
        radii_km = masses_to_radii(masses_kg, density_g_cm3=density_g_cm3)

    # --------------------------------------------------------
    # Build output table
    # --------------------------------------------------------

    distribution = pd.DataFrame({
        "particle_id": np.arange(n_particles),
        "radius_km": radii_km,
        "mass_kg": masses_kg,
        "mass_earth": masses_kg / M_EARTH_KG,
        "mass_solar": masses_kg / M_SUN_KG,
    })

    distribution.attrs.update({
        "n_particles": int(n_particles),
        "distribution_variable": distribution_variable,
        "slope": float(slope),
        "value_min": float(value_min),
        "value_max": float(value_max),
        "mass_unit": mass_unit,
        "density_g_cm3": float(density_g_cm3),
        "total_disk_mass_earth": (
            None if total_disk_mass_earth is None else float(total_disk_mass_earth)
        ),
        "seed": seed if (seed is None or isinstance(seed, int)) else None,
    })

    return distribution
