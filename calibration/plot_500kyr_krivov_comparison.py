"""
plot_500kyr_krivov_comparison.py

Compare the massive-planetesimal RMS eccentricity of the two 500 kyr,
1 M_earth, q = 3.5 runs with the Krivov & Booth (2018) self-stirring
prediction (their Eqs. 9 and 10):

    T^-1   = (1 / 2 pi) * C_e * Omega * (a / da) * (M / Mstar) * (Mdisc / Mstar)
    RMS(e) = (2 t / T)^(1/4)

with C_e = 40 (Ida & Makino 1993), Omega = sqrt(G Mstar / a^3) at the belt
centre, a / da from the config's disk block and Mdisc the total mass of the
massive planetesimals. The runs have a mass spectrum, so the individual
stirrer mass M is bracketed by two curves: M = the largest and M = the
smallest massive-planetesimal mass (read from the first snapshot; both runs
have identical massive planetesimals, so the analytic curves are shared).

N-body RMS(e) is drawn for all massive planetesimals (dashed) and with the
Rayleigh outlier cut (solid; the bodies the C_e diagnostic excludes, see
src/utilities/rayleigh_cut.py). Log-log axes, so t^(1/4) is a straight line;
the t = 0 snapshot is left out.

With --sim-ce, C_e is instead each run's own effective value, the one in its
report (compute_effective_stirring_C_e on the final snapshot: M = largest MP,
Rayleigh-cut RMS(e)). Note the largest-mass curve then passes through the
run's final cut RMS(e) by construction -- it shows how well a single t^(1/4)
law with that C_e describes the whole history, not an independent prediction.

Writes (calibration/):
    rms_e_vs_krivov_500kyr_noTP.png     run without test particles
    rms_e_vs_krivov_500kyr_1000TP.png   run with 1000 test particles
    rms_e_vs_krivov_500kyr_overlay.png  both runs + the analytic curves
    (with --sim-ce: the same names ending in _simCe.png)

Usage:
    python calibration/plot_500kyr_krivov_comparison.py            # C_e = 40
    python calibration/plot_500kyr_krivov_comparison.py --sim-ce   # each run's C_e
"""

import argparse

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
for _sub in ("simulation", "plotting", "utilities", "config_io", "diagnostics",
             "mass_models"):
    sys.path.insert(0, str(REPO_ROOT / "src" / _sub))

import matplotlib  # noqa: E402

matplotlib.use("Agg")

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib.ticker import FixedLocator, FormatStrFormatter, NullFormatter  # noqa: E402
import rebound  # noqa: E402

from config_utils import read_config  # noqa: E402
from rayleigh_cut import cut_nsigma_from_config  # noqa: E402
from run_simulation import compute_effective_stirring_C_e  # noqa: E402
from summary_figures import build_snapshot_table, rms_eccentricity_rayleigh_cut  # noqa: E402

OUTPUTS = REPO_ROOT / "outputs"
OUT_DIR = Path(__file__).resolve().parent
C_E = 40.0  # Ida & Makino (1993); Krivov & Booth (2018) Eq. 9

# run -> (label, colour, output file); colours are categorical slots 1 and 2
# of the dataviz reference palette, matching plot_500kyr_rms_e_overlay.py
RUNS = {
    "SS_800MP_500kyr_1Mearth_slopeq3.5":
        ("No test particles", "#2a78d6", "rms_e_vs_krivov_500kyr_noTP.png"),
    "SS_800MP_1000TP_500kyr_1Mearth_slopeq3.5":
        ("1000 test particles", "#eb6834", "rms_e_vs_krivov_500kyr_1000TP.png"),
}
ANALYTIC_STYLE = {"max": dict(color="0.15", linestyle=":", linewidth=2),
                  "min": dict(color="0.15", linestyle="-.", linewidth=1.5)}


def krivov_rms_e(t, m_stirrer, m_disc, m_star, a_belt, da_belt, G, c_e=C_E):
    """Krivov & Booth (2018) Eqs. 9-10 RMS eccentricity at times t (yr)."""
    omega = np.sqrt(G * m_star / a_belt ** 3)
    t_inv = (c_e / (2.0 * np.pi)) * omega * (a_belt / da_belt) \
        * (m_stirrer / m_star) * (m_disc / m_star)
    return (2.0 * t * t_inv) ** 0.25


def load_run(run):
    """N-body curves and the analytic ingredients for one run."""
    run_dir = OUTPUTS / run
    config = read_config(str(run_dir / "config.yaml"))
    archive = run_dir / f"{run}.bin"
    nsigma = cut_nsigma_from_config(config)

    df = build_snapshot_table(archive)  # also runs the particle-name check
    t, rms_all, rms_cut, excluded = rms_eccentricity_rayleigh_cut(
        df, float(config["disk"]["emax"]), nsigma)

    sa = rebound.Simulationarchive(str(archive))
    first = sa[0]
    sim_c_e = compute_effective_stirring_C_e(sa[-1], config)["C_e"]
    masses = np.array([p.m for p in first.particles[1:]
                       if (p.name or "").startswith("MP_")])
    amin, amax = float(config["disk"]["amin"]), float(config["disk"]["amax"])
    geometry = dict(m_disc=masses.sum(), m_star=first.particles[0].m,
                    a_belt=0.5 * (amin + amax), da_belt=amax - amin, G=first.G)

    keep = t > 0
    return dict(t=t[keep], rms_all=rms_all[keep], rms_cut=rms_cut[keep],
                excluded=excluded, nsigma=nsigma, sim_c_e=sim_c_e,
                m_max=masses.max(), m_min=masses.min(), geometry=geometry)


def analytic_curves(data, t, c_e):
    g = data["geometry"]
    return {kind: krivov_rms_e(t, data[f"m_{kind}"], g["m_disc"], g["m_star"],
                               g["a_belt"], g["da_belt"], g["G"], c_e)
            for kind in ("max", "min")}


def draw_analytic(ax, data, t, c_e, colour=None, prefix=""):
    """Analytic band for M = largest / smallest MP. ``colour`` ties the curves to
    a run (when each run has its own C_e); default is neutral ink."""
    curves = analytic_curves(data, t, c_e)
    ax.fill_between(t, curves["min"], curves["max"], color=colour or "0.5",
                    alpha=0.07 if colour else 0.10, linewidth=0)
    source = "run's effective " if colour or prefix else ""
    for kind, name in (("max", "largest"), ("min", "smallest")):
        style = dict(ANALYTIC_STYLE[kind])
        if colour:
            style["color"] = colour
        ax.plot(t, curves[kind], **style,
                label=f"{prefix}Krivov & Booth Eqs. 9-10, {source}C$_e$ = {c_e:.4g}, "
                      f"M = {name} MP ({data[f'm_{kind}']:.2e} M$_\\odot$)")
    return curves


def draw_run(ax, data, label, colour):
    cut = f"Rayleigh {data['nsigma']:g}σ cut ({', '.join(data['excluded'])} removed)"
    ax.plot(data["t"], data["rms_all"], color=colour, linestyle="--", linewidth=1.5,
            alpha=0.8, label=f"{label}: N-body, all MPs")
    ax.plot(data["t"], data["rms_cut"], color=colour, linewidth=2,
            label=f"{label}: N-body, {cut}")


def finish(ax, title, path):
    ax.set_xscale("log")
    ax.set_yscale("log")
    # plain-number ticks at 1-2-5 steps inside the data range
    for axis, (lo, hi) in ((ax.xaxis, ax.get_xlim()), (ax.yaxis, ax.get_ylim())):
        decades = range(int(np.floor(np.log10(lo))), int(np.ceil(np.log10(hi))) + 1)
        ticks = [m * 10.0 ** d for d in decades for m in (1, 2, 5) if lo <= m * 10.0 ** d <= hi]
        axis.set_major_locator(FixedLocator(ticks))
        axis.set_major_formatter(FormatStrFormatter("%g"))
        axis.set_minor_formatter(NullFormatter())
    ax.set_xlabel("Time (yr)")
    ax.set_ylabel("RMS eccentricity (massive planetesimals)")
    ax.set_title(title)
    ax.grid(alpha=0.25, linewidth=0.6, which="both")
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.13), fontsize=7.5,
              frameon=False, ncol=1)
    ax.figure.savefig(path, dpi=200, bbox_inches="tight")
    plt.close(ax.figure)
    print(f"Saved: {path.relative_to(REPO_ROOT)}")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--sim-ce", action="store_true",
                        help="use each run's effective C_e (as in its report) instead of 40")
    args = parser.parse_args(argv)

    runs = {run: load_run(run) for run in RUNS}
    base = "RMS eccentricity vs Krivov & Booth (2018): 500 kyr, 1 M$_\\oplus$, q = 3.5"
    suffix = "_simCe" if args.sim_ce else ""
    if args.sim_ce:
        base += ", each run's own C$_e$"

    def out(filename):
        return OUT_DIR / filename.replace(".png", f"{suffix}.png")

    for run, (label, colour, filename) in RUNS.items():
        data = runs[run]
        c_e = data["sim_c_e"] if args.sim_ce else C_E
        fig, ax = plt.subplots(figsize=(8, 5))
        curves = draw_analytic(ax, data, data["t"], c_e,
                               prefix=f"{label}: " if args.sim_ce else "")
        draw_run(ax, data, label, colour)
        finish(ax, f"{base}\n{label}", out(filename))
        print(f"  {run} at t = {data['t'][-1]:.3g} yr (C_e = {c_e:.4g}): N-body all = "
              f"{data['rms_all'][-1]:.4f}, cut = {data['rms_cut'][-1]:.4f}; analytic "
              f"M_max = {curves['max'][-1]:.4f}, M_min = {curves['min'][-1]:.4f}")

    fig, ax = plt.subplots(figsize=(8, 5.5 if args.sim_ce else 5))
    if args.sim_ce:
        for run, (label, colour, _) in RUNS.items():
            data = runs[run]
            draw_analytic(ax, data, data["t"], data["sim_c_e"], colour=colour,
                          prefix=f"{label}: ")
    else:
        first = next(iter(runs.values()))
        draw_analytic(ax, first, first["t"], C_E)
    for run, (label, colour, _) in RUNS.items():
        draw_run(ax, runs[run], label, colour)
    finish(ax, f"{base}\nboth runs", out("rms_e_vs_krivov_500kyr_overlay.png"))


if __name__ == "__main__":
    main()
