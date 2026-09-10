# Consensed_sim_1Myr_1au_1earthmass — Simulation Report

Config file: `/home/elaine/debris-disk-pipeline/config/Condensed_sim_1Myr_1au_1earthmass.yaml`
Archive file: `outputs/Consensed_sim_1Myr_1au_1earthmass/Consensed_sim_1Myr_1au_1earthmass.bin`

## Provenance

- Run UUID: `712bc651-064e-4397-84d4-b1c473a1586a`
- Created: 2026-09-04T16:37:27-04:00
- Finished: 2026-09-06T18:40:34-03:00
- Wall runtime: 176586.2 s
- Outcome: completed
- Command: `/home/elaine/debris-disk-pipeline/src/simulation/run_simulation.py /home/elaine/debris-disk-pipeline/config/Condensed_sim_1Myr_1au_1earthmass.yaml`
- Git commit: `7b03a88b3fe9735b5c9c121e57767164b2552cc5` (branch `feature/flexible-mass-and-notifications`) **(DIRTY — uncommitted tracked changes)**
    - modified: `scripts/remote/launch_tmux.sh`
    - modified: `src/launch/launch_simulation.py`
- Software: python 3.12.11, rebound 5.0.0, numpy 2.4.6, pandas 3.0.3, matplotlib 3.10.9, pyyaml 6.0.3
- Frozen config: `config.yaml` (this directory)
- Full environment: `environment.txt` (this directory)

## Simulation
- Name: Consensed_sim_1Myr_1au_1earthmass
- Output directory: outputs
- Dump/checkpoint enabled: True

## Units
- time = yr, length = AU, mass = Msun

## Integration
- Integrator: mercurius
- maxtime: 1000000
- time_step: 1000
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
- Archive time range: 0.000000e+00 to 1.000000e+06
- Number of snapshots: 1001

## Terminal Output

```
Saving SimulationArchive to: outputs/Consensed_sim_1Myr_1au_1earthmass/Consensed_sim_1Myr_1au_1earthmass.bin
No existing dump_data.json found; starting fresh run.

No giant planet: integrating the disk around the star alone.
  Timestep: 9.259630e-02 (0.1 x circular period at a=0.95 (disk inner edge) = 9.259630e-01)

Massive planetesimal mass setup:
  Mode: total_disk_mass_earth  (total disk mass given; divided evenly among N)
  Number of planetesimals: 100
  Individual MP mass: 1.283670e+00 Pluto masses / 2.800000e-03 Earth masses / 8.409771e-09 Msun
  Individual MP diameter: 3172.982 km (1.335093e+00 Pluto diameters) (uniform sphere, rho = 1 g/cm**3)
  Total disk mass: 2.800000e-01 Earth masses (8.409771e-07 Msun)

Beginning the main integration
Output 1/1000: t=0.0 yr, dE/E0=0.00e+00, N=101
  Estimated time remaining to complete simulation: 2 seconds
  Estimated time remaining to next output: 0 seconds
Output 2/1000: t=1000.0 yr, dE/E0=2.31e-10, N=101
  Estimated time remaining to complete simulation: 1 days, 18 minutes, 47 seconds
  Estimated time remaining to next output: 1 minutes, 27 seconds
Output 3/1000: t=2000.0 yr, dE/E0=5.39e-10, N=101
  Estimated time remaining to complete simulation: 1 days, 7 hours, 29 minutes, 44 seconds
  Estimated time remaining to next output: 1 minutes, 53 seconds
Output 4/1000: t=3000.0 yr, dE/E0=7.67e-10, N=101
  Estimated time remaining to complete simulation: 1 days, 11 hours, 1 minutes, 13 seconds
  Estimated time remaining to next output: 2 minutes, 6 seconds
Output 5/1000: t=4000.0 yr, dE/E0=6.03e-10, N=101
  Estimated time remaining to complete simulation: 1 days, 13 hours, 8 minutes, 42 seconds
  Estimated time remaining to next output: 2 minutes, 14 seconds
Output 6/1000: t=5000.0 yr, dE/E0=5.87e-10, N=101
  Estimated time remaining to complete simulation: 1 days, 14 hours, 44 minutes, 38 seconds
  Estimated time remaining to next output: 2 minutes, 20 seconds
Output 7/1000: t=6000.0 yr, dE/E0=1.55e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 15 hours, 57 minutes, 45 seconds
  Estimated time remaining to next output: 2 minutes, 24 seconds
Output 8/1000: t=7000.0 yr, dE/E0=1.42e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 16 hours, 53 minutes, 21 seconds
  Estimated time remaining to next output: 2 minutes, 28 seconds
Output 9/1000: t=8000.0 yr, dE/E0=1.75e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 17 hours, 35 minutes, 15 seconds
  Estimated time remaining to next output: 2 minutes, 31 seconds
Output 10/1000: t=9000.0 yr, dE/E0=1.67e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 18 hours, 9 minutes, 55 seconds
  Estimated time remaining to next output: 2 minutes, 33 seconds
Output 11/1000: t=10000.0 yr, dE/E0=7.54e-10, N=101
  Estimated time remaining to complete simulation: 1 days, 18 hours, 37 minutes, 47 seconds
  Estimated time remaining to next output: 2 minutes, 35 seconds
Output 12/1000: t=11000.0 yr, dE/E0=4.34e-10, N=101
  Estimated time remaining to complete simulation: 1 days, 19 hours, 2 minutes, 36 seconds
  Estimated time remaining to next output: 2 minutes, 36 seconds
Output 13/1000: t=12000.0 yr, dE/E0=8.52e-11, N=101
  Estimated time remaining to complete simulation: 1 days, 19 hours, 21 minutes, 40 seconds
  Estimated time remaining to next output: 2 minutes, 38 seconds
Output 14/1000: t=13000.0 yr, dE/E0=6.45e-10, N=101
  Estimated time remaining to complete simulation: 1 days, 19 hours, 37 minutes, 37 seconds
  Estimated time remaining to next output: 2 minutes, 39 seconds
Output 15/1000: t=14000.0 yr, dE/E0=1.14e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 19 hours, 55 minutes, 2 seconds
  Estimated time remaining to next output: 2 minutes, 40 seconds
Output 16/1000: t=15000.0 yr, dE/E0=1.67e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 20 hours, 5 minutes, 39 seconds
  Estimated time remaining to next output: 2 minutes, 41 seconds
Output 17/1000: t=16000.0 yr, dE/E0=7.01e-10, N=101
  Estimated time remaining to complete simulation: 1 days, 20 hours, 13 minutes, 8 seconds
  Estimated time remaining to next output: 2 minutes, 41 seconds
Output 18/1000: t=17000.0 yr, dE/E0=6.06e-10, N=101
  Estimated time remaining to complete simulation: 1 days, 20 hours, 20 minutes, 11 seconds
  Estimated time remaining to next output: 2 minutes, 42 seconds
Output 19/1000: t=18000.0 yr, dE/E0=1.55e-10, N=101
  Estimated time remaining to complete simulation: 1 days, 20 hours, 26 minutes, 24 seconds
  Estimated time remaining to next output: 2 minutes, 43 seconds
Output 20/1000: t=19000.0 yr, dE/E0=2.28e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 20 hours, 31 minutes, 40 seconds
  Estimated time remaining to next output: 2 minutes, 43 seconds
Output 21/1000: t=20000.0 yr, dE/E0=2.87e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 20 hours, 36 minutes, 13 seconds
  Estimated time remaining to next output: 2 minutes, 44 seconds
Output 22/1000: t=21000.0 yr, dE/E0=3.12e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 20 hours, 39 minutes, 52 seconds
  Estimated time remaining to next output: 2 minutes, 44 seconds
Output 23/1000: t=22000.0 yr, dE/E0=3.52e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 20 hours, 42 minutes, 53 seconds
  Estimated time remaining to next output: 2 minutes, 44 seconds
Output 24/1000: t=23000.0 yr, dE/E0=3.46e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 20 hours, 45 minutes, 6 seconds
  Estimated time remaining to next output: 2 minutes, 45 seconds
Output 25/1000: t=24000.0 yr, dE/E0=2.92e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 20 hours, 47 minutes, 1 seconds
  Estimated time remaining to next output: 2 minutes, 45 seconds
Output 26/1000: t=25000.0 yr, dE/E0=3.50e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 20 hours, 48 minutes, 34 seconds
  Estimated time remaining to next output: 2 minutes, 45 seconds
Output 27/1000: t=26000.0 yr, dE/E0=2.92e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 20 hours, 50 minutes
  Estimated time remaining to next output: 2 minutes, 45 seconds
Output 28/1000: t=27000.0 yr, dE/E0=2.44e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 20 hours, 50 minutes, 54 seconds
  Estimated time remaining to next output: 2 minutes, 46 seconds
Output 29/1000: t=28000.0 yr, dE/E0=1.18e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 20 hours, 52 minutes, 11 seconds
  Estimated time remaining to next output: 2 minutes, 46 seconds
Output 30/1000: t=29000.0 yr, dE/E0=2.46e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 20 hours, 52 minutes, 53 seconds
  Estimated time remaining to next output: 2 minutes, 46 seconds
Output 31/1000: t=30000.0 yr, dE/E0=4.88e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 20 hours, 53 minutes, 30 seconds
  Estimated time remaining to next output: 2 minutes, 46 seconds
Output 32/1000: t=31000.0 yr, dE/E0=3.99e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 20 hours, 53 minutes, 44 seconds
  Estimated time remaining to next output: 2 minutes, 46 seconds
Output 33/1000: t=32000.0 yr, dE/E0=4.92e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 20 hours, 53 minutes, 42 seconds
  Estimated time remaining to next output: 2 minutes, 47 seconds
Output 34/1000: t=33000.0 yr, dE/E0=3.83e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 20 hours, 53 minutes, 49 seconds
  Estimated time remaining to next output: 2 minutes, 47 seconds
Output 35/1000: t=34000.0 yr, dE/E0=1.22e-10, N=101
  Estimated time remaining to complete simulation: 1 days, 20 hours, 53 minutes, 46 seconds
  Estimated time remaining to next output: 2 minutes, 47 seconds
Output 36/1000: t=35000.0 yr, dE/E0=2.03e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 20 hours, 53 minutes, 29 seconds
  Estimated time remaining to next output: 2 minutes, 47 seconds
Output 37/1000: t=36000.0 yr, dE/E0=3.64e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 20 hours, 53 minutes, 12 seconds
  Estimated time remaining to next output: 2 minutes, 47 seconds
Output 38/1000: t=37000.0 yr, dE/E0=3.88e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 20 hours, 52 minutes, 40 seconds
  Estimated time remaining to next output: 2 minutes, 47 seconds
Output 39/1000: t=38000.0 yr, dE/E0=1.09e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 20 hours, 52 minutes, 5 seconds
  Estimated time remaining to next output: 2 minutes, 48 seconds
Output 40/1000: t=39000.0 yr, dE/E0=1.11e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 20 hours, 51 minutes, 26 seconds
  Estimated time remaining to next output: 2 minutes, 48 seconds
Output 41/1000: t=40000.0 yr, dE/E0=4.45e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 20 hours, 50 minutes, 30 seconds
  Estimated time remaining to next output: 2 minutes, 48 seconds
Output 42/1000: t=41000.0 yr, dE/E0=3.44e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 20 hours, 49 minutes, 37 seconds
  Estimated time remaining to next output: 2 minutes, 48 seconds
Output 43/1000: t=42000.0 yr, dE/E0=3.11e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 20 hours, 48 minutes, 35 seconds
  Estimated time remaining to next output: 2 minutes, 48 seconds
Output 44/1000: t=43000.0 yr, dE/E0=7.98e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 20 hours, 47 minutes, 23 seconds
  Estimated time remaining to next output: 2 minutes, 48 seconds
Output 45/1000: t=44000.0 yr, dE/E0=9.33e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 20 hours, 46 minutes, 7 seconds
  Estimated time remaining to next output: 2 minutes, 48 seconds
Output 46/1000: t=45000.0 yr, dE/E0=5.87e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 20 hours, 44 minutes, 38 seconds
  Estimated time remaining to next output: 2 minutes, 48 seconds
Output 47/1000: t=46000.0 yr, dE/E0=4.64e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 20 hours, 43 minutes, 19 seconds
  Estimated time remaining to next output: 2 minutes, 48 seconds
Output 48/1000: t=47000.0 yr, dE/E0=2.81e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 20 hours, 41 minutes, 50 seconds
  Estimated time remaining to next output: 2 minutes, 49 seconds
Output 49/1000: t=48000.0 yr, dE/E0=2.63e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 20 hours, 40 minutes, 31 seconds
  Estimated time remaining to next output: 2 minutes, 49 seconds
Output 50/1000: t=49000.0 yr, dE/E0=2.06e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 20 hours, 39 minutes, 1 seconds
  Estimated time remaining to next output: 2 minutes, 49 seconds
Output 51/1000: t=50000.0 yr, dE/E0=1.73e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 20 hours, 37 minutes, 29 seconds
  Estimated time remaining to next output: 2 minutes, 49 seconds
Output 52/1000: t=51000.0 yr, dE/E0=4.63e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 20 hours, 36 minutes, 1 seconds
  Estimated time remaining to next output: 2 minutes, 49 seconds
Output 53/1000: t=52000.0 yr, dE/E0=7.11e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 20 hours, 34 minutes, 30 seconds
  Estimated time remaining to next output: 2 minutes, 49 seconds
Output 54/1000: t=53000.0 yr, dE/E0=5.06e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 20 hours, 32 minutes, 47 seconds
  Estimated time remaining to next output: 2 minutes, 49 seconds
Output 55/1000: t=54000.0 yr, dE/E0=4.94e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 20 hours, 31 minutes, 3 seconds
  Estimated time remaining to next output: 2 minutes, 49 seconds
Output 56/1000: t=55000.0 yr, dE/E0=3.38e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 20 hours, 29 minutes, 23 seconds
  Estimated time remaining to next output: 2 minutes, 49 seconds
Output 57/1000: t=56000.0 yr, dE/E0=6.01e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 20 hours, 27 minutes, 41 seconds
  Estimated time remaining to next output: 2 minutes, 49 seconds
Output 58/1000: t=57000.0 yr, dE/E0=4.63e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 20 hours, 25 minutes, 54 seconds
  Estimated time remaining to next output: 2 minutes, 49 seconds
Output 59/1000: t=58000.0 yr, dE/E0=5.59e-10, N=101
  Estimated time remaining to complete simulation: 1 days, 20 hours, 24 minutes, 1 seconds
  Estimated time remaining to next output: 2 minutes, 49 seconds
Output 60/1000: t=59000.0 yr, dE/E0=4.01e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 20 hours, 22 minutes, 14 seconds
  Estimated time remaining to next output: 2 minutes, 49 seconds
Output 61/1000: t=60000.0 yr, dE/E0=1.73e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 20 hours, 20 minutes, 23 seconds
  Estimated time remaining to next output: 2 minutes, 49 seconds
Output 62/1000: t=61000.0 yr, dE/E0=4.93e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 20 hours, 18 minutes, 32 seconds
  Estimated time remaining to next output: 2 minutes, 50 seconds
Output 63/1000: t=62000.0 yr, dE/E0=7.16e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 20 hours, 16 minutes, 39 seconds
  Estimated time remaining to next output: 2 minutes, 50 seconds
Output 64/1000: t=63000.0 yr, dE/E0=5.45e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 20 hours, 14 minutes, 48 seconds
  Estimated time remaining to next output: 2 minutes, 50 seconds
Output 65/1000: t=64000.0 yr, dE/E0=4.31e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 20 hours, 12 minutes, 51 seconds
  Estimated time remaining to next output: 2 minutes, 50 seconds
Output 66/1000: t=65000.0 yr, dE/E0=6.29e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 20 hours, 10 minutes, 53 seconds
  Estimated time remaining to next output: 2 minutes, 50 seconds
Output 67/1000: t=66000.0 yr, dE/E0=2.53e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 20 hours, 8 minutes, 47 seconds
  Estimated time remaining to next output: 2 minutes, 50 seconds
Output 68/1000: t=67000.0 yr, dE/E0=1.65e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 20 hours, 6 minutes, 35 seconds
  Estimated time remaining to next output: 2 minutes, 50 seconds
Output 69/1000: t=68000.0 yr, dE/E0=3.03e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 20 hours, 4 minutes, 25 seconds
  Estimated time remaining to next output: 2 minutes, 50 seconds
Output 70/1000: t=69000.0 yr, dE/E0=2.12e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 20 hours, 2 minutes, 14 seconds
  Estimated time remaining to next output: 2 minutes, 50 seconds
Output 71/1000: t=70000.0 yr, dE/E0=3.48e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 20 hours, 4 seconds
  Estimated time remaining to next output: 2 minutes, 50 seconds
Output 72/1000: t=71000.0 yr, dE/E0=2.18e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 19 hours, 57 minutes, 59 seconds
  Estimated time remaining to next output: 2 minutes, 50 seconds
Output 73/1000: t=72000.0 yr, dE/E0=2.41e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 19 hours, 55 minutes, 47 seconds
  Estimated time remaining to next output: 2 minutes, 50 seconds
Output 74/1000: t=73000.0 yr, dE/E0=1.34e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 19 hours, 53 minutes, 30 seconds
  Estimated time remaining to next output: 2 minutes, 50 seconds
Output 75/1000: t=74000.0 yr, dE/E0=4.82e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 19 hours, 51 minutes, 11 seconds
  Estimated time remaining to next output: 2 minutes, 50 seconds
Output 76/1000: t=75000.0 yr, dE/E0=1.51e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 19 hours, 48 minutes, 55 seconds
  Estimated time remaining to next output: 2 minutes, 50 seconds
Output 77/1000: t=76000.0 yr, dE/E0=4.71e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 19 hours, 46 minutes, 34 seconds
  Estimated time remaining to next output: 2 minutes, 50 seconds
Output 78/1000: t=77000.0 yr, dE/E0=4.23e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 19 hours, 44 minutes, 16 seconds
  Estimated time remaining to next output: 2 minutes, 50 seconds
Output 79/1000: t=78000.0 yr, dE/E0=4.05e-10, N=101
  Estimated time remaining to complete simulation: 1 days, 19 hours, 41 minutes, 56 seconds
  Estimated time remaining to next output: 2 minutes, 50 seconds
Output 80/1000: t=79000.0 yr, dE/E0=2.54e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 19 hours, 39 minutes, 35 seconds
  Estimated time remaining to next output: 2 minutes, 50 seconds
Output 81/1000: t=80000.0 yr, dE/E0=7.01e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 19 hours, 37 minutes, 14 seconds
  Estimated time remaining to next output: 2 minutes, 50 seconds
Output 82/1000: t=81000.0 yr, dE/E0=6.84e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 19 hours, 34 minutes, 51 seconds
  Estimated time remaining to next output: 2 minutes, 50 seconds
Output 83/1000: t=82000.0 yr, dE/E0=7.05e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 19 hours, 32 minutes, 37 seconds
  Estimated time remaining to next output: 2 minutes, 50 seconds
Output 84/1000: t=83000.0 yr, dE/E0=9.55e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 19 hours, 30 minutes, 20 seconds
  Estimated time remaining to next output: 2 minutes, 50 seconds
Output 85/1000: t=84000.0 yr, dE/E0=4.12e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 19 hours, 28 minutes, 5 seconds
  Estimated time remaining to next output: 2 minutes, 51 seconds
Output 86/1000: t=85000.0 yr, dE/E0=6.40e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 19 hours, 25 minutes, 51 seconds
  Estimated time remaining to next output: 2 minutes, 51 seconds
Output 87/1000: t=86000.0 yr, dE/E0=5.28e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 19 hours, 23 minutes, 31 seconds
  Estimated time remaining to next output: 2 minutes, 51 seconds
Output 88/1000: t=87000.0 yr, dE/E0=7.73e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 19 hours, 21 minutes, 11 seconds
  Estimated time remaining to next output: 2 minutes, 51 seconds
Output 89/1000: t=88000.0 yr, dE/E0=3.30e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 19 hours, 18 minutes, 51 seconds
  Estimated time remaining to next output: 2 minutes, 51 seconds
Output 90/1000: t=89000.0 yr, dE/E0=2.39e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 19 hours, 16 minutes, 31 seconds
  Estimated time remaining to next output: 2 minutes, 51 seconds
Output 91/1000: t=90000.0 yr, dE/E0=8.85e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 19 hours, 14 minutes, 16 seconds
  Estimated time remaining to next output: 2 minutes, 51 seconds
Output 92/1000: t=91000.0 yr, dE/E0=8.04e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 19 hours, 11 minutes, 58 seconds
  Estimated time remaining to next output: 2 minutes, 51 seconds
Output 93/1000: t=92000.0 yr, dE/E0=1.38e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 19 hours, 9 minutes, 33 seconds
  Estimated time remaining to next output: 2 minutes, 51 seconds
Output 94/1000: t=93000.0 yr, dE/E0=1.76e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 19 hours, 7 minutes, 13 seconds
  Estimated time remaining to next output: 2 minutes, 51 seconds
Output 95/1000: t=94000.0 yr, dE/E0=2.08e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 19 hours, 4 minutes, 50 seconds
  Estimated time remaining to next output: 2 minutes, 51 seconds
Output 96/1000: t=95000.0 yr, dE/E0=2.05e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 19 hours, 2 minutes, 25 seconds
  Estimated time remaining to next output: 2 minutes, 51 seconds
Output 97/1000: t=96000.0 yr, dE/E0=2.15e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 18 hours, 59 minutes, 57 seconds
  Estimated time remaining to next output: 2 minutes, 51 seconds
Output 98/1000: t=97000.0 yr, dE/E0=2.19e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 18 hours, 57 minutes, 34 seconds
  Estimated time remaining to next output: 2 minutes, 51 seconds
Output 99/1000: t=98000.0 yr, dE/E0=1.90e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 18 hours, 55 minutes, 11 seconds
  Estimated time remaining to next output: 2 minutes, 51 seconds
Output 100/1000: t=99000.0 yr, dE/E0=2.05e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 18 hours, 52 minutes, 46 seconds
  Estimated time remaining to next output: 2 minutes, 51 seconds
Output 101/1000: t=100000.0 yr, dE/E0=2.19e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 18 hours, 50 minutes, 14 seconds
  Estimated time remaining to next output: 2 minutes, 51 seconds
Output 102/1000: t=101000.0 yr, dE/E0=1.74e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 18 hours, 47 minutes, 46 seconds
  Estimated time remaining to next output: 2 minutes, 51 seconds
Output 103/1000: t=102000.0 yr, dE/E0=2.46e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 18 hours, 45 minutes, 17 seconds
  Estimated time remaining to next output: 2 minutes, 51 seconds
Output 104/1000: t=103000.0 yr, dE/E0=2.00e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 18 hours, 42 minutes, 46 seconds
  Estimated time remaining to next output: 2 minutes, 51 seconds
Output 105/1000: t=104000.0 yr, dE/E0=2.45e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 18 hours, 40 minutes, 16 seconds
  Estimated time remaining to next output: 2 minutes, 51 seconds
Output 106/1000: t=105000.0 yr, dE/E0=3.00e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 18 hours, 37 minutes, 41 seconds
  Estimated time remaining to next output: 2 minutes, 51 seconds
Output 107/1000: t=106000.0 yr, dE/E0=2.77e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 18 hours, 35 minutes, 8 seconds
  Estimated time remaining to next output: 2 minutes, 51 seconds
Output 108/1000: t=107000.0 yr, dE/E0=2.75e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 18 hours, 32 minutes, 33 seconds
  Estimated time remaining to next output: 2 minutes, 51 seconds
Output 109/1000: t=108000.0 yr, dE/E0=2.82e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 18 hours, 29 minutes, 58 seconds
  Estimated time remaining to next output: 2 minutes, 51 seconds
Output 110/1000: t=109000.0 yr, dE/E0=2.69e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 18 hours, 27 minutes, 23 seconds
  Estimated time remaining to next output: 2 minutes, 51 seconds
Output 111/1000: t=110000.0 yr, dE/E0=2.98e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 18 hours, 24 minutes, 47 seconds
  Estimated time remaining to next output: 2 minutes, 51 seconds
Output 112/1000: t=111000.0 yr, dE/E0=2.69e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 18 hours, 22 minutes, 12 seconds
  Estimated time remaining to next output: 2 minutes, 51 seconds
Output 113/1000: t=112000.0 yr, dE/E0=2.67e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 18 hours, 19 minutes, 35 seconds
  Estimated time remaining to next output: 2 minutes, 51 seconds
Output 114/1000: t=113000.0 yr, dE/E0=3.07e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 18 hours, 16 minutes, 58 seconds
  Estimated time remaining to next output: 2 minutes, 51 seconds
Output 115/1000: t=114000.0 yr, dE/E0=2.99e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 18 hours, 14 minutes, 19 seconds
  Estimated time remaining to next output: 2 minutes, 51 seconds
Output 116/1000: t=115000.0 yr, dE/E0=3.25e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 18 hours, 11 minutes, 40 seconds
  Estimated time remaining to next output: 2 minutes, 51 seconds
Output 117/1000: t=116000.0 yr, dE/E0=3.10e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 18 hours, 9 minutes, 4 seconds
  Estimated time remaining to next output: 2 minutes, 51 seconds
Output 118/1000: t=117000.0 yr, dE/E0=2.58e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 18 hours, 6 minutes, 25 seconds
  Estimated time remaining to next output: 2 minutes, 51 seconds
Output 119/1000: t=118000.0 yr, dE/E0=2.68e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 18 hours, 3 minutes, 49 seconds
  Estimated time remaining to next output: 2 minutes, 51 seconds
Output 120/1000: t=119000.0 yr, dE/E0=3.45e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 18 hours, 1 minutes, 14 seconds
  Estimated time remaining to next output: 2 minutes, 51 seconds
Output 121/1000: t=120000.0 yr, dE/E0=3.53e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 17 hours, 58 minutes, 40 seconds
  Estimated time remaining to next output: 2 minutes, 51 seconds
Output 122/1000: t=121000.0 yr, dE/E0=3.62e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 17 hours, 56 minutes, 3 seconds
  Estimated time remaining to next output: 2 minutes, 51 seconds
Output 123/1000: t=122000.0 yr, dE/E0=3.54e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 17 hours, 53 minutes, 28 seconds
  Estimated time remaining to next output: 2 minutes, 51 seconds
Output 124/1000: t=123000.0 yr, dE/E0=2.87e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 17 hours, 50 minutes, 54 seconds
  Estimated time remaining to next output: 2 minutes, 51 seconds
Output 125/1000: t=124000.0 yr, dE/E0=4.18e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 17 hours, 48 minutes, 26 seconds
  Estimated time remaining to next output: 2 minutes, 52 seconds
Output 126/1000: t=125000.0 yr, dE/E0=3.36e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 17 hours, 45 minutes, 58 seconds
  Estimated time remaining to next output: 2 minutes, 52 seconds
Output 127/1000: t=126000.0 yr, dE/E0=2.98e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 17 hours, 43 minutes, 31 seconds
  Estimated time remaining to next output: 2 minutes, 52 seconds
Output 128/1000: t=127000.0 yr, dE/E0=2.15e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 17 hours, 41 minutes, 3 seconds
  Estimated time remaining to next output: 2 minutes, 52 seconds
Output 129/1000: t=128000.0 yr, dE/E0=1.57e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 17 hours, 38 minutes, 41 seconds
  Estimated time remaining to next output: 2 minutes, 52 seconds
Output 130/1000: t=129000.0 yr, dE/E0=1.14e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 17 hours, 36 minutes, 13 seconds
  Estimated time remaining to next output: 2 minutes, 52 seconds
Output 131/1000: t=130000.0 yr, dE/E0=7.70e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 17 hours, 33 minutes, 46 seconds
  Estimated time remaining to next output: 2 minutes, 52 seconds
Output 132/1000: t=131000.0 yr, dE/E0=2.24e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 17 hours, 31 minutes, 20 seconds
  Estimated time remaining to next output: 2 minutes, 52 seconds
Output 133/1000: t=132000.0 yr, dE/E0=4.41e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 17 hours, 28 minutes, 53 seconds
  Estimated time remaining to next output: 2 minutes, 52 seconds
Output 134/1000: t=133000.0 yr, dE/E0=3.58e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 17 hours, 26 minutes, 25 seconds
  Estimated time remaining to next output: 2 minutes, 52 seconds
Output 135/1000: t=134000.0 yr, dE/E0=2.44e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 17 hours, 23 minutes, 56 seconds
  Estimated time remaining to next output: 2 minutes, 52 seconds
Output 136/1000: t=135000.0 yr, dE/E0=6.88e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 17 hours, 21 minutes, 27 seconds
  Estimated time remaining to next output: 2 minutes, 52 seconds
Output 137/1000: t=136000.0 yr, dE/E0=9.19e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 17 hours, 18 minutes, 58 seconds
  Estimated time remaining to next output: 2 minutes, 52 seconds
Output 138/1000: t=137000.0 yr, dE/E0=9.24e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 17 hours, 16 minutes, 29 seconds
  Estimated time remaining to next output: 2 minutes, 52 seconds
Output 139/1000: t=138000.0 yr, dE/E0=4.13e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 17 hours, 13 minutes, 58 seconds
  Estimated time remaining to next output: 2 minutes, 52 seconds
Output 140/1000: t=139000.0 yr, dE/E0=4.32e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 17 hours, 11 minutes, 30 seconds
  Estimated time remaining to next output: 2 minutes, 52 seconds
Output 141/1000: t=140000.0 yr, dE/E0=4.78e-10, N=101
  Estimated time remaining to complete simulation: 1 days, 17 hours, 8 minutes, 58 seconds
  Estimated time remaining to next output: 2 minutes, 52 seconds
Output 142/1000: t=141000.0 yr, dE/E0=4.52e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 17 hours, 6 minutes, 30 seconds
  Estimated time remaining to next output: 2 minutes, 52 seconds
Output 143/1000: t=142000.0 yr, dE/E0=5.79e-10, N=101
  Estimated time remaining to complete simulation: 1 days, 17 hours, 3 minutes, 59 seconds
  Estimated time remaining to next output: 2 minutes, 52 seconds
Output 144/1000: t=143000.0 yr, dE/E0=3.43e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 17 hours, 1 minutes, 27 seconds
  Estimated time remaining to next output: 2 minutes, 52 seconds
Output 145/1000: t=144000.0 yr, dE/E0=9.91e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 16 hours, 59 minutes
  Estimated time remaining to next output: 2 minutes, 52 seconds
Output 146/1000: t=145000.0 yr, dE/E0=1.42e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 16 hours, 56 minutes, 30 seconds
  Estimated time remaining to next output: 2 minutes, 52 seconds
Output 147/1000: t=146000.0 yr, dE/E0=1.17e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 16 hours, 54 minutes, 1 seconds
  Estimated time remaining to next output: 2 minutes, 52 seconds
Output 148/1000: t=147000.0 yr, dE/E0=1.45e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 16 hours, 51 minutes, 31 seconds
  Estimated time remaining to next output: 2 minutes, 52 seconds
Output 149/1000: t=148000.0 yr, dE/E0=1.67e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 16 hours, 48 minutes, 58 seconds
  Estimated time remaining to next output: 2 minutes, 52 seconds
Output 150/1000: t=149000.0 yr, dE/E0=1.47e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 16 hours, 46 minutes, 25 seconds
  Estimated time remaining to next output: 2 minutes, 52 seconds
Output 151/1000: t=150000.0 yr, dE/E0=1.93e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 16 hours, 43 minutes, 53 seconds
  Estimated time remaining to next output: 2 minutes, 52 seconds
Output 152/1000: t=151000.0 yr, dE/E0=2.13e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 16 hours, 41 minutes, 17 seconds
  Estimated time remaining to next output: 2 minutes, 52 seconds
Output 153/1000: t=152000.0 yr, dE/E0=1.93e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 16 hours, 38 minutes, 43 seconds
  Estimated time remaining to next output: 2 minutes, 52 seconds
Output 154/1000: t=153000.0 yr, dE/E0=1.99e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 16 hours, 36 minutes, 11 seconds
  Estimated time remaining to next output: 2 minutes, 52 seconds
Output 155/1000: t=154000.0 yr, dE/E0=1.96e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 16 hours, 33 minutes, 36 seconds
  Estimated time remaining to next output: 2 minutes, 52 seconds
Output 156/1000: t=155000.0 yr, dE/E0=2.54e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 16 hours, 31 minutes, 2 seconds
  Estimated time remaining to next output: 2 minutes, 52 seconds
Output 157/1000: t=156000.0 yr, dE/E0=2.00e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 16 hours, 28 minutes, 29 seconds
  Estimated time remaining to next output: 2 minutes, 52 seconds
Output 158/1000: t=157000.0 yr, dE/E0=2.77e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 16 hours, 25 minutes, 55 seconds
  Estimated time remaining to next output: 2 minutes, 52 seconds
Output 159/1000: t=158000.0 yr, dE/E0=3.31e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 16 hours, 23 minutes, 20 seconds
  Estimated time remaining to next output: 2 minutes, 52 seconds
Output 160/1000: t=159000.0 yr, dE/E0=3.45e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 16 hours, 20 minutes, 44 seconds
  Estimated time remaining to next output: 2 minutes, 52 seconds
Output 161/1000: t=160000.0 yr, dE/E0=3.77e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 16 hours, 18 minutes, 10 seconds
  Estimated time remaining to next output: 2 minutes, 52 seconds
Output 162/1000: t=161000.0 yr, dE/E0=3.88e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 16 hours, 15 minutes, 36 seconds
  Estimated time remaining to next output: 2 minutes, 52 seconds
Output 163/1000: t=162000.0 yr, dE/E0=2.98e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 16 hours, 13 minutes, 1 seconds
  Estimated time remaining to next output: 2 minutes, 52 seconds
Output 164/1000: t=163000.0 yr, dE/E0=3.44e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 16 hours, 10 minutes, 24 seconds
  Estimated time remaining to next output: 2 minutes, 52 seconds
Output 165/1000: t=164000.0 yr, dE/E0=3.80e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 16 hours, 7 minutes, 48 seconds
  Estimated time remaining to next output: 2 minutes, 53 seconds
Output 166/1000: t=165000.0 yr, dE/E0=4.26e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 16 hours, 5 minutes, 12 seconds
  Estimated time remaining to next output: 2 minutes, 53 seconds
Output 167/1000: t=166000.0 yr, dE/E0=3.71e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 16 hours, 2 minutes, 36 seconds
  Estimated time remaining to next output: 2 minutes, 53 seconds
Output 168/1000: t=167000.0 yr, dE/E0=3.59e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 15 hours, 59 minutes, 57 seconds
  Estimated time remaining to next output: 2 minutes, 53 seconds
Output 169/1000: t=168000.0 yr, dE/E0=3.86e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 15 hours, 57 minutes, 17 seconds
  Estimated time remaining to next output: 2 minutes, 53 seconds
Output 170/1000: t=169000.0 yr, dE/E0=4.00e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 15 hours, 54 minutes, 38 seconds
  Estimated time remaining to next output: 2 minutes, 53 seconds
Output 171/1000: t=170000.0 yr, dE/E0=4.63e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 15 hours, 51 minutes, 58 seconds
  Estimated time remaining to next output: 2 minutes, 53 seconds
Output 172/1000: t=171000.0 yr, dE/E0=4.28e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 15 hours, 49 minutes, 17 seconds
  Estimated time remaining to next output: 2 minutes, 53 seconds
Output 173/1000: t=172000.0 yr, dE/E0=4.26e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 15 hours, 46 minutes, 38 seconds
  Estimated time remaining to next output: 2 minutes, 53 seconds
Output 174/1000: t=173000.0 yr, dE/E0=3.43e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 15 hours, 43 minutes, 58 seconds
  Estimated time remaining to next output: 2 minutes, 53 seconds
Output 175/1000: t=174000.0 yr, dE/E0=3.39e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 15 hours, 41 minutes, 15 seconds
  Estimated time remaining to next output: 2 minutes, 53 seconds
Output 176/1000: t=175000.0 yr, dE/E0=3.11e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 15 hours, 38 minutes, 34 seconds
  Estimated time remaining to next output: 2 minutes, 53 seconds
Output 177/1000: t=176000.0 yr, dE/E0=4.06e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 15 hours, 35 minutes, 55 seconds
  Estimated time remaining to next output: 2 minutes, 53 seconds
Output 178/1000: t=177000.0 yr, dE/E0=4.27e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 15 hours, 33 minutes, 15 seconds
  Estimated time remaining to next output: 2 minutes, 53 seconds
Output 179/1000: t=178000.0 yr, dE/E0=4.21e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 15 hours, 30 minutes, 36 seconds
  Estimated time remaining to next output: 2 minutes, 53 seconds
Output 180/1000: t=179000.0 yr, dE/E0=4.36e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 15 hours, 27 minutes, 56 seconds
  Estimated time remaining to next output: 2 minutes, 53 seconds
Output 181/1000: t=180000.0 yr, dE/E0=4.29e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 15 hours, 25 minutes, 16 seconds
  Estimated time remaining to next output: 2 minutes, 53 seconds
Output 182/1000: t=181000.0 yr, dE/E0=4.40e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 15 hours, 22 minutes, 32 seconds
  Estimated time remaining to next output: 2 minutes, 53 seconds
Output 183/1000: t=182000.0 yr, dE/E0=4.55e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 15 hours, 19 minutes, 47 seconds
  Estimated time remaining to next output: 2 minutes, 53 seconds
Output 184/1000: t=183000.0 yr, dE/E0=4.39e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 15 hours, 17 minutes, 1 seconds
  Estimated time remaining to next output: 2 minutes, 53 seconds
Output 185/1000: t=184000.0 yr, dE/E0=3.58e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 15 hours, 14 minutes, 14 seconds
  Estimated time remaining to next output: 2 minutes, 53 seconds
Output 186/1000: t=185000.0 yr, dE/E0=4.59e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 15 hours, 11 minutes, 29 seconds
  Estimated time remaining to next output: 2 minutes, 53 seconds
Output 187/1000: t=186000.0 yr, dE/E0=4.23e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 15 hours, 8 minutes, 44 seconds
  Estimated time remaining to next output: 2 minutes, 53 seconds
Output 188/1000: t=187000.0 yr, dE/E0=4.38e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 15 hours, 6 minutes, 3 seconds
  Estimated time remaining to next output: 2 minutes, 53 seconds
Output 189/1000: t=188000.0 yr, dE/E0=5.15e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 15 hours, 3 minutes, 23 seconds
  Estimated time remaining to next output: 2 minutes, 53 seconds
Output 190/1000: t=189000.0 yr, dE/E0=5.76e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 15 hours, 42 seconds
  Estimated time remaining to next output: 2 minutes, 53 seconds
Output 191/1000: t=190000.0 yr, dE/E0=4.75e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 14 hours, 58 minutes, 1 seconds
  Estimated time remaining to next output: 2 minutes, 53 seconds
Output 192/1000: t=191000.0 yr, dE/E0=5.64e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 14 hours, 55 minutes, 21 seconds
  Estimated time remaining to next output: 2 minutes, 53 seconds
Output 193/1000: t=192000.0 yr, dE/E0=6.13e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 14 hours, 52 minutes, 41 seconds
  Estimated time remaining to next output: 2 minutes, 53 seconds
Output 194/1000: t=193000.0 yr, dE/E0=6.05e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 14 hours, 50 minutes
  Estimated time remaining to next output: 2 minutes, 53 seconds
Output 195/1000: t=194000.0 yr, dE/E0=6.25e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 14 hours, 47 minutes, 17 seconds
  Estimated time remaining to next output: 2 minutes, 53 seconds
Output 196/1000: t=195000.0 yr, dE/E0=7.43e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 14 hours, 44 minutes, 35 seconds
  Estimated time remaining to next output: 2 minutes, 53 seconds
Output 197/1000: t=196000.0 yr, dE/E0=8.14e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 14 hours, 41 minutes, 52 seconds
  Estimated time remaining to next output: 2 minutes, 53 seconds
Output 198/1000: t=197000.0 yr, dE/E0=8.10e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 14 hours, 39 minutes, 10 seconds
  Estimated time remaining to next output: 2 minutes, 53 seconds
Output 199/1000: t=198000.0 yr, dE/E0=8.49e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 14 hours, 36 minutes, 27 seconds
  Estimated time remaining to next output: 2 minutes, 53 seconds
Output 200/1000: t=199000.0 yr, dE/E0=8.67e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 14 hours, 33 minutes, 41 seconds
  Estimated time remaining to next output: 2 minutes, 53 seconds
Output 201/1000: t=200000.0 yr, dE/E0=8.89e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 14 hours, 30 minutes, 57 seconds
  Estimated time remaining to next output: 2 minutes, 53 seconds
Output 202/1000: t=201000.0 yr, dE/E0=9.12e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 14 hours, 28 minutes, 11 seconds
  Estimated time remaining to next output: 2 minutes, 53 seconds
Output 203/1000: t=202000.0 yr, dE/E0=8.39e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 14 hours, 25 minutes, 26 seconds
  Estimated time remaining to next output: 2 minutes, 53 seconds
Output 204/1000: t=203000.0 yr, dE/E0=8.50e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 14 hours, 22 minutes, 41 seconds
  Estimated time remaining to next output: 2 minutes, 53 seconds
Output 205/1000: t=204000.0 yr, dE/E0=8.39e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 14 hours, 19 minutes, 56 seconds
  Estimated time remaining to next output: 2 minutes, 53 seconds
Output 206/1000: t=205000.0 yr, dE/E0=8.31e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 14 hours, 17 minutes, 14 seconds
  Estimated time remaining to next output: 2 minutes, 53 seconds
Output 207/1000: t=206000.0 yr, dE/E0=7.39e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 14 hours, 14 minutes, 29 seconds
  Estimated time remaining to next output: 2 minutes, 53 seconds
Output 208/1000: t=207000.0 yr, dE/E0=8.05e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 14 hours, 11 minutes, 45 seconds
  Estimated time remaining to next output: 2 minutes, 53 seconds
Output 209/1000: t=208000.0 yr, dE/E0=7.82e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 14 hours, 9 minutes
  Estimated time remaining to next output: 2 minutes, 53 seconds
Output 210/1000: t=209000.0 yr, dE/E0=8.17e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 14 hours, 6 minutes, 13 seconds
  Estimated time remaining to next output: 2 minutes, 53 seconds
Output 211/1000: t=210000.0 yr, dE/E0=7.86e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 14 hours, 3 minutes, 27 seconds
  Estimated time remaining to next output: 2 minutes, 53 seconds
Output 212/1000: t=211000.0 yr, dE/E0=7.60e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 14 hours, 39 seconds
  Estimated time remaining to next output: 2 minutes, 53 seconds
Output 213/1000: t=212000.0 yr, dE/E0=7.69e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 13 hours, 57 minutes, 54 seconds
  Estimated time remaining to next output: 2 minutes, 53 seconds
Output 214/1000: t=213000.0 yr, dE/E0=7.45e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 13 hours, 55 minutes, 8 seconds
  Estimated time remaining to next output: 2 minutes, 53 seconds
Output 215/1000: t=214000.0 yr, dE/E0=7.23e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 13 hours, 52 minutes, 23 seconds
  Estimated time remaining to next output: 2 minutes, 53 seconds
Output 216/1000: t=215000.0 yr, dE/E0=6.70e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 13 hours, 49 minutes, 37 seconds
  Estimated time remaining to next output: 2 minutes, 53 seconds
Output 217/1000: t=216000.0 yr, dE/E0=6.89e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 13 hours, 46 minutes, 50 seconds
  Estimated time remaining to next output: 2 minutes, 53 seconds
Output 218/1000: t=217000.0 yr, dE/E0=6.69e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 13 hours, 44 minutes, 3 seconds
  Estimated time remaining to next output: 2 minutes, 53 seconds
Output 219/1000: t=218000.0 yr, dE/E0=6.37e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 13 hours, 41 minutes, 15 seconds
  Estimated time remaining to next output: 2 minutes, 53 seconds
Output 220/1000: t=219000.0 yr, dE/E0=6.91e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 13 hours, 38 minutes, 27 seconds
  Estimated time remaining to next output: 2 minutes, 53 seconds
Output 221/1000: t=220000.0 yr, dE/E0=6.97e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 13 hours, 35 minutes, 40 seconds
  Estimated time remaining to next output: 2 minutes, 53 seconds
Output 222/1000: t=221000.0 yr, dE/E0=6.96e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 13 hours, 32 minutes, 53 seconds
  Estimated time remaining to next output: 2 minutes, 53 seconds
Output 223/1000: t=222000.0 yr, dE/E0=6.15e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 13 hours, 30 minutes, 5 seconds
  Estimated time remaining to next output: 2 minutes, 53 seconds
Output 224/1000: t=223000.0 yr, dE/E0=7.11e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 13 hours, 27 minutes, 18 seconds
  Estimated time remaining to next output: 2 minutes, 53 seconds
Output 225/1000: t=224000.0 yr, dE/E0=6.71e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 13 hours, 24 minutes, 28 seconds
  Estimated time remaining to next output: 2 minutes, 53 seconds
Output 226/1000: t=225000.0 yr, dE/E0=6.12e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 13 hours, 21 minutes, 41 seconds
  Estimated time remaining to next output: 2 minutes, 53 seconds
Output 227/1000: t=226000.0 yr, dE/E0=6.29e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 13 hours, 18 minutes, 54 seconds
  Estimated time remaining to next output: 2 minutes, 53 seconds
Output 228/1000: t=227000.0 yr, dE/E0=6.28e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 13 hours, 16 minutes, 8 seconds
  Estimated time remaining to next output: 2 minutes, 53 seconds
Output 229/1000: t=228000.0 yr, dE/E0=5.83e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 13 hours, 13 minutes, 20 seconds
  Estimated time remaining to next output: 2 minutes, 53 seconds
Output 230/1000: t=229000.0 yr, dE/E0=5.75e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 13 hours, 10 minutes, 28 seconds
  Estimated time remaining to next output: 2 minutes, 53 seconds
Output 231/1000: t=230000.0 yr, dE/E0=6.01e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 13 hours, 7 minutes, 39 seconds
  Estimated time remaining to next output: 2 minutes, 53 seconds
Output 232/1000: t=231000.0 yr, dE/E0=5.24e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 13 hours, 4 minutes, 49 seconds
  Estimated time remaining to next output: 2 minutes, 53 seconds
Output 233/1000: t=232000.0 yr, dE/E0=4.92e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 13 hours, 2 minutes, 2 seconds
  Estimated time remaining to next output: 2 minutes, 53 seconds
Output 234/1000: t=233000.0 yr, dE/E0=4.72e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 12 hours, 59 minutes, 15 seconds
  Estimated time remaining to next output: 2 minutes, 53 seconds
Output 235/1000: t=234000.0 yr, dE/E0=4.52e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 12 hours, 56 minutes, 29 seconds
  Estimated time remaining to next output: 2 minutes, 53 seconds
Output 236/1000: t=235000.0 yr, dE/E0=4.53e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 12 hours, 53 minutes, 43 seconds
  Estimated time remaining to next output: 2 minutes, 53 seconds
Output 237/1000: t=236000.0 yr, dE/E0=4.65e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 12 hours, 50 minutes, 57 seconds
  Estimated time remaining to next output: 2 minutes, 53 seconds
Output 238/1000: t=237000.0 yr, dE/E0=4.42e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 12 hours, 48 minutes, 11 seconds
  Estimated time remaining to next output: 2 minutes, 53 seconds
Output 239/1000: t=238000.0 yr, dE/E0=4.17e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 12 hours, 45 minutes, 22 seconds
  Estimated time remaining to next output: 2 minutes, 53 seconds
Output 240/1000: t=239000.0 yr, dE/E0=4.68e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 12 hours, 42 minutes, 36 seconds
  Estimated time remaining to next output: 2 minutes, 53 seconds
Output 241/1000: t=240000.0 yr, dE/E0=4.48e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 12 hours, 39 minutes, 50 seconds
  Estimated time remaining to next output: 2 minutes, 53 seconds
Output 242/1000: t=241000.0 yr, dE/E0=3.95e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 12 hours, 37 minutes, 3 seconds
  Estimated time remaining to next output: 2 minutes, 53 seconds
Output 243/1000: t=242000.0 yr, dE/E0=3.19e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 12 hours, 34 minutes, 15 seconds
  Estimated time remaining to next output: 2 minutes, 53 seconds
Output 244/1000: t=243000.0 yr, dE/E0=3.84e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 12 hours, 31 minutes, 28 seconds
  Estimated time remaining to next output: 2 minutes, 53 seconds
Output 245/1000: t=244000.0 yr, dE/E0=3.09e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 12 hours, 28 minutes, 40 seconds
  Estimated time remaining to next output: 2 minutes, 53 seconds
Output 246/1000: t=245000.0 yr, dE/E0=2.20e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 12 hours, 25 minutes, 53 seconds
  Estimated time remaining to next output: 2 minutes, 53 seconds
Output 247/1000: t=246000.0 yr, dE/E0=3.77e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 12 hours, 23 minutes, 4 seconds
  Estimated time remaining to next output: 2 minutes, 53 seconds
Output 248/1000: t=247000.0 yr, dE/E0=3.89e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 12 hours, 20 minutes, 16 seconds
  Estimated time remaining to next output: 2 minutes, 53 seconds
Output 249/1000: t=248000.0 yr, dE/E0=3.52e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 12 hours, 17 minutes, 29 seconds
  Estimated time remaining to next output: 2 minutes, 53 seconds
Output 250/1000: t=249000.0 yr, dE/E0=3.46e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 12 hours, 14 minutes, 40 seconds
  Estimated time remaining to next output: 2 minutes, 53 seconds
Output 251/1000: t=250000.0 yr, dE/E0=3.02e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 12 hours, 11 minutes, 51 seconds
  Estimated time remaining to next output: 2 minutes, 53 seconds
Output 252/1000: t=251000.0 yr, dE/E0=3.01e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 12 hours, 9 minutes, 3 seconds
  Estimated time remaining to next output: 2 minutes, 53 seconds
Output 253/1000: t=252000.0 yr, dE/E0=2.76e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 12 hours, 6 minutes, 14 seconds
  Estimated time remaining to next output: 2 minutes, 53 seconds
Output 254/1000: t=253000.0 yr, dE/E0=2.53e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 12 hours, 3 minutes, 27 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 255/1000: t=254000.0 yr, dE/E0=2.91e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 12 hours, 39 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 256/1000: t=255000.0 yr, dE/E0=2.35e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 11 hours, 57 minutes, 51 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 257/1000: t=256000.0 yr, dE/E0=1.79e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 11 hours, 55 minutes, 3 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 258/1000: t=257000.0 yr, dE/E0=2.47e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 11 hours, 52 minutes, 13 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 259/1000: t=258000.0 yr, dE/E0=2.63e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 11 hours, 49 minutes, 24 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 260/1000: t=259000.0 yr, dE/E0=2.52e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 11 hours, 46 minutes, 35 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 261/1000: t=260000.0 yr, dE/E0=2.26e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 11 hours, 43 minutes, 46 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 262/1000: t=261000.0 yr, dE/E0=2.21e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 11 hours, 40 minutes, 56 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 263/1000: t=262000.0 yr, dE/E0=1.58e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 11 hours, 38 minutes, 6 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 264/1000: t=263000.0 yr, dE/E0=1.51e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 11 hours, 35 minutes, 15 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 265/1000: t=264000.0 yr, dE/E0=1.19e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 11 hours, 32 minutes, 26 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 266/1000: t=265000.0 yr, dE/E0=1.82e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 11 hours, 29 minutes, 36 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 267/1000: t=266000.0 yr, dE/E0=2.63e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 11 hours, 26 minutes, 48 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 268/1000: t=267000.0 yr, dE/E0=3.03e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 11 hours, 23 minutes, 59 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 269/1000: t=268000.0 yr, dE/E0=4.20e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 11 hours, 21 minutes, 9 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 270/1000: t=269000.0 yr, dE/E0=3.58e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 11 hours, 18 minutes, 17 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 271/1000: t=270000.0 yr, dE/E0=3.53e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 11 hours, 15 minutes, 28 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 272/1000: t=271000.0 yr, dE/E0=3.48e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 11 hours, 12 minutes, 36 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 273/1000: t=272000.0 yr, dE/E0=4.06e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 11 hours, 9 minutes, 45 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 274/1000: t=273000.0 yr, dE/E0=4.10e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 11 hours, 6 minutes, 54 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 275/1000: t=274000.0 yr, dE/E0=4.45e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 11 hours, 4 minutes, 3 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 276/1000: t=275000.0 yr, dE/E0=4.40e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 11 hours, 1 minutes, 12 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 277/1000: t=276000.0 yr, dE/E0=4.46e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 10 hours, 58 minutes, 23 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 278/1000: t=277000.0 yr, dE/E0=4.48e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 10 hours, 55 minutes, 32 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 279/1000: t=278000.0 yr, dE/E0=4.97e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 10 hours, 52 minutes, 42 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 280/1000: t=279000.0 yr, dE/E0=4.94e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 10 hours, 49 minutes, 50 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 281/1000: t=280000.0 yr, dE/E0=4.62e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 10 hours, 46 minutes, 59 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 282/1000: t=281000.0 yr, dE/E0=4.90e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 10 hours, 44 minutes, 8 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 283/1000: t=282000.0 yr, dE/E0=5.09e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 10 hours, 41 minutes, 18 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 284/1000: t=283000.0 yr, dE/E0=5.65e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 10 hours, 38 minutes, 29 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 285/1000: t=284000.0 yr, dE/E0=5.84e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 10 hours, 35 minutes, 39 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 286/1000: t=285000.0 yr, dE/E0=5.77e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 10 hours, 32 minutes, 48 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 287/1000: t=286000.0 yr, dE/E0=5.41e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 10 hours, 29 minutes, 57 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 288/1000: t=287000.0 yr, dE/E0=5.72e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 10 hours, 27 minutes, 8 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 289/1000: t=288000.0 yr, dE/E0=5.55e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 10 hours, 24 minutes, 20 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 290/1000: t=289000.0 yr, dE/E0=5.85e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 10 hours, 21 minutes, 29 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 291/1000: t=290000.0 yr, dE/E0=5.41e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 10 hours, 18 minutes, 38 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 292/1000: t=291000.0 yr, dE/E0=4.86e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 10 hours, 15 minutes, 44 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 293/1000: t=292000.0 yr, dE/E0=5.18e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 10 hours, 12 minutes, 52 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 294/1000: t=293000.0 yr, dE/E0=4.47e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 10 hours, 9 minutes, 59 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 295/1000: t=294000.0 yr, dE/E0=4.32e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 10 hours, 7 minutes, 5 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 296/1000: t=295000.0 yr, dE/E0=3.67e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 10 hours, 4 minutes, 12 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 297/1000: t=296000.0 yr, dE/E0=3.53e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 10 hours, 1 minutes, 21 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 298/1000: t=297000.0 yr, dE/E0=3.29e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 9 hours, 58 minutes, 31 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 299/1000: t=298000.0 yr, dE/E0=3.10e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 9 hours, 55 minutes, 40 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 300/1000: t=299000.0 yr, dE/E0=3.13e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 9 hours, 52 minutes, 50 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 301/1000: t=300000.0 yr, dE/E0=3.63e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 9 hours, 50 minutes
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 302/1000: t=301000.0 yr, dE/E0=3.20e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 9 hours, 47 minutes, 9 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 303/1000: t=302000.0 yr, dE/E0=3.84e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 9 hours, 44 minutes, 17 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 304/1000: t=303000.0 yr, dE/E0=4.78e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 9 hours, 41 minutes, 27 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 305/1000: t=304000.0 yr, dE/E0=4.74e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 9 hours, 38 minutes, 36 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 306/1000: t=305000.0 yr, dE/E0=4.17e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 9 hours, 35 minutes, 45 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 307/1000: t=306000.0 yr, dE/E0=4.30e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 9 hours, 32 minutes, 54 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 308/1000: t=307000.0 yr, dE/E0=4.29e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 9 hours, 30 minutes, 3 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 309/1000: t=308000.0 yr, dE/E0=4.53e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 9 hours, 27 minutes, 12 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 310/1000: t=309000.0 yr, dE/E0=4.35e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 9 hours, 24 minutes, 22 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 311/1000: t=310000.0 yr, dE/E0=4.21e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 9 hours, 21 minutes, 31 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 312/1000: t=311000.0 yr, dE/E0=3.21e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 9 hours, 18 minutes, 39 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 313/1000: t=312000.0 yr, dE/E0=3.76e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 9 hours, 15 minutes, 48 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 314/1000: t=313000.0 yr, dE/E0=4.43e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 9 hours, 12 minutes, 57 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 315/1000: t=314000.0 yr, dE/E0=4.03e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 9 hours, 10 minutes, 7 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 316/1000: t=315000.0 yr, dE/E0=4.55e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 9 hours, 7 minutes, 17 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 317/1000: t=316000.0 yr, dE/E0=5.22e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 9 hours, 4 minutes, 26 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 318/1000: t=317000.0 yr, dE/E0=4.96e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 9 hours, 1 minutes, 37 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 319/1000: t=318000.0 yr, dE/E0=5.97e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 8 hours, 58 minutes, 47 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 320/1000: t=319000.0 yr, dE/E0=6.06e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 8 hours, 55 minutes, 57 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 321/1000: t=320000.0 yr, dE/E0=5.08e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 8 hours, 53 minutes, 6 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 322/1000: t=321000.0 yr, dE/E0=5.18e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 8 hours, 50 minutes, 15 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 323/1000: t=322000.0 yr, dE/E0=4.50e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 8 hours, 47 minutes, 24 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 324/1000: t=323000.0 yr, dE/E0=4.05e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 8 hours, 44 minutes, 32 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 325/1000: t=324000.0 yr, dE/E0=4.29e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 8 hours, 41 minutes, 41 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 326/1000: t=325000.0 yr, dE/E0=4.61e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 8 hours, 38 minutes, 49 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 327/1000: t=326000.0 yr, dE/E0=4.03e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 8 hours, 35 minutes, 58 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 328/1000: t=327000.0 yr, dE/E0=4.16e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 8 hours, 33 minutes, 8 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 329/1000: t=328000.0 yr, dE/E0=2.82e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 8 hours, 30 minutes, 18 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 330/1000: t=329000.0 yr, dE/E0=3.51e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 8 hours, 27 minutes, 27 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 331/1000: t=330000.0 yr, dE/E0=3.50e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 8 hours, 24 minutes, 34 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 332/1000: t=331000.0 yr, dE/E0=3.29e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 8 hours, 21 minutes, 42 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 333/1000: t=332000.0 yr, dE/E0=3.85e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 8 hours, 18 minutes, 52 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 334/1000: t=333000.0 yr, dE/E0=3.95e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 8 hours, 16 minutes
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 335/1000: t=334000.0 yr, dE/E0=4.67e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 8 hours, 13 minutes, 12 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 336/1000: t=335000.0 yr, dE/E0=4.29e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 8 hours, 10 minutes, 26 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 337/1000: t=336000.0 yr, dE/E0=3.57e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 8 hours, 7 minutes, 41 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 338/1000: t=337000.0 yr, dE/E0=2.17e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 8 hours, 4 minutes, 55 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 339/1000: t=338000.0 yr, dE/E0=6.20e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 8 hours, 2 minutes, 10 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 340/1000: t=339000.0 yr, dE/E0=2.11e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 7 hours, 59 minutes, 24 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 341/1000: t=340000.0 yr, dE/E0=3.95e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 7 hours, 56 minutes, 38 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 342/1000: t=341000.0 yr, dE/E0=2.71e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 7 hours, 53 minutes, 52 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 343/1000: t=342000.0 yr, dE/E0=6.45e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 7 hours, 51 minutes, 5 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 344/1000: t=343000.0 yr, dE/E0=1.34e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 7 hours, 48 minutes, 17 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 345/1000: t=344000.0 yr, dE/E0=1.50e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 7 hours, 45 minutes, 28 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 346/1000: t=345000.0 yr, dE/E0=1.74e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 7 hours, 42 minutes, 41 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 347/1000: t=346000.0 yr, dE/E0=1.92e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 7 hours, 39 minutes, 52 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 348/1000: t=347000.0 yr, dE/E0=2.22e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 7 hours, 37 minutes, 4 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 349/1000: t=348000.0 yr, dE/E0=2.13e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 7 hours, 34 minutes, 17 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 350/1000: t=349000.0 yr, dE/E0=1.34e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 7 hours, 31 minutes, 29 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 351/1000: t=350000.0 yr, dE/E0=9.03e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 7 hours, 28 minutes, 41 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 352/1000: t=351000.0 yr, dE/E0=6.52e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 7 hours, 25 minutes, 54 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 353/1000: t=352000.0 yr, dE/E0=1.91e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 7 hours, 23 minutes, 5 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 354/1000: t=353000.0 yr, dE/E0=2.70e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 7 hours, 20 minutes, 15 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 355/1000: t=354000.0 yr, dE/E0=1.93e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 7 hours, 17 minutes, 26 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 356/1000: t=355000.0 yr, dE/E0=1.46e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 7 hours, 14 minutes, 35 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 357/1000: t=356000.0 yr, dE/E0=1.27e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 7 hours, 11 minutes, 45 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 358/1000: t=357000.0 yr, dE/E0=6.89e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 7 hours, 8 minutes, 55 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 359/1000: t=358000.0 yr, dE/E0=8.08e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 7 hours, 6 minutes, 5 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 360/1000: t=359000.0 yr, dE/E0=4.24e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 7 hours, 3 minutes, 14 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 361/1000: t=360000.0 yr, dE/E0=5.80e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 7 hours, 23 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 362/1000: t=361000.0 yr, dE/E0=2.15e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 6 hours, 57 minutes, 32 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 363/1000: t=362000.0 yr, dE/E0=6.98e-10, N=101
  Estimated time remaining to complete simulation: 1 days, 6 hours, 54 minutes, 42 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 364/1000: t=363000.0 yr, dE/E0=1.24e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 6 hours, 51 minutes, 50 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 365/1000: t=364000.0 yr, dE/E0=8.63e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 6 hours, 49 minutes
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 366/1000: t=365000.0 yr, dE/E0=1.81e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 6 hours, 46 minutes, 10 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 367/1000: t=366000.0 yr, dE/E0=3.76e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 6 hours, 43 minutes, 19 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 368/1000: t=367000.0 yr, dE/E0=8.48e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 6 hours, 40 minutes, 27 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 369/1000: t=368000.0 yr, dE/E0=8.49e-10, N=101
  Estimated time remaining to complete simulation: 1 days, 6 hours, 37 minutes, 35 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 370/1000: t=369000.0 yr, dE/E0=2.85e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 6 hours, 34 minutes, 43 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 371/1000: t=370000.0 yr, dE/E0=1.36e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 6 hours, 31 minutes, 51 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 372/1000: t=371000.0 yr, dE/E0=2.58e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 6 hours, 28 minutes, 58 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 373/1000: t=372000.0 yr, dE/E0=1.97e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 6 hours, 26 minutes, 7 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 374/1000: t=373000.0 yr, dE/E0=2.08e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 6 hours, 23 minutes, 15 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 375/1000: t=374000.0 yr, dE/E0=1.47e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 6 hours, 20 minutes, 22 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 376/1000: t=375000.0 yr, dE/E0=2.27e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 6 hours, 17 minutes, 30 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 377/1000: t=376000.0 yr, dE/E0=2.37e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 6 hours, 14 minutes, 40 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 378/1000: t=377000.0 yr, dE/E0=2.22e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 6 hours, 11 minutes, 49 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 379/1000: t=378000.0 yr, dE/E0=2.40e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 6 hours, 8 minutes, 58 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 380/1000: t=379000.0 yr, dE/E0=3.98e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 6 hours, 6 minutes, 7 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 381/1000: t=380000.0 yr, dE/E0=3.20e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 6 hours, 3 minutes, 15 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 382/1000: t=381000.0 yr, dE/E0=2.98e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 6 hours, 23 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 383/1000: t=382000.0 yr, dE/E0=2.80e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 5 hours, 57 minutes, 33 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 384/1000: t=383000.0 yr, dE/E0=2.43e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 5 hours, 54 minutes, 42 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 385/1000: t=384000.0 yr, dE/E0=1.63e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 5 hours, 51 minutes, 49 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 386/1000: t=385000.0 yr, dE/E0=2.13e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 5 hours, 48 minutes, 59 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 387/1000: t=386000.0 yr, dE/E0=1.25e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 5 hours, 46 minutes, 8 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 388/1000: t=387000.0 yr, dE/E0=2.38e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 5 hours, 43 minutes, 17 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 389/1000: t=388000.0 yr, dE/E0=1.85e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 5 hours, 40 minutes, 24 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 390/1000: t=389000.0 yr, dE/E0=2.26e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 5 hours, 37 minutes, 33 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 391/1000: t=390000.0 yr, dE/E0=2.87e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 5 hours, 34 minutes, 39 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 392/1000: t=391000.0 yr, dE/E0=4.42e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 5 hours, 31 minutes, 46 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 393/1000: t=392000.0 yr, dE/E0=4.83e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 5 hours, 28 minutes, 53 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 394/1000: t=393000.0 yr, dE/E0=4.96e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 5 hours, 25 minutes, 58 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 395/1000: t=394000.0 yr, dE/E0=3.81e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 5 hours, 23 minutes, 5 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 396/1000: t=395000.0 yr, dE/E0=2.98e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 5 hours, 20 minutes, 13 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 397/1000: t=396000.0 yr, dE/E0=2.24e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 5 hours, 17 minutes, 19 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 398/1000: t=397000.0 yr, dE/E0=2.46e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 5 hours, 14 minutes, 27 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 399/1000: t=398000.0 yr, dE/E0=2.77e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 5 hours, 11 minutes, 33 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 400/1000: t=399000.0 yr, dE/E0=2.55e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 5 hours, 8 minutes, 40 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 401/1000: t=400000.0 yr, dE/E0=2.61e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 5 hours, 5 minutes, 48 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 402/1000: t=401000.0 yr, dE/E0=3.19e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 5 hours, 2 minutes, 56 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 403/1000: t=402000.0 yr, dE/E0=3.70e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 5 hours, 2 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 404/1000: t=403000.0 yr, dE/E0=4.18e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 4 hours, 57 minutes, 8 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 405/1000: t=404000.0 yr, dE/E0=5.33e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 4 hours, 54 minutes, 13 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 406/1000: t=405000.0 yr, dE/E0=5.67e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 4 hours, 51 minutes, 19 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 407/1000: t=406000.0 yr, dE/E0=5.54e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 4 hours, 48 minutes, 25 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 408/1000: t=407000.0 yr, dE/E0=5.08e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 4 hours, 45 minutes, 30 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 409/1000: t=408000.0 yr, dE/E0=5.44e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 4 hours, 42 minutes, 36 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 410/1000: t=409000.0 yr, dE/E0=5.20e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 4 hours, 39 minutes, 41 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 411/1000: t=410000.0 yr, dE/E0=4.73e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 4 hours, 36 minutes, 47 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 412/1000: t=411000.0 yr, dE/E0=4.70e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 4 hours, 33 minutes, 52 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 413/1000: t=412000.0 yr, dE/E0=3.99e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 4 hours, 30 minutes, 58 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 414/1000: t=413000.0 yr, dE/E0=3.88e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 4 hours, 28 minutes, 4 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 415/1000: t=414000.0 yr, dE/E0=3.58e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 4 hours, 25 minutes, 10 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 416/1000: t=415000.0 yr, dE/E0=1.77e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 4 hours, 22 minutes, 15 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 417/1000: t=416000.0 yr, dE/E0=9.38e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 4 hours, 19 minutes, 21 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 418/1000: t=417000.0 yr, dE/E0=1.33e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 4 hours, 16 minutes, 26 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 419/1000: t=418000.0 yr, dE/E0=6.41e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 4 hours, 13 minutes, 31 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 420/1000: t=419000.0 yr, dE/E0=5.50e-09, N=101
  Estimated time remaining to complete simulation: 1 days, 4 hours, 10 minutes, 36 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 421/1000: t=420000.0 yr, dE/E0=2.95e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 4 hours, 7 minutes, 42 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 422/1000: t=421000.0 yr, dE/E0=3.04e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 4 hours, 4 minutes, 47 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 423/1000: t=422000.0 yr, dE/E0=2.51e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 4 hours, 1 minutes, 53 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 424/1000: t=423000.0 yr, dE/E0=2.51e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 3 hours, 58 minutes, 58 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 425/1000: t=424000.0 yr, dE/E0=2.39e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 3 hours, 56 minutes, 3 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 426/1000: t=425000.0 yr, dE/E0=1.79e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 3 hours, 53 minutes, 9 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 427/1000: t=426000.0 yr, dE/E0=1.98e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 3 hours, 50 minutes, 15 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 428/1000: t=427000.0 yr, dE/E0=2.62e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 3 hours, 47 minutes, 21 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 429/1000: t=428000.0 yr, dE/E0=1.90e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 3 hours, 44 minutes, 27 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 430/1000: t=429000.0 yr, dE/E0=1.92e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 3 hours, 41 minutes, 32 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 431/1000: t=430000.0 yr, dE/E0=3.15e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 3 hours, 38 minutes, 37 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 432/1000: t=431000.0 yr, dE/E0=3.40e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 3 hours, 35 minutes, 42 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 433/1000: t=432000.0 yr, dE/E0=4.04e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 3 hours, 32 minutes, 48 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 434/1000: t=433000.0 yr, dE/E0=4.59e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 3 hours, 29 minutes, 54 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 435/1000: t=434000.0 yr, dE/E0=4.34e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 3 hours, 27 minutes
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 436/1000: t=435000.0 yr, dE/E0=4.42e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 3 hours, 24 minutes, 6 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 437/1000: t=436000.0 yr, dE/E0=5.26e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 3 hours, 21 minutes, 12 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 438/1000: t=437000.0 yr, dE/E0=5.90e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 3 hours, 18 minutes, 19 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 439/1000: t=438000.0 yr, dE/E0=7.01e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 3 hours, 15 minutes, 26 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 440/1000: t=439000.0 yr, dE/E0=7.43e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 3 hours, 12 minutes, 33 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 441/1000: t=440000.0 yr, dE/E0=7.59e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 3 hours, 9 minutes, 39 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 442/1000: t=441000.0 yr, dE/E0=7.11e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 3 hours, 6 minutes, 47 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 443/1000: t=442000.0 yr, dE/E0=7.55e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 3 hours, 3 minutes, 54 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 444/1000: t=443000.0 yr, dE/E0=7.95e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 3 hours, 1 minutes, 1 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 445/1000: t=444000.0 yr, dE/E0=8.01e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 2 hours, 58 minutes, 8 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 446/1000: t=445000.0 yr, dE/E0=9.17e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 2 hours, 55 minutes, 15 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 447/1000: t=446000.0 yr, dE/E0=9.28e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 2 hours, 52 minutes, 21 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 448/1000: t=447000.0 yr, dE/E0=9.88e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 2 hours, 49 minutes, 29 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 449/1000: t=448000.0 yr, dE/E0=9.35e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 2 hours, 46 minutes, 36 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 450/1000: t=449000.0 yr, dE/E0=9.78e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 2 hours, 43 minutes, 43 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 451/1000: t=450000.0 yr, dE/E0=1.09e-07, N=101
  Estimated time remaining to complete simulation: 1 days, 2 hours, 40 minutes, 51 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 452/1000: t=451000.0 yr, dE/E0=1.10e-07, N=101
  Estimated time remaining to complete simulation: 1 days, 2 hours, 37 minutes, 58 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 453/1000: t=452000.0 yr, dE/E0=1.01e-07, N=101
  Estimated time remaining to complete simulation: 1 days, 2 hours, 35 minutes, 6 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 454/1000: t=453000.0 yr, dE/E0=1.04e-07, N=101
  Estimated time remaining to complete simulation: 1 days, 2 hours, 32 minutes, 14 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 455/1000: t=454000.0 yr, dE/E0=1.13e-07, N=101
  Estimated time remaining to complete simulation: 1 days, 2 hours, 29 minutes, 21 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 456/1000: t=455000.0 yr, dE/E0=1.17e-07, N=101
  Estimated time remaining to complete simulation: 1 days, 2 hours, 26 minutes, 27 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 457/1000: t=456000.0 yr, dE/E0=1.20e-07, N=101
  Estimated time remaining to complete simulation: 1 days, 2 hours, 23 minutes, 34 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 458/1000: t=457000.0 yr, dE/E0=1.20e-07, N=101
  Estimated time remaining to complete simulation: 1 days, 2 hours, 20 minutes, 40 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 459/1000: t=458000.0 yr, dE/E0=1.24e-07, N=101
  Estimated time remaining to complete simulation: 1 days, 2 hours, 17 minutes, 46 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 460/1000: t=459000.0 yr, dE/E0=1.19e-07, N=101
  Estimated time remaining to complete simulation: 1 days, 2 hours, 14 minutes, 52 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 461/1000: t=460000.0 yr, dE/E0=1.22e-07, N=101
  Estimated time remaining to complete simulation: 1 days, 2 hours, 12 minutes, 1 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 462/1000: t=461000.0 yr, dE/E0=1.26e-07, N=101
  Estimated time remaining to complete simulation: 1 days, 2 hours, 9 minutes, 7 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 463/1000: t=462000.0 yr, dE/E0=1.27e-07, N=101
  Estimated time remaining to complete simulation: 1 days, 2 hours, 6 minutes, 13 seconds
  Estimated time remaining to next output: 2 minutes, 54 seconds
Output 464/1000: t=463000.0 yr, dE/E0=1.17e-07, N=101
  Estimated time remaining to complete simulation: 1 days, 2 hours, 3 minutes, 20 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 465/1000: t=464000.0 yr, dE/E0=1.31e-07, N=101
  Estimated time remaining to complete simulation: 1 days, 2 hours, 25 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 466/1000: t=465000.0 yr, dE/E0=1.25e-07, N=101
  Estimated time remaining to complete simulation: 1 days, 1 hours, 57 minutes, 32 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 467/1000: t=466000.0 yr, dE/E0=1.26e-07, N=101
  Estimated time remaining to complete simulation: 1 days, 1 hours, 54 minutes, 38 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 468/1000: t=467000.0 yr, dE/E0=1.37e-07, N=101
  Estimated time remaining to complete simulation: 1 days, 1 hours, 51 minutes, 45 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 469/1000: t=468000.0 yr, dE/E0=1.43e-07, N=101
  Estimated time remaining to complete simulation: 1 days, 1 hours, 48 minutes, 51 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 470/1000: t=469000.0 yr, dE/E0=1.30e-07, N=101
  Estimated time remaining to complete simulation: 1 days, 1 hours, 45 minutes, 57 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 471/1000: t=470000.0 yr, dE/E0=1.33e-07, N=101
  Estimated time remaining to complete simulation: 1 days, 1 hours, 43 minutes, 3 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 472/1000: t=471000.0 yr, dE/E0=1.37e-07, N=101
  Estimated time remaining to complete simulation: 1 days, 1 hours, 40 minutes, 10 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 473/1000: t=472000.0 yr, dE/E0=1.22e-07, N=101
  Estimated time remaining to complete simulation: 1 days, 1 hours, 37 minutes, 16 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 474/1000: t=473000.0 yr, dE/E0=1.22e-07, N=101
  Estimated time remaining to complete simulation: 1 days, 1 hours, 34 minutes, 22 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 475/1000: t=474000.0 yr, dE/E0=1.08e-07, N=101
  Estimated time remaining to complete simulation: 1 days, 1 hours, 31 minutes, 28 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 476/1000: t=475000.0 yr, dE/E0=1.04e-07, N=101
  Estimated time remaining to complete simulation: 1 days, 1 hours, 28 minutes, 35 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 477/1000: t=476000.0 yr, dE/E0=1.06e-07, N=101
  Estimated time remaining to complete simulation: 1 days, 1 hours, 25 minutes, 41 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 478/1000: t=477000.0 yr, dE/E0=1.06e-07, N=101
  Estimated time remaining to complete simulation: 1 days, 1 hours, 22 minutes, 47 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 479/1000: t=478000.0 yr, dE/E0=1.06e-07, N=101
  Estimated time remaining to complete simulation: 1 days, 1 hours, 19 minutes, 54 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 480/1000: t=479000.0 yr, dE/E0=1.01e-07, N=101
  Estimated time remaining to complete simulation: 1 days, 1 hours, 17 minutes
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 481/1000: t=480000.0 yr, dE/E0=9.25e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 1 hours, 14 minutes, 6 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 482/1000: t=481000.0 yr, dE/E0=1.01e-07, N=101
  Estimated time remaining to complete simulation: 1 days, 1 hours, 11 minutes, 13 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 483/1000: t=482000.0 yr, dE/E0=9.90e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 1 hours, 8 minutes, 19 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 484/1000: t=483000.0 yr, dE/E0=1.08e-07, N=101
  Estimated time remaining to complete simulation: 1 days, 1 hours, 5 minutes, 25 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 485/1000: t=484000.0 yr, dE/E0=1.09e-07, N=101
  Estimated time remaining to complete simulation: 1 days, 1 hours, 2 minutes, 31 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 486/1000: t=485000.0 yr, dE/E0=1.03e-07, N=101
  Estimated time remaining to complete simulation: 1 days, 59 minutes, 38 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 487/1000: t=486000.0 yr, dE/E0=1.07e-07, N=101
  Estimated time remaining to complete simulation: 1 days, 56 minutes, 44 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 488/1000: t=487000.0 yr, dE/E0=1.07e-07, N=101
  Estimated time remaining to complete simulation: 1 days, 53 minutes, 51 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 489/1000: t=488000.0 yr, dE/E0=1.11e-07, N=101
  Estimated time remaining to complete simulation: 1 days, 50 minutes, 57 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 490/1000: t=489000.0 yr, dE/E0=1.01e-07, N=101
  Estimated time remaining to complete simulation: 1 days, 48 minutes, 3 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 491/1000: t=490000.0 yr, dE/E0=9.67e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 45 minutes, 9 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 492/1000: t=491000.0 yr, dE/E0=1.07e-07, N=101
  Estimated time remaining to complete simulation: 1 days, 42 minutes, 16 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 493/1000: t=492000.0 yr, dE/E0=1.05e-07, N=101
  Estimated time remaining to complete simulation: 1 days, 39 minutes, 22 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 494/1000: t=493000.0 yr, dE/E0=1.12e-07, N=101
  Estimated time remaining to complete simulation: 1 days, 36 minutes, 27 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 495/1000: t=494000.0 yr, dE/E0=1.20e-07, N=101
  Estimated time remaining to complete simulation: 1 days, 33 minutes, 33 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 496/1000: t=495000.0 yr, dE/E0=1.14e-07, N=101
  Estimated time remaining to complete simulation: 1 days, 30 minutes, 40 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 497/1000: t=496000.0 yr, dE/E0=1.11e-07, N=101
  Estimated time remaining to complete simulation: 1 days, 27 minutes, 45 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 498/1000: t=497000.0 yr, dE/E0=1.05e-07, N=101
  Estimated time remaining to complete simulation: 1 days, 24 minutes, 51 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 499/1000: t=498000.0 yr, dE/E0=9.72e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 21 minutes, 57 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 500/1000: t=499000.0 yr, dE/E0=1.03e-07, N=101
  Estimated time remaining to complete simulation: 1 days, 19 minutes, 3 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 501/1000: t=500000.0 yr, dE/E0=9.78e-08, N=101
  Estimated time remaining to complete simulation: 1 days, 16 minutes, 9 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 502/1000: t=501000.0 yr, dE/E0=1.04e-07, N=101
  Estimated time remaining to complete simulation: 1 days, 13 minutes, 15 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 503/1000: t=502000.0 yr, dE/E0=1.20e-07, N=101
  Estimated time remaining to complete simulation: 1 days, 10 minutes, 21 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 504/1000: t=503000.0 yr, dE/E0=1.24e-07, N=101
  Estimated time remaining to complete simulation: 1 days, 7 minutes, 26 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 505/1000: t=504000.0 yr, dE/E0=1.35e-07, N=101
  Estimated time remaining to complete simulation: 1 days, 4 minutes, 33 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 506/1000: t=505000.0 yr, dE/E0=1.34e-07, N=101
  Estimated time remaining to complete simulation: 1 days, 1 minutes, 39 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 507/1000: t=506000.0 yr, dE/E0=1.30e-07, N=101
  Estimated time remaining to complete simulation: 23 hours, 58 minutes, 45 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 508/1000: t=507000.0 yr, dE/E0=1.30e-07, N=101
  Estimated time remaining to complete simulation: 23 hours, 55 minutes, 50 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 509/1000: t=508000.0 yr, dE/E0=1.35e-07, N=101
  Estimated time remaining to complete simulation: 23 hours, 52 minutes, 56 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 510/1000: t=509000.0 yr, dE/E0=1.44e-07, N=101
  Estimated time remaining to complete simulation: 23 hours, 50 minutes, 2 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 511/1000: t=510000.0 yr, dE/E0=1.54e-07, N=101
  Estimated time remaining to complete simulation: 23 hours, 47 minutes, 8 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 512/1000: t=511000.0 yr, dE/E0=1.57e-07, N=101
  Estimated time remaining to complete simulation: 23 hours, 44 minutes, 14 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 513/1000: t=512000.0 yr, dE/E0=1.45e-07, N=101
  Estimated time remaining to complete simulation: 23 hours, 41 minutes, 20 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 514/1000: t=513000.0 yr, dE/E0=1.61e-07, N=101
  Estimated time remaining to complete simulation: 23 hours, 38 minutes, 25 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 515/1000: t=514000.0 yr, dE/E0=1.67e-07, N=101
  Estimated time remaining to complete simulation: 23 hours, 35 minutes, 31 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 516/1000: t=515000.0 yr, dE/E0=1.77e-07, N=101
  Estimated time remaining to complete simulation: 23 hours, 32 minutes, 36 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 517/1000: t=516000.0 yr, dE/E0=1.85e-07, N=101
  Estimated time remaining to complete simulation: 23 hours, 29 minutes, 42 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 518/1000: t=517000.0 yr, dE/E0=1.76e-07, N=101
  Estimated time remaining to complete simulation: 23 hours, 26 minutes, 48 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 519/1000: t=518000.0 yr, dE/E0=1.69e-07, N=101
  Estimated time remaining to complete simulation: 23 hours, 23 minutes, 53 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 520/1000: t=519000.0 yr, dE/E0=1.86e-07, N=101
  Estimated time remaining to complete simulation: 23 hours, 20 minutes, 59 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 521/1000: t=520000.0 yr, dE/E0=1.84e-07, N=101
  Estimated time remaining to complete simulation: 23 hours, 18 minutes, 4 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 522/1000: t=521000.0 yr, dE/E0=1.67e-07, N=101
  Estimated time remaining to complete simulation: 23 hours, 15 minutes, 10 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 523/1000: t=522000.0 yr, dE/E0=1.80e-07, N=101
  Estimated time remaining to complete simulation: 23 hours, 12 minutes, 15 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 524/1000: t=523000.0 yr, dE/E0=1.67e-07, N=101
  Estimated time remaining to complete simulation: 23 hours, 9 minutes, 20 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 525/1000: t=524000.0 yr, dE/E0=1.74e-07, N=101
  Estimated time remaining to complete simulation: 23 hours, 6 minutes, 25 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 526/1000: t=525000.0 yr, dE/E0=1.88e-07, N=101
  Estimated time remaining to complete simulation: 23 hours, 3 minutes, 31 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 527/1000: t=526000.0 yr, dE/E0=2.03e-07, N=101
  Estimated time remaining to complete simulation: 23 hours, 36 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 528/1000: t=527000.0 yr, dE/E0=1.97e-07, N=101
  Estimated time remaining to complete simulation: 22 hours, 57 minutes, 42 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 529/1000: t=528000.0 yr, dE/E0=1.91e-07, N=101
  Estimated time remaining to complete simulation: 22 hours, 54 minutes, 48 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 530/1000: t=529000.0 yr, dE/E0=1.82e-07, N=101
  Estimated time remaining to complete simulation: 22 hours, 51 minutes, 53 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 531/1000: t=530000.0 yr, dE/E0=1.84e-07, N=101
  Estimated time remaining to complete simulation: 22 hours, 49 minutes
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 532/1000: t=531000.0 yr, dE/E0=1.77e-07, N=101
  Estimated time remaining to complete simulation: 22 hours, 46 minutes, 6 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 533/1000: t=532000.0 yr, dE/E0=1.76e-07, N=101
  Estimated time remaining to complete simulation: 22 hours, 43 minutes, 12 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 534/1000: t=533000.0 yr, dE/E0=1.73e-07, N=101
  Estimated time remaining to complete simulation: 22 hours, 40 minutes, 18 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 535/1000: t=534000.0 yr, dE/E0=1.79e-07, N=101
  Estimated time remaining to complete simulation: 22 hours, 37 minutes, 23 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 536/1000: t=535000.0 yr, dE/E0=1.97e-07, N=101
  Estimated time remaining to complete simulation: 22 hours, 34 minutes, 29 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 537/1000: t=536000.0 yr, dE/E0=2.03e-07, N=101
  Estimated time remaining to complete simulation: 22 hours, 31 minutes, 35 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 538/1000: t=537000.0 yr, dE/E0=2.19e-07, N=101
  Estimated time remaining to complete simulation: 22 hours, 28 minutes, 41 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 539/1000: t=538000.0 yr, dE/E0=2.22e-07, N=101
  Estimated time remaining to complete simulation: 22 hours, 25 minutes, 46 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 540/1000: t=539000.0 yr, dE/E0=2.22e-07, N=101
  Estimated time remaining to complete simulation: 22 hours, 22 minutes, 52 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 541/1000: t=540000.0 yr, dE/E0=2.23e-07, N=101
  Estimated time remaining to complete simulation: 22 hours, 19 minutes, 57 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 542/1000: t=541000.0 yr, dE/E0=2.30e-07, N=101
  Estimated time remaining to complete simulation: 22 hours, 17 minutes, 3 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 543/1000: t=542000.0 yr, dE/E0=2.23e-07, N=101
  Estimated time remaining to complete simulation: 22 hours, 14 minutes, 8 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 544/1000: t=543000.0 yr, dE/E0=2.15e-07, N=101
  Estimated time remaining to complete simulation: 22 hours, 11 minutes, 14 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 545/1000: t=544000.0 yr, dE/E0=2.25e-07, N=101
  Estimated time remaining to complete simulation: 22 hours, 8 minutes, 20 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 546/1000: t=545000.0 yr, dE/E0=2.13e-07, N=101
  Estimated time remaining to complete simulation: 22 hours, 5 minutes, 25 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 547/1000: t=546000.0 yr, dE/E0=2.14e-07, N=101
  Estimated time remaining to complete simulation: 22 hours, 2 minutes, 30 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 548/1000: t=547000.0 yr, dE/E0=2.24e-07, N=101
  Estimated time remaining to complete simulation: 21 hours, 59 minutes, 36 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 549/1000: t=548000.0 yr, dE/E0=2.27e-07, N=101
  Estimated time remaining to complete simulation: 21 hours, 56 minutes, 41 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 550/1000: t=549000.0 yr, dE/E0=2.42e-07, N=101
  Estimated time remaining to complete simulation: 21 hours, 53 minutes, 47 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 551/1000: t=550000.0 yr, dE/E0=2.35e-07, N=101
  Estimated time remaining to complete simulation: 21 hours, 50 minutes, 52 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 552/1000: t=551000.0 yr, dE/E0=2.41e-07, N=101
  Estimated time remaining to complete simulation: 21 hours, 47 minutes, 58 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 553/1000: t=552000.0 yr, dE/E0=2.47e-07, N=101
  Estimated time remaining to complete simulation: 21 hours, 45 minutes, 3 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 554/1000: t=553000.0 yr, dE/E0=2.38e-07, N=101
  Estimated time remaining to complete simulation: 21 hours, 42 minutes, 8 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 555/1000: t=554000.0 yr, dE/E0=2.29e-07, N=101
  Estimated time remaining to complete simulation: 21 hours, 39 minutes, 14 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 556/1000: t=555000.0 yr, dE/E0=2.11e-07, N=101
  Estimated time remaining to complete simulation: 21 hours, 36 minutes, 19 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 557/1000: t=556000.0 yr, dE/E0=2.04e-07, N=101
  Estimated time remaining to complete simulation: 21 hours, 33 minutes, 24 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 558/1000: t=557000.0 yr, dE/E0=2.31e-07, N=101
  Estimated time remaining to complete simulation: 21 hours, 30 minutes, 29 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 559/1000: t=558000.0 yr, dE/E0=2.63e-07, N=101
  Estimated time remaining to complete simulation: 21 hours, 27 minutes, 34 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 560/1000: t=559000.0 yr, dE/E0=2.48e-07, N=101
  Estimated time remaining to complete simulation: 21 hours, 24 minutes, 39 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 561/1000: t=560000.0 yr, dE/E0=2.41e-07, N=101
  Estimated time remaining to complete simulation: 21 hours, 21 minutes, 43 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 562/1000: t=561000.0 yr, dE/E0=2.42e-07, N=101
  Estimated time remaining to complete simulation: 21 hours, 18 minutes, 48 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 563/1000: t=562000.0 yr, dE/E0=2.28e-07, N=101
  Estimated time remaining to complete simulation: 21 hours, 15 minutes, 53 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 564/1000: t=563000.0 yr, dE/E0=2.36e-07, N=101
  Estimated time remaining to complete simulation: 21 hours, 12 minutes, 58 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 565/1000: t=564000.0 yr, dE/E0=2.37e-07, N=101
  Estimated time remaining to complete simulation: 21 hours, 10 minutes, 3 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 566/1000: t=565000.0 yr, dE/E0=2.44e-07, N=101
  Estimated time remaining to complete simulation: 21 hours, 7 minutes, 8 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 567/1000: t=566000.0 yr, dE/E0=2.53e-07, N=101
  Estimated time remaining to complete simulation: 21 hours, 4 minutes, 13 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 568/1000: t=567000.0 yr, dE/E0=2.59e-07, N=101
  Estimated time remaining to complete simulation: 21 hours, 1 minutes, 18 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 569/1000: t=568000.0 yr, dE/E0=2.72e-07, N=101
  Estimated time remaining to complete simulation: 20 hours, 58 minutes, 23 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 570/1000: t=569000.0 yr, dE/E0=2.73e-07, N=101
  Estimated time remaining to complete simulation: 20 hours, 55 minutes, 28 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 571/1000: t=570000.0 yr, dE/E0=2.68e-07, N=101
  Estimated time remaining to complete simulation: 20 hours, 52 minutes, 33 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 572/1000: t=571000.0 yr, dE/E0=2.88e-07, N=101
  Estimated time remaining to complete simulation: 20 hours, 49 minutes, 38 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 573/1000: t=572000.0 yr, dE/E0=2.95e-07, N=101
  Estimated time remaining to complete simulation: 20 hours, 46 minutes, 43 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 574/1000: t=573000.0 yr, dE/E0=2.97e-07, N=101
  Estimated time remaining to complete simulation: 20 hours, 43 minutes, 49 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 575/1000: t=574000.0 yr, dE/E0=3.03e-07, N=101
  Estimated time remaining to complete simulation: 20 hours, 40 minutes, 54 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 576/1000: t=575000.0 yr, dE/E0=3.28e-07, N=101
  Estimated time remaining to complete simulation: 20 hours, 37 minutes, 59 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 577/1000: t=576000.0 yr, dE/E0=3.39e-07, N=101
  Estimated time remaining to complete simulation: 20 hours, 35 minutes, 4 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 578/1000: t=577000.0 yr, dE/E0=3.39e-07, N=101
  Estimated time remaining to complete simulation: 20 hours, 32 minutes, 9 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 579/1000: t=578000.0 yr, dE/E0=3.57e-07, N=101
  Estimated time remaining to complete simulation: 20 hours, 29 minutes, 14 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 580/1000: t=579000.0 yr, dE/E0=3.66e-07, N=101
  Estimated time remaining to complete simulation: 20 hours, 26 minutes, 19 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 581/1000: t=580000.0 yr, dE/E0=3.85e-07, N=101
  Estimated time remaining to complete simulation: 20 hours, 23 minutes, 23 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 582/1000: t=581000.0 yr, dE/E0=3.89e-07, N=101
  Estimated time remaining to complete simulation: 20 hours, 20 minutes, 28 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 583/1000: t=582000.0 yr, dE/E0=3.92e-07, N=101
  Estimated time remaining to complete simulation: 20 hours, 17 minutes, 33 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 584/1000: t=583000.0 yr, dE/E0=3.94e-07, N=101
  Estimated time remaining to complete simulation: 20 hours, 14 minutes, 38 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 585/1000: t=584000.0 yr, dE/E0=4.03e-07, N=101
  Estimated time remaining to complete simulation: 20 hours, 11 minutes, 43 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 586/1000: t=585000.0 yr, dE/E0=3.99e-07, N=101
  Estimated time remaining to complete simulation: 20 hours, 8 minutes, 48 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 587/1000: t=586000.0 yr, dE/E0=4.10e-07, N=101
  Estimated time remaining to complete simulation: 20 hours, 5 minutes, 52 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 588/1000: t=587000.0 yr, dE/E0=4.23e-07, N=101
  Estimated time remaining to complete simulation: 20 hours, 2 minutes, 57 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 589/1000: t=588000.0 yr, dE/E0=4.33e-07, N=101
  Estimated time remaining to complete simulation: 20 hours, 3 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 590/1000: t=589000.0 yr, dE/E0=4.32e-07, N=101
  Estimated time remaining to complete simulation: 19 hours, 57 minutes, 8 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 591/1000: t=590000.0 yr, dE/E0=4.40e-07, N=101
  Estimated time remaining to complete simulation: 19 hours, 54 minutes, 13 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 592/1000: t=591000.0 yr, dE/E0=4.35e-07, N=101
  Estimated time remaining to complete simulation: 19 hours, 51 minutes, 18 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 593/1000: t=592000.0 yr, dE/E0=4.41e-07, N=101
  Estimated time remaining to complete simulation: 19 hours, 48 minutes, 22 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 594/1000: t=593000.0 yr, dE/E0=4.39e-07, N=101
  Estimated time remaining to complete simulation: 19 hours, 45 minutes, 27 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 595/1000: t=594000.0 yr, dE/E0=4.50e-07, N=101
  Estimated time remaining to complete simulation: 19 hours, 42 minutes, 32 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 596/1000: t=595000.0 yr, dE/E0=4.58e-07, N=101
  Estimated time remaining to complete simulation: 19 hours, 39 minutes, 37 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 597/1000: t=596000.0 yr, dE/E0=4.55e-07, N=101
  Estimated time remaining to complete simulation: 19 hours, 36 minutes, 42 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 598/1000: t=597000.0 yr, dE/E0=4.54e-07, N=101
  Estimated time remaining to complete simulation: 19 hours, 33 minutes, 47 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 599/1000: t=598000.0 yr, dE/E0=4.55e-07, N=101
  Estimated time remaining to complete simulation: 19 hours, 30 minutes, 51 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 600/1000: t=599000.0 yr, dE/E0=4.47e-07, N=101
  Estimated time remaining to complete simulation: 19 hours, 27 minutes, 56 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 601/1000: t=600000.0 yr, dE/E0=4.62e-07, N=101
  Estimated time remaining to complete simulation: 19 hours, 25 minutes, 1 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 602/1000: t=601000.0 yr, dE/E0=4.63e-07, N=101
  Estimated time remaining to complete simulation: 19 hours, 22 minutes, 6 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 603/1000: t=602000.0 yr, dE/E0=4.74e-07, N=101
  Estimated time remaining to complete simulation: 19 hours, 19 minutes, 11 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 604/1000: t=603000.0 yr, dE/E0=4.83e-07, N=101
  Estimated time remaining to complete simulation: 19 hours, 16 minutes, 16 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 605/1000: t=604000.0 yr, dE/E0=4.81e-07, N=101
  Estimated time remaining to complete simulation: 19 hours, 13 minutes, 20 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 606/1000: t=605000.0 yr, dE/E0=5.06e-07, N=101
  Estimated time remaining to complete simulation: 19 hours, 10 minutes, 25 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 607/1000: t=606000.0 yr, dE/E0=5.00e-07, N=101
  Estimated time remaining to complete simulation: 19 hours, 7 minutes, 29 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 608/1000: t=607000.0 yr, dE/E0=5.00e-07, N=101
  Estimated time remaining to complete simulation: 19 hours, 4 minutes, 34 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 609/1000: t=608000.0 yr, dE/E0=5.02e-07, N=101
  Estimated time remaining to complete simulation: 19 hours, 1 minutes, 39 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 610/1000: t=609000.0 yr, dE/E0=4.98e-07, N=101
  Estimated time remaining to complete simulation: 18 hours, 58 minutes, 43 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 611/1000: t=610000.0 yr, dE/E0=5.07e-07, N=101
  Estimated time remaining to complete simulation: 18 hours, 55 minutes, 48 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 612/1000: t=611000.0 yr, dE/E0=5.09e-07, N=101
  Estimated time remaining to complete simulation: 18 hours, 52 minutes, 53 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 613/1000: t=612000.0 yr, dE/E0=5.20e-07, N=101
  Estimated time remaining to complete simulation: 18 hours, 49 minutes, 58 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 614/1000: t=613000.0 yr, dE/E0=5.36e-07, N=101
  Estimated time remaining to complete simulation: 18 hours, 47 minutes, 2 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 615/1000: t=614000.0 yr, dE/E0=5.37e-07, N=101
  Estimated time remaining to complete simulation: 18 hours, 44 minutes, 7 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 616/1000: t=615000.0 yr, dE/E0=5.42e-07, N=101
  Estimated time remaining to complete simulation: 18 hours, 41 minutes, 12 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 617/1000: t=616000.0 yr, dE/E0=5.38e-07, N=101
  Estimated time remaining to complete simulation: 18 hours, 38 minutes, 16 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 618/1000: t=617000.0 yr, dE/E0=5.46e-07, N=101
  Estimated time remaining to complete simulation: 18 hours, 35 minutes, 21 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 619/1000: t=618000.0 yr, dE/E0=5.33e-07, N=101
  Estimated time remaining to complete simulation: 18 hours, 32 minutes, 26 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 620/1000: t=619000.0 yr, dE/E0=5.26e-07, N=101
  Estimated time remaining to complete simulation: 18 hours, 29 minutes, 30 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 621/1000: t=620000.0 yr, dE/E0=5.24e-07, N=101
  Estimated time remaining to complete simulation: 18 hours, 26 minutes, 35 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 622/1000: t=621000.0 yr, dE/E0=5.27e-07, N=101
  Estimated time remaining to complete simulation: 18 hours, 23 minutes, 39 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 623/1000: t=622000.0 yr, dE/E0=5.19e-07, N=101
  Estimated time remaining to complete simulation: 18 hours, 20 minutes, 44 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 624/1000: t=623000.0 yr, dE/E0=5.31e-07, N=101
  Estimated time remaining to complete simulation: 18 hours, 17 minutes, 48 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 625/1000: t=624000.0 yr, dE/E0=5.33e-07, N=101
  Estimated time remaining to complete simulation: 18 hours, 14 minutes, 53 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 626/1000: t=625000.0 yr, dE/E0=5.56e-07, N=101
  Estimated time remaining to complete simulation: 18 hours, 11 minutes, 57 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 627/1000: t=626000.0 yr, dE/E0=5.47e-07, N=101
  Estimated time remaining to complete simulation: 18 hours, 9 minutes, 2 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 628/1000: t=627000.0 yr, dE/E0=5.47e-07, N=101
  Estimated time remaining to complete simulation: 18 hours, 6 minutes, 7 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 629/1000: t=628000.0 yr, dE/E0=5.49e-07, N=101
  Estimated time remaining to complete simulation: 18 hours, 3 minutes, 12 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 630/1000: t=629000.0 yr, dE/E0=5.45e-07, N=101
  Estimated time remaining to complete simulation: 18 hours, 17 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 631/1000: t=630000.0 yr, dE/E0=5.47e-07, N=101
  Estimated time remaining to complete simulation: 17 hours, 57 minutes, 21 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 632/1000: t=631000.0 yr, dE/E0=5.54e-07, N=101
  Estimated time remaining to complete simulation: 17 hours, 54 minutes, 26 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 633/1000: t=632000.0 yr, dE/E0=5.68e-07, N=101
  Estimated time remaining to complete simulation: 17 hours, 51 minutes, 31 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 634/1000: t=633000.0 yr, dE/E0=5.70e-07, N=101
  Estimated time remaining to complete simulation: 17 hours, 48 minutes, 36 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 635/1000: t=634000.0 yr, dE/E0=5.76e-07, N=101
  Estimated time remaining to complete simulation: 17 hours, 45 minutes, 41 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 636/1000: t=635000.0 yr, dE/E0=5.87e-07, N=101
  Estimated time remaining to complete simulation: 17 hours, 42 minutes, 45 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 637/1000: t=636000.0 yr, dE/E0=5.97e-07, N=101
  Estimated time remaining to complete simulation: 17 hours, 39 minutes, 50 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 638/1000: t=637000.0 yr, dE/E0=5.86e-07, N=101
  Estimated time remaining to complete simulation: 17 hours, 36 minutes, 55 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 639/1000: t=638000.0 yr, dE/E0=5.84e-07, N=101
  Estimated time remaining to complete simulation: 17 hours, 34 minutes
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 640/1000: t=639000.0 yr, dE/E0=5.79e-07, N=101
  Estimated time remaining to complete simulation: 17 hours, 31 minutes, 5 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 641/1000: t=640000.0 yr, dE/E0=5.84e-07, N=101
  Estimated time remaining to complete simulation: 17 hours, 28 minutes, 10 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 642/1000: t=641000.0 yr, dE/E0=5.82e-07, N=101
  Estimated time remaining to complete simulation: 17 hours, 25 minutes, 15 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 643/1000: t=642000.0 yr, dE/E0=5.81e-07, N=101
  Estimated time remaining to complete simulation: 17 hours, 22 minutes, 20 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 644/1000: t=643000.0 yr, dE/E0=5.83e-07, N=101
  Estimated time remaining to complete simulation: 17 hours, 19 minutes, 25 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 645/1000: t=644000.0 yr, dE/E0=5.85e-07, N=101
  Estimated time remaining to complete simulation: 17 hours, 16 minutes, 29 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 646/1000: t=645000.0 yr, dE/E0=5.91e-07, N=101
  Estimated time remaining to complete simulation: 17 hours, 13 minutes, 34 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 647/1000: t=646000.0 yr, dE/E0=5.96e-07, N=101
  Estimated time remaining to complete simulation: 17 hours, 10 minutes, 39 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 648/1000: t=647000.0 yr, dE/E0=5.98e-07, N=101
  Estimated time remaining to complete simulation: 17 hours, 7 minutes, 44 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 649/1000: t=648000.0 yr, dE/E0=5.78e-07, N=101
  Estimated time remaining to complete simulation: 17 hours, 4 minutes, 48 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 650/1000: t=649000.0 yr, dE/E0=5.82e-07, N=101
  Estimated time remaining to complete simulation: 17 hours, 1 minutes, 53 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 651/1000: t=650000.0 yr, dE/E0=5.81e-07, N=101
  Estimated time remaining to complete simulation: 16 hours, 58 minutes, 58 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 652/1000: t=651000.0 yr, dE/E0=5.83e-07, N=101
  Estimated time remaining to complete simulation: 16 hours, 56 minutes, 3 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 653/1000: t=652000.0 yr, dE/E0=5.86e-07, N=101
  Estimated time remaining to complete simulation: 16 hours, 53 minutes, 7 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 654/1000: t=653000.0 yr, dE/E0=5.88e-07, N=101
  Estimated time remaining to complete simulation: 16 hours, 50 minutes, 12 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 655/1000: t=654000.0 yr, dE/E0=5.99e-07, N=101
  Estimated time remaining to complete simulation: 16 hours, 47 minutes, 17 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 656/1000: t=655000.0 yr, dE/E0=6.08e-07, N=101
  Estimated time remaining to complete simulation: 16 hours, 44 minutes, 21 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 657/1000: t=656000.0 yr, dE/E0=6.25e-07, N=101
  Estimated time remaining to complete simulation: 16 hours, 41 minutes, 27 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 658/1000: t=657000.0 yr, dE/E0=6.38e-07, N=101
  Estimated time remaining to complete simulation: 16 hours, 38 minutes, 32 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 659/1000: t=658000.0 yr, dE/E0=6.50e-07, N=101
  Estimated time remaining to complete simulation: 16 hours, 35 minutes, 38 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 660/1000: t=659000.0 yr, dE/E0=6.54e-07, N=101
  Estimated time remaining to complete simulation: 16 hours, 32 minutes, 43 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 661/1000: t=660000.0 yr, dE/E0=6.50e-07, N=101
  Estimated time remaining to complete simulation: 16 hours, 29 minutes, 49 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 662/1000: t=661000.0 yr, dE/E0=6.49e-07, N=101
  Estimated time remaining to complete simulation: 16 hours, 26 minutes, 55 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 663/1000: t=662000.0 yr, dE/E0=6.62e-07, N=101
  Estimated time remaining to complete simulation: 16 hours, 24 minutes, 1 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 664/1000: t=663000.0 yr, dE/E0=6.52e-07, N=101
  Estimated time remaining to complete simulation: 16 hours, 21 minutes, 6 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 665/1000: t=664000.0 yr, dE/E0=6.36e-07, N=101
  Estimated time remaining to complete simulation: 16 hours, 18 minutes, 12 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 666/1000: t=665000.0 yr, dE/E0=6.37e-07, N=101
  Estimated time remaining to complete simulation: 16 hours, 15 minutes, 17 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 667/1000: t=666000.0 yr, dE/E0=6.32e-07, N=101
  Estimated time remaining to complete simulation: 16 hours, 12 minutes, 23 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 668/1000: t=667000.0 yr, dE/E0=6.48e-07, N=101
  Estimated time remaining to complete simulation: 16 hours, 9 minutes, 29 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 669/1000: t=668000.0 yr, dE/E0=6.53e-07, N=101
  Estimated time remaining to complete simulation: 16 hours, 6 minutes, 34 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 670/1000: t=669000.0 yr, dE/E0=6.51e-07, N=101
  Estimated time remaining to complete simulation: 16 hours, 3 minutes, 39 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 671/1000: t=670000.0 yr, dE/E0=6.43e-07, N=101
  Estimated time remaining to complete simulation: 16 hours, 44 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 672/1000: t=671000.0 yr, dE/E0=6.44e-07, N=101
  Estimated time remaining to complete simulation: 15 hours, 57 minutes, 50 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 673/1000: t=672000.0 yr, dE/E0=6.37e-07, N=101
  Estimated time remaining to complete simulation: 15 hours, 54 minutes, 55 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 674/1000: t=673000.0 yr, dE/E0=6.34e-07, N=101
  Estimated time remaining to complete simulation: 15 hours, 52 minutes
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 675/1000: t=674000.0 yr, dE/E0=6.37e-07, N=101
  Estimated time remaining to complete simulation: 15 hours, 49 minutes, 5 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 676/1000: t=675000.0 yr, dE/E0=6.47e-07, N=101
  Estimated time remaining to complete simulation: 15 hours, 46 minutes, 11 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 677/1000: t=676000.0 yr, dE/E0=6.49e-07, N=101
  Estimated time remaining to complete simulation: 15 hours, 43 minutes, 16 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 678/1000: t=677000.0 yr, dE/E0=6.52e-07, N=101
  Estimated time remaining to complete simulation: 15 hours, 40 minutes, 22 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 679/1000: t=678000.0 yr, dE/E0=6.46e-07, N=101
  Estimated time remaining to complete simulation: 15 hours, 37 minutes, 27 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 680/1000: t=679000.0 yr, dE/E0=6.45e-07, N=101
  Estimated time remaining to complete simulation: 15 hours, 34 minutes, 32 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 681/1000: t=680000.0 yr, dE/E0=6.52e-07, N=101
  Estimated time remaining to complete simulation: 15 hours, 31 minutes, 37 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 682/1000: t=681000.0 yr, dE/E0=6.56e-07, N=101
  Estimated time remaining to complete simulation: 15 hours, 28 minutes, 43 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 683/1000: t=682000.0 yr, dE/E0=6.60e-07, N=101
  Estimated time remaining to complete simulation: 15 hours, 25 minutes, 47 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 684/1000: t=683000.0 yr, dE/E0=6.87e-07, N=101
  Estimated time remaining to complete simulation: 15 hours, 22 minutes, 52 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 685/1000: t=684000.0 yr, dE/E0=6.94e-07, N=101
  Estimated time remaining to complete simulation: 15 hours, 19 minutes, 57 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 686/1000: t=685000.0 yr, dE/E0=6.99e-07, N=101
  Estimated time remaining to complete simulation: 15 hours, 17 minutes, 2 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 687/1000: t=686000.0 yr, dE/E0=7.06e-07, N=101
  Estimated time remaining to complete simulation: 15 hours, 14 minutes, 8 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 688/1000: t=687000.0 yr, dE/E0=7.18e-07, N=101
  Estimated time remaining to complete simulation: 15 hours, 11 minutes, 13 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 689/1000: t=688000.0 yr, dE/E0=7.10e-07, N=101
  Estimated time remaining to complete simulation: 15 hours, 8 minutes, 18 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 690/1000: t=689000.0 yr, dE/E0=7.08e-07, N=101
  Estimated time remaining to complete simulation: 15 hours, 5 minutes, 23 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 691/1000: t=690000.0 yr, dE/E0=7.16e-07, N=101
  Estimated time remaining to complete simulation: 15 hours, 2 minutes, 28 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 692/1000: t=691000.0 yr, dE/E0=6.90e-07, N=101
  Estimated time remaining to complete simulation: 14 hours, 59 minutes, 32 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 693/1000: t=692000.0 yr, dE/E0=6.88e-07, N=101
  Estimated time remaining to complete simulation: 14 hours, 56 minutes, 37 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 694/1000: t=693000.0 yr, dE/E0=7.01e-07, N=101
  Estimated time remaining to complete simulation: 14 hours, 53 minutes, 42 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 695/1000: t=694000.0 yr, dE/E0=7.17e-07, N=101
  Estimated time remaining to complete simulation: 14 hours, 50 minutes, 47 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 696/1000: t=695000.0 yr, dE/E0=7.14e-07, N=101
  Estimated time remaining to complete simulation: 14 hours, 47 minutes, 51 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 697/1000: t=696000.0 yr, dE/E0=7.09e-07, N=101
  Estimated time remaining to complete simulation: 14 hours, 44 minutes, 57 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 698/1000: t=697000.0 yr, dE/E0=7.11e-07, N=101
  Estimated time remaining to complete simulation: 14 hours, 42 minutes, 2 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 699/1000: t=698000.0 yr, dE/E0=7.12e-07, N=101
  Estimated time remaining to complete simulation: 14 hours, 39 minutes, 7 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 700/1000: t=699000.0 yr, dE/E0=7.26e-07, N=101
  Estimated time remaining to complete simulation: 14 hours, 36 minutes, 12 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 701/1000: t=700000.0 yr, dE/E0=7.30e-07, N=101
  Estimated time remaining to complete simulation: 14 hours, 33 minutes, 17 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 702/1000: t=701000.0 yr, dE/E0=7.27e-07, N=101
  Estimated time remaining to complete simulation: 14 hours, 30 minutes, 22 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 703/1000: t=702000.0 yr, dE/E0=7.41e-07, N=101
  Estimated time remaining to complete simulation: 14 hours, 27 minutes, 27 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 704/1000: t=703000.0 yr, dE/E0=7.47e-07, N=101
  Estimated time remaining to complete simulation: 14 hours, 24 minutes, 32 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 705/1000: t=704000.0 yr, dE/E0=7.53e-07, N=101
  Estimated time remaining to complete simulation: 14 hours, 21 minutes, 37 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 706/1000: t=705000.0 yr, dE/E0=7.44e-07, N=101
  Estimated time remaining to complete simulation: 14 hours, 18 minutes, 43 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 707/1000: t=706000.0 yr, dE/E0=7.40e-07, N=101
  Estimated time remaining to complete simulation: 14 hours, 15 minutes, 48 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 708/1000: t=707000.0 yr, dE/E0=7.55e-07, N=101
  Estimated time remaining to complete simulation: 14 hours, 12 minutes, 54 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 709/1000: t=708000.0 yr, dE/E0=7.68e-07, N=101
  Estimated time remaining to complete simulation: 14 hours, 10 minutes
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 710/1000: t=709000.0 yr, dE/E0=7.76e-07, N=101
  Estimated time remaining to complete simulation: 14 hours, 7 minutes, 5 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 711/1000: t=710000.0 yr, dE/E0=7.81e-07, N=101
  Estimated time remaining to complete simulation: 14 hours, 4 minutes, 10 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 712/1000: t=711000.0 yr, dE/E0=8.00e-07, N=101
  Estimated time remaining to complete simulation: 14 hours, 1 minutes, 15 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 713/1000: t=712000.0 yr, dE/E0=7.99e-07, N=101
  Estimated time remaining to complete simulation: 13 hours, 58 minutes, 20 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 714/1000: t=713000.0 yr, dE/E0=8.00e-07, N=101
  Estimated time remaining to complete simulation: 13 hours, 55 minutes, 25 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 715/1000: t=714000.0 yr, dE/E0=7.99e-07, N=101
  Estimated time remaining to complete simulation: 13 hours, 52 minutes, 31 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 716/1000: t=715000.0 yr, dE/E0=8.00e-07, N=101
  Estimated time remaining to complete simulation: 13 hours, 49 minutes, 36 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 717/1000: t=716000.0 yr, dE/E0=7.94e-07, N=101
  Estimated time remaining to complete simulation: 13 hours, 46 minutes, 42 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 718/1000: t=717000.0 yr, dE/E0=8.07e-07, N=101
  Estimated time remaining to complete simulation: 13 hours, 43 minutes, 47 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 719/1000: t=718000.0 yr, dE/E0=8.07e-07, N=101
  Estimated time remaining to complete simulation: 13 hours, 40 minutes, 52 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 720/1000: t=719000.0 yr, dE/E0=8.22e-07, N=101
  Estimated time remaining to complete simulation: 13 hours, 37 minutes, 58 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 721/1000: t=720000.0 yr, dE/E0=8.34e-07, N=101
  Estimated time remaining to complete simulation: 13 hours, 35 minutes, 3 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 722/1000: t=721000.0 yr, dE/E0=8.31e-07, N=101
  Estimated time remaining to complete simulation: 13 hours, 32 minutes, 8 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 723/1000: t=722000.0 yr, dE/E0=8.17e-07, N=101
  Estimated time remaining to complete simulation: 13 hours, 29 minutes, 13 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 724/1000: t=723000.0 yr, dE/E0=8.13e-07, N=101
  Estimated time remaining to complete simulation: 13 hours, 26 minutes, 18 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 725/1000: t=724000.0 yr, dE/E0=8.24e-07, N=101
  Estimated time remaining to complete simulation: 13 hours, 23 minutes, 24 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 726/1000: t=725000.0 yr, dE/E0=8.35e-07, N=101
  Estimated time remaining to complete simulation: 13 hours, 20 minutes, 29 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 727/1000: t=726000.0 yr, dE/E0=8.42e-07, N=101
  Estimated time remaining to complete simulation: 13 hours, 17 minutes, 34 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 728/1000: t=727000.0 yr, dE/E0=8.46e-07, N=101
  Estimated time remaining to complete simulation: 13 hours, 14 minutes, 40 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 729/1000: t=728000.0 yr, dE/E0=8.68e-07, N=101
  Estimated time remaining to complete simulation: 13 hours, 11 minutes, 45 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 730/1000: t=729000.0 yr, dE/E0=9.07e-07, N=101
  Estimated time remaining to complete simulation: 13 hours, 8 minutes, 51 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 731/1000: t=730000.0 yr, dE/E0=9.08e-07, N=101
  Estimated time remaining to complete simulation: 13 hours, 5 minutes, 56 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 732/1000: t=731000.0 yr, dE/E0=9.11e-07, N=101
  Estimated time remaining to complete simulation: 13 hours, 3 minutes, 1 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 733/1000: t=732000.0 yr, dE/E0=9.05e-07, N=101
  Estimated time remaining to complete simulation: 13 hours, 6 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 734/1000: t=733000.0 yr, dE/E0=8.92e-07, N=101
  Estimated time remaining to complete simulation: 12 hours, 57 minutes, 12 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 735/1000: t=734000.0 yr, dE/E0=8.89e-07, N=101
  Estimated time remaining to complete simulation: 12 hours, 54 minutes, 17 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 736/1000: t=735000.0 yr, dE/E0=8.89e-07, N=101
  Estimated time remaining to complete simulation: 12 hours, 51 minutes, 23 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 737/1000: t=736000.0 yr, dE/E0=8.92e-07, N=101
  Estimated time remaining to complete simulation: 12 hours, 48 minutes, 28 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 738/1000: t=737000.0 yr, dE/E0=8.96e-07, N=101
  Estimated time remaining to complete simulation: 12 hours, 45 minutes, 34 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 739/1000: t=738000.0 yr, dE/E0=9.24e-07, N=101
  Estimated time remaining to complete simulation: 12 hours, 42 minutes, 39 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 740/1000: t=739000.0 yr, dE/E0=9.41e-07, N=101
  Estimated time remaining to complete simulation: 12 hours, 39 minutes, 45 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 741/1000: t=740000.0 yr, dE/E0=9.35e-07, N=101
  Estimated time remaining to complete simulation: 12 hours, 36 minutes, 50 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 742/1000: t=741000.0 yr, dE/E0=9.28e-07, N=101
  Estimated time remaining to complete simulation: 12 hours, 33 minutes, 56 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 743/1000: t=742000.0 yr, dE/E0=9.23e-07, N=101
  Estimated time remaining to complete simulation: 12 hours, 31 minutes, 1 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 744/1000: t=743000.0 yr, dE/E0=9.30e-07, N=101
  Estimated time remaining to complete simulation: 12 hours, 28 minutes, 6 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 745/1000: t=744000.0 yr, dE/E0=9.53e-07, N=101
  Estimated time remaining to complete simulation: 12 hours, 25 minutes, 11 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 746/1000: t=745000.0 yr, dE/E0=9.55e-07, N=101
  Estimated time remaining to complete simulation: 12 hours, 22 minutes, 17 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 747/1000: t=746000.0 yr, dE/E0=9.60e-07, N=101
  Estimated time remaining to complete simulation: 12 hours, 19 minutes, 22 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 748/1000: t=747000.0 yr, dE/E0=9.58e-07, N=101
  Estimated time remaining to complete simulation: 12 hours, 16 minutes, 28 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 749/1000: t=748000.0 yr, dE/E0=9.38e-07, N=101
  Estimated time remaining to complete simulation: 12 hours, 13 minutes, 33 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 750/1000: t=749000.0 yr, dE/E0=9.42e-07, N=101
  Estimated time remaining to complete simulation: 12 hours, 10 minutes, 38 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 751/1000: t=750000.0 yr, dE/E0=9.34e-07, N=101
  Estimated time remaining to complete simulation: 12 hours, 7 minutes, 44 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 752/1000: t=751000.0 yr, dE/E0=9.28e-07, N=101
  Estimated time remaining to complete simulation: 12 hours, 4 minutes, 49 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 753/1000: t=752000.0 yr, dE/E0=9.29e-07, N=101
  Estimated time remaining to complete simulation: 12 hours, 1 minutes, 54 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 754/1000: t=753000.0 yr, dE/E0=9.38e-07, N=101
  Estimated time remaining to complete simulation: 11 hours, 59 minutes
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 755/1000: t=754000.0 yr, dE/E0=9.24e-07, N=101
  Estimated time remaining to complete simulation: 11 hours, 56 minutes, 5 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 756/1000: t=755000.0 yr, dE/E0=9.14e-07, N=101
  Estimated time remaining to complete simulation: 11 hours, 53 minutes, 11 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 757/1000: t=756000.0 yr, dE/E0=9.06e-07, N=101
  Estimated time remaining to complete simulation: 11 hours, 50 minutes, 16 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 758/1000: t=757000.0 yr, dE/E0=9.05e-07, N=101
  Estimated time remaining to complete simulation: 11 hours, 47 minutes, 21 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 759/1000: t=758000.0 yr, dE/E0=9.38e-07, N=101
  Estimated time remaining to complete simulation: 11 hours, 44 minutes, 27 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 760/1000: t=759000.0 yr, dE/E0=9.61e-07, N=101
  Estimated time remaining to complete simulation: 11 hours, 41 minutes, 32 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 761/1000: t=760000.0 yr, dE/E0=9.56e-07, N=101
  Estimated time remaining to complete simulation: 11 hours, 38 minutes, 37 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 762/1000: t=761000.0 yr, dE/E0=9.55e-07, N=101
  Estimated time remaining to complete simulation: 11 hours, 35 minutes, 42 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 763/1000: t=762000.0 yr, dE/E0=9.60e-07, N=101
  Estimated time remaining to complete simulation: 11 hours, 32 minutes, 47 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 764/1000: t=763000.0 yr, dE/E0=9.58e-07, N=101
  Estimated time remaining to complete simulation: 11 hours, 29 minutes, 52 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 765/1000: t=764000.0 yr, dE/E0=9.65e-07, N=101
  Estimated time remaining to complete simulation: 11 hours, 26 minutes, 58 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 766/1000: t=765000.0 yr, dE/E0=9.75e-07, N=101
  Estimated time remaining to complete simulation: 11 hours, 24 minutes, 3 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 767/1000: t=766000.0 yr, dE/E0=9.78e-07, N=101
  Estimated time remaining to complete simulation: 11 hours, 21 minutes, 8 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 768/1000: t=767000.0 yr, dE/E0=1.00e-06, N=101
  Estimated time remaining to complete simulation: 11 hours, 18 minutes, 13 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 769/1000: t=768000.0 yr, dE/E0=1.00e-06, N=101
  Estimated time remaining to complete simulation: 11 hours, 15 minutes, 19 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 770/1000: t=769000.0 yr, dE/E0=1.01e-06, N=101
  Estimated time remaining to complete simulation: 11 hours, 12 minutes, 24 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 771/1000: t=770000.0 yr, dE/E0=1.02e-06, N=101
  Estimated time remaining to complete simulation: 11 hours, 9 minutes, 29 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 772/1000: t=771000.0 yr, dE/E0=1.02e-06, N=101
  Estimated time remaining to complete simulation: 11 hours, 6 minutes, 34 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 773/1000: t=772000.0 yr, dE/E0=1.04e-06, N=101
  Estimated time remaining to complete simulation: 11 hours, 3 minutes, 39 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 774/1000: t=773000.0 yr, dE/E0=1.04e-06, N=101
  Estimated time remaining to complete simulation: 11 hours, 44 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 775/1000: t=774000.0 yr, dE/E0=1.06e-06, N=101
  Estimated time remaining to complete simulation: 10 hours, 57 minutes, 49 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 776/1000: t=775000.0 yr, dE/E0=1.08e-06, N=101
  Estimated time remaining to complete simulation: 10 hours, 54 minutes, 55 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 777/1000: t=776000.0 yr, dE/E0=1.09e-06, N=101
  Estimated time remaining to complete simulation: 10 hours, 52 minutes
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 778/1000: t=777000.0 yr, dE/E0=1.09e-06, N=101
  Estimated time remaining to complete simulation: 10 hours, 49 minutes, 5 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 779/1000: t=778000.0 yr, dE/E0=1.12e-06, N=101
  Estimated time remaining to complete simulation: 10 hours, 46 minutes, 10 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 780/1000: t=779000.0 yr, dE/E0=1.12e-06, N=101
  Estimated time remaining to complete simulation: 10 hours, 43 minutes, 16 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 781/1000: t=780000.0 yr, dE/E0=1.11e-06, N=101
  Estimated time remaining to complete simulation: 10 hours, 40 minutes, 21 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 782/1000: t=781000.0 yr, dE/E0=1.10e-06, N=101
  Estimated time remaining to complete simulation: 10 hours, 37 minutes, 26 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 783/1000: t=782000.0 yr, dE/E0=1.10e-06, N=101
  Estimated time remaining to complete simulation: 10 hours, 34 minutes, 31 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 784/1000: t=783000.0 yr, dE/E0=1.10e-06, N=101
  Estimated time remaining to complete simulation: 10 hours, 31 minutes, 36 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 785/1000: t=784000.0 yr, dE/E0=1.09e-06, N=101
  Estimated time remaining to complete simulation: 10 hours, 28 minutes, 41 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 786/1000: t=785000.0 yr, dE/E0=1.10e-06, N=101
  Estimated time remaining to complete simulation: 10 hours, 25 minutes, 46 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 787/1000: t=786000.0 yr, dE/E0=1.09e-06, N=101
  Estimated time remaining to complete simulation: 10 hours, 22 minutes, 51 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 788/1000: t=787000.0 yr, dE/E0=1.10e-06, N=101
  Estimated time remaining to complete simulation: 10 hours, 19 minutes, 57 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 789/1000: t=788000.0 yr, dE/E0=1.12e-06, N=101
  Estimated time remaining to complete simulation: 10 hours, 17 minutes, 2 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 790/1000: t=789000.0 yr, dE/E0=1.13e-06, N=101
  Estimated time remaining to complete simulation: 10 hours, 14 minutes, 7 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 791/1000: t=790000.0 yr, dE/E0=1.12e-06, N=101
  Estimated time remaining to complete simulation: 10 hours, 11 minutes, 12 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 792/1000: t=791000.0 yr, dE/E0=1.13e-06, N=101
  Estimated time remaining to complete simulation: 10 hours, 8 minutes, 17 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 793/1000: t=792000.0 yr, dE/E0=1.12e-06, N=101
  Estimated time remaining to complete simulation: 10 hours, 5 minutes, 22 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 794/1000: t=793000.0 yr, dE/E0=1.11e-06, N=101
  Estimated time remaining to complete simulation: 10 hours, 2 minutes, 27 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 795/1000: t=794000.0 yr, dE/E0=1.11e-06, N=101
  Estimated time remaining to complete simulation: 9 hours, 59 minutes, 32 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 796/1000: t=795000.0 yr, dE/E0=1.10e-06, N=101
  Estimated time remaining to complete simulation: 9 hours, 56 minutes, 38 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 797/1000: t=796000.0 yr, dE/E0=1.09e-06, N=101
  Estimated time remaining to complete simulation: 9 hours, 53 minutes, 42 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 798/1000: t=797000.0 yr, dE/E0=1.10e-06, N=101
  Estimated time remaining to complete simulation: 9 hours, 50 minutes, 47 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 799/1000: t=798000.0 yr, dE/E0=1.11e-06, N=101
  Estimated time remaining to complete simulation: 9 hours, 47 minutes, 53 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 800/1000: t=799000.0 yr, dE/E0=1.11e-06, N=101
  Estimated time remaining to complete simulation: 9 hours, 44 minutes, 58 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 801/1000: t=800000.0 yr, dE/E0=1.12e-06, N=101
  Estimated time remaining to complete simulation: 9 hours, 42 minutes, 3 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 802/1000: t=801000.0 yr, dE/E0=1.14e-06, N=101
  Estimated time remaining to complete simulation: 9 hours, 39 minutes, 8 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 803/1000: t=802000.0 yr, dE/E0=1.13e-06, N=101
  Estimated time remaining to complete simulation: 9 hours, 36 minutes, 13 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 804/1000: t=803000.0 yr, dE/E0=1.15e-06, N=101
  Estimated time remaining to complete simulation: 9 hours, 33 minutes, 19 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 805/1000: t=804000.0 yr, dE/E0=1.15e-06, N=101
  Estimated time remaining to complete simulation: 9 hours, 30 minutes, 24 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 806/1000: t=805000.0 yr, dE/E0=1.17e-06, N=101
  Estimated time remaining to complete simulation: 9 hours, 27 minutes, 29 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 807/1000: t=806000.0 yr, dE/E0=1.17e-06, N=101
  Estimated time remaining to complete simulation: 9 hours, 24 minutes, 34 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 808/1000: t=807000.0 yr, dE/E0=1.19e-06, N=101
  Estimated time remaining to complete simulation: 9 hours, 21 minutes, 39 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 809/1000: t=808000.0 yr, dE/E0=1.21e-06, N=101
  Estimated time remaining to complete simulation: 9 hours, 18 minutes, 45 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 810/1000: t=809000.0 yr, dE/E0=1.22e-06, N=101
  Estimated time remaining to complete simulation: 9 hours, 15 minutes, 50 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 811/1000: t=810000.0 yr, dE/E0=1.22e-06, N=101
  Estimated time remaining to complete simulation: 9 hours, 12 minutes, 55 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 812/1000: t=811000.0 yr, dE/E0=1.22e-06, N=101
  Estimated time remaining to complete simulation: 9 hours, 10 minutes
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 813/1000: t=812000.0 yr, dE/E0=1.23e-06, N=101
  Estimated time remaining to complete simulation: 9 hours, 7 minutes, 6 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 814/1000: t=813000.0 yr, dE/E0=1.23e-06, N=101
  Estimated time remaining to complete simulation: 9 hours, 4 minutes, 11 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 815/1000: t=814000.0 yr, dE/E0=1.24e-06, N=101
  Estimated time remaining to complete simulation: 9 hours, 1 minutes, 16 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 816/1000: t=815000.0 yr, dE/E0=1.24e-06, N=101
  Estimated time remaining to complete simulation: 8 hours, 58 minutes, 21 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 817/1000: t=816000.0 yr, dE/E0=1.25e-06, N=101
  Estimated time remaining to complete simulation: 8 hours, 55 minutes, 27 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 818/1000: t=817000.0 yr, dE/E0=1.26e-06, N=101
  Estimated time remaining to complete simulation: 8 hours, 52 minutes, 32 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 819/1000: t=818000.0 yr, dE/E0=1.27e-06, N=101
  Estimated time remaining to complete simulation: 8 hours, 49 minutes, 38 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 820/1000: t=819000.0 yr, dE/E0=1.29e-06, N=101
  Estimated time remaining to complete simulation: 8 hours, 46 minutes, 43 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 821/1000: t=820000.0 yr, dE/E0=1.28e-06, N=101
  Estimated time remaining to complete simulation: 8 hours, 43 minutes, 48 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 822/1000: t=821000.0 yr, dE/E0=1.28e-06, N=101
  Estimated time remaining to complete simulation: 8 hours, 40 minutes, 54 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 823/1000: t=822000.0 yr, dE/E0=1.24e-06, N=101
  Estimated time remaining to complete simulation: 8 hours, 37 minutes, 59 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 824/1000: t=823000.0 yr, dE/E0=1.27e-06, N=101
  Estimated time remaining to complete simulation: 8 hours, 35 minutes, 5 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 825/1000: t=824000.0 yr, dE/E0=1.28e-06, N=101
  Estimated time remaining to complete simulation: 8 hours, 32 minutes, 10 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 826/1000: t=825000.0 yr, dE/E0=1.28e-06, N=101
  Estimated time remaining to complete simulation: 8 hours, 29 minutes, 15 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 827/1000: t=826000.0 yr, dE/E0=1.28e-06, N=101
  Estimated time remaining to complete simulation: 8 hours, 26 minutes, 20 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 828/1000: t=827000.0 yr, dE/E0=1.27e-06, N=101
  Estimated time remaining to complete simulation: 8 hours, 23 minutes, 26 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 829/1000: t=828000.0 yr, dE/E0=1.28e-06, N=101
  Estimated time remaining to complete simulation: 8 hours, 20 minutes, 31 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 830/1000: t=829000.0 yr, dE/E0=1.30e-06, N=101
  Estimated time remaining to complete simulation: 8 hours, 17 minutes, 36 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 831/1000: t=830000.0 yr, dE/E0=1.31e-06, N=101
  Estimated time remaining to complete simulation: 8 hours, 14 minutes, 41 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 832/1000: t=831000.0 yr, dE/E0=1.31e-06, N=101
  Estimated time remaining to complete simulation: 8 hours, 11 minutes, 47 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 833/1000: t=832000.0 yr, dE/E0=1.33e-06, N=101
  Estimated time remaining to complete simulation: 8 hours, 8 minutes, 52 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 834/1000: t=833000.0 yr, dE/E0=1.35e-06, N=101
  Estimated time remaining to complete simulation: 8 hours, 5 minutes, 57 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 835/1000: t=834000.0 yr, dE/E0=1.33e-06, N=101
  Estimated time remaining to complete simulation: 8 hours, 3 minutes, 2 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 836/1000: t=835000.0 yr, dE/E0=1.35e-06, N=101
  Estimated time remaining to complete simulation: 8 hours, 7 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 837/1000: t=836000.0 yr, dE/E0=1.34e-06, N=101
  Estimated time remaining to complete simulation: 7 hours, 57 minutes, 12 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 838/1000: t=837000.0 yr, dE/E0=1.34e-06, N=101
  Estimated time remaining to complete simulation: 7 hours, 54 minutes, 18 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 839/1000: t=838000.0 yr, dE/E0=1.35e-06, N=101
  Estimated time remaining to complete simulation: 7 hours, 51 minutes, 23 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 840/1000: t=839000.0 yr, dE/E0=1.37e-06, N=101
  Estimated time remaining to complete simulation: 7 hours, 48 minutes, 27 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 841/1000: t=840000.0 yr, dE/E0=1.39e-06, N=101
  Estimated time remaining to complete simulation: 7 hours, 45 minutes, 32 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 842/1000: t=841000.0 yr, dE/E0=1.39e-06, N=101
  Estimated time remaining to complete simulation: 7 hours, 42 minutes, 37 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 843/1000: t=842000.0 yr, dE/E0=1.39e-06, N=101
  Estimated time remaining to complete simulation: 7 hours, 39 minutes, 42 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 844/1000: t=843000.0 yr, dE/E0=1.38e-06, N=101
  Estimated time remaining to complete simulation: 7 hours, 36 minutes, 47 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 845/1000: t=844000.0 yr, dE/E0=1.41e-06, N=101
  Estimated time remaining to complete simulation: 7 hours, 33 minutes, 52 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 846/1000: t=845000.0 yr, dE/E0=1.40e-06, N=101
  Estimated time remaining to complete simulation: 7 hours, 30 minutes, 56 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 847/1000: t=846000.0 yr, dE/E0=1.39e-06, N=101
  Estimated time remaining to complete simulation: 7 hours, 28 minutes, 1 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 848/1000: t=847000.0 yr, dE/E0=1.40e-06, N=101
  Estimated time remaining to complete simulation: 7 hours, 25 minutes, 6 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 849/1000: t=848000.0 yr, dE/E0=1.40e-06, N=101
  Estimated time remaining to complete simulation: 7 hours, 22 minutes, 11 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 850/1000: t=849000.0 yr, dE/E0=1.39e-06, N=101
  Estimated time remaining to complete simulation: 7 hours, 19 minutes, 16 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 851/1000: t=850000.0 yr, dE/E0=1.41e-06, N=101
  Estimated time remaining to complete simulation: 7 hours, 16 minutes, 21 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 852/1000: t=851000.0 yr, dE/E0=1.41e-06, N=101
  Estimated time remaining to complete simulation: 7 hours, 13 minutes, 26 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 853/1000: t=852000.0 yr, dE/E0=1.43e-06, N=101
  Estimated time remaining to complete simulation: 7 hours, 10 minutes, 31 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 854/1000: t=853000.0 yr, dE/E0=1.47e-06, N=101
  Estimated time remaining to complete simulation: 7 hours, 7 minutes, 35 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 855/1000: t=854000.0 yr, dE/E0=1.48e-06, N=101
  Estimated time remaining to complete simulation: 7 hours, 4 minutes, 40 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 856/1000: t=855000.0 yr, dE/E0=1.51e-06, N=101
  Estimated time remaining to complete simulation: 7 hours, 1 minutes, 45 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 857/1000: t=856000.0 yr, dE/E0=1.49e-06, N=101
  Estimated time remaining to complete simulation: 6 hours, 58 minutes, 50 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 858/1000: t=857000.0 yr, dE/E0=1.49e-06, N=101
  Estimated time remaining to complete simulation: 6 hours, 55 minutes, 55 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 859/1000: t=858000.0 yr, dE/E0=1.48e-06, N=101
  Estimated time remaining to complete simulation: 6 hours, 53 minutes
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 860/1000: t=859000.0 yr, dE/E0=1.50e-06, N=101
  Estimated time remaining to complete simulation: 6 hours, 50 minutes, 5 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 861/1000: t=860000.0 yr, dE/E0=1.51e-06, N=101
  Estimated time remaining to complete simulation: 6 hours, 47 minutes, 10 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 862/1000: t=861000.0 yr, dE/E0=1.51e-06, N=101
  Estimated time remaining to complete simulation: 6 hours, 44 minutes, 15 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 863/1000: t=862000.0 yr, dE/E0=1.53e-06, N=101
  Estimated time remaining to complete simulation: 6 hours, 41 minutes, 20 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 864/1000: t=863000.0 yr, dE/E0=1.54e-06, N=101
  Estimated time remaining to complete simulation: 6 hours, 38 minutes, 25 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 865/1000: t=864000.0 yr, dE/E0=1.52e-06, N=101
  Estimated time remaining to complete simulation: 6 hours, 35 minutes, 30 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 866/1000: t=865000.0 yr, dE/E0=1.51e-06, N=101
  Estimated time remaining to complete simulation: 6 hours, 32 minutes, 35 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 867/1000: t=866000.0 yr, dE/E0=1.50e-06, N=101
  Estimated time remaining to complete simulation: 6 hours, 29 minutes, 39 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 868/1000: t=867000.0 yr, dE/E0=1.52e-06, N=101
  Estimated time remaining to complete simulation: 6 hours, 26 minutes, 44 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 869/1000: t=868000.0 yr, dE/E0=1.52e-06, N=101
  Estimated time remaining to complete simulation: 6 hours, 23 minutes, 49 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 870/1000: t=869000.0 yr, dE/E0=1.56e-06, N=101
  Estimated time remaining to complete simulation: 6 hours, 20 minutes, 54 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 871/1000: t=870000.0 yr, dE/E0=1.56e-06, N=101
  Estimated time remaining to complete simulation: 6 hours, 17 minutes, 59 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 872/1000: t=871000.0 yr, dE/E0=1.54e-06, N=101
  Estimated time remaining to complete simulation: 6 hours, 15 minutes, 3 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 873/1000: t=872000.0 yr, dE/E0=1.56e-06, N=101
  Estimated time remaining to complete simulation: 6 hours, 12 minutes, 8 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 874/1000: t=873000.0 yr, dE/E0=1.58e-06, N=101
  Estimated time remaining to complete simulation: 6 hours, 9 minutes, 13 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 875/1000: t=874000.0 yr, dE/E0=1.59e-06, N=101
  Estimated time remaining to complete simulation: 6 hours, 6 minutes, 18 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 876/1000: t=875000.0 yr, dE/E0=1.58e-06, N=101
  Estimated time remaining to complete simulation: 6 hours, 3 minutes, 23 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 877/1000: t=876000.0 yr, dE/E0=1.58e-06, N=101
  Estimated time remaining to complete simulation: 6 hours, 27 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 878/1000: t=877000.0 yr, dE/E0=1.58e-06, N=101
  Estimated time remaining to complete simulation: 5 hours, 57 minutes, 32 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 879/1000: t=878000.0 yr, dE/E0=1.56e-06, N=101
  Estimated time remaining to complete simulation: 5 hours, 54 minutes, 37 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 880/1000: t=879000.0 yr, dE/E0=1.58e-06, N=101
  Estimated time remaining to complete simulation: 5 hours, 51 minutes, 42 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 881/1000: t=880000.0 yr, dE/E0=1.60e-06, N=101
  Estimated time remaining to complete simulation: 5 hours, 48 minutes, 47 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 882/1000: t=881000.0 yr, dE/E0=1.59e-06, N=101
  Estimated time remaining to complete simulation: 5 hours, 45 minutes, 51 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 883/1000: t=882000.0 yr, dE/E0=1.60e-06, N=101
  Estimated time remaining to complete simulation: 5 hours, 42 minutes, 56 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 884/1000: t=883000.0 yr, dE/E0=1.59e-06, N=101
  Estimated time remaining to complete simulation: 5 hours, 40 minutes, 1 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 885/1000: t=884000.0 yr, dE/E0=1.62e-06, N=101
  Estimated time remaining to complete simulation: 5 hours, 37 minutes, 6 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 886/1000: t=885000.0 yr, dE/E0=1.62e-06, N=101
  Estimated time remaining to complete simulation: 5 hours, 34 minutes, 10 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 887/1000: t=886000.0 yr, dE/E0=1.62e-06, N=101
  Estimated time remaining to complete simulation: 5 hours, 31 minutes, 15 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 888/1000: t=887000.0 yr, dE/E0=1.62e-06, N=101
  Estimated time remaining to complete simulation: 5 hours, 28 minutes, 20 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 889/1000: t=888000.0 yr, dE/E0=1.61e-06, N=101
  Estimated time remaining to complete simulation: 5 hours, 25 minutes, 25 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 890/1000: t=889000.0 yr, dE/E0=1.62e-06, N=101
  Estimated time remaining to complete simulation: 5 hours, 22 minutes, 30 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 891/1000: t=890000.0 yr, dE/E0=1.62e-06, N=101
  Estimated time remaining to complete simulation: 5 hours, 19 minutes, 34 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 892/1000: t=891000.0 yr, dE/E0=1.62e-06, N=101
  Estimated time remaining to complete simulation: 5 hours, 16 minutes, 39 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 893/1000: t=892000.0 yr, dE/E0=1.61e-06, N=101
  Estimated time remaining to complete simulation: 5 hours, 13 minutes, 44 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 894/1000: t=893000.0 yr, dE/E0=1.61e-06, N=101
  Estimated time remaining to complete simulation: 5 hours, 10 minutes, 49 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 895/1000: t=894000.0 yr, dE/E0=1.60e-06, N=101
  Estimated time remaining to complete simulation: 5 hours, 7 minutes, 53 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 896/1000: t=895000.0 yr, dE/E0=1.60e-06, N=101
  Estimated time remaining to complete simulation: 5 hours, 4 minutes, 58 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 897/1000: t=896000.0 yr, dE/E0=1.61e-06, N=101
  Estimated time remaining to complete simulation: 5 hours, 2 minutes, 3 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 898/1000: t=897000.0 yr, dE/E0=1.62e-06, N=101
  Estimated time remaining to complete simulation: 4 hours, 59 minutes, 7 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 899/1000: t=898000.0 yr, dE/E0=1.61e-06, N=101
  Estimated time remaining to complete simulation: 4 hours, 56 minutes, 12 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 900/1000: t=899000.0 yr, dE/E0=1.63e-06, N=101
  Estimated time remaining to complete simulation: 4 hours, 53 minutes, 17 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 901/1000: t=900000.0 yr, dE/E0=1.64e-06, N=101
  Estimated time remaining to complete simulation: 4 hours, 50 minutes, 21 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 902/1000: t=901000.0 yr, dE/E0=1.65e-06, N=101
  Estimated time remaining to complete simulation: 4 hours, 47 minutes, 26 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 903/1000: t=902000.0 yr, dE/E0=1.65e-06, N=101
  Estimated time remaining to complete simulation: 4 hours, 44 minutes, 31 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 904/1000: t=903000.0 yr, dE/E0=1.65e-06, N=101
  Estimated time remaining to complete simulation: 4 hours, 41 minutes, 35 seconds
  Estimated time remaining to next output: 2 minutes, 55 seconds
Output 905/1000: t=904000.0 yr, dE/E0=1.65e-06, N=101
  Estimated time remaining to complete simulation: 4 hours, 38 minutes, 40 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 906/1000: t=905000.0 yr, dE/E0=1.67e-06, N=101
  Estimated time remaining to complete simulation: 4 hours, 35 minutes, 44 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 907/1000: t=906000.0 yr, dE/E0=1.66e-06, N=101
  Estimated time remaining to complete simulation: 4 hours, 32 minutes, 49 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 908/1000: t=907000.0 yr, dE/E0=1.67e-06, N=101
  Estimated time remaining to complete simulation: 4 hours, 29 minutes, 54 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 909/1000: t=908000.0 yr, dE/E0=1.68e-06, N=101
  Estimated time remaining to complete simulation: 4 hours, 26 minutes, 58 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 910/1000: t=909000.0 yr, dE/E0=1.70e-06, N=101
  Estimated time remaining to complete simulation: 4 hours, 24 minutes, 3 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 911/1000: t=910000.0 yr, dE/E0=1.70e-06, N=101
  Estimated time remaining to complete simulation: 4 hours, 21 minutes, 7 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 912/1000: t=911000.0 yr, dE/E0=1.72e-06, N=101
  Estimated time remaining to complete simulation: 4 hours, 18 minutes, 12 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 913/1000: t=912000.0 yr, dE/E0=1.72e-06, N=101
  Estimated time remaining to complete simulation: 4 hours, 15 minutes, 16 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 914/1000: t=913000.0 yr, dE/E0=1.73e-06, N=101
  Estimated time remaining to complete simulation: 4 hours, 12 minutes, 21 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 915/1000: t=914000.0 yr, dE/E0=1.72e-06, N=101
  Estimated time remaining to complete simulation: 4 hours, 9 minutes, 25 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 916/1000: t=915000.0 yr, dE/E0=1.71e-06, N=101
  Estimated time remaining to complete simulation: 4 hours, 6 minutes, 30 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 917/1000: t=916000.0 yr, dE/E0=1.71e-06, N=101
  Estimated time remaining to complete simulation: 4 hours, 3 minutes, 34 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 918/1000: t=917000.0 yr, dE/E0=1.71e-06, N=101
  Estimated time remaining to complete simulation: 4 hours, 38 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 919/1000: t=918000.0 yr, dE/E0=1.70e-06, N=101
  Estimated time remaining to complete simulation: 3 hours, 57 minutes, 43 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 920/1000: t=919000.0 yr, dE/E0=1.71e-06, N=101
  Estimated time remaining to complete simulation: 3 hours, 54 minutes, 47 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 921/1000: t=920000.0 yr, dE/E0=1.70e-06, N=101
  Estimated time remaining to complete simulation: 3 hours, 51 minutes, 51 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 922/1000: t=921000.0 yr, dE/E0=1.70e-06, N=101
  Estimated time remaining to complete simulation: 3 hours, 48 minutes, 56 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 923/1000: t=922000.0 yr, dE/E0=1.71e-06, N=101
  Estimated time remaining to complete simulation: 3 hours, 46 minutes
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 924/1000: t=923000.0 yr, dE/E0=1.72e-06, N=101
  Estimated time remaining to complete simulation: 3 hours, 43 minutes, 4 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 925/1000: t=924000.0 yr, dE/E0=1.73e-06, N=101
  Estimated time remaining to complete simulation: 3 hours, 40 minutes, 9 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 926/1000: t=925000.0 yr, dE/E0=1.76e-06, N=101
  Estimated time remaining to complete simulation: 3 hours, 37 minutes, 13 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 927/1000: t=926000.0 yr, dE/E0=1.77e-06, N=101
  Estimated time remaining to complete simulation: 3 hours, 34 minutes, 17 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 928/1000: t=927000.0 yr, dE/E0=1.76e-06, N=101
  Estimated time remaining to complete simulation: 3 hours, 31 minutes, 21 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 929/1000: t=928000.0 yr, dE/E0=1.78e-06, N=101
  Estimated time remaining to complete simulation: 3 hours, 28 minutes, 26 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 930/1000: t=929000.0 yr, dE/E0=1.78e-06, N=101
  Estimated time remaining to complete simulation: 3 hours, 25 minutes, 30 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 931/1000: t=930000.0 yr, dE/E0=1.79e-06, N=101
  Estimated time remaining to complete simulation: 3 hours, 22 minutes, 34 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 932/1000: t=931000.0 yr, dE/E0=1.78e-06, N=101
  Estimated time remaining to complete simulation: 3 hours, 19 minutes, 38 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 933/1000: t=932000.0 yr, dE/E0=1.79e-06, N=101
  Estimated time remaining to complete simulation: 3 hours, 16 minutes, 43 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 934/1000: t=933000.0 yr, dE/E0=1.80e-06, N=101
  Estimated time remaining to complete simulation: 3 hours, 13 minutes, 47 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 935/1000: t=934000.0 yr, dE/E0=1.81e-06, N=101
  Estimated time remaining to complete simulation: 3 hours, 10 minutes, 51 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 936/1000: t=935000.0 yr, dE/E0=1.84e-06, N=101
  Estimated time remaining to complete simulation: 3 hours, 7 minutes, 55 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 937/1000: t=936000.0 yr, dE/E0=1.84e-06, N=101
  Estimated time remaining to complete simulation: 3 hours, 4 minutes, 59 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 938/1000: t=937000.0 yr, dE/E0=1.86e-06, N=101
  Estimated time remaining to complete simulation: 3 hours, 2 minutes, 3 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 939/1000: t=938000.0 yr, dE/E0=1.87e-06, N=101
  Estimated time remaining to complete simulation: 2 hours, 59 minutes, 8 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 940/1000: t=939000.0 yr, dE/E0=1.90e-06, N=101
  Estimated time remaining to complete simulation: 2 hours, 56 minutes, 12 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 941/1000: t=940000.0 yr, dE/E0=1.89e-06, N=101
  Estimated time remaining to complete simulation: 2 hours, 53 minutes, 16 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 942/1000: t=941000.0 yr, dE/E0=1.92e-06, N=101
  Estimated time remaining to complete simulation: 2 hours, 50 minutes, 20 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 943/1000: t=942000.0 yr, dE/E0=1.91e-06, N=101
  Estimated time remaining to complete simulation: 2 hours, 47 minutes, 24 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 944/1000: t=943000.0 yr, dE/E0=1.91e-06, N=101
  Estimated time remaining to complete simulation: 2 hours, 44 minutes, 28 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 945/1000: t=944000.0 yr, dE/E0=1.91e-06, N=101
  Estimated time remaining to complete simulation: 2 hours, 41 minutes, 32 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 946/1000: t=945000.0 yr, dE/E0=1.95e-06, N=101
  Estimated time remaining to complete simulation: 2 hours, 38 minutes, 36 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 947/1000: t=946000.0 yr, dE/E0=1.98e-06, N=101
  Estimated time remaining to complete simulation: 2 hours, 35 minutes, 40 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 948/1000: t=947000.0 yr, dE/E0=1.99e-06, N=101
  Estimated time remaining to complete simulation: 2 hours, 32 minutes, 44 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 949/1000: t=948000.0 yr, dE/E0=1.97e-06, N=101
  Estimated time remaining to complete simulation: 2 hours, 29 minutes, 48 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 950/1000: t=949000.0 yr, dE/E0=1.98e-06, N=101
  Estimated time remaining to complete simulation: 2 hours, 26 minutes, 52 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 951/1000: t=950000.0 yr, dE/E0=1.98e-06, N=101
  Estimated time remaining to complete simulation: 2 hours, 23 minutes, 55 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 952/1000: t=951000.0 yr, dE/E0=1.99e-06, N=101
  Estimated time remaining to complete simulation: 2 hours, 20 minutes, 59 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 953/1000: t=952000.0 yr, dE/E0=2.01e-06, N=101
  Estimated time remaining to complete simulation: 2 hours, 18 minutes, 3 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 954/1000: t=953000.0 yr, dE/E0=2.02e-06, N=101
  Estimated time remaining to complete simulation: 2 hours, 15 minutes, 7 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 955/1000: t=954000.0 yr, dE/E0=2.01e-06, N=101
  Estimated time remaining to complete simulation: 2 hours, 12 minutes, 11 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 956/1000: t=955000.0 yr, dE/E0=2.02e-06, N=101
  Estimated time remaining to complete simulation: 2 hours, 9 minutes, 15 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 957/1000: t=956000.0 yr, dE/E0=2.02e-06, N=101
  Estimated time remaining to complete simulation: 2 hours, 6 minutes, 19 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 958/1000: t=957000.0 yr, dE/E0=2.02e-06, N=101
  Estimated time remaining to complete simulation: 2 hours, 3 minutes, 23 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 959/1000: t=958000.0 yr, dE/E0=2.04e-06, N=101
  Estimated time remaining to complete simulation: 2 hours, 27 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 960/1000: t=959000.0 yr, dE/E0=2.03e-06, N=101
  Estimated time remaining to complete simulation: 1 hours, 57 minutes, 31 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 961/1000: t=960000.0 yr, dE/E0=2.03e-06, N=101
  Estimated time remaining to complete simulation: 1 hours, 54 minutes, 34 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 962/1000: t=961000.0 yr, dE/E0=2.03e-06, N=101
  Estimated time remaining to complete simulation: 1 hours, 51 minutes, 38 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 963/1000: t=962000.0 yr, dE/E0=2.06e-06, N=101
  Estimated time remaining to complete simulation: 1 hours, 48 minutes, 42 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 964/1000: t=963000.0 yr, dE/E0=2.06e-06, N=101
  Estimated time remaining to complete simulation: 1 hours, 45 minutes, 46 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 965/1000: t=964000.0 yr, dE/E0=2.07e-06, N=101
  Estimated time remaining to complete simulation: 1 hours, 42 minutes, 50 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 966/1000: t=965000.0 yr, dE/E0=2.10e-06, N=101
  Estimated time remaining to complete simulation: 1 hours, 39 minutes, 53 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 967/1000: t=966000.0 yr, dE/E0=2.09e-06, N=101
  Estimated time remaining to complete simulation: 1 hours, 36 minutes, 57 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 968/1000: t=967000.0 yr, dE/E0=2.10e-06, N=101
  Estimated time remaining to complete simulation: 1 hours, 34 minutes, 1 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 969/1000: t=968000.0 yr, dE/E0=2.11e-06, N=101
  Estimated time remaining to complete simulation: 1 hours, 31 minutes, 5 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 970/1000: t=969000.0 yr, dE/E0=2.12e-06, N=101
  Estimated time remaining to complete simulation: 1 hours, 28 minutes, 9 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 971/1000: t=970000.0 yr, dE/E0=2.13e-06, N=101
  Estimated time remaining to complete simulation: 1 hours, 25 minutes, 12 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 972/1000: t=971000.0 yr, dE/E0=2.14e-06, N=101
  Estimated time remaining to complete simulation: 1 hours, 22 minutes, 16 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 973/1000: t=972000.0 yr, dE/E0=2.13e-06, N=101
  Estimated time remaining to complete simulation: 1 hours, 19 minutes, 20 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 974/1000: t=973000.0 yr, dE/E0=2.13e-06, N=101
  Estimated time remaining to complete simulation: 1 hours, 16 minutes, 24 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 975/1000: t=974000.0 yr, dE/E0=2.14e-06, N=101
  Estimated time remaining to complete simulation: 1 hours, 13 minutes, 28 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 976/1000: t=975000.0 yr, dE/E0=2.16e-06, N=101
  Estimated time remaining to complete simulation: 1 hours, 10 minutes, 31 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 977/1000: t=976000.0 yr, dE/E0=2.14e-06, N=101
  Estimated time remaining to complete simulation: 1 hours, 7 minutes, 35 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 978/1000: t=977000.0 yr, dE/E0=2.16e-06, N=101
  Estimated time remaining to complete simulation: 1 hours, 4 minutes, 39 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 979/1000: t=978000.0 yr, dE/E0=2.14e-06, N=101
  Estimated time remaining to complete simulation: 1 hours, 1 minutes, 43 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 980/1000: t=979000.0 yr, dE/E0=2.16e-06, N=101
  Estimated time remaining to complete simulation: 58 minutes, 46 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 981/1000: t=980000.0 yr, dE/E0=2.17e-06, N=101
  Estimated time remaining to complete simulation: 55 minutes, 50 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 982/1000: t=981000.0 yr, dE/E0=2.18e-06, N=101
  Estimated time remaining to complete simulation: 52 minutes, 54 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 983/1000: t=982000.0 yr, dE/E0=2.17e-06, N=101
  Estimated time remaining to complete simulation: 49 minutes, 57 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 984/1000: t=983000.0 yr, dE/E0=2.19e-06, N=101
  Estimated time remaining to complete simulation: 47 minutes, 1 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 985/1000: t=984000.0 yr, dE/E0=2.21e-06, N=101
  Estimated time remaining to complete simulation: 44 minutes, 5 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 986/1000: t=985000.0 yr, dE/E0=2.21e-06, N=101
  Estimated time remaining to complete simulation: 41 minutes, 9 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 987/1000: t=986000.0 yr, dE/E0=2.19e-06, N=101
  Estimated time remaining to complete simulation: 38 minutes, 12 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 988/1000: t=987000.0 yr, dE/E0=2.21e-06, N=101
  Estimated time remaining to complete simulation: 35 minutes, 16 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 989/1000: t=988000.0 yr, dE/E0=2.18e-06, N=101
  Estimated time remaining to complete simulation: 32 minutes, 20 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 990/1000: t=989000.0 yr, dE/E0=2.18e-06, N=101
  Estimated time remaining to complete simulation: 29 minutes, 23 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 991/1000: t=990000.0 yr, dE/E0=2.22e-06, N=101
  Estimated time remaining to complete simulation: 26 minutes, 27 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 992/1000: t=991000.0 yr, dE/E0=2.23e-06, N=101
  Estimated time remaining to complete simulation: 23 minutes, 31 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 993/1000: t=992000.0 yr, dE/E0=2.23e-06, N=101
  Estimated time remaining to complete simulation: 20 minutes, 34 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 994/1000: t=993000.0 yr, dE/E0=2.24e-06, N=101
  Estimated time remaining to complete simulation: 17 minutes, 38 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 995/1000: t=994000.0 yr, dE/E0=2.26e-06, N=101
  Estimated time remaining to complete simulation: 14 minutes, 41 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 996/1000: t=995000.0 yr, dE/E0=2.27e-06, N=101
  Estimated time remaining to complete simulation: 11 minutes, 45 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 997/1000: t=996000.0 yr, dE/E0=2.26e-06, N=101
  Estimated time remaining to complete simulation: 8 minutes, 49 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 998/1000: t=997000.0 yr, dE/E0=2.27e-06, N=101
  Estimated time remaining to complete simulation: 5 minutes, 52 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 999/1000: t=998000.0 yr, dE/E0=2.27e-06, N=101
  Estimated time remaining to complete simulation: 2 minutes, 56 seconds
  Estimated time remaining to next output: 2 minutes, 56 seconds
Output 1000/1000: t=999000.0 yr, dE/E0=2.28e-06, N=101
  Estimated time remaining to complete simulation: 0 seconds
Output 1001/1000: t=1000000.0 yr, dE/E0=2.29e-06, N=101
  Estimated time remaining to complete simulation: -1 months, 4 weeks, 1 days, 23 hours, 57 minutes, 4 seconds

Simulation complete.
Total runtime: 2 days, 1 hours, 3 minutes, 6 seconds
Saved archive: outputs/Consensed_sim_1Myr_1au_1earthmass/Consensed_sim_1Myr_1au_1earthmass.bin
Number of snapshots saved: 1001
Archive time range: 0.000e+00 yr to 1.000e+06 yr
Loaded snapshot table from archive.
role
massive_planetesimal    100
star                      1
Name: count, dtype: int64
Saved: outputs/Consensed_sim_1Myr_1au_1earthmass/figures/survival_fraction_vs_time.png
Saved: outputs/Consensed_sim_1Myr_1au_1earthmass/figures/mean_semimajor_axis_vs_time.png
Saved: outputs/Consensed_sim_1Myr_1au_1earthmass/figures/mean_eccentricity_vs_time.png
Saved: outputs/Consensed_sim_1Myr_1au_1earthmass/figures/rms_eccentricity_vs_time.png
Saved: outputs/Consensed_sim_1Myr_1au_1earthmass/figures/rms_inclination_vs_time.png
Saved: outputs/Consensed_sim_1Myr_1au_1earthmass/figures/a_vs_e_initial_final.png
Saved: outputs/Consensed_sim_1Myr_1au_1earthmass/figures/a_vs_i_initial_final.png
Inner plotted edge = 0.95 AU
Outer plotted edge = 1.05 AU
Saved: outputs/Consensed_sim_1Myr_1au_1earthmass/figures/xy_initial_final.png
All summary figures saved.
```

## Retroactive Krivov & Booth (2018) self-stirring diagnostics

_Added retroactively by `calibration/retroactive_kirvov_checks.py`; this run predates the in-pipeline checks in `src/simulation/run_simulation.py`. The same functions a live run now uses are applied to the archive: the coverage condition to the first snapshot (initial conditions), C_e to the last snapshot. Config used: `outputs/Consensed_sim_1Myr_1au_1earthmass/config.yaml`._

### Effective stirring constant C_e (Eqs. 9-10, final snapshot)

- Final time: t = 1.000000e+06 yr
- RMS eccentricity of the 100 massive planetesimals: 4.431278e-02
- Belt geometry: a = 1 au, da = 0.1 au, a/da = 10
- Masses: M_indiv = 8.409771e-09 Msun, M_disc = 8.409771e-07 Msun
- Mean motion at belt centre: Omega = 6.283067e+00 yr^-1
- Implied stirring timescale: T = 5.186976e+11 yr
- **Effective stirring constant: C_e = 27.2600** (Ida & Makino 1993 / Krivov & Booth 2018 reference value: 40)

### Stirrer-coverage condition  N x delta_af >= delta_a (initial snapshot)

- Stirrers inside the belt [0.95, 1.05] au: N = 100
- delta_af = 8 sqrt(3) h_M a_M: mean = 1.949984e-02 au, sum over stirrers = 1.949984e+00 au
- Belt width: delta_a = 1.000000e-01 au
- Coverage ratio (sum delta_af / delta_a) = 19.500
- **Condition satisfied**: the stirrer feeding zones span the belt.
