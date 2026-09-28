"""
plot_mass_vs_semimajor_axis.py

Preview of planetesimal mass vs. initial semimajor axis for each slope's
cascade selection, plus a uniform-mass control where every body gets the
single most massive body found across all slopes.

Semimajor axes reproduce ``run_simulation.build_simulation``'s draws exactly
(seed 42; per body a, e, inc, omega, Omega, M in that order), so the preview
shows the locations the runs will actually use. They don't depend on mass, so
every distribution shares the same N locations.

Example:

    python src/mass_models/plot_mass_vs_semimajor_axis.py \\
        --selection-dir src/mass_models/cascade_selection_1000km_drop100_800keep \\
        --config config/SS_800MP_10Myr_slopeq2.5.yaml \\
        --out outputs/mass_vs_semimajor_axis_drop100.png
"""

import argparse
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import yaml

from reference_bodies import add_mass_references

SIM_SEED = 42  # hardcoded in run_simulation.build_simulation
DRAWS_PER_BODY = 6  # a, e, inc, omega, Omega, M


def semimajor_axes(n, amin, amax, emax, imax, seed=SIM_SEED):
    """Initial a (AU) of each planetesimal, as run_simulation draws them."""
    rng = np.random.default_rng(seed)
    a = np.empty(n)
    for i in range(n):
        a[i] = rng.uniform(amin, amax)
        rng.uniform(0.0, emax)
        rng.uniform(0.0, imax)
        rng.uniform(0, 2 * np.pi, size=3)
    return a


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__.split("\n\n")[1])
    p.add_argument("--selection-dir", required=True,
                   help="directory holding slope_q<q>/selected.csv")
    p.add_argument("--config", required=True,
                   help="run config supplying disk.amin/amax/emax/imax_deg")
    p.add_argument("--out", required=True, help="output PNG path")
    args = p.parse_args(argv)

    sel_dir = Path(args.selection_dir)
    slope_dirs = sorted(sel_dir.glob("slope_q*"), key=lambda d: float(d.name[7:]))
    sets = {float(d.name[7:]): pd.read_csv(d / "selected.csv") for d in slope_dirs}
    n = {len(df) for df in sets.values()}
    if len(n) != 1:
        raise ValueError(f"selections have differing sizes: {sorted(n)}")
    n = n.pop()

    disk = yaml.safe_load(open(args.config))["disk"]
    a = semimajor_axes(n, float(disk["amin"]), float(disk["amax"]),
                       float(disk["emax"]), np.radians(float(disk["imax_deg"])))

    q_max, df_max = max(sets.items(), key=lambda kv: kv[1]["mass_earth"].max())
    i_max = int(df_max["mass_earth"].idxmax())
    m_max = float(df_max.loc[i_max, "mass_earth"])
    r_max = float(df_max.loc[i_max, "radius_km"])

    # Rescaled selections (--total-mass-earth) keep radii as drawn, so a radius
    # label would be misleading there; show the disk mass instead.
    summary_path = sel_dir / "selection_summary.csv"
    summary = pd.read_csv(summary_path) if summary_path.exists() else None
    rescaled = (summary is not None and "mass_scale" in summary
                and not np.allclose(summary["mass_scale"], 1.0))
    if rescaled:
        disk = f"slopes rescaled to M$_{{disk}}$ = {summary['total_mass_earth'].iloc[0]:g} M$_\\oplus$"
        max_label = f"{m_max:.4g} M$_\\oplus$"
    else:
        disk = None
        max_label = f"{m_max:.4g} M$_\\oplus$, R = {r_max:.4g} km"

    fig, ax = plt.subplots(figsize=(8, 6))
    for q, df in sets.items():
        ax.scatter(a, df["mass_earth"], s=10, alpha=0.65, label=f"q = {q:g}")
    ax.scatter(a, np.full(n, m_max), s=6, marker="s", color="tab:red",
               alpha=0.7, label=f"uniform max-mass ({n} bodies)")
    ax.scatter(a[i_max], m_max, s=300, marker="*", color="gold",
               edgecolor="k", zorder=5, label=f"global max source (q={q_max:g})")

    ax.set_yscale("log")
    add_mass_references(ax)
    ax.set_xlabel("Semimajor axis (AU)")
    ax.set_ylabel("Mass (Earth masses)")
    ax.set_title(
        "Planetesimal mass vs. semimajor axis"
        + (f" ({disk})" if disk else "") + "\n"
        f"{len(sets)} slope distributions + uniform max-mass "
        f"({max_label}), same {n} locations"
    )
    ax.grid(alpha=0.3)
    ax.legend(fontsize=8, loc="center left", bbox_to_anchor=(1.02, 0.5))
    fig.text(0.005, 0.005, f"{sel_dir} · a from run_simulation seed {SIM_SEED}",
             fontsize=6, color="0.5")

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out, dpi=200, bbox_inches="tight")
    print(f"Saved: {out}")
    print(f"Global max: {m_max:.6e} M_earth, R = {r_max:.4f} km "
          f"(slope_q{q_max:g}/selected.csv particle_id {i_max}); "
          f"uniform total = {m_max * n:.6e} M_earth")


if __name__ == "__main__":
    main()
