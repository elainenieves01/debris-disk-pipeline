"""
apply_rayleigh_cut.py

Apply the Rayleigh outlier cut to a finished run after the fact: redraw its
summary figures with the outlying massive planetesimals removed, without
rerunning the simulation or touching the original figures.

The outliers are massive planetesimals with final e > N sigma,
sigma = median(e) / sqrt(2 ln 2), once the disk is stirred (median(e) >= 30 x
disk.emax); see src/utilities/rayleigh_cut.py. N is --nsigma, else the run
config's rayleigh_cut.nsigma, else 5 (with the default these are the same
bodies the C_e diagnostic excludes). They are dropped from every snapshot, and
the output goes to a folder named for the factor, so different factors never
overwrite each other:

    outputs/<name>/figures/rayleigh_cut_<N>sigma/*.png   (same names as figures/)
    outputs/<name>/figures/rayleigh_cut_<N>sigma/rms_eccentricity_vs_time_all_vs_cut.png
    outputs/<name>/figures/rayleigh_cut_<N>sigma/excluded_bodies.csv

Usage:

    python src/plotting/apply_rayleigh_cut.py --run outputs/SS_800MP_500kyr_1Mearth_slopeq3.5

    # a different cut factor
    python src/plotting/apply_rayleigh_cut.py --run outputs/<name> --nsigma 4

    # archive stored somewhere other than outputs/<name>/<name>.bin
    python src/plotting/apply_rayleigh_cut.py --run outputs/<name> --archive /path/to/<name>.bin

Needs the run's frozen config.yaml (for the belt, disk.emax and plot
settings). If the disk is not stirred or no body is an outlier, nothing is
written.
"""

import argparse
import os
import sys
from pathlib import Path

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, "..", "utilities"))
sys.path.insert(0, _HERE)

import yaml  # noqa: E402

from provenance import FROZEN_CONFIG_FILENAME, load_run_metadata  # noqa: E402
from summary_figures import (  # noqa: E402
    build_snapshot_table,
    generate_rayleigh_cut_figures,
    set_default_provenance,
)


def parse_args(argv=None):
    p = argparse.ArgumentParser(
        description="Redraw a finished run's summary figures with the Rayleigh-cut "
                    "outliers removed, into figures/rayleigh_cut_<N>sigma/."
    )
    p.add_argument("--run", required=True,
                   help="run output directory, e.g. outputs/<simulation name>")
    p.add_argument("--archive",
                   help="SimulationArchive to read (default: <run>/<run name>.bin)")
    p.add_argument("--nsigma", type=float, default=None,
                   help="cut factor N: exclude bodies with e > N sigma "
                        "(default: the run config's rayleigh_cut.nsigma, else 5)")
    p.add_argument("--dpi", type=int, default=None,
                   help="figure dpi (default: the run config's plots.dpi, else 200)")
    p.add_argument("--no-stamp", action="store_true",
                   help="leave off the provenance footer")
    return p.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)
    run_dir = Path(args.run)

    config_path = run_dir / FROZEN_CONFIG_FILENAME
    if not config_path.exists():
        raise SystemExit(f"{config_path} not found; the cut needs the run's frozen config.")
    config = yaml.safe_load(open(config_path))
    config.setdefault("simulation", {}).setdefault("name", run_dir.name)

    archive = Path(args.archive) if args.archive else run_dir / f"{run_dir.name}.bin"
    if not archive.exists():
        raise SystemExit(f"{archive} not found; pass --archive <path to the .bin>.")

    set_default_provenance(None if args.no_stamp else load_run_metadata(run_dir))
    df = build_snapshot_table(archive)
    excluded = generate_rayleigh_cut_figures(df, config, run_dir, nsigma=args.nsigma,
                                             dpi=args.dpi)
    if excluded:
        print(f"Excluded: {', '.join(excluded)}")
    return excluded


if __name__ == "__main__":
    main()
