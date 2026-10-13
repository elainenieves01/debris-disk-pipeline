# SS_800MP_10Myr_10Mearth_slopeq2.5 — Simulation Report

> **Generated in post-processing.** This simulation was stopped before it finished (t = 360000 of 1e+07 after 36 outputs), so the pipeline never made its figures or this report. They were built afterwards from the archive on 2026-10-13 with `src/plotting/postprocess_killed_run.py`. "Final" below means the last saved output, not the end of the run, and the run's console output is not included.

Config file: `config/SS_800MP_10Myr_10Mearth_slopeq2.5.yaml`
Archive file: `outputs/SS_800MP_10Myr_10Mearth_slopeq2.5/SS_800MP_10Myr_10Mearth_slopeq2.5.bin`

## Provenance

- Run UUID: `78e85152-2e31-468f-97c8-25753d79e1b9`
- Created: 2026-09-25T15:16:25+00:00
- Command: `src/simulation/run_simulation.py config/SS_800MP_10Myr_10Mearth_slopeq2.5.yaml`
- Git: not available (run from a non-repo checkout)
- Software: python 3.12.14, rebound 5.0.0, numpy 2.4.6, pandas 3.0.3, matplotlib 3.10.9, pyyaml 6.0.3
- Frozen config: `config.yaml` (this directory)
- Full environment: `environment.txt` (this directory)

## Simulation
- Name: SS_800MP_10Myr_10Mearth_slopeq2.5
- Output directory: outputs
- Dump/checkpoint enabled: True

## Units
- time = yr, length = AU, mass = Msun

## Integration
- Integrator: mercurius
- maxtime: 10000000
- time_step: 10000
- timestep_fraction_of_planet_period: 0.1
- exit_max_distance: 1000.0 au

## Star
- Mass: 1.0 Msun

## Giant Planet
- None (disk integrated around the star alone)

## Disk
- a: [95, 105] au
- e: [0.0, 3.2e-05]
- inc: [0.0, 3.2e-05] deg

## Massive Planetesimals
- N: 800
- Mass-assignment method (config): loaded from CSV (mode=csv): variable=radius, path=src/mass_models/cascade_selection_1000km_drop100_800keep_10Mearth/slope_q2.5/selected.csv, slope=2.5 (radii/masses read verbatim from file; disk mass computed from file, not split by a power law)
- **Mass is NOT uniform** across the 800 massive planetesimals:
  - min / median / max: 6.066594e-09 / 2.175656e-08 / 1.652812e-07 Msun
  - min / median / max: 2.019848e-03 / 7.243762e-03 / 5.502971e-02 Earth masses
  - total disk mass: 1.000000e+01 Earth masses

## Test Particles
- N: 0
- Distribution: uniform

## Run Summary (from archive)
- Initial particle count: 801
- Final particle count: 800
- Particles lost (escaped / unbound / other removal): 1
- Archive time range: 0.000000e+00 to 3.600000e+05
- Number of snapshots: 37
