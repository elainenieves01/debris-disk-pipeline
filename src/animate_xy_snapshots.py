"""
animate_xy_snapshots.py

Make a GIF of x-y particle positions through a REBOUND SimulationArchive.

Shows:
- giant planet
- dwarf planets
- test particles
- original disk inner/outer edges as two rings
"""

import argparse
from pathlib import Path

import yaml
import rebound
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter


def load_config(config_path):
    with open(config_path, "r") as f:
        return yaml.safe_load(f)


def get_xy(sim, start, stop):
    xs, ys = [], []

    for i in range(start, min(stop, sim.N)):
        p = sim.particles[i]
        xs.append(p.x)
        ys.append(p.y)

    return np.array(xs), np.array(ys)


def make_animation(archive_path, config_path, output_path):
    config = load_config(config_path)

    sa = rebound.Simulationarchive(archive_path)

    n_gp = 1
    n_dp = int(config["dwarf_planets"]["N"])

    amin = float(config["disk"]["amin"])
    amax = float(config["disk"]["amax"])

    # Particle index convention:
    # 0 = star
    # 1 = giant planet
    # 2 to 2+n_dp-1 = dwarf planets
    # rest = test particles
    dp_start = 2
    dp_stop = 2 + n_dp
    tp_start = dp_stop

    fig, ax = plt.subplots(figsize=(7, 7))

    # Ring coordinates
    theta = np.linspace(0, 2 * np.pi, 600)
    inner_x = amin * np.cos(theta)
    inner_y = amin * np.sin(theta)
    outer_x = amax * np.cos(theta)
    outer_y = amax * np.sin(theta)

    # Plot objects initialized empty
    star_plot, = ax.plot([], [], marker="*", linestyle="None", markersize=12, label="Star")
    gp_plot, = ax.plot([], [], marker="o", linestyle="None", markersize=7, label="Giant planet")
    dp_plot = ax.scatter([], [], s=8, label="Dwarf planets")
    tp_plot = ax.scatter([], [], s=3, alpha=0.5, label="Test particles")

    # Original disk rings
    ax.plot(inner_x, inner_y, linestyle="--", linewidth=1.5, label="Initial disk inner edge")
    ax.plot(outer_x, outer_y, linestyle="--", linewidth=1.5, label="Initial disk outer edge")

    # Axis limits
    limit = 1.1 * max(amax, config["integration"].get("exit_max_distance", amax))
    limit = min(limit, 1.2 * amax)  # keep view focused on disk

    ax.set_xlim(-limit, limit)
    ax.set_ylim(-limit, limit)
    ax.set_aspect("equal", adjustable="box")
    ax.set_xlabel("x [AU]")
    ax.set_ylabel("y [AU]")
    ax.legend(loc="upper right", frameon=False)

    title = ax.set_title("")

    def update(frame_index):
        sim = sa[frame_index]

        # Star
        star = sim.particles[0]
        star_plot.set_data([star.x], [star.y])

        # Giant planet
        if sim.N > 1:
            gp = sim.particles[1]
            gp_plot.set_data([gp.x], [gp.y])
        else:
            gp_plot.set_data([], [])

        # Dwarf planets
        dp_x, dp_y = get_xy(sim, dp_start, dp_stop)
        if len(dp_x) > 0:
            dp_plot.set_offsets(np.column_stack([dp_x, dp_y]))
        else:
            dp_plot.set_offsets(np.empty((0, 2)))

        # Test particles
        tp_x, tp_y = get_xy(sim, tp_start, sim.N)
        if len(tp_x) > 0:
            tp_plot.set_offsets(np.column_stack([tp_x, tp_y]))
        else:
            tp_plot.set_offsets(np.empty((0, 2)))

        title.set_text(
            f"{config['simulation']['name']} | "
            f"Snapshot {frame_index + 1}/{len(sa)} | "
            f"t = {sim.t:.2e} yr | N = {sim.N}"
        )

        return star_plot, gp_plot, dp_plot, tp_plot, title

    anim = FuncAnimation(
        fig,
        update,
        frames=len(sa),
        interval=500,
        blit=False,
    )

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    writer = PillowWriter(fps=2)
    anim.save(output_path, writer=writer)

    plt.close(fig)

    print(f"Saved GIF to: {output_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Animate x-y snapshots from a REBOUND SimulationArchive."
    )

    parser.add_argument("archive_path", type=str)
    parser.add_argument("config_path", type=str)
    parser.add_argument("--output", type=str, default="xy_animation.gif")

    args = parser.parse_args()

    make_animation(
        archive_path=args.archive_path,
        config_path=args.config_path,
        output_path=args.output,
    )


if __name__ == "__main__":
    main()
