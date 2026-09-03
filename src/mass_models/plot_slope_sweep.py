"""
plot_slope_sweep.py

Sweep the power-law slope of the planetesimal mass spectrum and show how it
reshapes a population of 1000 massive planetesimals.

For each slope q in {0, 0.5, 1.0, ..., 5.0} we draw 1000 masses from

    dN/dm  ~  m^-q,      1e-6 <= m/M_earth <= 1e-2

(no rescaling to a target disk mass, so every slope shares the same mass
support and the histograms are directly comparable), bin them in shared
log-spaced mass bins, and plot number-per-bin vs mass.

Uses the standalone sampler in mass_models.py. Styled after
src/mass_models/plots.py (Agg backend, PNG with bbox_inches="tight", a
"Saved: <path>" line, a small grey footer).

Writes, directly into src/mass_models/:
  * mass_distribution_slope_sweep.png       -- all slopes overlaid
  * mass_distribution_slope_sweep_grid.png  -- one panel per slope
"""

import os
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.cm import ScalarMappable
from matplotlib.colors import Normalize

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)

from mass_models import generate_distribution  # noqa: E402

# --- sweep configuration ---------------------------------------------------
N_PARTICLES = 1000
SLOPES = np.arange(0.0, 5.0 + 1e-9, 0.5)  # 0, 0.5, 1.0, ..., 5.0
MASS_MIN_EARTH = 1.0e-6
MASS_MAX_EARTH = 1.0e-2
DENSITY_G_CM3 = 1.0
BASE_SEED = 42
N_BINS = 24

MASS_BINS = np.logspace(
    np.log10(MASS_MIN_EARTH), np.log10(MASS_MAX_EARTH), N_BINS + 1
)
BIN_CENTRES = np.sqrt(MASS_BINS[:-1] * MASS_BINS[1:])

_CMAP = plt.get_cmap("viridis")
_NORM = Normalize(vmin=SLOPES.min(), vmax=SLOPES.max())


def _footer():
    return (
        f"N={N_PARTICLES} per slope · dN/dm ~ m^-q · "
        f"m in [{MASS_MIN_EARTH:g}, {MASS_MAX_EARTH:g}] M_earth · "
        f"rho={DENSITY_G_CM3:g} g/cm^3 · seed={BASE_SEED} (+ slope index)"
    )


def _save(fig, filename, dpi=200):
    fig.text(
        0.005, 0.005, _footer(),
        fontsize=6, color="0.5", ha="left", va="bottom", alpha=0.8,
    )
    save_path = Path(_HERE) / filename
    fig.savefig(save_path, dpi=dpi, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved: {save_path}")
    return save_path


def sample_counts(slope, seed):
    """Number of the 1000 planetesimals falling in each shared mass bin."""
    df = generate_distribution(
        n_particles=N_PARTICLES,
        distribution_variable="mass",
        value_min=MASS_MIN_EARTH,
        value_max=MASS_MAX_EARTH,
        slope=float(slope),
        density_g_cm3=DENSITY_G_CM3,
        mass_unit="earth",
        total_disk_mass_earth=None,  # keep the raw power-law support
        seed=seed,
    )
    counts, _ = np.histogram(df["mass_earth"], bins=MASS_BINS)
    return counts


def expected_counts(slope):
    """Expected number of N_PARTICLES per shared bin for dN/dm ~ m^-q.

    Integrates the truncated power law over each bin analytically, so the
    curve is the smooth Poisson mean the sampled histograms scatter around.
    """
    a, b = MASS_BINS[:-1], MASS_BINS[1:]
    if np.isclose(slope, 1.0):
        weight = np.log(b / a)
    else:
        p = 1.0 - slope
        weight = (b ** p - a ** p) / p
    return N_PARTICLES * weight / weight.sum()


def plot_overlay(counts_by_slope):
    fig, ax = plt.subplots(figsize=(9, 6))

    for slope, counts in counts_by_slope:
        color = _CMAP(_NORM(slope))
        # smooth analytic expectation ...
        ax.plot(BIN_CENTRES, expected_counts(slope), color=color, lw=2.0)
        # ... with the actual 1000-body draw as faint markers
        drawn = counts.astype(float)
        drawn[drawn == 0] = np.nan
        ax.plot(
            BIN_CENTRES, drawn, color=color, lw=0,
            marker="o", ms=3, alpha=0.35,
        )

    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_ylim(1e-2, 5e2)
    ax.set_xlabel("Mass (Earth masses)")
    ax.set_ylabel(f"Number of planetesimals per bin  (N = {N_PARTICLES})")
    ax.set_title(
        "Planetesimal mass distribution vs power-law slope\n"
        r"$dN/dm \propto m^{-q}$, 1000 bodies, "
        f"{MASS_MIN_EARTH:g}–{MASS_MAX_EARTH:g} $M_\\oplus$ "
        "(lines: expected; points: one draw)"
    )
    ax.grid(alpha=0.3, which="both")

    cbar = fig.colorbar(ScalarMappable(norm=_NORM, cmap=_CMAP), ax=ax)
    cbar.set_label("slope  q")
    cbar.set_ticks(SLOPES)

    fig.tight_layout()
    return _save(fig, "mass_distribution_slope_sweep.png")


def plot_grid(counts_by_slope):
    n = len(counts_by_slope)
    ncols = 4
    nrows = int(np.ceil(n / ncols))

    fig, axes = plt.subplots(
        nrows, ncols, figsize=(3.2 * ncols, 2.6 * nrows),
        sharex=True, sharey=True,
    )
    axes = np.atleast_1d(axes).ravel()

    ymax = max(counts.max() for _, counts in counts_by_slope)

    for ax, (slope, counts) in zip(axes, counts_by_slope):
        color = _CMAP(_NORM(slope))
        ax.step(BIN_CENTRES, counts, where="mid", color=color, lw=1.6)
        ax.plot(BIN_CENTRES, expected_counts(slope), color="0.35", lw=1.0, ls="--")
        ax.set_xscale("log")
        ax.set_yscale("log")
        ax.set_title(f"q = {slope:g}", fontsize=10)
        ax.grid(alpha=0.3, which="both")
        ax.set_ylim(0.7, ymax * 1.4)

    for ax in axes[n:]:
        ax.set_visible(False)

    fig.supxlabel("Mass (Earth masses)")
    fig.supylabel(f"Number per bin  (N = {N_PARTICLES})")
    fig.suptitle(
        r"Planetesimal mass distribution vs slope $q$  ($dN/dm \propto m^{-q}$)",
        fontsize=14,
    )
    fig.tight_layout()
    return _save(fig, "mass_distribution_slope_sweep_grid.png")


def main():
    counts_by_slope = [
        (slope, sample_counts(slope, seed=BASE_SEED + i))
        for i, slope in enumerate(SLOPES)
    ]
    plot_overlay(counts_by_slope)
    plot_grid(counts_by_slope)


if __name__ == "__main__":
    main()
