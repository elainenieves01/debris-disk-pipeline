"""Rebuild the debris-disk Blender scene from scratch.

Scene: black background, pale emissive star, low-poly asteroids in an
off-centre (eccentric) disk, orbiting with motion blur.

Usage (headless, writes the .blend and optionally renders a still):
    blender --background --python blender/build_scene.py -- \
        --out outputs/blender/Disk_v04.blend [--render outputs/blender/Disk_v04.png]

Or open Blender > Scripting > load this file > Run Script (no args needed).
Re-running the script rebuilds everything, so tweak the CONFIG block and rerun.
"""
import math
import random
import sys

import bpy
import bmesh
from mathutils import Vector

# ---------------------------------------------------------------- CONFIG
CONFIG = dict(
    seed=7,
    n_asteroids=2500,
    n_rings=48,               # asteroids share a pivot per ring (cheap Keplerian shear)
    a_min=6.0, a_max=11.0,    # disk radial extent (Blender units)
    disk_offset=(1.6, 0.0, 0.0),  # disk centre offset from the star (forced eccentricity)
    height_frac=0.04,         # vertical scale height as a fraction of a
    star_radius=0.9,
    star_color=(1.0, 0.93, 0.80, 1.0),   # pale yellow-white
    star_strength=12.0,
    asteroid_size=(0.03, 0.10),
    asteroid_color=(0.35, 0.31, 0.28, 1.0),
    fps=24, frames=240,
    base_period_frames=120,   # orbital period at a = a_min
    shutter=0.9,              # motion blur shutter (frames)
    resolution=(1920, 1080),
    samples=64,
    camera_loc=(0.0, -24.0, 13.0),
)


def parse_args():
    argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    out = render = None
    for i, a in enumerate(argv):
        if a == "--out":
            out = argv[i + 1]
        elif a == "--render":
            render = argv[i + 1]
    return out, render


def reset_scene():
    bpy.ops.wm.read_factory_settings(use_empty=True)
    return bpy.context.scene


def make_material(name, color, emission=None):
    mat = bpy.data.materials.new(name)
    mat.use_nodes = True
    nt = mat.node_tree
    nt.nodes.clear()
    out = nt.nodes.new("ShaderNodeOutputMaterial")
    if emission:
        n = nt.nodes.new("ShaderNodeEmission")
        n.inputs["Color"].default_value = color
        n.inputs["Strength"].default_value = emission
    else:
        n = nt.nodes.new("ShaderNodeBsdfPrincipled")
        n.inputs["Base Color"].default_value = color
        n.inputs["Roughness"].default_value = 0.9
    nt.links.new(n.outputs[0], out.inputs["Surface"])
    return mat


def low_poly_rock(name, rng, mat):
    """Icosphere (1 subdivision = 80 faces) with jittered verts, flat shaded."""
    bm = bmesh.new()
    bmesh.ops.create_icosphere(bm, subdivisions=1, radius=1.0)
    for v in bm.verts:
        v.co *= rng.uniform(0.65, 1.15)
        v.co.x *= rng.uniform(0.8, 1.3)
    me = bpy.data.meshes.new(name)
    bm.to_mesh(me)
    bm.free()
    for p in me.polygons:
        p.use_smooth = False
    me.materials.append(mat)
    return me


def build(cfg):
    rng = random.Random(cfg["seed"])
    scene = reset_scene()

    # --- world: pure black
    world = bpy.data.worlds.new("Black")
    world.use_nodes = True
    bg = world.node_tree.nodes["Background"]
    bg.inputs["Color"].default_value = (0, 0, 0, 1)
    bg.inputs["Strength"].default_value = 0.0
    scene.world = world

    # --- star
    bpy.ops.mesh.primitive_uv_sphere_add(radius=cfg["star_radius"], segments=48, ring_count=24)
    star = bpy.context.active_object
    star.name = "Star"
    bpy.ops.object.shade_smooth()
    star.data.materials.append(make_material("StarMat", cfg["star_color"], cfg["star_strength"]))
    light = bpy.data.lights.new("StarLight", "POINT")
    light.energy = 8000
    light.color = cfg["star_color"][:3]
    light.shadow_soft_size = cfg["star_radius"]
    lo = bpy.data.objects.new("StarLight", light)
    scene.collection.objects.link(lo)

    # --- asteroid mesh variants (shared) and rock material
    rock_mat = make_material("RockMat", cfg["asteroid_color"])
    variants = [low_poly_rock(f"Rock{i}", rng, rock_mat) for i in range(6)]

    # --- ring pivots centred on the offset disk centre
    centre = Vector(cfg["disk_offset"])
    nr = cfg["n_rings"]
    pivots = []
    for r in range(nr):
        a = cfg["a_min"] + (cfg["a_max"] - cfg["a_min"]) * (r + 0.5) / nr
        piv = bpy.data.objects.new(f"Ring{r:02d}", None)
        piv.location = centre
        scene.collection.objects.link(piv)
        period = cfg["base_period_frames"] * (a / cfg["a_min"]) ** 1.5   # Kepler's 3rd law
        piv.rotation_euler = (0, 0, 0)
        piv.keyframe_insert("rotation_euler", frame=1)
        piv.rotation_euler = (0, 0, 2 * math.pi * (cfg["frames"] / period))
        piv.keyframe_insert("rotation_euler", frame=cfg["frames"])
        for fc in piv.animation_data.action.fcurves:   # constant angular speed
            for kp in fc.keyframe_points:
                kp.interpolation = "LINEAR"
        pivots.append((a, piv))

    # --- asteroids
    lo_s, hi_s = cfg["asteroid_size"]
    for i in range(cfg["n_asteroids"]):
        a, piv = pivots[rng.randrange(nr)]
        a += rng.uniform(-0.5, 0.5) * (cfg["a_max"] - cfg["a_min"]) / nr
        phi = rng.uniform(0, 2 * math.pi)
        z = rng.gauss(0, cfg["height_frac"] * a)
        ob = bpy.data.objects.new(f"Ast{i:04d}", rng.choice(variants))
        ob.parent = piv
        ob.location = (a * math.cos(phi), a * math.sin(phi), z)
        ob.rotation_euler = [rng.uniform(0, 2 * math.pi) for _ in range(3)]
        ob.scale = [rng.uniform(lo_s, hi_s) ** 1.0] * 3
        scene.collection.objects.link(ob)

    # --- camera aimed at the disk centre
    cam = bpy.data.cameras.new("Cam")
    cam.lens = 35
    co = bpy.data.objects.new("Camera", cam)
    co.location = cfg["camera_loc"]
    scene.collection.objects.link(co)
    direction = centre - Vector(co.location)
    co.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()
    scene.camera = co

    # --- render / motion blur
    scene.render.engine = "CYCLES"
    scene.cycles.samples = cfg["samples"]
    scene.cycles.use_denoising = True
    scene.render.use_motion_blur = True
    scene.render.motion_blur_shutter = cfg["shutter"]
    scene.render.fps = cfg["fps"]
    scene.frame_start, scene.frame_end = 1, cfg["frames"]
    scene.render.resolution_x, scene.render.resolution_y = cfg["resolution"]
    scene.render.film_transparent = False
    scene.view_settings.view_transform = "Standard"

    # --- star glow in the compositor
    scene.use_nodes = True
    nt = scene.node_tree
    nt.nodes.clear()
    rl = nt.nodes.new("CompositorNodeRLayers")
    glare = nt.nodes.new("CompositorNodeGlare")
    glare.glare_type = "FOG_GLOW"
    glare.threshold = 1.0
    comp = nt.nodes.new("CompositorNodeComposite")
    nt.links.new(rl.outputs["Image"], glare.inputs["Image"])
    nt.links.new(glare.outputs["Image"], comp.inputs["Image"])
    return scene


if __name__ == "__main__":
    out, render = parse_args()
    scene = build(CONFIG)
    if out:
        bpy.ops.wm.save_as_mainfile(filepath=bpy.path.abspath(out))
        print("saved", out)
    if render:
        scene.frame_set(1)
        scene.render.filepath = render
        bpy.ops.render.render(write_still=True)
        print("rendered", render)
