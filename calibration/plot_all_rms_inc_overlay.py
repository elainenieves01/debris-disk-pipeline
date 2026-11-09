"""
plot_all_rms_inc_overlay.py

Inclination counterpart of plot_all_rms_e_overlay.py: overlay the
massive-planetesimal RMS inclination (degrees) vs time (log-log) of the same
runs, in the same three figures and with the same colours / line styles.

The bodies left out are the ones the eccentricity overlay leaves out (the
Rayleigh sigma outlier cut on e, see src/utilities/rayleigh_cut.py), so the e and
inclination curves describe the same set of bodies. Runs with test particles also
get a dotted curve for the test-particle RMS inclination (all surviving test
particles, no cut).

Every curve is fitted as i = A t^p (degree-1 log-log polyfit; thin black line = fit
for t >= 1e5 yr, legend gives p for t >= 1e5 yr and for the whole run).

A run restarted from a checkpoint repeats the snapshot at the restart time in its
archive; repeated times are dropped (first one kept) before plotting and fitting.

Writes: calibration/rms_inc_all_runs_overlay.png
        calibration/rms_inc_all_runs_plus_stir_overlay.png
        calibration/rms_inc_100Myr_800MP_slopes_overlay.png
        calibration/rms_inc_all_runs_fits.md
"""

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
for _sub in ("plotting", "utilities", "config_io"):
    sys.path.insert(0, str(REPO_ROOT / "src" / _sub))

import matplotlib  # noqa: E402

matplotlib.use("Agg")

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

from config_utils import read_config  # noqa: E402
from plot_all_rms_e_overlay import (  # noqa: E402
    FIT_T_MIN, OUTPUTS, OUT_DIR, RUNS, SLOPE_100MYR_RUNS, STIR_RUNS)
from rayleigh_cut import cut_nsigma_from_config  # noqa: E402
from summary_figures import (  # noqa: E402
    build_snapshot_table, get_times, rms_eccentricity_rayleigh_cut)

_CACHE = {}


def load_inclination(run):
    """(df, t, rms_inc_cut_deg): RMS inclination of the MPs the e overlay keeps."""
    if run not in _CACHE:
        run_dir = OUTPUTS / run
        config = read_config(str(run_dir / "config.yaml"))
        df = build_snapshot_table(run_dir / f"{run}.bin")
        _, _, _, excluded = rms_eccentricity_rayleigh_cut(
            df, float(config["disk"]["emax"]), cut_nsigma_from_config(config))
        mp = df[(df["role"] == "massive_planetesimal") & ~df["name"].isin(excluded)]
        snapshots = sorted(df["snapshot"].unique())
        rms = (mp.groupby("snapshot")["inc_deg"]
               .apply(lambda x: np.sqrt(np.mean(x ** 2))).reindex(snapshots).to_numpy())
        _CACHE[run] = (df, get_times(df), rms)
    return _CACHE[run]


def clean(t, y):
    """Positive-time, finite points with repeated times (checkpoint restarts) dropped."""
    t = np.asarray(t, dtype=float)
    y = np.asarray(y, dtype=float)
    ok = (t > 0) & np.isfinite(y) & (y > 0)
    t, y = t[ok], y[ok]
    _, first = np.unique(t, return_index=True)
    first.sort()
    return t[first], y[first]


def plot_with_fit(ax, t, y, label, colour, linestyle, linewidth, fits):
    p_all, log_a_all = np.polyfit(np.log10(t), np.log10(y), 1)
    late = t >= FIT_T_MIN
    p_late, log_a_late = np.polyfit(np.log10(t[late]), np.log10(y[late]), 1)
    fits.append((label, p_late, 10 ** log_a_late, p_all, 10 ** log_a_all))
    ax.plot(t, y, color=colour, linestyle=linestyle, linewidth=linewidth,
            label=f"{label}  (p = {p_late:.2f} for t$\\geq$10$^5$ yr; {p_all:.2f} all)")
    ax.plot(t[late], 10 ** (p_late * np.log10(t[late]) + log_a_late), color="black",
            linestyle="-", linewidth=0.7, alpha=0.8, zorder=5)


def make_figure(runs, out_name, title):
    fig, ax = plt.subplots(figsize=(9, 5.5))
    fits = []

    for run, (label, colour, linestyle) in runs.items():
        df, t, rms = load_inclination(run)
        tc, yc = clean(t, rms)
        plot_with_fit(ax, tc, yc, label, colour, linestyle, 1.8, fits)
        print(f"{run}: final RMS inc = {yc[-1]:.4e} deg at t = {tc[-1]:.3g} yr")
        if (df["role"] == "test_particle").any():
            tp = df[df["role"] == "test_particle"]
            snapshots = sorted(df["snapshot"].unique())
            rms_tp = (tp.groupby("snapshot")["inc_deg"]
                      .apply(lambda x: np.sqrt(np.mean(x ** 2))).reindex(snapshots).to_numpy())
            t_tp, y_tp = clean(get_times(df), rms_tp)
            plot_with_fit(ax, t_tp, y_tp, label.replace(", MPs", ", test particles"),
                          "#d4a017", ":", 2.2, fits)

    ax.plot([], [], color="black", linewidth=0.7,
            label="Log-log polyfit of each curve, t $\\geq$ 10$^5$ yr")
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel("Time (yr)")
    ax.set_ylabel("RMS inclination (deg) (MPs = massive planetesimals)")
    ax.set_title(title)
    ax.grid(alpha=0.25, linewidth=0.6, which="both")
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    ax.legend(loc="upper left", bbox_to_anchor=(1.02, 1), fontsize=8, frameon=False)

    out_path = OUT_DIR / out_name
    fig.savefig(out_path, dpi=200, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved: {out_path.relative_to(REPO_ROOT)}")
    return fits


def write_fit_table(fits):
    lines = ["# RMS inclination power-law fits, i = A t^p (log-log degree-1 polyfit, i in deg)", "",
             "Written by plot_all_rms_inc_overlay.py.", "",
             "| Run | p (t >= 1e5 yr) | A (t >= 1e5 yr) | p (all t) | A (all t) |",
             "|---|---|---|---|---|"]
    for label, p_late, a_late, p_all, a_all in fits:
        lines.append(f"| {label} | {p_late:.3f} | {a_late:.3e} | {p_all:.3f} | {a_all:.3e} |")
    (OUT_DIR / "rms_inc_all_runs_fits.md").write_text("\n".join(lines) + "\n")


def main():
    make_figure(RUNS, "rms_inc_all_runs_overlay.png",
                "RMS Inclination vs Time: all finished SS_800MP runs")
    all_fits = make_figure({**RUNS, **STIR_RUNS}, "rms_inc_all_runs_plus_stir_overlay.png",
                           "RMS Inclination vs Time: SS_800MP runs + 10x / 30x / 50x Stir")
    slope_fits = make_figure(SLOPE_100MYR_RUNS, "rms_inc_100Myr_800MP_slopes_overlay.png",
                             "RMS Inclination vs Time: 100 Myr SS_800MP q = 2 / 2.5 / 3 / 3.5 / 4 / 5")
    write_fit_table(all_fits + slope_fits)


if __name__ == "__main__":
    main()
