# config_utils.py

import yaml


VALID_COMPUTE_TARGETS = ("local", "cluster")
REQUIRED_CLUSTER_KEYS = ("host", "username", "remote_dir", "conda_env")


def read_config(filename):
    """
    Read a YAML configuration file and return it as a Python dictionary.
    """

    with open(filename, "r") as file:
        config = yaml.safe_load(file)

    validate_config(config)

    return config


def validate_config(config):
    """
    Check that the config file contains the required sections.
    """

    required_sections = [
        "simulation",
        "units",
        "integration",
        "star",
        "disk",
        "massive_planetesimals",
        "test_particles",
    ]

    for section in required_sections:
        if section not in config:
            raise KeyError(f"Missing required section in config.yaml: {section}")

    # "giant_planet" is optional: it may be omitted entirely or set to null
    # to integrate the disk around the star alone.

    # "compute" is optional: absence means run locally (see launch_simulation.py).
    compute = config.get("compute")
    if compute is not None:
        if not isinstance(compute, dict):
            raise TypeError(
                "Config section 'compute' must be a mapping, "
                "e.g. 'compute: {target: local}'."
            )

        target = compute.get("target", "local")
        if target not in VALID_COMPUTE_TARGETS:
            raise ValueError(
                f"compute.target must be one of {VALID_COMPUTE_TARGETS}, got {target!r}."
            )

        if target == "cluster":
            cluster = compute.get("cluster")
            if not isinstance(cluster, dict):
                raise KeyError(
                    "compute.target is 'cluster' but no 'compute.cluster' block was given."
                )
            missing = [key for key in REQUIRED_CLUSTER_KEYS if not cluster.get(key)]
            if missing:
                raise KeyError(
                    "compute.cluster is missing required key(s): " + ", ".join(missing)
                )


def print_config(config):
    """
    Print the configuration dictionary in a readable way.
    """

    print("\nSimulation Configuration")
    print("=" * 50)

    for section, parameters in config.items():
        print(f"\n[{section}]")

        if isinstance(parameters, dict):
            for key, value in parameters.items():
                print(f"{key:40s}: {value}")
        else:
            print(parameters)

    print("=" * 50)