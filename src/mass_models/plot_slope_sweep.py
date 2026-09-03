"""
plot_slope_sweep.py

Sweep the power-law slope of the planetesimal *size* spectrum and show how it
reshapes a population of 1000 massive planetesimals.

For each slope q in {2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0} we draw 1000 radii from

    dN/dR  ~  R^-q,      1 km <= R <= 100 km

and plot the cumulative size distribution: every one of the 1000 planetesimals
is a single point at (its radius, its rank), i.e. the number of bodies at least
that large, N(>=R). The smooth analytic N(>=R) for the truncated power law is
overlaid.

Uses the standalone sampler in mass_models.py. Styled after
src/mass_models/plots.py (Agg backend, PNG with bbox_inches="tight", a
"Saved: <path>" line, a small grey footer).

Writes, directly into src/mass_models/:
  * radius_distribution_slope_sweep.png       -- all slopes overlaid
  * radius_distribution_slope_sweep_grid.png  -- one panel per slope
  * radius_distribution_slope_q<q>.png        -- one standalone figure per slope
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
SLOPES = np.arange(2.0, 5.0 + 1e-9, 0.5)  # 2.0, 2.5, 3.0, ..., 5.0
RADIUS_MIN_KM = 1.0
RADIUS_MAX_KM = 100.0
DENSITY_G_CM3 = 1.0
BASE_SEED = 42

RANKS = np.arange(1, N_PARTICLES + 1)  # y-axis: cumulative count N(>=R)

_CMAP = plt.get_cmap("viridis")
_NORM = Normalize(vmin=SLOPES.min(), vmax=SLOPES.max())


def _footer():
    return (
        f"N={N_PARTICLES} per slope · dN/dR ~ R^-q · "
        f"R in [{RADIUS_MIN_KM:g}, {RADIUS_MAX_KM:g}] km · "
        f"seed={BASE_SEED} (+ slope index)"
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


def sample_radii_descending(slope, seed):
    """The 1000 sampled radii (km), sorted largest -> smallest."""
    df = generate_distribution(
        n_particles=N_PARTICLES,
        distribution_variable="radius",
        value_min=RADIUS_MIN_KM,
        value_max=RADIUS_MAX_KM,
        slope=float(slope),
        density_g_cm3=DENSITY_G_CM3,
        seed=seed,
    )
    return np.sort(df["radius_km"].to_numpy())[::-1]


def expected_cumulative(radii_km, slope):
    """Analytic N(>=R) for dN/dR ~ R^-q truncated to [RADIUS_MIN_KM, RADIUS_MAX_KM].

    Normalised so N(>=RADIUS_MIN_KM) = N_PARTICLES and N(>=RADIUS_MAX_KM) = 0.
    """
    r = np.asarray(radii_km, dtype=float)
    if np.isclose(slope, 1.0):
        num = np.log(RADIUS_MAX_KM / r)
        den = np.log(RADIUS_MAX_KM / RADIUS_MIN_KM)
    else:
        p = 1.0 - slope
        num = r ** p - RADIUS_MAX_KM ** p
        den = RADIUS_MIN_KM ** p - RADIUS_MAX_KM ** p
    return N_PARTICLES * num / den


def _plot_one(ax, slope, radii_desc, color, marker_size, expected_color=None):
    """Draw one slope's cumulative distribution (every body) + analytic curve."""
    ax.plot(
        radii_desc, RANKS,
        color=color, lw=0, marker="o", ms=marker_size,
        alpha=0.5, mew=0,
    )
    r_line = np.logspace(np.log10(RADIUS_MIN_KM), np.log10(RADIUS_MAX_KM), 300)
    ax.plot(
        r_line, expected_cumulative(r_line, slope),
        color=expected_color or color, lw=1.6,
    )


def plot_overlay(radii_by_slope):
    fig, ax = plt.subplots(figsize=(9, 6))

    for slope, radii_desc in radii_by_slope:
        _plot_one(ax, slope, radii_desc, _CMAP(_NORM(slope)), marker_size=2.5)

    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlim(RADIUS_MIN_KM, RADIUS_MAX_KM)
    ax.set_ylim(0.8, N_PARTICLES * 1.3)
    ax.set_xlabel("Radius (km)")
    ax.set_ylabel(r"Number of planetesimals with radius $\geq R$")
    ax.set_title(
        "Planetesimal size distribution vs power-law slope\n"
        r"$dN/dR \propto R^{-q}$, 1000 bodies each, "
        f"{RADIUS_MIN_KM:g}–{RADIUS_MAX_KM:g} km "
        "(points: every body; lines: analytic)"
    )
    ax.grid(alpha=0.3, which="both")

    cbar = fig.colorbar(ScalarMappable(norm=_NORM, cmap=_CMAP), ax=ax)
    cbar.set_label("slope  q")
    cbar.set_ticks(SLOPES)

    fig.tight_layout()
    return _save(fig, "radius_distribution_slope_sweep.png")


def plot_per_slope(radii_by_slope):
    """One standalone figure per slope, every planetesimal shown."""
    paths = []
    for slope, radii_desc in radii_by_slope:
        color = _CMAP(_NORM(slope))

        fig, ax = plt.subplots(figsize=(8, 5.5))
        _plot_one(ax, slope, radii_desc, color, marker_size=4,
                  expected_color="0.25")

        ax.set_xscale("log")
        ax.set_yscale("log")
        ax.set_xlim(RADIUS_MIN_KM, RADIUS_MAX_KM)
        ax.set_ylim(0.8, N_PARTICLES * 1.3)
        ax.set_xlabel("Radius (km)")
        ax.set_ylabel(r"Number of planetesimals with radius $\geq R$")
        ax.set_title(
            r"Planetesimal size distribution, $dN/dR \propto R^{-q}$"
            f"\nslope q = {slope:g}"
        )
        ax.grid(alpha=0.3, which="both")
        ax.legend(
            handles=[
                plt.Line2D([], [], color=color, lw=0, marker="o", ms=5,
                           alpha=0.6, label=f"every body (N = {N_PARTICLES})"),
                plt.Line2D([], [], color="0.25", lw=1.6, label="analytic N(≥R)"),
            ]
        )

        fig.tight_layout()
        paths.append(_save(fig, f"radius_distribution_slope_q{slope:g}.png"))
    return paths


def plot_grid(radii_by_slope):
    n = len(radii_by_slope)
    ncols = 4
    nrows = int(np.ceil(n / ncols))

    fig, axes = plt.subplots(
        nrows, ncols, figsize=(3.4 * ncols, 2.8 * nrows),
        sharex=True, sharey=True,
    )
    axes = np.atleast_1d(axes).ravel()

    for ax, (slope, radii_desc) in zip(axes, radii_by_slope):
        _plot_one(ax, slope, radii_desc, _CMAP(_NORM(slope)), marker_size=2.5,
                  expected_color="0.25")
        ax.set_xscale("log")
        ax.set_yscale("log")
        ax.set_xlim(RADIUS_MIN_KM, RADIUS_MAX_KM)
        ax.set_ylim(0.8, N_PARTICLES * 1.3)
        ax.set_title(f"q = {slope:g}", fontsize=10)
        ax.grid(alpha=0.3, which="both")

    for ax in axes[n:]:
        ax.set_visible(False)

    fig.supxlabel("Radius (km)")
    fig.supylabel(r"Number with radius $\geq R$")
    fig.suptitle(
        r"Planetesimal size distribution vs slope $q$  ($dN/dR \propto R^{-q}$)",
        fontsize=14,
    )
    fig.tight_layout()
    return _save(fig, "radius_distribution_slope_sweep_grid.png")


def main():
    radii_by_slope = [
        (slope, sample_radii_descending(slope, seed=BASE_SEED + i))
        for i, slope in enumerate(SLOPES)
    ]
    plot_overlay(radii_by_slope)
    plot_grid(radii_by_slope)
    plot_per_slope(radii_by_slope)


if __name__ == "__main__":
    main()
