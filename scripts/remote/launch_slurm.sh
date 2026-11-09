#!/usr/bin/env bash
# Submit a simulation to Slurm on the remote machine (the sbatch counterpart of
# launch_tmux.sh).
# Usage: launch_slurm.sh <env_name> <job_name> <remote_dir> <config_path> \
#                        <partition|-> <mem> <time> <cpus>
set -euo pipefail

ENV_NAME="$1"
JOB="$2"
REMOTE_DIR="$3"
CONFIG_PATH="$4"
PARTITION="$5"
MEM="$6"
TIME_LIMIT="$7"
CPUS="$8"

cd "$REMOTE_DIR"
mkdir -p logs/slurm

if squeue -h -n "$JOB" -u "$USER" 2>/dev/null | grep -q .; then
  echo "[launch] job '$JOB' is already queued or running; not submitting a duplicate." >&2
  echo "[launch] check with: squeue -n $JOB" >&2
  exit 1
fi

SCRIPT="logs/slurm/$JOB.sbatch"
{
  echo "#!/usr/bin/env bash"
  echo "#SBATCH --job-name=$JOB"
  echo "#SBATCH --output=$REMOTE_DIR/logs/slurm/%x-%j.out"
  echo "#SBATCH --chdir=$REMOTE_DIR"
  echo "#SBATCH --ntasks=1"
  echo "#SBATCH --cpus-per-task=$CPUS"
  echo "#SBATCH --mem=$MEM"
  echo "#SBATCH --time=$TIME_LIMIT"
  # A node reboot or preemption requeues the job; run_simulation.py then
  # restores from the run's dump file and carries on.
  echo "#SBATCH --requeue"
  if [ "$PARTITION" != "-" ]; then echo "#SBATCH --partition=$PARTITION"; fi
  cat <<EOS
set -uo pipefail
source "\$(conda info --base)/etc/profile.d/conda.sh"
conda activate "$ENV_NAME"
# DEBRIS_UNATTENDED=1: nobody is watching, so run_simulation.py must warn and
# continue rather than stop at a prompt.
DEBRIS_UNATTENDED=1 python -u src/simulation/run_simulation.py '$CONFIG_PATH'
EOS
} > "$SCRIPT"

JOBID=$(sbatch --parsable "$SCRIPT")
echo "[launch] submitted Slurm job $JOBID ('$JOB') on $(hostname)"
