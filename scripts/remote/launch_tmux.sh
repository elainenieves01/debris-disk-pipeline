#!/usr/bin/env bash
# Launch a simulation inside a detached tmux session on the remote cluster.
# Usage: launch_tmux.sh <env_name> <session> <remote_dir> <config_path>
set -euo pipefail

ENV_NAME="$1"
SESSION="$2"
REMOTE_DIR="$3"
CONFIG_PATH="$4"

if tmux has-session -t "$SESSION" 2>/dev/null; then
  echo "[launch] session '$SESSION' already running; not starting a duplicate." >&2
  echo "[launch] attach with: tmux attach -t $SESSION" >&2
  exit 1
fi

source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate "$ENV_NAME"

cd "$REMOTE_DIR"
tmux new-session -d -s "$SESSION" \
  "python -u src/simulation/run_simulation.py '$CONFIG_PATH'; ec=\$?; echo; echo \"[finished, exit \$ec]\"; exit \$ec"

echo "[launch] started tmux session '$SESSION' on $(hostname)"
