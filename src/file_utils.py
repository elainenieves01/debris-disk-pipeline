import os


def generate_simulation_tag(config):
    """
    Generate a unique simulation tag from config parameters.
    """

    name = config["simulation"]["name"]

    Npart = config["test_particles"]["N"]
    npl = config["dwarf_planets"]["N"]

    distribution = config["test_particles"]["distribution"]

    maxtime = config["integration"]["maxtime"]

    maxtime_myr = maxtime / 1e6

    tag = (
        f"{name}"
        f"_Np{Npart}"
        f"_Nd{npl}"
        f"_{distribution}"
        f"_{maxtime_myr:.1f}Myr"
    )

    return tag


def generate_filenames(config):
    name = config["simulation"]["name"]
    output_dir = config["simulation"].get("output_dir", "outputs")

    os.makedirs(output_dir, exist_ok=True)

    files = {}
    files["tag"] = name
    files["archive"] = os.path.join(output_dir, f"{name}.bin")
    files["initial_conditions"] = os.path.join(output_dir, f"{name}_InitialConditions.png")
    files["final_conditions"] = os.path.join(output_dir, f"{name}_FinalConditions.png")
    files["report"] = os.path.join(output_dir, f"{name}_Report.pdf")
    files["config_copy"] = os.path.join(output_dir, f"{name}_config.yaml")

    return files