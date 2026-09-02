"""
plot_kirvov_calibration.py

Calibration plot: RMS eccentricity vs time (log-log) for the self-stirring
runs SS_100MP_100Myr_{10,30,50}xStir, overlaid with the Krivov & Booth (2018)
analytic self-stirring prediction.

Analytic model (Krivov & Booth 2018, MNRAS 479, 3300), two-population case
-- negligible-mass field planetesimals stirred by equal-mass stirrers on
near-circular orbits (their Eqs. 9 and 10):

    T^-1   = (1 / 2 pi) * C_e * Omega * (a / da) * (M / Mstar) * (Mdisc / Mstar)
    RMS(e) = (2 t / T)^(1/4)

with C_e ~= 40 (Ida & Makino 1993), Omega = sqrt(G Mstar / a^3) the mean
motion at the belt centre, a / da the belt radius over its full width, M the
individual stirrer mass and Mdisc the total mass in stirrers.

In these runs every one of the 100 massive planetesimals is a stirrer, so
M = Mdisc / 100 and the measured RMS(e) is that of the stirrer population
itself. Each run therefore gets its own analytic curve (they differ only by
the M * Mdisc product, i.e. RMS(e) ~ (M Mdisc)^(1/4)).

Writes: calibration/rmse_kirvov_calibration.png
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import rebound

# --- physical constants (units: yr, AU, Msun; G = 4 pi^2) --------------------
EARTH_MASS_TO_SOLAR_MASS = 3.0034896149156e-6
C_E = 40.0  # Ida & Makino (1993) numerical stirring factor

# --- belt / star geometry (common to all three runs) ------------------------
M_STAR = 1.0          # Msun
A_BELT = 100.0        # AU  (disk spans 95-105 AU)
DA_BELT = 10.0        # AU  (full radial width)

REPO_ROOT = Path(__file__).resolve().parent.parent
OUTPUTS = REPO_ROOT / "outputs"

# run name -> (label, colour, total disk mass in Earth masses) from each config.yaml
RUNS = {
    "SS_100MP_100Myr_6e-5Mearth": ("control (6e-5 M_earth)", "#7f7f7f", 6e-5),
    "SS_100MP_100Myr_10xStir": ("10x stirrers", "#1f77b4", 2.8),
    "SS_100MP_100Myr_30xStir": ("30x stirrers", "#d62728", 8.4),
    "SS_100MP_100Myr_50xStir": ("50x stirrers", "#2ca02c", 14.0),
}

# which runs go on which figure
FIGURES = {
    "rmse_kirvov_calibration.png": list(RUNS),
    "rmse_kirvov_calibration_stir_only.png": [
        "SS_100MP_100Myr_10xStir",
        "SS_100MP_100Myr_30xStir",
        "SS_100MP_100Myr_50xStir",
    ],
}
N_MP = 100
SNAPSHOT_STRIDE = 10  # subsample the 10001-snapshot archives for speed


def rms_e_vs_time(archive_path, stride=SNAPSHOT_STRIDE):
    """RMS eccentricity of the massive planetesimals at each sampled snapshot.

    Orbits are taken explicitly relative to the star (particle 0), matching
    src/plotting/summary_figures.py.
    """
    sa = rebound.Simulationarchive(str(archive_path))

    times = []
    rms_e = []
    for i in range(0, len(sa), stride):
        sim = sa[i]
        star = sim.particles[0]
        e_sq = [
            sim.particles[k].orbit(primary=star).e ** 2
            for k in range(1, sim.N)
        ]
        times.append(sim.t)
        rms_e.append(np.sqrt(np.mean(e_sq)))

    return np.array(times), np.array(rms_e)


def krivov_rms_e(times_yr, m_disc_earth, n_stirrers=N_MP):
    """Krivov & Booth (2018) Eqs. (9)-(10) RMS eccentricity vs time."""
    m_disc = m_disc_earth * EARTH_MASS_TO_SOLAR_MASS      # Msun
    m_indiv = m_disc / n_stirrers                          # Msun, per stirrer

    omega = 2.0 * np.pi * np.sqrt(M_STAR / A_BELT ** 3)    # yr^-1 (G = 4 pi^2)

    t_inv = (
        (1.0 / (2.0 * np.pi))
        * C_E
        * omega
        * (A_BELT / DA_BELT)
        * (m_indiv / M_STAR)
        * (m_disc / M_STAR)
    )  # yr^-1

    return (2.0 * times_yr * t_inv) ** 0.25


def make_plot(run_names, save_path):
    """Draw the calibration figure for the given subset of runs."""
    fig, ax = plt.subplots(figsize=(8, 6))

    last_times = None
    for run_name in run_names:
        label, color, m_disc_earth = RUNS[run_name]
        archive = OUTPUTS / run_name / f"{run_name}.bin"
        times, rms_e = rms_e_vs_time(archive)

        # drop t = 0 for the log axis
        mask = times > 0
        times, rms_e = times[mask], rms_e[mask]
        last_times = times

        ax.plot(times, rms_e, color=color, lw=1.5, label=f"{label} (N-body)")
        ax.plot(
            times,
            krivov_rms_e(times, m_disc_earth),
            color=color,
            lw=1.8,
            ls="--",
            label=f"{label} (Krivov & Booth 2018)",
        )

    # t^(1/4) slope guide
    t_guide = np.array([last_times.min(), last_times.max()])
    e_guide = 0.02 * (t_guide / t_guide.min()) ** 0.25
    ax.plot(t_guide, e_guide, color="0.5", lw=1.0, ls=":", label=r"$\propto t^{1/4}$")

    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel("Time (yr)")
    ax.set_ylabel("RMS eccentricity")
    ax.set_title(
        "Self-stirring calibration: N-body vs Krivov & Booth (2018)\n"
        "100 massive planetesimals, 95-105 AU, 1 $M_\\odot$ star"
    )
    ax.grid(alpha=0.3, which="both")
    ax.legend(fontsize=8, ncol=2)

    fig.tight_layout()
    fig.savefig(save_path, dpi=200, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved: {save_path}")


def main():
    out_dir = Path(__file__).resolve().parent
    for filename, run_names in FIGURES.items():
        make_plot(run_names, out_dir / filename)


if __name__ == "__main__":
    main()
