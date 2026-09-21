"""tmux session naming shared by the local and cluster launch paths."""

import re


def sanitize_session_name(name):
    """tmux session names can't contain ':' or '.' safely across versions;
    collapse anything outside [A-Za-z0-9_-] to '_'. Note: tmux itself silently
    mangles literal dots in session names it creates, so dots are excluded
    here too -- this keeps our computed name matching what tmux actually
    names the session, instead of drifting from it."""
    return re.sub(r"[^A-Za-z0-9_-]", "_", name)


def session_name_for(config):
    """compute.tmux_session if set, else a sanitized simulation.name."""
    compute = config.get("compute") or {}
    override = compute.get("tmux_session")
    if override:
        return sanitize_session_name(override)
    return sanitize_session_name(config["simulation"]["name"])
