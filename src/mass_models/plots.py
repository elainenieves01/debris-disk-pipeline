"""
Plots for a sampled planetesimal mass/size distribution.

Styled to match src/plotting/summary_figures.py: Agg backend, PNG output with
bbox_inches="tight", figures written into a ``figures/`` subdirectory, and a
"Saved: <path>" line printed for each file.
"""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def _footer_text(df):
    """One-line provenance-style footer built from df.attrs."""
    a = getattr(df, "attrs", {}) or {}
    parts = [
        f"N={a.get('n_particles', len(df))}",
        f"var={a.get('distribution_variable', '?')}",
        f"slope={a.get('slope', float('nan')):.4g}",
        f"rho={a.get('density_g_cm3', float('nan')):.3g} g/cm^3",
    ]
    if a.get("total_disk_mass_earth") is not None:
        parts.append(f"M_disk={a['total_disk_mass_earth']:.4g} M_earth")
    if a.get("seed") is not None:
        parts.append(f"seed={a['seed']}")
    return " · ".join(parts)


def _save(fig, output_dir, filename, dpi=200, footer=None):
    if footer:
        fig.text(
            0.005, 0.005, footer,
            fontsize=6, color="0.5", ha="left", va="bottom", alpha=0.8,
        )
    figures_dir = Path(output_dir) / "figures"
    figures_dir.mkdir(parents=True, exist_ok=True)
    save_path = figures_dir / filename
    fig.savefig(save_path, dpi=dpi, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved: {save_path}")
    return save_path


def plot_per_particle(df, output_dir, label="", dpi=200):
    """
    Scatter of every particle's mass and radius, ordered by descending mass.

    Left panel:  mass (Earth masses) vs rank.
    Right panel: radius (km) vs rank.
    """
    ordered = df.sort_values("mass_kg", ascending=False).reset_index(drop=True)
    rank = np.arange(1, len(ordered) + 1)

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    axes[0].scatter(rank, ordered["mass_earth"], s=12)
    axes[0].set_yscale("log")
    axes[0].set_xlabel("Rank (most to least massive)")
    axes[0].set_ylabel("Mass (Earth masses)")
    axes[0].set_title("Individual masses")
    axes[0].grid(alpha=0.3)

    axes[1].scatter(rank, ordered["radius_km"], s=12, color="C1")
    axes[1].set_yscale("log")
    axes[1].set_xlabel("Rank (most to least massive)")
    axes[1].set_ylabel("Radius (km)")
    axes[1].set_title("Individual radii")
    axes[1].grid(alpha=0.3)

    suptitle = "Per-particle masses and sizes"
    if label:
        suptitle = f"{label}\n{suptitle}"
    fig.suptitle(suptitle, fontsize=15)
    fig.tight_layout()

    return _save(fig, output_dir, "dohnanyi_per_particle.png",
                 dpi=dpi, footer=_footer_text(df))


def _differential(values, n_bins=25):
    """Log-spaced differential distribution dN/dx at bin centres."""
    values = np.asarray(values, dtype=float)
    edges = np.logspace(np.log10(values.min()), np.log10(values.max()), n_bins + 1)
    counts, edges = np.histogram(values, bins=edges)
    widths = np.diff(edges)
    centres = np.sqrt(edges[:-1] * edges[1:])
    with np.errstate(divide="ignore", invalid="ignore"):
        density = counts / widths
    keep = counts > 0
    return centres[keep], density[keep], edges


def plot_differential_histogram(df, output_dir, slope, label="", dpi=200):
    """
    Log-log differential distributions dN/dm and dN/dR with the input
    power-law slope overlaid.

    The sampled variable follows dN/dx ~ x^-slope.  Under m ~ R^3 the other
    variable follows an equivalent slope: if mass is sampled with slope q,
    the size slope is 3q - 2 (and vice versa).
    """
    var = (getattr(df, "attrs", {}) or {}).get("distribution_variable", "mass")
    if var == "mass":
        mass_slope = slope
        size_slope = 3.0 * slope - 2.0
    else:
        size_slope = slope
        mass_slope = (slope + 2.0) / 3.0

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    for ax, col, xlabel, ylabel, title, q in (
        (axes[0], "mass_earth", "Mass (Earth masses)", "dN/dm", "Mass spectrum", mass_slope),
        (axes[1], "radius_km", "Radius (km)", "dN/dR", "Size spectrum", size_slope),
    ):
        centres, density, _ = _differential(df[col])
        ax.plot(centres, density, drawstyle="steps-mid", label="sampled")

        # reference power law anchored to the first populated bin
        ref = density[0] * (centres / centres[0]) ** (-q)
        ax.plot(centres, ref, "k--", lw=1, label=f"slope q = {q:.3g}")

        ax.set_xscale("log")
        ax.set_yscale("log")
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.set_title(title)
        ax.grid(alpha=0.3, which="both")
        ax.legend()

    suptitle = "Differential mass / size distribution"
    if label:
        suptitle = f"{label}\n{suptitle}"
    fig.suptitle(suptitle, fontsize=15)
    fig.tight_layout()

    return _save(fig, output_dir, "dohnanyi_differential_histogram.png",
                 dpi=dpi, footer=_footer_text(df))
