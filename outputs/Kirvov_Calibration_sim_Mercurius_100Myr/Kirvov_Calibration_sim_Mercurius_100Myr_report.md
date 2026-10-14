# Kirvov_Calibration_sim_Mercurius_100Myr — Simulation Report

Config file: `config/Kirvov_Calibration_sim_Mercurius_100Myr.yaml`
Archive file: `outputs/Kirvov_Calibration_sim_Mercurius_100Myr/Kirvov_Calibration_sim_Mercurius_100Myr.bin`

## Provenance

- Run UUID: `7fd0f7ec-9e6a-45c2-be76-01fe64160542`
- Created: 2026-10-05T21:30:54+00:00
- Finished: 2026-10-07T18:35:01+00:00
- Wall runtime: 10661.3 s
- Outcome: completed
- Command: `src/simulation/run_simulation.py config/Kirvov_Calibration_sim_Mercurius_100Myr.yaml`
- Git: not available (run from a non-repo checkout)
- Software: python 3.12.14, rebound 5.0.0, numpy 2.4.6, pandas 3.0.3, matplotlib 3.10.9, pyyaml 6.0.3
- Frozen config: `config.yaml` (this directory)
- Full environment: `environment.txt` (this directory)

## Simulation
- Name: Kirvov_Calibration_sim_Mercurius_100Myr
- Output directory: outputs
- Dump/checkpoint enabled: True

## Units
- time = yr, length = AU, mass = Msun

## Integration
- Integrator: IAS15
- maxtime: 100000000
- time_step: 1000000
- timestep_fraction_of_planet_period: 0.1
- exit_max_distance: 1000.0 au

## Star
- Mass: 1.0 Msun

## Giant Planet
- Mass: 0.00011 Mjup
- a: 100 au, e: 3.2e-05, inc: 3.2e-05 deg
- omega: 100.0 deg, Omega random: True
- t_peri_jd: 2450870.0, orbital_period_days: 1311.0, epoch_jd: 2451545.0

## Disk
- a: [95, 105] au
- e: [0.0, 3.2e-05]
- inc: [0.0, 3.2e-05] deg

## Massive Planetesimals
- N: 100
- Mass-assignment method (config): total_disk_mass_earth = 5.800000e-06 Earth masses (total disk mass, split evenly across N)
- Individual mass (uniform across all 100): 1.742024e-13 Msun (0.000000 Earth masses)

## Test Particles
- N: 0
- Distribution: uniform

## Run Summary (from archive)
- Initial particle count: 102
- Final particle count: 102
- Particles lost (escaped / unbound / other removal): 0
- Archive time range: 0.000000e+00 to 1.000000e+08
- Number of snapshots: 101

## Terminal Output

```
Saving SimulationArchive to: outputs/Kirvov_Calibration_sim_Mercurius_100Myr/Kirvov_Calibration_sim_Mercurius_100Myr.bin
No existing dump_data.json found; starting fresh run.
  Timestep: 1.000019e+02 (0.1 x giant planet orbital period = 1.000019e+03)

Disk semimajor axes: uniform in [95, 105] AU

Massive planetesimal mass setup:
  Mode: total_disk_mass_earth  (total disk mass given; divided evenly among N)
  Number of planetesimals: 100
  Individual MP mass: 2.659031e-05 Pluto masses / 5.800000e-08 Earth masses / 1.742024e-13 Msun
  Individual MP diameter: 87.141 km (3.666639e-02 Pluto diameters) (uniform sphere, rho = 1 g/cm**3)
  Total disk mass: 5.800000e-06 Earth masses (1.742024e-11 Msun)

Stirrer-coverage check (Krivov & Booth 2018: N x delta_af >= delta_a):
  Stirrers inside the belt [95, 105]: N = 101  (incl. giant planet)
  delta_af = 8 sqrt(3) h_M a_M:  mean = 9.790355e-02, sum over stirrers = 9.888259e+00
  Belt width delta_a = 1.000000e+01
  Coverage ratio (sum delta_af / delta_a) = 0.989
  WARNING: stirrer feeding zones do NOT span the belt (sum delta_af = 9.8883e+00 < delta_a = 1.0000e+01). The Krivov & Booth (2018) self-stirring picture assumes the stirrers can dynamically reach across the whole disk width.
  Continue the simulation anyway? [y/N]   Continuing at user request.

Beginning the main integration
Output 1/100: t=0.0 yr, dE/E0=0.00e+00, N=102
  Estimated time remaining to complete simulation: 7 seconds
  Estimated time remaining to next output: 0 seconds
Output 2/100: t=1000000.0 yr, dE/E0=2.69e-13, N=102
  Estimated time remaining to complete simulation: 1 hours, 20 minutes, 27 seconds
  Estimated time remaining to next output: 49 seconds
Output 3/100: t=2000000.0 yr, dE/E0=4.47e-15, N=102
  Estimated time remaining to complete simulation: 1 hours, 46 minutes, 10 seconds
  Estimated time remaining to next output: 1 minutes, 5 seconds
Output 4/100: t=3000000.0 yr, dE/E0=3.61e-14, N=102
  Estimated time remaining to complete simulation: 1 hours, 58 minutes, 40 seconds
  Estimated time remaining to next output: 1 minutes, 14 seconds
Output 5/100: t=4000000.0 yr, dE/E0=4.25e-13, N=102
  Estimated time remaining to complete simulation: 2 hours, 5 minutes, 31 seconds
  Estimated time remaining to next output: 1 minutes, 19 seconds
Output 6/100: t=5000000.0 yr, dE/E0=7.18e-13, N=102
  Estimated time remaining to complete simulation: 2 hours, 9 minutes, 37 seconds
  Estimated time remaining to next output: 1 minutes, 22 seconds
Output 7/100: t=6000000.0 yr, dE/E0=1.07e-12, N=102
  Estimated time remaining to complete simulation: 2 hours, 12 minutes, 21 seconds
  Estimated time remaining to next output: 1 minutes, 25 seconds
Output 8/100: t=7000000.0 yr, dE/E0=1.02e-12, N=102
  Estimated time remaining to complete simulation: 2 hours, 13 minutes, 56 seconds
  Estimated time remaining to next output: 1 minutes, 27 seconds
Output 9/100: t=8000000.0 yr, dE/E0=1.33e-12, N=102
  Estimated time remaining to complete simulation: 2 hours, 14 minutes, 34 seconds
  Estimated time remaining to next output: 1 minutes, 28 seconds
Output 10/100: t=9000000.0 yr, dE/E0=1.49e-12, N=102
  Estimated time remaining to complete simulation: 2 hours, 15 minutes, 33 seconds
  Estimated time remaining to next output: 1 minutes, 30 seconds
Output 11/100: t=10000000.0 yr, dE/E0=1.39e-12, N=102
  Estimated time remaining to complete simulation: 2 hours, 15 minutes, 29 seconds
  Estimated time remaining to next output: 1 minutes, 31 seconds
Output 12/100: t=11000000.0 yr, dE/E0=1.29e-12, N=102
  Estimated time remaining to complete simulation: 2 hours, 15 minutes, 8 seconds
  Estimated time remaining to next output: 1 minutes, 32 seconds
Output 13/100: t=12000000.0 yr, dE/E0=8.83e-13, N=102
  Estimated time remaining to complete simulation: 2 hours, 14 minutes, 43 seconds
  Estimated time remaining to next output: 1 minutes, 32 seconds
Output 14/100: t=13000000.0 yr, dE/E0=4.45e-13, N=102
  Estimated time remaining to complete simulation: 2 hours, 14 minutes, 3 seconds
  Estimated time remaining to next output: 1 minutes, 33 seconds
Output 15/100: t=14000000.0 yr, dE/E0=3.51e-13, N=102
  Estimated time remaining to complete simulation: 2 hours, 13 minutes, 20 seconds
  Estimated time remaining to next output: 1 minutes, 34 seconds
Output 16/100: t=15000000.0 yr, dE/E0=5.69e-13, N=102
  Estimated time remaining to complete simulation: 2 hours, 12 minutes, 30 seconds
  Estimated time remaining to next output: 1 minutes, 34 seconds
Output 17/100: t=16000000.0 yr, dE/E0=7.30e-13, N=102
  Estimated time remaining to complete simulation: 2 hours, 11 minutes, 37 seconds
  Estimated time remaining to next output: 1 minutes, 35 seconds
Output 18/100: t=17000000.0 yr, dE/E0=3.85e-13, N=102
  Estimated time remaining to complete simulation: 2 hours, 10 minutes, 42 seconds
  Estimated time remaining to next output: 1 minutes, 35 seconds
Output 19/100: t=18000000.0 yr, dE/E0=4.09e-13, N=102
  Estimated time remaining to complete simulation: 2 hours, 9 minutes, 44 seconds
  Estimated time remaining to next output: 1 minutes, 36 seconds
Output 20/100: t=19000000.0 yr, dE/E0=5.89e-13, N=102
  Estimated time remaining to complete simulation: 2 hours, 8 minutes, 38 seconds
  Estimated time remaining to next output: 1 minutes, 36 seconds
Output 21/100: t=20000000.0 yr, dE/E0=5.78e-13, N=102
  Estimated time remaining to complete simulation: 2 hours, 7 minutes, 27 seconds
  Estimated time remaining to next output: 1 minutes, 36 seconds
Output 22/100: t=21000000.0 yr, dE/E0=9.18e-13, N=102
  Estimated time remaining to complete simulation: 2 hours, 6 minutes, 12 seconds
  Estimated time remaining to next output: 1 minutes, 37 seconds
Output 23/100: t=22000000.0 yr, dE/E0=9.14e-13, N=102
  Estimated time remaining to complete simulation: 2 hours, 5 minutes, 2 seconds
  Estimated time remaining to next output: 1 minutes, 37 seconds
Output 24/100: t=23000000.0 yr, dE/E0=8.81e-13, N=102
  Estimated time remaining to complete simulation: 2 hours, 3 minutes, 38 seconds
  Estimated time remaining to next output: 1 minutes, 37 seconds
Output 25/100: t=24000000.0 yr, dE/E0=1.05e-12, N=102
  Estimated time remaining to complete simulation: 2 hours, 2 minutes, 21 seconds
  Estimated time remaining to next output: 1 minutes, 37 seconds
Output 26/100: t=25000000.0 yr, dE/E0=9.21e-13, N=102
  Estimated time remaining to complete simulation: 2 hours, 1 minutes, 3 seconds
  Estimated time remaining to next output: 1 minutes, 38 seconds
Output 27/100: t=26000000.0 yr, dE/E0=7.36e-13, N=102
  Estimated time remaining to complete simulation: 1 hours, 59 minutes, 41 seconds
  Estimated time remaining to next output: 1 minutes, 38 seconds
Output 28/100: t=27000000.0 yr, dE/E0=5.32e-13, N=102
  Estimated time remaining to complete simulation: 1 hours, 58 minutes, 17 seconds
  Estimated time remaining to next output: 1 minutes, 38 seconds
Output 29/100: t=28000000.0 yr, dE/E0=5.25e-13, N=102
  Estimated time remaining to complete simulation: 1 hours, 56 minutes, 54 seconds
  Estimated time remaining to next output: 1 minutes, 38 seconds
Output 30/100: t=29000000.0 yr, dE/E0=1.73e-13, N=102
  Estimated time remaining to complete simulation: 1 hours, 55 minutes, 28 seconds
  Estimated time remaining to next output: 1 minutes, 38 seconds
Output 31/100: t=30000000.0 yr, dE/E0=1.49e-13, N=102
  Estimated time remaining to complete simulation: 1 hours, 54 minutes, 3 seconds
  Estimated time remaining to next output: 1 minutes, 39 seconds
Output 32/100: t=31000000.0 yr, dE/E0=1.06e-12, N=102
  Estimated time remaining to complete simulation: 1 hours, 52 minutes, 35 seconds
  Estimated time remaining to next output: 1 minutes, 39 seconds
Output 33/100: t=32000000.0 yr, dE/E0=1.28e-12, N=102
  Estimated time remaining to complete simulation: 1 hours, 51 minutes, 8 seconds
  Estimated time remaining to next output: 1 minutes, 39 seconds
Output 34/100: t=33000000.0 yr, dE/E0=1.40e-12, N=102
  Estimated time remaining to complete simulation: 1 hours, 49 minutes, 40 seconds
  Estimated time remaining to next output: 1 minutes, 39 seconds
Output 35/100: t=34000000.0 yr, dE/E0=1.52e-12, N=102
  Estimated time remaining to complete simulation: 1 hours, 48 minutes, 11 seconds
  Estimated time remaining to next output: 1 minutes, 39 seconds
Output 36/100: t=35000000.0 yr, dE/E0=1.15e-12, N=102
  Estimated time remaining to complete simulation: 1 hours, 46 minutes, 41 seconds
  Estimated time remaining to next output: 1 minutes, 40 seconds
Output 37/100: t=36000000.0 yr, dE/E0=8.79e-13, N=102
  Estimated time remaining to complete simulation: 1 hours, 45 minutes, 10 seconds
  Estimated time remaining to next output: 1 minutes, 40 seconds
Output 38/100: t=37000000.0 yr, dE/E0=6.95e-13, N=102
  Estimated time remaining to complete simulation: 1 hours, 43 minutes, 39 seconds
  Estimated time remaining to next output: 1 minutes, 40 seconds
Output 39/100: t=38000000.0 yr, dE/E0=2.73e-13, N=102
  Estimated time remaining to complete simulation: 1 hours, 42 minutes, 8 seconds
  Estimated time remaining to next output: 1 minutes, 40 seconds
Output 40/100: t=39000000.0 yr, dE/E0=1.61e-13, N=102
  Estimated time remaining to complete simulation: 1 hours, 40 minutes, 36 seconds
  Estimated time remaining to next output: 1 minutes, 40 seconds
Output 41/100: t=40000000.0 yr, dE/E0=2.05e-13, N=102
  Estimated time remaining to complete simulation: 1 hours, 39 minutes, 4 seconds
  Estimated time remaining to next output: 1 minutes, 40 seconds
Output 42/100: t=41000000.0 yr, dE/E0=1.10e-13, N=102
  Estimated time remaining to complete simulation: 1 hours, 37 minutes, 31 seconds
  Estimated time remaining to next output: 1 minutes, 40 seconds
Output 43/100: t=42000000.0 yr, dE/E0=1.40e-13, N=102
  Estimated time remaining to complete simulation: 1 hours, 35 minutes, 59 seconds
  Estimated time remaining to next output: 1 minutes, 41 seconds
Output 44/100: t=43000000.0 yr, dE/E0=3.22e-13, N=102
  Estimated time remaining to complete simulation: 1 hours, 34 minutes, 27 seconds
  Estimated time remaining to next output: 1 minutes, 41 seconds
Output 45/100: t=44000000.0 yr, dE/E0=4.35e-13, N=102
  Estimated time remaining to complete simulation: 1 hours, 32 minutes, 54 seconds
  Estimated time remaining to next output: 1 minutes, 41 seconds
Output 46/100: t=45000000.0 yr, dE/E0=6.81e-13, N=102
  Estimated time remaining to complete simulation: 1 hours, 31 minutes, 20 seconds
  Estimated time remaining to next output: 1 minutes, 41 seconds
Output 47/100: t=46000000.0 yr, dE/E0=6.56e-13, N=102
  Estimated time remaining to complete simulation: 1 hours, 29 minutes, 47 seconds
  Estimated time remaining to next output: 1 minutes, 41 seconds
Output 48/100: t=47000000.0 yr, dE/E0=8.77e-13, N=102
  Estimated time remaining to complete simulation: 1 hours, 28 minutes, 11 seconds
  Estimated time remaining to next output: 1 minutes, 41 seconds
Output 49/100: t=48000000.0 yr, dE/E0=5.89e-13, N=102
  Estimated time remaining to complete simulation: 1 hours, 26 minutes, 37 seconds
  Estimated time remaining to next output: 1 minutes, 41 seconds
Output 50/100: t=49000000.0 yr, dE/E0=5.19e-13, N=102
  Estimated time remaining to complete simulation: 1 hours, 25 minutes, 1 seconds
  Estimated time remaining to next output: 1 minutes, 42 seconds
Output 51/100: t=50000000.0 yr, dE/E0=3.11e-12, N=102
  Estimated time remaining to complete simulation: 1 hours, 23 minutes, 25 seconds
  Estimated time remaining to next output: 1 minutes, 42 seconds
Output 52/100: t=51000000.0 yr, dE/E0=2.85e-12, N=102
  Estimated time remaining to complete simulation: 1 hours, 21 minutes, 49 seconds
  Estimated time remaining to next output: 1 minutes, 42 seconds
Output 53/100: t=52000000.0 yr, dE/E0=3.51e-12, N=102
  Estimated time remaining to complete simulation: 1 hours, 20 minutes, 12 seconds
  Estimated time remaining to next output: 1 minutes, 42 seconds
Output 54/100: t=53000000.0 yr, dE/E0=3.64e-12, N=102
  Estimated time remaining to complete simulation: 1 hours, 18 minutes, 35 seconds
  Estimated time remaining to next output: 1 minutes, 42 seconds
Output 55/100: t=54000000.0 yr, dE/E0=4.12e-12, N=102
  Estimated time remaining to complete simulation: 1 hours, 16 minutes, 57 seconds
  Estimated time remaining to next output: 1 minutes, 42 seconds
Output 56/100: t=55000000.0 yr, dE/E0=4.35e-12, N=102
  Estimated time remaining to complete simulation: 1 hours, 15 minutes, 19 seconds
  Estimated time remaining to next output: 1 minutes, 42 seconds
Output 57/100: t=56000000.0 yr, dE/E0=5.07e-12, N=102
  Estimated time remaining to complete simulation: 1 hours, 13 minutes, 42 seconds
  Estimated time remaining to next output: 1 minutes, 42 seconds
Output 58/100: t=57000000.0 yr, dE/E0=5.15e-12, N=102
  Estimated time remaining to complete simulation: 1 hours, 12 minutes, 3 seconds
  Estimated time remaining to next output: 1 minutes, 42 seconds
Output 59/100: t=58000000.0 yr, dE/E0=4.63e-12, N=102
  Estimated time remaining to complete simulation: 1 hours, 10 minutes, 24 seconds
  Estimated time remaining to next output: 1 minutes, 43 seconds
Output 60/100: t=59000000.0 yr, dE/E0=4.74e-12, N=102
  Estimated time remaining to complete simulation: 1 hours, 8 minutes, 45 seconds
  Estimated time remaining to next output: 1 minutes, 43 seconds
Output 61/100: t=60000000.0 yr, dE/E0=4.66e-12, N=102
  Estimated time remaining to complete simulation: 1 hours, 7 minutes, 5 seconds
  Estimated time remaining to next output: 1 minutes, 43 seconds
Output 62/100: t=61000000.0 yr, dE/E0=4.90e-12, N=102
  Estimated time remaining to complete simulation: 1 hours, 5 minutes, 25 seconds
  Estimated time remaining to next output: 1 minutes, 43 seconds
Output 63/100: t=62000000.0 yr, dE/E0=4.39e-12, N=102
  Estimated time remaining to complete simulation: 1 hours, 3 minutes, 45 seconds
  Estimated time remaining to next output: 1 minutes, 43 seconds
Output 64/100: t=63000000.0 yr, dE/E0=4.91e-12, N=102
  Estimated time remaining to complete simulation: 1 hours, 2 minutes, 4 seconds
  Estimated time remaining to next output: 1 minutes, 43 seconds
Output 65/100: t=64000000.0 yr, dE/E0=5.30e-12, N=102
  Estimated time remaining to complete simulation: 1 hours, 24 seconds
  Estimated time remaining to next output: 1 minutes, 43 seconds
Output 66/100: t=65000000.0 yr, dE/E0=5.73e-12, N=102
  Estimated time remaining to complete simulation: 58 minutes, 43 seconds
  Estimated time remaining to next output: 1 minutes, 43 seconds
Output 67/100: t=66000000.0 yr, dE/E0=5.73e-12, N=102
  Estimated time remaining to complete simulation: 57 minutes, 2 seconds
  Estimated time remaining to next output: 1 minutes, 43 seconds
Output 68/100: t=67000000.0 yr, dE/E0=6.47e-12, N=102
  Estimated time remaining to complete simulation: 55 minutes, 20 seconds
  Estimated time remaining to next output: 1 minutes, 43 seconds
Output 69/100: t=68000000.0 yr, dE/E0=6.45e-12, N=102
  Estimated time remaining to complete simulation: 53 minutes, 39 seconds
  Estimated time remaining to next output: 1 minutes, 43 seconds
Output 70/100: t=69000000.0 yr, dE/E0=6.36e-12, N=102
  Estimated time remaining to complete simulation: 51 minutes, 57 seconds
  Estimated time remaining to next output: 1 minutes, 43 seconds
Output 71/100: t=70000000.0 yr, dE/E0=6.46e-12, N=102
  Estimated time remaining to complete simulation: 50 minutes, 14 seconds
  Estimated time remaining to next output: 1 minutes, 43 seconds
Output 72/100: t=71000000.0 yr, dE/E0=6.50e-12, N=102
  Estimated time remaining to complete simulation: 48 minutes, 32 seconds
  Estimated time remaining to next output: 1 minutes, 44 seconds
Output 73/100: t=72000000.0 yr, dE/E0=6.15e-12, N=102
  Estimated time remaining to complete simulation: 46 minutes, 50 seconds
  Estimated time remaining to next output: 1 minutes, 44 seconds
Output 74/100: t=73000000.0 yr, dE/E0=6.30e-12, N=102
  Estimated time remaining to complete simulation: 45 minutes, 7 seconds
  Estimated time remaining to next output: 1 minutes, 44 seconds
Output 75/100: t=74000000.0 yr, dE/E0=7.77e-12, N=102
  Estimated time remaining to complete simulation: 43 minutes, 25 seconds
  Estimated time remaining to next output: 1 minutes, 44 seconds
Output 76/100: t=75000000.0 yr, dE/E0=7.89e-12, N=102
  Estimated time remaining to complete simulation: 41 minutes, 42 seconds
  Estimated time remaining to next output: 1 minutes, 44 seconds
Output 77/100: t=76000000.0 yr, dE/E0=8.59e-12, N=102
  Estimated time remaining to complete simulation: 39 minutes, 59 seconds
  Estimated time remaining to next output: 1 minutes, 44 seconds
Output 78/100: t=77000000.0 yr, dE/E0=8.57e-12, N=102
  Estimated time remaining to complete simulation: 38 minutes, 16 seconds
  Estimated time remaining to next output: 1 minutes, 44 seconds
Output 79/100: t=78000000.0 yr, dE/E0=8.67e-12, N=102
  Estimated time remaining to complete simulation: 36 minutes, 33 seconds
  Estimated time remaining to next output: 1 minutes, 44 seconds
Output 80/100: t=79000000.0 yr, dE/E0=8.71e-12, N=102
  Estimated time remaining to complete simulation: 34 minutes, 50 seconds
  Estimated time remaining to next output: 1 minutes, 44 seconds
Output 81/100: t=80000000.0 yr, dE/E0=8.80e-12, N=102
  Estimated time remaining to complete simulation: 33 minutes, 7 seconds
  Estimated time remaining to next output: 1 minutes, 44 seconds
Output 82/100: t=81000000.0 yr, dE/E0=9.18e-12, N=102
  Estimated time remaining to complete simulation: 31 minutes, 24 seconds
  Estimated time remaining to next output: 1 minutes, 44 seconds
Output 83/100: t=82000000.0 yr, dE/E0=8.61e-12, N=102
  Estimated time remaining to complete simulation: 29 minutes, 40 seconds
  Estimated time remaining to next output: 1 minutes, 44 seconds
Output 84/100: t=83000000.0 yr, dE/E0=8.32e-12, N=102
  Estimated time remaining to complete simulation: 27 minutes, 56 seconds
  Estimated time remaining to next output: 1 minutes, 44 seconds
Output 85/100: t=84000000.0 yr, dE/E0=8.43e-12, N=102
  Estimated time remaining to complete simulation: 26 minutes, 13 seconds
  Estimated time remaining to next output: 1 minutes, 44 seconds
Output 86/100: t=85000000.0 yr, dE/E0=8.74e-12, N=102
  Estimated time remaining to complete simulation: 24 minutes, 28 seconds
  Estimated time remaining to next output: 1 minutes, 44 seconds
Output 87/100: t=86000000.0 yr, dE/E0=9.01e-12, N=102
  Estimated time remaining to complete simulation: 22 minutes, 44 seconds
  Estimated time remaining to next output: 1 minutes, 44 seconds
Output 88/100: t=87000000.0 yr, dE/E0=8.33e-12, N=102
  Estimated time remaining to complete simulation: 21 minutes
  Estimated time remaining to next output: 1 minutes, 45 seconds
Output 89/100: t=88000000.0 yr, dE/E0=8.11e-12, N=102
  Estimated time remaining to complete simulation: 19 minutes, 16 seconds
  Estimated time remaining to next output: 1 minutes, 45 seconds
Output 90/100: t=89000000.0 yr, dE/E0=8.08e-12, N=102
  Estimated time remaining to complete simulation: 17 minutes, 31 seconds
  Estimated time remaining to next output: 1 minutes, 45 seconds
Output 91/100: t=90000000.0 yr, dE/E0=8.17e-12, N=102
  Estimated time remaining to complete simulation: 15 minutes, 46 seconds
  Estimated time remaining to next output: 1 minutes, 45 seconds
Output 92/100: t=91000000.0 yr, dE/E0=8.04e-12, N=102
  Estimated time remaining to complete simulation: 14 minutes, 1 seconds
  Estimated time remaining to next output: 1 minutes, 45 seconds
Output 93/100: t=92000000.0 yr, dE/E0=8.38e-12, N=102
  Estimated time remaining to complete simulation: 12 minutes, 16 seconds
  Estimated time remaining to next output: 1 minutes, 45 seconds
Output 94/100: t=93000000.0 yr, dE/E0=8.98e-12, N=102
  Estimated time remaining to complete simulation: 10 minutes, 31 seconds
  Estimated time remaining to next output: 1 minutes, 45 seconds
Output 95/100: t=94000000.0 yr, dE/E0=8.97e-12, N=102
  Estimated time remaining to complete simulation: 8 minutes, 46 seconds
  Estimated time remaining to next output: 1 minutes, 45 seconds
Output 96/100: t=95000000.0 yr, dE/E0=9.51e-12, N=102
  Estimated time remaining to complete simulation: 7 minutes, 1 seconds
  Estimated time remaining to next output: 1 minutes, 45 seconds
Output 97/100: t=96000000.0 yr, dE/E0=9.40e-12, N=102
  Estimated time remaining to complete simulation: 5 minutes, 16 seconds
  Estimated time remaining to next output: 1 minutes, 45 seconds
Output 98/100: t=97000000.0 yr, dE/E0=9.14e-12, N=102
  Estimated time remaining to complete simulation: 3 minutes, 30 seconds
  Estimated time remaining to next output: 1 minutes, 45 seconds
Output 99/100: t=98000000.0 yr, dE/E0=9.05e-12, N=102
  Estimated time remaining to complete simulation: 1 minutes, 45 seconds
  Estimated time remaining to next output: 1 minutes, 45 seconds
Output 100/100: t=99000000.0 yr, dE/E0=8.56e-12, N=102
  Estimated time remaining to complete simulation: 0 seconds
Output 101/100: t=100000000.0 yr, dE/E0=8.77e-12, N=102
  Estimated time remaining to complete simulation: -1 months, 4 weeks, 1 days, 23 hours, 58 minutes, 15 seconds

Simulation complete.
Total runtime: 2 hours, 57 minutes, 41 seconds

Krivov & Booth (2018) self-stirring check (Eqs. 9-10):
  NOTE: a giant planet is present; the two-population self-stirring model assumes no external perturber, so C_e below is only indicative.
  Final time:                 t = 1.000000e+08 yr
  Rayleigh outlier cut:       e > 5 sigma = 1.9916e-03 (sigma = median(e)/sqrt(2 ln 2) = 3.9831e-04)
  Stirred-disk check:         median(e) = 4.6897e-04 vs 30 x disk.emax = 9.6000e-04 -> NOT stirred, cut not applied (every MP used)
  KS test of kept e vs Rayleigh: D = 0.7355, p = 6.41e-56  (WARNING: p < 0.05, kept e deviates from a Rayleigh distribution)
  RMS eccentricity (100 of 100 MPs): 1.460155e-02  (all MPs: 1.460155e-02)
  Belt geometry:              a = 100, da = 10, a/da = 10
  Masses:                     M_max = 1.742024e-13 Msun, M_disc = 1.742024e-11 Msun
  Implied stirring timescale: T = 4.399809e+15 yr
  Effective stirring factor:  C_e = 7489728606.5216  (all MPs, no cut: 7489728606.5216)
  WARNING: C_e = 7489728606.5216 >= 40 (Ida & Makino 1993 canonical value) -- this run stirs at or above the analytic self-stirring rate.
Saved archive: outputs/Kirvov_Calibration_sim_Mercurius_100Myr/Kirvov_Calibration_sim_Mercurius_100Myr.bin
Number of snapshots saved: 101
Archive time range: 0.000e+00 yr to 1.000e+08 yr
Particle-name check: OK (101 snapshots)
Loaded snapshot table from archive.
role
massive_planetesimal    100
star                      1
giant_planet              1
Name: count, dtype: int64
Saved: outputs/Kirvov_Calibration_sim_Mercurius_100Myr/figures/survival_fraction_vs_time.png
Saved: outputs/Kirvov_Calibration_sim_Mercurius_100Myr/figures/mean_semimajor_axis_vs_time.png
Saved: outputs/Kirvov_Calibration_sim_Mercurius_100Myr/figures/mean_eccentricity_vs_time.png
Saved: outputs/Kirvov_Calibration_sim_Mercurius_100Myr/figures/rms_eccentricity_vs_time.png
Saved: outputs/Kirvov_Calibration_sim_Mercurius_100Myr/figures/rms_inclination_vs_time.png
Saved: outputs/Kirvov_Calibration_sim_Mercurius_100Myr/figures/data/orbits_initial_final.csv
Saved: outputs/Kirvov_Calibration_sim_Mercurius_100Myr/figures/a_vs_e_initial_final.png
Saved: outputs/Kirvov_Calibration_sim_Mercurius_100Myr/figures/a_vs_i_initial_final.png
Inner plotted edge = 95.07 AU
Outer plotted edge = 104.89 AU
Saved: outputs/Kirvov_Calibration_sim_Mercurius_100Myr/figures/xy_initial_final.png
All summary figures saved.
```
