"""
snapshot_inspector.py

Purpose
-------
Inspect a REBOUND SimulationArchive and save a table showing what is inside
each snapshot.

This script helps answer:
- How many particles are in each snapshot?
- What are their indices?
- What are their masses, positions, and velocities?
- What are their orbital elements?
- Are they stars, giant planets, dwarf planets, or test particles?
- Do REBOUND hashes survive inside the archive?

Outputs
-------
1. snapshot_table.csv
2. snapshot_table.parquet, optional
3. snapshot_summary.txt

Default particle-index assumption
---------------------------------
If hashes are unavailable, this script assumes:

index 0             = star
index 1             = giant planet
index 2 to 2+n_dp-1 = dwarf planets
remaining particles = test particles

Future-proof hash convention
----------------------------
If particles have hashes like:

star
planet_0
disk_0_dp_000
disk_0_tp_000

then the script will classify particles using hashes instead.
"""

import argparse
from pathlib import Path
import sys

import numpy as np
import pandas as pd
import rebound


def safe_hash_to_string(particle):
    """
    Try to convert a REBOUND particle hash into a readable string.

    REBOUND hashes can behave differently depending on the version.
    This function is intentionally defensive.

    Returns
    -------
    str or None
        A readable hash string if available, otherwise None.
    """

    try:
        h = particle.hash
    except Exception:
        return None

    if h is None:
        return None

    try:
        h_str = str(h)
    except Exception:
        return None

    # Some particles may have a default hash like "c_uint(0)".
    # That is not useful as a physical label.
    if h_str in ["0", "c_uint(0)", "None"]:
        return None

    return h_str


def classify_from_hash(hash_name):
    """
    Classify a particle using its hash name.

    Parameters
    ----------
    hash_name : str or None
        Particle hash converted to a string.

    Returns
    -------
    tuple
        role, disk_id, object_id
    """

    if hash_name is None:
        return None, None, None

    if hash_name == "star":
        return "star", None, "star"

    if hash_name.startswith("planet_"):
        return "giant_planet", None, hash_name

    if hash_name.startswith("disk_") and "_dp_" in hash_name:
        parts = hash_name.split("_")
        disk_id = f"disk_{parts[1]}"
        return "dwarf_planet", disk_id, hash_name

    if hash_name.startswith("disk_") and "_tp_" in hash_name:
        parts = hash_name.split("_")
        disk_id = f"disk_{parts[1]}"
        return "test_particle", disk_id, hash_name

    return "unknown", None, hash_name


def classify_from_index(index, n_giant_planets, n_dp):
    """
    Classify a particle using the old index-based assumption.

    Parameters
    ----------
    index : int
        Particle index inside the snapshot.

    n_giant_planets : int
        Number of giant planets expected.

    n_dp : int
        Number of dwarf planets expected.

    Returns
    -------
    tuple
        role, disk_id, object_id
    """

    if index == 0:
        return "star", None, "star"

    first_planet = 1
    last_planet = first_planet + n_giant_planets

    first_dp = last_planet
    last_dp = first_dp + n_dp

    if first_planet <= index < last_planet:
        planet_number = index - first_planet
        return "giant_planet", None, f"planet_{planet_number}"

    if first_dp <= index < last_dp:
        dp_number = index - first_dp
        return "dwarf_planet", "disk_0", f"disk_0_dp_{dp_number:03d}"

    tp_number = index - last_dp
    return "test_particle", "disk_0", f"disk_0_tp_{tp_number:03d}"


def get_particle_classification(particle, index, n_giant_planets, n_dp):
    """
    Classify a particle.

    First tries hash-based classification.
    If no useful hash exists, falls back to index-based classification.
    """

    hash_name = safe_hash_to_string(particle)

    role, disk_id, object_id = classify_from_hash(hash_name)

    if role is not None:
        classification_method = "hash"
        return role, disk_id, object_id, hash_name, classification_method

    role, disk_id, object_id = classify_from_index(
        index=index,
        n_giant_planets=n_giant_planets,
        n_dp=n_dp,
    )

    classification_method = "index"
    return role, disk_id, object_id, hash_name, classification_method


def get_orbital_elements(sim, particle_index):
    """
    Get orbital elements for one particle relative to the star.

    The star itself does not have meaningful orbital elements around itself,
    so this returns NaN for index 0.

    Returns
    -------
    dict
        Orbital elements.
    """

    if particle_index == 0:
        return {
            "a_AU": np.nan,
            "e": np.nan,
            "inc_rad": np.nan,
            "inc_deg": np.nan,
            "Omega_rad": np.nan,
            "omega_rad": np.nan,
            "f_rad": np.nan,
        }

    try:
        orbit = sim.particles[particle_index].orbit(primary=sim.particles[0])

        return {
            "a_AU": orbit.a,
            "e": orbit.e,
            "inc_rad": orbit.inc,
            "inc_deg": np.degrees(orbit.inc),
            "Omega_rad": orbit.Omega,
            "omega_rad": orbit.omega,
            "f_rad": orbit.f,
        }

    except Exception:
        return {
            "a_AU": np.nan,
            "e": np.nan,
            "inc_rad": np.nan,
            "inc_deg": np.nan,
            "Omega_rad": np.nan,
            "omega_rad": np.nan,
            "f_rad": np.nan,
        }


def inspect_archive(archive_path, n_giant_planets=1, n_dp=0):
    """
    Inspect every snapshot in a REBOUND SimulationArchive.

    Parameters
    ----------
    archive_path : str or Path
        Path to the SimulationArchive .bin file.

    n_giant_planets : int
        Number of giant planets expected if using index classification.

    n_dp : int
        Number of dwarf planets expected if using index classification.

    Returns
    -------
    pandas.DataFrame
        One row per particle per snapshot.
    """

    archive_path = Path(archive_path)

    if not archive_path.exists():
        raise FileNotFoundError(f"Could not find archive: {archive_path}")

    sa = rebound.Simulationarchive(str(archive_path))

    rows = []

    print(f"Loaded archive: {archive_path}")
    print(f"Number of snapshots: {len(sa)}")

    for snapshot_index, sim in enumerate(sa):
        print(
            f"Reading snapshot {snapshot_index + 1}/{len(sa)} "
            f"| t = {sim.t:.6e} | N = {sim.N}"
        )

        for particle_index, particle in enumerate(sim.particles):
            role, disk_id, object_id, hash_name, classification_method = (
                get_particle_classification(
                    particle=particle,
                    index=particle_index,
                    n_giant_planets=n_giant_planets,
                    n_dp=n_dp,
                )
            )

            elements = get_orbital_elements(sim, particle_index)

            row = {
                "snapshot": snapshot_index,
                "time_yr": sim.t,
                "N_particles_in_snapshot": sim.N,

                "particle_index": particle_index,
                "hash": hash_name,
                "classification_method": classification_method,

                "role": role,
                "disk_id": disk_id,
                "object_id": object_id,

                "mass_Msun": particle.m,

                "x_AU": particle.x,
                "y_AU": particle.y,
                "z_AU": particle.z,

                "vx_AU_per_yr": particle.vx,
                "vy_AU_per_yr": particle.vy,
                "vz_AU_per_yr": particle.vz,

                "a_AU": elements["a_AU"],
                "e": elements["e"],
                "inc_rad": elements["inc_rad"],
                "inc_deg": elements["inc_deg"],
                "Omega_rad": elements["Omega_rad"],
                "omega_rad": elements["omega_rad"],
                "f_rad": elements["f_rad"],
            }

            rows.append(row)

    return pd.DataFrame(rows)


def write_summary(df, output_path):
    """
    Write a plain-English summary of the inspected archive.

    This is useful when you want a quick sanity check without opening the CSV.
    """

    output_path = Path(output_path)

    lines = []

    lines.append("Snapshot Inspection Summary")
    lines.append("===========================")
    lines.append("")
    lines.append(f"Total rows: {len(df)}")
    lines.append(f"Number of snapshots: {df['snapshot'].nunique()}")
    lines.append("")

    lines.append("Particles per snapshot:")
    particle_counts = df.groupby("snapshot")["particle_index"].count()
    for snapshot, count in particle_counts.items():
        lines.append(f"  Snapshot {snapshot}: {count} particles")

    lines.append("")
    lines.append("Role counts by snapshot:")
    role_counts = (
        df.groupby(["snapshot", "role"])
        .size()
        .reset_index(name="count")
    )

    for snapshot in sorted(df["snapshot"].unique()):
        lines.append(f"")
        lines.append(f"  Snapshot {snapshot}:")
        subset = role_counts[role_counts["snapshot"] == snapshot]

        for _, row in subset.iterrows():
            lines.append(f"    {row['role']}: {row['count']}")

    lines.append("")
    lines.append("Classification methods used:")
    method_counts = df["classification_method"].value_counts(dropna=False)
    for method, count in method_counts.items():
        lines.append(f"  {method}: {count}")

    output_path.write_text("\n".join(lines))

    print(f"Saved summary to: {output_path}")


def save_outputs(df, output_base):
    """
    Save CSV, Parquet, and summary files.

    Parameters
    ----------
    df : pandas.DataFrame
        Inspection table.

    output_base : str or Path
        Base output name without extension.
        Example: outputs/snapshot_table
    """

    output_base = Path(output_base)
    output_base.parent.mkdir(parents=True, exist_ok=True)

    csv_path = output_base.with_suffix(".csv")
    parquet_path = output_base.with_suffix(".parquet")
    summary_path = output_base.with_name(output_base.name + "_summary.txt")

    df.to_csv(csv_path, index=False)
    print(f"Saved CSV to: {csv_path}")

    try:
        df.to_parquet(parquet_path, index=False)
        print(f"Saved Parquet to: {parquet_path}")
    except Exception as error:
        print("Could not save Parquet file.")
        print("This is usually because pyarrow or fastparquet is not installed.")
        print(f"Error: {error}")

    write_summary(df, summary_path)


def main():
    """
    Command-line entry point.
    """

    parser = argparse.ArgumentParser(
        description="Inspect a REBOUND SimulationArchive and save its contents to a table."
    )

    parser.add_argument(
        "archive_path",
        type=str,
        help="Path to the REBOUND SimulationArchive .bin file.",
    )

    parser.add_argument(
        "--n_giant_planets",
        type=int,
        default=1,
        help="Number of giant planets expected if using index-based classification.",
    )

    parser.add_argument(
        "--n_dp",
        type=int,
        default=0,
        help="Number of dwarf planets expected if using index-based classification.",
    )

    parser.add_argument(
        "--output_base",
        type=str,
        default="snapshot_table",
        help="Base output path without extension. Example: outputs/snapshot_table",
    )

    args = parser.parse_args()

    df = inspect_archive(
        archive_path=args.archive_path,
        n_giant_planets=args.n_giant_planets,
        n_dp=args.n_dp,
    )

    save_outputs(df, args.output_base)

    print("")
    print("Done.")
    print(f"Final table shape: {df.shape[0]} rows x {df.shape[1]} columns")


if __name__ == "__main__":
    main()
