#!/usr/bin/env bash
# Idempotent conda env bootstrap for the remote cluster side of the launcher.
# Usage: bootstrap_env.sh <env_name> <environment_file>
set -euo pipefail

ENV_NAME="$1"
ENV_FILE="$2"

source "$(conda info --base)/etc/profile.d/conda.sh"

if conda env list | awk '{print $1}' | grep -qx "$ENV_NAME"; then
  echo "[bootstrap] '$ENV_NAME' already exists, skipping."
else
  echo "[bootstrap] creating '$ENV_NAME' from $ENV_FILE ..."
  conda env create -n "$ENV_NAME" -f "$ENV_FILE"
fi
