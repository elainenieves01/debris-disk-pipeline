"""
plot_publication_figures.py

Purpose
-------
Generate publication-ready dynamical evolution plots from snapshot_table.csv.

Input
-----
A snapshot table created by snapshot_inspector.py.

Outputs
-------
Separate PNG and PDF figures for:
- RMS eccentricity evolution
- RMS inclination evolution
- semimajor axis evolution
- mean/median a-e evolution
- mean/median a-i evolution
- mean eccentricity evolution
- mean inclination evolution
- survival fraction

Example
-------
python src/plot_publication_figures.py \
    outputs/HD216435/snapshot_table.csv \
    --output_dir outputs/HD216435/figures
"""

import argparse
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


ROLE_LABELS = {
    "dwarf_planet": "Dwarf planets",
    "test_particle": "Test particles",
    "giant_planet": "Giant planet",
}

ROLE_COLORS = {
    "dwarf_planet": "tab:blue",
    "test_particle": "tab:orange",
    "giant_planet": "tab:green",
}


def set_publication_style():
    """
    Set consistent plot styling.
    """

    plt.rcParams.update({
        "figure.figsize": (7.0, 5.0),
        "figure.dpi": 150,
        "savefig.dpi": 300,
        "font.size": 12,
        "axes.labelsize": 13,
        "axes.titlesize": 14,
        "legend.fontsize": 11,
        "xtick.labelsize": 11,
        "ytick.labelsize": 11,
        "axes.linewidth": 1.2,
        "lines.linewidth": 2.2,
        "lines.markersize": 4.5,
        "xtick.direction": "in",
        "ytick.direction": "in",
        "xtick.top": True,
        "ytick.right": True,
    })


def load_snapshot_table(path):
    """
    Load CSV or Parquet snapshot table.
    """

    path = Path(path)

    if path.suffix == ".csv":
        return pd.read_csv(path)

    if path.suffix == ".parquet":
        return pd.read_parquet(path)

    raise ValueError("Input must be .csv or .parquet")


def save_figure(fig, output_dir, name):
    """
    Save figure as both PNG and PDF.
    """

    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    png_path = output_dir / f"{name}.png"
    pdf_path = output_dir / f"{name}.pdf"

    fig.savefig(png_path, bbox_inches="tight")
    fig.savefig(pdf_path, bbox_inches="tight")

    print(f"Saved: {png_path}")
    print(f"Saved: {pdf_path}")

    plt.close(fig)


def compute_summary(df):
    """
    Compute mean, median, and RMS quantities by snapshot and role.
    """

    usable = df[df["role"] != "star"].copy()

    grouped = usable.groupby(["snapshot", "time_yr", "role"])

    summary = grouped.agg(
        N=("particle_index", "count"),

        a_mean_AU=("a_AU", "mean"),
        a_median_AU=("a_AU", "median"),

        e_mean=("e", "mean"),
        e_median=("e", "median"),

        inc_mean_deg=("inc_deg", "mean"),
        inc_median_deg=("inc_deg", "median"),
    ).reset_index()

    rms = grouped.agg(
        e_rms=("e", lambda x: np.sqrt(np.nanmean(x**2))),
        inc_rms_deg=("inc_deg", lambda x: np.sqrt(np.nanmean(x**2))),
        a_rms_AU=("a_AU", lambda x: np.sqrt(np.nanmean(x**2))),
    ).reset_index()

    return summary.merge(rms, on=["snapshot", "time_yr", "role"])


def compute_survival(df):
    """
    Compute survival fraction by role, including zero after all particles
    of that role have escaped.
    """

    all_snapshots = (
        df[["snapshot", "time_yr"]]
        .drop_duplicates()
        .sort_values("snapshot")
    )

    rows = []

    for role in ["dwarf_planet", "test_particle", "giant_planet"]:
        sub = df[df["role"] == role]

        if len(sub) == 0:
            continue

        counts = (
            sub.groupby(["snapshot", "time_yr"])
            .size()
            .reset_index(name="N")
        )

        counts = all_snapshots.merge(
            counts,
            on=["snapshot", "time_yr"],
            how="left",
        )

        counts["N"] = counts["N"].fillna(0)

        N_initial = counts["N"].iloc[0]

        if N_initial == 0:
            continue

        counts["role"] = role
        counts["survival_fraction"] = counts["N"] / N_initial

        rows.append(counts)

    if not rows:
        return pd.DataFrame()

    return pd.concat(rows, ignore_index=True)


def plot_single_role_time(summary, role, ycol, ylabel, title, output_dir, name):
    """
    Plot one role and one quantity versus time.
    """

    sub = summary[summary["role"] == role]

    if len(sub) == 0:
        print(f"Skipping {name}: no data for {role}")
        return

    fig, ax = plt.subplots()

    ax.plot(
        sub["time_yr"],
        sub[ycol],
        marker="o",
        color=ROLE_COLORS.get(role),
        label=ROLE_LABELS.get(role, role),
    )

    ax.set_xlabel("Time [yr]")
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.grid(alpha=0.25)
    ax.legend(frameon=False)

    save_figure(fig, output_dir, name)


def plot_two_role_time(summary, roles, ycol, ylabel, title, output_dir, name):
    """
    Plot two or more roles and one quantity versus time.
    """

    fig, ax = plt.subplots()

    plotted = False

    for role in roles:
        sub = summary[summary["role"] == role]

        if len(sub) == 0:
            continue

        ax.plot(
            sub["time_yr"],
            sub[ycol],
            marker="o",
            color=ROLE_COLORS.get(role),
            label=ROLE_LABELS.get(role, role),
        )

        plotted = True

    if not plotted:
        plt.close(fig)
        print(f"Skipping {name}: no matching roles")
        return

    ax.set_xlabel("Time [yr]")
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.grid(alpha=0.25)
    ax.legend(frameon=False)

    save_figure(fig, output_dir, name)


def plot_a_mean_median_single(summary, role, output_dir, name):
    """
    Plot mean and median semimajor axis versus time for one role.
    """

    sub = summary[summary["role"] == role]

    if len(sub) == 0:
        print(f"Skipping {name}: no data for {role}")
        return

    label = ROLE_LABELS.get(role, role)
    color = ROLE_COLORS.get(role)

    fig, ax = plt.subplots()

    ax.plot(
        sub["time_yr"],
        sub["a_mean_AU"],
        marker="o",
        linestyle="-",
        color=color,
        label=f"{label} mean",
    )

    ax.plot(
        sub["time_yr"],
        sub["a_median_AU"],
        marker="s",
        linestyle="--",
        color=color,
        label=f"{label} median",
    )

    ax.set_xlabel("Time [yr]")
    ax.set_ylabel("Semimajor axis [AU]")
    ax.set_title(f"{label} semimajor axis evolution")
    ax.grid(alpha=0.25)
    ax.legend(frameon=False)

    save_figure(fig, output_dir, name)


def plot_a_mean_median_combined(summary, output_dir):
    """
    Plot mean and median semimajor axis versus time for DP, TP, and GP.
    """

    fig, ax = plt.subplots()

    plotted = False

    for role in ["dwarf_planet", "test_particle", "giant_planet"]:
        sub = summary[summary["role"] == role]

        if len(sub) == 0:
            continue

        label = ROLE_LABELS.get(role, role)
        color = ROLE_COLORS.get(role)

        ax.plot(
            sub["time_yr"],
            sub["a_mean_AU"],
            linestyle="-",
            marker="o",
            color=color,
            label=f"{label} mean",
        )

        ax.plot(
            sub["time_yr"],
            sub["a_median_AU"],
            linestyle="--",
            marker="s",
            color=color,
            label=f"{label} median",
        )

        plotted = True

    if not plotted:
        plt.close(fig)
        print("Skipping combined semimajor axis plot: no data")
        return

    ax.set_xlabel("Time [yr]")
    ax.set_ylabel("Semimajor axis [AU]")
    ax.set_title("Semimajor axis evolution")
    ax.grid(alpha=0.25)
    ax.legend(frameon=False)

    save_figure(fig, output_dir, "semimajor_axis_mean_median_combined")


def plot_ae_mean_median(summary, output_dir):
    """
    Plot mean and median semimajor axis versus eccentricity.

    Each point is one snapshot summary.
    """

    fig, ax = plt.subplots()

    plotted = False

    for role in ["dwarf_planet", "test_particle"]:
        sub = summary[summary["role"] == role]

        if len(sub) == 0:
            continue

        label = ROLE_LABELS.get(role, role)
        color = ROLE_COLORS.get(role)

        ax.plot(
            sub["a_mean_AU"],
            sub["e_mean"],
            linestyle="-",
            marker="o",
            color=color,
            label=f"{label} mean",
        )

        ax.plot(
            sub["a_median_AU"],
            sub["e_median"],
            linestyle="--",
            marker="s",
            color=color,
            label=f"{label} median",
        )

        plotted = True

    if not plotted:
        plt.close(fig)
        print("Skipping a-e plot: no DP or TP data")
        return

    ax.set_xlabel("Semimajor axis [AU]")
    ax.set_ylabel("Eccentricity")
    ax.set_title("Mean and median evolution in a-e space")
    ax.grid(alpha=0.25)
    ax.legend(frameon=False)

    save_figure(fig, output_dir, "ae_mean_median_dp_tp")


def plot_ai_mean_median(summary, output_dir):
    """
    Plot mean and median semimajor axis versus inclination.

    Each point is one snapshot summary.
    """

    fig, ax = plt.subplots()

    plotted = False

    for role in ["dwarf_planet", "test_particle"]:
        sub = summary[summary["role"] == role]

        if len(sub) == 0:
            continue

        label = ROLE_LABELS.get(role, role)
        color = ROLE_COLORS.get(role)

        ax.plot(
            sub["a_mean_AU"],
            sub["inc_mean_deg"],
            linestyle="-",
            marker="o",
            color=color,
            label=f"{label} mean",
        )

        ax.plot(
            sub["a_median_AU"],
            sub["inc_median_deg"],
            linestyle="--",
            marker="s",
            color=color,
            label=f"{label} median",
        )

        plotted = True

    if not plotted:
        plt.close(fig)
        print("Skipping a-i plot: no DP or TP data")
        return

    ax.set_xlabel("Semimajor axis [AU]")
    ax.set_ylabel("Inclination [deg]")
    ax.set_title("Mean and median evolution in a-i space")
    ax.grid(alpha=0.25)
    ax.legend(frameon=False)

    save_figure(fig, output_dir, "ai_mean_median_dp_tp")


def plot_survival(survival, output_dir):
    """
    Plot survival fraction versus time.
    """

    if len(survival) == 0:
        print("Skipping survival plot: no survival data")
        return

    fig, ax = plt.subplots()

    for role in ["dwarf_planet", "test_particle", "giant_planet"]:
        sub = survival[survival["role"] == role]

        if len(sub) == 0:
            continue

        ax.plot(
            sub["time_yr"],
            sub["survival_fraction"],
            marker="o",
            color=ROLE_COLORS.get(role),
            label=ROLE_LABELS.get(role, role),
        )

    ax.set_xlabel("Time [yr]")
    ax.set_ylabel("Survival fraction")
    ax.set_ylim(-0.05, 1.05)
    ax.set_title("Survival fraction")
    ax.grid(alpha=0.25)
    ax.legend(frameon=False)

    save_figure(fig, output_dir, "survival_fraction")


def make_all_plots(snapshot_table, output_dir):
    """
    Generate all requested publication figures.
    """

    set_publication_style()

    df = load_snapshot_table(snapshot_table)
    summary = compute_summary(df)
    survival = compute_survival(df)

    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # 1-3. RMS eccentricity
    plot_single_role_time(
        summary,
        "dwarf_planet",
        "e_rms",
        "RMS eccentricity",
        "Dwarf planet RMS eccentricity evolution",
        output_dir,
        "rms_eccentricity_dwarf_planets",
    )

    plot_single_role_time(
        summary,
        "test_particle",
        "e_rms",
        "RMS eccentricity",
        "Test particle RMS eccentricity evolution",
        output_dir,
        "rms_eccentricity_test_particles",
    )

    plot_two_role_time(
        summary,
        ["dwarf_planet", "test_particle"],
        "e_rms",
        "RMS eccentricity",
        "RMS eccentricity evolution",
        output_dir,
        "rms_eccentricity_combined_dp_tp",
    )

    # 4-6. RMS inclination
    plot_single_role_time(
        summary,
        "dwarf_planet",
        "inc_rms_deg",
        "RMS inclination [deg]",
        "Dwarf planet RMS inclination evolution",
        output_dir,
        "rms_inclination_dwarf_planets",
    )

    plot_single_role_time(
        summary,
        "test_particle",
        "inc_rms_deg",
        "RMS inclination [deg]",
        "Test particle RMS inclination evolution",
        output_dir,
        "rms_inclination_test_particles",
    )

    plot_two_role_time(
        summary,
        ["dwarf_planet", "test_particle"],
        "inc_rms_deg",
        "RMS inclination [deg]",
        "RMS inclination evolution",
        output_dir,
        "rms_inclination_combined_dp_tp",
    )

    # 7-10. Semimajor axis evolution
    plot_a_mean_median_single(
        summary,
        "dwarf_planet",
        output_dir,
        "semimajor_axis_mean_median_dwarf_planets",
    )

    plot_a_mean_median_single(
        summary,
        "test_particle",
        output_dir,
        "semimajor_axis_mean_median_test_particles",
    )

    plot_a_mean_median_single(
        summary,
        "giant_planet",
        output_dir,
        "semimajor_axis_mean_median_giant_planet",
    )

    plot_a_mean_median_combined(summary, output_dir)

    # 11. a-e mean/median evolution
    plot_ae_mean_median(summary, output_dir)

    # 12. a-i mean/median evolution
    plot_ai_mean_median(summary, output_dir)

    # 13. Mean eccentricity over time
    plot_two_role_time(
        summary,
        ["dwarf_planet", "test_particle", "giant_planet"],
        "e_mean",
        "Mean eccentricity",
        "Mean eccentricity evolution",
        output_dir,
        "mean_eccentricity_dp_tp_gp",
    )

    # 14. Mean inclination over time
    plot_two_role_time(
        summary,
        ["dwarf_planet", "test_particle", "giant_planet"],
        "inc_mean_deg",
        "Mean inclination [deg]",
        "Mean inclination evolution",
        output_dir,
        "mean_inclination_dp_tp_gp",
    )

    # 15. Survival fraction
    plot_survival(survival, output_dir)

    print("")
    print("All available publication figures generated.")


def main():
    parser = argparse.ArgumentParser(
        description="Generate publication-ready plots from a snapshot table."
    )

    parser.add_argument(
        "snapshot_table",
        type=str,
        help="Path to snapshot_table.csv or snapshot_table.parquet",
    )

    parser.add_argument(
        "--output_dir",
        type=str,
        default="figures",
        help="Directory where figures will be saved.",
    )

    args = parser.parse_args()

    make_all_plots(args.snapshot_table, args.output_dir)


if __name__ == "__main__":
    main()
