"""
plot_lorentzian_rms_120au_cut.py

RMS e and RMS inclination vs time (log-log) for every completed 10 Myr Lorentzian
PSD2 run, leaving out every massive planetesimal that ever reaches 120 AU from the star.

"Reaches 120 AU" = heliocentric distance r >= R_CUT at any snapshot, or the body was
removed from the simulation during the run (an escape past exit_max_distance, which
is > R_CUT, even if no snapshot caught it beyond R_CUT). Like the Rayleigh cut, this
is a property of a body: a flagged body is left out at every snapshot, so the curves
always follow the same set of bodies. This cut REPLACES the Rayleigh sigma cut used
in the other overlays (no Rayleigh cut is applied here).

Same colours / line styles as plot_lorentzian_rms_e_overlay.py; the e figure keeps
the onset-of-fragmentation line (RMS e = 0.01) and the time each curve reaches it.

Writes: calibration/rms_e_lorentzian_overlay_120AU_cut.png
        calibration/rms_inc_lorentzian_overlay_120AU_cut.png
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import matplotlib  # noqa: E402

matplotlib.use("Agg")

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402
import yaml  # noqa: E402

import plot_all_rms_e_overlay as base  # noqa: E402
from plot_all_rms_inc_overlay import clean  # noqa: E402
from plot_lorentzian_rms_e_overlay import (  # noqa: E402
    PLANET_LABELS, PLANET_STYLES, PSD_COLOURS, completed_runs)
from summary_figures import build_snapshot_table, get_times  # noqa: E402

R_CUT = 120.0  # AU


def flagged_bodies(df):
    """Names of MPs that ever reach r >= R_CUT (heliocentric) or are removed mid-run."""
    star = df[df["role"] == "star"].set_index("snapshot")[["x_AU", "y_AU", "z_AU"]]
    mp = df[df["role"] == "massive_planetesimal"]
    s = star.loc[mp["snapshot"]].to_numpy()
    r = np.linalg.norm(mp[["x_AU", "y_AU", "z_AU"]].to_numpy() - s, axis=1)
    far = set(mp["name"].to_numpy()[r >= R_CUT])
    last = mp["snapshot"].max()
    removed = set(mp["name"]) - set(mp.loc[mp["snapshot"] == last, "name"])
    return far | removed, len(far), len(removed)


def rms_curve(mp, column, snapshots):
    return (mp.groupby("snapshot")[column].apply(lambda x: np.sqrt(np.mean(x ** 2)))
            .reindex(snapshots).to_numpy())


def style(ax, ylabel, title):
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel("Time (yr)")
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.grid(alpha=0.25, linewidth=0.6, which="both")
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    ax.legend(loc="upper left", bbox_to_anchor=(1.02, 1), fontsize=8, frameon=False)


def main():
    fig_e, ax_e = plt.subplots(figsize=(9, 5.5))
    fig_i, ax_i = plt.subplots(figsize=(9, 5.5))
    for run in completed_runs():
        psd, planet = run.split("_")[3:5]
        psd = psd[-1]
        cfg = yaml.safe_load((base.OUTPUTS / run / "config.yaml").read_text())
        q = cfg["massive_planetesimals"]["distribution"]["slope"]
        df = build_snapshot_table(base.OUTPUTS / run / f"{run}.bin")
        flagged, n_far, n_removed = flagged_bodies(df)
        n_mp = df.loc[(df["role"] == "massive_planetesimal") & (df["snapshot"] == 0), "name"].nunique()
        mp = df[(df["role"] == "massive_planetesimal") & ~df["name"].isin(flagged)]
        snapshots = sorted(df["snapshot"].unique())
        times = get_times(df)
        te, rms_e = clean(times, rms_curve(mp, "e", snapshots))
        ti, rms_i = clean(times, rms_curve(mp, "inc_deg", snapshots))
        kept = n_mp - len(flagged)
        head = f"PSD2{psd}, {PLANET_LABELS[planet]} planet, q = {q} ({kept}/{n_mp} MPs kept)"

        t_on = base.onset_time(te, rms_e)
        onset_txt = ("$\\leq$ 1e4 yr (above at first output)"
                     if t_on is not None and t_on <= te[0] * 1.0001 else base.fmt_onset(t_on))
        ax_e.plot(te, rms_e, color=PSD_COLOURS[psd], linestyle=PLANET_STYLES[planet],
                  linewidth=1.8, label=f"{head}; t$_{{onset}}$ {onset_txt}")
        if t_on is not None:
            ax_e.plot([t_on], [base.E_ONSET], "o", color=PSD_COLOURS[psd],
                      markeredgecolor="black", markersize=6, zorder=6)
        ax_i.plot(ti, rms_i, color=PSD_COLOURS[psd], linestyle=PLANET_STYLES[planet],
                  linewidth=1.8, label=f"{head}; final RMS i = {rms_i[-1]:.3f}$^\\circ$")
        print(f"{run}: {len(flagged)} MPs cut (r >= {R_CUT:g} AU in a snapshot: {n_far}, "
              f"removed mid-run: {n_removed}); onset = {base.fmt_onset(t_on)}, "
              f"final RMS e = {rms_e[-1]:.3e}, final RMS inc = {rms_i[-1]:.3e} deg")

    ax_e.axhline(base.E_ONSET, color="crimson", linestyle="-.", linewidth=1.2, zorder=1,
                 label=f"Fragmentation onset (RMS e = {base.E_ONSET}); dots = time reached")
    style(ax_e, "RMS eccentricity (MPs that stay inside 120 AU)",
          "RMS Eccentricity vs Time: 10 Myr Lorentzian PSD2 runs, MPs reaching 120 AU removed")
    style(ax_i, "RMS inclination (deg) (MPs that stay inside 120 AU)",
          "RMS Inclination vs Time: 10 Myr Lorentzian PSD2 runs, MPs reaching 120 AU removed")
    for fig, name in ((fig_e, "rms_e_lorentzian_overlay_120AU_cut.png"),
                      (fig_i, "rms_inc_lorentzian_overlay_120AU_cut.png")):
        out = base.OUT_DIR / name
        fig.savefig(out, dpi=200, bbox_inches="tight")
        print(f"saved {out}")


if __name__ == "__main__":
    main()
