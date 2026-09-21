#!/usr/bin/env bash
# Idempotent conda env bootstrap for the remote cluster side of the launcher.
# Usage: bootstrap_env.sh <env_name> <environment_file> <remote_dir>
set -euo pipefail

ENV_NAME="$1"
ENV_FILE="$2"
REMOTE_DIR="$3"

# ENV_FILE (e.g. "environment.yml") is relative to the repo, not to whatever
# directory the SSH login happened to start in (usually $HOME) -- cd there
# first, same as launch_tmux.sh does before running the simulation itself.
cd "$REMOTE_DIR"

source "$(conda info --base)/etc/profile.d/conda.sh"

if conda env list | awk '{print $1}' | grep -qx "$ENV_NAME"; then
  echo "[bootstrap] '$ENV_NAME' already exists, skipping."
else
  echo "[bootstrap] creating '$ENV_NAME' from $ENV_FILE ..."
  conda env create -n "$ENV_NAME" -f "$ENV_FILE"
fi
