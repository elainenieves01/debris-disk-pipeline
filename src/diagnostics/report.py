from pathlib import Path

import numpy as np
import rebound

from provenance import load_run_metadata

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


def _format_mass_assignment_config(config):
    mp_config = config["massive_planetesimals"]

    if mp_config.get("total_disk_mass_earth") is not None:
        return (
            f"total_disk_mass_earth = "
            f"{float(mp_config['total_disk_mass_earth']):.6e} "
            f"Earth masses (total disk mass, split evenly across N)"
        )

    if mp_config.get("total_mass_earth") is not None:
        return (
            f"total_mass_earth = {float(mp_config['total_mass_earth']):.6e} "
            f"Earth masses (deprecated alias of total_disk_mass_earth; "
            f"split evenly across N)"
        )

    if mp_config.get("individual_MP_mass_plutos") is not None:
        return (
            f"individual_MP_mass_plutos = "
            f"{float(mp_config['individual_MP_mass_plutos']):.6e} "
            f"Pluto masses per planetesimal (total disk mass = value * N)"
        )

    if mp_config.get("mass_fraction_of_giant_planet") is not None:
        return (
            f"mass_fraction_of_giant_planet = "
            f"{float(mp_config['mass_fraction_of_giant_planet']):.6e}"
        )

    return "unspecified"


def _provenance_lines(metadata):
    """Markdown lines for the Provenance section, or [] if no metadata."""
    if not metadata:
        return []

    lines = ["## Provenance", ""]
    lines.append(f"- Run UUID: `{metadata.get('run_uuid', 'unknown')}`")

    created = metadata.get("created")
    finished = metadata.get("finished")
    if created:
        lines.append(f"- Created: {created}")
    if finished:
        lines.append(f"- Finished: {finished}")
    if metadata.get("wall_runtime_seconds") is not None:
        lines.append(f"- Wall runtime: {metadata['wall_runtime_seconds']} s")
    if metadata.get("outcome"):
        lines.append(f"- Outcome: {metadata['outcome']}")
    if metadata.get("error"):
        lines.append(f"- Error: {metadata['error']}")
    if metadata.get("command"):
        lines.append(f"- Command: `{metadata['command']}`")

    git = metadata.get("git") or {}
    if git.get("available"):
        flag = " **(DIRTY — uncommitted tracked changes)**" if git.get("dirty") else ""
        lines.append(
            f"- Git commit: `{git.get('commit', '?')}` "
            f"(branch `{git.get('branch', '?')}`){flag}"
        )
        for name in git.get("dirty_files", []) or []:
            lines.append(f"    - modified: `{name}`")
    else:
        lines.append("- Git: not available (run from a non-repo checkout)")

    software = metadata.get("software") or {}
    if software:
        rendered = ", ".join(f"{k} {v}" for k, v in software.items())
        lines.append(f"- Software: {rendered}")

    if metadata.get("resumes"):
        lines.append(f"- Resumed {len(metadata['resumes'])} time(s) after the first run")

    lines.append("- Frozen config: `config.yaml` (this directory)")
    lines.append("- Full environment: `environment.txt` (this directory)")
    lines.append("")
    return lines


def generate_report(config, config_path, archive_path, output_path, terminal_output=None):
    """
    Write a Markdown report summarizing the YAML config used for a run,
    including whether the massive planetesimal mass is uniform and, if so,
    what it is.

    `terminal_output`, if given, is the run's captured console output,
    appended as its own section.
    """
    sim_cfg = config["simulation"]
    units_cfg = config["units"]
    integration_cfg = config["integration"]
    star_cfg = config["star"]
    gp_cfg = config.get("giant_planet")
    disk_cfg = config["disk"]
    mp_cfg = config["massive_planetesimals"]
    tp_cfg = config["test_particles"]

    sa = rebound.Simulationarchive(str(archive_path))
    initial_sim = sa[0]
    final_sim = sa[-1]

    n_mp, mp_mass_msun, mp_uniform, mp_masses = _massive_planetesimal_mass_summary(
        initial_sim
    )

    run_metadata = load_run_metadata(Path(output_path).parent)

    lines = []
    lines.append(f"# {sim_cfg['name']} — Simulation Report")
    lines.append("")
    lines.append(f"Config file: `{config_path}`")
    lines.append(f"Archive file: `{archive_path}`")
    lines.append("")
    lines.extend(_provenance_lines(run_metadata))

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
    if gp_cfg is None:
        lines.append("- None (disk integrated around the star alone)")
    else:
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
    lines.append(f"- Mass-assignment method (config): {_format_mass_assignment_config(config)}")

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

    if terminal_output:
        lines.append("## Terminal Output")
        lines.append("")
        lines.append("```")
        lines.append(terminal_output.rstrip("\n"))
        lines.append("```")
        lines.append("")

    with open(output_path, "w", encoding="utf-8") as file:
        file.write("\n".join(lines))

    print(f"Saved report to: {output_path}")

    return output_path
