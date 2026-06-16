from pathlib import Path
import argparse
import subprocess

import numpy as np
import matplotlib.pyplot as plt
import rebound


def get_positions(sim):
    ps = sim.particles
    x = np.array([p.x for p in ps])
    y = np.array([p.y for p in ps])
    z = np.array([p.z for p in ps])
    return x, y, z


def compute_auto_limit(sa, padding=1.1):
    max_abs = 0.0

    for sim in sa:
        x, y, z = get_positions(sim)
        current_max = np.nanmax(np.abs([x, y, z]))
        max_abs = max(max_abs, current_max)

    return max_abs * padding

def add_initial_disk_torus(ax, r_inner, r_outer, z_height=2.0, n=160):
    theta = np.linspace(0, 2 * np.pi, n)
    r = np.linspace(r_inner, r_outer, 2)

    theta_grid, r_grid = np.meshgrid(theta, r)

    x = r_grid * np.cos(theta_grid)
    y = r_grid * np.sin(theta_grid)
    z_top = np.full_like(x, z_height)
    z_bot = np.full_like(x, -z_height)

    ax.plot_surface(x, y, z_top, alpha=0.12, linewidth=0)
    ax.plot_surface(x, y, z_bot, alpha=0.12, linewidth=0)

    # inner and outer edge guide lines
    for radius in [r_inner, r_outer]:
        ax.plot(
            radius * np.cos(theta),
            radius * np.sin(theta),
            np.zeros_like(theta),
            linewidth=1.5,
            alpha=0.8,
        )

def add_initial_disk_edge_rings(ax, r_inner, r_outer, z_height=2.0, n=200):
    theta = np.linspace(0, 2 * np.pi, n)

    for radius, label in [(r_inner, "Initial inner edge"), (r_outer, "Initial outer edge")]:
        x = radius * np.cos(theta)
        y = radius * np.sin(theta)

        ax.plot(x, y, np.zeros_like(theta), linewidth=2.0, alpha=0.9, label=label)

        # faint vertical wall so the edge is visible in 3D
        theta_grid, z_grid = np.meshgrid(theta, np.linspace(-z_height, z_height, 2))
        x_wall = radius * np.cos(theta_grid)
        y_wall = radius * np.sin(theta_grid)

        ax.plot_surface(
            x_wall,
            y_wall,
            z_grid,
            alpha=0.08,
            linewidth=0,
        )

def make_frames(archive_path, frames_dir, limit=None, every=1):
    sa = rebound.Simulationarchive(str(archive_path))

    if limit is None:
        print("Computing automatic plot limits...")
        limit = compute_auto_limit(sa)

    frames_dir.mkdir(parents=True, exist_ok=True)

    initial_sim = sa[0]

    # skip star and giant planet
    # this assumes everything after particle 1 is disk objects
    a0 = np.array([p.a for p in initial_sim.particles[2:]])

    r_inner = np.nanmin(a0)
    r_outer = np.nanmax(a0)
    z_height = 0.03 * r_outer

    for k, sim in enumerate(sa):

        
        if k % every != 0:
            continue

        x, y, z = get_positions(sim)

        fig = plt.figure(figsize=(8, 7))
        ax = fig.add_subplot(111, projection="3d")


        add_initial_disk_edge_rings(
            ax,
            r_inner=r_inner,
            r_outer=r_outer,
            z_height=z_height,
        )

        ax.scatter(x[0], y[0], z[0], s=120, label="Star")
        ax.scatter(x[1], y[1], z[1], s=70, label="Giant planet")
        ax.scatter(x[2:], y[2:], z[2:], s=3, alpha=0.45, label="Disk particles")

        ax.set_title(f"t = {sim.t:.2e} yr")
        ax.set_xlabel("x [AU]")
        ax.set_ylabel("y [AU]")
        ax.set_zlabel("z [AU]")

        ax.set_xlim(-limit, limit)
        ax.set_ylim(-limit, limit)
        ax.set_zlim(-limit, limit)

        ax.legend()
        plt.tight_layout()

        frame_path = frames_dir / f"frame_{k:04d}.png"
        plt.savefig(frame_path, dpi=180)
        plt.close()

        print(f"Saved {frame_path}")


def make_gif(frames_dir, gif_path, fps=8):
    cmd = [
        "ffmpeg",
        "-y",
        "-framerate", str(fps),
        "-i", str(frames_dir / "frame_%04d.png"),
        str(gif_path),
    ]

    subprocess.run(cmd, check=True)
    print(f"Saved GIF: {gif_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Make a 3D GIF from a REBOUND SimulationArchive."
    )

    parser.add_argument("archive", help="Path to SimulationArchive .bin file")
    parser.add_argument("--out", default=None, help="Output GIF path")
    parser.add_argument("--frames-dir", default=None, help="Directory for PNG frames")
    parser.add_argument("--fps", type=int, default=8)
    parser.add_argument("--every", type=int, default=1)
    parser.add_argument("--limit", type=float, default=None)

    args = parser.parse_args()

    archive_path = Path(args.archive)
    base = archive_path.stem

    frames_dir = Path(args.frames_dir) if args.frames_dir else Path("outputs") / f"{base}_3d_frames"
    gif_path = Path(args.out) if args.out else Path("outputs") / f"{base}_3d.gif"

    make_frames(
        archive_path=archive_path,
        frames_dir=frames_dir,
        limit=args.limit,
        every=args.every,
    )

    make_gif(
        frames_dir=frames_dir,
        gif_path=gif_path,
        fps=args.fps,
    )


if __name__ == "__main__":
    main()

