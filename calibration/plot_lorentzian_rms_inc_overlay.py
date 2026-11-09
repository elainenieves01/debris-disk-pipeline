"""
plot_lorentzian_rms_inc_overlay.py

Inclination counterpart of plot_lorentzian_rms_e_overlay.py: overlay the
massive-planetesimal RMS inclination (deg) vs time (log-log) of every *completed*
10 Myr Lorentzian PSD2 run, with the same colours (PSD2 A/B/C) and line styles
(planet mass) as the eccentricity overlay.

The bodies are the ones the eccentricity overlay keeps (Rayleigh sigma cut on e;
see plot_all_rms_inc_overlay.load_inclination), so the two figures describe the
same set of bodies. Repeated snapshot times (checkpoint restarts) are dropped.

Writes: calibration/rms_inc_lorentzian_overlay.png
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import matplotlib  # noqa: E402

matplotlib.use("Agg")

import matplotlib.pyplot as plt  # noqa: E402
import pandas as pd  # noqa: E402
import yaml  # noqa: E402

import plot_all_rms_e_overlay as base  # noqa: E402
from plot_all_rms_inc_overlay import clean, load_inclination  # noqa: E402
from plot_lorentzian_rms_e_overlay import (  # noqa: E402
    PLANET_LABELS, PLANET_STYLES, PSD_COLOURS, completed_runs)


def main():
    fig, ax = plt.subplots(figsize=(9, 5.5))
    for run in completed_runs():
        psd, planet = run.split("_")[3:5]
        psd = psd[-1]
        cfg = yaml.safe_load((base.OUTPUTS / run / "config.yaml").read_text())
        q = cfg["massive_planetesimals"]["distribution"]["slope"]
        m_disk = pd.read_csv(base.OUTPUTS / run / "distribution.csv")["mass_earth"].sum()
        _, t, rms = load_inclination(run)
        t, rms = clean(t, rms)
        label = (f"PSD2{psd}, {PLANET_LABELS[planet]} planet: M$_{{disk}}$ = {m_disk:.2f} M$_\\oplus$, "
                 f"q = {q}; final RMS i = {rms[-1]:.3f}$^\\circ$")
        ax.plot(t, rms, color=PSD_COLOURS[psd], linestyle=PLANET_STYLES[planet],
                linewidth=1.8, label=label)
        print(f"{run}: q = {q}, first RMS inc = {rms[0]:.3e} deg, final RMS inc = {rms[-1]:.3e} deg "
              f"at t = {t[-1]:.3g} yr")
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel("Time (yr)")
    ax.set_ylabel("RMS inclination (deg) (MPs = massive planetesimals)")
    ax.set_title("RMS Inclination vs Time: completed 10 Myr Lorentzian PSD2 runs")
    ax.grid(alpha=0.25, linewidth=0.6, which="both")
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    ax.legend(loc="upper left", bbox_to_anchor=(1.02, 1), fontsize=8, frameon=False)
    out = base.OUT_DIR / "rms_inc_lorentzian_overlay.png"
    fig.savefig(out, dpi=200, bbox_inches="tight")
    print(f"saved {out}")


if __name__ == "__main__":
    main()
