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

Opt-in: generate_rayleigh_cut_figures() redraws figures 1-8 with the
Rayleigh-cut outliers removed, plus an all-vs-cut RMS eccentricity comparison,
into figures/rayleigh_cut_<n>sigma/. The pipeline never calls it; run
apply_rayleigh_cut.py on a finished run.

Figures 6 and 7 frame their axes on the disk (see auto_orbit_limits) unless
plots.limits.ae / plots.limits.ai set them, and the first/last snapshot rows
they're drawn from are saved to figures/data/orbits_initial_final.csv so
replot_orbits.py can redraw them with other limits later.
"""

from contextlib import contextmanager
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import rebound

from archive_names import ArchiveNameChecker
from provenance import load_run_metadata, stamp_figure
from rayleigh_cut import cut_nsigma_from_config, rayleigh_outlier_cut


# Provenance metadata stamped onto every figure saved via save_figure().
# Set once per run by generate_summary_figures(); None disables stamping.
_DEFAULT_PROVENANCE = None


def set_default_provenance(metadata):
    """Set the provenance metadata that save_figure() stamps onto figures."""
    global _DEFAULT_PROVENANCE
    _DEFAULT_PROVENANCE = metadata


# Figure variant: save_figure() writes into figures/<subdir>/ and adds a label
# in the bottom-right corner. Set only inside figure_variant().
_FIGURE_SUBDIR = None
_FIGURE_LABEL = None


@contextmanager
def figure_variant(subdir, label):
    """Route every save_figure() call in the block to figures/<subdir>/ with a label."""
    global _FIGURE_SUBDIR, _FIGURE_LABEL
    _FIGURE_SUBDIR, _FIGURE_LABEL = subdir, label
    try:
        yield
    finally:
        _FIGURE_SUBDIR, _FIGURE_LABEL = None, None


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

    Roles come from particle names, so every snapshot's names are checked
    first (``archive_names.ArchiveNameChecker``); ArchiveNameError is raised
    rather than building a table with misidentified bodies.
    """
    sa = rebound.Simulationarchive(str(archive_path))
    name_checker = ArchiveNameChecker(str(archive_path))

    records = []

    for snapshot_number, sim in enumerate(sa):
        name_checker.check(sim, snapshot_number)
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
    if _FIGURE_LABEL:
        fig.text(0.995, 0.005, _FIGURE_LABEL, fontsize=6, color="C1",
                 ha="right", va="bottom")

    output_dir = Path(output_dir) / "figures"
    if _FIGURE_SUBDIR:
        output_dir = output_dir / _FIGURE_SUBDIR
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
    # Show absolute AU (e.g. 99.98) rather than an offset like "+1e2 / -0.02".
    ax.ticklabel_format(axis="y", useOffset=False)
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


def rms_eccentricity_rayleigh_cut(df, e_initial_max, nsigma):
    """Per-snapshot RMS(e) of the massive planetesimals, all vs Rayleigh-cut.

    The outliers are identified once, at the final snapshot, with the same cut
    the C_e diagnostic uses (``rayleigh_cut.rayleigh_outlier_cut``), and those
    bodies are left out at every snapshot -- "outlier" is a property of a body,
    so the cut curve is continuous and matches the bodies C_e excludes.
    ``e_initial_max`` is ``config["disk"]["emax"]``; ``nsigma`` the cut factor.

    Returns (times, rms_all, rms_cut, excluded_names); rms_all / rms_cut are
    NaN at snapshots with no massive planetesimals.
    """
    all_snapshots = sorted(df["snapshot"].unique())
    times = get_times(df)
    mp = df[df["role"] == "massive_planetesimal"]
    rms_all = np.full(len(all_snapshots), np.nan)
    rms_cut = np.full(len(all_snapshots), np.nan)
    if mp.empty:
        return times, rms_all, rms_cut, []

    last = mp[mp["snapshot"] == mp["snapshot"].max()]
    cut = rayleigh_outlier_cut(last["e"].to_numpy(), e_initial_max, nsigma)
    excluded = list(last["name"].to_numpy()[~cut["keep"]])

    groups = dict(tuple(mp.groupby("snapshot")))
    for i, snap in enumerate(all_snapshots):
        g = groups.get(snap)
        if g is None or g.empty:
            continue
        ecc = g["e"].to_numpy()
        kept = ecc[~g["name"].isin(excluded).to_numpy()]
        rms_all[i] = np.sqrt(np.mean(ecc ** 2))
        rms_cut[i] = np.sqrt(np.mean(kept ** 2))

    return times, rms_all, rms_cut, excluded


def plot_rms_eccentricity_rayleigh_cut(df, output_dir, e_initial_max, nsigma, dpi=200):
    """Plot massive-planetesimal RMS eccentricity vs time with and without the cut.

    Saved as rms_eccentricity_vs_time_all_vs_cut.png (inside the cut folder
    when called from generate_rayleigh_cut_figures). Skipped if the run has no
    massive planetesimals.
    """
    times, rms_all, rms_cut, excluded = rms_eccentricity_rayleigh_cut(
        df, e_initial_max, nsigma)
    if np.all(np.isnan(rms_all)):
        return

    fig, ax = plt.subplots(figsize=(8, 5))

    ax.plot(times, rms_all, color="0.55", linestyle="--",
            label="Massive planetesimals, all")
    ax.plot(times, rms_cut, color="C1",
            label=f"Massive planetesimals, Rayleigh {nsigma:g}\u03c3 cut")

    note = ("Excluded at every snapshot (outliers at final snapshot): "
            + ", ".join(excluded) if excluded else "No outliers at final snapshot")
    ax.text(0.02, 0.98, note, transform=ax.transAxes,
            ha="left", va="top", fontsize=8, color="0.3")

    ax.set_xlabel("Time (yr)")
    ax.set_ylabel("RMS Eccentricity")
    ax.set_title("RMS Eccentricity vs Time (Rayleigh outlier cut)")
    ax.legend(loc="lower right")
    ax.grid(alpha=0.3)

    save_figure(fig, output_dir, "rms_eccentricity_vs_time_all_vs_cut.png", dpi=dpi)


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

DISK_ROLES = ("test_particle", "massive_planetesimal")

# Fraction of disk bodies (each tail) ignored when auto-framing the axes, so a
# few scattered or ejected bodies can't zoom the whole plot out.
OUTLIER_PERCENTILE = 0.5

# Auto limits pad the disk's a-range by this fraction of its width.
A_PAD_FRACTION = 0.15

# Auto y-range upper limit used only when every disk body sits exactly on
# e = 0 / i = 0 (otherwise the range follows the data, however small).
Y_FALLBACK = {"e": 0.01, "inc_deg": 0.5}

ORBIT_PLOTS = {
    "ae": dict(column="e", ylabel="Eccentricity", title="Eccentricity",
               filename="a_vs_e_initial_final.png"),
    "ai": dict(column="inc_deg", ylabel="Inclination (deg)", title="Inclination",
               filename="a_vs_i_initial_final.png"),
}

ORBIT_TABLE_FILENAME = "orbits_initial_final.csv"
ORBIT_TABLE_COLUMNS = [
    "snapshot", "time_yr", "role", "particle_index", "name", "a_AU", "e", "inc_deg",
]


def _bound_disk(snap_df):
    """Disk bodies with a finite, bound orbit (a > 0)."""
    disk = snap_df[snap_df["role"].isin(DISK_ROLES)]
    return disk[np.isfinite(disk["a_AU"]) & (disk["a_AU"] > 0)]


def auto_orbit_limits(first, last, column):
    """
    Axis limits framed on the disk: the giant planet and the most extreme
    OUTLIER_PERCENTILE of disk bodies on each side are left out, and the
    initial disk box always stays in view.
    """
    disk = pd.concat([_bound_disk(first), _bound_disk(last)])
    disk_first = _bound_disk(first)
    if disk.empty:
        return None, None

    a_lo, a_hi = np.percentile(disk["a_AU"], [OUTLIER_PERCENTILE, 100 - OUTLIER_PERCENTILE])
    a_lo = min(a_lo, disk_first["a_AU"].min())
    a_hi = max(a_hi, disk_first["a_AU"].max())
    pad = max(A_PAD_FRACTION * (a_hi - a_lo), 0.01 * a_hi)

    y = disk[column].dropna()
    y_hi = max(np.percentile(y, 100 - OUTLIER_PERCENTILE), disk_first[column].max())
    y_hi = 1.15 * y_hi if y_hi > 0 else Y_FALLBACK[column]

    # a little below zero so bodies sitting on e = 0 / i = 0 aren't cut in half
    return (a_lo - pad, a_hi + pad), (-0.03 * y_hi, y_hi)


def _outside(x, y, xlim, ylim):
    return (x < xlim[0]) | (x > xlim[1]) | (y < ylim[0]) | (y > ylim[1])


def _draw_offaxis_planet(ax, gp, column, xlim, ylim):
    """Mark an off-axis giant planet with an arrow at the edge it lies past."""
    for _, row in gp.iterrows():
        a, y = row["a_AU"], row[column]
        xc = float(np.clip(a, *xlim))
        yc = float(np.clip(y, *ylim))
        if a < xlim[0]:
            marker, ha, dx = "<", "left", 8
        elif a > xlim[1]:
            marker, ha, dx = ">", "right", -8
        else:
            marker, ha, dx = "^", "center", 0
        ax.scatter([xc], [yc], s=150, marker=marker, color="C2", edgecolors="k",
                   clip_on=False, zorder=5, label="Giant planet (off-axis)")
        unit = " deg" if column == "inc_deg" else ""
        ax.annotate(f"GP: a = {a:.3g} AU, {column.split('_')[0]} = {y:.3g}{unit}",
                    (xc, yc), xytext=(dx, -12 if marker == "^" else 0),
                    textcoords="offset points", ha=ha, va="center", fontsize=8,
                    bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none", alpha=0.8))


def build_orbit_figure(first, last, kind, simulation_name, xlim=None, ylim=None):
    """
    Initial and final snapshot panels of semimajor axis vs e (kind="ae") or
    inclination (kind="ai"). xlim / ylim override the auto limits; either may
    be None, and so may either end of one ([lo, None]).
    """
    spec = ORBIT_PLOTS[kind]
    column = spec["column"]

    disk_first = first[first["role"].isin(DISK_ROLES)]
    a_init_min = disk_first["a_AU"].min()
    a_init_max = disk_first["a_AU"].max()
    y_init_max = disk_first[column].max()

    auto_x, auto_y = auto_orbit_limits(first, last, column)
    xlim = _merge_limits(xlim, auto_x)
    ylim = _merge_limits(ylim, auto_y)

    fig, axes = plt.subplots(1, 2, figsize=(12, 5), sharex=True, sharey=True)

    for ax, snap_df, label in zip(axes, [first, last], ["Initial", "Final"]):
        tp = snap_df[snap_df["role"] == "test_particle"]
        mp = snap_df[snap_df["role"] == "massive_planetesimal"]
        gp = snap_df[snap_df["role"] == "giant_planet"]

        ax.scatter(tp["a_AU"], tp[column], s=5, label="Test particles")
        ax.scatter(mp["a_AU"], mp[column], s=20, marker="o", label="Massive planetesimals")

        gp_off = _outside(gp["a_AU"], gp[column], xlim, ylim)
        if (~gp_off).any():
            ax.scatter(gp.loc[~gp_off, "a_AU"], gp.loc[~gp_off, column], s=150,
                       marker="D", edgecolors="k", color="C2", label="Giant planet")
        _draw_offaxis_planet(ax, gp[gp_off], column, xlim, ylim)

        ax.plot(
            [a_init_min, a_init_max, a_init_max, a_init_min, a_init_min],
            [0, 0, y_init_max, y_init_max, 0],
            "k--",
            linewidth=2,
            label="Initial disk limits",
        )

        disk = snap_df[snap_df["role"].isin(DISK_ROLES)]
        n_off = int(_outside(disk["a_AU"], disk[column], xlim, ylim).sum())
        if n_off:
            ax.text(0.01, 0.99, f"{n_off} of {len(disk)} disk bodies off-axis",
                    transform=ax.transAxes, ha="left", va="top", fontsize=8,
                    color="0.3")

        ax.set_xlim(xlim)
        ax.set_ylim(ylim)
        ax.tick_params(labelleft=True)

        ax.set_xlabel("Semimajor Axis (AU)")
        ax.set_ylabel(spec["ylabel"])
        ax.set_title(f"{label} Snapshot\nt = {snap_df['time_yr'].iloc[0]:.0f} yr")
        ax.legend(fontsize=8, loc="upper right")

    fig.suptitle(f"{simulation_name}\nSemimajor Axis vs. {spec['title']}", fontsize=16)
    fig.tight_layout()
    return fig


def _merge_limits(user, auto):
    """User limits where given, auto limits for anything left as None."""
    if user is None:
        return auto
    lo, hi = user
    auto_lo, auto_hi = auto if auto is not None else (None, None)
    return (auto_lo if lo is None else float(lo), auto_hi if hi is None else float(hi))


def orbit_table(first, last):
    """First and final snapshot rows, as saved for replot_orbits.py."""
    return pd.concat([first, last])[ORBIT_TABLE_COLUMNS]


def save_orbit_table(first, last, output_dir):
    """Write the first/last snapshot rows so the a-e / a-i plots can be redrawn."""
    data_dir = Path(output_dir) / "figures" / "data"
    data_dir.mkdir(parents=True, exist_ok=True)
    path = data_dir / ORBIT_TABLE_FILENAME
    orbit_table(first, last).to_csv(path, index=False)
    print(f"Saved: {path}")
    return path


def load_orbit_table(path):
    """Read a saved orbit table back into (first, last) snapshot frames."""
    df = pd.read_csv(path)
    return get_first_last_snapshots(df)


def _config_limits(config, kind):
    """plots.limits.<kind>.{xlim,ylim} from the run config (None when unset)."""
    limits = (config.get("plots", {}) or {}).get("limits", {}) or {}
    entry = limits.get(kind, {}) or {}
    return entry.get("xlim"), entry.get("ylim")


def plot_a_vs_e_initial_final(df, output_dir, simulation_name, dpi=200,
                              xlim=None, ylim=None):
    """Plot semimajor axis vs eccentricity for the first and final snapshots."""
    first, last = get_first_last_snapshots(df)
    fig = build_orbit_figure(first, last, "ae", simulation_name, xlim, ylim)
    save_figure(fig, output_dir, ORBIT_PLOTS["ae"]["filename"], dpi=dpi)


def plot_a_vs_i_initial_final(df, output_dir, simulation_name, dpi=200,
                              xlim=None, ylim=None):
    """Plot semimajor axis vs inclination for the first and final snapshots."""
    first, last = get_first_last_snapshots(df)
    fig = build_orbit_figure(first, last, "ai", simulation_name, xlim, ylim)
    save_figure(fig, output_dir, ORBIT_PLOTS["ai"]["filename"], dpi=dpi)


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
# Rayleigh-cut variant of the summary figures
# ============================================================

EXCLUDED_BODIES_FILENAME = "excluded_bodies.csv"


def rayleigh_cut_subdir(nsigma):
    """figures/ subfolder for a cut factor, e.g. 5 -> rayleigh_cut_5sigma."""
    return f"rayleigh_cut_{nsigma:g}sigma"


def generate_rayleigh_cut_figures(df, config, run_output_dir, nsigma=None, dpi=None):
    """Redraw the summary figures with the Rayleigh-cut outliers removed.

    The outliers are the massive planetesimals with final e > nsigma * sigma
    (``rms_eccentricity_rayleigh_cut``; nsigma defaults to the run config's
    ``rayleigh_cut.nsigma``, else 5 -- the same bodies the C_e diagnostic
    excludes). They are dropped from every snapshot; figures 1-8 are written to
    figures/rayleigh_cut_<n>sigma/ under their usual names, along with an
    all-vs-cut RMS eccentricity comparison and excluded_bodies.csv. The regular
    figures are not touched. Returns the excluded names; if there are none
    (e.g. the disk is not stirred), nothing is written.
    """
    if nsigma is None:
        nsigma = cut_nsigma_from_config(config)
    nsigma = float(nsigma)
    emax = float(config["disk"]["emax"])
    simulation_name = config["simulation"]["name"]
    if dpi is None:
        dpi = int(config.get("plots", {}).get("dpi", 200))

    excluded = rms_eccentricity_rayleigh_cut(df, emax, nsigma)[3]
    if not excluded:
        print("Rayleigh cut: no outliers at the final snapshot (or disk not "
              "stirred) -- the cut figures would match the originals; nothing written.")
        return excluded

    subdir = rayleigh_cut_subdir(nsigma)
    out_dir = Path(run_output_dir) / "figures" / subdir
    out_dir.mkdir(parents=True, exist_ok=True)
    mp = df[df["role"] == "massive_planetesimal"]
    last = mp[mp["snapshot"] == mp["snapshot"].max()]
    cut = rayleigh_outlier_cut(last["e"].to_numpy(), emax, nsigma)
    table = last[last["name"].isin(excluded)][["name", "time_yr", "a_AU", "e"]].copy()
    table = table.rename(columns={"time_yr": "final_time_yr", "a_AU": "final_a_AU",
                                  "e": "final_e"})
    table["nsigma"] = nsigma
    table["e_cut"] = cut["e_cut"]
    table["median_e"] = cut["median_e"]
    table.sort_values("final_e", ascending=False).to_csv(
        out_dir / EXCLUDED_BODIES_FILENAME, index=False)
    print(f"Saved: {out_dir / EXCLUDED_BODIES_FILENAME}")

    df_cut = df[~df["name"].isin(excluded)]
    label = (f"Rayleigh {nsigma:g}\u03c3 outlier cut: "
             + ", ".join(excluded) + " removed from every snapshot")
    with figure_variant(subdir, label):
        plot_rms_eccentricity_rayleigh_cut(df, run_output_dir, emax, nsigma, dpi=dpi)
        plot_survival_fraction(df_cut, run_output_dir, dpi=dpi)
        plot_mean_semimajor_axis(df_cut, run_output_dir, dpi=dpi)
        plot_mean_eccentricity(df_cut, run_output_dir, dpi=dpi)
        plot_rms_eccentricity(df_cut, run_output_dir, dpi=dpi)
        plot_rms_inclination(df_cut, run_output_dir, dpi=dpi)
        for kind, plot in (("ae", plot_a_vs_e_initial_final),
                           ("ai", plot_a_vs_i_initial_final)):
            xlim, ylim = _config_limits(config, kind)
            plot(df_cut, run_output_dir, simulation_name, dpi=dpi, xlim=xlim, ylim=ylim)
        plot_xy_initial_final(df_cut, run_output_dir, simulation_name, dpi=dpi)

    return excluded


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

    first, last = get_first_last_snapshots(df)
    save_orbit_table(first, last, run_output_dir)
    for kind, plot in (("ae", plot_a_vs_e_initial_final), ("ai", plot_a_vs_i_initial_final)):
        xlim, ylim = _config_limits(config, kind)
        plot(df, run_output_dir, simulation_name, dpi=dpi, xlim=xlim, ylim=ylim)
    plot_xy_initial_final(df, run_output_dir, simulation_name, dpi=dpi)

    print("All summary figures saved.")
