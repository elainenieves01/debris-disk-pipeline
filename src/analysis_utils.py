"""
analysis_utils.py

Purpose
-------
Utilities for analyzing snapshot tables created by snapshot_inspector.py.

This file does NOT make plots.
It only computes useful quantities from the inspected simulation data.

Core idea
---------
Instead of starting from mysterious arrays like aps, eps, ips, we start from
a readable table:

snapshot_table.csv

Then we compute:
- particle counts over time
- survival fractions
- mean/median orbital elements
- RMS eccentricity, inclination, and semimajor axis
- final snapshot summaries

This makes the analysis easier to inspect, debug, and trust.
"""

from pathlib import Path

import numpy as np
import pandas as pd


def load_snapshot_table(path):
    """
    Load a snapshot table from CSV or Parquet.

    Parameters
    ----------
    path : str or Path
        Path to snapshot_table.csv or snapshot_table.parquet.

    Returns
    -------
    pandas.DataFrame
        Snapshot table.
    """

    path = Path(path)

    if not path.exists():
        raise FileNotFoundError(f"Could not find snapshot table: {path}")

    if path.suffix == ".csv":
        df = pd.read_csv(path)

    elif path.suffix == ".parquet":
        df = pd.read_parquet(path)

    else:
        raise ValueError(
            "Unsupported file type. Use .csv or .parquet."
        )

    return df


def get_role_counts(df):
    """
    Count how many particles of each role exist in each snapshot.

    Returns
    -------
    pandas.DataFrame
        Columns: snapshot, time_yr, role, count
    """

    counts = (
        df.groupby(["snapshot", "time_yr", "role"])
        .size()
        .reset_index(name="count")
    )

    return counts


def get_particle_counts(df):
    """
    Count total number of particles in each snapshot.

    Returns
    -------
    pandas.DataFrame
        Columns: snapshot, time_yr, N_particles
    """

    counts = (
        df.groupby(["snapshot", "time_yr"])
        .size()
        .reset_index(name="N_particles")
    )

    return counts


def compute_survival_fraction(df, role):
    """
    Compute survival fraction for one particle role.

    Example roles:
    - "test_particle"
    - "dwarf_planet"
    - "giant_planet"

    Survival fraction is:

        N_current / N_initial

    Parameters
    ----------
    df : pandas.DataFrame
        Snapshot table.

    role : str
        Particle role to analyze.

    Returns
    -------
    pandas.DataFrame
        Columns: snapshot, time_yr, role, N, survival_fraction
    """

    subset = df[df["role"] == role].copy()

    counts = (
        subset.groupby(["snapshot", "time_yr"])
        .size()
        .reset_index(name="N")
    )

    if len(counts) == 0:
        return pd.DataFrame(
            columns=["snapshot", "time_yr", "role", "N", "survival_fraction"]
        )

    N_initial = counts["N"].iloc[0]

    counts["role"] = role
    counts["survival_fraction"] = counts["N"] / N_initial

    return counts


def summarize_orbital_elements(df, role):
    """
    Compute mean, median, and RMS orbital elements for a role.

    Parameters
    ----------
    df : pandas.DataFrame
        Snapshot table.

    role : str
        Particle role to analyze.

    Returns
    -------
    pandas.DataFrame
        One row per snapshot.
    """

    subset = df[df["role"] == role].copy()

    if len(subset) == 0:
        return pd.DataFrame()

    grouped = subset.groupby(["snapshot", "time_yr"])

    summary = grouped.agg(
        N=("particle_index", "count"),

        a_mean_AU=("a_AU", "mean"),
        a_median_AU=("a_AU", "median"),
        a_std_AU=("a_AU", "std"),

        e_mean=("e", "mean"),
        e_median=("e", "median"),
        e_std=("e", "std"),

        inc_mean_deg=("inc_deg", "mean"),
        inc_median_deg=("inc_deg", "median"),
        inc_std_deg=("inc_deg", "std"),
    ).reset_index()

    # RMS means sqrt(mean(x^2)).
    rms = grouped.agg(
        a_rms_AU=("a_AU", lambda x: np.sqrt(np.nanmean(x**2))),
        e_rms=("e", lambda x: np.sqrt(np.nanmean(x**2))),
        inc_rms_deg=("inc_deg", lambda x: np.sqrt(np.nanmean(x**2))),
    ).reset_index()

    summary = summary.merge(rms, on=["snapshot", "time_yr"])

    summary["role"] = role

    return summary


def summarize_all_roles(df):
    """
    Compute orbital summaries for all roles except the star.

    Returns
    -------
    pandas.DataFrame
        Combined orbital summary table.
    """

    roles = sorted(df["role"].dropna().unique())

    summaries = []

    for role in roles:
        if role == "star":
            continue

        role_summary = summarize_orbital_elements(df, role)

        if len(role_summary) > 0:
            summaries.append(role_summary)

    if len(summaries) == 0:
        return pd.DataFrame()

    return pd.concat(summaries, ignore_index=True)


def get_final_snapshot(df):
    """
    Return only the final snapshot.

    Parameters
    ----------
    df : pandas.DataFrame

    Returns
    -------
    pandas.DataFrame
        Rows from the final snapshot.
    """

    final_snapshot = df["snapshot"].max()

    return df[df["snapshot"] == final_snapshot].copy()


def summarize_final_snapshot(df):
    """
    Summarize the final snapshot by role.

    Returns
    -------
    pandas.DataFrame
    """

    final_df = get_final_snapshot(df)

    summary = (
        final_df.groupby("role")
        .agg(
            N=("particle_index", "count"),
            a_mean_AU=("a_AU", "mean"),
            e_mean=("e", "mean"),
            inc_mean_deg=("inc_deg", "mean"),
            a_median_AU=("a_AU", "median"),
            e_median=("e", "median"),
            inc_median_deg=("inc_deg", "median"),
        )
        .reset_index()
    )

    return summary


def save_analysis_tables(df, output_dir):
    """
    Save common analysis products to CSV files.

    Parameters
    ----------
    df : pandas.DataFrame
        Snapshot table.

    output_dir : str or Path
        Directory where analysis outputs should be saved.
    """

    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    particle_counts = get_particle_counts(df)
    role_counts = get_role_counts(df)
    orbital_summary = summarize_all_roles(df)
    final_summary = summarize_final_snapshot(df)

    particle_counts.to_csv(output_dir / "particle_counts.csv", index=False)
    role_counts.to_csv(output_dir / "role_counts.csv", index=False)
    orbital_summary.to_csv(output_dir / "orbital_summary.csv", index=False)
    final_summary.to_csv(output_dir / "final_snapshot_summary.csv", index=False)

    # Survival fractions for the main evolving populations.
    for role in ["test_particle", "dwarf_planet"]:
        survival = compute_survival_fraction(df, role)

        if len(survival) > 0:
            survival.to_csv(
                output_dir / f"{role}_survival_fraction.csv",
                index=False,
            )

    print(f"Saved analysis tables to: {output_dir}")