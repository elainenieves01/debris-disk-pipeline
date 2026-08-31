#!/usr/bin/env bash
# Launch the 100x-stirrer-mass run (SS_800MP_100Myr_100xStir).
# Per-run resume snapshot lives in outputs/SS_800MP_100Myr_100xStir/dump_data.json,
# so this can run concurrently with the other stir_* runs.
set -euo pipefail
cd /home/elaine/debris-disk-pipeline
exec /home/elaine/miniconda3/envs/debris_pipeline/bin/python -u \
  src/simulation/run_simulation.py config/SS_800MP_100Myr_100xStir.yaml
