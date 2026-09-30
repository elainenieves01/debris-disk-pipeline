"""
plot_500kyr_rms_e_overlay.py

Overlay the massive-planetesimal RMS eccentricity vs time of the two 500 kyr,
1 M_earth, q = 3.5 runs -- without test particles
(SS_800MP_500kyr_1Mearth_slopeq3.5) and with 1000 test particles
(SS_800MP_1000TP_500kyr_1Mearth_slopeq3.5). Both runs start from identical
massive planetesimals; the test particles are massless.

Each run is drawn twice: all massive planetesimals (dashed) and with the
Rayleigh 5 sigma outlier cut (solid; the same bodies the C_e diagnostic
excludes -- MP_107 and MP_335 in both runs, see src/utilities/rayleigh_cut.py).

Writes: calibration/rms_e_500kyr_overlay.png
"""

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
for _sub in ("plotting", "utilities", "config_io"):
    sys.path.insert(0, str(REPO_ROOT / "src" / _sub))

import matplotlib  # noqa: E402

matplotlib.use("Agg")

import matplotlib.pyplot as plt  # noqa: E402

from config_utils import read_config  # noqa: E402
from rayleigh_cut import cut_nsigma_from_config  # noqa: E402
from summary_figures import build_snapshot_table, rms_eccentricity_rayleigh_cut  # noqa: E402

OUTPUTS = REPO_ROOT / "outputs"
OUT_PATH = Path(__file__).resolve().parent / "rms_e_500kyr_overlay.png"

# run -> (label, colour): categorical slots 1 and 2 of the dataviz reference palette
RUNS = {
    "SS_800MP_500kyr_1Mearth_slopeq3.5": ("No test particles", "#2a78d6"),
    "SS_800MP_1000TP_500kyr_1Mearth_slopeq3.5": ("1000 test particles", "#eb6834"),
}


def main():
    fig, ax = plt.subplots(figsize=(8, 5))
    end_labels = []  # (t_end, y_end, text, ink)

    for run, (label, colour) in RUNS.items():
        run_dir = OUTPUTS / run
        config = read_config(str(run_dir / "config.yaml"))
        nsigma = cut_nsigma_from_config(config)
        df = build_snapshot_table(run_dir / f"{run}.bin")
        t, rms_all, rms_cut, excluded = rms_eccentricity_rayleigh_cut(
            df, float(config["disk"]["emax"]), nsigma)

        ax.plot(t, rms_all, color=colour, linestyle="--", linewidth=1.5, alpha=0.8,
                label=f"{label}, all MPs")
        ax.plot(t, rms_cut, color=colour, linewidth=2,
                label=f"{label}, Rayleigh {nsigma:g}σ cut ({', '.join(excluded)} removed)")
        # final values as direct labels (text in ink, not series colour)
        end_labels.append((t[-1], rms_cut[-1], f"{rms_cut[-1]:.4f}", "0.25"))
        end_labels.append((t[-1], rms_all[-1], f"{rms_all[-1]:.4f}", "0.45"))
        print(f"{run}: final RMS e all = {rms_all[-1]:.4e}, cut = {rms_cut[-1]:.4e}")

    # spread end labels that would overlap (keep >= ~3% of the axis height apart)
    ax.set_ylim(bottom=0)
    min_gap = 0.03 * ax.get_ylim()[1]
    placed = []
    for t_end, y, text, ink in sorted(end_labels, key=lambda item: item[1]):
        y_text = max(y, placed[-1] + min_gap) if placed else y
        placed.append(y_text)
        ax.annotate(text, (t_end, y), xytext=(1.01 * t_end, y_text), textcoords="data",
                    va="center", fontsize=8, color=ink,
                    xycoords="data", annotation_clip=False,
                    horizontalalignment="left")

    ax.set_xlabel("Time (yr)")
    ax.set_ylabel("RMS eccentricity (massive planetesimals)")
    ax.set_title("RMS Eccentricity vs Time: 500 kyr, 1 M$_\\oplus$, q = 3.5 runs")
    ax.set_xlim(left=0)
    ax.set_ylim(bottom=0)
    ax.margins(x=0.08)
    ax.grid(alpha=0.25, linewidth=0.6)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    ax.legend(loc="lower right", fontsize=8, frameon=False)

    fig.savefig(OUT_PATH, dpi=200, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved: {OUT_PATH.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
