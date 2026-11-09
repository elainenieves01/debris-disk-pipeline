"""
plot_psd2_rms_e.py

RMS e vs time (log-log) for each finished 10 Myr Lorentzian PSD2 run, with the
onset-of-fragmentation line (RMS e = 0.01) and the time the curve first reaches it.

Same RMS e as plot_all_rms_e_overlay.py (massive planetesimals, Rayleigh sigma cut).

Writes: calibration/rms_e_<run>.png for each run in RUNS
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import matplotlib  # noqa: E402

matplotlib.use("Agg")

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

import plot_all_rms_e_overlay as base  # noqa: E402

RUNS = {
    "SS_800MP_10Myr_PSD2A_500Mearth_lorentzian": "PSD2A, 500 M$_\\oplus$ planet",
    "SS_800MP_10Myr_PSD2B_500Mearth_lorentzian": "PSD2B, 500 M$_\\oplus$ planet",
}


def main():
    for run, label in RUNS.items():
        df, t, rms = base.load_curves(run)
        keep = t > 0
        t, rms = t[keep], rms[keep]
        t_on = base.onset_time(t, rms)
        late = t >= base.FIT_T_MIN
        p, log_a = np.polyfit(np.log10(t[late]), np.log10(rms[late]), 1)

        fig, ax = plt.subplots(figsize=(8, 5))
        ax.plot(t, rms, color="#2a78d6", linewidth=1.8, label=f"{label}, MPs (Rayleigh cut)")
        ax.plot(t[late], 10 ** (p * np.log10(t[late]) + log_a), color="black", linewidth=0.8,
                label=f"fit e = A t$^p$, p = {p:.2f} (t $\\geq$ 10$^5$ yr)")
        ax.axhline(base.E_ONSET, color="crimson", linestyle="-.", linewidth=1.2,
                   label=f"Onset of fragmentation (RMS e = {base.E_ONSET})")
        if t_on is not None:
            ax.plot([t_on], [base.E_ONSET], "o", color="#2a78d6", markeredgecolor="black",
                    markersize=7, zorder=6)
            ax.axvline(t_on, color="crimson", linestyle=":", linewidth=0.9)
            # the first output is at t = 1e4 yr; if RMS e is already above the line there,
            # the true crossing happened earlier and only an upper bound is known
            first = t_on <= t[0] * 1.0001
            txt = (f"already > {base.E_ONSET} at first output:\nt$_{{onset}}$ $\\leq$ {t_on:.0e} yr"
                   if first else f"reached at t = {t_on:.2e} yr")
            ax.annotate(txt, (t_on, base.E_ONSET), xytext=(10, 28), textcoords="offset points",
                        fontsize=9, color="crimson")
        ax.set_xscale("log")
        ax.set_yscale("log")
        ax.set_xlabel("Time (yr)")
        ax.set_ylabel("RMS eccentricity (MPs)")
        ax.set_title(f"RMS e vs time: {run}", fontsize=10)
        ax.grid(alpha=0.25, linewidth=0.6, which="both")
        for side in ("top", "right"):
            ax.spines[side].set_visible(False)
        ax.legend(loc="upper left", fontsize=8, frameon=False)
        out = base.OUT_DIR / f"rms_e_{run}.png"
        fig.savefig(out, dpi=200, bbox_inches="tight")
        plt.close(fig)
        print(f"{run}: onset = {base.fmt_onset(t_on)}, p = {p:.3f}, final RMS e = {rms[-1]:.4e}, "
              f"t_end = {t[-1]:.3e}\n  saved {out}")


if __name__ == "__main__":
    main()
