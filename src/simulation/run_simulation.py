import os
import time
import random
import rebound
import sys
import urllib.request

_SRC_DIR = os.path.dirname(os.path.abspath(__file__))
for _subdir in ("config_io", "plotting", "diagnostics", "utilities", "mass_models"):
    sys.path.insert(0, os.path.join(_SRC_DIR, "..", _subdir))

from config_utils import read_config
from summary_figures import generate_summary_figures
from report import generate_report
from mass_models import generate_distribution
from plots import (
    plot_per_particle,
    plot_differential_histogram,
    plot_count_histograms,
)
from tee_output import start_capturing_stdout, stop_capturing_stdout
from provenance import (
    run_output_dir_for,
    capture_run_provenance,
    update_run_metadata,
    now_iso,
)
from pathlib import Path
import numpy as np
import pandas as pd
import json


EARTH_MASS_TO_SOLAR_MASS = 3.0034896149156e-6
JUPITER_MASS_TO_SOLAR_MASS = 9.5479e-4
# Pluto mass 1.303e22 kg / solar mass 1.98892e30 kg
PLUTO_MASS_TO_SOLAR_MASS = 6.55135e-9
SOLAR_MASS_G = 1.98892e33
PLUTO_DIAMETER_KM = 2376.6  # Stern et al. 2015 (New Horizons)


def dump_path_for(config):
    """Path to a run's resume snapshot, inside its own output directory.

    Keeping the dump per-run (rather than a single ``dump_data.json`` in the
    working directory) lets several runs execute concurrently without
    clobbering each other's resume state.
    """
    return Path(run_output_dir_for(config)) / "dump_data.json"


def sphere_diameter_from_mass(mass_solar, density_g_per_cm3=1.0):
    """Diameter of a uniform sphere with the given mass and density.

    mass_solar is in solar masses; density defaults to 1 g/cm**3.
    Returns the diameter in kilometres.
    """
    mass_g = mass_solar * SOLAR_MASS_G
    volume_cm3 = mass_g / density_g_per_cm3
    radius_cm = (3.0 * volume_cm3 / (4.0 * np.pi)) ** (1.0 / 3.0)
    return 2.0 * radius_cm / 1.0e5  # cm -> km



def send_ntfy(config, title, message):
    """POST a one-line status to the configured ntfy topic. Never raises.

    Controlled by an optional top-level "notify" section in the config:

        notify:
          enabled: true
          ntfy_topic: "https://ntfy.sh/your-topic"

    If the section is missing, disabled, or has no topic, this is a no-op.
    """
    notify_cfg = config.get("notify") or {}

    if not notify_cfg.get("enabled"):
        return

    topic = notify_cfg.get("ntfy_topic")
    if not topic:
        print("WARNING: notify.enabled is true but notify.ntfy_topic is unset.")
        return

    try:
        request = urllib.request.Request(
            topic,
            data=message.encode("utf-8"),
            headers={"Title": title},
            method="POST",
        )
        urllib.request.urlopen(request, timeout=10)
    except Exception as error:
        print(f"WARNING: ntfy notification failed: {error}")


def random_angle():
    rng = np.random.default_rng(seed=42)
    psi = rng.uniform(0.0,2.0*np.pi)
    return psi


def format_time(seconds):
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


def choose_timestep(sim, config, has_giant_planet, Mstar, a_ref):
    """Pick the integrator timestep.

    With a giant planet, use a fraction of its orbital period (particle 1).
    Without one, use the same fraction of a circular orbital period at
    ``a_ref`` (the inner edge of the disk) around the star.
    """
    fraction = float(
        config["integration"]["timestep_fraction_of_planet_period"]
    )

    if has_giant_planet:
        ref_period = sim.particles[1].P
        basis = "giant planet orbital period"
    else:
        ref_period = 2.0 * np.pi * np.sqrt(a_ref ** 3 / (sim.G * Mstar))
        basis = f"circular period at a={a_ref:g} (disk inner edge)"

    dt = fraction * ref_period
    print(
        f"  Timestep: {dt:.6e} "
        f"({fraction:g} x {basis} = {ref_period:.6e})"
    )
    return dt


# The "distribution" block draws per-planetesimal masses from a power law.
# Two named modes:
#   "total_mass"  - total_disk_mass_earth is the anchor; the sampled masses are
#                   rescaled to sum to it. slope + [min, max] ratio set only the
#                   shape. (Sibling key total_disk_mass_earth is required.)
#   "size_range"  - [min, max] are literal physical limits; each mass follows
#                   from radius + density and the disk mass is whatever the N
#                   bodies sum to. (No sibling mass key.)
DISTRIBUTION_MODES = ("total_mass", "size_range")


def _sample_mp_distribution(dist_cfg, npl, config, total_disk_mass_earth=None):
    """Sample per-planetesimal masses from a power-law "distribution" block.

    Returns the DataFrame from ``generate_distribution`` (columns include
    ``mass_solar``). When ``total_disk_mass_earth`` is given the sampled masses
    are rescaled to sum to it; otherwise ``[min, max]`` are used literally.
    """
    dtype = dist_cfg.get("type", "power_law")
    if dtype != "power_law":
        raise ValueError(
            f"massive_planetesimals.distribution.type='{dtype}' is not supported "
            "(only 'power_law')."
        )

    variable = str(dist_cfg["variable"]).lower()
    unit = str(dist_cfg["unit"]).lower()
    expected_unit = {"radius": "km", "mass": "earth_mass"}
    if variable not in expected_unit:
        raise ValueError(
            "massive_planetesimals.distribution.variable must be 'radius' or 'mass' "
            f"(got '{variable}')."
        )
    if unit != expected_unit[variable]:
        raise ValueError(
            "massive_planetesimals.distribution.unit must be "
            f"'{expected_unit[variable]}' when variable='{variable}' (got '{unit}')."
        )

    seed = dist_cfg.get("seed")
    if seed is None:
        seed = config["simulation"].get("random_seed", 42)

    return generate_distribution(
        n_particles=npl,
        distribution_variable=variable,
        value_min=float(dist_cfg["min"]),
        value_max=float(dist_cfg["max"]),
        slope=float(dist_cfg["slope"]),
        density_g_cm3=1.0,
        mass_unit="earth",
        total_disk_mass_earth=(
            None if total_disk_mass_earth is None else float(total_disk_mass_earth)
        ),
        seed=int(seed),
    )


def _write_distribution_diagnostics(dist_df, dist_cfg, config):
    """Record the sampled input spectrum next to the run (never raises)."""
    try:
        out_dir = Path(run_output_dir_for(config))
        out_dir.mkdir(parents=True, exist_ok=True)

        csv_path = out_dir / "distribution.csv"
        dist_df.to_csv(csv_path, index=False)
        print(f"Saved: {csv_path}")

        label = (
            f"{config['simulation']['name']} - power-law {dist_cfg['variable']} "
            f"spectrum (slope {float(dist_cfg['slope']):g}, N = {len(dist_df)})"
        )
        plot_per_particle(dist_df, out_dir, label=label)
        plot_differential_histogram(
            dist_df, out_dir, slope=float(dist_cfg["slope"]), label=label
        )
        plot_count_histograms(dist_df, out_dir, label=label)
    except Exception as error:
        print(f"WARNING: could not write distribution diagnostics: {error}")


def build_simulation(config):

    random_seed = 42
    rng = np.random.default_rng(random_seed)
    
    Mstar = float(config["star"]["mass"])

    # The giant planet is optional. Set "giant_planet: null" in the config
    # (or omit the section) to integrate the disk around the star alone.
    gp = config.get("giant_planet")
    has_giant_planet = gp is not None

    if has_giant_planet:
        M_planet = float(gp["mass_jupiter"]) * JUPITER_MASS_TO_SOLAR_MASS
        a_planet = float(gp["a"])
        e_planet = float(gp["e"])
        inc_planet = np.deg2rad(float(gp["inc_deg"]))
        omega_planet = np.deg2rad(float(gp["omega_deg"]))

        t_peri = float(gp["t_peri_jd"])
        orbital_period = float(gp["orbital_period_days"])
        epoch_t = float(gp["epoch_jd"])

        MA_planet = (2.0 * np.pi / orbital_period) * (epoch_t - t_peri)

        if gp["Omega_random"]:
            Omega_planet = random_angle()
        else:
            Omega_planet = 0.0
    else:
        M_planet = 0.0
        print("\nNo giant planet: integrating the disk around the star alone.")

    disk = config["disk"]

    amin = float(disk["amin"])
    amax = float(disk["amax"])

    emin = float(disk["emin"])
    emax = float(disk["emax"])

    imin = np.deg2rad(float(disk["imin_deg"]))
    imax = np.deg2rad(float(disk["imax_deg"]))

    npl = int(config["massive_planetesimals"]["N"])
    Npart = int(config["test_particles"]["N"])


    sim = rebound.Simulation()

    sim.units = (
        config["units"]["time"],
        config["units"]["length"],
        config["units"]["mass"],
    )

    sim.integrator = config["integration"]["integrator"]

    sim.exit_max_distance = float(config["integration"]["exit_max_distance"])
    file_path = dump_path_for(config)

    dump_condition = config['simulation']["dump"]

    if dump_condition and file_path.exists():
        print("Found dump file. Restoring simulation from snapshot...")

        with open(file_path, "r", encoding="utf-8") as file:
            dump_data = json.load(file)

        sim_time = 0.0
        for name, particle in dump_data.items():
            sim.add(
                m=particle["m"],
                x=particle["x"],
                y=particle["y"],
                z=particle["z"],
                vx=particle["vx"],
                vy=particle["vy"],
                vz=particle["vz"],
                name=name,
            )
        
            
            sim_time = particle["time"]

        sim.t = sim_time
        sim.N_active = sum(
            1 for name in dump_data if not name.startswith("TP_")
        )

        sim.dt = choose_timestep(
            sim, config, has_giant_planet, Mstar, amin
        )

        print(
            f"Restored simulation from snapshot number at t={sim.t:.6e} yr "
            f"with N={sim.N} particles."
        )

        return sim

    # Star
    sim.add(m=Mstar, name="star")

    # Giant planet (optional)
    if has_giant_planet:
        sim.add(
            primary=sim.particles[0],
            m=M_planet,
            a=a_planet,
            e=e_planet,
            inc=inc_planet,
            omega=omega_planet,
            Omega=Omega_planet,
            M=MA_planet,
            name="GP",
        )

    sim.dt = choose_timestep(sim, config, has_giant_planet, Mstar, amin)

    # Massive planetesimals
    # ---------------------
    # Planetesimal masses are set by EXACTLY ONE of these keys under
    # "massive_planetesimals" (value not null):
    #
    #   total_disk_mass_earth: M
    #       M is the TOTAL mass of the planetesimal disk, in Earth masses.
    #       Each of the N planetesimals gets an equal share, M / N.
    #
    #   individual_MP_mass_plutos: m
    #       m is the mass of a SINGLE planetesimal, in Pluto masses.
    #       The total disk mass is then m * N.
    #
    #   mass_fraction_of_giant_planet: f   (legacy)
    #       Each planetesimal has mass f * M_giant_planet. Requires a
    #       giant planet.
    #
    # "total_mass_earth" is accepted as a deprecated alias for
    # "total_disk_mass_earth".
    # "massive_planetesimals" used to be referred to as dwarf_planets.
    #
    # An optional "distribution" block draws the N masses from a power law.
    # It has two named modes (distribution.mode):
    #
    #   mode: total_mass   (default)  - needs the sibling total_disk_mass_earth;
    #       the sampled masses are rescaled to sum to it. slope and the
    #       [min, max] ratio set only the shape.
    #
    #   mode: size_range              - no sibling mass key; [min, max] are used
    #       literally and the disk mass is whatever the N bodies sum to.
    #
    #   distribution:
    #     type: power_law
    #     mode: size_range        # total_mass | size_range
    #     variable: radius        # radius | mass
    #     min: 1
    #     max: 100
    #     unit: km                # km for radius, earth_mass for mass
    #     slope: 3.5              # dN/dvariable ~ variable^-slope
    #     seed: 42                # optional

    if npl > 0:
        mp_cfg = config["massive_planetesimals"]

        if mp_cfg.get("total_mass_earth") is not None:
            print(
                "\nWARNING: 'total_mass_earth' is deprecated; "
                "use 'total_disk_mass_earth'."
            )
            if mp_cfg.get("total_disk_mass_earth") is not None:
                raise ValueError(
                    "massive_planetesimals sets both 'total_mass_earth' and "
                    "'total_disk_mass_earth'. Keep only 'total_disk_mass_earth'."
                )
            mp_cfg = {
                **mp_cfg,
                "total_disk_mass_earth": mp_cfg["total_mass_earth"],
            }

        MASS_KEYS = (
            "total_disk_mass_earth",
            "individual_MP_mass_plutos",
            "mass_fraction_of_giant_planet",
        )
        present = [k for k in MASS_KEYS if mp_cfg.get(k) is not None]

        dist_cfg = mp_cfg.get("distribution")
        dist_mode = None
        if dist_cfg is not None:
            dist_mode = str(dist_cfg.get("mode", "total_mass")).lower()
            if dist_mode not in DISTRIBUTION_MODES:
                raise ValueError(
                    "massive_planetesimals.distribution.mode must be one of "
                    f"{DISTRIBUTION_MODES} (got '{dist_mode}')."
                )

        dist_df = None

        if dist_mode == "size_range":
            # Standalone mode: the [min, max] size range and N set everything;
            # the disk mass is an output, so no MASS_KEYS should be set.
            if present:
                raise ValueError(
                    "massive_planetesimals.distribution.mode='size_range' computes "
                    f"the disk mass from the sampled sizes; remove {present}."
                )
            mode = "distribution/size_range"
            mode_note = "power-law size range given; disk mass computed from N bodies"
            dist_df = _sample_mp_distribution(dist_cfg, npl, config)
            mp_masses = dist_df["mass_solar"].to_numpy()
            m_mps = float(np.median(mp_masses))

        else:
            if len(present) != 1:
                raise ValueError(
                    "massive_planetesimals must set exactly one of "
                    f"{MASS_KEYS} (found: {present or 'none'})."
                )

            mode = present[0]

            if dist_cfg is not None and mode != "total_disk_mass_earth":
                raise ValueError(
                    "massive_planetesimals.distribution.mode='total_mass' splits "
                    "'total_disk_mass_earth' by a power law and requires it; it "
                    f"cannot be combined with '{mode}'."
                )

            if mode == "total_disk_mass_earth":
                total_disk_mass_earth = float(mp_cfg["total_disk_mass_earth"])
                m_mps = total_disk_mass_earth * EARTH_MASS_TO_SOLAR_MASS / npl
                mode_note = "total disk mass given; divided evenly among N"
                if dist_cfg is not None:
                    mode_note = "total disk mass given; split among N by a power law"

            elif mode == "individual_MP_mass_plutos":
                individual_MP_mass_plutos = float(mp_cfg["individual_MP_mass_plutos"])
                m_mps = individual_MP_mass_plutos * PLUTO_MASS_TO_SOLAR_MASS
                mode_note = "per-planetesimal mass given; disk mass = m * N"

            else:  # mass_fraction_of_giant_planet
                if not has_giant_planet:
                    raise ValueError(
                        "massive_planetesimals uses 'mass_fraction_of_giant_planet' "
                        "but there is no giant planet. Use 'total_disk_mass_earth' "
                        "or 'individual_MP_mass_plutos' instead."
                    )
                mass_fraction = float(mp_cfg["mass_fraction_of_giant_planet"])
                m_mps = M_planet * mass_fraction
                mode_note = "fraction of giant-planet mass, per planetesimal"

            # Per-particle masses (solar masses): uniform unless the "total_mass"
            # distribution turns total_disk_mass_earth into a spectrum.
            if dist_cfg is not None:
                dist_df = _sample_mp_distribution(
                    dist_cfg, npl, config,
                    total_disk_mass_earth=total_disk_mass_earth,
                )
                mp_masses = dist_df["mass_solar"].to_numpy()
            else:
                mp_masses = np.full(npl, m_mps, dtype=float)

        print("\nMassive planetesimal mass setup:")
        print(f"  Mode: {mode}  ({mode_note})")
        print(f"  Number of planetesimals: {npl}")

        if dist_df is not None:
            masses_earth = dist_df["mass_earth"].to_numpy()
            radius_km = dist_df["radius_km"].to_numpy()
            diam_km = 2.0 * radius_km
            dyn_range = float(dist_cfg["max"]) / float(dist_cfg["min"])
            if dist_mode == "size_range":
                print(
                    f"  Mass spectrum: power_law in {dist_cfg['variable']}, "
                    f"slope={float(dist_cfg['slope']):g}, "
                    f"[{dist_cfg['min']}, {dist_cfg['max']}] {dist_cfg['unit']} "
                    f"(literal limits), seed={dist_df.attrs.get('seed')}"
                )
            else:
                print(
                    f"  Mass spectrum: power_law in {dist_cfg['variable']}, "
                    f"slope={float(dist_cfg['slope']):g}, "
                    f"{dyn_range:g}x dynamic range "
                    f"([{dist_cfg['min']}, {dist_cfg['max']}] {dist_cfg['unit']} "
                    f"sets the shape), seed={dist_df.attrs.get('seed')}"
                )
                print(
                    "  NOTE: absolute scale is fixed by total_disk_mass_earth / N, "
                    "not by the min/max above."
                )
            print(
                "  Per-MP mass (Earth masses): "
                f"min={masses_earth.min():.6e} / "
                f"median={np.median(masses_earth):.6e} / "
                f"max={masses_earth.max():.6e}"
            )
            print(
                "  Per-MP diameter (km, uniform sphere, rho = 1 g/cm**3): "
                f"min={diam_km.min():.3f} / median={np.median(diam_km):.3f} / "
                f"max={diam_km.max():.3f}"
            )
            total_label = (
                "Total disk mass (computed)"
                if dist_mode == "size_range"
                else "Total disk mass"
            )
            print(
                f"  {total_label}: {masses_earth.sum():.6e} Earth masses "
                f"({mp_masses.sum():.6e} Msun)"
            )
        else:
            m_mps_pluto = m_mps / PLUTO_MASS_TO_SOLAR_MASS
            m_mps_earth = m_mps / EARTH_MASS_TO_SOLAR_MASS
            total_disk_earth = m_mps_earth * npl
            mp_diameter_km = sphere_diameter_from_mass(m_mps, density_g_per_cm3=1.0)
            print(
                f"  Individual MP mass: {m_mps_pluto:.6e} Pluto masses / "
                f"{m_mps_earth:.6e} Earth masses / {m_mps:.6e} Msun"
            )
            print(
                f"  Individual MP diameter: {mp_diameter_km:.3f} km "
                f"({mp_diameter_km / PLUTO_DIAMETER_KM:.6e} Pluto diameters) "
                f"(uniform sphere, rho = 1 g/cm**3)"
            )
            print(
                f"  Total disk mass: {total_disk_earth:.6e} Earth masses "
                f"({m_mps * npl:.6e} Msun)"
            )

        for i in range(npl):

            sim.add(
                primary=sim.particles[0],
                m=float(mp_masses[i]),
                a=rng.uniform(amin, amax),
                e=rng.uniform(emin, emax),
                inc=rng.uniform(imin, imax),
                omega=rng.uniform(0,2*np.pi),
                Omega=rng.uniform(0,2*np.pi),
                M = rng.uniform(0,2*np.pi),
                name= f"MP_{i}"
            )

        if dist_df is not None:
            _write_distribution_diagnostics(dist_df, dist_cfg, config)


    else:
        m_mps = 0.0

        print("\nMassive planetesimal mass setup:")
        print("  Number of MPs: 0")
        print("  No massive planetesimals added.")

    sim.N_active = npl + (2 if has_giant_planet else 1)
    sim.move_to_com()

    # Test particles
    for i in range(Npart):
        M_deg = config["disk"].get("M_deg", None)

        if M_deg is None:
            M = rng.uniform(0,2*np.pi)
        else:
            M = np.radians(float(M_deg))

        sim.add(
            primary=sim.particles[0],
            m=0.0,
            a=rng.uniform(amin, amax),
            e=rng.uniform(emin, emax),
            inc=rng.uniform(imin, imax),
            omega=rng.uniform(0,2*np.pi),
            Omega=rng.uniform(0,2*np.pi),
            M = M,
            name= f"TP_{i}"
        )

    return sim


def get_particles(snap_number, sim, dump_path):
    '''
    prints out the particles in a snapshot
    takes in: i, simulation, dump_path ; saves the particle in the dump file
    i is the snapshot number
    example sim = rebound.Simulation()
    '''
    particles = sim.particles
    dict_row = {}

    for i, p in enumerate(particles):
        dict_row[p.name] = {
                "time": sim.t,
                "snapshot_number": snap_number,
                "m": p.m,
                "x": p.x,
                "y": p.y,
                "z": p.z,
                "vx": p.vx,
                "vy": p.vy,
                "vz": p.vz
            }

    # Write to a temp file and atomically rename over dump_path, so a crash
    # (power loss, kill -9) mid-write can never leave a truncated/corrupt
    # checkpoint -- the resume path either sees the old complete file or the
    # new complete file, never a half-written one.
    dump_path = Path(dump_path)
    tmp_path = dump_path.with_suffix(dump_path.suffix + ".tmp")
    with open(tmp_path, "w") as file:
        json.dump(dict_row, file, indent=4)
    os.replace(tmp_path, dump_path)



# Ida & Makino (1993) numerical stirring factor; the canonical value adopted by
# Krivov & Booth (2018) in their Eq. 9. calibration/plot_kirvov_calibration.py
# uses this as a fixed input -- here we invert Eqs. 9-10 to back out the value
# the N-body run actually produced.
KIRVOV_C_E_REFERENCE = 40.0


def _belt_geometry(config):
    """(amin, amax, a_belt, da_belt, Mstar) from the config's disk/star blocks."""
    Mstar = float(config["star"]["mass"])
    amin = float(config["disk"]["amin"])
    amax = float(config["disk"]["amax"])
    return amin, amax, 0.5 * (amin + amax), amax - amin, Mstar


def compute_effective_stirring_C_e(sim, config):
    """Back out the Krivov & Booth (2018) self-stirring constant C_e from a run.

    Krivov & Booth (2018, MNRAS 479, 3300), two-population self-stirring case
    -- negligible-mass field planetesimals stirred by equal-mass stirrers on
    near-circular orbits (their Eqs. 9 and 10):

        T^-1   = (1 / 2 pi) * C_e * Omega * (a / da) * (M / Mstar) * (Mdisc / Mstar)
        RMS(e) = (2 t / T)^(1/4)

    with Omega = sqrt(G Mstar / a^3) the mean motion at the belt centre, a / da
    the belt radius over its full width, M the individual stirrer mass and Mdisc
    the total mass in stirrers -- exactly the terms formed in
    ``calibration/plot_kirvov_calibration.py`` (``krivov_rms_e``).

    Measures RMS(e) of the massive planetesimals at the current ``sim`` state
    (orbits relative to the star, matching ``src/plotting/summary_figures.py``),
    inverts Eq. 10 for T, then Eq. 9 for C_e. Returns a dict of the ingredients
    and results, or ``None`` if the run has no massive planetesimals / t <= 0.
    """
    if int(config["massive_planetesimals"]["N"]) <= 0 or sim.t <= 0.0:
        return None

    star = sim.particles[0]
    mp_indices = [
        k for k in range(1, sim.N)
        if (sim.particles[k].name or "").startswith("MP_")
    ]
    if not mp_indices:
        return None

    n_mp = len(mp_indices)
    e_sq = [sim.particles[k].orbit(primary=star).e ** 2 for k in mp_indices]
    rms_e = float(np.sqrt(np.mean(e_sq)))

    m_disc = float(sum(sim.particles[k].m for k in mp_indices))  # Msun
    m_indiv = m_disc / n_mp                                      # Msun

    _, _, a_belt, da_belt, Mstar = _belt_geometry(config)
    omega = float(np.sqrt(sim.G * Mstar / a_belt ** 3))  # mean motion at belt centre

    # Invert RMS(e) = (2 t / T)^(1/4)  ->  T^-1 = RMS(e)^4 / (2 t)
    t_inv = rms_e ** 4 / (2.0 * sim.t)

    # Invert Eq. 9 for C_e.
    c_e = (
        2.0 * np.pi * t_inv
        / (omega * (a_belt / da_belt) * (m_indiv / Mstar) * (m_disc / Mstar))
    )

    return {
        "t": float(sim.t),
        "n_mp": n_mp,
        "rms_e": rms_e,
        "a_belt": a_belt,
        "da_belt": da_belt,
        "a_over_da": a_belt / da_belt,
        "Mstar": Mstar,
        "m_indiv": m_indiv,
        "m_disc": m_disc,
        "omega": omega,
        "T": float(1.0 / t_inv),
        "C_e": float(c_e),
        "has_giant_planet": config.get("giant_planet") is not None,
        "exceeds_reference": bool(c_e >= KIRVOV_C_E_REFERENCE),
        "reference": KIRVOV_C_E_REFERENCE,
    }


def report_effective_stirring_C_e(sim, config):
    """Print ``compute_effective_stirring_C_e`` and WARN if C_e >= 40. Never raises."""
    try:
        r = compute_effective_stirring_C_e(sim, config)
        if r is None:
            return

        print("\nKrivov & Booth (2018) self-stirring check (Eqs. 9-10):")
        if r["has_giant_planet"]:
            print(
                "  NOTE: a giant planet is present; the two-population "
                "self-stirring model assumes no external perturber, so C_e "
                "below is only indicative."
            )
        print(f"  Final time:                 t = {r['t']:.6e} yr")
        print(f"  RMS eccentricity ({r['n_mp']} MPs):   {r['rms_e']:.6e}")
        print(
            f"  Belt geometry:              a = {r['a_belt']:g}, "
            f"da = {r['da_belt']:g}, a/da = {r['a_over_da']:g}"
        )
        print(
            f"  Masses:                     M_indiv = {r['m_indiv']:.6e} Msun, "
            f"M_disc = {r['m_disc']:.6e} Msun"
        )
        print(f"  Implied stirring timescale: T = {r['T']:.6e} yr")
        print(f"  Effective stirring factor:  C_e = {r['C_e']:.4f}")

        if r["exceeds_reference"]:
            print(
                f"  WARNING: C_e = {r['C_e']:.4f} >= {r['reference']:g} "
                "(Ida & Makino 1993 canonical value) -- this run stirs at or "
                "above the analytic self-stirring rate."
            )
    except Exception as error:
        print(f"WARNING: could not compute effective C_e: {error}")


def compute_stirrer_disk_coverage(sim, config):
    """Check that the stirrers' feeding zones span the belt (Krivov & Booth 2018).

    Self-stirring assumes the stirrers can dynamically reach across the whole
    disk width, i.e.

        N * delta_af  >=  delta_a

    with delta_a = amax - amin the belt width, N the number of stirrers inside
    the belt, and per stirrer

        delta_af = 8 sqrt(3) * h_M * a_M ,   h_M = (M / (3 Mstar))^(1/3)

    (h_M the reduced/mutual Hill factor, a_M the stirrer semi-major axis).

    "Stirrers inside the disk" = the massive planetesimals, plus the giant
    planet if present, whose semi-major axis lies in [amin, amax]. delta_af is
    summed over them, which equals N * delta_af in the equal-mass case.

    Returns a dict of the ingredients and the ``covered`` verdict, or ``None``
    if there are no in-belt stirrers / the belt width is non-positive.
    """
    amin, amax, _, _, Mstar = _belt_geometry(config)
    delta_a = amax - amin
    if delta_a <= 0.0:
        return None

    star = sim.particles[0]
    stirrers = []  # (name, mass_solar, a)
    for k in range(1, sim.N):
        p = sim.particles[k]
        name = p.name or ""
        if not (name.startswith("MP_") or name == "GP"):
            continue
        a = p.orbit(primary=star).a
        if amin <= a <= amax:
            stirrers.append((name, p.m, a))

    if not stirrers:
        return None

    def delta_af(mass_solar, a):
        h_M = (mass_solar / (3.0 * Mstar)) ** (1.0 / 3.0)
        return 8.0 * np.sqrt(3.0) * h_M * a

    widths = [delta_af(m, a) for _, m, a in stirrers]
    total_width = float(np.sum(widths))
    n_stirrers = len(stirrers)

    return {
        "amin": amin,
        "amax": amax,
        "delta_a": delta_a,
        "n_stirrers": n_stirrers,
        "has_giant_planet": any(name == "GP" for name, _, _ in stirrers),
        "delta_af_mean": total_width / n_stirrers,
        "delta_af_sum": total_width,
        "ratio": total_width / delta_a,
        "covered": bool(total_width >= delta_a),
    }


def check_stirrer_disk_coverage(sim, config):
    """Run ``compute_stirrer_disk_coverage``; on failure WARN and, when stdin is
    a TTY, pause and ask whether to continue (aborting on anything but yes). In a
    non-interactive session it prints the warning and continues.
    """
    r = compute_stirrer_disk_coverage(sim, config)
    if r is None:
        return

    print("\nStirrer-coverage check (Krivov & Booth 2018: N x delta_af >= delta_a):")
    print(
        f"  Stirrers inside the belt [{r['amin']:g}, {r['amax']:g}]: "
        f"N = {r['n_stirrers']}"
        + ("  (incl. giant planet)" if r["has_giant_planet"] else "")
    )
    print(
        f"  delta_af = 8 sqrt(3) h_M a_M:  mean = {r['delta_af_mean']:.6e}, "
        f"sum over stirrers = {r['delta_af_sum']:.6e}"
    )
    print(f"  Belt width delta_a = {r['delta_a']:.6e}")
    print(f"  Coverage ratio (sum delta_af / delta_a) = {r['ratio']:.3f}")

    if r["covered"]:
        print("  OK: stirrer feeding zones span the belt.")
        return

    print(
        f"  WARNING: stirrer feeding zones do NOT span the belt "
        f"(sum delta_af = {r['delta_af_sum']:.4e} < delta_a = {r['delta_a']:.4e}). "
        "The Krivov & Booth (2018) self-stirring picture assumes the stirrers "
        "can dynamically reach across the whole disk width."
    )

    if not sys.stdin.isatty():
        print(
            "  Non-interactive session: continuing anyway (cannot prompt). "
            "Re-run interactively to be asked for confirmation."
        )
        return

    reply = input("  Continue the simulation anyway? [y/N] ").strip().lower()
    if reply not in ("y", "yes"):
        raise SystemExit(
            "Aborted before integration: N x delta_af >= delta_a is not "
            "satisfied (stirrers do not span the belt)."
        )
    print("  Continuing at user request.")


def run_simulation(config, config_path=None):
    terminal_buffer = start_capturing_stdout()

    maxtime = float(config["integration"]["maxtime"])
    time_step = (config["integration"]["time_step"])

    start_time = 0.0
    file_path = dump_path_for(config)
    dump_condition = config['simulation']["dump"]
    if dump_condition and os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            dump_data = json.load(file)
        start_time = dump_data["star"]['time']
    times = np.arange(start_time, maxtime+1, time_step)


    sim_name = config["simulation"]["name"]

    run_output_dir = run_output_dir_for(config)
    os.makedirs(run_output_dir, exist_ok=True)

    dump_path = dump_path_for(config)

    # Provenance: freeze the config, record git/software/UUID, dump pip freeze.
    capture_run_provenance(config, config_path, run_output_dir)

    output_file = os.path.join(run_output_dir, f"{sim_name}.bin")

    print(f"Saving SimulationArchive to: {output_file}")

    dump_condition = config['simulation']["dump"] 


    if not dump_condition:
        if os.path.exists(output_file):
            os.remove(output_file)
    else:
        file_path = dump_path
        if file_path.exists():
            with open(file_path, "r", encoding="utf-8") as file:
                dump_data = json.load(file)

            start_time = list(dump_data.items())[0][1]["time"]

            # Resume on the same output grid as a fresh run, rather than
            # recomputing it with np.arange(start, maxtime+step, step): that
            # accumulates floating-point error over many steps and can
            # overshoot maxtime by a full step.
            idx = int(np.argmin(np.abs(times - start_time)))
            times = times[idx:]
            print(f"Resuming from t={start_time:.6e} yr: {times=}")
        else:
            print("No existing dump_data.json found; starting fresh run.")





    sim = build_simulation(config)

    check_stirrer_disk_coverage(sim, config)

    E0 = sim.energy()

    print("\nBeginning the main integration")

    start_walltime = time.time()

    for i, int_time in enumerate(times):

        if dump_condition:
            get_particles(i, sim, dump_path)

        try:
            sim.integrate(int_time)

        except rebound.Escape as error:
            print(error)

            exit_max_distance = float(
                config["integration"]["exit_max_distance"]
            )

            escaped_indices = []

            for index in range(1, sim.N):  # skip the star
                p = sim.particles[index]
                r = np.sqrt(p.x**2 + p.y**2 + p.z**2)

                if r > exit_max_distance:
                    escaped_indices.append(index)

            for index in reversed(escaped_indices):
                print(f"Removing escaped particle at index {index}")
                sim.remove(index)

                print(f"Remaining particles: {sim.N}")

        # Keep only bound orbits: drop anything that has gone hyperbolic/
        # parabolic (e > 1) or picked up an invalid eccentricity (e < 0).
        unbound_indices = []

        for index in range(1, sim.N):  # skip the star
            p = sim.particles[index]

            if p.e > 1.0 or p.e < 0.0:
                unbound_indices.append(index)

        for index in reversed(unbound_indices):
            p = sim.particles[index]
            name = p.name

            if name.startswith("TP_"):
                role = "Test particle"
            elif name.startswith("MP_"):
                role = "Massive planetesimal"
            else:
                role = name

            print(
                f"{role} was removed at index {index} for unbound orbit "
                f"(e={p.e:.6f})"
            )
            sim.remove(index)

            print(f"Remaining particles: {sim.N}")

        sim.save_to_file(output_file)

        E1 = sim.energy()
        dE = abs((E1 - E0) / E0)
        Noutputs = int((maxtime - start_time)/time_step)
        
        outputs_done = i + 1
        outputs_remaining = Noutputs - outputs_done
        avg_time_per_output = (time.time() - start_walltime) / outputs_done
        eta_completion = avg_time_per_output * outputs_remaining

        print(
            f"Output {i+1}/{Noutputs}: "
            f"t={sim.t:.1f} yr, "
            f"dE/E0={dE:.2e}, "
            f"N={sim.N}"
        )
        print(
            f"  Estimated time remaining to complete simulation: "
            f"{format_time(eta_completion)}"
        )
        if outputs_remaining > 0:
            print(
                f"  Estimated time remaining to next output: "
                f"{format_time(avg_time_per_output)}"
            )

    total_runtime = time.time() - start_walltime

    print("\nSimulation complete.")
    print(f"Total runtime: {format_time(total_runtime)}")

    report_effective_stirring_C_e(sim, config)

    # Quick archive check
    initial_N = None
    try:
        sa = rebound.Simulationarchive(output_file)
        initial_N = sa[0].N
        print(f"Saved archive: {output_file}")
        print(f"Number of snapshots saved: {len(sa)}")
        print(f"Archive time range: {sa.tmin:.3e} yr to {sa.tmax:.3e} yr")
    except Exception as error:
        print(f"Could not verify archive: {error}")

    update_run_metadata(
        run_output_dir,
        finished=now_iso(),
        wall_runtime_seconds=round(total_runtime, 1),
        outcome="completed",
        initial_particle_count=initial_N,
        final_particle_count=sim.N,
    )

    plots_enabled = bool(config.get("plots", {}).get("enabled", False))

    if plots_enabled:
        generate_summary_figures(output_file, config, run_output_dir)

        report_path = os.path.join(run_output_dir, f"{sim_name}_report.md")
        generate_report(
            config,
            config_path,
            output_file,
            report_path,
            terminal_output=terminal_buffer.getvalue(),
        )

    n_summary = (
        f"{initial_N}->{sim.N}" if initial_N is not None else f"{sim.N}"
    )
    send_ntfy(
        config,
        f"{sim_name} finished",
        f"{sim_name} finished in {format_time(total_runtime)} "
        f"({n_summary} particles). Archive: {output_file}",
    )

    stop_capturing_stdout()


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage:")
        print("python src/run_simulation.py config/config.yaml")
        sys.exit(1)

    config_path = sys.argv[1]

    print(f"Reading configuration from: {config_path}")

    config = read_config(config_path)

    try:
        run_simulation(config, config_path=config_path)
    except Exception as error:
        try:
            update_run_metadata(
                run_output_dir_for(config),
                outcome="failed",
                finished=now_iso(),
                error=f"{type(error).__name__}: {error}",
            )
        except Exception:  # noqa: BLE001 - never mask the real error
            pass
        send_ntfy(
            config,
            f"{config['simulation']['name']} FAILED",
            f"{config['simulation']['name']} FAILED: "
            f"{type(error).__name__}: {error}",
        )
        raise