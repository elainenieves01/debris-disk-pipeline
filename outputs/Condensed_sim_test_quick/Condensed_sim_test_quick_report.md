# Condensed_sim_test_quick — Simulation Report

Config file: `/home/elaine/debris-disk-pipeline/config/Condensed_sim_test_quick.yaml`
Archive file: `outputs/Condensed_sim_test_quick/Condensed_sim_test_quick.bin`

## Provenance

- Run UUID: `04b0c8e7-b992-40a2-a99d-ebff003daedc`
- Created: 2026-09-04T16:49:19-04:00
- Finished: 2026-09-04T16:49:41-04:00
- Wall runtime: 22.2 s
- Outcome: completed
- Command: `/home/elaine/debris-disk-pipeline/src/simulation/run_simulation.py /home/elaine/debris-disk-pipeline/config/Condensed_sim_test_quick.yaml`
- Git commit: `7b03a88b3fe9735b5c9c121e57767164b2552cc5` (branch `feature/flexible-mass-and-notifications`) **(DIRTY — uncommitted tracked changes)**
    - modified: `README.md`
    - modified: `scripts/remote/launch_tmux.sh`
    - modified: `src/config_io/config_utils.py`
    - modified: `src/launch/launch_simulation.py`
    - modified: `src/launch/remote_cluster.py`
    - modified: `tests/test_compute_config.py`
    - modified: `tests/test_launch_simulation.py`
    - modified: `tests/test_remote_cluster.py`
- Software: python 3.12.11, rebound 5.0.0, numpy 2.4.6, pandas 3.0.3, matplotlib 3.10.9, pyyaml 6.0.3
- Frozen config: `config.yaml` (this directory)
- Full environment: `environment.txt` (this directory)

## Simulation
- Name: Condensed_sim_test_quick
- Output directory: outputs
- Dump/checkpoint enabled: False

## Units
- time = yr, length = AU, mass = Msun

## Integration
- Integrator: mercurius
- maxtime: 100
- time_step: 1
- timestep_fraction_of_planet_period: 0.1
- exit_max_distance: 1000.0 au

## Star
- Mass: 1.0 Msun

## Giant Planet
- None (disk integrated around the star alone)

## Disk
- a: [0.95, 1.05] au
- e: [0.0, 3.2e-05]
- inc: [0.0, 3.2e-05] deg

## Massive Planetesimals
- N: 100
- Mass-assignment method (config): total_disk_mass_earth = 2.800000e-01 Earth masses (total disk mass, split evenly across N)
- Individual mass (uniform across all 100): 8.409771e-09 Msun (0.002800 Earth masses)

## Test Particles
- N: 0
- Distribution: uniform

## Run Summary (from archive)
- Initial particle count: 101
- Final particle count: 101
- Particles lost (escaped / unbound / other removal): 0
- Archive time range: 0.000000e+00 to 1.000000e+02
- Number of snapshots: 101

## Terminal Output

```
Saving SimulationArchive to: outputs/Condensed_sim_test_quick/Condensed_sim_test_quick.bin

No giant planet: integrating the disk around the star alone.
  Timestep: 9.259630e-02 (0.1 x circular period at a=0.95 (disk inner edge) = 9.259630e-01)

Massive planetesimal mass setup:
  Mode: total_disk_mass_earth  (total disk mass given; divided evenly among N)
  Number of planetesimals: 100
  Individual MP mass: 1.283670e+00 Pluto masses / 2.800000e-03 Earth masses / 8.409771e-09 Msun
  Individual MP diameter: 3172.982 km (1.335093e+00 Pluto diameters) (uniform sphere, rho = 1 g/cm**3)
  Total disk mass: 2.800000e-01 Earth masses (8.409771e-07 Msun)

Beginning the main integration
Output 1/100: t=0.0 yr, dE/E0=0.00e+00, N=101
  Estimated time remaining to complete simulation: 0 seconds
  Estimated time remaining to next output: 0 seconds
Output 2/100: t=1.0 yr, dE/E0=2.58e-11, N=101
  Estimated time remaining to complete simulation: 9 seconds
  Estimated time remaining to next output: 0 seconds
Output 3/100: t=2.0 yr, dE/E0=1.30e-10, N=101
  Estimated time remaining to complete simulation: 11 seconds
  Estimated time remaining to next output: 0 seconds
Output 4/100: t=3.0 yr, dE/E0=1.12e-11, N=101
  Estimated time remaining to complete simulation: 12 seconds
  Estimated time remaining to next output: 0 seconds
Output 5/100: t=4.0 yr, dE/E0=3.37e-11, N=101
  Estimated time remaining to complete simulation: 13 seconds
  Estimated time remaining to next output: 0 seconds
Output 6/100: t=5.0 yr, dE/E0=8.68e-11, N=101
  Estimated time remaining to complete simulation: 13 seconds
  Estimated time remaining to next output: 0 seconds
Output 7/100: t=6.0 yr, dE/E0=2.91e-10, N=101
  Estimated time remaining to complete simulation: 13 seconds
  Estimated time remaining to next output: 0 seconds
Output 8/100: t=7.0 yr, dE/E0=1.30e-10, N=101
  Estimated time remaining to complete simulation: 13 seconds
  Estimated time remaining to next output: 0 seconds
Output 9/100: t=8.0 yr, dE/E0=1.15e-10, N=101
  Estimated time remaining to complete simulation: 14 seconds
  Estimated time remaining to next output: 0 seconds
Output 10/100: t=9.0 yr, dE/E0=2.18e-10, N=101
  Estimated time remaining to complete simulation: 16 seconds
  Estimated time remaining to next output: 0 seconds
Output 11/100: t=10.0 yr, dE/E0=2.96e-10, N=101
  Estimated time remaining to complete simulation: 16 seconds
  Estimated time remaining to next output: 0 seconds
Output 12/100: t=11.0 yr, dE/E0=2.52e-10, N=101
  Estimated time remaining to complete simulation: 15 seconds
  Estimated time remaining to next output: 0 seconds
Output 13/100: t=12.0 yr, dE/E0=3.53e-11, N=101
  Estimated time remaining to complete simulation: 15 seconds
  Estimated time remaining to next output: 0 seconds
Output 14/100: t=13.0 yr, dE/E0=1.18e-10, N=101
  Estimated time remaining to complete simulation: 15 seconds
  Estimated time remaining to next output: 0 seconds
Output 15/100: t=14.0 yr, dE/E0=2.95e-11, N=101
  Estimated time remaining to complete simulation: 15 seconds
  Estimated time remaining to next output: 0 seconds
Output 16/100: t=15.0 yr, dE/E0=2.11e-10, N=101
  Estimated time remaining to complete simulation: 14 seconds
  Estimated time remaining to next output: 0 seconds
Output 17/100: t=16.0 yr, dE/E0=1.92e-11, N=101
  Estimated time remaining to complete simulation: 14 seconds
  Estimated time remaining to next output: 0 seconds
Output 18/100: t=17.0 yr, dE/E0=1.09e-10, N=101
  Estimated time remaining to complete simulation: 15 seconds
  Estimated time remaining to next output: 0 seconds
Output 19/100: t=18.0 yr, dE/E0=2.51e-10, N=101
  Estimated time remaining to complete simulation: 15 seconds
  Estimated time remaining to next output: 0 seconds
Output 20/100: t=19.0 yr, dE/E0=2.56e-10, N=101
  Estimated time remaining to complete simulation: 14 seconds
  Estimated time remaining to next output: 0 seconds
Output 21/100: t=20.0 yr, dE/E0=3.85e-10, N=101
  Estimated time remaining to complete simulation: 14 seconds
  Estimated time remaining to next output: 0 seconds
Output 22/100: t=21.0 yr, dE/E0=2.63e-10, N=101
  Estimated time remaining to complete simulation: 14 seconds
  Estimated time remaining to next output: 0 seconds
Output 23/100: t=22.0 yr, dE/E0=2.50e-10, N=101
  Estimated time remaining to complete simulation: 14 seconds
  Estimated time remaining to next output: 0 seconds
Output 24/100: t=23.0 yr, dE/E0=2.56e-10, N=101
  Estimated time remaining to complete simulation: 13 seconds
  Estimated time remaining to next output: 0 seconds
Output 25/100: t=24.0 yr, dE/E0=1.96e-10, N=101
  Estimated time remaining to complete simulation: 13 seconds
  Estimated time remaining to next output: 0 seconds
Output 26/100: t=25.0 yr, dE/E0=1.91e-10, N=101
  Estimated time remaining to complete simulation: 13 seconds
  Estimated time remaining to next output: 0 seconds
Output 27/100: t=26.0 yr, dE/E0=2.88e-10, N=101
  Estimated time remaining to complete simulation: 13 seconds
  Estimated time remaining to next output: 0 seconds
Output 28/100: t=27.0 yr, dE/E0=2.16e-10, N=101
  Estimated time remaining to complete simulation: 13 seconds
  Estimated time remaining to next output: 0 seconds
Output 29/100: t=28.0 yr, dE/E0=3.74e-10, N=101
  Estimated time remaining to complete simulation: 13 seconds
  Estimated time remaining to next output: 0 seconds
Output 30/100: t=29.0 yr, dE/E0=2.52e-10, N=101
  Estimated time remaining to complete simulation: 13 seconds
  Estimated time remaining to next output: 0 seconds
Output 31/100: t=30.0 yr, dE/E0=3.28e-10, N=101
  Estimated time remaining to complete simulation: 13 seconds
  Estimated time remaining to next output: 0 seconds
Output 32/100: t=31.0 yr, dE/E0=2.97e-10, N=101
  Estimated time remaining to complete simulation: 12 seconds
  Estimated time remaining to next output: 0 seconds
Output 33/100: t=32.0 yr, dE/E0=1.20e-10, N=101
  Estimated time remaining to complete simulation: 13 seconds
  Estimated time remaining to next output: 0 seconds
Output 34/100: t=33.0 yr, dE/E0=2.26e-10, N=101
  Estimated time remaining to complete simulation: 13 seconds
  Estimated time remaining to next output: 0 seconds
Output 35/100: t=34.0 yr, dE/E0=3.27e-10, N=101
  Estimated time remaining to complete simulation: 12 seconds
  Estimated time remaining to next output: 0 seconds
Output 36/100: t=35.0 yr, dE/E0=3.22e-10, N=101
  Estimated time remaining to complete simulation: 12 seconds
  Estimated time remaining to next output: 0 seconds
Output 37/100: t=36.0 yr, dE/E0=3.83e-10, N=101
  Estimated time remaining to complete simulation: 12 seconds
  Estimated time remaining to next output: 0 seconds
Output 38/100: t=37.0 yr, dE/E0=3.46e-10, N=101
  Estimated time remaining to complete simulation: 12 seconds
  Estimated time remaining to next output: 0 seconds
Output 39/100: t=38.0 yr, dE/E0=2.73e-10, N=101
  Estimated time remaining to complete simulation: 12 seconds
  Estimated time remaining to next output: 0 seconds
Output 40/100: t=39.0 yr, dE/E0=2.86e-10, N=101
  Estimated time remaining to complete simulation: 12 seconds
  Estimated time remaining to next output: 0 seconds
Output 41/100: t=40.0 yr, dE/E0=4.07e-10, N=101
  Estimated time remaining to complete simulation: 11 seconds
  Estimated time remaining to next output: 0 seconds
Output 42/100: t=41.0 yr, dE/E0=5.48e-10, N=101
  Estimated time remaining to complete simulation: 11 seconds
  Estimated time remaining to next output: 0 seconds
Output 43/100: t=42.0 yr, dE/E0=3.64e-10, N=101
  Estimated time remaining to complete simulation: 11 seconds
  Estimated time remaining to next output: 0 seconds
Output 44/100: t=43.0 yr, dE/E0=3.35e-10, N=101
  Estimated time remaining to complete simulation: 11 seconds
  Estimated time remaining to next output: 0 seconds
Output 45/100: t=44.0 yr, dE/E0=3.25e-10, N=101
  Estimated time remaining to complete simulation: 11 seconds
  Estimated time remaining to next output: 0 seconds
Output 46/100: t=45.0 yr, dE/E0=5.00e-10, N=101
  Estimated time remaining to complete simulation: 11 seconds
  Estimated time remaining to next output: 0 seconds
Output 47/100: t=46.0 yr, dE/E0=5.28e-10, N=101
  Estimated time remaining to complete simulation: 11 seconds
  Estimated time remaining to next output: 0 seconds
Output 48/100: t=47.0 yr, dE/E0=4.07e-10, N=101
  Estimated time remaining to complete simulation: 10 seconds
  Estimated time remaining to next output: 0 seconds
Output 49/100: t=48.0 yr, dE/E0=3.96e-10, N=101
  Estimated time remaining to complete simulation: 11 seconds
  Estimated time remaining to next output: 0 seconds
Output 50/100: t=49.0 yr, dE/E0=6.17e-10, N=101
  Estimated time remaining to complete simulation: 10 seconds
  Estimated time remaining to next output: 0 seconds
Output 51/100: t=50.0 yr, dE/E0=4.35e-10, N=101
  Estimated time remaining to complete simulation: 10 seconds
  Estimated time remaining to next output: 0 seconds
Output 52/100: t=51.0 yr, dE/E0=4.72e-10, N=101
  Estimated time remaining to complete simulation: 10 seconds
  Estimated time remaining to next output: 0 seconds
Output 53/100: t=52.0 yr, dE/E0=4.32e-10, N=101
  Estimated time remaining to complete simulation: 10 seconds
  Estimated time remaining to next output: 0 seconds
Output 54/100: t=53.0 yr, dE/E0=4.38e-10, N=101
  Estimated time remaining to complete simulation: 10 seconds
  Estimated time remaining to next output: 0 seconds
Output 55/100: t=54.0 yr, dE/E0=4.83e-10, N=101
  Estimated time remaining to complete simulation: 9 seconds
  Estimated time remaining to next output: 0 seconds
Output 56/100: t=55.0 yr, dE/E0=7.00e-10, N=101
  Estimated time remaining to complete simulation: 9 seconds
  Estimated time remaining to next output: 0 seconds
Output 57/100: t=56.0 yr, dE/E0=4.57e-10, N=101
  Estimated time remaining to complete simulation: 9 seconds
  Estimated time remaining to next output: 0 seconds
Output 58/100: t=57.0 yr, dE/E0=3.86e-10, N=101
  Estimated time remaining to complete simulation: 9 seconds
  Estimated time remaining to next output: 0 seconds
Output 59/100: t=58.0 yr, dE/E0=3.34e-10, N=101
  Estimated time remaining to complete simulation: 9 seconds
  Estimated time remaining to next output: 0 seconds
Output 60/100: t=59.0 yr, dE/E0=4.56e-10, N=101
  Estimated time remaining to complete simulation: 9 seconds
  Estimated time remaining to next output: 0 seconds
Output 61/100: t=60.0 yr, dE/E0=3.43e-10, N=101
  Estimated time remaining to complete simulation: 8 seconds
  Estimated time remaining to next output: 0 seconds
Output 62/100: t=61.0 yr, dE/E0=3.03e-10, N=101
  Estimated time remaining to complete simulation: 8 seconds
  Estimated time remaining to next output: 0 seconds
Output 63/100: t=62.0 yr, dE/E0=3.43e-10, N=101
  Estimated time remaining to complete simulation: 8 seconds
  Estimated time remaining to next output: 0 seconds
Output 64/100: t=63.0 yr, dE/E0=6.06e-10, N=101
  Estimated time remaining to complete simulation: 8 seconds
  Estimated time remaining to next output: 0 seconds
Output 65/100: t=64.0 yr, dE/E0=5.94e-10, N=101
  Estimated time remaining to complete simulation: 7 seconds
  Estimated time remaining to next output: 0 seconds
Output 66/100: t=65.0 yr, dE/E0=3.76e-10, N=101
  Estimated time remaining to complete simulation: 7 seconds
  Estimated time remaining to next output: 0 seconds
Output 67/100: t=66.0 yr, dE/E0=4.23e-10, N=101
  Estimated time remaining to complete simulation: 7 seconds
  Estimated time remaining to next output: 0 seconds
Output 68/100: t=67.0 yr, dE/E0=4.71e-10, N=101
  Estimated time remaining to complete simulation: 7 seconds
  Estimated time remaining to next output: 0 seconds
Output 69/100: t=68.0 yr, dE/E0=5.40e-10, N=101
  Estimated time remaining to complete simulation: 6 seconds
  Estimated time remaining to next output: 0 seconds
Output 70/100: t=69.0 yr, dE/E0=4.86e-10, N=101
  Estimated time remaining to complete simulation: 6 seconds
  Estimated time remaining to next output: 0 seconds
Output 71/100: t=70.0 yr, dE/E0=6.14e-10, N=101
  Estimated time remaining to complete simulation: 6 seconds
  Estimated time remaining to next output: 0 seconds
Output 72/100: t=71.0 yr, dE/E0=4.48e-10, N=101
  Estimated time remaining to complete simulation: 6 seconds
  Estimated time remaining to next output: 0 seconds
Output 73/100: t=72.0 yr, dE/E0=5.09e-10, N=101
  Estimated time remaining to complete simulation: 5 seconds
  Estimated time remaining to next output: 0 seconds
Output 74/100: t=73.0 yr, dE/E0=5.72e-10, N=101
  Estimated time remaining to complete simulation: 5 seconds
  Estimated time remaining to next output: 0 seconds
Output 75/100: t=74.0 yr, dE/E0=5.13e-10, N=101
  Estimated time remaining to complete simulation: 5 seconds
  Estimated time remaining to next output: 0 seconds
Output 76/100: t=75.0 yr, dE/E0=6.24e-10, N=101
  Estimated time remaining to complete simulation: 5 seconds
  Estimated time remaining to next output: 0 seconds
Output 77/100: t=76.0 yr, dE/E0=6.01e-10, N=101
  Estimated time remaining to complete simulation: 5 seconds
  Estimated time remaining to next output: 0 seconds
Output 78/100: t=77.0 yr, dE/E0=7.29e-10, N=101
  Estimated time remaining to complete simulation: 4 seconds
  Estimated time remaining to next output: 0 seconds
Output 79/100: t=78.0 yr, dE/E0=4.05e-10, N=101
  Estimated time remaining to complete simulation: 4 seconds
  Estimated time remaining to next output: 0 seconds
Output 80/100: t=79.0 yr, dE/E0=3.45e-10, N=101
  Estimated time remaining to complete simulation: 4 seconds
  Estimated time remaining to next output: 0 seconds
Output 81/100: t=80.0 yr, dE/E0=4.63e-10, N=101
  Estimated time remaining to complete simulation: 4 seconds
  Estimated time remaining to next output: 0 seconds
Output 82/100: t=81.0 yr, dE/E0=3.92e-10, N=101
  Estimated time remaining to complete simulation: 3 seconds
  Estimated time remaining to next output: 0 seconds
Output 83/100: t=82.0 yr, dE/E0=5.41e-10, N=101
  Estimated time remaining to complete simulation: 3 seconds
  Estimated time remaining to next output: 0 seconds
Output 84/100: t=83.0 yr, dE/E0=4.36e-10, N=101
  Estimated time remaining to complete simulation: 3 seconds
  Estimated time remaining to next output: 0 seconds
Output 85/100: t=84.0 yr, dE/E0=4.51e-10, N=101
  Estimated time remaining to complete simulation: 3 seconds
  Estimated time remaining to next output: 0 seconds
Output 86/100: t=85.0 yr, dE/E0=4.64e-10, N=101
  Estimated time remaining to complete simulation: 3 seconds
  Estimated time remaining to next output: 0 seconds
Output 87/100: t=86.0 yr, dE/E0=5.64e-10, N=101
  Estimated time remaining to complete simulation: 2 seconds
  Estimated time remaining to next output: 0 seconds
Output 88/100: t=87.0 yr, dE/E0=4.85e-10, N=101
  Estimated time remaining to complete simulation: 2 seconds
  Estimated time remaining to next output: 0 seconds
Output 89/100: t=88.0 yr, dE/E0=5.36e-10, N=101
  Estimated time remaining to complete simulation: 2 seconds
  Estimated time remaining to next output: 0 seconds
Output 90/100: t=89.0 yr, dE/E0=4.22e-10, N=101
  Estimated time remaining to complete simulation: 2 seconds
  Estimated time remaining to next output: 0 seconds
Output 91/100: t=90.0 yr, dE/E0=5.78e-10, N=101
  Estimated time remaining to complete simulation: 1 seconds
  Estimated time remaining to next output: 0 seconds
Output 92/100: t=91.0 yr, dE/E0=6.41e-10, N=101
  Estimated time remaining to complete simulation: 1 seconds
  Estimated time remaining to next output: 0 seconds
Output 93/100: t=92.0 yr, dE/E0=5.52e-10, N=101
  Estimated time remaining to complete simulation: 1 seconds
  Estimated time remaining to next output: 0 seconds
Output 94/100: t=93.0 yr, dE/E0=5.04e-10, N=101
  Estimated time remaining to complete simulation: 1 seconds
  Estimated time remaining to next output: 0 seconds
Output 95/100: t=94.0 yr, dE/E0=6.32e-10, N=101
  Estimated time remaining to complete simulation: 1 seconds
  Estimated time remaining to next output: 0 seconds
Output 96/100: t=95.0 yr, dE/E0=8.79e-10, N=101
  Estimated time remaining to complete simulation: 0 seconds
  Estimated time remaining to next output: 0 seconds
Output 97/100: t=96.0 yr, dE/E0=8.39e-10, N=101
  Estimated time remaining to complete simulation: 0 seconds
  Estimated time remaining to next output: 0 seconds
Output 98/100: t=97.0 yr, dE/E0=8.44e-10, N=101
  Estimated time remaining to complete simulation: 0 seconds
  Estimated time remaining to next output: 0 seconds
Output 99/100: t=98.0 yr, dE/E0=8.24e-10, N=101
  Estimated time remaining to complete simulation: 0 seconds
  Estimated time remaining to next output: 0 seconds
Output 100/100: t=99.0 yr, dE/E0=8.16e-10, N=101
  Estimated time remaining to complete simulation: 0 seconds
Output 101/100: t=100.0 yr, dE/E0=9.10e-10, N=101
  Estimated time remaining to complete simulation: 0 seconds

Simulation complete.
Total runtime: 22 seconds
Saved archive: outputs/Condensed_sim_test_quick/Condensed_sim_test_quick.bin
Number of snapshots saved: 101
Archive time range: 0.000e+00 yr to 1.000e+02 yr
Loaded snapshot table from archive.
role
massive_planetesimal    100
star                      1
Name: count, dtype: int64
Saved: outputs/Condensed_sim_test_quick/figures/survival_fraction_vs_time.png
Saved: outputs/Condensed_sim_test_quick/figures/mean_semimajor_axis_vs_time.png
Saved: outputs/Condensed_sim_test_quick/figures/mean_eccentricity_vs_time.png
Saved: outputs/Condensed_sim_test_quick/figures/rms_eccentricity_vs_time.png
Saved: outputs/Condensed_sim_test_quick/figures/rms_inclination_vs_time.png
Saved: outputs/Condensed_sim_test_quick/figures/a_vs_e_initial_final.png
Saved: outputs/Condensed_sim_test_quick/figures/a_vs_i_initial_final.png
Inner plotted edge = 0.95 AU
Outer plotted edge = 1.05 AU
Saved: outputs/Condensed_sim_test_quick/figures/xy_initial_final.png
All summary figures saved.
```
