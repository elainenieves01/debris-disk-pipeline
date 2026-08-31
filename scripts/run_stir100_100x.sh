#!/usr/bin/env bash
# Launch SS_100MP_100Myr_100xStir (100-stirrer set).
# Per-run resume snapshot: outputs/SS_100MP_100Myr_100xStir/dump_data.json
set -euo pipefail
cd /home/elaine/debris-disk-pipeline
exec /home/elaine/miniconda3/envs/debris_pipeline/bin/python -u \
  src/simulation/run_simulation.py config/SS_100MP_100Myr_100xStir.yaml
