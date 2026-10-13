"""
plot_all_rms_e_overlay.py

Overlay the massive-planetesimal RMS eccentricity vs time (log-log) of every
finished SS_800MP production run (smoke tests excluded): the 500 kyr runs
(without / with 1000 test particles) and the 10 Myr 1 and 10 M_earth runs.

Each massive-planetesimal curve uses the Rayleigh sigma outlier cut (the same
bodies the C_e diagnostic excludes; see src/utilities/rayleigh_cut.py). Runs
with test particles also get a dotted curve for the test-particle RMS e
(all surviving test particles, no cut).

A second figure adds the 100 Myr SS_100MP 10x / 30x / 50x Stir runs to the same
curves.

Every curve is fitted as e = A t^p (degree-1 log-log polyfit; thin black line = fit for
t >= 1e5 yr, legend gives p for t >= 1e5 yr and for the whole run) and a dashed reference line of slope 1/4 is drawn.

A dash-dot line marks the onset of fragmentation at RMS e = 0.01; each curve gets a dot where
it first reaches it and the time is given in the legend and the fit table.

Writes: calibration/rms_e_all_runs_overlay.png
        calibration/rms_e_all_runs_plus_stir_overlay.png
        calibration/rms_e_all_runs_fits.md
"""

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
for _sub in ("plotting", "utilities", "config_io"):
    sys.path.insert(0, str(REPO_ROOT / "src" / _sub))

import matplotlib  # noqa: E402

matplotlib.use("Agg")

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

from config_utils import read_config  # noqa: E402
from rayleigh_cut import cut_nsigma_from_config  # noqa: E402
from summary_figures import (  # noqa: E402
    build_snapshot_table, rms_by_snapshot, rms_eccentricity_rayleigh_cut)

OUTPUTS = REPO_ROOT / "outputs"
OUT_DIR = Path(__file__).resolve().parent

# run -> (label, colour, linestyle)
RUNS = {
    "SS_800MP_500kyr_1Mearth_slopeq3.5": ("500 kyr, 1 M$_\\oplus$, q=3.5 (no TP), MPs", "#2a78d6", "-"),
    "SS_800MP_1000TP_500kyr_1Mearth_slopeq3.5": ("500 kyr, 1 M$_\\oplus$, q=3.5 (1000 TP), MPs", "#2a78d6", "--"),
    "SS_800MP_10Myr_1Mearth_slopeq3.5": ("10 Myr, 1 M$_\\oplus$, q=3.5, MPs", "#eb6834", "-"),
    "SS_800MP_10Myr_1Mearth_slopeq4.5": ("10 Myr, 1 M$_\\oplus$, q=4.5, MPs", "#2f9e6b", "-"),
    "SS_800MP_10Myr_1Mearth_uniform": ("10 Myr, 1 M$_\\oplus$, uniform, MPs", "#8a5fd1", "-"),
    "SS_800MP_10Myr_10Mearth_uniform": ("10 Myr, 10 M$_\\oplus$, uniform, MPs", "#8a5fd1", "--"),
}

# extra runs for the second figure (100 Myr, 100 massive planetesimals)
STIR_RUNS = {
    "SS_100MP_100Myr_10xStir": ("100 Myr, 10x Stir, MPs", "#c9302c", "-"),
    "SS_100MP_100Myr_30xStir": ("100 Myr, 30x Stir, MPs", "#7a4a2b", "-"),
    "SS_100MP_100Myr_50xStir": ("100 Myr, 50x Stir, MPs", "#4a4a4a", "-"),
}


FIT_T_MIN = 1e5  # yr; the plotted fit line uses only t >= this
E_ONSET = 0.01  # RMS e at which fragmentation is taken to begin


def onset_time(t, y, threshold=E_ONSET):
    """First time the curve reaches ``threshold`` (log-log interpolation), or None."""
    above = np.nonzero(y >= threshold)[0]
    if len(above) == 0:
        return None
    i = above[0]
    if i == 0:
        return float(t[0])
    frac = (np.log10(threshold) - np.log10(y[i - 1])) / (np.log10(y[i]) - np.log10(y[i - 1]))
    return float(10 ** (np.log10(t[i - 1]) + frac * (np.log10(t[i]) - np.log10(t[i - 1]))))


def fmt_onset(t_on):
    return "not reached" if t_on is None else f"{t_on:.2e} yr"


def plot_with_fit(ax, t, y, label, colour, linestyle, linewidth, fits):
    """Plot a curve and its log-log degree-1 polyfit e = A t^p.

    Two fits are made: over the whole run and over t >= FIT_T_MIN. The thin
    black line drawn on top is the t >= FIT_T_MIN fit; both slopes are in the
    legend entry and recorded in ``fits``.
    """
    p_all, log_a_all = np.polyfit(np.log10(t), np.log10(y), 1)
    late = t >= FIT_T_MIN
    p_late, log_a_late = np.polyfit(np.log10(t[late]), np.log10(y[late]), 1)
    t_on = onset_time(t, y)
    fits.append((label, p_late, 10 ** log_a_late, p_all, 10 ** log_a_all, t_on))
    ax.plot(t, y, color=colour, linestyle=linestyle, linewidth=linewidth,
            label=f"{label}  (p = {p_late:.2f} for t$\\geq$10$^5$ yr; {p_all:.2f} all; "
                  f"t$_{{onset}}$ = {fmt_onset(t_on)})")
    if t_on is not None:
        ax.plot([t_on], [E_ONSET], marker="o", markersize=5, color=colour,
                markeredgecolor="black", markeredgewidth=0.6, zorder=6)
    ax.plot(t[late], 10 ** (p_late * np.log10(t[late]) + log_a_late), color="black",
            linestyle="-", linewidth=0.7, alpha=0.8, zorder=5)


def make_figure(runs, out_name, title):
    fig, ax = plt.subplots(figsize=(9, 5.5))
    fits = []

    for run, (label, colour, linestyle) in runs.items():
        run_dir = OUTPUTS / run
        config = read_config(str(run_dir / "config.yaml"))
        nsigma = cut_nsigma_from_config(config)
        df = build_snapshot_table(run_dir / f"{run}.bin")
        t, _, rms_cut, _ = rms_eccentricity_rayleigh_cut(
            df, float(config["disk"]["emax"]), nsigma)
        keep = t > 0  # log axis
        plot_with_fit(ax, t[keep], rms_cut[keep], label, colour, linestyle, 1.8, fits)
        if (df["role"] == "test_particle").any():
            rms_tp = rms_by_snapshot(df, "test_particle", "e")
            t_all = df.groupby("snapshot")["time_yr"].first().sort_index().to_numpy()
            keep_tp = (t_all > 0) & ~np.isnan(rms_tp)
            plot_with_fit(ax, t_all[keep_tp], rms_tp[keep_tp],
                          label.replace(", MPs", ", test particles"), "#d4a017", ":", 2.2, fits)
            print(f"{run}: final TP RMS e = {rms_tp[keep_tp][-1]:.4e}")
        print(f"{run}: final RMS e = {rms_cut[-1]:.4e}")

    # reference slope 1/4 (Krivov & Booth 2018 viscous stirring, RMS e ~ t^(1/4))
    t_ref = np.array([1e4, ax.get_xlim()[1] if False else 1e7])
    ax.plot(t_ref, 1.2e-3 * (t_ref / 1e4) ** 0.25, color="black", linestyle="--",
            linewidth=1.5, label="Reference slope 1/4 (RMS e $\\propto$ t$^{1/4}$)")
    ax.text(t_ref[1], 1.2e-3 * (t_ref[1] / 1e4) ** 0.25, " slope 1/4", va="center",
            fontsize=8)
    ax.axhline(E_ONSET, color="crimson", linestyle="-.", linewidth=1.2, zorder=1,
               label=f"Onset of fragmentation (RMS e = {E_ONSET}); dots = time reached")
    ax.plot([], [], color="black", linewidth=0.7, label="Log-log polyfit of each curve, t $\\geq$ 10$^5$ yr")

    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel("Time (yr)")
    ax.set_ylabel("RMS eccentricity (MPs = massive planetesimals)")
    ax.set_title(title)
    ax.grid(alpha=0.25, linewidth=0.6, which="both")
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    ax.legend(loc="upper left", bbox_to_anchor=(1.02, 1), fontsize=8, frameon=False)

    out_path = OUT_DIR / out_name
    fig.savefig(out_path, dpi=200, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved: {out_path.relative_to(REPO_ROOT)}")
    for label, p_late, a_late, p_all, a_all, t_on in fits:
        print(f"  fit {label}: t>=1e5 p = {p_late:.3f}, A = {a_late:.3e}; "
              f"all p = {p_all:.3f}, A = {a_all:.3e}; onset (e={E_ONSET}) = {fmt_onset(t_on)}")
    return fits


def write_fit_table(fits):
    lines = ["# RMS e power-law fits, e = A t^p (log-log degree-1 polyfit)", "",
             "Written by plot_all_rms_e_overlay.py.", "",
             "| Run | p (t >= 1e5 yr) | A (t >= 1e5 yr) | p (all t) | A (all t) | t at RMS e = 0.01 (yr) |",
             "|---|---|---|---|---|---|"]
    for label, p_late, a_late, p_all, a_all, t_on in fits:
        t_txt = "not reached" if t_on is None else f"{t_on:.3e}"
        lines.append(f"| {label} | {p_late:.3f} | {a_late:.3e} | {p_all:.3f} | {a_all:.3e} | {t_txt} |")
    (OUT_DIR / "rms_e_all_runs_fits.md").write_text("\n".join(lines) + "\n")


def main():
    make_figure(RUNS, "rms_e_all_runs_overlay.png",
                "RMS Eccentricity vs Time: all finished SS_800MP runs")
    all_fits = make_figure({**RUNS, **STIR_RUNS}, "rms_e_all_runs_plus_stir_overlay.png",
                           "RMS Eccentricity vs Time: SS_800MP runs + 10x / 30x / 50x Stir")
    write_fit_table(all_fits)


if __name__ == "__main__":
    main()
