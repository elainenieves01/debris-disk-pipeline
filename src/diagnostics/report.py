import numpy as np
import rebound

EARTH_MASS_TO_SOLAR_MASS = 3.0034896149156e-6


def _massive_planetesimal_mass_summary(sim):
    """
    Read each massive planetesimal's mass off the simulation and report
    whether it's uniform across all of them.

    Returns (count, mass_msun_or_None, uniform_bool, masses_array).
    mass_msun is the single shared mass if uniform, otherwise None.
    """
    masses = np.array(
        [p.m for p in sim.particles[1 : sim.N] if (p.name or "").startswith("MP_")]
    )

    if masses.size == 0:
        return 0, None, True, masses

    uniform = bool(np.allclose(masses, masses[0]))
    mass_msun = float(masses[0]) if uniform else None

    return masses.size, mass_msun, uniform, masses


def _format_mass_fraction_config(config):
    mp_config = config["massive_planetesimals"]

    if "total_mass_earth" in mp_config:
        return (
            f"total_mass_earth = {float(mp_config['total_mass_earth']):.6f} "
            f"Earth masses (split evenly across N)"
        )

    if "mass_fraction_of_giant_planet" in mp_config:
        return (
            f"mass_fraction_of_giant_planet = "
            f"{float(mp_config['mass_fraction_of_giant_planet']):.6e}"
        )

    return "unspecified"


def generate_report(config, config_path, archive_path, output_path):
    """
    Write a Markdown report summarizing the YAML config used for a run,
    including whether the massive planetesimal mass is uniform and, if so,
    what it is.
    """
    sim_cfg = config["simulation"]
    units_cfg = config["units"]
    integration_cfg = config["integration"]
    star_cfg = config["star"]
    gp_cfg = config["giant_planet"]
    disk_cfg = config["disk"]
    mp_cfg = config["massive_planetesimals"]
    tp_cfg = config["test_particles"]

    sa = rebound.Simulationarchive(str(archive_path))
    initial_sim = sa[0]
    final_sim = sa[-1]

    n_mp, mp_mass_msun, mp_uniform, mp_masses = _massive_planetesimal_mass_summary(
        initial_sim
    )

    lines = []
    lines.append(f"# {sim_cfg['name']} — Simulation Report")
    lines.append("")
    lines.append(f"Config file: `{config_path}`")
    lines.append(f"Archive file: `{archive_path}`")
    lines.append("")

    lines.append("## Simulation")
    lines.append(f"- Name: {sim_cfg['name']}")
    lines.append(f"- Output directory: {sim_cfg.get('output_dir', 'outputs')}")
    lines.append(f"- Dump/checkpoint enabled: {bool(sim_cfg.get('dump', False))}")
    lines.append("")

    lines.append("## Units")
    lines.append(
        f"- time = {units_cfg['time']}, length = {units_cfg['length']}, "
        f"mass = {units_cfg['mass']}"
    )
    lines.append("")

    lines.append("## Integration")
    lines.append(f"- Integrator: {integration_cfg['integrator']}")
    lines.append(f"- maxtime: {integration_cfg['maxtime']}")
    lines.append(f"- time_step: {integration_cfg['time_step']}")
    lines.append(
        "- timestep_fraction_of_planet_period: "
        f"{integration_cfg['timestep_fraction_of_planet_period']}"
    )
    lines.append(f"- exit_max_distance: {integration_cfg['exit_max_distance']} au")
    lines.append("")

    lines.append("## Star")
    lines.append(f"- Mass: {star_cfg['mass']} Msun")
    lines.append("")

    lines.append("## Giant Planet")
    lines.append(f"- Mass: {gp_cfg['mass_jupiter']} Mjup")
    lines.append(f"- a: {gp_cfg['a']} au, e: {gp_cfg['e']}, inc: {gp_cfg['inc_deg']} deg")
    lines.append(f"- omega: {gp_cfg['omega_deg']} deg, Omega random: {gp_cfg['Omega_random']}")
    lines.append(
        f"- t_peri_jd: {gp_cfg['t_peri_jd']}, orbital_period_days: "
        f"{gp_cfg['orbital_period_days']}, epoch_jd: {gp_cfg['epoch_jd']}"
    )
    lines.append("")

    lines.append("## Disk")
    lines.append(f"- a: [{disk_cfg['amin']}, {disk_cfg['amax']}] au")
    lines.append(f"- e: [{disk_cfg['emin']}, {disk_cfg['emax']}]")
    lines.append(f"- inc: [{disk_cfg['imin_deg']}, {disk_cfg['imax_deg']}] deg")
    if disk_cfg.get("M_deg") is not None:
        lines.append(f"- Fixed mean anomaly: {disk_cfg['M_deg']} deg")
    lines.append("")

    lines.append("## Massive Planetesimals")
    lines.append(f"- N: {mp_cfg['N']}")
    lines.append(f"- Mass-assignment method (config): {_format_mass_fraction_config(config)}")

    if n_mp == 0:
        lines.append("- No massive planetesimals present in the initial snapshot.")
    elif mp_uniform:
        mp_mass_earth = mp_mass_msun / EARTH_MASS_TO_SOLAR_MASS
        lines.append(
            f"- Individual mass (uniform across all {n_mp}): "
            f"{mp_mass_msun:.6e} Msun ({mp_mass_earth:.6f} Earth masses)"
        )
    else:
        lines.append(
            f"- **Mass is NOT uniform** across the {n_mp} massive planetesimals: "
            f"min = {mp_masses.min():.6e} Msun, max = {mp_masses.max():.6e} Msun"
        )
    lines.append("")

    lines.append("## Test Particles")
    lines.append(f"- N: {tp_cfg['N']}")
    lines.append(f"- Distribution: {tp_cfg.get('distribution', 'unknown')}")
    lines.append("")

    lines.append("## Run Summary (from archive)")
    lines.append(f"- Initial particle count: {initial_sim.N}")
    lines.append(f"- Final particle count: {final_sim.N}")
    lines.append(
        f"- Particles lost (escaped / unbound / other removal): "
        f"{initial_sim.N - final_sim.N}"
    )
    lines.append(f"- Archive time range: {sa.tmin:.6e} to {sa.tmax:.6e}")
    lines.append(f"- Number of snapshots: {len(sa)}")
    lines.append("")

    with open(output_path, "w", encoding="utf-8") as file:
        file.write("\n".join(lines))

    print(f"Saved report to: {output_path}")

    return output_path
