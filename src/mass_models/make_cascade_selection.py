"""
make_cascade_selection.py

Sample a large planetesimal size *cascade*  dN/dR ~ R^-q  on [radius_min,
radius_max], then keep the ``--n-keep`` bodies that best *preserve* the power
law.

Why: the largest bodies of any finite draw scatter away from the analytic
N(>=R) -- there are only a handful of them, so Poisson noise on the count is
large. If you just took "the N_keep largest" you would inherit that noisy tail.
Instead we:

  1. draw a big cascade (``--n-cascade``; sampled in chunks, only the top ranks
     are retained so this scales past what fits in memory),
  2. compare the sampled cumulative count to the analytic truncated power law,
  3. drop every rank (in the small-count regime) that deviates from the analytic
     curve by more than ``--tol`` fractionally, and
  4. keep the contiguous block of ``--n-keep`` bodies starting just below the
     deepest such deviation -- the largest bodies that still trace dN/dR ~ R^-q.

For each slope q in the sweep this writes, under ``--outdir``:

  slope_q<q>/selected.csv              -- the N_keep kept bodies
  slope_q<q>/figures/*.png             -- plots.py per-particle / differential /
                                         count histograms of the kept sample
  slope_q<q>/cascade_top.csv           -- retained top ranks (only with --save-cascade)

and, spanning all slopes:

  residual_diagnostic_grid.png         -- sampled / analytic vs rank, cut marked
  selection_cumulative_grid.png        -- N(>=R), tail dropped / block kept / below

Example:

    python src/mass_models/make_cascade_selection.py \\
        --n-cascade 5_000_000 --n-keep 800 --radius-max 200 \\
        --outdir src/mass_models/cascade_selection_200km_800keep
"""

import argparse
import os
import sys
from dataclasses import dataclass
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np
import pandas as pd
from matplotlib.colors import Normalize

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)

from mass_models import (  # noqa: E402
    M_EARTH_KG,
    M_SUN_KG,
    radii_to_masses,
    sample_powerlaw,
)
from plots import (  # noqa: E402
    plot_per_particle,
    plot_differential_histogram,
    plot_count_histograms,
)

DEFAULT_N_CASCADE = 5_000_000
DEFAULT_N_KEEP = 800
DEFAULT_RADIUS_MIN_KM = 1.0
DEFAULT_RADIUS_MAX_KM = 200.0
DEFAULT_SLOPE_MIN = 2.0
DEFAULT_SLOPE_MAX = 5.0
DEFAULT_SLOPE_STEP = 0.5
DEFAULT_DENSITY_G_CM3 = 1.0
DEFAULT_TOL = 0.2
DEFAULT_SEED = 42
_SAMPLE_CHUNK = 5_000_000


@dataclass
class Cfg:
    n_cascade: int
    n_keep: int
    radius_min: float
    radius_max: float
    slopes: np.ndarray
    density_g_cm3: float
    tol: float
    seed: int
    outdir: str
    save_cascade: bool

    @property
    def keep_top(self):
        """How many of the largest cascade radii to retain in memory."""
        return max(20_000, 25 * self.n_keep)


# ---------------------------------------------------------------------------
# analytic truncated power law
# ---------------------------------------------------------------------------

def analytic_cumulative(cfg, radii_km, slope, n):
    """Analytic N(>=R) for dN/dR ~ R^-q on [radius_min, radius_max], scaled so
    N(>=radius_min) = n."""
    r = np.asarray(radii_km, dtype=float)
    rmin, rmax = cfg.radius_min, cfg.radius_max
    if np.isclose(slope, 1.0):
        num = np.log(rmax / r)
        den = np.log(rmax / rmin)
    else:
        p = 1.0 - slope
        num = r ** p - rmax ** p
        den = rmin ** p - rmax ** p
    return n * num / den


# ---------------------------------------------------------------------------
# chunked top-k cascade sampler
# ---------------------------------------------------------------------------

def sample_cascade_top(cfg, slope, seed):
    """Draw ``cfg.n_cascade`` radii from dN/dR ~ R^-slope in chunks, keeping only
    the ``cfg.keep_top`` largest. Returns them sorted largest -> smallest."""
    rng = np.random.default_rng(seed)
    kept = np.empty(0, dtype=float)
    remaining = int(cfg.n_cascade)
    keep_top = cfg.keep_top
    while remaining > 0:
        m = min(_SAMPLE_CHUNK, remaining)
        remaining -= m
        r = sample_powerlaw(m, cfg.radius_min, cfg.radius_max, float(slope), seed=rng)
        if kept.size:
            r = np.concatenate([kept, r])
        if r.size > keep_top:
            r = np.partition(r, r.size - keep_top)[-keep_top:]
        kept = r
    return np.sort(kept)[::-1]


# ---------------------------------------------------------------------------
# selection
# ---------------------------------------------------------------------------

_CLEAN_COUNT = 1000.0  # beyond this expected count, Poisson scatter << tol, so a
                       # tol-sized excursion there is a fluke, not real structure


def find_cut_rank(cfg, radii_desc, slope):
    """First rank (1-based, into the descending list) at or after which every one
    of the next ``n_keep`` bodies sits within ``cfg.tol`` of the analytic power
    law -- i.e. drop the whole deviant tail.

    The cut is one past the deepest rank (restricted to the genuinely
    small-count regime) whose sampled cumulative count deviates by more than
    ``cfg.tol``. Returns (k_start, ratio); the kept block is ranks
    ``k_start .. k_start + n_keep - 1``.
    """
    counts = np.arange(1, radii_desc.size + 1, dtype=float)
    expected = analytic_cumulative(cfg, radii_desc, slope, cfg.n_cascade)
    ratio = counts / expected

    max_start = radii_desc.size - cfg.n_keep + 1
    if max_start < 1:
        raise ValueError(
            f"retained {radii_desc.size} ranks but need n_keep={cfg.n_keep}; "
            "raise keep_top / n_cascade"
        )

    horizon = int(np.searchsorted(expected, _CLEAN_COUNT))
    horizon = min(horizon, max_start)
    bad = np.abs(ratio[:horizon] - 1.0) > cfg.tol
    bad_idx = np.where(bad)[0]
    k_start = int(bad_idx[-1]) + 2 if bad_idx.size else 1  # +1 past it, +1 to 1-based
    k_start = min(k_start, max_start)
    return k_start, ratio


def build_kept_frame(cfg, radii_desc, slope, k_start, seed):
    """DataFrame for the kept block, matching generate_distribution's columns."""
    block = radii_desc[k_start - 1 : k_start - 1 + cfg.n_keep].copy()
    mass_kg = radii_to_masses(block, density_g_cm3=cfg.density_g_cm3)
    df = pd.DataFrame(
        {
            "particle_id": np.arange(cfg.n_keep),
            "radius_km": block,
            "mass_kg": mass_kg,
            "mass_earth": mass_kg / M_EARTH_KG,
            "mass_solar": mass_kg / M_SUN_KG,
        }
    )
    df.attrs.update(
        n_particles=cfg.n_keep,
        distribution_variable="radius",
        slope=float(slope),
        density_g_cm3=cfg.density_g_cm3,
        seed=seed,
        total_disk_mass_earth=None,
        n_cascade=cfg.n_cascade,
        rank_window=(k_start, k_start + cfg.n_keep - 1),
        radius_min=cfg.radius_min,
        radius_max=cfg.radius_max,
        selection_tol=cfg.tol,
    )
    return df


# ---------------------------------------------------------------------------
# sweep plots
# ---------------------------------------------------------------------------

def _cmap_norm(cfg):
    return plt.get_cmap("viridis"), Normalize(
        vmin=float(cfg.slopes.min()), vmax=float(cfg.slopes.max())
    )


def _footer(cfg):
    return (
        f"cascade N={cfg.n_cascade:g} · keep {cfg.n_keep} · dN/dR ~ R^-q · "
        f"R in [{cfg.radius_min:g}, {cfg.radius_max:g}] km · "
        f"tol={cfg.tol:g} · seed={cfg.seed} (+ slope index)"
    )


def _save(cfg, fig, filename, dpi=200):
    fig.text(0.005, 0.005, _footer(cfg), fontsize=6, color="0.5",
             ha="left", va="bottom", alpha=0.8)
    path = Path(cfg.outdir) / filename
    fig.savefig(path, dpi=dpi, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved: {path}")
    return path


def plot_residual_grid(cfg, per_slope):
    cmap, norm = _cmap_norm(cfg)
    n = len(per_slope)
    ncols = 4
    nrows = int(np.ceil(n / ncols))
    fig, axes = plt.subplots(nrows, ncols, figsize=(3.6 * ncols, 3.0 * nrows),
                             sharex=True, sharey=True)
    axes = np.atleast_1d(axes).ravel()

    for ax, rec in zip(axes, per_slope):
        slope, ratio, k_start = rec["slope"], rec["ratio"], rec["k_start"]
        ranks = np.arange(1, ratio.size + 1)
        ax.axhspan(1 - cfg.tol, 1 + cfg.tol, color="0.85", zorder=0)
        ax.axhline(1.0, color="0.4", lw=0.8)
        ax.plot(ranks, ratio, lw=0, marker="o", ms=2, alpha=0.5,
                color=cmap(norm(slope)))
        ax.axvspan(k_start, k_start + cfg.n_keep - 1, color="tab:green",
                   alpha=0.18, zorder=1)
        ax.axvline(k_start, color="tab:red", lw=1.2)
        ax.set_xscale("log")
        ax.set_xlim(1, max(5000, 3 * (k_start + cfg.n_keep)))
        ax.set_ylim(0.0, 2.0)
        ax.set_title(f"q = {slope:g}   (cut at rank {k_start})", fontsize=10)
        ax.grid(alpha=0.3, which="both")

    for ax in axes[n:]:
        ax.set_visible(False)

    fig.supxlabel("Rank  (number of bodies at least this large)")
    fig.supylabel("sampled  N(≥R)  /  analytic")
    fig.suptitle(
        "Where the finite sample departs from the power law\n"
        "red line: cut rank · green band: the "
        f"{cfg.n_keep} bodies kept",
        fontsize=13,
    )
    fig.tight_layout()
    return _save(cfg, fig, "residual_diagnostic_grid.png")


def plot_selection_cumulative_grid(cfg, per_slope):
    cmap, norm = _cmap_norm(cfg)
    n = len(per_slope)
    ncols = 4
    nrows = int(np.ceil(n / ncols))
    fig, axes = plt.subplots(nrows, ncols, figsize=(3.6 * ncols, 3.0 * nrows))
    axes = np.atleast_1d(axes).ravel()

    for ax, rec in zip(axes, per_slope):
        slope = rec["slope"]
        radii_desc = rec["radii_desc"]
        k_start = rec["k_start"]
        counts = np.arange(1, radii_desc.size + 1)

        lo = k_start
        hi = k_start + cfg.n_keep - 1
        ax.plot(radii_desc[:lo - 1], counts[:lo - 1], lw=0, marker="o", ms=3,
                alpha=0.55, color="tab:red", label="dropped tail")
        ax.plot(radii_desc[lo - 1:hi], counts[lo - 1:hi], lw=0, marker="o",
                ms=3, alpha=0.6, color="tab:green", label="kept")
        ax.plot(radii_desc[hi:], counts[hi:], lw=0, marker="o", ms=2,
                alpha=0.3, color="0.6", label="below block")

        r_hi = radii_desc[lo - 1]
        r_lo = radii_desc[hi - 1]
        r_line = np.logspace(np.log10(0.7 * r_lo), np.log10(cfg.radius_max), 300)
        ax.plot(r_line, analytic_cumulative(cfg, r_line, slope, cfg.n_cascade),
                color="0.2", lw=1.3, label="analytic")

        ax.set_xscale("log")
        ax.set_yscale("log")
        ax.set_xlim(0.8 * r_lo, cfg.radius_max * 1.03)
        ax.set_ylim(0.7, 6 * hi)
        ax.xaxis.set_major_formatter(mticker.ScalarFormatter())
        ax.xaxis.set_minor_formatter(mticker.NullFormatter())
        ax.set_title(f"q = {slope:g}   keep {r_lo:.3g}–{r_hi:.3g} km", fontsize=10)
        ax.grid(alpha=0.3, which="both")

    for ax in axes[n:]:
        ax.set_visible(False)

    axes[0].legend(fontsize=7, loc="lower left")
    fig.supxlabel("Radius (km)")
    fig.supylabel(r"Number of bodies with radius $\geq R$")
    fig.suptitle(
        r"Cascade $dN/dR \propto R^{-q}$: tail dropped, "
        f"{cfg.n_keep}-body block kept (line: analytic)",
        fontsize=13,
    )
    fig.tight_layout()
    return _save(cfg, fig, "selection_cumulative_grid.png")


# ---------------------------------------------------------------------------
# driver
# ---------------------------------------------------------------------------

def parse_args(argv=None):
    p = argparse.ArgumentParser(
        description="Sample a large size cascade per slope and keep the block of "
                    "bodies that preserves the power law."
    )
    p.add_argument("--n-cascade", type=int, default=DEFAULT_N_CASCADE,
                   help=f"bodies in the full cascade (default: {DEFAULT_N_CASCADE:g})")
    p.add_argument("--n-keep", type=int, default=DEFAULT_N_KEEP,
                   help=f"bodies to keep per slope (default: {DEFAULT_N_KEEP})")
    p.add_argument("--radius-min", type=float, default=DEFAULT_RADIUS_MIN_KM,
                   help=f"lower radius truncation, km (default: {DEFAULT_RADIUS_MIN_KM:g})")
    p.add_argument("--radius-max", type=float, default=DEFAULT_RADIUS_MAX_KM,
                   help=f"upper radius truncation, km (default: {DEFAULT_RADIUS_MAX_KM:g})")
    p.add_argument("--slope-min", type=float, default=DEFAULT_SLOPE_MIN)
    p.add_argument("--slope-max", type=float, default=DEFAULT_SLOPE_MAX)
    p.add_argument("--slope-step", type=float, default=DEFAULT_SLOPE_STEP)
    p.add_argument("--tol", type=float, default=DEFAULT_TOL,
                   help="max fractional deviation from the analytic power law "
                        f"tolerated in the kept block (default: {DEFAULT_TOL:g})")
    p.add_argument("--seed", type=int, default=DEFAULT_SEED,
                   help=f"base seed; slope i uses seed+i (default: {DEFAULT_SEED})")
    p.add_argument("--density", type=float, default=DEFAULT_DENSITY_G_CM3,
                   help=f"bulk density, g/cm^3 (default: {DEFAULT_DENSITY_G_CM3:g})")
    p.add_argument("--outdir", required=True, help="output directory")
    p.add_argument("--save-cascade", action="store_true",
                   help="also write the retained top ranks per slope (cascade_top.csv)")
    return p.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)
    slopes = np.arange(args.slope_min, args.slope_max + 1e-9, args.slope_step)
    cfg = Cfg(
        n_cascade=args.n_cascade,
        n_keep=args.n_keep,
        radius_min=args.radius_min,
        radius_max=args.radius_max,
        slopes=slopes,
        density_g_cm3=args.density,
        tol=args.tol,
        seed=args.seed,
        outdir=args.outdir,
        save_cascade=args.save_cascade,
    )
    os.makedirs(cfg.outdir, exist_ok=True)

    per_slope = []
    rows = []
    for i, slope in enumerate(cfg.slopes):
        slope = float(slope)
        seed = cfg.seed + i
        radii_desc = sample_cascade_top(cfg, slope, seed)
        k_start, ratio = find_cut_rank(cfg, radii_desc, slope)
        kept = build_kept_frame(cfg, radii_desc, slope, k_start, seed)

        slope_dir = Path(cfg.outdir) / f"slope_q{slope:g}"
        slope_dir.mkdir(parents=True, exist_ok=True)
        sel_path = slope_dir / "selected.csv"
        kept.to_csv(sel_path, index=False)
        print(f"Saved: {sel_path}")
        if cfg.save_cascade:
            top_path = slope_dir / "cascade_top.csv"
            pd.DataFrame({"radius_km": radii_desc}).to_csv(top_path, index=False)
            print(f"Saved: {top_path}")

        label = (
            f"Cascade q = {slope:g}: kept {cfg.n_keep} bodies "
            f"({kept['radius_km'].min():.3g}–{kept['radius_km'].max():.3g} km) "
            f"of N={cfg.n_cascade:g}"
        )
        plot_per_particle(kept, slope_dir, label=label)
        plot_differential_histogram(kept, slope_dir, slope=slope, label=label)
        plot_count_histograms(kept, slope_dir, label=label)

        per_slope.append(dict(slope=slope, ratio=ratio, k_start=k_start,
                              radii_desc=radii_desc))
        rows.append(dict(
            slope=slope, cut_rank=k_start,
            keep_r_min=float(kept["radius_km"].min()),
            keep_r_max=float(kept["radius_km"].max()),
            cascade_r_max=float(radii_desc[0]),
            frac_of_cascade=cfg.n_keep / cfg.n_cascade,
        ))

    plot_residual_grid(cfg, per_slope)
    plot_selection_cumulative_grid(cfg, per_slope)

    summary = pd.DataFrame(rows)
    summary_path = Path(cfg.outdir) / "selection_summary.csv"
    summary.to_csv(summary_path, index=False)
    print(f"Saved: {summary_path}")
    print("\n" + summary.to_string(index=False))


if __name__ == "__main__":
    main()
