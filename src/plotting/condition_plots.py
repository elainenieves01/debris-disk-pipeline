import os

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import rebound


def _classify_particles(sim):
    """
    Split a simulation's particles into (giant planet, massive planetesimals,
    test particles) by name, skipping the star at index 0.

    Classifying by name rather than by fixed index range is required here
    because particles may have been removed mid-run (escape, unbound orbit),
    which shifts indices but leaves names untouched.
    """
    gp = None
    mps = []
    tps = []

    for index in range(1, sim.N):
        p = sim.particles[index]
        name = p.name or ""

        if name == "GP":
            gp = p
        elif name.startswith("MP_"):
            mps.append(p)
        elif name.startswith("TP_"):
            tps.append(p)

    return gp, mps, tps


def plot_conditions(sim, config, output_path, label):
    """
    Save a 3x2 figure (X-Y position, Z-X position, a-e, a-i, MP mass vs a,
    a histogram) summarizing one simulation snapshot.

    `label` (e.g. "Initial" or "Final") is used in titles and console output.
    """
    simulation_name = config["simulation"]["name"]
    distribution = config["test_particles"].get("distribution", "unknown")

    gp, mps, tps = _classify_particles(sim)

    a_mp = np.array([p.a for p in mps])
    e_mp = np.array([p.e for p in mps])
    i_mp = np.array([np.rad2deg(p.inc) for p in mps])
    m_mp = np.array([p.m for p in mps])
    x_mp = np.array([p.x for p in mps])
    y_mp = np.array([p.y for p in mps])
    z_mp = np.array([p.z for p in mps])

    a_tp = np.array([p.a for p in tps])
    e_tp = np.array([p.e for p in tps])
    i_tp = np.array([np.rad2deg(p.inc) for p in tps])
    x_tp = np.array([p.x for p in tps])
    y_tp = np.array([p.y for p in tps])
    z_tp = np.array([p.z for p in tps])

    a_mean = float(np.mean(a_tp)) if a_tp.size else float("nan")
    a_sig = float(np.std(a_tp)) if a_tp.size else float("nan")

    fig, ((ax1, ax2), (ax3, ax4), (ax5, ax6)) = plt.subplots(3, 2, figsize=(18, 14))

    fig.suptitle(
        (
            f"{simulation_name}: {label} Conditions\n"
            f"N test particles = {len(tps)}, "
            f"N massive planetesimals = {len(mps)}, "
            f"Distribution = {distribution}\n"
            f"$a_{{mean}}$ (TPs) = {a_mean:.2f} au, "
            f"$\\sigma_a$ = {a_sig:.2f} au"
        ),
        fontsize=16,
    )

    def _mark_a_stats(ax):
        ax.axvline(a_mean, linestyle="--")
        ax.axvline(a_mean + a_sig, linestyle=":")
        ax.axvline(a_mean - a_sig, linestyle=":")

    # X-Y position
    ax1.scatter(x_mp, y_mp, label="MPs")
    ax1.scatter(x_tp, y_tp, label="TPs", alpha=0.5)
    if gp is not None:
        ax1.scatter(gp.x, gp.y, label="GP", color="black")
    ax1.legend(loc="best")
    ax1.set_xlabel("X [au]")
    ax1.set_ylabel("Y [au]")
    ax1.set_title(f"{label} X-Y Position")

    # Z-X position
    ax2.scatter(z_mp, x_mp, label="MPs")
    ax2.scatter(z_tp, x_tp, label="TPs", alpha=0.5)
    if gp is not None:
        ax2.scatter(gp.z, gp.x, label="GP", color="black")
    ax2.legend(loc="best")
    ax2.set_xlabel("Z [au]")
    ax2.set_ylabel("X [au]")
    ax2.set_title(f"{label} Z-X Position")

    # a-e
    ax3.scatter(a_mp, e_mp, label="MPs")
    ax3.scatter(a_tp, e_tp, label="TPs", alpha=0.5)
    if gp is not None:
        ax3.scatter(gp.a, gp.e, label="GP", color="black")
    _mark_a_stats(ax3)
    ax3.legend(loc="best")
    ax3.set_xlabel("$a$ [au]")
    ax3.set_ylabel("$e$")
    ax3.set_title(f"{label} Semimajor Axis vs. Eccentricity")

    # a-i
    ax4.scatter(a_mp, i_mp, label="MPs")
    ax4.scatter(a_tp, i_tp, label="TPs", alpha=0.5)
    if gp is not None:
        ax4.scatter(gp.a, np.rad2deg(gp.inc), label="GP", color="black")
    _mark_a_stats(ax4)
    ax4.legend(loc="best")
    ax4.set_xlabel("$a$ [au]")
    ax4.set_ylabel("$i$ [$^\\circ$]")
    ax4.set_title(f"{label} Semimajor Axis vs. Inclination")

    # a-mass (massive planetesimals only)
    ax5.scatter(a_mp, m_mp, label="MPs")
    _mark_a_stats(ax5)
    ax5.legend(loc="best")
    ax5.set_xlabel("$a$ [au]")
    ax5.set_ylabel("Mass [$M_\\odot$]")
    ax5.set_title(f"{label} MP Mass vs. Semimajor Axis")

    # a histogram
    if a_mp.size:
        ax6.hist(a_mp, bins=100, density=True, align="mid", label="MPs")
    if a_tp.size:
        ax6.hist(a_tp, bins=100, density=True, align="mid", label="TPs", alpha=0.5)
    ax6.axvline(a_mean, linestyle="--", label="$a_{mean}$")
    ax6.axvline(a_mean + a_sig, linestyle=":", label="$a_{mean} \\pm \\sigma_a$")
    ax6.axvline(a_mean - a_sig, linestyle=":")
    ax6.legend(loc="best")
    ax6.set_xlabel("$a$ [au]")
    ax6.set_ylabel("Density")
    ax6.set_title(f"{label} Semimajor Axis Histogram")

    plt.tight_layout(rect=[0, 0, 1, 0.94])

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    dpi = int(config.get("plots", {}).get("dpi", 200))

    plt.savefig(output_path, dpi=dpi)
    plt.close(fig)

    print(f"Saved {label.lower()} conditions plot to: {output_path}")

    return output_path


def plot_initial_and_final_conditions(archive_path, config, run_output_dir):
    """Generate and save the initial- and final-conditions figures for a completed run."""
    simulation_name = config["simulation"]["name"]

    sa = rebound.Simulationarchive(str(archive_path))

    initial_path = os.path.join(
        run_output_dir, f"{simulation_name}_InitialConditions.png"
    )
    final_path = os.path.join(
        run_output_dir, f"{simulation_name}_FinalConditions.png"
    )

    plot_conditions(sa[0], config, initial_path, label="Initial")
    plot_conditions(sa[-1], config, final_path, label="Final")

    return initial_path, final_path
