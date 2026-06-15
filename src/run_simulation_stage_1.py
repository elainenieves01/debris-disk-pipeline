#!/usr/bin/env python3
"""
run_simulation.py

REBOUND-based prototype for building asteroid-belt dynamical maps.

Main goals of this version:
1. Build a Solar-System-like model from a YAML configuration file.
2. Add massless asteroid test particles on a grid or random distribution.
3. Integrate with WHFast using a fixed timestep.
4. Remove particles that become unbound, collide with the Sun, or reach a very small perihelion.
5. Save a REBOUND SimulationArchive.
6. Produce initial, final, survival-time, and Stage-1 approximate proper-element maps.

Important scientific note
-------------------------
The standard final map in this script still uses osculating or time-averaged
osculating elements. This version also adds Stage-1 approximate synthetic
proper elements from filtered time series of the secular variables h, k, p, q.
These are NOT full AstDyS-quality proper elements; full synthetic proper
elements require stronger filtering and frequency analysis.
"""

import os
import time
import random
import csv
from itertools import product

import rebound
import numpy as np
import matplotlib.pyplot as plt


JUPITER_MASS_TO_SOLAR_MASS = 9.5479e-4


# ============================================================
# Utility functions
# ============================================================

def random_angle():
    """Return a random angle in radians in the interval [0, 2*pi)."""
    return random.random() * 2.0 * np.pi


def format_time(seconds):
    """Format wall-clock time in a readable way."""
    seconds = int(seconds)

    months = seconds // (30 * 24 * 3600)
    seconds %= 30 * 24 * 3600

    weeks = seconds // (7 * 24 * 3600)
    seconds %= 7 * 24 * 3600

    days = seconds // (24 * 3600)
    seconds %= 24 * 3600

    hours = seconds // 3600
    seconds %= 3600

    minutes = seconds // 60
    seconds %= 60

    parts = []

    if months:
        parts.append(f"{months} months")
    if weeks:
        parts.append(f"{weeks} weeks")
    if days:
        parts.append(f"{days} days")
    if hours:
        parts.append(f"{hours} hours")
    if minutes:
        parts.append(f"{minutes} minutes")
    if seconds:
        parts.append(f"{seconds} seconds")

    return ", ".join(parts) if parts else "0 seconds"


def resolve_output_file(config):
    """
    Resolve the output archive path safely.

    Recommended config form:
        simulation:
          output_file: "outputs/simulationarchive.bin"

    If the user writes:
        output_file: "outputs"

    this function interprets it as:
        outputs/simulationarchive.bin

    Extra protection:
    If a regular file called "outputs" already exists from an older run,
    the script automatically renames that file to "outputs.backup_<timestamp>"
    and then creates the directory "outputs/".

    This avoids the common error:
        FileExistsError: [Errno 17] File exists: 'outputs'
    """
    output_file = str(config["simulation"]["output_file"])

    # If output_file is a directory-like path, use a default archive name inside it.
    if output_file.endswith(os.sep) or output_file in {"outputs", "output", "archive"}:
        output_file = os.path.join(output_file, "simulationarchive.bin")

    output_dir = os.path.dirname(output_file)

    if output_dir:
        # If a regular file already exists with the same name as the desired
        # directory, rename it automatically instead of stopping the program.
        if os.path.exists(output_dir) and not os.path.isdir(output_dir):
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            backup_name = f"{output_dir}.backup_{timestamp}"

            os.rename(output_dir, backup_name)

            print(
                f"Warning: '{output_dir}' existed as a regular file, not a directory.\n"
                f"         It was renamed to '{backup_name}'.\n"
                f"         A new directory '{output_dir}/' will be created."
            )

        os.makedirs(output_dir, exist_ok=True)

    # If an old archive file exists, remove it before starting a new run.
    # REBOUND appends snapshots to SimulationArchive files, so removing
    # the old file avoids mixing old and new simulations.
    if os.path.exists(output_file):
        if os.path.isdir(output_file):
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            backup_name = f"{output_file.rstrip(os.sep)}.backup_dir_{timestamp}"
            os.rename(output_file, backup_name)

            print(
                f"Warning: output archive path '{output_file}' was a directory.\n"
                f"         It was renamed to '{backup_name}'."
            )
        else:
            os.remove(output_file)

    return output_file

def remove_particle_from_sim(sim, initial_conditions, index):
    """
    Remove a particle from the REBOUND simulation and update stored indices.

    REBOUND particles are stored in an array. When one particle is removed,
    all particles after it shift by one position. Therefore, every saved
    particle_index larger than the removed index must be decreased by one.
    """
    sim.remove(index)

    for ic in initial_conditions.values():
        if ic.get("particle_index", -1) > index:
            ic["particle_index"] -= 1


def mark_lost(sim, initial_conditions, particle_id, reason):
    """
    Mark a test particle as lost and remove it from the REBOUND simulation.

    This function protects against removing a particle twice.
    """
    ic = initial_conditions[particle_id]

    if ic["status"] == "lost":
        return

    index = ic["particle_index"]

    ic["status"] = "lost"
    ic["loss_reason"] = reason
    ic["survival_time"] = sim.t

    if 0 <= index < sim.N:
        remove_particle_from_sim(sim, initial_conditions, index)


# ============================================================
# Plotting functions
# ============================================================

def plot_initial_map(initial_conditions, png_file_name, config):
    """Plot the initial asteroid grid in (a,e) and (a,sin i)."""
    a_vals = [float(ic["a0"]) for ic in initial_conditions.values()]
    e_vals = [float(ic["e0"]) for ic in initial_conditions.values()]
    sini_vals = [float(np.sin(ic["inc0"])) for ic in initial_conditions.values()]

    fig, axes = plt.subplots(1, 2, figsize=(12, 5), sharex=True)

    axes[0].scatter(a_vals, e_vals, c="black", s=1)
    axes[0].set_xlabel("Initial a [AU]")
    axes[0].set_ylabel("Initial e")
    axes[0].set_title("Initial map: (a, e)")
    axes[0].set_xlim(config["disk"]["amin"], config["disk"]["amax"])
    axes[0].set_ylim(config["disk"]["emin"], config["disk"]["emax"])

    axes[1].scatter(a_vals, sini_vals, c="black", s=1)
    axes[1].set_xlabel("Initial a [AU]")
    axes[1].set_ylabel(r"$\sin(i_0)$")
    axes[1].set_title(r"Initial map: $(a, \sin i)$")
    axes[1].set_xlim(config["disk"]["amin"], config["disk"]["amax"])
    axes[1].set_ylim(
        np.sin(np.radians(config["disk"]["imin_deg"])),
        np.sin(np.radians(config["disk"]["imax_deg"]))
    )

    plt.tight_layout()
    plt.savefig(png_file_name, dpi=300, bbox_inches="tight")
    plt.close(fig)


def plot_final_map(final_conditions, png_file_name, config):
    """
    Plot surviving particles using mean osculating elements.

    Important:
    These are not proper elements. They are simple time averages of
    osculating orbital elements sampled during the integration.
    """
    survived = {
        k: v for k, v in final_conditions.items()
        if v.get("status") == "survived"
    }

    if len(survived) == 0:
        print("No surviving particles to plot in final map.")
        return

    a_vals = [float(ic["a"]) for ic in survived.values()]
    e_vals = [float(ic["e"]) for ic in survived.values()]
    sini_vals = [float(np.sin(ic["inc"])) for ic in survived.values()]

    fig, axes = plt.subplots(1, 2, figsize=(12, 5), sharex=True)

    axes[0].scatter(a_vals, e_vals, c="black", s=1)
    axes[0].set_xlabel("Mean osculating a [AU]")
    axes[0].set_ylabel("Mean osculating e")
    axes[0].set_title("Final survivor map: (mean a, mean e)")
    axes[0].set_xlim(config["disk"]["amin"], config["disk"]["amax"])
    axes[0].set_ylim(config["disk"]["emin"], config["disk"]["emax"])

    axes[1].scatter(a_vals, sini_vals, c="black", s=1)
    axes[1].set_xlabel("Mean osculating a [AU]")
    axes[1].set_ylabel(r"$\sin(\mathrm{mean}\ i)$")
    axes[1].set_title(r"Final survivor map: $(\mathrm{mean}\ a, \sin \mathrm{mean}\ i)$")
    axes[1].set_xlim(config["disk"]["amin"], config["disk"]["amax"])
    axes[1].set_ylim(
        np.sin(np.radians(config["disk"]["imin_deg"])),
        np.sin(np.radians(config["disk"]["imax_deg"]))
    )

    plt.tight_layout()
    plt.savefig(png_file_name, dpi=300, bbox_inches="tight")
    plt.close(fig)


def plot_survival_time_map(initial_conditions, png_file_name, config):
    """
    Plot the initial (a,e) grid colored by survival time.

    This is more informative than plotting only the surviving particles.
    Unstable regions appear as particles with shorter survival times.
    """
    a_vals = np.array([ic["a0"] for ic in initial_conditions.values()])
    e_vals = np.array([ic["e0"] for ic in initial_conditions.values()])
    survival_times = np.array([ic.get("survival_time", 0.0) for ic in initial_conditions.values()])

    fig, ax = plt.subplots(figsize=(8, 6))

    sc = ax.scatter(a_vals, e_vals, c=survival_times, s=3)
    cbar = plt.colorbar(sc, ax=ax)
    cbar.set_label("Survival time [yr]")

    ax.set_xlabel("Initial a [AU]")
    ax.set_ylabel("Initial e")
    ax.set_title("Dynamical map colored by survival time")
    ax.set_xlim(config["disk"]["amin"], config["disk"]["amax"])
    ax.set_ylim(config["disk"]["emin"], config["disk"]["emax"])

    plt.tight_layout()
    plt.savefig(png_file_name, dpi=300, bbox_inches="tight")
    plt.close(fig)


def plot_max_e_map(initial_conditions, png_file_name, config):
    """
    Plot the initial (a,e) grid colored by maximum eccentricity reached.

    This is useful for identifying chaotic diffusion even when particles
    do not escape during the integration.
    """
    a_vals = np.array([ic["a0"] for ic in initial_conditions.values()])
    e_vals = np.array([ic["e0"] for ic in initial_conditions.values()])
    max_e = np.array([ic.get("max_e", ic["e0"]) for ic in initial_conditions.values()])

    fig, ax = plt.subplots(figsize=(8, 6))

    sc = ax.scatter(a_vals, e_vals, c=max_e, s=3)
    cbar = plt.colorbar(sc, ax=ax)
    cbar.set_label("Maximum eccentricity")

    ax.set_xlabel("Initial a [AU]")
    ax.set_ylabel("Initial e")
    ax.set_title("Dynamical map colored by maximum eccentricity")
    ax.set_xlim(config["disk"]["amin"], config["disk"]["amax"])
    ax.set_ylim(config["disk"]["emin"], config["disk"]["emax"])

    plt.tight_layout()
    plt.savefig(png_file_name, dpi=300, bbox_inches="tight")
    plt.close(fig)



# ============================================================
# Stage-1 approximate synthetic proper elements
# ============================================================

def moving_average_filter(x, window):
    """
    Apply a simple boxcar moving-average filter.

    This is a first-stage digital smoothing step, not a full professional
    proper-element filter. It suppresses short-period oscillations before
    estimating secular amplitudes.
    """
    x = np.asarray(x, dtype=float)

    if window <= 1 or len(x) < window:
        return x.copy()

    kernel = np.ones(window, dtype=float) / float(window)
    return np.convolve(x, kernel, mode="valid")


def initialize_proper_series(initial_conditions):
    """
    Create time-series storage for Stage-1 approximate proper elements.

    For each particle we store:
        a
        h = e sin(varpi)
        k = e cos(varpi)
        p = sin(i) sin(Omega)
        q = sin(i) cos(Omega)

    where varpi = Omega + omega.
    """
    return {
        particle_id: {"t": [], "a": [], "h": [], "k": [], "p": [], "q": []}
        for particle_id in initial_conditions
    }


def store_proper_sample(proper_series, particle_id, t, orb):
    """Store one osculating-element sample for one test particle."""
    varpi = orb.Omega + orb.omega

    h = orb.e * np.sin(varpi)
    k = orb.e * np.cos(varpi)

    p_inc = np.sin(orb.inc) * np.sin(orb.Omega)
    q_inc = np.sin(orb.inc) * np.cos(orb.Omega)

    proper_series[particle_id]["t"].append(float(t))
    proper_series[particle_id]["a"].append(float(orb.a))
    proper_series[particle_id]["h"].append(float(h))
    proper_series[particle_id]["k"].append(float(k))
    proper_series[particle_id]["p"].append(float(p_inc))
    proper_series[particle_id]["q"].append(float(q_inc))


def compute_approx_synthetic_proper_elements(
    proper_series,
    initial_conditions,
    filter_window=101,
    discard_fraction=0.20,
    min_samples=50,
):
    """
    Compute Stage-1 approximate synthetic proper elements.

    The output is approximate:
        a_p      = mean of filtered a
        e_p      = approximate free eccentricity-vector amplitude
        sin_i_p  = approximate free inclination-vector amplitude

    The forced vector is approximated by the mean of the filtered h-k and p-q
    variables. This is useful for exploratory maps but should not be presented
    as full proper elements in a publication without stronger validation.
    """
    proper_elements = {}

    for particle_id, data in proper_series.items():
        ic = initial_conditions[particle_id]

        base_row = {
            "a0": float(ic["a0"]),
            "e0": float(ic["e0"]),
            "sin_i0": float(np.sin(ic["inc0"])),
            "survival_time": float(ic.get("survival_time", 0.0)),
            "loss_reason": ic.get("loss_reason"),
        }

        if ic["status"] == "lost":
            proper_elements[particle_id] = {
                "status": "lost",
                **base_row,
                "a_p": np.nan,
                "e_p": np.nan,
                "sin_i_p": np.nan,
                "N_samples": len(data["a"]),
            }
            continue

        a = np.asarray(data["a"], dtype=float)
        h = np.asarray(data["h"], dtype=float)
        k = np.asarray(data["k"], dtype=float)
        p = np.asarray(data["p"], dtype=float)
        q = np.asarray(data["q"], dtype=float)

        if len(a) < min_samples:
            proper_elements[particle_id] = {
                "status": "failed_too_few_samples",
                **base_row,
                "a_p": np.nan,
                "e_p": np.nan,
                "sin_i_p": np.nan,
                "N_samples": len(a),
                "loss_reason": "too_few_samples",
            }
            continue

        # Smooth all variables with the same moving-average window.
        a_f = moving_average_filter(a, filter_window)
        h_f = moving_average_filter(h, filter_window)
        k_f = moving_average_filter(k, filter_window)
        p_f = moving_average_filter(p, filter_window)
        q_f = moving_average_filter(q, filter_window)

        n = min(len(a_f), len(h_f), len(k_f), len(p_f), len(q_f))

        if n < min_samples:
            proper_elements[particle_id] = {
                "status": "failed_too_few_filtered_samples",
                **base_row,
                "a_p": np.nan,
                "e_p": np.nan,
                "sin_i_p": np.nan,
                "N_samples": len(a),
                "loss_reason": "too_few_filtered_samples",
            }
            continue

        a_f = a_f[:n]
        h_f = h_f[:n]
        k_f = k_f[:n]
        p_f = p_f[:n]
        q_f = q_f[:n]

        # Discard the beginning of the filtered signal to reduce dependence on
        # initial transient behavior.
        start = int(discard_fraction * n)
        a_f = a_f[start:]
        h_f = h_f[start:]
        k_f = k_f[start:]
        p_f = p_f[start:]
        q_f = q_f[start:]

        if len(a_f) < min_samples:
            proper_elements[particle_id] = {
                "status": "failed_too_few_post_discard_samples",
                **base_row,
                "a_p": np.nan,
                "e_p": np.nan,
                "sin_i_p": np.nan,
                "N_samples": len(a),
                "loss_reason": "too_few_post_discard_samples",
            }
            continue

        a_p = np.mean(a_f)

        # Approximate forced component by the mean vector.
        h_free = h_f - np.mean(h_f)
        k_free = k_f - np.mean(k_f)
        p_free = p_f - np.mean(p_f)
        q_free = q_f - np.mean(q_f)

        # If x = A cos(gt), std(x) = A/sqrt(2). Combining both vector
        # components gives a rough free-amplitude estimate.
        e_p = np.sqrt(2.0) * np.sqrt(np.var(h_free) + np.var(k_free))
        sin_i_p = np.sqrt(2.0) * np.sqrt(np.var(p_free) + np.var(q_free))

        proper_elements[particle_id] = {
            "status": "ok",
            **base_row,
            "a_p": float(a_p),
            "e_p": float(e_p),
            "sin_i_p": float(sin_i_p),
            "N_samples": len(a),
            "loss_reason": None,
        }

    return proper_elements


def save_proper_elements_csv(proper_elements, csv_file_name):
    """Save the Stage-1 approximate proper elements to a CSV file."""
    fieldnames = [
        "particle_id",
        "status",
        "a0",
        "e0",
        "sin_i0",
        "a_p",
        "e_p",
        "sin_i_p",
        "N_samples",
        "survival_time",
        "loss_reason",
    ]

    with open(csv_file_name, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for particle_id, pe in proper_elements.items():
            row = {"particle_id": particle_id}
            row.update(pe)
            writer.writerow(row)


def plot_approx_proper_element_map(proper_elements, png_file_name, config):
    """
    Plot Stage-1 approximate synthetic proper-element maps.

    Left panel:  (a_p, e_p)
    Right panel: (a_p, sin i_p)
    """
    good = {
        particle_id: pe
        for particle_id, pe in proper_elements.items()
        if pe.get("status") == "ok"
        and np.isfinite(pe.get("a_p", np.nan))
        and np.isfinite(pe.get("e_p", np.nan))
        and np.isfinite(pe.get("sin_i_p", np.nan))
    }

    if len(good) == 0:
        print("No valid approximate proper elements to plot.")
        return

    a_p = np.array([pe["a_p"] for pe in good.values()])
    e_p = np.array([pe["e_p"] for pe in good.values()])
    sin_i_p = np.array([pe["sin_i_p"] for pe in good.values()])

    fig, axes = plt.subplots(1, 2, figsize=(12, 5), sharex=True)

    axes[0].scatter(a_p, e_p, c="black", s=1)
    axes[0].set_xlabel(r"Approx. proper semimajor axis $a_p$ [AU]")
    axes[0].set_ylabel(r"Approx. proper eccentricity $e_p$")
    axes[0].set_title(r"Stage-1 approximate proper map: $(a_p, e_p)$")
    axes[0].set_xlim(config["disk"]["amin"], config["disk"]["amax"])

    axes[1].scatter(a_p, sin_i_p, c="black", s=1)
    axes[1].set_xlabel(r"Approx. proper semimajor axis $a_p$ [AU]")
    axes[1].set_ylabel(r"Approx. proper $\sin i_p$")
    axes[1].set_title(r"Stage-1 approximate proper map: $(a_p, \sin i_p)$")
    axes[1].set_xlim(config["disk"]["amin"], config["disk"]["amax"])

    plt.tight_layout()
    plt.savefig(png_file_name, dpi=300, bbox_inches="tight")
    plt.close(fig)


# ============================================================
# Simulation builder
# ============================================================

def build_simulation(config):
    """
    Build a REBOUND simulation from the YAML configuration.

    The model is:
    - one central star,
    - massive planets,
    - optional massive dwarf planets,
    - massless asteroid test particles.
    """
    Mstar = float(config["star"]["mass"])
    planets_config = config["planets"]
    disk = config["disk"]

    amin = float(disk["amin"])
    amax = float(disk["amax"])
    emin = float(disk["emin"])
    emax = float(disk["emax"])
    imin = np.deg2rad(float(disk["imin_deg"]))
    imax = np.deg2rad(float(disk["imax_deg"]))

    npl = int(config["dwarf_planets"]["N"])
    mass_fraction = float(
        config["dwarf_planets"].get("mass_fraction_of_planet", 1.0e-5)
    )

    sim = rebound.Simulation()

    sim.units = (
        config["units"]["time"],
        config["units"]["length"],
        config["units"]["mass"],
    )

    sim.integrator = config["integration"]["integrator"]
    sim.collision = "none"
    sim.exit_max_distance = float(config["integration"]["exit_max_distance"])

    # ------------------------------------------------------------
    # Add the star
    # ------------------------------------------------------------
    sim.add(m=Mstar)

    # ------------------------------------------------------------
    # Add planets
    # ------------------------------------------------------------
    n_planets = len(planets_config)

    for gp in planets_config:
        M_planet = float(gp["mass_jupiter"]) * JUPITER_MASS_TO_SOLAR_MASS
        a_planet = float(gp["a"])
        e_planet = float(gp["e"])
        inc_planet = np.deg2rad(float(gp["inc_deg"]))
        omega_planet = np.deg2rad(float(gp["omega_deg"]))

        t_peri = float(gp["t_peri_jd"])
        orbital_period = float(gp["orbital_period_days"])
        epoch_t = float(gp["epoch_jd"])

        # Mean anomaly at epoch:
        # M = n * (t_epoch - t_peri)
        # where n = 2*pi/P.
        MA_planet = (2.0 * np.pi / orbital_period) * (epoch_t - t_peri)
        MA_planet = np.mod(MA_planet, 2.0 * np.pi)

        if "Omega_deg" in gp:
            Omega_planet = np.deg2rad(float(gp["Omega_deg"]))
        elif gp.get("Omega_random", False):
            # Random node is acceptable for synthetic tests,
            # but not recommended for real Solar-System configurations.
            Omega_planet = random_angle()
        else:
            Omega_planet = 0.0

        sim.add(
            primary=sim.particles[0],
            m=M_planet,
            a=a_planet,
            e=e_planet,
            inc=inc_planet,
            omega=omega_planet,
            Omega=Omega_planet,
            M=MA_planet,
        )

    # ------------------------------------------------------------
    # Add optional massive dwarf planets
    # ------------------------------------------------------------
    if n_planets > 0:
        ref_planet = planets_config[0]
        M_ref = float(ref_planet["mass_jupiter"]) * JUPITER_MASS_TO_SOLAR_MASS
        mdps = M_ref * mass_fraction
    else:
        mdps = 0.0

    for _ in range(npl):
        sim.add(
            primary=sim.particles[0],
            m=mdps,
            a=np.random.uniform(amin, amax),
            e=np.random.uniform(emin, emax),
            inc=np.random.uniform(imin, imax),
            omega=random_angle(),
            Omega=random_angle(),
            M=random_angle(),
        )

    # Number of massive/active particles:
    # star + planets + optional massive dwarf planets.
    # All particles added after this point are massless test particles.
    sim.N_active = 1 + n_planets + npl

    # Move the massive system to the center-of-mass frame.
    # After this call, the Sun is not exactly at (0, 0, 0).
    # Therefore, distances to the Sun must later be computed relative
    # to sim.particles[0], not relative to the coordinate origin.
    sim.move_to_com()

    # ------------------------------------------------------------
    # Add massless asteroid test particles
    # ------------------------------------------------------------
    distribution = config["test_particles"].get("distribution", "grid")
    initial_conditions = {}
    counter = 0

    if distribution == "grid":
        Na = int(config["test_particles"].get("Na", 50))
        Ne = int(config["test_particles"].get("Ne", 50))
        Ninc = int(config["test_particles"].get("Ninc", 1))

        list_a = np.linspace(amin, amax, Na)
        list_e = np.linspace(emin, emax, Ne)
        list_i = np.linspace(imin, imax, Ninc)

        for a, e, inc in product(list_a, list_e, list_i):
            omega = random_angle()
            Omega = random_angle()
            M = random_angle()

            initial_conditions[counter] = {
                "particle_index": sim.N,
                "a0": float(a),
                "e0": float(e),
                "inc0": float(inc),
                "omega0": float(omega),
                "Omega0": float(Omega),
                "M0": float(M),
                "status": "survived",
                "loss_reason": None,
                "survival_time": 0.0,
                "max_e": float(e),
            }

            sim.add(
                primary=sim.particles[0],
                m=0.0,
                a=a,
                e=e,
                inc=inc,
                omega=omega,
                Omega=Omega,
                M=M,
            )

            counter += 1

    elif distribution == "uniform":
        Ntest = int(config["test_particles"].get("N", 1000))

        for _ in range(Ntest):
            a = np.random.uniform(amin, amax)
            e = np.random.uniform(emin, emax)
            inc = np.random.uniform(imin, imax)
            omega = random_angle()
            Omega = random_angle()
            M = random_angle()

            initial_conditions[counter] = {
                "particle_index": sim.N,
                "a0": float(a),
                "e0": float(e),
                "inc0": float(inc),
                "omega0": float(omega),
                "Omega0": float(Omega),
                "M0": float(M),
                "status": "survived",
                "loss_reason": None,
                "survival_time": 0.0,
                "max_e": float(e),
            }

            sim.add(
                primary=sim.particles[0],
                m=0.0,
                a=a,
                e=e,
                inc=inc,
                omega=omega,
                Omega=Omega,
                M=M,
            )

            counter += 1

    else:
        raise ValueError(
            f"Unknown test particle distribution '{distribution}'. "
            f"Use 'grid' or 'uniform'."
        )

    print(f"Number of test particles: {len(initial_conditions)}")
    print(f"Total particles in simulation: {sim.N}")

    # ------------------------------------------------------------
    # Set timestep
    # ------------------------------------------------------------
    timestep_fraction = float(
        config["integration"].get("timestep_fraction_of_planet_period", 0.01)
    )

    planet_periods = [
        sim.particles[1 + i].P
        for i in range(n_planets)
        if hasattr(sim.particles[1 + i], "P") and sim.particles[1 + i].P > 0
    ]

    dt_planet = timestep_fraction * min(planet_periods) if planet_periods else timestep_fraction

    # A conservative timestep based on the shortest particle period.
    # This protects the integration if the inner edge of the disk has
    # a shorter period than the planets.
    particle_periods = [
        p.P
        for p in sim.particles[1 + n_planets + npl:]
        if hasattr(p, "P") and p.P > 0
    ]

    if particle_periods:
        dt_particle = 0.05 * min(particle_periods)
    else:
        dt_particle = dt_planet

    sim.dt = min(dt_planet, dt_particle)

    # If timestep_days is explicitly provided in the config, it overrides
    # the automatically estimated timestep.
    if "timestep_days" in config["integration"]:
        sim.dt = float(config["integration"]["timestep_days"]) / 365.25

    # Optional WHFast settings.
    # REBOUND versions differ in how they expose WHFast options.
    # Older versions may use sim.ri_whfast.
    # Newer versions may use sim.integrator.
    # If neither interface is available, the simulation runs with default WHFast settings.

    if str(config["integration"]["integrator"]).lower() == "whfast":

        whfast_obj = None

        if hasattr(sim, "ri_whfast"):
            whfast_obj = sim.ri_whfast
        elif hasattr(sim, "integrator"):
            whfast_obj = sim.integrator

        if whfast_obj is not None:
            if hasattr(whfast_obj, "safe_mode"):
                whfast_obj.safe_mode = int(config["integration"].get("whfast_safe_mode", 1))

            if "whfast_corrector" in config["integration"] and hasattr(whfast_obj, "corrector"):
                whfast_obj.corrector = int(config["integration"]["whfast_corrector"])
        else:
            print("Warning: WHFast settings object not found. Using default WHFast settings.")


    print(f"Timestep: {sim.dt:.6e} yr")
    print(f"Timestep: {sim.dt * 365.25:.3f} days")

    return sim, initial_conditions


# ============================================================
# Main integration
# ============================================================

def run_simulation(config):
    """
    Run the asteroid dynamical-map simulation.
    """
    maxtime = float(config["integration"]["maxtime"])
    output_interval = float(config["integration"].get("output_interval", 1000.0))

    times = np.arange(0.0, maxtime + output_interval, output_interval)
    Noutputs = len(times)

    output_file = resolve_output_file(config)

    sim, initial_conditions = build_simulation(config)

    # Storage for Stage-1 approximate synthetic proper elements.
    proper_series = initialize_proper_series(initial_conditions)

    # Produce the initial map before integration.
    plot_initial_map(
        initial_conditions,
        png_file_name="initial_dynamical_map.png",
        config=config,
    )

    E0 = sim.energy()

    print("\nBeginning the main integration")
    print(f"Output archive: {output_file}")
    print(f"Number of outputs: {Noutputs}")
    print(f"Integration end time: {maxtime:.3e} yr")
    print(f"Output interval: {output_interval:.3e} yr\n")

    start_walltime = time.time()

    # Orbital sums for simple time averages of osculating elements.
    orbital_sums = {
        particle_id: {
            "a": 0.0,
            "e": 0.0,
            "sin_inc": 0.0,
            "cos_inc": 0.0,
            "sin_omega": 0.0,
            "cos_omega": 0.0,
            "sin_Omega": 0.0,
            "cos_Omega": 0.0,
            "sin_M": 0.0,
            "cos_M": 0.0,
            "count": 0,
        }
        for particle_id in initial_conditions
    }

    # Removal thresholds.
    #
    # sun_collision_distance:
    #     Heliocentric distance below which a particle is considered lost
    #     by collision with the Sun. Default 0.01 AU.
    #
    # min_perihelion:
    #     If q = a(1-e) becomes smaller than this value, the particle is
    #     removed. This helps avoid WHFast convergence issues caused by
    #     particles entering very short-period orbits.
    sun_collision_distance = float(config["integration"].get("sun_collision_distance", 0.01))
    min_perihelion = float(config["integration"].get("min_perihelion", 0.3))

    for i, int_time in enumerate(times):
        try:
            # For WHFast, avoid forcing the integration to finish exactly
            # at each requested output time.
            #
            # Forcing exact output times can require a shortened final step.
            # That weakens the symplectic behavior of a fixed-timestep
            # integrator in long-term integrations.
            #
            # With exact_finish_time=0, REBOUND advances to the nearest
            # normal timestep instead of changing the step size.
            sim.integrate(int_time, exact_finish_time=0)

            # Loop over test particles.
            # We do not change the dictionary size here. We only update
            # the fields stored for each particle.
            for particle_id, ic in initial_conditions.items():

                # Important:
                # once a particle is lost and removed from REBOUND,
                # its old index must not be used again.
                if ic["status"] == "lost":
                    continue

                index = ic["particle_index"]

                if index >= sim.N:
                    ic["status"] = "lost"
                    ic["loss_reason"] = "index_out_of_range"
                    ic["survival_time"] = sim.t
                    continue

                p = sim.particles[index]
                sun = sim.particles[0]

                # After sim.move_to_com(), the Sun is no longer exactly at
                # (0, 0, 0). Therefore, distances to the Sun must be computed
                # relative to sim.particles[0], not relative to the origin.
                dx = p.x - sun.x
                dy = p.y - sun.y
                dz = p.z - sun.z
                r_sun2 = dx*dx + dy*dy + dz*dz
                r_sun = np.sqrt(r_sun2)

                # Remove particles ejected far from the Sun.
                if r_sun > sim.exit_max_distance:
                    mark_lost(sim, initial_conditions, particle_id, "ejected")
                    continue

                # Remove particles that collide with or pass too close to the Sun.
                if r_sun < sun_collision_distance:
                    mark_lost(sim, initial_conditions, particle_id, "sun_collision")
                    continue

                try:
                    # Osculating orbital elements relative to the Sun.
                    orb = p.orbit(primary=sun)

                    # Remove unbound or hyperbolic particles.
                    if orb.e >= 1.0 or orb.a <= 0.0:
                        mark_lost(sim, initial_conditions, particle_id, "unbound")
                        continue

                    # Remove particles whose perihelion becomes too small.
                    # This avoids integrating particles that are no longer
                    # main-belt-like asteroids and may create timestep problems.
                    q = orb.a * (1.0 - orb.e)

                    if q < min_perihelion:
                        mark_lost(sim, initial_conditions, particle_id, "small_perihelion")
                        continue

                    # Store the sample used for Stage-1 approximate synthetic
                    # proper elements. Only surviving, bound, main-belt-like
                    # particles are sampled.
                    store_proper_sample(
                        proper_series=proper_series,
                        particle_id=particle_id,
                        t=sim.t,
                        orb=orb,
                    )

                    # Track maximum eccentricity for the dynamical map.
                    if orb.e > ic["max_e"]:
                        ic["max_e"] = float(orb.e)

                    # If the particle survives this output, update its survival time.
                    ic["survival_time"] = sim.t

                    # Accumulate time-averaged osculating elements.
                    orbital_sums[particle_id]["a"] += orb.a
                    orbital_sums[particle_id]["e"] += orb.e
                    orbital_sums[particle_id]["sin_inc"] += np.sin(orb.inc)
                    orbital_sums[particle_id]["cos_inc"] += np.cos(orb.inc)
                    orbital_sums[particle_id]["sin_omega"] += np.sin(orb.omega)
                    orbital_sums[particle_id]["cos_omega"] += np.cos(orb.omega)
                    orbital_sums[particle_id]["sin_Omega"] += np.sin(orb.Omega)
                    orbital_sums[particle_id]["cos_Omega"] += np.cos(orb.Omega)
                    orbital_sums[particle_id]["sin_M"] += np.sin(orb.M)
                    orbital_sums[particle_id]["cos_M"] += np.cos(orb.M)
                    orbital_sums[particle_id]["count"] += 1

                except Exception as error:
                    # If orbital element calculation fails, mark the particle lost.
                    # This is safer than silently ignoring problematic particles.
                    ic["status"] = "lost"
                    ic["loss_reason"] = f"orbit_error: {error}"
                    ic["survival_time"] = sim.t
                    continue

            # Save current snapshot to the SimulationArchive.
            sim.save_to_file(output_file)

            E1 = sim.energy()
            dE_over_E0 = (E1 - E0) / E0 if E0 != 0.0 else np.nan

            elapsed_total = time.time() - start_walltime
            completed_outputs = i + 1
            avg_time_per_output = elapsed_total / completed_outputs
            remaining_outputs = Noutputs - completed_outputs
            estimated_remaining = avg_time_per_output * remaining_outputs

            n_surviving_now = sum(
                1 for ic in initial_conditions.values()
                if ic["status"] == "survived"
            )

            print(f"    Output {completed_outputs}/{Noutputs}")
            print(f"    Requested time       = {int_time:.3e} yr")
            print(f"    Actual sim time      = {sim.t:.3e} yr")
            print(f"    Current REBOUND N    = {sim.N}")
            print(f"    Surviving test parts = {n_surviving_now}")
            print(f"    dE/E0                = {dE_over_E0:.3e}")

            if completed_outputs >= 2:
                print(f"    Estimated remaining  = {format_time(estimated_remaining)}\n")
            else:
                print()

        except rebound.Escape:
            # REBOUND can raise an Escape exception when a particle crosses
            # sim.exit_max_distance. We identify and remove such particles.
            for particle_id, ic in initial_conditions.items():
                if ic["status"] == "lost":
                    continue

                index = ic["particle_index"]

                if index >= sim.N:
                    ic["status"] = "lost"
                    ic["loss_reason"] = "index_out_of_range_after_escape"
                    ic["survival_time"] = sim.t
                    continue

                p = sim.particles[index]
                sun = sim.particles[0]

                dx = p.x - sun.x
                dy = p.y - sun.y
                dz = p.z - sun.z
                r_sun = np.sqrt(dx*dx + dy*dy + dz*dz)

                if r_sun > sim.exit_max_distance:
                    mark_lost(sim, initial_conditions, particle_id, "ejected")
                    print(
                        f"    Particle {particle_id} escaped at "
                        f"t = {sim.t:.3e} yr "
                        f"(r > {sim.exit_max_distance}), remaining: {sim.N}"
                    )

    total_runtime = time.time() - start_walltime

    # ============================================================
    # Build final-condition table
    # ============================================================

    final_conditions = {}

    for particle_id, sums in orbital_sums.items():
        n = sums["count"]
        ic = initial_conditions[particle_id]
        is_lost = ic["status"] == "lost"

        if is_lost or n == 0:
            final_conditions[particle_id] = {
                "status": "lost",
                "N_samples": n,
                "loss_reason": ic.get("loss_reason"),
                "survival_time": ic.get("survival_time", 0.0),
                "max_e": ic.get("max_e", ic["e0"]),
            }
        else:
            final_conditions[particle_id] = {
                "status": "survived",
                "a": sums["a"] / n,
                "e": sums["e"] / n,
                "inc": np.arctan2(sums["sin_inc"], sums["cos_inc"]),
                "omega": np.arctan2(sums["sin_omega"], sums["cos_omega"]),
                "Omega": np.arctan2(sums["sin_Omega"], sums["cos_Omega"]),
                "M": np.arctan2(sums["sin_M"], sums["cos_M"]),
                "N_samples": n,
                "loss_reason": None,
                "survival_time": ic.get("survival_time", sim.t),
                "max_e": ic.get("max_e", ic["e0"]),
            }

    # ============================================================
    # Final plots
    # ============================================================

    plot_final_map(
        final_conditions,
        png_file_name="final_dynamical_map.png",
        config=config,
    )

    plot_survival_time_map(
        initial_conditions,
        png_file_name="survival_time_map.png",
        config=config,
    )

    plot_max_e_map(
        initial_conditions,
        png_file_name="max_eccentricity_map.png",
        config=config,
    )

    # ============================================================
    # Stage-1 approximate synthetic proper elements
    # ============================================================

    proper_config = config.get("proper_elements", {})
    proper_enabled = bool(proper_config.get("enabled", True))

    if proper_enabled:
        filter_window = int(proper_config.get("filter_window", 101))
        discard_fraction = float(proper_config.get("discard_fraction", 0.20))
        min_samples = int(proper_config.get("min_samples", 50))

        print("\nComputing Stage-1 approximate synthetic proper elements")
        print(f"Filter window:    {filter_window} output samples")
        print(f"Discard fraction: {discard_fraction:.2f}")
        print(f"Minimum samples:  {min_samples}")

        proper_elements = compute_approx_synthetic_proper_elements(
            proper_series=proper_series,
            initial_conditions=initial_conditions,
            filter_window=filter_window,
            discard_fraction=discard_fraction,
            min_samples=min_samples,
        )

        save_proper_elements_csv(
            proper_elements,
            csv_file_name="proper_elements_stage1.csv",
        )

        plot_approx_proper_element_map(
            proper_elements,
            png_file_name="approx_proper_element_map.png",
            config=config,
        )

        n_ok_proper = sum(1 for pe in proper_elements.values() if pe.get("status") == "ok")
        print(f"Valid Stage-1 proper elements: {n_ok_proper}/{len(proper_elements)}")
        print("Saved: proper_elements_stage1.csv")
        print("Saved: approx_proper_element_map.png")

    # ============================================================
    # Summary report
    # ============================================================

    n_total = len(final_conditions)
    n_survived = sum(
        1 for fc in final_conditions.values()
        if fc["status"] == "survived"
    )
    n_lost = n_total - n_survived

    loss_reasons = {}

    for fc in final_conditions.values():
        reason = fc.get("loss_reason")
        if reason is not None:
            loss_reasons[reason] = loss_reasons.get(reason, 0) + 1

    print("\n" + "=" * 60)
    print("PARTICLE SUMMARY REPORT")
    print("=" * 60)
    print(f"Total test particles:   {n_total}")
    print(f"Survived:               {n_survived}")
    print(f"Lost:                   {n_lost}")
    print(f"Simulation end:         {sim.t:.3e} yr")
    print(f"Total runtime:          {format_time(total_runtime)}")

    if loss_reasons:
        print("\nLoss reasons:")
        for reason, count in sorted(loss_reasons.items()):
            print(f"  {reason}: {count}")

    print("=" * 60)

    # ============================================================
    # Quick archive check
    # ============================================================

    try:
        sa = rebound.Simulationarchive(output_file)
        print(f"\nSaved archive: {output_file}")
        print(f"Number of snapshots saved: {len(sa)}")
        print(f"Archive time range: {sa.tmin:.3e} yr to {sa.tmax:.3e} yr")
    except Exception as error:
        print(f"\nCould not verify archive: {error}")


# ============================================================
# Script entry point
# ============================================================

def read_config_fallback(config_file):
    """Read a YAML config file if config_utils.py is not available."""
    try:
        import yaml
    except ImportError as exc:
        raise ImportError(
            "PyYAML is required when config_utils.py is not available. "
            "Install it with: pip install pyyaml"
        ) from exc

    with open(config_file, "r") as f:
        return yaml.safe_load(f)


def print_config_fallback(config):
    """Print config in a readable form."""
    try:
        import yaml
        print(yaml.safe_dump(config, sort_keys=False))
    except Exception:
        print(config)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Run REBOUND asteroid-belt map and compute Stage-1 approximate synthetic proper elements."
    )
    parser.add_argument(
        "--config",
        default="../config/config_stage1_proper_test.yaml",
        help="Path to YAML configuration file. Default: ../config/config_stage1_proper_test.yaml",
    )
    args = parser.parse_args()

    try:
        from config_utils import read_config, print_config
    except ImportError:
        read_config = read_config_fallback
        print_config = print_config_fallback

    config = read_config(args.config)

    seed = int(config["simulation"].get("random_seed", 0))
    np.random.seed(seed)
    random.seed(seed)

    print_config(config)
    run_simulation(config)
