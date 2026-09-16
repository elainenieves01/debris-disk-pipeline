"""tmux session naming shared by the local and cluster launch paths."""

import re


def sanitize_session_name(name):
    """tmux session names can't contain ':' or '.' safely across versions;
    collapse anything outside [A-Za-z0-9_.-] to '_'."""
    return re.sub(r"[^A-Za-z0-9_.-]", "_", name)


def session_name_for(config):
    """compute.tmux_session if set, else a sanitized simulation.name."""
    compute = config.get("compute") or {}
    override = compute.get("tmux_session")
    if override:
        return sanitize_session_name(override)
    return sanitize_session_name(config["simulation"]["name"])
