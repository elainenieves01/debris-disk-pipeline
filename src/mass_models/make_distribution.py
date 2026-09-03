"""
Command-line entry point for building a Dohnanyi planetesimal
mass/size distribution and plotting the individual particles.

Standalone -- this does NOT feed the simulation. Example:

    python src/mass_models/make_distribution.py \\
        --n 800 --slope 1.8333 --mass-min 1e-6 --mass-max 1e-2 \\
        --total-disk-mass-earth 2.8 --seed 42 --outdir outputs/dohnanyi_demo
"""

import argparse
import os
import sys

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)

from mass_models import generate_distribution, DOHNANYI_MASS_SLOPE
from plots import plot_per_particle, plot_differential_histogram


def parse_args(argv=None):
    p = argparse.ArgumentParser(
        description="Sample a Dohnanyi planetesimal mass/size distribution and plot it."
    )
    p.add_argument("--n", type=int, default=800, help="number of particles")
    p.add_argument(
        "--variable", choices=("mass", "radius"), default="mass",
        help="quantity the power law is drawn in (default: mass)",
    )
    p.add_argument(
        "--slope", type=float, default=DOHNANYI_MASS_SLOPE,
        help="power-law slope q in dN/dx ~ x^-q (default: Dohnanyi 11/6)",
    )
    p.add_argument("--mass-min", type=float, default=1e-6,
                   help="min mass in Earth masses (variable=mass)")
    p.add_argument("--mass-max", type=float, default=1e-2,
                   help="max mass in Earth masses (variable=mass)")
    p.add_argument("--size-min", type=float, default=1.0,
                   help="min radius in km (variable=radius)")
    p.add_argument("--size-max", type=float, default=500.0,
                   help="max radius in km (variable=radius)")
    p.add_argument(
        "--total-disk-mass-earth", type=float, default=2.8,
        help="rescale masses to this total (Earth masses); 0 disables rescaling",
    )
    p.add_argument("--density", type=float, default=1.0, help="bulk density in g/cm^3")
    p.add_argument("--seed", type=int, default=42, help="random seed")
    p.add_argument("--outdir", default=None,
                   help="output directory (default: outputs/dohnanyi_<slope>_<n>)")
    return p.parse_args(argv)


def _summary(df):
    def stats(col, unit):
        v = df[col]
        print(
            f"  {col:12s} [{unit}]  "
            f"min={v.min():.4e}  max={v.max():.4e}  "
            f"mean={v.mean():.4e}  median={v.median():.4e}"
        )

    a = df.attrs
    print("\nDistribution summary")
    print(f"  n_particles           : {a['n_particles']}")
    print(f"  sampled variable      : {a['distribution_variable']}")
    print(f"  slope (q)             : {a['slope']:.6g}")
    print(f"  density               : {a['density_g_cm3']} g/cm^3")
    print(f"  seed                  : {a['seed']}")
    stats("mass_earth", "M_earth")
    stats("radius_km", "km")
    print(f"  realized total disk mass: {df['mass_earth'].sum():.6g} M_earth")


def main(argv=None):
    args = parse_args(argv)

    if args.variable == "mass":
        value_min, value_max = args.mass_min, args.mass_max
    else:
        value_min, value_max = args.size_min, args.size_max

    total = None if args.total_disk_mass_earth in (0, 0.0) else args.total_disk_mass_earth

    df = generate_distribution(
        n_particles=args.n,
        distribution_variable=args.variable,
        value_min=value_min,
        value_max=value_max,
        slope=args.slope,
        density_g_cm3=args.density,
        mass_unit="earth",
        total_disk_mass_earth=total,
        seed=args.seed,
    )

    outdir = args.outdir or os.path.join(
        "outputs", f"dohnanyi_{args.slope:g}_{args.n}"
    )
    os.makedirs(outdir, exist_ok=True)

    csv_path = os.path.join(outdir, "distribution.csv")
    df.to_csv(csv_path, index=False)
    print(f"Saved: {csv_path}")

    label = f"Dohnanyi {args.variable} spectrum (q = {args.slope:g}, N = {args.n})"
    plot_per_particle(df, outdir, label=label)
    plot_differential_histogram(df, outdir, slope=args.slope, label=label)

    _summary(df)
    return df


if __name__ == "__main__":
    main()
