"""
plot_lorentzian_rms_e_overlay.py

Overlay the massive-planetesimal RMS e vs time (log-log) of every *completed* 10 Myr
Lorentzian PSD2 run (outputs/SS_800MP_10Myr_PSD2*_lorentzian), with the onset-of-fragmentation
line at RMS e = 0.01. Each legend entry gives the planet, the total disk mass (sum of the
massive-planetesimal masses in distribution.csv) and the radius-slope q of the simulation.

Colour = size distribution (PSD2 A/B/C), linestyle = planet mass.

Writes: calibration/rms_e_lorentzian_overlay.png
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

PSD_COLOURS = {"A": "#2a78d6", "B": "#eb6834", "C": "#2f9e6b"}
PLANET_STYLES = {"none": "-", "10Mearth": (0, (5, 1)), "50Mearth": (0, (3, 1, 1, 1)),
                 "100Mearth": "--", "500Mearth": "-.", "1Mjup": ":"}
PLANET_LABELS = {"none": "no planet", "10Mearth": "10 M$_\\oplus$", "50Mearth": "50 M$_\\oplus$",
                 "100Mearth": "100 M$_\\oplus$", "500Mearth": "500 M$_\\oplus$",
                 "1Mjup": "1 M$_{Jup}$"}


def completed_runs():
    runs = []
    for d in sorted(base.OUTPUTS.glob("SS_800MP_10Myr_PSD2*_lorentzian")):
        meta = d / "run_metadata.yaml"
        if (d / f"{d.name}.bin").exists() and meta.exists() \
                and yaml.safe_load(meta.read_text()).get("outcome") == "completed":
            runs.append(d.name)
    order = list(PLANET_STYLES)
    return sorted(runs, key=lambda r: (r.split("_")[3], order.index(r.split("_")[4])))


def main():
    fig, ax = plt.subplots(figsize=(9, 5.5))
    for run in completed_runs():
        psd, planet = run.split("_")[3:5]
        psd = psd[-1]
        cfg = yaml.safe_load((base.OUTPUTS / run / "config.yaml").read_text())
        q = cfg["massive_planetesimals"]["distribution"]["slope"]
        m_disk = pd.read_csv(base.OUTPUTS / run / "distribution.csv")["mass_earth"].sum()
        _, t, rms = base.load_curves(run)
        keep = t > 0
        t, rms = t[keep], rms[keep]
        t_on = base.onset_time(t, rms)
        # the first output is at t = 1e4 yr; already above the line there means only an upper bound
        onset_txt = ("$\\leq$ 1e4 yr (above at first output)" if t_on is not None and t_on <= t[0] * 1.0001
                     else base.fmt_onset(t_on))
        label = (f"PSD2{psd}, {PLANET_LABELS[planet]} planet: M$_{{disk}}$ = {m_disk:.2f} M$_\\oplus$, "
                 f"q = {q}; t$_{{onset}}$ {onset_txt}")
        ax.plot(t, rms, color=PSD_COLOURS[psd], linestyle=PLANET_STYLES[planet],
                linewidth=1.8, label=label)
        if t_on is not None:
            ax.plot([t_on], [base.E_ONSET], "o", color=PSD_COLOURS[psd], markeredgecolor="black",
                    markersize=6, zorder=6)
        print(f"{run}: M_disk = {m_disk:.3f} Mearth, q = {q}, onset = {base.fmt_onset(t_on)}, "
              f"final RMS e = {rms[-1]:.3e}")
    ax.axhline(base.E_ONSET, color="crimson", linestyle="-.", linewidth=1.2, zorder=1,
               label=f"Fragmentation onset (RMS e = {base.E_ONSET}); dots = time reached")
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel("Time (yr)")
    ax.set_ylabel("RMS eccentricity (MPs = massive planetesimals)")
    ax.set_title("RMS Eccentricity vs Time: completed 10 Myr Lorentzian PSD2 runs")
    ax.grid(alpha=0.25, linewidth=0.6, which="both")
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    ax.legend(loc="upper left", bbox_to_anchor=(1.02, 1), fontsize=8, frameon=False)
    out = base.OUT_DIR / "rms_e_lorentzian_overlay.png"
    fig.savefig(out, dpi=200, bbox_inches="tight")
    print(f"saved {out}")


if __name__ == "__main__":
    main()
