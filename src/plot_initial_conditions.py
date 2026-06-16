# %%
import rebound
import numpy as np
import matplotlib.pyplot as plt
import os

from config_utils import read_config


def get_particle_hash(p):
    return str(p.hash)


def plot_initial_conditions(config_file="config.yaml", output_plot=None, config=None):
    if config is None:
        config = read_config(config_file)
    archive_name = config["simulation"]["output_file"]
    simulation_name = config["simulation"]["name"]

    npl = int(config["dwarf_planets"]["N"])
    Npart = int(config["test_particles"]["N"])

    distribution = config["test_particles"]["distribution"]

    mass_fraction = config["dwarf_planets"]["mass_fraction_of_giant_planet"]

    print(f"Loading archive: {archive_name}")
    print("npl =", npl)
    print("Npart =", Npart)

    # Load simulation archive
    sa = rebound.SimulationArchive(archive_name)

    # First snapshot only
    sim = sa[0]

    # ------------------------------------------------------
    # Create arrays
    # ------------------------------------------------------

    xdps = np.zeros(npl)
    ydps = np.zeros(npl)
    zdps = np.zeros(npl)

    adps = np.zeros(npl)
    edps = np.zeros(npl)
    idps = np.zeros(npl)
    mdps = np.zeros(npl)

    xpart = np.zeros(Npart)
    ypart = np.zeros(Npart)
    zpart = np.zeros(Npart)

    apart = np.zeros(Npart)
    epart = np.zeros(Npart)
    ipart = np.zeros(Npart)

    # ------------------------------------------------------
    # Fill dwarf planet arrays
    # ------------------------------------------------------

    for i in range(npl):
        particle_index = i + 2
        p = sim.particles[particle_index]

        xdps[i] = p.x
        ydps[i] = p.y
        zdps[i] = p.z

        adps[i] = p.a
        edps[i] = p.e
        idps[i] = np.rad2deg(p.inc)

        mdps[i] = p.m

    # ------------------------------------------------------
    # Fill test particle arrays
    # ------------------------------------------------------

    for i in range(Npart):
        particle_index = i + 2 + npl
        p = sim.particles[particle_index]

        xpart[i] = p.x
        ypart[i] = p.y
        zpart[i] = p.z

        apart[i] = p.a
        epart[i] = p.e
        ipart[i] = np.rad2deg(p.inc)

    a_mean = np.mean(apart)
    a_sig = np.std(apart)

    print(f"a_mean = {a_mean:.3f} au")
    print(f"a_sig  = {a_sig:.3f} au")

    # ------------------------------------------------------
    # Giant planet
    # ------------------------------------------------------

    gp = sim.particles[1]

    # ------------------------------------------------------
    # Plot initial conditions
    # ------------------------------------------------------

    fig, ((ax1, ax2), (ax3, ax4), (ax5, ax6)) = plt.subplots(
        3, 2, figsize=(18, 14)
    )

    fig.suptitle(
    (
        f"{simulation_name}: Initial Conditions\n"
        f"N particles = {Npart}, "
        f"N DPs = {npl}, "
        f"Distribution = {distribution}, "
        f"DP Mass Fraction = {mass_fraction:.1e}\n"
        f"$a_{{mean}}$ = {a_mean:.2f} au, "
        f"$\\sigma_a$ = {a_sig:.2f} au"
    ),
    fontsize=16,
)

    # X-Y position
    ax1.scatter(xdps, ydps, label="DPs")
    ax1.scatter(xpart, ypart, label="Particles", alpha=0.5)
    ax1.scatter(gp.x, gp.y, label="GP", color="black")

    ax1.legend(loc="best")
    ax1.set_ylabel("Y [au]")
    ax1.set_xlabel("X [au]")
    ax1.set_title("Initial X-Y Position")

    # Z-X position
    ax2.scatter(zdps, xdps, label="DPs")
    ax2.scatter(zpart, xpart, label="Particles", alpha=0.5)
    ax2.scatter(gp.z, gp.x, label="GP", color="black")

    ax2.legend(loc="best")
    ax2.set_ylabel("X [au]")
    ax2.set_xlabel("Z [au]")
    ax2.set_title("Initial Z-X Position")

    # a-e
    ax3.scatter(adps, edps, label="DPs")
    ax3.scatter(apart, epart, label="Particles", alpha=0.5)
    ax3.scatter(gp.a, gp.e, label="GP", color="black")

    ax3.axvline(a_mean, linestyle="--")
    ax3.axvline(a_mean + a_sig, linestyle=":")
    ax3.axvline(a_mean - a_sig, linestyle=":")

    ax3.legend(loc="best")
    ax3.set_ylabel("$e$")
    ax3.set_xlabel("$a$ [au]")
    ax3.set_title("Initial Semimajor Axis vs. Eccentricity")

    # a-i
    ax4.scatter(adps, idps, label="DPs")
    ax4.scatter(apart, ipart, label="Particles", alpha=0.5)
    ax4.scatter(gp.a, np.rad2deg(gp.inc), label="GP", color="black")

    ax4.axvline(a_mean, linestyle="--")
    ax4.axvline(a_mean + a_sig, linestyle=":")
    ax4.axvline(a_mean - a_sig, linestyle=":")

    ax4.legend(loc="best")
    ax4.set_ylabel("$i$ [$^\\circ$]")
    ax4.set_xlabel("$a$ [au]")
    ax4.set_title("Initial Semimajor Axis vs. Inclination")

    # a-mass
    ax5.scatter(adps, mdps, label="DPs")

    ax5.axvline(a_mean, linestyle="--")
    ax5.axvline(a_mean + a_sig, linestyle=":")
    ax5.axvline(a_mean - a_sig, linestyle=":")

    ax5.legend(loc="best")
    ax5.set_ylabel("Mass [$M_\\odot$]")
    ax5.set_xlabel("$a$ [au]")
    ax5.set_title("Initial DP Mass vs. Semimajor Axis")

    # a histogram
    ax6.hist(adps, bins=100, density=True, align="mid", label="DPs")
    ax6.hist(apart, bins=100, density=True, align="mid", label="Particles", alpha=0.5)

    ax6.axvline(a_mean, linestyle="--", label="$a_{mean}$")
    ax6.axvline(a_mean + a_sig, linestyle=":", label="$a_{mean} \\pm \\sigma_a$")
    ax6.axvline(a_mean - a_sig, linestyle=":")

    ax6.legend(loc="best")
    ax6.set_ylabel("Density")
    ax6.set_xlabel("$a$ [au]")
    ax6.set_title("Initial Semimajor Axis Histogram")

    plt.tight_layout(rect=[0, 0, 1, 0.94])

    if output_plot is None:
        output_plot = f"outputs/{simulation_name}_InitialConditions.png"

    os.makedirs(os.path.dirname(output_plot), exist_ok=True)

    dpi = int(config.get("plots", {}).get("dpi", 200))

    plt.savefig(output_plot, dpi=dpi)
    plt.show()

    print(f"Saved plot to: {output_plot}")

    return output_plot


if __name__ == "__main__":
    plot_initial_conditions("config.yaml")

# %%



