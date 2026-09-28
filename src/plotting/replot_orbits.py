"""
replot_orbits.py

Redraw a run's a_vs_e_initial_final.png / a_vs_i_initial_final.png with your
own axis limits, without rerunning the simulation.

Reads outputs/<name>/figures/data/orbits_initial_final.csv, which
summary_figures.py writes alongside the figures. Runs made before that file
existed can be replotted from their SimulationArchive with --archive (this also
writes the CSV, so later replots don't need the archive).

Any limit left out keeps its automatic value, and either end of a range can
be "auto":

    python src/plotting/replot_orbits.py --run outputs/SS_100MP_100Myr_30xStir \\
        --a 90 115 --e 0 0.1 --i 0 auto

    # older run: rebuild the table from the archive first
    python src/plotting/replot_orbits.py --run outputs/Sim_100MP_100thouyr_dohnanyi \\
        --archive /path/to/Sim_100MP_100thouyr_dohnanyi.bin

    # open a zoom/pan window (needs a display) as well as saving
    python src/plotting/replot_orbits.py --run outputs/SS_100MP_100Myr_30xStir --show

With no limits given the figures are redrawn with the automatic limits, i.e.
exactly as the pipeline makes them. Figures are overwritten in place unless
--suffix is given.
"""

import argparse
import os
import sys
from pathlib import Path

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, "..", "utilities"))
sys.path.insert(0, _HERE)

import matplotlib.pyplot as plt  # noqa: E402
import yaml  # noqa: E402

from provenance import FROZEN_CONFIG_FILENAME, load_run_metadata, stamp_figure  # noqa: E402
from summary_figures import (  # noqa: E402
    ORBIT_PLOTS,
    ORBIT_TABLE_FILENAME,
    build_orbit_figure,
    build_snapshot_table,
    get_first_last_snapshots,
    load_orbit_table,
    save_figure,
    save_orbit_table,
    set_default_provenance,
)

INTERACTIVE_BACKENDS = ("QtAgg", "TkAgg", "GTK4Agg", "GTK3Agg", "MacOSX")


def _limit(value):
    return None if value.lower() in ("auto", "none") else float(value)


def parse_args(argv=None):
    p = argparse.ArgumentParser(
        description="Redraw a run's a-e / a-i initial-final figures with custom axis limits."
    )
    p.add_argument("--run", required=True,
                   help="run output directory, e.g. outputs/<simulation name>")
    p.add_argument("--archive",
                   help="SimulationArchive to rebuild the orbit table from "
                        "(for runs made before the table was saved)")
    lim = dict(nargs=2, type=_limit, metavar=("LO", "HI"))
    p.add_argument("--a", **lim, help="semimajor axis range, AU (both figures)")
    p.add_argument("--e", **lim, help="eccentricity range (a_vs_e figure)")
    p.add_argument("--i", **lim, help="inclination range, deg (a_vs_i figure)")
    p.add_argument("--which", choices=("ae", "ai", "both"), default="both",
                   help="which figure(s) to redraw (default: both)")
    p.add_argument("--suffix", default="",
                   help="append to the output filenames instead of overwriting, "
                        "e.g. --suffix _zoom -> a_vs_e_initial_final_zoom.png")
    p.add_argument("--dpi", type=int, default=None,
                   help="figure dpi (default: the run config's plots.dpi, else 200)")
    p.add_argument("--show", action="store_true",
                   help="also open an interactive window to zoom and pan")
    p.add_argument("--no-stamp", action="store_true",
                   help="leave off the provenance footer")
    return p.parse_args(argv)


def _use_interactive_backend():
    for backend in INTERACTIVE_BACKENDS:
        try:
            plt.switch_backend(backend)
            return backend
        except Exception:
            continue
    raise SystemExit("--show: no interactive matplotlib backend available "
                     "(is there a display?)")


def main(argv=None):
    args = parse_args(argv)
    run_dir = Path(args.run)

    config_path = run_dir / FROZEN_CONFIG_FILENAME
    config = yaml.safe_load(open(config_path)) if config_path.exists() else {}
    simulation_name = (config.get("simulation", {}) or {}).get("name", run_dir.name)
    dpi = args.dpi or int((config.get("plots", {}) or {}).get("dpi", 200))

    table_path = run_dir / "figures" / "data" / ORBIT_TABLE_FILENAME
    if args.archive:
        first, last = get_first_last_snapshots(build_snapshot_table(args.archive))
        save_orbit_table(first, last, run_dir)
    elif table_path.exists():
        first, last = load_orbit_table(table_path)
    else:
        raise SystemExit(
            f"{table_path} not found. This run predates the saved orbit table; "
            "pass --archive <path to its .bin SimulationArchive> to rebuild it."
        )

    metadata = None if args.no_stamp else load_run_metadata(run_dir)
    set_default_provenance(metadata)

    if args.show:
        _use_interactive_backend()

    y_limits = {"ae": args.e, "ai": args.i}
    kinds = ("ae", "ai") if args.which == "both" else (args.which,)
    for kind in kinds:
        fig = build_orbit_figure(first, last, kind, simulation_name,
                                 xlim=args.a, ylim=y_limits[kind])
        filename = ORBIT_PLOTS[kind]["filename"].replace(".png", f"{args.suffix}.png")
        if args.show:
            # save_figure() closes the figure, so save by hand and keep it open
            if metadata:
                stamp_figure(fig, metadata)
            path = run_dir / "figures" / filename
            fig.savefig(path, dpi=dpi, bbox_inches="tight")
            print(f"Saved: {path}")
        else:
            save_figure(fig, run_dir, filename, dpi=dpi)

    if args.show:
        plt.show()


if __name__ == "__main__":
    main()
