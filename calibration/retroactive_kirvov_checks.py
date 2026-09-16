"""
retroactive_kirvov_checks.py

One-off: compute the Krivov & Booth (2018) diagnostics that
``src/simulation/run_simulation.py`` now emits for every new run --

  * the effective self-stirring constant C_e (Eqs. 9-10, inverted from the
    final-snapshot RMS eccentricity of the massive planetesimals), and
  * the stirrer-coverage condition  N x delta_af >= delta_a
    (delta_af = 8 sqrt(3) h_M a_M, h_M = (M / 3 Mstar)^(1/3))

-- for the runs already sitting in ``outputs/`` that predate those checks, and
append the results to each run's ``*_report.md`` under a clearly-labelled
"Retroactive ..." section.

Re-uses the exact implementations from run_simulation.py
(``compute_effective_stirring_C_e`` / ``compute_stirrer_disk_coverage``) so the
retroactive numbers match what a fresh run would print.

Idempotent: skips a report that already carries the retroactive section.

Usage:
    python calibration/retroactive_kirvov_checks.py           # write into reports
    python calibration/retroactive_kirvov_checks.py --dry-run  # print only
"""

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
for _sub in ("simulation", "config_io", "plotting", "diagnostics", "utilities",
             "mass_models"):
    sys.path.insert(0, str(REPO_ROOT / "src" / _sub))

import rebound  # noqa: E402

from config_utils import read_config  # noqa: E402
from run_simulation import (  # noqa: E402
    compute_effective_stirring_C_e,
    compute_stirrer_disk_coverage,
)

OUTPUTS = REPO_ROOT / "outputs"
CONFIGS = REPO_ROOT / "config"
SECTION_HEADING = "## Retroactive Krivov & Booth (2018) self-stirring diagnostics"

# Scratch / debugging runs -- skipped by default (pass --all to include them).
SKIP_RUNS = {
    "Test",
    "Test2",
    "Testing",
    "delayed_escape_test_new_test",
    "delayed_escape_test_new_test2",
}


def load_config_for(run_dir):
    """Frozen config.yaml in the run dir, else config/<name>.yaml, else None."""
    frozen = run_dir / "config.yaml"
    if frozen.exists():
        return read_config(str(frozen)), f"`{frozen.relative_to(REPO_ROOT)}`"

    named = CONFIGS / f"{run_dir.name}.yaml"
    if named.exists():
        return read_config(str(named)), f"`{named.relative_to(REPO_ROOT)}` (not frozen with the run)"

    return None, None


def first_and_last_snapshots(archive_path):
    """(initial sim, final sim, tmin, tmax, n_snapshots).

    The stirrer-coverage condition is a check on the *initial* setup (the live
    pipeline runs it before integrating), so it is evaluated on the first
    snapshot. C_e depends on the stirred eccentricity, so it is evaluated on
    the last snapshot.
    """
    sa = rebound.Simulationarchive(str(archive_path))
    return sa[0], sa[-1], sa.tmin, sa.tmax, len(sa)


def format_section(run_name, config_note, c_e, cov, tmax):
    lines = [
        SECTION_HEADING,
        "",
        "_Added retroactively by `calibration/retroactive_kirvov_checks.py`; "
        "this run predates the in-pipeline checks in "
        "`src/simulation/run_simulation.py`. The same functions a live run now "
        "uses are applied to the archive: the coverage condition to the first "
        "snapshot (initial conditions), C_e to the last snapshot. "
        f"Config used: {config_note}._",
        "",
    ]

    lines.append("### Effective stirring constant C_e (Eqs. 9-10, final snapshot)")
    lines.append("")
    if c_e is None:
        lines += [
            "Not applicable: this run has no massive planetesimals (or the "
            "final snapshot is at t = 0).",
            "",
        ]
    else:
        lines += [
            f"- Final time: t = {c_e['t']:.6e} yr",
            f"- RMS eccentricity of the {c_e['n_mp']} massive planetesimals: "
            f"{c_e['rms_e']:.6e}",
            f"- Belt geometry: a = {c_e['a_belt']:g} au, da = {c_e['da_belt']:g} au, "
            f"a/da = {c_e['a_over_da']:g}",
            f"- Masses: M_indiv = {c_e['m_indiv']:.6e} Msun, "
            f"M_disc = {c_e['m_disc']:.6e} Msun",
            f"- Mean motion at belt centre: Omega = {c_e['omega']:.6e} yr^-1",
            f"- Implied stirring timescale: T = {c_e['T']:.6e} yr",
            f"- **Effective stirring constant: C_e = {c_e['C_e']:.4f}** "
            f"(Ida & Makino 1993 / Krivov & Booth 2018 reference value: "
            f"{c_e['reference']:g})",
        ]
        if c_e["has_giant_planet"]:
            lines.append(
                "- NOTE: a giant planet is present; the two-population "
                "self-stirring model assumes no external perturber, so C_e is "
                "only indicative."
            )
        if c_e["exceeds_reference"]:
            lines.append(
                f"- **WARNING: C_e = {c_e['C_e']:.4f} >= {c_e['reference']:g}** "
                "-- this run stirs at or above the analytic self-stirring rate."
            )
        lines.append("")

    lines.append(
        "### Stirrer-coverage condition  N x delta_af >= delta_a "
        "(initial snapshot)"
    )
    lines.append("")
    if cov is None:
        lines += [
            "Not applicable: no stirrers (massive planetesimals or giant "
            "planet) fall inside the belt, or the belt width is non-positive.",
            "",
        ]
    else:
        incl = " (incl. giant planet)" if cov["has_giant_planet"] else ""
        lines += [
            f"- Stirrers inside the belt [{cov['amin']:g}, {cov['amax']:g}] au: "
            f"N = {cov['n_stirrers']}{incl}",
            f"- delta_af = 8 sqrt(3) h_M a_M: mean = {cov['delta_af_mean']:.6e} au, "
            f"sum over stirrers = {cov['delta_af_sum']:.6e} au",
            f"- Belt width: delta_a = {cov['delta_a']:.6e} au",
            f"- Coverage ratio (sum delta_af / delta_a) = {cov['ratio']:.3f}",
        ]
        if cov["covered"]:
            lines.append(
                "- **Condition satisfied**: the stirrer feeding zones span the "
                "belt."
            )
        else:
            lines.append(
                f"- **WARNING: condition NOT satisfied** "
                f"(sum delta_af = {cov['delta_af_sum']:.4e} au < "
                f"delta_a = {cov['delta_a']:.4e} au) -- the stirrers do not "
                "dynamically reach across the whole disk width."
            )
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def main():
    dry_run = "--dry-run" in sys.argv[1:]
    include_all = "--all" in sys.argv[1:]

    run_dirs = sorted(
        p.parent for p in OUTPUTS.glob("*/*_report.md")
    )

    for report_path in [d / f"{d.name}_report.md" for d in run_dirs]:
        run_dir = report_path.parent
        run_name = run_dir.name
        archive = run_dir / f"{run_name}.bin"

        print(f"\n=== {run_name} ===")

        if run_name in SKIP_RUNS and not include_all:
            print("  skip: scratch/debug run (pass --all to include).")
            continue

        if not archive.exists():
            print(f"  skip: no archive at {archive.relative_to(REPO_ROOT)}")
            continue

        config, config_note = load_config_for(run_dir)
        if config is None:
            print("  skip: no config.yaml in the run dir and no "
                  f"config/{run_name}.yaml -- cannot define the belt geometry.")
            continue

        existing = report_path.read_text()
        if SECTION_HEADING in existing:
            print("  skip: report already has the retroactive section.")
            continue

        try:
            sim_initial, sim_final, tmin, tmax, n_snap = first_and_last_snapshots(
                archive
            )
        except Exception as error:
            print(f"  skip: could not read archive ({error}).")
            continue

        c_e = compute_effective_stirring_C_e(sim_final, config)
        cov = compute_stirrer_disk_coverage(sim_initial, config)

        if c_e is not None:
            flag = "  <-- WARNING (>= 40)" if c_e["exceeds_reference"] else ""
            print(f"  C_e = {c_e['C_e']:.4f}{flag}")
        else:
            print("  C_e: n/a")
        if cov is not None:
            verdict = "satisfied" if cov["covered"] else "NOT satisfied  <-- WARNING"
            print(f"  coverage: N={cov['n_stirrers']}, "
                  f"sum(delta_af)/delta_a = {cov['ratio']:.3f} -> {verdict}")
        else:
            print("  coverage: n/a")

        section = format_section(run_name, config_note, c_e, cov, tmax)

        if dry_run:
            print("  --- would append ---")
            print("\n".join("  " + ln for ln in section.splitlines()))
            continue

        with report_path.open("a") as fh:
            fh.write("\n" + section)
        print(f"  appended to {report_path.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
