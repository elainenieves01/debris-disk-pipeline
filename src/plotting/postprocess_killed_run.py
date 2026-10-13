"""
postprocess_killed_run.py

Make the summary figures and the run report for a run that was stopped before
it finished, from the archive (.bin) it had written so far. The pipeline only
makes these at the end of a run, so a killed run has none.

The report starts with a note that it was generated afterwards because the
simulation was stopped, and how far the archive got. The run's console output
isn't available after the fact, so that section is left out.

    python src/plotting/postprocess_killed_run.py --run outputs/<name>

Run it with the conda env the simulation used (needs the same rebound version
as the archive, e.g. debris_pipeline). Existing figures and the report are
overwritten.
"""

import argparse
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, "..", "utilities"))
sys.path.insert(0, os.path.join(_HERE, "..", "diagnostics"))
sys.path.insert(0, _HERE)

import rebound  # noqa: E402
import yaml  # noqa: E402

from provenance import FROZEN_CONFIG_FILENAME, load_run_metadata  # noqa: E402
from report import generate_report  # noqa: E402
from summary_figures import generate_summary_figures  # noqa: E402


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    p.add_argument("--run", required=True,
                   help="run output directory, e.g. outputs/<simulation name>")
    args = p.parse_args(argv)
    run_dir = Path(args.run)

    config = yaml.safe_load(open(run_dir / FROZEN_CONFIG_FILENAME))
    config.setdefault("simulation", {}).setdefault("name", run_dir.name)
    name = config["simulation"]["name"]
    archive = run_dir / f"{run_dir.name}.bin"

    sa = rebound.Simulationarchive(str(archive))
    t_last, maxtime = sa[-1].t, config["integration"]["maxtime"]
    n_out = len(sa) - 1

    generate_summary_figures(str(archive), config, str(run_dir))

    report_path = run_dir / f"{name}_report.md"
    generate_report(config, load_run_metadata(run_dir)["config"]["source_path"],
                    str(archive), str(report_path))

    note = (
        "> **Generated in post-processing.** This simulation was stopped before "
        f"it finished (t = {t_last:g} of {maxtime:g} after {n_out} outputs), so "
        "the pipeline never made its figures or this report. They were built "
        f"afterwards from the archive on {datetime.now(timezone.utc):%Y-%m-%d} "
        "with `src/plotting/postprocess_killed_run.py`. \"Final\" below means "
        "the last saved output, not the end of the run, and the run's console "
        "output is not included.\n\n"
    )
    text = report_path.read_text()
    head, sep, rest = text.partition("\n\n")
    report_path.write_text(head + "\n\n" + note + rest)
    print(f"Wrote {report_path}")


if __name__ == "__main__":
    main()
