import os
import time
import random
import rebound
import sys
import urllib.request

_SRC_DIR = os.path.dirname(os.path.abspath(__file__))
for _subdir in ("config_io", "plotting", "diagnostics", "utilities"):
    sys.path.insert(0, os.path.join(_SRC_DIR, "..", _subdir))

from config_utils import read_config
from summary_figures import generate_summary_figures
from report import generate_report
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

        if len(present) != 1:
            raise ValueError(
                "massive_planetesimals must set exactly one of "
                f"{MASS_KEYS} (found: {present or 'none'})."
            )

        mode = present[0]

        if mode == "total_disk_mass_earth":
            total_disk_mass_earth = float(mp_cfg["total_disk_mass_earth"])
            m_mps = total_disk_mass_earth * EARTH_MASS_TO_SOLAR_MASS / npl
            mode_note = "total disk mass given; divided evenly among N"

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

        m_mps_pluto = m_mps / PLUTO_MASS_TO_SOLAR_MASS
        m_mps_earth = m_mps / EARTH_MASS_TO_SOLAR_MASS
        total_disk_earth = m_mps_earth * npl
        mp_diameter_km = sphere_diameter_from_mass(m_mps, density_g_per_cm3=1.0)

        print("\nMassive planetesimal mass setup:")
        print(f"  Mode: {mode}  ({mode_note})")
        print(f"  Number of planetesimals: {npl}")
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
                m=m_mps,
                a=rng.uniform(amin, amax),
                e=rng.uniform(emin, emax),
                inc=rng.uniform(imin, imax),
                omega=rng.uniform(0,2*np.pi),
                Omega=rng.uniform(0,2*np.pi),
                M = rng.uniform(0,2*np.pi),
                name= f"MP_{i}"
            )


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
        
        
        
    
    with open(dump_path, "w") as file:
        json.dump(dict_row, file, indent=4)



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