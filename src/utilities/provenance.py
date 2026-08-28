"""
provenance.py

Computational provenance for pipeline runs. Each run gets a UUID, a frozen
copy of its config, a run_metadata.yaml (git commit + dirty flag + software
versions + timestamps + outcome), a full `pip freeze`, and a one-line stamp
that the plotting code writes onto every figure.

Goal: months later, point at a figure or an output directory and recover
exactly what produced it.

Pure standard library plus PyYAML (already a pipeline dependency). Nothing in
here is allowed to abort a run -- every entry point degrades gracefully.
"""

import os
import shutil
import subprocess
import sys
import platform
import uuid
from datetime import datetime
from importlib.metadata import version, PackageNotFoundError
from pathlib import Path

import yaml


RUN_METADATA_FILENAME = "run_metadata.yaml"
FROZEN_CONFIG_FILENAME = "config.yaml"
ENVIRONMENT_FILENAME = "environment.txt"

# Package versions worth recording inline (the ones that actually affect
# simulation or figure output). The full pip freeze goes to environment.txt.
_KEY_PACKAGES = ("rebound", "numpy", "pandas", "matplotlib", "pyyaml")

_REPO_DIR = Path(__file__).resolve().parents[2]


def run_output_dir_for(config):
    """Return the per-run output directory path for a config (not created)."""
    base = config["simulation"].get("output_dir", "outputs")
    return os.path.join(base, config["simulation"]["name"])


def now_iso():
    """Current local time as an ISO-8601 string with timezone offset."""
    return datetime.now().astimezone().isoformat(timespec="seconds")


def _git(args, repo_dir):
    """Run a git command, returning stripped stdout or None on any failure."""
    try:
        result = subprocess.run(
            ["git", *args],
            cwd=repo_dir,
            capture_output=True,
            text=True,
            timeout=10,
        )
    except (OSError, subprocess.SubprocessError):
        return None

    if result.returncode != 0:
        return None

    return result.stdout.strip()


def collect_git_info(repo_dir=None):
    """Git state of the pipeline repo. {'available': False} if not a repo."""
    repo_dir = str(repo_dir or _REPO_DIR)

    commit = _git(["rev-parse", "HEAD"], repo_dir)
    if commit is None:
        return {"available": False}

    # `git diff --quiet` exits 1 when tracked files have uncommitted changes.
    try:
        dirty = (
            subprocess.run(
                ["git", "diff", "--quiet"],
                cwd=repo_dir,
                capture_output=True,
                timeout=10,
            ).returncode
            != 0
        )
    except (OSError, subprocess.SubprocessError):
        dirty = False

    info = {
        "available": True,
        "commit": commit,
        "short": commit[:7],
        "branch": _git(["rev-parse", "--abbrev-ref", "HEAD"], repo_dir),
        "describe": _git(["describe", "--tags", "--always", "--dirty"], repo_dir),
        "dirty": dirty,
    }

    if dirty:
        names = _git(["diff", "--name-only", "HEAD"], repo_dir)
        info["dirty_files"] = names.splitlines() if names else []

    return info


def collect_software_versions():
    """Python version plus the key packages that affect run output."""
    versions = {"python": platform.python_version()}

    for package in _KEY_PACKAGES:
        try:
            versions[package] = version(package)
        except PackageNotFoundError:
            pass

    return versions


def collect_host_info():
    return {"hostname": platform.node(), "platform": platform.platform()}


def build_run_metadata(config, config_path, *, command=None):
    """Assemble the metadata dict for a fresh run."""
    return {
        "run_name": config["simulation"]["name"],
        "run_uuid": str(uuid.uuid4()),
        "created": now_iso(),
        "command": command if command is not None else " ".join(sys.argv),
        "config": {
            "source_path": str(config_path) if config_path else None,
            "frozen_copy": FROZEN_CONFIG_FILENAME,
        },
        "git": collect_git_info(),
        "software": collect_software_versions(),
        "host": collect_host_info(),
    }


def load_run_metadata(run_output_dir):
    """Return the run's metadata dict, or None if missing / unreadable."""
    path = Path(run_output_dir) / RUN_METADATA_FILENAME
    try:
        with open(path, "r", encoding="utf-8") as handle:
            data = yaml.safe_load(handle)
    except (OSError, yaml.YAMLError):
        return None

    return data if isinstance(data, dict) else None


def _dump_metadata(metadata, run_output_dir):
    path = Path(run_output_dir) / RUN_METADATA_FILENAME
    with open(path, "w", encoding="utf-8") as handle:
        yaml.safe_dump(metadata, handle, sort_keys=False, default_flow_style=False)
    return path


def write_run_metadata(metadata, run_output_dir):
    """Write run_metadata.yaml.

    If one already exists (a `dump: true` resume), keep the original run_uuid
    and created timestamp and record this invocation under `resumes:` instead
    of starting a new identity.
    """
    existing = load_run_metadata(run_output_dir)

    if existing and existing.get("run_uuid"):
        existing.setdefault("resumes", []).append(
            {
                "timestamp": metadata["created"],
                "command": metadata["command"],
                "git": metadata["git"],
                "software": metadata["software"],
            }
        )
        return _dump_metadata(existing, run_output_dir)

    return _dump_metadata(metadata, run_output_dir)


def update_run_metadata(run_output_dir, **fields):
    """Merge `fields` into an existing run_metadata.yaml. No-op if absent."""
    metadata = load_run_metadata(run_output_dir)
    if metadata is None:
        return None

    metadata.update(fields)
    return _dump_metadata(metadata, run_output_dir)


def freeze_config(config_path, config, run_output_dir):
    """Save the exact config used into the run directory.

    Copies the source file verbatim when we have its path (preserves comments);
    otherwise dumps the parsed config.
    """
    dest = Path(run_output_dir) / FROZEN_CONFIG_FILENAME

    if config_path and os.path.isfile(config_path):
        shutil.copy2(config_path, dest)
    else:
        with open(dest, "w", encoding="utf-8") as handle:
            yaml.safe_dump(config, handle, sort_keys=False)

    return dest


def write_environment_freeze(run_output_dir):
    """Write a full `pip freeze` to environment.txt (best-effort)."""
    dest = Path(run_output_dir) / ENVIRONMENT_FILENAME

    try:
        result = subprocess.run(
            [sys.executable, "-m", "pip", "freeze"],
            capture_output=True,
            text=True,
            timeout=120,
        )
        content = (
            result.stdout
            if result.returncode == 0
            else f"# pip freeze failed (exit {result.returncode})\n{result.stderr}"
        )
    except (OSError, subprocess.SubprocessError) as error:
        content = f"# pip freeze could not be run: {error}\n"

    with open(dest, "w", encoding="utf-8") as handle:
        handle.write(content)

    return dest


def capture_run_provenance(config, config_path, run_output_dir):
    """Write run_metadata.yaml + config.yaml + environment.txt for a run.

    Never raises: a failure here prints a warning but must not stop the run.
    """
    try:
        metadata = build_run_metadata(config, config_path)
        write_run_metadata(metadata, run_output_dir)
        freeze_config(config_path, config, run_output_dir)
        write_environment_freeze(run_output_dir)
        return metadata
    except Exception as error:  # noqa: BLE001 - provenance must never abort a run
        print(f"WARNING: provenance capture failed: {error}")
        return None


def provenance_footer_text(metadata):
    """One-line stamp for the bottom of a figure."""
    if not metadata:
        return ""

    git = metadata.get("git") or {}
    if git.get("available"):
        git_part = f"git {git.get('short', '?')}"
        if git.get("dirty"):
            git_part += " (DIRTY)"
    else:
        git_part = "git unknown"

    run_uuid = str(metadata.get("run_uuid", ""))
    created = str(metadata.get("created", ""))[:10]

    return (
        f"run {metadata.get('run_name', '?')} · "
        f"uuid {run_uuid[:8]} · {git_part} · {created}"
    )


def stamp_figure(fig, metadata):
    """Add the provenance footer to a matplotlib figure."""
    text = provenance_footer_text(metadata)
    if not text:
        return

    fig.text(
        0.005,
        0.005,
        text,
        fontsize=6,
        color="0.5",
        ha="left",
        va="bottom",
        alpha=0.8,
    )
