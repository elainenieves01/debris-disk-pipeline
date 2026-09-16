"""
plot_slope_sweep.py

Sweep the power-law slope of the planetesimal *size* spectrum and show how it
reshapes a population of massive planetesimals.

For each slope q in {2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0} we draw ``--n`` radii from

    dN/dR  ~  R^-q,      radius_min <= R <= radius_max

and plot the cumulative size distribution: every one of the sampled planetesimals
is a single point at (its radius, its rank), i.e. the number of bodies at least
that large, N(>=R). The smooth analytic N(>=R) for the truncated power law is
overlaid.

Uses the standalone sampler in mass_models.py. Styled after
src/mass_models/plots.py (Agg backend, PNG with bbox_inches="tight", a
"Saved: <path>" line, a small grey footer).

Run with no arguments to regenerate the committed sweep figures
(N=1000, 1-100 km) in place under src/mass_models/:
  * radius_distribution_slope_sweep.png       -- all slopes overlaid
  * radius_distribution_slope_sweep_grid.png  -- one panel per slope
  * radius_distribution_slope_q<q>.png        -- one standalone figure per slope

Pass --outdir to write elsewhere, and --per-slope to also dump a
distribution.csv plus the src/mass_models/plots.py histogram set for every slope:

    python src/mass_models/plot_slope_sweep.py \\
        --n 500 --radius-max 200 \\
        --outdir outputs/radius_slope_sweep_200km_500N --per-slope
"""

import argparse
import os
import sys
from dataclasses import dataclass, field
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
from plots import (  # noqa: E402
    plot_per_particle,
    plot_differential_histogram,
    plot_count_histograms,
)

# --- defaults (also the values baked into the committed figures) ----------
DEFAULT_N = 1000
DEFAULT_SLOPE_MIN = 2.0
DEFAULT_SLOPE_MAX = 5.0
DEFAULT_SLOPE_STEP = 0.5
DEFAULT_RADIUS_MIN_KM = 1.0
DEFAULT_RADIUS_MAX_KM = 100.0
DEFAULT_DENSITY_G_CM3 = 1.0
DEFAULT_SEED = 42


@dataclass
class SweepCfg:
    n: int = DEFAULT_N
    radius_min: float = DEFAULT_RADIUS_MIN_KM
    radius_max: float = DEFAULT_RADIUS_MAX_KM
    slopes: np.ndarray = field(
        default_factory=lambda: np.arange(
            DEFAULT_SLOPE_MIN, DEFAULT_SLOPE_MAX + 1e-9, DEFAULT_SLOPE_STEP
        )
    )
    density_g_cm3: float = DEFAULT_DENSITY_G_CM3
    seed: int = DEFAULT_SEED
    outdir: str = _HERE

    @property
    def ranks(self):
        return np.arange(1, self.n + 1)  # y-axis: cumulative count N(>=R)

    @property
    def norm(self):
        return Normalize(vmin=float(self.slopes.min()), vmax=float(self.slopes.max()))

    @property
    def cmap(self):
        return plt.get_cmap("viridis")


def _footer(cfg):
    return (
        f"N={cfg.n} per slope · dN/dR ~ R^-q · "
        f"R in [{cfg.radius_min:g}, {cfg.radius_max:g}] km · "
        f"seed={cfg.seed} (+ slope index)"
    )


def _save(cfg, fig, filename, dpi=200):
    fig.text(
        0.005, 0.005, _footer(cfg),
        fontsize=6, color="0.5", ha="left", va="bottom", alpha=0.8,
    )
    save_path = Path(cfg.outdir) / filename
    fig.savefig(save_path, dpi=dpi, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved: {save_path}")
    return save_path


def sample_radii_descending(cfg, slope, seed):
    """The sampled radii (km) for one slope, sorted largest -> smallest."""
    df = generate_distribution(
        n_particles=cfg.n,
        distribution_variable="radius",
        value_min=cfg.radius_min,
        value_max=cfg.radius_max,
        slope=float(slope),
        density_g_cm3=cfg.density_g_cm3,
        seed=seed,
    )
    return np.sort(df["radius_km"].to_numpy())[::-1]


def expected_cumulative(cfg, radii_km, slope):
    """Analytic N(>=R) for dN/dR ~ R^-q truncated to [radius_min, radius_max].

    Normalised so N(>=radius_min) = cfg.n and N(>=radius_max) = 0.
    """
    r = np.asarray(radii_km, dtype=float)
    if np.isclose(slope, 1.0):
        num = np.log(cfg.radius_max / r)
        den = np.log(cfg.radius_max / cfg.radius_min)
    else:
        p = 1.0 - slope
        num = r ** p - cfg.radius_max ** p
        den = cfg.radius_min ** p - cfg.radius_max ** p
    return cfg.n * num / den


def _plot_one(cfg, ax, slope, radii_desc, color, marker_size, expected_color=None):
    """Draw one slope's cumulative distribution (every body) + analytic curve."""
    ax.plot(
        radii_desc, cfg.ranks,
        color=color, lw=0, marker="o", ms=marker_size,
        alpha=0.5, mew=0,
    )
    r_line = np.logspace(np.log10(cfg.radius_min), np.log10(cfg.radius_max), 300)
    ax.plot(
        r_line, expected_cumulative(cfg, r_line, slope),
        color=expected_color or color, lw=1.6,
    )


def plot_overlay(cfg, radii_by_slope):
    fig, ax = plt.subplots(figsize=(9, 6))

    for slope, radii_desc in radii_by_slope:
        _plot_one(cfg, ax, slope, radii_desc, cfg.cmap(cfg.norm(slope)),
                  marker_size=2.5)

    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlim(cfg.radius_min, cfg.radius_max)
    ax.set_ylim(0.8, cfg.n * 1.3)
    ax.set_xlabel("Radius (km)")
    ax.set_ylabel(r"Number of planetesimals with radius $\geq R$")
    ax.set_title(
        "Planetesimal size distribution vs power-law slope\n"
        r"$dN/dR \propto R^{-q}$, "
        f"{cfg.n} bodies each, "
        f"{cfg.radius_min:g}-{cfg.radius_max:g} km "
        "(points: every body; lines: analytic)"
    )
    ax.grid(alpha=0.3, which="both")

    cbar = fig.colorbar(ScalarMappable(norm=cfg.norm, cmap=cfg.cmap), ax=ax)
    cbar.set_label("slope  q")
    cbar.set_ticks(cfg.slopes)

    fig.tight_layout()
    return _save(cfg, fig, "radius_distribution_slope_sweep.png")


def plot_per_slope(cfg, radii_by_slope):
    """One standalone figure per slope, every planetesimal shown."""
    paths = []
    for slope, radii_desc in radii_by_slope:
        color = cfg.cmap(cfg.norm(slope))

        fig, ax = plt.subplots(figsize=(8, 5.5))
        _plot_one(cfg, ax, slope, radii_desc, color, marker_size=4,
                  expected_color="0.25")

        ax.set_xscale("log")
        ax.set_yscale("log")
        ax.set_xlim(cfg.radius_min, cfg.radius_max)
        ax.set_ylim(0.8, cfg.n * 1.3)
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
                           alpha=0.6, label=f"every body (N = {cfg.n})"),
                plt.Line2D([], [], color="0.25", lw=1.6, label="analytic N(≥R)"),
            ]
        )

        fig.tight_layout()
        paths.append(_save(cfg, fig, f"radius_distribution_slope_q{slope:g}.png"))
    return paths


def plot_grid(cfg, radii_by_slope):
    n = len(radii_by_slope)
    ncols = 4
    nrows = int(np.ceil(n / ncols))

    fig, axes = plt.subplots(
        nrows, ncols, figsize=(3.4 * ncols, 2.8 * nrows),
        sharex=True, sharey=True,
    )
    axes = np.atleast_1d(axes).ravel()

    for ax, (slope, radii_desc) in zip(axes, radii_by_slope):
        _plot_one(cfg, ax, slope, radii_desc, cfg.cmap(cfg.norm(slope)),
                  marker_size=2.5, expected_color="0.25")
        ax.set_xscale("log")
        ax.set_yscale("log")
        ax.set_xlim(cfg.radius_min, cfg.radius_max)
        ax.set_ylim(0.8, cfg.n * 1.3)
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
    return _save(cfg, fig, "radius_distribution_slope_sweep_grid.png")


def _write_per_slope_diagnostics(cfg):
    """distribution.csv + plots.py histogram set for each slope, one folder each."""
    for i, slope in enumerate(cfg.slopes):
        slope = float(slope)
        df = generate_distribution(
            n_particles=cfg.n,
            distribution_variable="radius",
            value_min=cfg.radius_min,
            value_max=cfg.radius_max,
            slope=slope,
            density_g_cm3=cfg.density_g_cm3,
            seed=cfg.seed + i,
        )

        slope_dir = Path(cfg.outdir) / f"slope_q{slope:g}"
        slope_dir.mkdir(parents=True, exist_ok=True)
        csv_path = slope_dir / "distribution.csv"
        df.to_csv(csv_path, index=False)
        print(f"Saved: {csv_path}")

        label = (
            f"Size spectrum q = {slope:g}  (N = {cfg.n}, "
            f"{cfg.radius_min:g}-{cfg.radius_max:g} km)"
        )
        plot_per_particle(df, slope_dir, label=label)
        plot_differential_histogram(df, slope_dir, slope=slope, label=label)
        plot_count_histograms(df, slope_dir, label=label)


def parse_args(argv=None):
    p = argparse.ArgumentParser(
        description=(
            "Sweep the planetesimal size-spectrum power-law slope and plot the "
            "resulting populations."
        )
    )
    p.add_argument("--n", type=int, default=DEFAULT_N,
                   help=f"planetesimals per slope (default: {DEFAULT_N})")
    p.add_argument("--radius-min", type=float, default=DEFAULT_RADIUS_MIN_KM,
                   help=f"lower radius truncation in km (default: {DEFAULT_RADIUS_MIN_KM:g})")
    p.add_argument("--radius-max", type=float, default=DEFAULT_RADIUS_MAX_KM,
                   help=f"upper radius truncation in km (default: {DEFAULT_RADIUS_MAX_KM:g})")
    p.add_argument("--slope-min", type=float, default=DEFAULT_SLOPE_MIN,
                   help=f"first slope q (default: {DEFAULT_SLOPE_MIN:g})")
    p.add_argument("--slope-max", type=float, default=DEFAULT_SLOPE_MAX,
                   help=f"last slope q, inclusive (default: {DEFAULT_SLOPE_MAX:g})")
    p.add_argument("--slope-step", type=float, default=DEFAULT_SLOPE_STEP,
                   help=f"slope increment (default: {DEFAULT_SLOPE_STEP:g})")
    p.add_argument("--seed", type=int, default=DEFAULT_SEED,
                   help=f"base RNG seed; slope i uses seed+i (default: {DEFAULT_SEED})")
    p.add_argument("--outdir", default=_HERE,
                   help="output directory (default: src/mass_models/, i.e. "
                        "regenerate the committed figures in place)")
    p.add_argument("--per-slope", action="store_true",
                   help="also write <outdir>/slope_q<q>/distribution.csv and the "
                        "per-particle / differential / count histograms per slope")
    return p.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)
    slopes = np.arange(args.slope_min, args.slope_max + 1e-9, args.slope_step)
    cfg = SweepCfg(
        n=args.n,
        radius_min=args.radius_min,
        radius_max=args.radius_max,
        slopes=slopes,
        seed=args.seed,
        outdir=args.outdir,
    )
    os.makedirs(cfg.outdir, exist_ok=True)

    radii_by_slope = [
        (float(slope), sample_radii_descending(cfg, float(slope), seed=cfg.seed + i))
        for i, slope in enumerate(cfg.slopes)
    ]
    plot_overlay(cfg, radii_by_slope)
    plot_grid(cfg, radii_by_slope)
    plot_per_slope(cfg, radii_by_slope)

    if args.per_slope:
        _write_per_slope_diagnostics(cfg)


if __name__ == "__main__":
    main()
