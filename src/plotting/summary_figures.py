"""
summary_figures.py

Builds a per-particle-per-snapshot table directly from a REBOUND
SimulationArchive (no intermediate parquet/CSV file) and saves summary
figures for a debris disk simulation.

Figures created:
1. Mean semimajor axis vs time
2. Mean eccentricity vs time
3. RMS eccentricity vs time
4. RMS inclination vs time
5. Survival fraction vs time
6. Initial/final semimajor axis vs eccentricity
7. Initial/final semimajor axis vs inclination
8. Initial/final x-y disk view
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import rebound

from provenance import load_run_metadata, stamp_figure


# Provenance metadata stamped onto every figure saved via save_figure().
# Set once per run by generate_summary_figures(); None disables stamping.
_DEFAULT_PROVENANCE = None


def set_default_provenance(metadata):
    """Set the provenance metadata that save_figure() stamps onto figures."""
    global _DEFAULT_PROVENANCE
    _DEFAULT_PROVENANCE = metadata


# ============================================================
# Building the snapshot table directly from the archive
# ============================================================

def _role_for_name(name):
    if name == "star":
        return "star"
    if name == "GP":
        return "giant_planet"
    if name.startswith("MP_"):
        return "massive_planetesimal"
    if name.startswith("TP_"):
        return "test_particle"
    return name or "unknown"


def build_snapshot_table(archive_path):
    """
    Read a REBOUND SimulationArchive directly and build a DataFrame with one
    row per particle per snapshot: snapshot, time_yr, role, particle_index,
    a_AU, e, inc_deg, x_AU, y_AU, z_AU.

    A particle that was removed mid-run (escape, unbound orbit) simply has
    no rows for snapshots after its removal, rather than a placeholder NaN
    row.
    """
    sa = rebound.Simulationarchive(str(archive_path))

    records = []

    for snapshot_number, sim in enumerate(sa):
        for index in range(sim.N):
            p = sim.particles[index]
            name = p.name or ""

            if index == 0:
                role = "star"
                a = np.nan
                e = np.nan
                inc_deg = np.nan
            else:
                role = _role_for_name(name)
                # Explicitly orbit relative to the star. The bare p.a/p.e/p.inc
                # shorthand computes the orbit relative to the coordinate
                # origin, which after sim.move_to_com() is the system
                # barycenter, not the star -- that mismatch shows up as a
                # roughly constant spurious eccentricity/inclination offset
                # that swamps real secular evolution.
                orbit = p.orbit(primary=sim.particles[0])
                a = orbit.a
                e = orbit.e
                inc_deg = np.rad2deg(orbit.inc)

            records.append(
                {
                    "snapshot": snapshot_number,
                    "time_yr": sim.t,
                    "role": role,
                    "particle_index": index,
                    "name": name,
                    "a_AU": a,
                    "e": e,
                    "inc_deg": inc_deg,
                    "x_AU": p.x,
                    "y_AU": p.y,
                    "z_AU": p.z,
                }
            )

    return pd.DataFrame.from_records(records)


# ============================================================
# Helper functions
# ============================================================

def save_figure(fig, output_dir, filename, dpi=200, provenance=None):
    """Save a matplotlib figure as a PNG and close it.

    If provenance metadata is given (or a default was set via
    set_default_provenance), a one-line provenance footer is stamped on first.
    """
    metadata = provenance if provenance is not None else _DEFAULT_PROVENANCE
    if metadata:
        stamp_figure(fig, metadata)

    output_dir = Path(output_dir) / "figures"
    output_dir.mkdir(parents=True, exist_ok=True)

    save_path = output_dir / filename
    fig.savefig(save_path, dpi=dpi, bbox_inches="tight")
    plt.close(fig)

    print(f"Saved: {save_path}")


def get_times(df):
    """Return one time value per snapshot."""
    return df.groupby("snapshot")["time_yr"].first().sort_index().to_numpy()


def mean_by_snapshot(df, role, column):
    """Compute the mean of one orbital quantity for one particle role."""
    all_snapshots = sorted(df["snapshot"].unique())

    return (
        df[df["role"] == role]
        .groupby("snapshot")[column]
        .mean()
        .reindex(all_snapshots)
        .to_numpy()
    )


def rms_by_snapshot(df, role, column):
    """Compute the RMS value of one orbital quantity for one particle role."""
    all_snapshots = sorted(df["snapshot"].unique())

    return (
        df[df["role"] == role]
        .groupby("snapshot")[column]
        .apply(lambda x: np.sqrt(np.mean(x**2)))
        .reindex(all_snapshots)
        .to_numpy()
    )


def get_first_last_snapshots(df):
    """Return the first and final snapshot DataFrames."""
    first_snap = df["snapshot"].min()
    last_snap = df["snapshot"].max()

    first = df[df["snapshot"] == first_snap]
    last = df[df["snapshot"] == last_snap]

    return first, last


# ============================================================
# Time-evolution plots
# ============================================================

def plot_mean_semimajor_axis(df, output_dir, dpi=200):
    """Plot mean semimajor axis vs time."""
    times = get_times(df)

    a_means_tp = mean_by_snapshot(df, "test_particle", "a_AU")
    a_means_mp = mean_by_snapshot(df, "massive_planetesimal", "a_AU")

    fig, ax = plt.subplots(figsize=(8, 5))

    ax.plot(times, a_means_tp, label="Test particles")

    if not np.all(np.isnan(a_means_mp)):
        ax.plot(times, a_means_mp, label="Massive planetesimals")

    ax.set_xlabel("Time (yr)")
    ax.set_ylabel("Mean Semimajor Axis (AU)")
    ax.set_title("Mean Semimajor Axis vs Time")
    ax.legend()
    ax.grid(alpha=0.3)

    save_figure(fig, output_dir, "mean_semimajor_axis_vs_time.png", dpi=dpi)


def plot_mean_eccentricity(df, output_dir, dpi=200):
    """Plot mean eccentricity vs time for test particles and massive planetesimals."""
    times = get_times(df)

    e_means_tp = mean_by_snapshot(df, "test_particle", "e")
    e_means_mp = mean_by_snapshot(df, "massive_planetesimal", "e")

    fig, ax = plt.subplots(figsize=(8, 5))

    ax.plot(times, e_means_tp, label="Test particles")

    if not np.all(np.isnan(e_means_mp)):
        ax.plot(times, e_means_mp, label="Massive planetesimals")

    ax.set_xlabel("Time (yr)")
    ax.set_ylabel("Mean Eccentricity")
    ax.set_title("Mean Eccentricity vs Time")
    ax.legend()
    ax.grid(alpha=0.3)

    save_figure(fig, output_dir, "mean_eccentricity_vs_time.png", dpi=dpi)


def plot_rms_eccentricity(df, output_dir, dpi=200):
    """Plot RMS eccentricity vs time for test particles and massive planetesimals."""
    times = get_times(df)

    e_rms_tp = rms_by_snapshot(df, "test_particle", "e")
    e_rms_mp = rms_by_snapshot(df, "massive_planetesimal", "e")

    fig, ax = plt.subplots(figsize=(8, 5))

    ax.plot(times, e_rms_tp, label="Test particles")
    if not np.all(np.isnan(e_rms_mp)):
        ax.plot(times, e_rms_mp, label="Massive planetesimals")

    ax.set_xlabel("Time (yr)")
    ax.set_ylabel("RMS Eccentricity")
    ax.set_title("RMS Eccentricity vs Time")
    ax.legend()
    ax.grid(alpha=0.3)

    save_figure(fig, output_dir, "rms_eccentricity_vs_time.png", dpi=dpi)


def plot_rms_inclination(df, output_dir, dpi=200):
    """Plot RMS inclination vs time for test particles and massive planetesimals."""
    times = get_times(df)

    i_rms_tp = rms_by_snapshot(df, "test_particle", "inc_deg")
    i_rms_mp = rms_by_snapshot(df, "massive_planetesimal", "inc_deg")

    fig, ax = plt.subplots(figsize=(8, 5))

    ax.plot(times, i_rms_tp, label="Test particles")
    if not np.all(np.isnan(i_rms_mp)):
        ax.plot(times, i_rms_mp, label="Massive planetesimals")

    ax.set_xlabel("Time (yr)")
    ax.set_ylabel("RMS Inclination (deg)")
    ax.set_title("RMS Inclination vs Time")
    ax.legend()
    ax.grid(alpha=0.3)

    save_figure(fig, output_dir, "rms_inclination_vs_time.png", dpi=dpi)


def plot_survival_fraction(df, output_dir, dpi=200):
    """
    Plot the survival fraction of each particle population.

    A particle "survives" a snapshot if it has a row there at all -- once
    removed (escape, unbound orbit) it simply stops appearing in the table.
    """
    times = get_times(df)
    all_snapshots = sorted(df["snapshot"].unique())

    fig, ax = plt.subplots(figsize=(8, 5))

    plotted_anything = False

    for role, label in [
        ("test_particle", "Test particles"),
        ("massive_planetesimal", "Massive planetesimals"),
    ]:
        role_df = df[df["role"] == role]

        if role_df.empty:
            continue

        surviving = (
            role_df.groupby("snapshot")
            .size()
            .reindex(all_snapshots, fill_value=0)
            .to_numpy()
        )

        initial = surviving[0]

        if initial == 0:
            continue

        survival_fraction = surviving / initial

        ax.plot(times, survival_fraction, linewidth=2, label=label)
        plotted_anything = True

    ax.set_xlabel("Time (yr)")
    ax.set_ylabel("Survival Fraction")
    ax.set_ylim(-0.05, 1.05)
    ax.set_title("Survival Fraction vs Time")
    ax.grid(alpha=0.3)

    if plotted_anything:
        ax.legend()

    save_figure(fig, output_dir, "survival_fraction_vs_time.png", dpi=dpi)


# ============================================================
# Initial/final orbital element plots
# ============================================================

def plot_a_vs_e_initial_final(df, output_dir, simulation_name, dpi=200):
    """Plot semimajor axis vs eccentricity for the first and final snapshots."""
    first, last = get_first_last_snapshots(df)

    disk_first = first[first["role"].isin(["test_particle", "massive_planetesimal"])]

    a_init_min = disk_first["a_AU"].min()
    a_init_max = disk_first["a_AU"].max()
    e_init_max = disk_first["e"].max()

    a_min = min(first["a_AU"].min(), last["a_AU"].min()) - 20
    a_max = max(first["a_AU"].max(), last["a_AU"].max()) + 20
    e_max = max(first["e"].max(), last["e"].max()) * 1.05

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    for ax, snap_df, label in zip(axes, [first, last], ["Initial", "Final"]):
        tp = snap_df[snap_df["role"] == "test_particle"]
        mp = snap_df[snap_df["role"] == "massive_planetesimal"]
        gp = snap_df[snap_df["role"] == "giant_planet"]

        ax.scatter(tp["a_AU"], tp["e"], s=5, label="Test particles")
        ax.scatter(mp["a_AU"], mp["e"], s=20, marker="o", label="Massive planetesimals")
        ax.scatter(gp["a_AU"], gp["e"], s=150, marker="D", edgecolors="k", label="Giant planet")

        ax.plot(
            [a_init_min, a_init_max, a_init_max, a_init_min, a_init_min],
            [0, 0, e_init_max, e_init_max, 0],
            "k--",
            linewidth=2,
            label="Initial disk limits",
        )

        ax.set_xlim(a_min, a_max)
        ax.set_ylim(0, e_max)

        ax.set_xlabel("Semimajor Axis (AU)")
        ax.set_ylabel("Eccentricity")
        ax.set_title(f"{label} Snapshot\nt = {snap_df['time_yr'].iloc[0]:.0f} yr")
        ax.legend()

    fig.suptitle(f"{simulation_name}\nSemimajor Axis vs. Eccentricity", fontsize=16)
    fig.tight_layout()

    save_figure(fig, output_dir, "a_vs_e_initial_final.png", dpi=dpi)


def plot_a_vs_i_initial_final(df, output_dir, simulation_name, dpi=200):
    """Plot semimajor axis vs inclination for the first and final snapshots."""
    first, last = get_first_last_snapshots(df)

    disk_first = first[first["role"].isin(["test_particle", "massive_planetesimal"])]

    a_init_min = disk_first["a_AU"].min()
    a_init_max = disk_first["a_AU"].max()
    i_init_max = disk_first["inc_deg"].max()

    a_min = min(first["a_AU"].min(), last["a_AU"].min()) - 20
    a_max = max(first["a_AU"].max(), last["a_AU"].max()) + 20

    i_min = -0.5
    i_max = max(i_init_max, first["inc_deg"].max(), last["inc_deg"].max()) * 1.2
    i_max = max(i_max, 0.5)

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    for ax, snap_df, label in zip(axes, [first, last], ["Initial", "Final"]):
        tp = snap_df[snap_df["role"] == "test_particle"]
        mp = snap_df[snap_df["role"] == "massive_planetesimal"]
        gp = snap_df[snap_df["role"] == "giant_planet"]

        ax.scatter(tp["a_AU"], tp["inc_deg"], s=5, label="Test particles")
        ax.scatter(mp["a_AU"], mp["inc_deg"], s=20, marker="o", label="Massive planetesimals")
        ax.scatter(gp["a_AU"], gp["inc_deg"], s=150, marker="D", edgecolors="k", label="Giant planet")

        ax.plot(
            [a_init_min, a_init_max, a_init_max, a_init_min, a_init_min],
            [0, 0, i_init_max, i_init_max, 0],
            "k--",
            linewidth=2,
            label="Initial disk limits",
        )

        ax.set_xlim(a_min, a_max)
        ax.set_ylim(i_min, i_max)

        ax.set_xlabel("Semimajor Axis (AU)")
        ax.set_ylabel("Inclination (deg)")
        ax.set_title(f"{label} Snapshot\nt = {snap_df['time_yr'].iloc[0]:.0f} yr")
        ax.legend()

    fig.suptitle(f"{simulation_name}\nSemimajor Axis vs. Inclination", fontsize=16)
    fig.tight_layout()

    save_figure(fig, output_dir, "a_vs_i_initial_final.png", dpi=dpi)


# ============================================================
# Initial/final x-y disk plot
# ============================================================

def plot_xy_initial_final(df, output_dir, simulation_name, dpi=200):
    """Plot the x-y positions of particles in the first and final snapshots."""
    theta = np.linspace(0, 2 * np.pi, 500)

    first, last = get_first_last_snapshots(df)

    initial_disk = first[first["role"].isin(["test_particle", "massive_planetesimal"])]

    r_peri = initial_disk["a_AU"] * (1 - initial_disk["e"])
    r_apo = initial_disk["a_AU"] * (1 + initial_disk["e"])

    inner_radius = r_peri.min()
    outer_radius = r_apo.max()

    print(f"Inner plotted edge = {inner_radius:.2f} AU")
    print(f"Outer plotted edge = {outer_radius:.2f} AU")

    fig, axes = plt.subplots(1, 2, figsize=(14, 7))

    for ax, snap_df, label in zip(axes, [first, last], ["Initial", "Final"]):
        tp = snap_df[snap_df["role"] == "test_particle"]
        mp = snap_df[snap_df["role"] == "massive_planetesimal"]
        gp = snap_df[snap_df["role"] == "giant_planet"]
        star = snap_df[snap_df["role"] == "star"]

        ax.scatter(tp["x_AU"], tp["y_AU"], s=5, alpha=0.5, label="Test particles")
        ax.scatter(mp["x_AU"], mp["y_AU"], s=25, marker="o", label="Massive planetesimals")

        ax.scatter(
            gp["x_AU"],
            gp["y_AU"],
            s=150,
            marker="D",
            edgecolors="k",
            label="Giant planet",
        )

        ax.scatter(
            star["x_AU"],
            star["y_AU"],
            s=300,
            marker="*",
            edgecolors="k",
            label="Star",
        )

        ax.plot(
            inner_radius * np.cos(theta),
            inner_radius * np.sin(theta),
            linestyle="--",
            linewidth=2,
            color="black",
            label="Initial radial orbit edges",
        )

        ax.plot(
            outer_radius * np.cos(theta),
            outer_radius * np.sin(theta),
            linestyle="--",
            linewidth=2,
            color="black",
        )

        ax.set_xlabel("x (AU)")
        ax.set_ylabel("y (AU)")
        ax.set_title(f"{label} Snapshot\nt = {snap_df['time_yr'].iloc[0]:.0f} yr")
        ax.axis("equal")

    handles, labels = axes[0].get_legend_handles_labels()

    fig.legend(
        handles,
        labels,
        loc="lower center",
        bbox_to_anchor=(0.5, -0.02),
        ncol=3,
        fontsize=9,
        frameon=True,
    )

    fig.tight_layout(rect=[0, 0.08, 1, 1])

    save_figure(fig, output_dir, "xy_initial_final.png", dpi=dpi)


# ============================================================
# Entry point
# ============================================================

def generate_summary_figures(archive_path, config, run_output_dir):
    """Build the snapshot table from the archive and save all summary figures."""
    df = build_snapshot_table(archive_path)

    simulation_name = config["simulation"]["name"]
    dpi = int(config.get("plots", {}).get("dpi", 200))

    stamp_on = bool(config.get("plots", {}).get("provenance_stamp", True))
    set_default_provenance(load_run_metadata(run_output_dir) if stamp_on else None)

    print("Loaded snapshot table from archive.")
    print(df[df["snapshot"] == 0]["role"].value_counts())

    plot_survival_fraction(df, run_output_dir, dpi=dpi)
    plot_mean_semimajor_axis(df, run_output_dir, dpi=dpi)
    plot_mean_eccentricity(df, run_output_dir, dpi=dpi)
    plot_rms_eccentricity(df, run_output_dir, dpi=dpi)
    plot_rms_inclination(df, run_output_dir, dpi=dpi)

    plot_a_vs_e_initial_final(df, run_output_dir, simulation_name, dpi=dpi)
    plot_a_vs_i_initial_final(df, run_output_dir, simulation_name, dpi=dpi)
    plot_xy_initial_final(df, run_output_dir, simulation_name, dpi=dpi)

    print("All summary figures saved.")
