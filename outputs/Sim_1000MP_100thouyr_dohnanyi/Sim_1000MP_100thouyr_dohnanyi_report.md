# Sim_1000MP_100thouyr_dohnanyi — Simulation Report

Config file: `config/Sim_1000MP_100thouyr_dohnanyi.yaml`
Archive file: `outputs/Sim_1000MP_100thouyr_dohnanyi/Sim_1000MP_100thouyr_dohnanyi.bin`

## Provenance

- Run UUID: `a051955b-cea7-4987-ab5e-601a7aaab68e`
- Created: 2026-09-01T15:54:20-04:00
- Finished: 2026-09-02T22:55:20-04:00
- Wall runtime: 111656.2 s
- Outcome: completed
- Command: `src/simulation/run_simulation.py config/Sim_1000MP_100thouyr_dohnanyi.yaml`
- Git commit: `11237f126d1246bf36de360fd289542c0aeb86f8` (branch `main`) **(DIRTY — uncommitted tracked changes)**
    - modified: `config/Sim_1000MP_100thouyr_dohnanyi.yaml`
- Software: python 3.12.11, rebound 5.0.0, numpy 2.4.6, pandas 3.0.3, matplotlib 3.10.9, pyyaml 6.0.3
- Frozen config: `config.yaml` (this directory)
- Full environment: `environment.txt` (this directory)

## Simulation
- Name: Sim_1000MP_100thouyr_dohnanyi
- Output directory: outputs
- Dump/checkpoint enabled: True

## Units
- time = yr, length = AU, mass = Msun

## Integration
- Integrator: mercurius
- maxtime: 100000
- time_step: 100
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
- N: 1000
- Mass-assignment method (config): power_law distribution (mode=total_mass): variable=mass, [1e-06, 0.01] earth_mass, slope=1.8333, seed=42 (total_disk_mass_earth = 2.800000e-01 Earth masses, split across N by the power law)
- **Mass is NOT uniform** across the 1000 massive planetesimals:
  - min / median / max: 5.002424e-11 / 1.132883e-10 / 1.376425e-07 Msun
  - min / median / max: 1.665537e-05 / 3.771888e-05 / 4.582752e-02 Earth masses
  - total disk mass: 2.800000e-01 Earth masses

## Test Particles
- N: 0
- Distribution: uniform

## Run Summary (from archive)
- Initial particle count: 1001
- Final particle count: 1001
- Particles lost (escaped / unbound / other removal): 0
- Archive time range: 0.000000e+00 to 1.000000e+05
- Number of snapshots: 1001

## Terminal Output

```
Saving SimulationArchive to: outputs/Sim_1000MP_100thouyr_dohnanyi/Sim_1000MP_100thouyr_dohnanyi.bin
No existing dump_data.json found; starting fresh run.

No giant planet: integrating the disk around the star alone.
  Timestep: 9.259630e+01 (0.1 x circular period at a=95 (disk inner edge) = 9.259630e+02)

Massive planetesimal mass setup:
  Mode: total_disk_mass_earth  (total disk mass given; split among N by a power law)
  Number of planetesimals: 1000
  Mass spectrum: power_law in mass, slope=1.8333, 10000x dynamic range ([1e-06, 0.01] earth_mass sets the shape), seed=42
  NOTE: absolute scale is fixed by total_disk_mass_earth / N, not by the min/max above.
  Per-MP mass (Earth masses): min=1.665537e-05 / median=3.771888e-05 / max=4.582752e-02
  Per-MP diameter (km, uniform sphere, rho = 1 g/cm**3): min=574.910 / median=754.978 / max=8056.079
  Total disk mass: 2.800000e-01 Earth masses (8.409771e-07 Msun)
Saved: outputs/Sim_1000MP_100thouyr_dohnanyi/distribution.csv
Saved: outputs/Sim_1000MP_100thouyr_dohnanyi/figures/dohnanyi_per_particle.png
Saved: outputs/Sim_1000MP_100thouyr_dohnanyi/figures/dohnanyi_differential_histogram.png

Beginning the main integration
Output 1/1000: t=0.0 yr, dE/E0=0.00e+00, N=1001
  Estimated time remaining to complete simulation: 51 seconds
  Estimated time remaining to next output: 0 seconds
Output 2/1000: t=100.0 yr, dE/E0=5.01e-11, N=1001
  Estimated time remaining to complete simulation: 5 hours, 49 minutes, 52 seconds
  Estimated time remaining to next output: 21 seconds
Output 3/1000: t=200.0 yr, dE/E0=2.00e-10, N=1001
  Estimated time remaining to complete simulation: 7 hours, 11 minutes, 58 seconds
  Estimated time remaining to next output: 25 seconds
Output 4/1000: t=300.0 yr, dE/E0=4.05e-10, N=1001
  Estimated time remaining to complete simulation: 6 hours, 49 minutes, 19 seconds
  Estimated time remaining to next output: 24 seconds
Output 5/1000: t=400.0 yr, dE/E0=3.83e-10, N=1001
  Estimated time remaining to complete simulation: 6 hours, 40 minutes, 32 seconds
  Estimated time remaining to next output: 24 seconds
Output 6/1000: t=500.0 yr, dE/E0=2.11e-10, N=1001
  Estimated time remaining to complete simulation: 5 hours, 52 minutes, 23 seconds
  Estimated time remaining to next output: 21 seconds
Output 7/1000: t=600.0 yr, dE/E0=9.63e-11, N=1001
  Estimated time remaining to complete simulation: 5 hours, 30 minutes, 30 seconds
  Estimated time remaining to next output: 19 seconds
Output 8/1000: t=700.0 yr, dE/E0=1.48e-10, N=1001
  Estimated time remaining to complete simulation: 4 hours, 54 minutes, 47 seconds
  Estimated time remaining to next output: 17 seconds
Output 9/1000: t=800.0 yr, dE/E0=2.82e-10, N=1001
  Estimated time remaining to complete simulation: 4 hours, 43 minutes, 36 seconds
  Estimated time remaining to next output: 17 seconds
Output 10/1000: t=900.0 yr, dE/E0=2.35e-10, N=1001
  Estimated time remaining to complete simulation: 4 hours, 25 minutes, 47 seconds
  Estimated time remaining to next output: 16 seconds
Output 11/1000: t=1000.0 yr, dE/E0=2.89e-10, N=1001
  Estimated time remaining to complete simulation: 4 hours, 5 minutes, 46 seconds
  Estimated time remaining to next output: 14 seconds
Output 12/1000: t=1100.0 yr, dE/E0=3.53e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 48 minutes, 57 seconds
  Estimated time remaining to next output: 13 seconds
Output 13/1000: t=1200.0 yr, dE/E0=2.82e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 35 minutes, 10 seconds
  Estimated time remaining to next output: 13 seconds
Output 14/1000: t=1300.0 yr, dE/E0=4.74e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 38 minutes, 59 seconds
  Estimated time remaining to next output: 13 seconds
Output 15/1000: t=1400.0 yr, dE/E0=3.16e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 37 minutes, 3 seconds
  Estimated time remaining to next output: 13 seconds
Output 16/1000: t=1500.0 yr, dE/E0=1.59e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 26 minutes, 24 seconds
  Estimated time remaining to next output: 12 seconds
Output 17/1000: t=1600.0 yr, dE/E0=1.23e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 43 minutes, 21 seconds
  Estimated time remaining to next output: 13 seconds
Output 18/1000: t=1700.0 yr, dE/E0=5.25e-11, N=1001
  Estimated time remaining to complete simulation: 3 hours, 33 minutes, 32 seconds
  Estimated time remaining to next output: 13 seconds
Output 19/1000: t=1800.0 yr, dE/E0=5.91e-11, N=1001
  Estimated time remaining to complete simulation: 3 hours, 24 minutes, 49 seconds
  Estimated time remaining to next output: 12 seconds
Output 20/1000: t=1900.0 yr, dE/E0=1.97e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 17 minutes, 46 seconds
  Estimated time remaining to next output: 12 seconds
Output 21/1000: t=2000.0 yr, dE/E0=3.31e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 25 minutes, 29 seconds
  Estimated time remaining to next output: 12 seconds
Output 22/1000: t=2100.0 yr, dE/E0=4.42e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 23 minutes, 56 seconds
  Estimated time remaining to next output: 12 seconds
Output 23/1000: t=2200.0 yr, dE/E0=4.46e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 16 minutes, 52 seconds
  Estimated time remaining to next output: 12 seconds
Output 24/1000: t=2300.0 yr, dE/E0=3.64e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 21 minutes, 43 seconds
  Estimated time remaining to next output: 12 seconds
Output 25/1000: t=2400.0 yr, dE/E0=3.02e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 15 minutes, 19 seconds
  Estimated time remaining to next output: 12 seconds
Output 26/1000: t=2500.0 yr, dE/E0=4.47e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 9 minutes, 21 seconds
  Estimated time remaining to next output: 11 seconds
Output 27/1000: t=2600.0 yr, dE/E0=5.53e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 3 minutes, 46 seconds
  Estimated time remaining to next output: 11 seconds
Output 28/1000: t=2700.0 yr, dE/E0=5.03e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 4 minutes, 45 seconds
  Estimated time remaining to next output: 11 seconds
Output 29/1000: t=2800.0 yr, dE/E0=3.37e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 30 seconds
  Estimated time remaining to next output: 11 seconds
Output 30/1000: t=2900.0 yr, dE/E0=1.83e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 44 seconds
  Estimated time remaining to next output: 11 seconds
Output 31/1000: t=3000.0 yr, dE/E0=2.14e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 34 seconds
  Estimated time remaining to next output: 11 seconds
Output 32/1000: t=3100.0 yr, dE/E0=3.20e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 1 minutes, 50 seconds
  Estimated time remaining to next output: 11 seconds
Output 33/1000: t=3200.0 yr, dE/E0=3.28e-10, N=1001
  Estimated time remaining to complete simulation: 2 hours, 57 minutes, 30 seconds
  Estimated time remaining to next output: 11 seconds
Output 34/1000: t=3300.0 yr, dE/E0=2.92e-10, N=1001
  Estimated time remaining to complete simulation: 2 hours, 53 minutes, 23 seconds
  Estimated time remaining to next output: 10 seconds
Output 35/1000: t=3400.0 yr, dE/E0=1.65e-10, N=1001
  Estimated time remaining to complete simulation: 2 hours, 49 minutes, 32 seconds
  Estimated time remaining to next output: 10 seconds
Output 36/1000: t=3500.0 yr, dE/E0=4.79e-11, N=1001
  Estimated time remaining to complete simulation: 2 hours, 45 minutes, 55 seconds
  Estimated time remaining to next output: 10 seconds
Output 37/1000: t=3600.0 yr, dE/E0=1.12e-10, N=1001
  Estimated time remaining to complete simulation: 2 hours, 50 minutes, 27 seconds
  Estimated time remaining to next output: 10 seconds
Output 38/1000: t=3700.0 yr, dE/E0=1.30e-10, N=1001
  Estimated time remaining to complete simulation: 2 hours, 46 minutes, 58 seconds
  Estimated time remaining to next output: 10 seconds
Output 39/1000: t=3800.0 yr, dE/E0=1.35e-10, N=1001
  Estimated time remaining to complete simulation: 2 hours, 46 minutes, 44 seconds
  Estimated time remaining to next output: 10 seconds
Output 40/1000: t=3900.0 yr, dE/E0=1.82e-10, N=1001
  Estimated time remaining to complete simulation: 2 hours, 47 minutes, 25 seconds
  Estimated time remaining to next output: 10 seconds
Output 41/1000: t=4000.0 yr, dE/E0=3.36e-10, N=1001
  Estimated time remaining to complete simulation: 2 hours, 44 minutes, 18 seconds
  Estimated time remaining to next output: 10 seconds
Output 42/1000: t=4100.0 yr, dE/E0=3.66e-10, N=1001
  Estimated time remaining to complete simulation: 2 hours, 43 minutes, 51 seconds
  Estimated time remaining to next output: 10 seconds
Output 43/1000: t=4200.0 yr, dE/E0=4.50e-10, N=1001
  Estimated time remaining to complete simulation: 2 hours, 41 minutes, 45 seconds
  Estimated time remaining to next output: 10 seconds
Output 44/1000: t=4300.0 yr, dE/E0=6.40e-10, N=1001
  Estimated time remaining to complete simulation: 2 hours, 44 minutes, 10 seconds
  Estimated time remaining to next output: 10 seconds
Output 45/1000: t=4400.0 yr, dE/E0=6.68e-10, N=1001
  Estimated time remaining to complete simulation: 2 hours, 41 minutes, 20 seconds
  Estimated time remaining to next output: 10 seconds
Output 46/1000: t=4500.0 yr, dE/E0=4.19e-10, N=1001
  Estimated time remaining to complete simulation: 2 hours, 51 minutes, 48 seconds
  Estimated time remaining to next output: 10 seconds
Output 47/1000: t=4600.0 yr, dE/E0=1.16e-11, N=1001
  Estimated time remaining to complete simulation: 2 hours, 48 minutes, 55 seconds
  Estimated time remaining to next output: 10 seconds
Output 48/1000: t=4700.0 yr, dE/E0=2.63e-10, N=1001
  Estimated time remaining to complete simulation: 2 hours, 50 minutes, 52 seconds
  Estimated time remaining to next output: 10 seconds
Output 49/1000: t=4800.0 yr, dE/E0=6.45e-10, N=1001
  Estimated time remaining to complete simulation: 2 hours, 49 minutes, 28 seconds
  Estimated time remaining to next output: 10 seconds
Output 50/1000: t=4900.0 yr, dE/E0=6.64e-10, N=1001
  Estimated time remaining to complete simulation: 2 hours, 48 minutes, 6 seconds
  Estimated time remaining to next output: 10 seconds
Output 51/1000: t=5000.0 yr, dE/E0=4.91e-10, N=1001
  Estimated time remaining to complete simulation: 2 hours, 46 minutes, 31 seconds
  Estimated time remaining to next output: 10 seconds
Output 52/1000: t=5100.0 yr, dE/E0=2.11e-10, N=1001
  Estimated time remaining to complete simulation: 2 hours, 45 minutes, 47 seconds
  Estimated time remaining to next output: 10 seconds
Output 53/1000: t=5200.0 yr, dE/E0=1.93e-10, N=1001
  Estimated time remaining to complete simulation: 2 hours, 43 minutes, 21 seconds
  Estimated time remaining to next output: 10 seconds
Output 54/1000: t=5300.0 yr, dE/E0=2.20e-10, N=1001
  Estimated time remaining to complete simulation: 2 hours, 48 minutes, 55 seconds
  Estimated time remaining to next output: 10 seconds
Output 55/1000: t=5400.0 yr, dE/E0=3.05e-10, N=1001
  Estimated time remaining to complete simulation: 2 hours, 57 minutes, 27 seconds
  Estimated time remaining to next output: 11 seconds
Output 56/1000: t=5500.0 yr, dE/E0=3.22e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 4 minutes, 47 seconds
  Estimated time remaining to next output: 11 seconds
Output 57/1000: t=5600.0 yr, dE/E0=3.94e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 6 minutes, 21 seconds
  Estimated time remaining to next output: 11 seconds
Output 58/1000: t=5700.0 yr, dE/E0=3.76e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 3 minutes, 42 seconds
  Estimated time remaining to next output: 11 seconds
Output 59/1000: t=5800.0 yr, dE/E0=3.35e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 1 minutes, 49 seconds
  Estimated time remaining to next output: 11 seconds
Output 60/1000: t=5900.0 yr, dE/E0=1.89e-10, N=1001
  Estimated time remaining to complete simulation: 2 hours, 59 minutes, 23 seconds
  Estimated time remaining to next output: 11 seconds
Output 61/1000: t=6000.0 yr, dE/E0=2.22e-10, N=1001
  Estimated time remaining to complete simulation: 2 hours, 56 minutes, 59 seconds
  Estimated time remaining to next output: 11 seconds
Output 62/1000: t=6100.0 yr, dE/E0=2.96e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 1 minutes, 6 seconds
  Estimated time remaining to next output: 11 seconds
Output 63/1000: t=6200.0 yr, dE/E0=3.15e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 6 minutes, 31 seconds
  Estimated time remaining to next output: 11 seconds
Output 64/1000: t=6300.0 yr, dE/E0=1.37e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 6 minutes, 5 seconds
  Estimated time remaining to next output: 11 seconds
Output 65/1000: t=6400.0 yr, dE/E0=6.81e-11, N=1001
  Estimated time remaining to complete simulation: 3 hours, 6 minutes, 32 seconds
  Estimated time remaining to next output: 11 seconds
Output 66/1000: t=6500.0 yr, dE/E0=9.28e-11, N=1001
  Estimated time remaining to complete simulation: 3 hours, 7 minutes, 41 seconds
  Estimated time remaining to next output: 12 seconds
Output 67/1000: t=6600.0 yr, dE/E0=2.47e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 10 minutes, 43 seconds
  Estimated time remaining to next output: 12 seconds
Output 68/1000: t=6700.0 yr, dE/E0=3.52e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 11 minutes, 48 seconds
  Estimated time remaining to next output: 12 seconds
Output 69/1000: t=6800.0 yr, dE/E0=3.33e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 9 minutes, 28 seconds
  Estimated time remaining to next output: 12 seconds
Output 70/1000: t=6900.0 yr, dE/E0=3.94e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 9 minutes, 56 seconds
  Estimated time remaining to next output: 12 seconds
Output 71/1000: t=7000.0 yr, dE/E0=3.33e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 7 minutes, 40 seconds
  Estimated time remaining to next output: 12 seconds
Output 72/1000: t=7100.0 yr, dE/E0=1.41e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 10 minutes, 52 seconds
  Estimated time remaining to next output: 12 seconds
Output 73/1000: t=7200.0 yr, dE/E0=8.78e-11, N=1001
  Estimated time remaining to complete simulation: 3 hours, 8 minutes, 46 seconds
  Estimated time remaining to next output: 12 seconds
Output 74/1000: t=7300.0 yr, dE/E0=1.10e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 6 minutes, 37 seconds
  Estimated time remaining to next output: 12 seconds
Output 75/1000: t=7400.0 yr, dE/E0=2.62e-11, N=1001
  Estimated time remaining to complete simulation: 3 hours, 4 minutes, 34 seconds
  Estimated time remaining to next output: 11 seconds
Output 76/1000: t=7500.0 yr, dE/E0=3.49e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 3 minutes, 16 seconds
  Estimated time remaining to next output: 11 seconds
Output 77/1000: t=7600.0 yr, dE/E0=6.02e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 1 minutes, 17 seconds
  Estimated time remaining to next output: 11 seconds
Output 78/1000: t=7700.0 yr, dE/E0=4.54e-10, N=1001
  Estimated time remaining to complete simulation: 2 hours, 59 minutes, 20 seconds
  Estimated time remaining to next output: 11 seconds
Output 79/1000: t=7800.0 yr, dE/E0=1.13e-11, N=1001
  Estimated time remaining to complete simulation: 2 hours, 57 minutes, 29 seconds
  Estimated time remaining to next output: 11 seconds
Output 80/1000: t=7900.0 yr, dE/E0=7.86e-11, N=1001
  Estimated time remaining to complete simulation: 2 hours, 55 minutes, 38 seconds
  Estimated time remaining to next output: 11 seconds
Output 81/1000: t=8000.0 yr, dE/E0=5.34e-10, N=1001
  Estimated time remaining to complete simulation: 2 hours, 53 minutes, 49 seconds
  Estimated time remaining to next output: 11 seconds
Output 82/1000: t=8100.0 yr, dE/E0=6.68e-10, N=1001
  Estimated time remaining to complete simulation: 2 hours, 53 minutes, 16 seconds
  Estimated time remaining to next output: 11 seconds
Output 83/1000: t=8200.0 yr, dE/E0=9.18e-10, N=1001
  Estimated time remaining to complete simulation: 2 hours, 56 minutes, 7 seconds
  Estimated time remaining to next output: 11 seconds
Output 84/1000: t=8300.0 yr, dE/E0=3.69e-10, N=1001
  Estimated time remaining to complete simulation: 4 hours, 19 minutes, 23 seconds
  Estimated time remaining to next output: 16 seconds
Output 85/1000: t=8400.0 yr, dE/E0=2.56e-10, N=1001
  Estimated time remaining to complete simulation: 4 hours, 17 minutes, 9 seconds
  Estimated time remaining to next output: 16 seconds
Output 86/1000: t=8500.0 yr, dE/E0=2.02e-10, N=1001
  Estimated time remaining to complete simulation: 4 hours, 17 minutes, 48 seconds
  Estimated time remaining to next output: 16 seconds
Output 87/1000: t=8600.0 yr, dE/E0=5.87e-10, N=1001
  Estimated time remaining to complete simulation: 4 hours, 15 minutes, 5 seconds
  Estimated time remaining to next output: 16 seconds
Output 88/1000: t=8700.0 yr, dE/E0=7.04e-10, N=1001
  Estimated time remaining to complete simulation: 4 hours, 12 minutes, 29 seconds
  Estimated time remaining to next output: 16 seconds
Output 89/1000: t=8800.0 yr, dE/E0=4.93e-10, N=1001
  Estimated time remaining to complete simulation: 4 hours, 11 minutes, 32 seconds
  Estimated time remaining to next output: 16 seconds
Output 90/1000: t=8900.0 yr, dE/E0=4.68e-10, N=1001
  Estimated time remaining to complete simulation: 4 hours, 10 minutes, 23 seconds
  Estimated time remaining to next output: 16 seconds
Output 91/1000: t=9000.0 yr, dE/E0=2.69e-10, N=1001
  Estimated time remaining to complete simulation: 4 hours, 7 minutes, 51 seconds
  Estimated time remaining to next output: 16 seconds
Output 92/1000: t=9100.0 yr, dE/E0=2.67e-10, N=1001
  Estimated time remaining to complete simulation: 4 hours, 8 minutes, 52 seconds
  Estimated time remaining to next output: 16 seconds
Output 93/1000: t=9200.0 yr, dE/E0=2.73e-10, N=1001
  Estimated time remaining to complete simulation: 4 hours, 9 minutes, 26 seconds
  Estimated time remaining to next output: 16 seconds
Output 94/1000: t=9300.0 yr, dE/E0=2.95e-10, N=1001
  Estimated time remaining to complete simulation: 4 hours, 6 minutes, 58 seconds
  Estimated time remaining to next output: 16 seconds
Output 95/1000: t=9400.0 yr, dE/E0=5.01e-11, N=1001
  Estimated time remaining to complete simulation: 4 hours, 4 minutes, 53 seconds
  Estimated time remaining to next output: 16 seconds
Output 96/1000: t=9500.0 yr, dE/E0=4.05e-11, N=1001
  Estimated time remaining to complete simulation: 4 hours, 3 minutes, 11 seconds
  Estimated time remaining to next output: 16 seconds
Output 97/1000: t=9600.0 yr, dE/E0=2.43e-12, N=1001
  Estimated time remaining to complete simulation: 4 hours, 22 minutes, 18 seconds
  Estimated time remaining to next output: 17 seconds
Output 98/1000: t=9700.0 yr, dE/E0=4.96e-10, N=1001
  Estimated time remaining to complete simulation: 4 hours, 19 minutes, 50 seconds
  Estimated time remaining to next output: 17 seconds
Output 99/1000: t=9800.0 yr, dE/E0=7.30e-10, N=1001
  Estimated time remaining to complete simulation: 4 hours, 20 minutes, 7 seconds
  Estimated time remaining to next output: 17 seconds
Output 100/1000: t=9900.0 yr, dE/E0=6.88e-10, N=1001
  Estimated time remaining to complete simulation: 4 hours, 17 minutes, 45 seconds
  Estimated time remaining to next output: 17 seconds
Output 101/1000: t=10000.0 yr, dE/E0=3.82e-10, N=1001
  Estimated time remaining to complete simulation: 4 hours, 15 minutes, 22 seconds
  Estimated time remaining to next output: 17 seconds
Output 102/1000: t=10100.0 yr, dE/E0=1.42e-10, N=1001
  Estimated time remaining to complete simulation: 4 hours, 13 minutes
  Estimated time remaining to next output: 16 seconds
Output 103/1000: t=10200.0 yr, dE/E0=5.32e-11, N=1001
  Estimated time remaining to complete simulation: 4 hours, 11 minutes, 30 seconds
  Estimated time remaining to next output: 16 seconds
Output 104/1000: t=10300.0 yr, dE/E0=2.76e-11, N=1001
  Estimated time remaining to complete simulation: 4 hours, 9 minutes, 13 seconds
  Estimated time remaining to next output: 16 seconds
Output 105/1000: t=10400.0 yr, dE/E0=7.73e-11, N=1001
  Estimated time remaining to complete simulation: 4 hours, 8 minutes, 45 seconds
  Estimated time remaining to next output: 16 seconds
Output 106/1000: t=10500.0 yr, dE/E0=1.63e-10, N=1001
  Estimated time remaining to complete simulation: 4 hours, 6 minutes, 38 seconds
  Estimated time remaining to next output: 16 seconds
Output 107/1000: t=10600.0 yr, dE/E0=2.57e-10, N=1001
  Estimated time remaining to complete simulation: 4 hours, 6 minutes, 36 seconds
  Estimated time remaining to next output: 16 seconds
Output 108/1000: t=10700.0 yr, dE/E0=3.71e-10, N=1001
  Estimated time remaining to complete simulation: 4 hours, 4 minutes, 35 seconds
  Estimated time remaining to next output: 16 seconds
Output 109/1000: t=10800.0 yr, dE/E0=2.11e-10, N=1001
  Estimated time remaining to complete simulation: 4 hours, 2 minutes, 30 seconds
  Estimated time remaining to next output: 16 seconds
Output 110/1000: t=10900.0 yr, dE/E0=1.10e-10, N=1001
  Estimated time remaining to complete simulation: 4 hours, 1 minutes, 21 seconds
  Estimated time remaining to next output: 16 seconds
Output 111/1000: t=11000.0 yr, dE/E0=2.36e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 59 minutes, 48 seconds
  Estimated time remaining to next output: 16 seconds
Output 112/1000: t=11100.0 yr, dE/E0=5.19e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 57 minutes, 48 seconds
  Estimated time remaining to next output: 16 seconds
Output 113/1000: t=11200.0 yr, dE/E0=5.06e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 55 minutes, 53 seconds
  Estimated time remaining to next output: 15 seconds
Output 114/1000: t=11300.0 yr, dE/E0=4.89e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 55 minutes, 21 seconds
  Estimated time remaining to next output: 15 seconds
Output 115/1000: t=11400.0 yr, dE/E0=3.41e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 53 minutes, 26 seconds
  Estimated time remaining to next output: 15 seconds
Output 116/1000: t=11500.0 yr, dE/E0=2.05e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 51 minutes, 31 seconds
  Estimated time remaining to next output: 15 seconds
Output 117/1000: t=11600.0 yr, dE/E0=1.38e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 49 minutes, 38 seconds
  Estimated time remaining to next output: 15 seconds
Output 118/1000: t=11700.0 yr, dE/E0=1.10e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 51 minutes, 24 seconds
  Estimated time remaining to next output: 15 seconds
Output 119/1000: t=11800.0 yr, dE/E0=1.42e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 49 minutes, 34 seconds
  Estimated time remaining to next output: 15 seconds
Output 120/1000: t=11900.0 yr, dE/E0=1.04e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 47 minutes, 46 seconds
  Estimated time remaining to next output: 15 seconds
Output 121/1000: t=12000.0 yr, dE/E0=6.22e-11, N=1001
  Estimated time remaining to complete simulation: 3 hours, 45 minutes, 59 seconds
  Estimated time remaining to next output: 15 seconds
Output 122/1000: t=12100.0 yr, dE/E0=7.73e-11, N=1001
  Estimated time remaining to complete simulation: 3 hours, 45 minutes, 5 seconds
  Estimated time remaining to next output: 15 seconds
Output 123/1000: t=12200.0 yr, dE/E0=2.55e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 43 minutes, 22 seconds
  Estimated time remaining to next output: 15 seconds
Output 124/1000: t=12300.0 yr, dE/E0=5.73e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 41 minutes, 40 seconds
  Estimated time remaining to next output: 15 seconds
Output 125/1000: t=12400.0 yr, dE/E0=6.35e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 41 minutes, 38 seconds
  Estimated time remaining to next output: 15 seconds
Output 126/1000: t=12500.0 yr, dE/E0=5.06e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 39 minutes, 57 seconds
  Estimated time remaining to next output: 15 seconds
Output 127/1000: t=12600.0 yr, dE/E0=9.06e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 38 minutes, 24 seconds
  Estimated time remaining to next output: 15 seconds
Output 128/1000: t=12700.0 yr, dE/E0=6.15e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 37 minutes, 51 seconds
  Estimated time remaining to next output: 14 seconds
Output 129/1000: t=12800.0 yr, dE/E0=6.39e-11, N=1001
  Estimated time remaining to complete simulation: 3 hours, 36 minutes, 17 seconds
  Estimated time remaining to next output: 14 seconds
Output 130/1000: t=12900.0 yr, dE/E0=1.98e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 37 minutes, 20 seconds
  Estimated time remaining to next output: 14 seconds
Output 131/1000: t=13000.0 yr, dE/E0=4.92e-11, N=1001
  Estimated time remaining to complete simulation: 3 hours, 37 minutes, 58 seconds
  Estimated time remaining to next output: 15 seconds
Output 132/1000: t=13100.0 yr, dE/E0=3.58e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 40 minutes, 7 seconds
  Estimated time remaining to next output: 15 seconds
Output 133/1000: t=13200.0 yr, dE/E0=5.18e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 42 minutes, 13 seconds
  Estimated time remaining to next output: 15 seconds
Output 134/1000: t=13300.0 yr, dE/E0=5.01e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 40 minutes, 47 seconds
  Estimated time remaining to next output: 15 seconds
Output 135/1000: t=13400.0 yr, dE/E0=1.59e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 39 minutes, 15 seconds
  Estimated time remaining to next output: 15 seconds
Output 136/1000: t=13500.0 yr, dE/E0=1.19e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 37 minutes, 54 seconds
  Estimated time remaining to next output: 15 seconds
Output 137/1000: t=13600.0 yr, dE/E0=1.65e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 36 minutes, 25 seconds
  Estimated time remaining to next output: 15 seconds
Output 138/1000: t=13700.0 yr, dE/E0=1.86e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 35 minutes, 41 seconds
  Estimated time remaining to next output: 15 seconds
Output 139/1000: t=13800.0 yr, dE/E0=1.79e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 34 minutes, 15 seconds
  Estimated time remaining to next output: 14 seconds
Output 140/1000: t=13900.0 yr, dE/E0=2.87e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 33 minutes, 9 seconds
  Estimated time remaining to next output: 14 seconds
Output 141/1000: t=14000.0 yr, dE/E0=2.53e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 31 minutes, 45 seconds
  Estimated time remaining to next output: 14 seconds
Output 142/1000: t=14100.0 yr, dE/E0=2.21e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 30 minutes, 20 seconds
  Estimated time remaining to next output: 14 seconds
Output 143/1000: t=14200.0 yr, dE/E0=2.86e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 31 minutes, 13 seconds
  Estimated time remaining to next output: 14 seconds
Output 144/1000: t=14300.0 yr, dE/E0=2.78e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 35 minutes, 51 seconds
  Estimated time remaining to next output: 15 seconds
Output 145/1000: t=14400.0 yr, dE/E0=1.86e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 34 minutes, 24 seconds
  Estimated time remaining to next output: 15 seconds
Output 146/1000: t=14500.0 yr, dE/E0=4.81e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 34 minutes, 23 seconds
  Estimated time remaining to next output: 15 seconds
Output 147/1000: t=14600.0 yr, dE/E0=7.02e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 33 minutes, 3 seconds
  Estimated time remaining to next output: 14 seconds
Output 148/1000: t=14700.0 yr, dE/E0=6.46e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 31 minutes, 42 seconds
  Estimated time remaining to next output: 14 seconds
Output 149/1000: t=14800.0 yr, dE/E0=5.58e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 31 minutes, 33 seconds
  Estimated time remaining to next output: 14 seconds
Output 150/1000: t=14900.0 yr, dE/E0=4.82e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 30 minutes, 12 seconds
  Estimated time remaining to next output: 14 seconds
Output 151/1000: t=15000.0 yr, dE/E0=4.20e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 28 minutes, 50 seconds
  Estimated time remaining to next output: 14 seconds
Output 152/1000: t=15100.0 yr, dE/E0=2.67e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 30 minutes, 6 seconds
  Estimated time remaining to next output: 14 seconds
Output 153/1000: t=15200.0 yr, dE/E0=7.29e-11, N=1001
  Estimated time remaining to complete simulation: 3 hours, 28 minutes, 46 seconds
  Estimated time remaining to next output: 14 seconds
Output 154/1000: t=15300.0 yr, dE/E0=2.79e-11, N=1001
  Estimated time remaining to complete simulation: 3 hours, 29 minutes, 29 seconds
  Estimated time remaining to next output: 14 seconds
Output 155/1000: t=15400.0 yr, dE/E0=2.03e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 28 minutes, 27 seconds
  Estimated time remaining to next output: 14 seconds
Output 156/1000: t=15500.0 yr, dE/E0=2.95e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 31 minutes, 14 seconds
  Estimated time remaining to next output: 15 seconds
Output 157/1000: t=15600.0 yr, dE/E0=2.78e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 30 minutes, 1 seconds
  Estimated time remaining to next output: 14 seconds
Output 158/1000: t=15700.0 yr, dE/E0=7.90e-13, N=1001
  Estimated time remaining to complete simulation: 3 hours, 28 minutes, 42 seconds
  Estimated time remaining to next output: 14 seconds
Output 159/1000: t=15800.0 yr, dE/E0=9.84e-11, N=1001
  Estimated time remaining to complete simulation: 3 hours, 27 minutes, 25 seconds
  Estimated time remaining to next output: 14 seconds
Output 160/1000: t=15900.0 yr, dE/E0=4.92e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 26 minutes, 53 seconds
  Estimated time remaining to next output: 14 seconds
Output 161/1000: t=16000.0 yr, dE/E0=4.33e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 26 minutes, 31 seconds
  Estimated time remaining to next output: 14 seconds
Output 162/1000: t=16100.0 yr, dE/E0=3.73e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 25 minutes, 15 seconds
  Estimated time remaining to next output: 14 seconds
Output 163/1000: t=16200.0 yr, dE/E0=2.83e-11, N=1001
  Estimated time remaining to complete simulation: 3 hours, 25 minutes
  Estimated time remaining to next output: 14 seconds
Output 164/1000: t=16300.0 yr, dE/E0=8.29e-11, N=1001
  Estimated time remaining to complete simulation: 3 hours, 25 minutes, 4 seconds
  Estimated time remaining to next output: 14 seconds
Output 165/1000: t=16400.0 yr, dE/E0=6.32e-11, N=1001
  Estimated time remaining to complete simulation: 3 hours, 25 minutes, 45 seconds
  Estimated time remaining to next output: 14 seconds
Output 166/1000: t=16500.0 yr, dE/E0=3.16e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 24 minutes, 54 seconds
  Estimated time remaining to next output: 14 seconds
Output 167/1000: t=16600.0 yr, dE/E0=4.75e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 23 minutes, 44 seconds
  Estimated time remaining to next output: 14 seconds
Output 168/1000: t=16700.0 yr, dE/E0=4.66e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 23 minutes, 21 seconds
  Estimated time remaining to next output: 14 seconds
Output 169/1000: t=16800.0 yr, dE/E0=1.45e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 22 minutes, 18 seconds
  Estimated time remaining to next output: 14 seconds
Output 170/1000: t=16900.0 yr, dE/E0=1.63e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 21 minutes, 17 seconds
  Estimated time remaining to next output: 14 seconds
Output 171/1000: t=17000.0 yr, dE/E0=1.37e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 20 minutes, 24 seconds
  Estimated time remaining to next output: 14 seconds
Output 172/1000: t=17100.0 yr, dE/E0=3.49e-12, N=1001
  Estimated time remaining to complete simulation: 3 hours, 19 minutes, 55 seconds
  Estimated time remaining to next output: 14 seconds
Output 173/1000: t=17200.0 yr, dE/E0=5.25e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 19 minutes, 5 seconds
  Estimated time remaining to next output: 14 seconds
Output 174/1000: t=17300.0 yr, dE/E0=9.04e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 19 minutes, 43 seconds
  Estimated time remaining to next output: 14 seconds
Output 175/1000: t=17400.0 yr, dE/E0=8.40e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 18 minutes, 34 seconds
  Estimated time remaining to next output: 14 seconds
Output 176/1000: t=17500.0 yr, dE/E0=4.89e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 17 minutes, 26 seconds
  Estimated time remaining to next output: 14 seconds
Output 177/1000: t=17600.0 yr, dE/E0=1.00e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 16 minutes, 38 seconds
  Estimated time remaining to next output: 14 seconds
Output 178/1000: t=17700.0 yr, dE/E0=3.39e-11, N=1001
  Estimated time remaining to complete simulation: 3 hours, 15 minutes, 31 seconds
  Estimated time remaining to next output: 14 seconds
Output 179/1000: t=17800.0 yr, dE/E0=1.10e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 14 minutes, 24 seconds
  Estimated time remaining to next output: 14 seconds
Output 180/1000: t=17900.0 yr, dE/E0=3.82e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 13 minutes, 18 seconds
  Estimated time remaining to next output: 14 seconds
Output 181/1000: t=18000.0 yr, dE/E0=3.86e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 12 minutes, 32 seconds
  Estimated time remaining to next output: 14 seconds
Output 182/1000: t=18100.0 yr, dE/E0=2.10e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 12 minutes, 23 seconds
  Estimated time remaining to next output: 14 seconds
Output 183/1000: t=18200.0 yr, dE/E0=1.95e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 11 minutes, 19 seconds
  Estimated time remaining to next output: 14 seconds
Output 184/1000: t=18300.0 yr, dE/E0=4.11e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 10 minutes, 16 seconds
  Estimated time remaining to next output: 13 seconds
Output 185/1000: t=18400.0 yr, dE/E0=6.25e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 9 minutes, 13 seconds
  Estimated time remaining to next output: 13 seconds
Output 186/1000: t=18500.0 yr, dE/E0=5.42e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 9 minutes, 39 seconds
  Estimated time remaining to next output: 13 seconds
Output 187/1000: t=18600.0 yr, dE/E0=2.35e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 8 minutes, 38 seconds
  Estimated time remaining to next output: 13 seconds
Output 188/1000: t=18700.0 yr, dE/E0=4.04e-11, N=1001
  Estimated time remaining to complete simulation: 3 hours, 7 minutes, 59 seconds
  Estimated time remaining to next output: 13 seconds
Output 189/1000: t=18800.0 yr, dE/E0=1.10e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 8 minutes, 23 seconds
  Estimated time remaining to next output: 13 seconds
Output 190/1000: t=18900.0 yr, dE/E0=3.15e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 7 minutes, 28 seconds
  Estimated time remaining to next output: 13 seconds
Output 191/1000: t=19000.0 yr, dE/E0=3.67e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 6 minutes, 34 seconds
  Estimated time remaining to next output: 13 seconds
Output 192/1000: t=19100.0 yr, dE/E0=3.81e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 7 minutes, 40 seconds
  Estimated time remaining to next output: 13 seconds
Output 193/1000: t=19200.0 yr, dE/E0=2.31e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 6 minutes, 58 seconds
  Estimated time remaining to next output: 13 seconds
Output 194/1000: t=19300.0 yr, dE/E0=1.32e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 6 minutes, 35 seconds
  Estimated time remaining to next output: 13 seconds
Output 195/1000: t=19400.0 yr, dE/E0=3.59e-11, N=1001
  Estimated time remaining to complete simulation: 3 hours, 6 minutes, 26 seconds
  Estimated time remaining to next output: 13 seconds
Output 196/1000: t=19500.0 yr, dE/E0=4.13e-11, N=1001
  Estimated time remaining to complete simulation: 3 hours, 6 minutes, 56 seconds
  Estimated time remaining to next output: 13 seconds
Output 197/1000: t=19600.0 yr, dE/E0=2.88e-11, N=1001
  Estimated time remaining to complete simulation: 3 hours, 8 minutes, 52 seconds
  Estimated time remaining to next output: 14 seconds
Output 198/1000: t=19700.0 yr, dE/E0=2.24e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 8 minutes, 41 seconds
  Estimated time remaining to next output: 14 seconds
Output 199/1000: t=19800.0 yr, dE/E0=1.62e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 7 minutes, 52 seconds
  Estimated time remaining to next output: 14 seconds
Output 200/1000: t=19900.0 yr, dE/E0=2.14e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 6 minutes, 57 seconds
  Estimated time remaining to next output: 14 seconds
Output 201/1000: t=20000.0 yr, dE/E0=3.50e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 6 minutes, 22 seconds
  Estimated time remaining to next output: 13 seconds
Output 202/1000: t=20100.0 yr, dE/E0=6.03e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 7 minutes, 16 seconds
  Estimated time remaining to next output: 14 seconds
Output 203/1000: t=20200.0 yr, dE/E0=7.00e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 7 minutes, 27 seconds
  Estimated time remaining to next output: 14 seconds
Output 204/1000: t=20300.0 yr, dE/E0=6.46e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 7 minutes, 2 seconds
  Estimated time remaining to next output: 14 seconds
Output 205/1000: t=20400.0 yr, dE/E0=4.08e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 6 minutes, 18 seconds
  Estimated time remaining to next output: 14 seconds
Output 206/1000: t=20500.0 yr, dE/E0=3.40e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 6 minutes, 38 seconds
  Estimated time remaining to next output: 14 seconds
Output 207/1000: t=20600.0 yr, dE/E0=7.18e-11, N=1001
  Estimated time remaining to complete simulation: 3 hours, 6 minutes
  Estimated time remaining to next output: 14 seconds
Output 208/1000: t=20700.0 yr, dE/E0=9.98e-12, N=1001
  Estimated time remaining to complete simulation: 3 hours, 5 minutes, 42 seconds
  Estimated time remaining to next output: 14 seconds
Output 209/1000: t=20800.0 yr, dE/E0=9.77e-11, N=1001
  Estimated time remaining to complete simulation: 3 hours, 5 minutes, 54 seconds
  Estimated time remaining to next output: 14 seconds
Output 210/1000: t=20900.0 yr, dE/E0=2.47e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 5 minutes, 8 seconds
  Estimated time remaining to next output: 14 seconds
Output 211/1000: t=21000.0 yr, dE/E0=1.71e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 4 minutes, 30 seconds
  Estimated time remaining to next output: 14 seconds
Output 212/1000: t=21100.0 yr, dE/E0=6.41e-11, N=1001
  Estimated time remaining to complete simulation: 3 hours, 3 minutes, 51 seconds
  Estimated time remaining to next output: 13 seconds
Output 213/1000: t=21200.0 yr, dE/E0=1.32e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 3 minutes, 1 seconds
  Estimated time remaining to next output: 13 seconds
Output 214/1000: t=21300.0 yr, dE/E0=2.93e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 4 minutes, 40 seconds
  Estimated time remaining to next output: 14 seconds
Output 215/1000: t=21400.0 yr, dE/E0=4.98e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 4 minutes, 23 seconds
  Estimated time remaining to next output: 14 seconds
Output 216/1000: t=21500.0 yr, dE/E0=4.66e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 6 minutes, 16 seconds
  Estimated time remaining to next output: 14 seconds
Output 217/1000: t=21600.0 yr, dE/E0=3.58e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 6 minutes, 20 seconds
  Estimated time remaining to next output: 14 seconds
Output 218/1000: t=21700.0 yr, dE/E0=2.73e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 5 minutes, 55 seconds
  Estimated time remaining to next output: 14 seconds
Output 219/1000: t=21800.0 yr, dE/E0=1.45e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 5 minutes, 23 seconds
  Estimated time remaining to next output: 14 seconds
Output 220/1000: t=21900.0 yr, dE/E0=3.74e-11, N=1001
  Estimated time remaining to complete simulation: 3 hours, 5 minutes, 12 seconds
  Estimated time remaining to next output: 14 seconds
Output 221/1000: t=22000.0 yr, dE/E0=9.56e-12, N=1001
  Estimated time remaining to complete simulation: 3 hours, 6 minutes, 5 seconds
  Estimated time remaining to next output: 14 seconds
Output 222/1000: t=22100.0 yr, dE/E0=3.02e-11, N=1001
  Estimated time remaining to complete simulation: 3 hours, 7 minutes, 9 seconds
  Estimated time remaining to next output: 14 seconds
Output 223/1000: t=22200.0 yr, dE/E0=3.92e-11, N=1001
  Estimated time remaining to complete simulation: 3 hours, 6 minutes, 17 seconds
  Estimated time remaining to next output: 14 seconds
Output 224/1000: t=22300.0 yr, dE/E0=8.73e-11, N=1001
  Estimated time remaining to complete simulation: 3 hours, 5 minutes, 42 seconds
  Estimated time remaining to next output: 14 seconds
Output 225/1000: t=22400.0 yr, dE/E0=2.89e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 5 minutes, 9 seconds
  Estimated time remaining to next output: 14 seconds
Output 226/1000: t=22500.0 yr, dE/E0=4.62e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 4 minutes, 22 seconds
  Estimated time remaining to next output: 14 seconds
Output 227/1000: t=22600.0 yr, dE/E0=4.42e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 4 minutes, 26 seconds
  Estimated time remaining to next output: 14 seconds
Output 228/1000: t=22700.0 yr, dE/E0=7.40e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 3 minutes, 41 seconds
  Estimated time remaining to next output: 14 seconds
Output 229/1000: t=22800.0 yr, dE/E0=5.97e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 3 minutes, 22 seconds
  Estimated time remaining to next output: 14 seconds
Output 230/1000: t=22900.0 yr, dE/E0=2.35e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 3 minutes, 29 seconds
  Estimated time remaining to next output: 14 seconds
Output 231/1000: t=23000.0 yr, dE/E0=1.11e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 3 minutes
  Estimated time remaining to next output: 14 seconds
Output 232/1000: t=23100.0 yr, dE/E0=3.57e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 2 minutes, 21 seconds
  Estimated time remaining to next output: 14 seconds
Output 233/1000: t=23200.0 yr, dE/E0=5.86e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 1 minutes, 35 seconds
  Estimated time remaining to next output: 14 seconds
Output 234/1000: t=23300.0 yr, dE/E0=5.50e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 1 minutes, 9 seconds
  Estimated time remaining to next output: 14 seconds
Output 235/1000: t=23400.0 yr, dE/E0=3.08e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 1 minutes, 26 seconds
  Estimated time remaining to next output: 14 seconds
Output 236/1000: t=23500.0 yr, dE/E0=1.40e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 48 seconds
  Estimated time remaining to next output: 14 seconds
Output 237/1000: t=23600.0 yr, dE/E0=7.34e-11, N=1001
  Estimated time remaining to complete simulation: 3 hours, 1 minutes, 12 seconds
  Estimated time remaining to next output: 14 seconds
Output 238/1000: t=23700.0 yr, dE/E0=8.28e-11, N=1001
  Estimated time remaining to complete simulation: 3 hours, 6 minutes, 3 seconds
  Estimated time remaining to next output: 14 seconds
Output 239/1000: t=23800.0 yr, dE/E0=1.25e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 5 minutes, 21 seconds
  Estimated time remaining to next output: 14 seconds
Output 240/1000: t=23900.0 yr, dE/E0=1.66e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 5 minutes
  Estimated time remaining to next output: 14 seconds
Output 241/1000: t=24000.0 yr, dE/E0=1.26e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 5 minutes, 29 seconds
  Estimated time remaining to next output: 14 seconds
Output 242/1000: t=24100.0 yr, dE/E0=1.30e-11, N=1001
  Estimated time remaining to complete simulation: 3 hours, 4 minutes, 38 seconds
  Estimated time remaining to next output: 14 seconds
Output 243/1000: t=24200.0 yr, dE/E0=2.56e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 4 minutes, 39 seconds
  Estimated time remaining to next output: 14 seconds
Output 244/1000: t=24300.0 yr, dE/E0=5.20e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 4 minutes, 3 seconds
  Estimated time remaining to next output: 14 seconds
Output 245/1000: t=24400.0 yr, dE/E0=7.04e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 3 minutes, 21 seconds
  Estimated time remaining to next output: 14 seconds
Output 246/1000: t=24500.0 yr, dE/E0=4.19e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 2 minutes, 49 seconds
  Estimated time remaining to next output: 14 seconds
Output 247/1000: t=24600.0 yr, dE/E0=1.79e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 2 minutes, 59 seconds
  Estimated time remaining to next output: 14 seconds
Output 248/1000: t=24700.0 yr, dE/E0=7.92e-11, N=1001
  Estimated time remaining to complete simulation: 3 hours, 3 minutes, 24 seconds
  Estimated time remaining to next output: 14 seconds
Output 249/1000: t=24800.0 yr, dE/E0=5.71e-11, N=1001
  Estimated time remaining to complete simulation: 3 hours, 2 minutes, 44 seconds
  Estimated time remaining to next output: 14 seconds
Output 250/1000: t=24900.0 yr, dE/E0=1.77e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 3 minutes, 48 seconds
  Estimated time remaining to next output: 14 seconds
Output 251/1000: t=25000.0 yr, dE/E0=1.17e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 3 minutes, 9 seconds
  Estimated time remaining to next output: 14 seconds
Output 252/1000: t=25100.0 yr, dE/E0=2.94e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 5 minutes, 28 seconds
  Estimated time remaining to next output: 14 seconds
Output 253/1000: t=25200.0 yr, dE/E0=4.23e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 4 minutes, 39 seconds
  Estimated time remaining to next output: 14 seconds
Output 254/1000: t=25300.0 yr, dE/E0=6.67e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 4 minutes
  Estimated time remaining to next output: 14 seconds
Output 255/1000: t=25400.0 yr, dE/E0=4.48e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 3 minutes, 43 seconds
  Estimated time remaining to next output: 14 seconds
Output 256/1000: t=25500.0 yr, dE/E0=4.84e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 3 minutes, 8 seconds
  Estimated time remaining to next output: 14 seconds
Output 257/1000: t=25600.0 yr, dE/E0=6.85e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 2 minutes, 30 seconds
  Estimated time remaining to next output: 14 seconds
Output 258/1000: t=25700.0 yr, dE/E0=5.20e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 1 minutes, 41 seconds
  Estimated time remaining to next output: 14 seconds
Output 259/1000: t=25800.0 yr, dE/E0=2.17e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 2 minutes, 16 seconds
  Estimated time remaining to next output: 14 seconds
Output 260/1000: t=25900.0 yr, dE/E0=8.98e-11, N=1001
  Estimated time remaining to complete simulation: 3 hours, 2 minutes, 25 seconds
  Estimated time remaining to next output: 14 seconds
Output 261/1000: t=26000.0 yr, dE/E0=2.66e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 1 minutes, 56 seconds
  Estimated time remaining to next output: 14 seconds
Output 262/1000: t=26100.0 yr, dE/E0=1.65e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 1 minutes, 20 seconds
  Estimated time remaining to next output: 14 seconds
Output 263/1000: t=26200.0 yr, dE/E0=2.16e-11, N=1001
  Estimated time remaining to complete simulation: 3 hours, 48 seconds
  Estimated time remaining to next output: 14 seconds
Output 264/1000: t=26300.0 yr, dE/E0=6.42e-11, N=1001
  Estimated time remaining to complete simulation: 3 hours, 13 seconds
  Estimated time remaining to next output: 14 seconds
Output 265/1000: t=26400.0 yr, dE/E0=4.82e-10, N=1001
  Estimated time remaining to complete simulation: 2 hours, 59 minutes, 40 seconds
  Estimated time remaining to next output: 14 seconds
Output 266/1000: t=26500.0 yr, dE/E0=5.39e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 1 seconds
  Estimated time remaining to next output: 14 seconds
Output 267/1000: t=26600.0 yr, dE/E0=7.55e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 22 seconds
  Estimated time remaining to next output: 14 seconds
Output 268/1000: t=26700.0 yr, dE/E0=4.02e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 18 seconds
  Estimated time remaining to next output: 14 seconds
Output 269/1000: t=26800.0 yr, dE/E0=1.85e-10, N=1001
  Estimated time remaining to complete simulation: 2 hours, 59 minutes, 44 seconds
  Estimated time remaining to next output: 14 seconds
Output 270/1000: t=26900.0 yr, dE/E0=3.63e-12, N=1001
  Estimated time remaining to complete simulation: 2 hours, 59 minutes, 4 seconds
  Estimated time remaining to next output: 14 seconds
Output 271/1000: t=27000.0 yr, dE/E0=3.72e-10, N=1001
  Estimated time remaining to complete simulation: 2 hours, 58 minutes, 25 seconds
  Estimated time remaining to next output: 14 seconds
Output 272/1000: t=27100.0 yr, dE/E0=4.42e-10, N=1001
  Estimated time remaining to complete simulation: 2 hours, 58 minutes, 36 seconds
  Estimated time remaining to next output: 14 seconds
Output 273/1000: t=27200.0 yr, dE/E0=5.94e-10, N=1001
  Estimated time remaining to complete simulation: 2 hours, 57 minutes, 53 seconds
  Estimated time remaining to next output: 14 seconds
Output 274/1000: t=27300.0 yr, dE/E0=3.33e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 26 minutes, 47 seconds
  Estimated time remaining to next output: 17 seconds
Output 275/1000: t=27400.0 yr, dE/E0=1.42e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 36 minutes, 16 seconds
  Estimated time remaining to next output: 17 seconds
Output 276/1000: t=27500.0 yr, dE/E0=1.37e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 49 minutes, 50 seconds
  Estimated time remaining to next output: 19 seconds
Output 277/1000: t=27600.0 yr, dE/E0=3.06e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 49 minutes, 18 seconds
  Estimated time remaining to next output: 19 seconds
Output 278/1000: t=27700.0 yr, dE/E0=2.87e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 56 minutes, 19 seconds
  Estimated time remaining to next output: 19 seconds
Output 279/1000: t=27800.0 yr, dE/E0=3.07e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 55 minutes, 31 seconds
  Estimated time remaining to next output: 19 seconds
Output 280/1000: t=27900.0 yr, dE/E0=2.29e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 55 minutes, 25 seconds
  Estimated time remaining to next output: 19 seconds
Output 281/1000: t=28000.0 yr, dE/E0=1.12e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 54 minutes, 34 seconds
  Estimated time remaining to next output: 19 seconds
Output 282/1000: t=28100.0 yr, dE/E0=2.84e-11, N=1001
  Estimated time remaining to complete simulation: 3 hours, 54 minutes, 2 seconds
  Estimated time remaining to next output: 19 seconds
Output 283/1000: t=28200.0 yr, dE/E0=2.57e-11, N=1001
  Estimated time remaining to complete simulation: 3 hours, 53 minutes, 17 seconds
  Estimated time remaining to next output: 19 seconds
Output 284/1000: t=28300.0 yr, dE/E0=9.72e-11, N=1001
  Estimated time remaining to complete simulation: 3 hours, 52 minutes, 27 seconds
  Estimated time remaining to next output: 19 seconds
Output 285/1000: t=28400.0 yr, dE/E0=2.38e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 52 minutes, 1 seconds
  Estimated time remaining to next output: 19 seconds
Output 286/1000: t=28500.0 yr, dE/E0=2.49e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 51 minutes, 7 seconds
  Estimated time remaining to next output: 19 seconds
Output 287/1000: t=28600.0 yr, dE/E0=3.49e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 50 minutes, 7 seconds
  Estimated time remaining to next output: 19 seconds
Output 288/1000: t=28700.0 yr, dE/E0=3.73e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 49 minutes, 43 seconds
  Estimated time remaining to next output: 19 seconds
Output 289/1000: t=28800.0 yr, dE/E0=4.02e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 48 minutes, 55 seconds
  Estimated time remaining to next output: 19 seconds
Output 290/1000: t=28900.0 yr, dE/E0=7.05e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 48 minutes
  Estimated time remaining to next output: 19 seconds
Output 291/1000: t=29000.0 yr, dE/E0=6.60e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 47 minutes, 13 seconds
  Estimated time remaining to next output: 19 seconds
Output 292/1000: t=29100.0 yr, dE/E0=6.46e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 46 minutes, 15 seconds
  Estimated time remaining to next output: 19 seconds
Output 293/1000: t=29200.0 yr, dE/E0=6.76e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 46 minutes, 8 seconds
  Estimated time remaining to next output: 19 seconds
Output 294/1000: t=29300.0 yr, dE/E0=1.04e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 45 minutes, 22 seconds
  Estimated time remaining to next output: 19 seconds
Output 295/1000: t=29400.0 yr, dE/E0=1.07e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 44 minutes, 25 seconds
  Estimated time remaining to next output: 19 seconds
Output 296/1000: t=29500.0 yr, dE/E0=7.66e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 43 minutes, 56 seconds
  Estimated time remaining to next output: 19 seconds
Output 297/1000: t=29600.0 yr, dE/E0=4.32e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 42 minutes, 59 seconds
  Estimated time remaining to next output: 19 seconds
Output 298/1000: t=29700.0 yr, dE/E0=2.82e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 42 minutes, 54 seconds
  Estimated time remaining to next output: 19 seconds
Output 299/1000: t=29800.0 yr, dE/E0=1.86e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 42 minutes, 6 seconds
  Estimated time remaining to next output: 19 seconds
Output 300/1000: t=29900.0 yr, dE/E0=2.32e-10, N=1001
  Estimated time remaining to complete simulation: 3 hours, 41 minutes, 44 seconds
  Estimated time remaining to next output: 19 seconds
Output 301/1000: t=30000.0 yr, dE/E0=6.68e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 45 minutes, 13 seconds
  Estimated time remaining to next output: 19 seconds
Output 302/1000: t=30100.0 yr, dE/E0=6.63e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 44 minutes, 18 seconds
  Estimated time remaining to next output: 19 seconds
Output 303/1000: t=30200.0 yr, dE/E0=6.69e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 43 minutes, 30 seconds
  Estimated time remaining to next output: 19 seconds
Output 304/1000: t=30300.0 yr, dE/E0=6.73e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 42 minutes, 51 seconds
  Estimated time remaining to next output: 19 seconds
Output 305/1000: t=30400.0 yr, dE/E0=6.68e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 42 minutes, 3 seconds
  Estimated time remaining to next output: 19 seconds
Output 306/1000: t=30500.0 yr, dE/E0=6.53e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 41 minutes, 14 seconds
  Estimated time remaining to next output: 19 seconds
Output 307/1000: t=30600.0 yr, dE/E0=6.22e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 40 minutes, 26 seconds
  Estimated time remaining to next output: 19 seconds
Output 308/1000: t=30700.0 yr, dE/E0=6.34e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 40 minutes, 12 seconds
  Estimated time remaining to next output: 19 seconds
Output 309/1000: t=30800.0 yr, dE/E0=6.55e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 39 minutes, 30 seconds
  Estimated time remaining to next output: 19 seconds
Output 310/1000: t=30900.0 yr, dE/E0=6.80e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 38 minutes, 44 seconds
  Estimated time remaining to next output: 19 seconds
Output 311/1000: t=31000.0 yr, dE/E0=6.88e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 37 minutes, 54 seconds
  Estimated time remaining to next output: 18 seconds
Output 312/1000: t=31100.0 yr, dE/E0=6.99e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 36 minutes, 59 seconds
  Estimated time remaining to next output: 18 seconds
Output 313/1000: t=31200.0 yr, dE/E0=7.06e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 37 minutes
  Estimated time remaining to next output: 18 seconds
Output 314/1000: t=31300.0 yr, dE/E0=7.01e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 36 minutes, 16 seconds
  Estimated time remaining to next output: 18 seconds
Output 315/1000: t=31400.0 yr, dE/E0=6.90e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 35 minutes, 28 seconds
  Estimated time remaining to next output: 18 seconds
Output 316/1000: t=31500.0 yr, dE/E0=6.89e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 34 minutes, 49 seconds
  Estimated time remaining to next output: 18 seconds
Output 317/1000: t=31600.0 yr, dE/E0=6.80e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 34 minutes, 45 seconds
  Estimated time remaining to next output: 18 seconds
Output 318/1000: t=31700.0 yr, dE/E0=6.63e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 34 minutes, 7 seconds
  Estimated time remaining to next output: 18 seconds
Output 319/1000: t=31800.0 yr, dE/E0=6.59e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 33 minutes, 38 seconds
  Estimated time remaining to next output: 18 seconds
Output 320/1000: t=31900.0 yr, dE/E0=6.75e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 32 minutes, 49 seconds
  Estimated time remaining to next output: 18 seconds
Output 321/1000: t=32000.0 yr, dE/E0=6.48e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 32 minutes, 4 seconds
  Estimated time remaining to next output: 18 seconds
Output 322/1000: t=32100.0 yr, dE/E0=6.55e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 31 minutes, 11 seconds
  Estimated time remaining to next output: 18 seconds
Output 323/1000: t=32200.0 yr, dE/E0=6.82e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 30 minutes, 28 seconds
  Estimated time remaining to next output: 18 seconds
Output 324/1000: t=32300.0 yr, dE/E0=6.79e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 29 minutes, 45 seconds
  Estimated time remaining to next output: 18 seconds
Output 325/1000: t=32400.0 yr, dE/E0=6.85e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 29 minutes, 11 seconds
  Estimated time remaining to next output: 18 seconds
Output 326/1000: t=32500.0 yr, dE/E0=6.78e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 28 minutes, 47 seconds
  Estimated time remaining to next output: 18 seconds
Output 327/1000: t=32600.0 yr, dE/E0=6.47e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 28 minutes, 25 seconds
  Estimated time remaining to next output: 18 seconds
Output 328/1000: t=32700.0 yr, dE/E0=6.56e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 27 minutes, 46 seconds
  Estimated time remaining to next output: 18 seconds
Output 329/1000: t=32800.0 yr, dE/E0=6.42e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 27 minutes, 8 seconds
  Estimated time remaining to next output: 18 seconds
Output 330/1000: t=32900.0 yr, dE/E0=6.81e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 26 minutes, 18 seconds
  Estimated time remaining to next output: 18 seconds
Output 331/1000: t=33000.0 yr, dE/E0=6.77e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 25 minutes, 36 seconds
  Estimated time remaining to next output: 18 seconds
Output 332/1000: t=33100.0 yr, dE/E0=6.84e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 25 minutes, 24 seconds
  Estimated time remaining to next output: 18 seconds
Output 333/1000: t=33200.0 yr, dE/E0=6.74e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 24 minutes, 45 seconds
  Estimated time remaining to next output: 18 seconds
Output 334/1000: t=33300.0 yr, dE/E0=6.69e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 24 minutes, 31 seconds
  Estimated time remaining to next output: 18 seconds
Output 335/1000: t=33400.0 yr, dE/E0=6.72e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 24 minutes, 27 seconds
  Estimated time remaining to next output: 18 seconds
Output 336/1000: t=33500.0 yr, dE/E0=6.85e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 24 minutes, 11 seconds
  Estimated time remaining to next output: 18 seconds
Output 337/1000: t=33600.0 yr, dE/E0=6.82e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 23 minutes, 36 seconds
  Estimated time remaining to next output: 18 seconds
Output 338/1000: t=33700.0 yr, dE/E0=6.55e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 23 minutes, 31 seconds
  Estimated time remaining to next output: 18 seconds
Output 339/1000: t=33800.0 yr, dE/E0=6.39e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 23 minutes, 6 seconds
  Estimated time remaining to next output: 18 seconds
Output 340/1000: t=33900.0 yr, dE/E0=6.43e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 22 minutes, 37 seconds
  Estimated time remaining to next output: 18 seconds
Output 341/1000: t=34000.0 yr, dE/E0=6.71e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 21 minutes, 56 seconds
  Estimated time remaining to next output: 18 seconds
Output 342/1000: t=34100.0 yr, dE/E0=6.74e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 21 minutes, 18 seconds
  Estimated time remaining to next output: 18 seconds
Output 343/1000: t=34200.0 yr, dE/E0=6.71e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 21 minutes, 25 seconds
  Estimated time remaining to next output: 18 seconds
Output 344/1000: t=34300.0 yr, dE/E0=6.87e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 20 minutes, 55 seconds
  Estimated time remaining to next output: 18 seconds
Output 345/1000: t=34400.0 yr, dE/E0=7.04e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 20 minutes, 8 seconds
  Estimated time remaining to next output: 18 seconds
Output 346/1000: t=34500.0 yr, dE/E0=6.93e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 19 minutes, 42 seconds
  Estimated time remaining to next output: 18 seconds
Output 347/1000: t=34600.0 yr, dE/E0=6.63e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 18 minutes, 58 seconds
  Estimated time remaining to next output: 18 seconds
Output 348/1000: t=34700.0 yr, dE/E0=6.57e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 18 minutes, 15 seconds
  Estimated time remaining to next output: 18 seconds
Output 349/1000: t=34800.0 yr, dE/E0=6.63e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 17 minutes, 32 seconds
  Estimated time remaining to next output: 18 seconds
Output 350/1000: t=34900.0 yr, dE/E0=6.85e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 16 minutes, 45 seconds
  Estimated time remaining to next output: 18 seconds
Output 351/1000: t=35000.0 yr, dE/E0=6.92e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 16 minutes, 5 seconds
  Estimated time remaining to next output: 18 seconds
Output 352/1000: t=35100.0 yr, dE/E0=6.79e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 15 minutes, 25 seconds
  Estimated time remaining to next output: 18 seconds
Output 353/1000: t=35200.0 yr, dE/E0=6.78e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 14 minutes, 52 seconds
  Estimated time remaining to next output: 18 seconds
Output 354/1000: t=35300.0 yr, dE/E0=6.98e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 14 minutes, 50 seconds
  Estimated time remaining to next output: 18 seconds
Output 355/1000: t=35400.0 yr, dE/E0=7.33e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 14 minutes, 35 seconds
  Estimated time remaining to next output: 18 seconds
Output 356/1000: t=35500.0 yr, dE/E0=6.80e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 13 minutes, 57 seconds
  Estimated time remaining to next output: 18 seconds
Output 357/1000: t=35600.0 yr, dE/E0=6.05e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 13 minutes, 18 seconds
  Estimated time remaining to next output: 18 seconds
Output 358/1000: t=35700.0 yr, dE/E0=5.83e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 12 minutes, 35 seconds
  Estimated time remaining to next output: 17 seconds
Output 359/1000: t=35800.0 yr, dE/E0=5.98e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 11 minutes, 52 seconds
  Estimated time remaining to next output: 17 seconds
Output 360/1000: t=35900.0 yr, dE/E0=6.57e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 11 minutes, 8 seconds
  Estimated time remaining to next output: 17 seconds
Output 361/1000: t=36000.0 yr, dE/E0=6.96e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 11 minutes, 13 seconds
  Estimated time remaining to next output: 17 seconds
Output 362/1000: t=36100.0 yr, dE/E0=6.98e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 10 minutes, 35 seconds
  Estimated time remaining to next output: 17 seconds
Output 363/1000: t=36200.0 yr, dE/E0=6.82e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 9 minutes, 57 seconds
  Estimated time remaining to next output: 17 seconds
Output 364/1000: t=36300.0 yr, dE/E0=6.75e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 9 minutes, 17 seconds
  Estimated time remaining to next output: 17 seconds
Output 365/1000: t=36400.0 yr, dE/E0=6.84e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 8 minutes, 39 seconds
  Estimated time remaining to next output: 17 seconds
Output 366/1000: t=36500.0 yr, dE/E0=6.92e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 8 minutes, 4 seconds
  Estimated time remaining to next output: 17 seconds
Output 367/1000: t=36600.0 yr, dE/E0=6.96e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 7 minutes, 34 seconds
  Estimated time remaining to next output: 17 seconds
Output 368/1000: t=36700.0 yr, dE/E0=6.93e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 7 minutes, 28 seconds
  Estimated time remaining to next output: 17 seconds
Output 369/1000: t=36800.0 yr, dE/E0=6.76e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 7 minutes, 2 seconds
  Estimated time remaining to next output: 17 seconds
Output 370/1000: t=36900.0 yr, dE/E0=6.70e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 6 minutes, 19 seconds
  Estimated time remaining to next output: 17 seconds
Output 371/1000: t=37000.0 yr, dE/E0=6.83e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 5 minutes, 44 seconds
  Estimated time remaining to next output: 17 seconds
Output 372/1000: t=37100.0 yr, dE/E0=6.84e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 5 minutes, 8 seconds
  Estimated time remaining to next output: 17 seconds
Output 373/1000: t=37200.0 yr, dE/E0=6.65e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 4 minutes, 45 seconds
  Estimated time remaining to next output: 17 seconds
Output 374/1000: t=37300.0 yr, dE/E0=6.63e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 4 minutes, 11 seconds
  Estimated time remaining to next output: 17 seconds
Output 375/1000: t=37400.0 yr, dE/E0=6.61e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 3 minutes, 41 seconds
  Estimated time remaining to next output: 17 seconds
Output 376/1000: t=37500.0 yr, dE/E0=6.80e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 3 minutes, 49 seconds
  Estimated time remaining to next output: 17 seconds
Output 377/1000: t=37600.0 yr, dE/E0=6.86e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 3 minutes, 13 seconds
  Estimated time remaining to next output: 17 seconds
Output 378/1000: t=37700.0 yr, dE/E0=6.95e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 2 minutes, 31 seconds
  Estimated time remaining to next output: 17 seconds
Output 379/1000: t=37800.0 yr, dE/E0=6.93e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 2 minutes
  Estimated time remaining to next output: 17 seconds
Output 380/1000: t=37900.0 yr, dE/E0=6.84e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 1 minutes, 19 seconds
  Estimated time remaining to next output: 17 seconds
Output 381/1000: t=38000.0 yr, dE/E0=6.87e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 1 minutes, 1 seconds
  Estimated time remaining to next output: 17 seconds
Output 382/1000: t=38100.0 yr, dE/E0=7.14e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 1 minutes, 37 seconds
  Estimated time remaining to next output: 17 seconds
Output 383/1000: t=38200.0 yr, dE/E0=7.07e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 1 minutes, 13 seconds
  Estimated time remaining to next output: 17 seconds
Output 384/1000: t=38300.0 yr, dE/E0=6.56e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 39 seconds
  Estimated time remaining to next output: 17 seconds
Output 385/1000: t=38400.0 yr, dE/E0=6.23e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 12 seconds
  Estimated time remaining to next output: 17 seconds
Output 386/1000: t=38500.0 yr, dE/E0=6.45e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 59 minutes, 39 seconds
  Estimated time remaining to next output: 17 seconds
Output 387/1000: t=38600.0 yr, dE/E0=6.54e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 59 minutes, 2 seconds
  Estimated time remaining to next output: 17 seconds
Output 388/1000: t=38700.0 yr, dE/E0=6.15e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 58 minutes, 22 seconds
  Estimated time remaining to next output: 17 seconds
Output 389/1000: t=38800.0 yr, dE/E0=6.37e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 57 minutes, 50 seconds
  Estimated time remaining to next output: 17 seconds
Output 390/1000: t=38900.0 yr, dE/E0=6.74e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 57 minutes, 12 seconds
  Estimated time remaining to next output: 17 seconds
Output 391/1000: t=39000.0 yr, dE/E0=7.10e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 56 minutes, 41 seconds
  Estimated time remaining to next output: 17 seconds
Output 392/1000: t=39100.0 yr, dE/E0=7.10e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 56 minutes, 5 seconds
  Estimated time remaining to next output: 17 seconds
Output 393/1000: t=39200.0 yr, dE/E0=7.00e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 55 minutes, 26 seconds
  Estimated time remaining to next output: 17 seconds
Output 394/1000: t=39300.0 yr, dE/E0=6.91e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 54 minutes, 55 seconds
  Estimated time remaining to next output: 17 seconds
Output 395/1000: t=39400.0 yr, dE/E0=6.91e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 54 minutes, 16 seconds
  Estimated time remaining to next output: 17 seconds
Output 396/1000: t=39500.0 yr, dE/E0=6.87e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 54 minutes, 15 seconds
  Estimated time remaining to next output: 17 seconds
Output 397/1000: t=39600.0 yr, dE/E0=6.91e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 53 minutes, 59 seconds
  Estimated time remaining to next output: 17 seconds
Output 398/1000: t=39700.0 yr, dE/E0=6.92e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 53 minutes, 25 seconds
  Estimated time remaining to next output: 17 seconds
Output 399/1000: t=39800.0 yr, dE/E0=6.86e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 52 minutes, 57 seconds
  Estimated time remaining to next output: 17 seconds
Output 400/1000: t=39900.0 yr, dE/E0=6.73e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 52 minutes, 18 seconds
  Estimated time remaining to next output: 17 seconds
Output 401/1000: t=40000.0 yr, dE/E0=6.75e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 51 minutes, 44 seconds
  Estimated time remaining to next output: 17 seconds
Output 402/1000: t=40100.0 yr, dE/E0=6.56e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 51 minutes, 9 seconds
  Estimated time remaining to next output: 17 seconds
Output 403/1000: t=40200.0 yr, dE/E0=6.45e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 50 minutes, 38 seconds
  Estimated time remaining to next output: 17 seconds
Output 404/1000: t=40300.0 yr, dE/E0=6.66e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 50 minutes, 6 seconds
  Estimated time remaining to next output: 17 seconds
Output 405/1000: t=40400.0 yr, dE/E0=6.80e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 49 minutes, 33 seconds
  Estimated time remaining to next output: 17 seconds
Output 406/1000: t=40500.0 yr, dE/E0=7.11e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 48 minutes, 57 seconds
  Estimated time remaining to next output: 17 seconds
Output 407/1000: t=40600.0 yr, dE/E0=7.23e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 48 minutes, 22 seconds
  Estimated time remaining to next output: 17 seconds
Output 408/1000: t=40700.0 yr, dE/E0=7.13e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 47 minutes, 44 seconds
  Estimated time remaining to next output: 17 seconds
Output 409/1000: t=40800.0 yr, dE/E0=6.53e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 47 minutes, 27 seconds
  Estimated time remaining to next output: 17 seconds
Output 410/1000: t=40900.0 yr, dE/E0=6.08e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 47 minutes, 11 seconds
  Estimated time remaining to next output: 17 seconds
Output 411/1000: t=41000.0 yr, dE/E0=6.15e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 46 minutes, 46 seconds
  Estimated time remaining to next output: 16 seconds
Output 412/1000: t=41100.0 yr, dE/E0=6.76e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 46 minutes, 12 seconds
  Estimated time remaining to next output: 16 seconds
Output 413/1000: t=41200.0 yr, dE/E0=7.02e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 45 minutes, 38 seconds
  Estimated time remaining to next output: 16 seconds
Output 414/1000: t=41300.0 yr, dE/E0=6.99e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 45 minutes, 11 seconds
  Estimated time remaining to next output: 16 seconds
Output 415/1000: t=41400.0 yr, dE/E0=6.88e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 44 minutes, 39 seconds
  Estimated time remaining to next output: 16 seconds
Output 416/1000: t=41500.0 yr, dE/E0=6.69e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 44 minutes, 16 seconds
  Estimated time remaining to next output: 16 seconds
Output 417/1000: t=41600.0 yr, dE/E0=6.66e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 43 minutes, 43 seconds
  Estimated time remaining to next output: 16 seconds
Output 418/1000: t=41700.0 yr, dE/E0=6.82e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 43 minutes, 32 seconds
  Estimated time remaining to next output: 16 seconds
Output 419/1000: t=41800.0 yr, dE/E0=6.87e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 43 minutes, 8 seconds
  Estimated time remaining to next output: 16 seconds
Output 420/1000: t=41900.0 yr, dE/E0=6.98e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 43 minutes, 2 seconds
  Estimated time remaining to next output: 16 seconds
Output 421/1000: t=42000.0 yr, dE/E0=7.02e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 42 minutes, 54 seconds
  Estimated time remaining to next output: 16 seconds
Output 422/1000: t=42100.0 yr, dE/E0=6.93e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 42 minutes, 22 seconds
  Estimated time remaining to next output: 16 seconds
Output 423/1000: t=42200.0 yr, dE/E0=6.86e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 41 minutes, 53 seconds
  Estimated time remaining to next output: 16 seconds
Output 424/1000: t=42300.0 yr, dE/E0=6.94e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 41 minutes, 24 seconds
  Estimated time remaining to next output: 16 seconds
Output 425/1000: t=42400.0 yr, dE/E0=6.93e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 40 minutes, 54 seconds
  Estimated time remaining to next output: 16 seconds
Output 426/1000: t=42500.0 yr, dE/E0=6.85e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 40 minutes, 44 seconds
  Estimated time remaining to next output: 16 seconds
Output 427/1000: t=42600.0 yr, dE/E0=6.64e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 40 minutes, 12 seconds
  Estimated time remaining to next output: 16 seconds
Output 428/1000: t=42700.0 yr, dE/E0=6.40e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 40 minutes, 32 seconds
  Estimated time remaining to next output: 16 seconds
Output 429/1000: t=42800.0 yr, dE/E0=6.58e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 40 minutes, 5 seconds
  Estimated time remaining to next output: 16 seconds
Output 430/1000: t=42900.0 yr, dE/E0=6.19e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 39 minutes, 34 seconds
  Estimated time remaining to next output: 16 seconds
Output 431/1000: t=43000.0 yr, dE/E0=6.13e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 39 minutes
  Estimated time remaining to next output: 16 seconds
Output 432/1000: t=43100.0 yr, dE/E0=6.28e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 38 minutes, 28 seconds
  Estimated time remaining to next output: 16 seconds
Output 433/1000: t=43200.0 yr, dE/E0=6.33e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 37 minutes, 54 seconds
  Estimated time remaining to next output: 16 seconds
Output 434/1000: t=43300.0 yr, dE/E0=6.63e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 37 minutes, 34 seconds
  Estimated time remaining to next output: 16 seconds
Output 435/1000: t=43400.0 yr, dE/E0=6.89e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 37 minutes, 11 seconds
  Estimated time remaining to next output: 16 seconds
Output 436/1000: t=43500.0 yr, dE/E0=6.95e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 36 minutes, 54 seconds
  Estimated time remaining to next output: 16 seconds
Output 437/1000: t=43600.0 yr, dE/E0=6.83e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 37 minutes
  Estimated time remaining to next output: 16 seconds
Output 438/1000: t=43700.0 yr, dE/E0=6.78e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 36 minutes, 26 seconds
  Estimated time remaining to next output: 16 seconds
Output 439/1000: t=43800.0 yr, dE/E0=6.81e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 35 minutes, 58 seconds
  Estimated time remaining to next output: 16 seconds
Output 440/1000: t=43900.0 yr, dE/E0=6.88e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 36 minutes, 3 seconds
  Estimated time remaining to next output: 16 seconds
Output 441/1000: t=44000.0 yr, dE/E0=6.95e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 35 minutes, 31 seconds
  Estimated time remaining to next output: 16 seconds
Output 442/1000: t=44100.0 yr, dE/E0=7.02e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 35 minutes
  Estimated time remaining to next output: 16 seconds
Output 443/1000: t=44200.0 yr, dE/E0=7.06e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 34 minutes, 26 seconds
  Estimated time remaining to next output: 16 seconds
Output 444/1000: t=44300.0 yr, dE/E0=7.13e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 34 minutes, 1 seconds
  Estimated time remaining to next output: 16 seconds
Output 445/1000: t=44400.0 yr, dE/E0=6.84e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 33 minutes, 44 seconds
  Estimated time remaining to next output: 16 seconds
Output 446/1000: t=44500.0 yr, dE/E0=6.21e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 33 minutes, 21 seconds
  Estimated time remaining to next output: 16 seconds
Output 447/1000: t=44600.0 yr, dE/E0=6.11e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 32 minutes, 52 seconds
  Estimated time remaining to next output: 16 seconds
Output 448/1000: t=44700.0 yr, dE/E0=5.87e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 32 minutes, 19 seconds
  Estimated time remaining to next output: 16 seconds
Output 449/1000: t=44800.0 yr, dE/E0=6.58e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 31 minutes, 51 seconds
  Estimated time remaining to next output: 16 seconds
Output 450/1000: t=44900.0 yr, dE/E0=6.94e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 31 minutes, 22 seconds
  Estimated time remaining to next output: 16 seconds
Output 451/1000: t=45000.0 yr, dE/E0=6.85e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 31 minutes, 2 seconds
  Estimated time remaining to next output: 16 seconds
Output 452/1000: t=45100.0 yr, dE/E0=7.12e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 30 minutes, 33 seconds
  Estimated time remaining to next output: 16 seconds
Output 453/1000: t=45200.0 yr, dE/E0=6.86e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 30 minutes, 2 seconds
  Estimated time remaining to next output: 16 seconds
Output 454/1000: t=45300.0 yr, dE/E0=6.65e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 30 minutes, 10 seconds
  Estimated time remaining to next output: 16 seconds
Output 455/1000: t=45400.0 yr, dE/E0=6.62e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 29 minutes, 40 seconds
  Estimated time remaining to next output: 16 seconds
Output 456/1000: t=45500.0 yr, dE/E0=6.69e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 29 minutes, 11 seconds
  Estimated time remaining to next output: 16 seconds
Output 457/1000: t=45600.0 yr, dE/E0=6.19e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 28 minutes, 47 seconds
  Estimated time remaining to next output: 16 seconds
Output 458/1000: t=45700.0 yr, dE/E0=6.41e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 28 minutes, 20 seconds
  Estimated time remaining to next output: 16 seconds
Output 459/1000: t=45800.0 yr, dE/E0=6.81e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 27 minutes, 48 seconds
  Estimated time remaining to next output: 16 seconds
Output 460/1000: t=45900.0 yr, dE/E0=7.11e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 27 minutes, 31 seconds
  Estimated time remaining to next output: 16 seconds
Output 461/1000: t=46000.0 yr, dE/E0=6.98e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 27 minutes
  Estimated time remaining to next output: 16 seconds
Output 462/1000: t=46100.0 yr, dE/E0=6.74e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 26 minutes, 34 seconds
  Estimated time remaining to next output: 16 seconds
Output 463/1000: t=46200.0 yr, dE/E0=6.72e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 26 minutes, 39 seconds
  Estimated time remaining to next output: 16 seconds
Output 464/1000: t=46300.0 yr, dE/E0=6.62e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 26 minutes, 20 seconds
  Estimated time remaining to next output: 16 seconds
Output 465/1000: t=46400.0 yr, dE/E0=6.66e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 25 minutes, 51 seconds
  Estimated time remaining to next output: 16 seconds
Output 466/1000: t=46500.0 yr, dE/E0=6.66e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 25 minutes, 21 seconds
  Estimated time remaining to next output: 16 seconds
Output 467/1000: t=46600.0 yr, dE/E0=6.63e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 24 minutes, 57 seconds
  Estimated time remaining to next output: 16 seconds
Output 468/1000: t=46700.0 yr, dE/E0=6.58e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 24 minutes, 45 seconds
  Estimated time remaining to next output: 16 seconds
Output 469/1000: t=46800.0 yr, dE/E0=6.71e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 24 minutes, 22 seconds
  Estimated time remaining to next output: 16 seconds
Output 470/1000: t=46900.0 yr, dE/E0=6.81e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 23 minutes, 55 seconds
  Estimated time remaining to next output: 16 seconds
Output 471/1000: t=47000.0 yr, dE/E0=6.87e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 23 minutes, 25 seconds
  Estimated time remaining to next output: 16 seconds
Output 472/1000: t=47100.0 yr, dE/E0=6.68e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 23 minutes, 4 seconds
  Estimated time remaining to next output: 16 seconds
Output 473/1000: t=47200.0 yr, dE/E0=6.64e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 22 minutes, 38 seconds
  Estimated time remaining to next output: 16 seconds
Output 474/1000: t=47300.0 yr, dE/E0=6.66e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 22 minutes, 9 seconds
  Estimated time remaining to next output: 16 seconds
Output 475/1000: t=47400.0 yr, dE/E0=6.71e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 21 minutes, 40 seconds
  Estimated time remaining to next output: 16 seconds
Output 476/1000: t=47500.0 yr, dE/E0=6.77e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 21 minutes, 51 seconds
  Estimated time remaining to next output: 16 seconds
Output 477/1000: t=47600.0 yr, dE/E0=6.78e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 21 minutes, 26 seconds
  Estimated time remaining to next output: 16 seconds
Output 478/1000: t=47700.0 yr, dE/E0=6.76e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 21 minutes
  Estimated time remaining to next output: 16 seconds
Output 479/1000: t=47800.0 yr, dE/E0=6.86e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 20 minutes, 31 seconds
  Estimated time remaining to next output: 16 seconds
Output 480/1000: t=47900.0 yr, dE/E0=6.84e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 20 minutes, 4 seconds
  Estimated time remaining to next output: 16 seconds
Output 481/1000: t=48000.0 yr, dE/E0=6.75e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 19 minutes, 46 seconds
  Estimated time remaining to next output: 16 seconds
Output 482/1000: t=48100.0 yr, dE/E0=5.74e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 22 minutes, 30 seconds
  Estimated time remaining to next output: 16 seconds
Output 483/1000: t=48200.0 yr, dE/E0=5.76e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 24 minutes, 51 seconds
  Estimated time remaining to next output: 16 seconds
Output 484/1000: t=48300.0 yr, dE/E0=5.45e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 27 minutes, 11 seconds
  Estimated time remaining to next output: 17 seconds
Output 485/1000: t=48400.0 yr, dE/E0=5.27e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 29 minutes, 50 seconds
  Estimated time remaining to next output: 17 seconds
Output 486/1000: t=48500.0 yr, dE/E0=5.41e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 31 minutes, 37 seconds
  Estimated time remaining to next output: 17 seconds
Output 487/1000: t=48600.0 yr, dE/E0=5.49e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 35 minutes, 56 seconds
  Estimated time remaining to next output: 18 seconds
Output 488/1000: t=48700.0 yr, dE/E0=5.64e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 38 minutes, 19 seconds
  Estimated time remaining to next output: 18 seconds
Output 489/1000: t=48800.0 yr, dE/E0=5.98e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 40 minutes, 11 seconds
  Estimated time remaining to next output: 18 seconds
Output 490/1000: t=48900.0 yr, dE/E0=5.86e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 44 minutes, 2 seconds
  Estimated time remaining to next output: 19 seconds
Output 491/1000: t=49000.0 yr, dE/E0=5.69e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 46 minutes, 21 seconds
  Estimated time remaining to next output: 19 seconds
Output 492/1000: t=49100.0 yr, dE/E0=6.23e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 49 minutes, 18 seconds
  Estimated time remaining to next output: 19 seconds
Output 493/1000: t=49200.0 yr, dE/E0=6.32e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 51 minutes, 11 seconds
  Estimated time remaining to next output: 20 seconds
Output 494/1000: t=49300.0 yr, dE/E0=6.48e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 53 minutes, 11 seconds
  Estimated time remaining to next output: 20 seconds
Output 495/1000: t=49400.0 yr, dE/E0=6.58e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 55 minutes, 56 seconds
  Estimated time remaining to next output: 20 seconds
Output 496/1000: t=49500.0 yr, dE/E0=6.46e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 57 minutes, 43 seconds
  Estimated time remaining to next output: 21 seconds
Output 497/1000: t=49600.0 yr, dE/E0=6.46e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 6 seconds
  Estimated time remaining to next output: 21 seconds
Output 498/1000: t=49700.0 yr, dE/E0=6.49e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 2 minutes, 13 seconds
  Estimated time remaining to next output: 21 seconds
Output 499/1000: t=49800.0 yr, dE/E0=6.52e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 4 minutes, 35 seconds
  Estimated time remaining to next output: 22 seconds
Output 500/1000: t=49900.0 yr, dE/E0=6.64e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 7 minutes, 11 seconds
  Estimated time remaining to next output: 22 seconds
Output 501/1000: t=50000.0 yr, dE/E0=6.70e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 9 minutes, 15 seconds
  Estimated time remaining to next output: 22 seconds
Output 502/1000: t=50100.0 yr, dE/E0=6.58e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 11 minutes, 21 seconds
  Estimated time remaining to next output: 23 seconds
Output 503/1000: t=50200.0 yr, dE/E0=7.05e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 14 minutes, 47 seconds
  Estimated time remaining to next output: 23 seconds
Output 504/1000: t=50300.0 yr, dE/E0=6.94e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 16 minutes, 8 seconds
  Estimated time remaining to next output: 23 seconds
Output 505/1000: t=50400.0 yr, dE/E0=6.98e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 18 minutes, 55 seconds
  Estimated time remaining to next output: 24 seconds
Output 506/1000: t=50500.0 yr, dE/E0=7.07e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 20 minutes, 51 seconds
  Estimated time remaining to next output: 24 seconds
Output 507/1000: t=50600.0 yr, dE/E0=7.25e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 22 minutes, 49 seconds
  Estimated time remaining to next output: 24 seconds
Output 508/1000: t=50700.0 yr, dE/E0=7.32e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 26 minutes, 8 seconds
  Estimated time remaining to next output: 25 seconds
Output 509/1000: t=50800.0 yr, dE/E0=7.20e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 27 minutes, 44 seconds
  Estimated time remaining to next output: 25 seconds
Output 510/1000: t=50900.0 yr, dE/E0=7.12e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 29 minutes, 40 seconds
  Estimated time remaining to next output: 25 seconds
Output 511/1000: t=51000.0 yr, dE/E0=7.05e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 32 minutes, 46 seconds
  Estimated time remaining to next output: 26 seconds
Output 512/1000: t=51100.0 yr, dE/E0=7.00e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 34 minutes, 45 seconds
  Estimated time remaining to next output: 26 seconds
Output 513/1000: t=51200.0 yr, dE/E0=5.66e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 37 minutes, 21 seconds
  Estimated time remaining to next output: 26 seconds
Output 514/1000: t=51300.0 yr, dE/E0=5.85e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 36 minutes, 32 seconds
  Estimated time remaining to next output: 26 seconds
Output 515/1000: t=51400.0 yr, dE/E0=5.91e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 35 minutes, 47 seconds
  Estimated time remaining to next output: 26 seconds
Output 516/1000: t=51500.0 yr, dE/E0=5.59e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 35 minutes, 16 seconds
  Estimated time remaining to next output: 26 seconds
Output 517/1000: t=51600.0 yr, dE/E0=4.95e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 34 minutes, 37 seconds
  Estimated time remaining to next output: 26 seconds
Output 518/1000: t=51700.0 yr, dE/E0=4.80e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 34 minutes, 28 seconds
  Estimated time remaining to next output: 26 seconds
Output 519/1000: t=51800.0 yr, dE/E0=4.85e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 36 minutes, 22 seconds
  Estimated time remaining to next output: 26 seconds
Output 520/1000: t=51900.0 yr, dE/E0=4.52e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 38 minutes, 17 seconds
  Estimated time remaining to next output: 27 seconds
Output 521/1000: t=52000.0 yr, dE/E0=4.70e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 39 minutes, 59 seconds
  Estimated time remaining to next output: 27 seconds
Output 522/1000: t=52100.0 yr, dE/E0=5.21e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 41 minutes, 54 seconds
  Estimated time remaining to next output: 27 seconds
Output 523/1000: t=52200.0 yr, dE/E0=5.39e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 43 minutes, 32 seconds
  Estimated time remaining to next output: 28 seconds
Output 524/1000: t=52300.0 yr, dE/E0=5.24e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 44 minutes, 41 seconds
  Estimated time remaining to next output: 28 seconds
Output 525/1000: t=52400.0 yr, dE/E0=5.27e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 45 minutes, 59 seconds
  Estimated time remaining to next output: 28 seconds
Output 526/1000: t=52500.0 yr, dE/E0=5.40e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 47 minutes, 9 seconds
  Estimated time remaining to next output: 28 seconds
Output 527/1000: t=52600.0 yr, dE/E0=5.50e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 48 minutes, 6 seconds
  Estimated time remaining to next output: 28 seconds
Output 528/1000: t=52700.0 yr, dE/E0=5.57e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 49 minutes, 23 seconds
  Estimated time remaining to next output: 29 seconds
Output 529/1000: t=52800.0 yr, dE/E0=5.64e-09, N=1001
  Estimated time remaining to complete simulation: 4 hours, 14 minutes, 27 seconds
  Estimated time remaining to next output: 32 seconds
Output 530/1000: t=52900.0 yr, dE/E0=5.67e-09, N=1001
  Estimated time remaining to complete simulation: 4 hours, 36 minutes, 39 seconds
  Estimated time remaining to next output: 35 seconds
Output 531/1000: t=53000.0 yr, dE/E0=5.56e-09, N=1001
  Estimated time remaining to complete simulation: 5 hours, 1 minutes, 43 seconds
  Estimated time remaining to next output: 38 seconds
Output 532/1000: t=53100.0 yr, dE/E0=5.53e-09, N=1001
  Estimated time remaining to complete simulation: 5 hours, 4 minutes, 9 seconds
  Estimated time remaining to next output: 38 seconds
Output 533/1000: t=53200.0 yr, dE/E0=5.76e-09, N=1001
  Estimated time remaining to complete simulation: 5 hours, 6 minutes, 11 seconds
  Estimated time remaining to next output: 39 seconds
Output 534/1000: t=53300.0 yr, dE/E0=5.18e-09, N=1001
  Estimated time remaining to complete simulation: 5 hours, 7 minutes, 56 seconds
  Estimated time remaining to next output: 39 seconds
Output 535/1000: t=53400.0 yr, dE/E0=4.61e-09, N=1001
  Estimated time remaining to complete simulation: 5 hours, 9 minutes, 48 seconds
  Estimated time remaining to next output: 39 seconds
Output 536/1000: t=53500.0 yr, dE/E0=4.77e-09, N=1001
  Estimated time remaining to complete simulation: 5 hours, 11 minutes, 42 seconds
  Estimated time remaining to next output: 40 seconds
Output 537/1000: t=53600.0 yr, dE/E0=5.16e-09, N=1001
  Estimated time remaining to complete simulation: 5 hours, 25 minutes, 4 seconds
  Estimated time remaining to next output: 42 seconds
Output 538/1000: t=53700.0 yr, dE/E0=5.74e-09, N=1001
  Estimated time remaining to complete simulation: 5 hours, 43 minutes, 58 seconds
  Estimated time remaining to next output: 44 seconds
Output 539/1000: t=53800.0 yr, dE/E0=5.82e-09, N=1001
  Estimated time remaining to complete simulation: 5 hours, 49 minutes, 7 seconds
  Estimated time remaining to next output: 45 seconds
Output 540/1000: t=53900.0 yr, dE/E0=5.42e-09, N=1001
  Estimated time remaining to complete simulation: 5 hours, 51 minutes, 4 seconds
  Estimated time remaining to next output: 45 seconds
Output 541/1000: t=54000.0 yr, dE/E0=4.92e-09, N=1001
  Estimated time remaining to complete simulation: 5 hours, 53 minutes, 13 seconds
  Estimated time remaining to next output: 46 seconds
Output 542/1000: t=54100.0 yr, dE/E0=5.01e-09, N=1001
  Estimated time remaining to complete simulation: 5 hours, 54 minutes, 52 seconds
  Estimated time remaining to next output: 46 seconds
Output 543/1000: t=54200.0 yr, dE/E0=4.85e-09, N=1001
  Estimated time remaining to complete simulation: 5 hours, 55 minutes, 51 seconds
  Estimated time remaining to next output: 46 seconds
Output 544/1000: t=54300.0 yr, dE/E0=5.34e-09, N=1001
  Estimated time remaining to complete simulation: 5 hours, 56 minutes, 52 seconds
  Estimated time remaining to next output: 46 seconds
Output 545/1000: t=54400.0 yr, dE/E0=5.82e-09, N=1001
  Estimated time remaining to complete simulation: 5 hours, 58 minutes, 50 seconds
  Estimated time remaining to next output: 47 seconds
Output 546/1000: t=54500.0 yr, dE/E0=5.82e-09, N=1001
  Estimated time remaining to complete simulation: 6 hours, 34 seconds
  Estimated time remaining to next output: 47 seconds
Output 547/1000: t=54600.0 yr, dE/E0=5.77e-09, N=1001
  Estimated time remaining to complete simulation: 6 hours, 1 minutes, 54 seconds
  Estimated time remaining to next output: 47 seconds
Output 548/1000: t=54700.0 yr, dE/E0=5.59e-09, N=1001
  Estimated time remaining to complete simulation: 6 hours, 3 minutes, 12 seconds
  Estimated time remaining to next output: 48 seconds
Output 549/1000: t=54800.0 yr, dE/E0=5.37e-09, N=1001
  Estimated time remaining to complete simulation: 6 hours, 4 minutes, 45 seconds
  Estimated time remaining to next output: 48 seconds
Output 550/1000: t=54900.0 yr, dE/E0=5.33e-09, N=1001
  Estimated time remaining to complete simulation: 6 hours, 6 minutes, 45 seconds
  Estimated time remaining to next output: 48 seconds
Output 551/1000: t=55000.0 yr, dE/E0=5.18e-09, N=1001
  Estimated time remaining to complete simulation: 6 hours, 8 minutes, 35 seconds
  Estimated time remaining to next output: 49 seconds
Output 552/1000: t=55100.0 yr, dE/E0=5.08e-09, N=1001
  Estimated time remaining to complete simulation: 6 hours, 10 minutes, 35 seconds
  Estimated time remaining to next output: 49 seconds
Output 553/1000: t=55200.0 yr, dE/E0=5.31e-09, N=1001
  Estimated time remaining to complete simulation: 6 hours, 12 minutes, 30 seconds
  Estimated time remaining to next output: 50 seconds
Output 554/1000: t=55300.0 yr, dE/E0=5.50e-09, N=1001
  Estimated time remaining to complete simulation: 6 hours, 40 minutes, 33 seconds
  Estimated time remaining to next output: 53 seconds
Output 555/1000: t=55400.0 yr, dE/E0=5.53e-09, N=1001
  Estimated time remaining to complete simulation: 7 hours, 2 minutes, 37 seconds
  Estimated time remaining to next output: 56 seconds
Output 556/1000: t=55500.0 yr, dE/E0=5.51e-09, N=1001
  Estimated time remaining to complete simulation: 7 hours, 26 minutes, 42 seconds
  Estimated time remaining to next output: 1 minutes
Output 557/1000: t=55600.0 yr, dE/E0=5.53e-09, N=1001
  Estimated time remaining to complete simulation: 7 hours, 29 minutes, 15 seconds
  Estimated time remaining to next output: 1 minutes
Output 558/1000: t=55700.0 yr, dE/E0=5.61e-09, N=1001
  Estimated time remaining to complete simulation: 7 hours, 46 minutes, 4 seconds
  Estimated time remaining to next output: 1 minutes, 3 seconds
Output 559/1000: t=55800.0 yr, dE/E0=5.77e-09, N=1001
  Estimated time remaining to complete simulation: 8 hours, 7 minutes, 23 seconds
  Estimated time remaining to next output: 1 minutes, 6 seconds
Output 560/1000: t=55900.0 yr, dE/E0=5.68e-09, N=1001
  Estimated time remaining to complete simulation: 8 hours, 28 minutes, 31 seconds
  Estimated time remaining to next output: 1 minutes, 9 seconds
Output 561/1000: t=56000.0 yr, dE/E0=5.49e-09, N=1001
  Estimated time remaining to complete simulation: 8 hours, 45 minutes, 25 seconds
  Estimated time remaining to next output: 1 minutes, 11 seconds
Output 562/1000: t=56100.0 yr, dE/E0=5.18e-09, N=1001
  Estimated time remaining to complete simulation: 9 hours, 6 minutes, 16 seconds
  Estimated time remaining to next output: 1 minutes, 14 seconds
Output 563/1000: t=56200.0 yr, dE/E0=5.19e-09, N=1001
  Estimated time remaining to complete simulation: 9 hours, 24 minutes, 16 seconds
  Estimated time remaining to next output: 1 minutes, 17 seconds
Output 564/1000: t=56300.0 yr, dE/E0=5.71e-09, N=1001
  Estimated time remaining to complete simulation: 9 hours, 32 minutes, 27 seconds
  Estimated time remaining to next output: 1 minutes, 18 seconds
Output 565/1000: t=56400.0 yr, dE/E0=5.53e-09, N=1001
  Estimated time remaining to complete simulation: 9 hours, 52 minutes, 52 seconds
  Estimated time remaining to next output: 1 minutes, 21 seconds
Output 566/1000: t=56500.0 yr, dE/E0=5.25e-09, N=1001
  Estimated time remaining to complete simulation: 10 hours, 12 minutes, 54 seconds
  Estimated time remaining to next output: 1 minutes, 24 seconds
Output 567/1000: t=56600.0 yr, dE/E0=4.88e-09, N=1001
  Estimated time remaining to complete simulation: 10 hours, 28 minutes, 45 seconds
  Estimated time remaining to next output: 1 minutes, 27 seconds
Output 568/1000: t=56700.0 yr, dE/E0=4.35e-09, N=1001
  Estimated time remaining to complete simulation: 10 hours, 28 minutes, 39 seconds
  Estimated time remaining to next output: 1 minutes, 27 seconds
Output 569/1000: t=56800.0 yr, dE/E0=4.51e-09, N=1001
  Estimated time remaining to complete simulation: 10 hours, 39 minutes, 54 seconds
  Estimated time remaining to next output: 1 minutes, 29 seconds
Output 570/1000: t=56900.0 yr, dE/E0=4.92e-09, N=1001
  Estimated time remaining to complete simulation: 10 hours, 48 minutes, 47 seconds
  Estimated time remaining to next output: 1 minutes, 30 seconds
Output 571/1000: t=57000.0 yr, dE/E0=5.12e-09, N=1001
  Estimated time remaining to complete simulation: 11 hours, 8 minutes, 22 seconds
  Estimated time remaining to next output: 1 minutes, 33 seconds
Output 572/1000: t=57100.0 yr, dE/E0=5.38e-09, N=1001
  Estimated time remaining to complete simulation: 11 hours, 27 minutes
  Estimated time remaining to next output: 1 minutes, 36 seconds
Output 573/1000: t=57200.0 yr, dE/E0=5.24e-09, N=1001
  Estimated time remaining to complete simulation: 11 hours, 50 minutes, 7 seconds
  Estimated time remaining to next output: 1 minutes, 39 seconds
Output 574/1000: t=57300.0 yr, dE/E0=5.11e-09, N=1001
  Estimated time remaining to complete simulation: 12 hours, 7 minutes, 20 seconds
  Estimated time remaining to next output: 1 minutes, 42 seconds
Output 575/1000: t=57400.0 yr, dE/E0=5.10e-09, N=1001
  Estimated time remaining to complete simulation: 12 hours, 36 minutes, 9 seconds
  Estimated time remaining to next output: 1 minutes, 46 seconds
Output 576/1000: t=57500.0 yr, dE/E0=5.16e-09, N=1001
  Estimated time remaining to complete simulation: 12 hours, 35 minutes, 11 seconds
  Estimated time remaining to next output: 1 minutes, 46 seconds
Output 577/1000: t=57600.0 yr, dE/E0=5.38e-09, N=1001
  Estimated time remaining to complete simulation: 12 hours, 33 minutes, 42 seconds
  Estimated time remaining to next output: 1 minutes, 46 seconds
Output 578/1000: t=57700.0 yr, dE/E0=5.38e-09, N=1001
  Estimated time remaining to complete simulation: 12 hours, 35 minutes, 37 seconds
  Estimated time remaining to next output: 1 minutes, 47 seconds
Output 579/1000: t=57800.0 yr, dE/E0=5.73e-09, N=1001
  Estimated time remaining to complete simulation: 12 hours, 33 minutes, 56 seconds
  Estimated time remaining to next output: 1 minutes, 47 seconds
Output 580/1000: t=57900.0 yr, dE/E0=5.79e-09, N=1001
  Estimated time remaining to complete simulation: 12 hours, 37 minutes, 16 seconds
  Estimated time remaining to next output: 1 minutes, 48 seconds
Output 581/1000: t=58000.0 yr, dE/E0=5.75e-09, N=1001
  Estimated time remaining to complete simulation: 12 hours, 36 minutes, 4 seconds
  Estimated time remaining to next output: 1 minutes, 48 seconds
Output 582/1000: t=58100.0 yr, dE/E0=5.59e-09, N=1001
  Estimated time remaining to complete simulation: 12 hours, 34 minutes, 35 seconds
  Estimated time remaining to next output: 1 minutes, 48 seconds
Output 583/1000: t=58200.0 yr, dE/E0=5.47e-09, N=1001
  Estimated time remaining to complete simulation: 12 hours, 33 minutes, 15 seconds
  Estimated time remaining to next output: 1 minutes, 48 seconds
Output 584/1000: t=58300.0 yr, dE/E0=5.52e-09, N=1001
  Estimated time remaining to complete simulation: 12 hours, 31 minutes, 43 seconds
  Estimated time remaining to next output: 1 minutes, 48 seconds
Output 585/1000: t=58400.0 yr, dE/E0=5.63e-09, N=1001
  Estimated time remaining to complete simulation: 12 hours, 30 minutes, 21 seconds
  Estimated time remaining to next output: 1 minutes, 48 seconds
Output 586/1000: t=58500.0 yr, dE/E0=5.65e-09, N=1001
  Estimated time remaining to complete simulation: 12 hours, 28 minutes, 50 seconds
  Estimated time remaining to next output: 1 minutes, 48 seconds
Output 587/1000: t=58600.0 yr, dE/E0=5.52e-09, N=1001
  Estimated time remaining to complete simulation: 12 hours, 27 minutes, 22 seconds
  Estimated time remaining to next output: 1 minutes, 48 seconds
Output 588/1000: t=58700.0 yr, dE/E0=5.50e-09, N=1001
  Estimated time remaining to complete simulation: 12 hours, 25 minutes, 41 seconds
  Estimated time remaining to next output: 1 minutes, 48 seconds
Output 589/1000: t=58800.0 yr, dE/E0=5.25e-09, N=1001
  Estimated time remaining to complete simulation: 12 hours, 24 minutes, 2 seconds
  Estimated time remaining to next output: 1 minutes, 48 seconds
Output 590/1000: t=58900.0 yr, dE/E0=5.16e-09, N=1001
  Estimated time remaining to complete simulation: 12 hours, 22 minutes, 47 seconds
  Estimated time remaining to next output: 1 minutes, 48 seconds
Output 591/1000: t=59000.0 yr, dE/E0=5.24e-09, N=1001
  Estimated time remaining to complete simulation: 12 hours, 21 minutes, 16 seconds
  Estimated time remaining to next output: 1 minutes, 48 seconds
Output 592/1000: t=59100.0 yr, dE/E0=5.43e-09, N=1001
  Estimated time remaining to complete simulation: 12 hours, 19 minutes, 45 seconds
  Estimated time remaining to next output: 1 minutes, 48 seconds
Output 593/1000: t=59200.0 yr, dE/E0=5.29e-09, N=1001
  Estimated time remaining to complete simulation: 12 hours, 18 minutes, 18 seconds
  Estimated time remaining to next output: 1 minutes, 48 seconds
Output 594/1000: t=59300.0 yr, dE/E0=5.19e-09, N=1001
  Estimated time remaining to complete simulation: 12 hours, 16 minutes, 51 seconds
  Estimated time remaining to next output: 1 minutes, 48 seconds
Output 595/1000: t=59400.0 yr, dE/E0=5.19e-09, N=1001
  Estimated time remaining to complete simulation: 12 hours, 15 minutes, 18 seconds
  Estimated time remaining to next output: 1 minutes, 48 seconds
Output 596/1000: t=59500.0 yr, dE/E0=5.38e-09, N=1001
  Estimated time remaining to complete simulation: 12 hours, 14 minutes, 28 seconds
  Estimated time remaining to next output: 1 minutes, 49 seconds
Output 597/1000: t=59600.0 yr, dE/E0=5.47e-09, N=1001
  Estimated time remaining to complete simulation: 12 hours, 13 minutes, 27 seconds
  Estimated time remaining to next output: 1 minutes, 49 seconds
Output 598/1000: t=59700.0 yr, dE/E0=5.41e-09, N=1001
  Estimated time remaining to complete simulation: 12 hours, 11 minutes, 56 seconds
  Estimated time remaining to next output: 1 minutes, 49 seconds
Output 599/1000: t=59800.0 yr, dE/E0=5.25e-09, N=1001
  Estimated time remaining to complete simulation: 12 hours, 10 minutes, 36 seconds
  Estimated time remaining to next output: 1 minutes, 49 seconds
Output 600/1000: t=59900.0 yr, dE/E0=5.15e-09, N=1001
  Estimated time remaining to complete simulation: 12 hours, 9 minutes, 6 seconds
  Estimated time remaining to next output: 1 minutes, 49 seconds
Output 601/1000: t=60000.0 yr, dE/E0=5.11e-09, N=1001
  Estimated time remaining to complete simulation: 12 hours, 7 minutes, 34 seconds
  Estimated time remaining to next output: 1 minutes, 49 seconds
Output 602/1000: t=60100.0 yr, dE/E0=5.10e-09, N=1001
  Estimated time remaining to complete simulation: 12 hours, 6 minutes, 4 seconds
  Estimated time remaining to next output: 1 minutes, 49 seconds
Output 603/1000: t=60200.0 yr, dE/E0=5.11e-09, N=1001
  Estimated time remaining to complete simulation: 12 hours, 4 minutes, 32 seconds
  Estimated time remaining to next output: 1 minutes, 49 seconds
Output 604/1000: t=60300.0 yr, dE/E0=5.21e-09, N=1001
  Estimated time remaining to complete simulation: 12 hours, 3 minutes, 3 seconds
  Estimated time remaining to next output: 1 minutes, 49 seconds
Output 605/1000: t=60400.0 yr, dE/E0=5.43e-09, N=1001
  Estimated time remaining to complete simulation: 12 hours, 1 minutes, 34 seconds
  Estimated time remaining to next output: 1 minutes, 49 seconds
Output 606/1000: t=60500.0 yr, dE/E0=5.47e-09, N=1001
  Estimated time remaining to complete simulation: 12 hours, 2 seconds
  Estimated time remaining to next output: 1 minutes, 49 seconds
Output 607/1000: t=60600.0 yr, dE/E0=5.48e-09, N=1001
  Estimated time remaining to complete simulation: 11 hours, 58 minutes, 28 seconds
  Estimated time remaining to next output: 1 minutes, 49 seconds
Output 608/1000: t=60700.0 yr, dE/E0=5.50e-09, N=1001
  Estimated time remaining to complete simulation: 11 hours, 56 minutes, 51 seconds
  Estimated time remaining to next output: 1 minutes, 49 seconds
Output 609/1000: t=60800.0 yr, dE/E0=5.54e-09, N=1001
  Estimated time remaining to complete simulation: 12 hours, 8 seconds
  Estimated time remaining to next output: 1 minutes, 50 seconds
Output 610/1000: t=60900.0 yr, dE/E0=5.56e-09, N=1001
  Estimated time remaining to complete simulation: 11 hours, 58 minutes, 34 seconds
  Estimated time remaining to next output: 1 minutes, 50 seconds
Output 611/1000: t=61000.0 yr, dE/E0=5.53e-09, N=1001
  Estimated time remaining to complete simulation: 11 hours, 57 minutes, 6 seconds
  Estimated time remaining to next output: 1 minutes, 50 seconds
Output 612/1000: t=61100.0 yr, dE/E0=5.56e-09, N=1001
  Estimated time remaining to complete simulation: 11 hours, 55 minutes, 39 seconds
  Estimated time remaining to next output: 1 minutes, 50 seconds
Output 613/1000: t=61200.0 yr, dE/E0=5.47e-09, N=1001
  Estimated time remaining to complete simulation: 11 hours, 54 minutes, 21 seconds
  Estimated time remaining to next output: 1 minutes, 50 seconds
Output 614/1000: t=61300.0 yr, dE/E0=5.25e-09, N=1001
  Estimated time remaining to complete simulation: 11 hours, 52 minutes, 55 seconds
  Estimated time remaining to next output: 1 minutes, 50 seconds
Output 615/1000: t=61400.0 yr, dE/E0=5.19e-09, N=1001
  Estimated time remaining to complete simulation: 11 hours, 51 minutes, 27 seconds
  Estimated time remaining to next output: 1 minutes, 50 seconds
Output 616/1000: t=61500.0 yr, dE/E0=5.28e-09, N=1001
  Estimated time remaining to complete simulation: 11 hours, 50 minutes, 3 seconds
  Estimated time remaining to next output: 1 minutes, 50 seconds
Output 617/1000: t=61600.0 yr, dE/E0=5.41e-09, N=1001
  Estimated time remaining to complete simulation: 11 hours, 48 minutes, 32 seconds
  Estimated time remaining to next output: 1 minutes, 50 seconds
Output 618/1000: t=61700.0 yr, dE/E0=5.46e-09, N=1001
  Estimated time remaining to complete simulation: 11 hours, 46 minutes, 44 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 619/1000: t=61800.0 yr, dE/E0=5.62e-09, N=1001
  Estimated time remaining to complete simulation: 11 hours, 44 minutes, 54 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 620/1000: t=61900.0 yr, dE/E0=5.65e-09, N=1001
  Estimated time remaining to complete simulation: 11 hours, 43 minutes, 12 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 621/1000: t=62000.0 yr, dE/E0=5.66e-09, N=1001
  Estimated time remaining to complete simulation: 11 hours, 41 minutes, 38 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 622/1000: t=62100.0 yr, dE/E0=5.61e-09, N=1001
  Estimated time remaining to complete simulation: 11 hours, 40 minutes, 2 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 623/1000: t=62200.0 yr, dE/E0=5.06e-09, N=1001
  Estimated time remaining to complete simulation: 11 hours, 38 minutes, 25 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 624/1000: t=62300.0 yr, dE/E0=4.84e-09, N=1001
  Estimated time remaining to complete simulation: 11 hours, 36 minutes, 55 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 625/1000: t=62400.0 yr, dE/E0=5.27e-09, N=1001
  Estimated time remaining to complete simulation: 11 hours, 35 minutes, 25 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 626/1000: t=62500.0 yr, dE/E0=4.84e-09, N=1001
  Estimated time remaining to complete simulation: 11 hours, 33 minutes, 46 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 627/1000: t=62600.0 yr, dE/E0=5.18e-09, N=1001
  Estimated time remaining to complete simulation: 11 hours, 32 minutes, 8 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 628/1000: t=62700.0 yr, dE/E0=5.50e-09, N=1001
  Estimated time remaining to complete simulation: 11 hours, 30 minutes, 22 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 629/1000: t=62800.0 yr, dE/E0=5.34e-09, N=1001
  Estimated time remaining to complete simulation: 11 hours, 28 minutes, 38 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 630/1000: t=62900.0 yr, dE/E0=5.43e-09, N=1001
  Estimated time remaining to complete simulation: 11 hours, 26 minutes, 48 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 631/1000: t=63000.0 yr, dE/E0=5.58e-09, N=1001
  Estimated time remaining to complete simulation: 11 hours, 25 minutes, 10 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 632/1000: t=63100.0 yr, dE/E0=5.76e-09, N=1001
  Estimated time remaining to complete simulation: 11 hours, 23 minutes, 6 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 633/1000: t=63200.0 yr, dE/E0=5.51e-09, N=1001
  Estimated time remaining to complete simulation: 11 hours, 21 minutes, 3 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 634/1000: t=63300.0 yr, dE/E0=5.41e-09, N=1001
  Estimated time remaining to complete simulation: 11 hours, 19 minutes, 8 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 635/1000: t=63400.0 yr, dE/E0=5.37e-09, N=1001
  Estimated time remaining to complete simulation: 11 hours, 17 minutes, 4 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 636/1000: t=63500.0 yr, dE/E0=5.24e-09, N=1001
  Estimated time remaining to complete simulation: 11 hours, 15 minutes, 2 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 637/1000: t=63600.0 yr, dE/E0=5.56e-09, N=1001
  Estimated time remaining to complete simulation: 11 hours, 12 minutes, 53 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 638/1000: t=63700.0 yr, dE/E0=5.92e-09, N=1001
  Estimated time remaining to complete simulation: 11 hours, 10 minutes, 49 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 639/1000: t=63800.0 yr, dE/E0=5.50e-09, N=1001
  Estimated time remaining to complete simulation: 11 hours, 8 minutes, 46 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 640/1000: t=63900.0 yr, dE/E0=5.17e-09, N=1001
  Estimated time remaining to complete simulation: 11 hours, 6 minutes, 44 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 641/1000: t=64000.0 yr, dE/E0=5.19e-09, N=1001
  Estimated time remaining to complete simulation: 11 hours, 4 minutes, 40 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 642/1000: t=64100.0 yr, dE/E0=5.33e-09, N=1001
  Estimated time remaining to complete simulation: 11 hours, 2 minutes, 51 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 643/1000: t=64200.0 yr, dE/E0=5.55e-09, N=1001
  Estimated time remaining to complete simulation: 11 hours, 1 minutes, 5 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 644/1000: t=64300.0 yr, dE/E0=5.61e-09, N=1001
  Estimated time remaining to complete simulation: 10 hours, 59 minutes, 19 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 645/1000: t=64400.0 yr, dE/E0=5.59e-09, N=1001
  Estimated time remaining to complete simulation: 10 hours, 57 minutes, 29 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 646/1000: t=64500.0 yr, dE/E0=5.60e-09, N=1001
  Estimated time remaining to complete simulation: 10 hours, 55 minutes, 33 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 647/1000: t=64600.0 yr, dE/E0=5.88e-09, N=1001
  Estimated time remaining to complete simulation: 10 hours, 53 minutes, 35 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 648/1000: t=64700.0 yr, dE/E0=5.73e-09, N=1001
  Estimated time remaining to complete simulation: 10 hours, 51 minutes, 40 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 649/1000: t=64800.0 yr, dE/E0=4.99e-09, N=1001
  Estimated time remaining to complete simulation: 10 hours, 49 minutes, 42 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 650/1000: t=64900.0 yr, dE/E0=4.58e-09, N=1001
  Estimated time remaining to complete simulation: 10 hours, 47 minutes, 45 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 651/1000: t=65000.0 yr, dE/E0=4.51e-09, N=1001
  Estimated time remaining to complete simulation: 10 hours, 45 minutes, 48 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 652/1000: t=65100.0 yr, dE/E0=4.91e-09, N=1001
  Estimated time remaining to complete simulation: 10 hours, 43 minutes, 55 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 653/1000: t=65200.0 yr, dE/E0=4.92e-09, N=1001
  Estimated time remaining to complete simulation: 10 hours, 42 minutes, 3 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 654/1000: t=65300.0 yr, dE/E0=5.36e-09, N=1001
  Estimated time remaining to complete simulation: 10 hours, 40 minutes, 23 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 655/1000: t=65400.0 yr, dE/E0=5.82e-09, N=1001
  Estimated time remaining to complete simulation: 10 hours, 38 minutes, 40 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 656/1000: t=65500.0 yr, dE/E0=5.85e-09, N=1001
  Estimated time remaining to complete simulation: 10 hours, 36 minutes, 50 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 657/1000: t=65600.0 yr, dE/E0=5.68e-09, N=1001
  Estimated time remaining to complete simulation: 10 hours, 35 minutes
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 658/1000: t=65700.0 yr, dE/E0=5.62e-09, N=1001
  Estimated time remaining to complete simulation: 10 hours, 33 minutes, 6 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 659/1000: t=65800.0 yr, dE/E0=5.55e-09, N=1001
  Estimated time remaining to complete simulation: 10 hours, 31 minutes, 14 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 660/1000: t=65900.0 yr, dE/E0=5.50e-09, N=1001
  Estimated time remaining to complete simulation: 10 hours, 29 minutes, 23 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 661/1000: t=66000.0 yr, dE/E0=5.44e-09, N=1001
  Estimated time remaining to complete simulation: 10 hours, 27 minutes, 31 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 662/1000: t=66100.0 yr, dE/E0=5.60e-09, N=1001
  Estimated time remaining to complete simulation: 10 hours, 25 minutes, 40 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 663/1000: t=66200.0 yr, dE/E0=5.64e-09, N=1001
  Estimated time remaining to complete simulation: 10 hours, 23 minutes, 51 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 664/1000: t=66300.0 yr, dE/E0=5.51e-09, N=1001
  Estimated time remaining to complete simulation: 10 hours, 22 minutes, 12 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 665/1000: t=66400.0 yr, dE/E0=5.30e-09, N=1001
  Estimated time remaining to complete simulation: 10 hours, 20 minutes, 35 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 666/1000: t=66500.0 yr, dE/E0=5.30e-09, N=1001
  Estimated time remaining to complete simulation: 10 hours, 18 minutes, 55 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 667/1000: t=66600.0 yr, dE/E0=5.31e-09, N=1001
  Estimated time remaining to complete simulation: 10 hours, 17 minutes, 17 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 668/1000: t=66700.0 yr, dE/E0=5.13e-09, N=1001
  Estimated time remaining to complete simulation: 10 hours, 15 minutes, 29 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 669/1000: t=66800.0 yr, dE/E0=5.03e-09, N=1001
  Estimated time remaining to complete simulation: 10 hours, 13 minutes, 46 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 670/1000: t=66900.0 yr, dE/E0=5.05e-09, N=1001
  Estimated time remaining to complete simulation: 10 hours, 12 minutes, 5 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 671/1000: t=67000.0 yr, dE/E0=5.08e-09, N=1001
  Estimated time remaining to complete simulation: 10 hours, 10 minutes, 21 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 672/1000: t=67100.0 yr, dE/E0=5.27e-09, N=1001
  Estimated time remaining to complete simulation: 10 hours, 8 minutes, 40 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 673/1000: t=67200.0 yr, dE/E0=5.43e-09, N=1001
  Estimated time remaining to complete simulation: 10 hours, 6 minutes, 56 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 674/1000: t=67300.0 yr, dE/E0=5.44e-09, N=1001
  Estimated time remaining to complete simulation: 10 hours, 5 minutes, 22 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 675/1000: t=67400.0 yr, dE/E0=5.43e-09, N=1001
  Estimated time remaining to complete simulation: 10 hours, 3 minutes, 55 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 676/1000: t=67500.0 yr, dE/E0=5.36e-09, N=1001
  Estimated time remaining to complete simulation: 10 hours, 2 minutes, 25 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 677/1000: t=67600.0 yr, dE/E0=5.47e-09, N=1001
  Estimated time remaining to complete simulation: 10 hours, 45 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 678/1000: t=67700.0 yr, dE/E0=5.54e-09, N=1001
  Estimated time remaining to complete simulation: 9 hours, 59 minutes, 3 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 679/1000: t=67800.0 yr, dE/E0=5.54e-09, N=1001
  Estimated time remaining to complete simulation: 9 hours, 57 minutes, 31 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 680/1000: t=67900.0 yr, dE/E0=5.64e-09, N=1001
  Estimated time remaining to complete simulation: 9 hours, 56 minutes, 1 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 681/1000: t=68000.0 yr, dE/E0=5.52e-09, N=1001
  Estimated time remaining to complete simulation: 9 hours, 54 minutes, 31 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 682/1000: t=68100.0 yr, dE/E0=5.25e-09, N=1001
  Estimated time remaining to complete simulation: 9 hours, 52 minutes, 52 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 683/1000: t=68200.0 yr, dE/E0=5.26e-09, N=1001
  Estimated time remaining to complete simulation: 9 hours, 51 minutes, 9 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 684/1000: t=68300.0 yr, dE/E0=5.18e-09, N=1001
  Estimated time remaining to complete simulation: 9 hours, 49 minutes, 40 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 685/1000: t=68400.0 yr, dE/E0=5.23e-09, N=1001
  Estimated time remaining to complete simulation: 9 hours, 48 minutes, 13 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 686/1000: t=68500.0 yr, dE/E0=5.41e-09, N=1001
  Estimated time remaining to complete simulation: 9 hours, 46 minutes, 36 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 687/1000: t=68600.0 yr, dE/E0=5.51e-09, N=1001
  Estimated time remaining to complete simulation: 9 hours, 44 minutes, 54 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 688/1000: t=68700.0 yr, dE/E0=5.45e-09, N=1001
  Estimated time remaining to complete simulation: 9 hours, 43 minutes, 21 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 689/1000: t=68800.0 yr, dE/E0=5.31e-09, N=1001
  Estimated time remaining to complete simulation: 9 hours, 41 minutes, 40 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 690/1000: t=68900.0 yr, dE/E0=5.30e-09, N=1001
  Estimated time remaining to complete simulation: 9 hours, 40 minutes
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 691/1000: t=69000.0 yr, dE/E0=5.48e-09, N=1001
  Estimated time remaining to complete simulation: 9 hours, 38 minutes, 17 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 692/1000: t=69100.0 yr, dE/E0=5.57e-09, N=1001
  Estimated time remaining to complete simulation: 9 hours, 36 minutes, 31 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 693/1000: t=69200.0 yr, dE/E0=5.45e-09, N=1001
  Estimated time remaining to complete simulation: 9 hours, 34 minutes, 44 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 694/1000: t=69300.0 yr, dE/E0=5.35e-09, N=1001
  Estimated time remaining to complete simulation: 9 hours, 33 minutes, 1 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 695/1000: t=69400.0 yr, dE/E0=5.37e-09, N=1001
  Estimated time remaining to complete simulation: 9 hours, 31 minutes, 31 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 696/1000: t=69500.0 yr, dE/E0=5.38e-09, N=1001
  Estimated time remaining to complete simulation: 9 hours, 29 minutes, 49 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 697/1000: t=69600.0 yr, dE/E0=5.49e-09, N=1001
  Estimated time remaining to complete simulation: 9 hours, 28 minutes, 1 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 698/1000: t=69700.0 yr, dE/E0=5.54e-09, N=1001
  Estimated time remaining to complete simulation: 9 hours, 26 minutes, 9 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 699/1000: t=69800.0 yr, dE/E0=5.55e-09, N=1001
  Estimated time remaining to complete simulation: 9 hours, 24 minutes, 18 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 700/1000: t=69900.0 yr, dE/E0=5.44e-09, N=1001
  Estimated time remaining to complete simulation: 9 hours, 22 minutes, 27 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 701/1000: t=70000.0 yr, dE/E0=5.33e-09, N=1001
  Estimated time remaining to complete simulation: 9 hours, 20 minutes, 35 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 702/1000: t=70100.0 yr, dE/E0=5.24e-09, N=1001
  Estimated time remaining to complete simulation: 9 hours, 18 minutes, 41 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 703/1000: t=70200.0 yr, dE/E0=5.09e-09, N=1001
  Estimated time remaining to complete simulation: 9 hours, 16 minutes, 57 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 704/1000: t=70300.0 yr, dE/E0=4.80e-09, N=1001
  Estimated time remaining to complete simulation: 9 hours, 15 minutes, 5 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 705/1000: t=70400.0 yr, dE/E0=5.16e-09, N=1001
  Estimated time remaining to complete simulation: 9 hours, 13 minutes, 22 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 706/1000: t=70500.0 yr, dE/E0=5.46e-09, N=1001
  Estimated time remaining to complete simulation: 9 hours, 11 minutes, 35 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 707/1000: t=70600.0 yr, dE/E0=5.40e-09, N=1001
  Estimated time remaining to complete simulation: 9 hours, 9 minutes, 45 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 708/1000: t=70700.0 yr, dE/E0=5.38e-09, N=1001
  Estimated time remaining to complete simulation: 9 hours, 7 minutes, 49 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 709/1000: t=70800.0 yr, dE/E0=5.51e-09, N=1001
  Estimated time remaining to complete simulation: 9 hours, 5 minutes, 53 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 710/1000: t=70900.0 yr, dE/E0=5.56e-09, N=1001
  Estimated time remaining to complete simulation: 9 hours, 3 minutes, 57 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 711/1000: t=71000.0 yr, dE/E0=5.52e-09, N=1001
  Estimated time remaining to complete simulation: 9 hours, 1 minutes, 59 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 712/1000: t=71100.0 yr, dE/E0=5.68e-09, N=1001
  Estimated time remaining to complete simulation: 9 hours, 1 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 713/1000: t=71200.0 yr, dE/E0=5.59e-09, N=1001
  Estimated time remaining to complete simulation: 8 hours, 58 minutes, 3 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 714/1000: t=71300.0 yr, dE/E0=4.97e-09, N=1001
  Estimated time remaining to complete simulation: 8 hours, 56 minutes, 8 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 715/1000: t=71400.0 yr, dE/E0=4.86e-09, N=1001
  Estimated time remaining to complete simulation: 8 hours, 54 minutes, 18 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 716/1000: t=71500.0 yr, dE/E0=4.86e-09, N=1001
  Estimated time remaining to complete simulation: 8 hours, 52 minutes, 30 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 717/1000: t=71600.0 yr, dE/E0=5.46e-09, N=1001
  Estimated time remaining to complete simulation: 8 hours, 50 minutes, 30 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 718/1000: t=71700.0 yr, dE/E0=5.74e-09, N=1001
  Estimated time remaining to complete simulation: 8 hours, 48 minutes, 39 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 719/1000: t=71800.0 yr, dE/E0=5.60e-09, N=1001
  Estimated time remaining to complete simulation: 8 hours, 46 minutes, 38 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 720/1000: t=71900.0 yr, dE/E0=5.38e-09, N=1001
  Estimated time remaining to complete simulation: 8 hours, 44 minutes, 38 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 721/1000: t=72000.0 yr, dE/E0=5.27e-09, N=1001
  Estimated time remaining to complete simulation: 8 hours, 42 minutes, 39 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 722/1000: t=72100.0 yr, dE/E0=5.14e-09, N=1001
  Estimated time remaining to complete simulation: 8 hours, 40 minutes, 39 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 723/1000: t=72200.0 yr, dE/E0=5.25e-09, N=1001
  Estimated time remaining to complete simulation: 8 hours, 38 minutes, 38 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 724/1000: t=72300.0 yr, dE/E0=5.31e-09, N=1001
  Estimated time remaining to complete simulation: 8 hours, 36 minutes, 43 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 725/1000: t=72400.0 yr, dE/E0=5.53e-09, N=1001
  Estimated time remaining to complete simulation: 8 hours, 34 minutes, 54 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 726/1000: t=72500.0 yr, dE/E0=5.41e-09, N=1001
  Estimated time remaining to complete simulation: 8 hours, 33 minutes, 4 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 727/1000: t=72600.0 yr, dE/E0=5.55e-09, N=1001
  Estimated time remaining to complete simulation: 8 hours, 31 minutes, 6 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 728/1000: t=72700.0 yr, dE/E0=5.74e-09, N=1001
  Estimated time remaining to complete simulation: 8 hours, 29 minutes, 7 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 729/1000: t=72800.0 yr, dE/E0=5.19e-09, N=1001
  Estimated time remaining to complete simulation: 8 hours, 27 minutes, 6 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 730/1000: t=72900.0 yr, dE/E0=4.91e-09, N=1001
  Estimated time remaining to complete simulation: 8 hours, 25 minutes, 4 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 731/1000: t=73000.0 yr, dE/E0=4.90e-09, N=1001
  Estimated time remaining to complete simulation: 8 hours, 23 minutes, 3 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 732/1000: t=73100.0 yr, dE/E0=5.35e-09, N=1001
  Estimated time remaining to complete simulation: 8 hours, 21 minutes, 9 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 733/1000: t=73200.0 yr, dE/E0=5.80e-09, N=1001
  Estimated time remaining to complete simulation: 8 hours, 19 minutes, 8 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 734/1000: t=73300.0 yr, dE/E0=5.73e-09, N=1001
  Estimated time remaining to complete simulation: 8 hours, 17 minutes, 7 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 735/1000: t=73400.0 yr, dE/E0=5.35e-09, N=1001
  Estimated time remaining to complete simulation: 8 hours, 15 minutes, 7 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 736/1000: t=73500.0 yr, dE/E0=5.06e-09, N=1001
  Estimated time remaining to complete simulation: 8 hours, 13 minutes, 13 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 737/1000: t=73600.0 yr, dE/E0=4.95e-09, N=1001
  Estimated time remaining to complete simulation: 8 hours, 11 minutes, 16 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 738/1000: t=73700.0 yr, dE/E0=4.97e-09, N=1001
  Estimated time remaining to complete simulation: 8 hours, 9 minutes, 16 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 739/1000: t=73800.0 yr, dE/E0=5.12e-09, N=1001
  Estimated time remaining to complete simulation: 8 hours, 7 minutes, 19 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 740/1000: t=73900.0 yr, dE/E0=5.16e-09, N=1001
  Estimated time remaining to complete simulation: 8 hours, 5 minutes, 37 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 741/1000: t=74000.0 yr, dE/E0=5.26e-09, N=1001
  Estimated time remaining to complete simulation: 8 hours, 3 minutes, 39 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 742/1000: t=74100.0 yr, dE/E0=5.37e-09, N=1001
  Estimated time remaining to complete simulation: 8 hours, 1 minutes, 37 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 743/1000: t=74200.0 yr, dE/E0=5.29e-09, N=1001
  Estimated time remaining to complete simulation: 7 hours, 59 minutes, 35 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 744/1000: t=74300.0 yr, dE/E0=5.35e-09, N=1001
  Estimated time remaining to complete simulation: 7 hours, 57 minutes, 35 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 745/1000: t=74400.0 yr, dE/E0=5.35e-09, N=1001
  Estimated time remaining to complete simulation: 7 hours, 55 minutes, 37 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 746/1000: t=74500.0 yr, dE/E0=5.47e-09, N=1001
  Estimated time remaining to complete simulation: 7 hours, 53 minutes, 42 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 747/1000: t=74600.0 yr, dE/E0=5.42e-09, N=1001
  Estimated time remaining to complete simulation: 7 hours, 51 minutes, 45 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 748/1000: t=74700.0 yr, dE/E0=5.18e-09, N=1001
  Estimated time remaining to complete simulation: 7 hours, 49 minutes, 45 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 749/1000: t=74800.0 yr, dE/E0=5.00e-09, N=1001
  Estimated time remaining to complete simulation: 7 hours, 47 minutes, 44 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 750/1000: t=74900.0 yr, dE/E0=4.98e-09, N=1001
  Estimated time remaining to complete simulation: 7 hours, 45 minutes, 43 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 751/1000: t=75000.0 yr, dE/E0=5.06e-09, N=1001
  Estimated time remaining to complete simulation: 7 hours, 43 minutes, 41 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 752/1000: t=75100.0 yr, dE/E0=5.15e-09, N=1001
  Estimated time remaining to complete simulation: 7 hours, 41 minutes, 37 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 753/1000: t=75200.0 yr, dE/E0=5.23e-09, N=1001
  Estimated time remaining to complete simulation: 7 hours, 39 minutes, 42 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 754/1000: t=75300.0 yr, dE/E0=5.27e-09, N=1001
  Estimated time remaining to complete simulation: 7 hours, 37 minutes, 44 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 755/1000: t=75400.0 yr, dE/E0=5.38e-09, N=1001
  Estimated time remaining to complete simulation: 7 hours, 35 minutes, 48 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 756/1000: t=75500.0 yr, dE/E0=5.52e-09, N=1001
  Estimated time remaining to complete simulation: 7 hours, 33 minutes, 57 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 757/1000: t=75600.0 yr, dE/E0=5.47e-09, N=1001
  Estimated time remaining to complete simulation: 7 hours, 32 minutes, 9 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 758/1000: t=75700.0 yr, dE/E0=5.22e-09, N=1001
  Estimated time remaining to complete simulation: 7 hours, 30 minutes, 13 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 759/1000: t=75800.0 yr, dE/E0=5.05e-09, N=1001
  Estimated time remaining to complete simulation: 7 hours, 28 minutes, 16 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 760/1000: t=75900.0 yr, dE/E0=5.16e-09, N=1001
  Estimated time remaining to complete simulation: 7 hours, 26 minutes, 20 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 761/1000: t=76000.0 yr, dE/E0=5.04e-09, N=1001
  Estimated time remaining to complete simulation: 7 hours, 24 minutes, 22 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 762/1000: t=76100.0 yr, dE/E0=5.22e-09, N=1001
  Estimated time remaining to complete simulation: 7 hours, 22 minutes, 24 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 763/1000: t=76200.0 yr, dE/E0=5.42e-09, N=1001
  Estimated time remaining to complete simulation: 7 hours, 20 minutes, 26 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 764/1000: t=76300.0 yr, dE/E0=5.44e-09, N=1001
  Estimated time remaining to complete simulation: 7 hours, 18 minutes, 30 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 765/1000: t=76400.0 yr, dE/E0=5.34e-09, N=1001
  Estimated time remaining to complete simulation: 7 hours, 16 minutes, 35 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 766/1000: t=76500.0 yr, dE/E0=5.18e-09, N=1001
  Estimated time remaining to complete simulation: 7 hours, 14 minutes, 46 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 767/1000: t=76600.0 yr, dE/E0=5.20e-09, N=1001
  Estimated time remaining to complete simulation: 7 hours, 12 minutes, 55 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 768/1000: t=76700.0 yr, dE/E0=5.29e-09, N=1001
  Estimated time remaining to complete simulation: 7 hours, 11 minutes, 3 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 769/1000: t=76800.0 yr, dE/E0=5.36e-09, N=1001
  Estimated time remaining to complete simulation: 7 hours, 9 minutes, 7 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 770/1000: t=76900.0 yr, dE/E0=5.37e-09, N=1001
  Estimated time remaining to complete simulation: 7 hours, 7 minutes, 10 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 771/1000: t=77000.0 yr, dE/E0=5.41e-09, N=1001
  Estimated time remaining to complete simulation: 7 hours, 5 minutes, 15 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 772/1000: t=77100.0 yr, dE/E0=5.37e-09, N=1001
  Estimated time remaining to complete simulation: 7 hours, 3 minutes, 17 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 773/1000: t=77200.0 yr, dE/E0=5.31e-09, N=1001
  Estimated time remaining to complete simulation: 7 hours, 1 minutes, 20 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 774/1000: t=77300.0 yr, dE/E0=5.24e-09, N=1001
  Estimated time remaining to complete simulation: 6 hours, 59 minutes, 26 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 775/1000: t=77400.0 yr, dE/E0=5.29e-09, N=1001
  Estimated time remaining to complete simulation: 6 hours, 57 minutes, 31 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 776/1000: t=77500.0 yr, dE/E0=5.53e-09, N=1001
  Estimated time remaining to complete simulation: 6 hours, 55 minutes, 41 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 777/1000: t=77600.0 yr, dE/E0=5.42e-09, N=1001
  Estimated time remaining to complete simulation: 6 hours, 53 minutes, 52 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 778/1000: t=77700.0 yr, dE/E0=5.30e-09, N=1001
  Estimated time remaining to complete simulation: 6 hours, 52 minutes, 6 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 779/1000: t=77800.0 yr, dE/E0=5.12e-09, N=1001
  Estimated time remaining to complete simulation: 6 hours, 50 minutes, 16 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 780/1000: t=77900.0 yr, dE/E0=5.06e-09, N=1001
  Estimated time remaining to complete simulation: 6 hours, 48 minutes, 21 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 781/1000: t=78000.0 yr, dE/E0=5.08e-09, N=1001
  Estimated time remaining to complete simulation: 6 hours, 46 minutes, 27 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 782/1000: t=78100.0 yr, dE/E0=5.12e-09, N=1001
  Estimated time remaining to complete simulation: 6 hours, 44 minutes, 38 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 783/1000: t=78200.0 yr, dE/E0=5.20e-09, N=1001
  Estimated time remaining to complete simulation: 6 hours, 42 minutes, 45 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 784/1000: t=78300.0 yr, dE/E0=5.37e-09, N=1001
  Estimated time remaining to complete simulation: 6 hours, 40 minutes, 55 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 785/1000: t=78400.0 yr, dE/E0=5.56e-09, N=1001
  Estimated time remaining to complete simulation: 6 hours, 39 minutes, 3 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 786/1000: t=78500.0 yr, dE/E0=5.62e-09, N=1001
  Estimated time remaining to complete simulation: 6 hours, 37 minutes, 16 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 787/1000: t=78600.0 yr, dE/E0=5.42e-09, N=1001
  Estimated time remaining to complete simulation: 6 hours, 35 minutes, 30 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 788/1000: t=78700.0 yr, dE/E0=5.14e-09, N=1001
  Estimated time remaining to complete simulation: 6 hours, 33 minutes, 42 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 789/1000: t=78800.0 yr, dE/E0=5.03e-09, N=1001
  Estimated time remaining to complete simulation: 6 hours, 31 minutes, 54 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 790/1000: t=78900.0 yr, dE/E0=5.08e-09, N=1001
  Estimated time remaining to complete simulation: 6 hours, 30 minutes, 4 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 791/1000: t=79000.0 yr, dE/E0=5.12e-09, N=1001
  Estimated time remaining to complete simulation: 6 hours, 28 minutes, 14 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 792/1000: t=79100.0 yr, dE/E0=4.94e-09, N=1001
  Estimated time remaining to complete simulation: 6 hours, 26 minutes, 25 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 793/1000: t=79200.0 yr, dE/E0=5.19e-09, N=1001
  Estimated time remaining to complete simulation: 6 hours, 24 minutes, 35 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 794/1000: t=79300.0 yr, dE/E0=5.52e-09, N=1001
  Estimated time remaining to complete simulation: 6 hours, 22 minutes, 44 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 795/1000: t=79400.0 yr, dE/E0=5.57e-09, N=1001
  Estimated time remaining to complete simulation: 6 hours, 20 minutes, 56 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 796/1000: t=79500.0 yr, dE/E0=5.22e-09, N=1001
  Estimated time remaining to complete simulation: 6 hours, 19 minutes, 12 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 797/1000: t=79600.0 yr, dE/E0=5.04e-09, N=1001
  Estimated time remaining to complete simulation: 6 hours, 17 minutes, 31 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 798/1000: t=79700.0 yr, dE/E0=5.39e-09, N=1001
  Estimated time remaining to complete simulation: 6 hours, 15 minutes, 48 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 799/1000: t=79800.0 yr, dE/E0=5.35e-09, N=1001
  Estimated time remaining to complete simulation: 6 hours, 14 minutes, 2 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 800/1000: t=79900.0 yr, dE/E0=5.31e-09, N=1001
  Estimated time remaining to complete simulation: 6 hours, 12 minutes, 15 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 801/1000: t=80000.0 yr, dE/E0=5.38e-09, N=1001
  Estimated time remaining to complete simulation: 6 hours, 10 minutes, 33 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 802/1000: t=80100.0 yr, dE/E0=5.54e-09, N=1001
  Estimated time remaining to complete simulation: 6 hours, 8 minutes, 50 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 803/1000: t=80200.0 yr, dE/E0=5.38e-09, N=1001
  Estimated time remaining to complete simulation: 6 hours, 7 minutes, 6 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 804/1000: t=80300.0 yr, dE/E0=5.44e-09, N=1001
  Estimated time remaining to complete simulation: 6 hours, 5 minutes, 21 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 805/1000: t=80400.0 yr, dE/E0=5.61e-09, N=1001
  Estimated time remaining to complete simulation: 6 hours, 3 minutes, 39 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 806/1000: t=80500.0 yr, dE/E0=5.30e-09, N=1001
  Estimated time remaining to complete simulation: 6 hours, 1 minutes, 58 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 807/1000: t=80600.0 yr, dE/E0=4.93e-09, N=1001
  Estimated time remaining to complete simulation: 6 hours, 25 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 808/1000: t=80700.0 yr, dE/E0=5.12e-09, N=1001
  Estimated time remaining to complete simulation: 5 hours, 58 minutes, 50 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 809/1000: t=80800.0 yr, dE/E0=4.83e-09, N=1001
  Estimated time remaining to complete simulation: 5 hours, 57 minutes, 8 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 810/1000: t=80900.0 yr, dE/E0=5.04e-09, N=1001
  Estimated time remaining to complete simulation: 5 hours, 55 minutes, 24 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 811/1000: t=81000.0 yr, dE/E0=5.43e-09, N=1001
  Estimated time remaining to complete simulation: 5 hours, 53 minutes, 45 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 812/1000: t=81100.0 yr, dE/E0=5.38e-09, N=1001
  Estimated time remaining to complete simulation: 5 hours, 52 minutes, 8 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 813/1000: t=81200.0 yr, dE/E0=5.64e-09, N=1001
  Estimated time remaining to complete simulation: 5 hours, 50 minutes, 29 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 814/1000: t=81300.0 yr, dE/E0=5.39e-09, N=1001
  Estimated time remaining to complete simulation: 5 hours, 53 minutes, 11 seconds
  Estimated time remaining to next output: 1 minutes, 53 seconds
Output 815/1000: t=81400.0 yr, dE/E0=5.13e-09, N=1001
  Estimated time remaining to complete simulation: 5 hours, 51 minutes, 32 seconds
  Estimated time remaining to next output: 1 minutes, 54 seconds
Output 816/1000: t=81500.0 yr, dE/E0=4.95e-09, N=1001
  Estimated time remaining to complete simulation: 5 hours, 49 minutes, 44 seconds
  Estimated time remaining to next output: 1 minutes, 54 seconds
Output 817/1000: t=81600.0 yr, dE/E0=5.17e-09, N=1001
  Estimated time remaining to complete simulation: 5 hours, 48 minutes, 1 seconds
  Estimated time remaining to next output: 1 minutes, 54 seconds
Output 818/1000: t=81700.0 yr, dE/E0=5.32e-09, N=1001
  Estimated time remaining to complete simulation: 5 hours, 46 minutes, 12 seconds
  Estimated time remaining to next output: 1 minutes, 54 seconds
Output 819/1000: t=81800.0 yr, dE/E0=5.23e-09, N=1001
  Estimated time remaining to complete simulation: 5 hours, 44 minutes, 22 seconds
  Estimated time remaining to next output: 1 minutes, 54 seconds
Output 820/1000: t=81900.0 yr, dE/E0=5.36e-09, N=1001
  Estimated time remaining to complete simulation: 5 hours, 42 minutes, 36 seconds
  Estimated time remaining to next output: 1 minutes, 54 seconds
Output 821/1000: t=82000.0 yr, dE/E0=5.42e-09, N=1001
  Estimated time remaining to complete simulation: 5 hours, 40 minutes, 45 seconds
  Estimated time remaining to next output: 1 minutes, 54 seconds
Output 822/1000: t=82100.0 yr, dE/E0=5.44e-09, N=1001
  Estimated time remaining to complete simulation: 5 hours, 38 minutes, 59 seconds
  Estimated time remaining to next output: 1 minutes, 54 seconds
Output 823/1000: t=82200.0 yr, dE/E0=5.43e-09, N=1001
  Estimated time remaining to complete simulation: 5 hours, 37 minutes, 14 seconds
  Estimated time remaining to next output: 1 minutes, 54 seconds
Output 824/1000: t=82300.0 yr, dE/E0=5.47e-09, N=1001
  Estimated time remaining to complete simulation: 5 hours, 35 minutes, 22 seconds
  Estimated time remaining to next output: 1 minutes, 54 seconds
Output 825/1000: t=82400.0 yr, dE/E0=5.54e-09, N=1001
  Estimated time remaining to complete simulation: 5 hours, 33 minutes, 30 seconds
  Estimated time remaining to next output: 1 minutes, 54 seconds
Output 826/1000: t=82500.0 yr, dE/E0=5.47e-09, N=1001
  Estimated time remaining to complete simulation: 5 hours, 31 minutes, 40 seconds
  Estimated time remaining to next output: 1 minutes, 54 seconds
Output 827/1000: t=82600.0 yr, dE/E0=5.16e-09, N=1001
  Estimated time remaining to complete simulation: 5 hours, 29 minutes, 53 seconds
  Estimated time remaining to next output: 1 minutes, 54 seconds
Output 828/1000: t=82700.0 yr, dE/E0=5.28e-09, N=1001
  Estimated time remaining to complete simulation: 5 hours, 28 minutes, 5 seconds
  Estimated time remaining to next output: 1 minutes, 54 seconds
Output 829/1000: t=82800.0 yr, dE/E0=5.23e-09, N=1001
  Estimated time remaining to complete simulation: 5 hours, 26 minutes, 14 seconds
  Estimated time remaining to next output: 1 minutes, 54 seconds
Output 830/1000: t=82900.0 yr, dE/E0=5.78e-09, N=1001
  Estimated time remaining to complete simulation: 5 hours, 24 minutes, 20 seconds
  Estimated time remaining to next output: 1 minutes, 54 seconds
Output 831/1000: t=83000.0 yr, dE/E0=5.96e-09, N=1001
  Estimated time remaining to complete simulation: 5 hours, 22 minutes, 25 seconds
  Estimated time remaining to next output: 1 minutes, 54 seconds
Output 832/1000: t=83100.0 yr, dE/E0=5.58e-09, N=1001
  Estimated time remaining to complete simulation: 5 hours, 20 minutes, 30 seconds
  Estimated time remaining to next output: 1 minutes, 54 seconds
Output 833/1000: t=83200.0 yr, dE/E0=5.16e-09, N=1001
  Estimated time remaining to complete simulation: 5 hours, 18 minutes, 37 seconds
  Estimated time remaining to next output: 1 minutes, 54 seconds
Output 834/1000: t=83300.0 yr, dE/E0=4.92e-09, N=1001
  Estimated time remaining to complete simulation: 5 hours, 16 minutes, 44 seconds
  Estimated time remaining to next output: 1 minutes, 54 seconds
Output 835/1000: t=83400.0 yr, dE/E0=4.73e-09, N=1001
  Estimated time remaining to complete simulation: 5 hours, 14 minutes, 49 seconds
  Estimated time remaining to next output: 1 minutes, 54 seconds
Output 836/1000: t=83500.0 yr, dE/E0=4.74e-09, N=1001
  Estimated time remaining to complete simulation: 5 hours, 12 minutes, 58 seconds
  Estimated time remaining to next output: 1 minutes, 54 seconds
Output 837/1000: t=83600.0 yr, dE/E0=4.89e-09, N=1001
  Estimated time remaining to complete simulation: 5 hours, 11 minutes, 5 seconds
  Estimated time remaining to next output: 1 minutes, 54 seconds
Output 838/1000: t=83700.0 yr, dE/E0=5.06e-09, N=1001
  Estimated time remaining to complete simulation: 5 hours, 9 minutes, 13 seconds
  Estimated time remaining to next output: 1 minutes, 54 seconds
Output 839/1000: t=83800.0 yr, dE/E0=5.27e-09, N=1001
  Estimated time remaining to complete simulation: 5 hours, 7 minutes, 17 seconds
  Estimated time remaining to next output: 1 minutes, 54 seconds
Output 840/1000: t=83900.0 yr, dE/E0=5.48e-09, N=1001
  Estimated time remaining to complete simulation: 5 hours, 5 minutes, 19 seconds
  Estimated time remaining to next output: 1 minutes, 54 seconds
Output 841/1000: t=84000.0 yr, dE/E0=5.29e-09, N=1001
  Estimated time remaining to complete simulation: 5 hours, 3 minutes, 21 seconds
  Estimated time remaining to next output: 1 minutes, 54 seconds
Output 842/1000: t=84100.0 yr, dE/E0=4.82e-09, N=1001
  Estimated time remaining to complete simulation: 5 hours, 1 minutes, 23 seconds
  Estimated time remaining to next output: 1 minutes, 54 seconds
Output 843/1000: t=84200.0 yr, dE/E0=4.80e-09, N=1001
  Estimated time remaining to complete simulation: 4 hours, 59 minutes, 25 seconds
  Estimated time remaining to next output: 1 minutes, 54 seconds
Output 844/1000: t=84300.0 yr, dE/E0=4.85e-09, N=1001
  Estimated time remaining to complete simulation: 4 hours, 57 minutes, 27 seconds
  Estimated time remaining to next output: 1 minutes, 54 seconds
Output 845/1000: t=84400.0 yr, dE/E0=5.11e-09, N=1001
  Estimated time remaining to complete simulation: 4 hours, 55 minutes, 29 seconds
  Estimated time remaining to next output: 1 minutes, 54 seconds
Output 846/1000: t=84500.0 yr, dE/E0=5.20e-09, N=1001
  Estimated time remaining to complete simulation: 4 hours, 53 minutes, 31 seconds
  Estimated time remaining to next output: 1 minutes, 54 seconds
Output 847/1000: t=84600.0 yr, dE/E0=5.22e-09, N=1001
  Estimated time remaining to complete simulation: 4 hours, 51 minutes, 36 seconds
  Estimated time remaining to next output: 1 minutes, 54 seconds
Output 848/1000: t=84700.0 yr, dE/E0=5.45e-09, N=1001
  Estimated time remaining to complete simulation: 4 hours, 49 minutes, 42 seconds
  Estimated time remaining to next output: 1 minutes, 54 seconds
Output 849/1000: t=84800.0 yr, dE/E0=5.46e-09, N=1001
  Estimated time remaining to complete simulation: 4 hours, 47 minutes, 45 seconds
  Estimated time remaining to next output: 1 minutes, 54 seconds
Output 850/1000: t=84900.0 yr, dE/E0=5.41e-09, N=1001
  Estimated time remaining to complete simulation: 4 hours, 45 minutes, 47 seconds
  Estimated time remaining to next output: 1 minutes, 54 seconds
Output 851/1000: t=85000.0 yr, dE/E0=5.42e-09, N=1001
  Estimated time remaining to complete simulation: 4 hours, 43 minutes, 48 seconds
  Estimated time remaining to next output: 1 minutes, 54 seconds
Output 852/1000: t=85100.0 yr, dE/E0=5.32e-09, N=1001
  Estimated time remaining to complete simulation: 4 hours, 41 minutes, 50 seconds
  Estimated time remaining to next output: 1 minutes, 54 seconds
Output 853/1000: t=85200.0 yr, dE/E0=5.37e-09, N=1001
  Estimated time remaining to complete simulation: 4 hours, 39 minutes, 52 seconds
  Estimated time remaining to next output: 1 minutes, 54 seconds
Output 854/1000: t=85300.0 yr, dE/E0=5.38e-09, N=1001
  Estimated time remaining to complete simulation: 4 hours, 37 minutes, 53 seconds
  Estimated time remaining to next output: 1 minutes, 54 seconds
Output 855/1000: t=85400.0 yr, dE/E0=5.30e-09, N=1001
  Estimated time remaining to complete simulation: 4 hours, 35 minutes, 55 seconds
  Estimated time remaining to next output: 1 minutes, 54 seconds
Output 856/1000: t=85500.0 yr, dE/E0=5.29e-09, N=1001
  Estimated time remaining to complete simulation: 4 hours, 33 minutes, 57 seconds
  Estimated time remaining to next output: 1 minutes, 54 seconds
Output 857/1000: t=85600.0 yr, dE/E0=5.24e-09, N=1001
  Estimated time remaining to complete simulation: 4 hours, 32 minutes
  Estimated time remaining to next output: 1 minutes, 54 seconds
Output 858/1000: t=85700.0 yr, dE/E0=5.32e-09, N=1001
  Estimated time remaining to complete simulation: 4 hours, 30 minutes, 5 seconds
  Estimated time remaining to next output: 1 minutes, 54 seconds
Output 859/1000: t=85800.0 yr, dE/E0=5.37e-09, N=1001
  Estimated time remaining to complete simulation: 4 hours, 28 minutes, 8 seconds
  Estimated time remaining to next output: 1 minutes, 54 seconds
Output 860/1000: t=85900.0 yr, dE/E0=5.40e-09, N=1001
  Estimated time remaining to complete simulation: 4 hours, 26 minutes, 8 seconds
  Estimated time remaining to next output: 1 minutes, 54 seconds
Output 861/1000: t=86000.0 yr, dE/E0=5.33e-09, N=1001
  Estimated time remaining to complete simulation: 4 hours, 24 minutes, 11 seconds
  Estimated time remaining to next output: 1 minutes, 54 seconds
Output 862/1000: t=86100.0 yr, dE/E0=5.26e-09, N=1001
  Estimated time remaining to complete simulation: 4 hours, 22 minutes, 11 seconds
  Estimated time remaining to next output: 1 minutes, 53 seconds
Output 863/1000: t=86200.0 yr, dE/E0=5.40e-09, N=1001
  Estimated time remaining to complete simulation: 4 hours, 20 minutes, 13 seconds
  Estimated time remaining to next output: 1 minutes, 53 seconds
Output 864/1000: t=86300.0 yr, dE/E0=5.51e-09, N=1001
  Estimated time remaining to complete simulation: 4 hours, 18 minutes, 13 seconds
  Estimated time remaining to next output: 1 minutes, 53 seconds
Output 865/1000: t=86400.0 yr, dE/E0=5.50e-09, N=1001
  Estimated time remaining to complete simulation: 4 hours, 16 minutes, 14 seconds
  Estimated time remaining to next output: 1 minutes, 53 seconds
Output 866/1000: t=86500.0 yr, dE/E0=5.32e-09, N=1001
  Estimated time remaining to complete simulation: 4 hours, 14 minutes, 14 seconds
  Estimated time remaining to next output: 1 minutes, 53 seconds
Output 867/1000: t=86600.0 yr, dE/E0=5.09e-09, N=1001
  Estimated time remaining to complete simulation: 4 hours, 12 minutes, 21 seconds
  Estimated time remaining to next output: 1 minutes, 53 seconds
Output 868/1000: t=86700.0 yr, dE/E0=5.23e-09, N=1001
  Estimated time remaining to complete simulation: 4 hours, 10 minutes, 25 seconds
  Estimated time remaining to next output: 1 minutes, 53 seconds
Output 869/1000: t=86800.0 yr, dE/E0=5.11e-09, N=1001
  Estimated time remaining to complete simulation: 4 hours, 8 minutes, 26 seconds
  Estimated time remaining to next output: 1 minutes, 53 seconds
Output 870/1000: t=86900.0 yr, dE/E0=5.18e-09, N=1001
  Estimated time remaining to complete simulation: 4 hours, 6 minutes, 30 seconds
  Estimated time remaining to next output: 1 minutes, 53 seconds
Output 871/1000: t=87000.0 yr, dE/E0=5.37e-09, N=1001
  Estimated time remaining to complete simulation: 4 hours, 4 minutes, 34 seconds
  Estimated time remaining to next output: 1 minutes, 53 seconds
Output 872/1000: t=87100.0 yr, dE/E0=5.30e-09, N=1001
  Estimated time remaining to complete simulation: 4 hours, 2 minutes, 34 seconds
  Estimated time remaining to next output: 1 minutes, 53 seconds
Output 873/1000: t=87200.0 yr, dE/E0=5.32e-09, N=1001
  Estimated time remaining to complete simulation: 4 hours, 36 seconds
  Estimated time remaining to next output: 1 minutes, 53 seconds
Output 874/1000: t=87300.0 yr, dE/E0=5.38e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 58 minutes, 39 seconds
  Estimated time remaining to next output: 1 minutes, 53 seconds
Output 875/1000: t=87400.0 yr, dE/E0=5.40e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 56 minutes, 43 seconds
  Estimated time remaining to next output: 1 minutes, 53 seconds
Output 876/1000: t=87500.0 yr, dE/E0=5.36e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 54 minutes, 46 seconds
  Estimated time remaining to next output: 1 minutes, 53 seconds
Output 877/1000: t=87600.0 yr, dE/E0=5.38e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 52 minutes, 50 seconds
  Estimated time remaining to next output: 1 minutes, 53 seconds
Output 878/1000: t=87700.0 yr, dE/E0=5.39e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 50 minutes, 53 seconds
  Estimated time remaining to next output: 1 minutes, 53 seconds
Output 879/1000: t=87800.0 yr, dE/E0=5.50e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 48 minutes, 57 seconds
  Estimated time remaining to next output: 1 minutes, 53 seconds
Output 880/1000: t=87900.0 yr, dE/E0=5.45e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 46 minutes, 58 seconds
  Estimated time remaining to next output: 1 minutes, 53 seconds
Output 881/1000: t=88000.0 yr, dE/E0=5.44e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 45 minutes, 1 seconds
  Estimated time remaining to next output: 1 minutes, 53 seconds
Output 882/1000: t=88100.0 yr, dE/E0=5.32e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 43 minutes, 3 seconds
  Estimated time remaining to next output: 1 minutes, 53 seconds
Output 883/1000: t=88200.0 yr, dE/E0=5.07e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 41 minutes, 5 seconds
  Estimated time remaining to next output: 1 minutes, 53 seconds
Output 884/1000: t=88300.0 yr, dE/E0=5.00e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 39 minutes, 7 seconds
  Estimated time remaining to next output: 1 minutes, 53 seconds
Output 885/1000: t=88400.0 yr, dE/E0=5.13e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 37 minutes, 10 seconds
  Estimated time remaining to next output: 1 minutes, 53 seconds
Output 886/1000: t=88500.0 yr, dE/E0=5.22e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 35 minutes, 13 seconds
  Estimated time remaining to next output: 1 minutes, 53 seconds
Output 887/1000: t=88600.0 yr, dE/E0=5.34e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 33 minutes, 17 seconds
  Estimated time remaining to next output: 1 minutes, 53 seconds
Output 888/1000: t=88700.0 yr, dE/E0=5.44e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 31 minutes, 22 seconds
  Estimated time remaining to next output: 1 minutes, 53 seconds
Output 889/1000: t=88800.0 yr, dE/E0=5.50e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 29 minutes, 25 seconds
  Estimated time remaining to next output: 1 minutes, 53 seconds
Output 890/1000: t=88900.0 yr, dE/E0=5.32e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 27 minutes, 29 seconds
  Estimated time remaining to next output: 1 minutes, 53 seconds
Output 891/1000: t=89000.0 yr, dE/E0=5.03e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 25 minutes, 33 seconds
  Estimated time remaining to next output: 1 minutes, 53 seconds
Output 892/1000: t=89100.0 yr, dE/E0=5.16e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 23 minutes, 35 seconds
  Estimated time remaining to next output: 1 minutes, 53 seconds
Output 893/1000: t=89200.0 yr, dE/E0=5.28e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 21 minutes, 40 seconds
  Estimated time remaining to next output: 1 minutes, 53 seconds
Output 894/1000: t=89300.0 yr, dE/E0=5.66e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 19 minutes, 44 seconds
  Estimated time remaining to next output: 1 minutes, 53 seconds
Output 895/1000: t=89400.0 yr, dE/E0=5.57e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 17 minutes, 48 seconds
  Estimated time remaining to next output: 1 minutes, 53 seconds
Output 896/1000: t=89500.0 yr, dE/E0=5.60e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 15 minutes, 52 seconds
  Estimated time remaining to next output: 1 minutes, 53 seconds
Output 897/1000: t=89600.0 yr, dE/E0=5.55e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 13 minutes, 57 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 898/1000: t=89700.0 yr, dE/E0=5.46e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 12 minutes, 3 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 899/1000: t=89800.0 yr, dE/E0=5.18e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 10 minutes, 11 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 900/1000: t=89900.0 yr, dE/E0=4.73e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 8 minutes, 17 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 901/1000: t=90000.0 yr, dE/E0=4.61e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 6 minutes, 20 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 902/1000: t=90100.0 yr, dE/E0=4.80e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 4 minutes, 27 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 903/1000: t=90200.0 yr, dE/E0=5.17e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 2 minutes, 32 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 904/1000: t=90300.0 yr, dE/E0=5.63e-09, N=1001
  Estimated time remaining to complete simulation: 3 hours, 35 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 905/1000: t=90400.0 yr, dE/E0=5.52e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 58 minutes, 41 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 906/1000: t=90500.0 yr, dE/E0=5.14e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 56 minutes, 45 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 907/1000: t=90600.0 yr, dE/E0=4.84e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 54 minutes, 50 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 908/1000: t=90700.0 yr, dE/E0=4.90e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 52 minutes, 57 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 909/1000: t=90800.0 yr, dE/E0=5.10e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 51 minutes, 6 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 910/1000: t=90900.0 yr, dE/E0=5.31e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 49 minutes, 11 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 911/1000: t=91000.0 yr, dE/E0=5.38e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 47 minutes, 16 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 912/1000: t=91100.0 yr, dE/E0=5.38e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 45 minutes, 23 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 913/1000: t=91200.0 yr, dE/E0=5.34e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 43 minutes, 29 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 914/1000: t=91300.0 yr, dE/E0=5.34e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 41 minutes, 41 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 915/1000: t=91400.0 yr, dE/E0=5.40e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 39 minutes, 48 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 916/1000: t=91500.0 yr, dE/E0=5.07e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 37 minutes, 53 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 917/1000: t=91600.0 yr, dE/E0=5.15e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 36 minutes, 1 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 918/1000: t=91700.0 yr, dE/E0=5.44e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 34 minutes, 11 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 919/1000: t=91800.0 yr, dE/E0=5.62e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 32 minutes, 20 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 920/1000: t=91900.0 yr, dE/E0=5.60e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 30 minutes, 28 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 921/1000: t=92000.0 yr, dE/E0=5.56e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 28 minutes, 34 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 922/1000: t=92100.0 yr, dE/E0=5.37e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 26 minutes, 40 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 923/1000: t=92200.0 yr, dE/E0=5.14e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 24 minutes, 48 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 924/1000: t=92300.0 yr, dE/E0=5.05e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 22 minutes, 54 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 925/1000: t=92400.0 yr, dE/E0=5.03e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 21 minutes, 1 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 926/1000: t=92500.0 yr, dE/E0=5.28e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 19 minutes, 7 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 927/1000: t=92600.0 yr, dE/E0=5.50e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 17 minutes, 14 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 928/1000: t=92700.0 yr, dE/E0=5.50e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 15 minutes, 23 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 929/1000: t=92800.0 yr, dE/E0=5.44e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 13 minutes, 32 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 930/1000: t=92900.0 yr, dE/E0=5.49e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 11 minutes, 42 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 931/1000: t=93000.0 yr, dE/E0=5.56e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 9 minutes, 49 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 932/1000: t=93100.0 yr, dE/E0=5.50e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 7 minutes, 57 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 933/1000: t=93200.0 yr, dE/E0=5.16e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 6 minutes, 4 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 934/1000: t=93300.0 yr, dE/E0=4.82e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 4 minutes, 12 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 935/1000: t=93400.0 yr, dE/E0=4.91e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 2 minutes, 19 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 936/1000: t=93500.0 yr, dE/E0=5.05e-09, N=1001
  Estimated time remaining to complete simulation: 2 hours, 26 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 937/1000: t=93600.0 yr, dE/E0=4.89e-09, N=1001
  Estimated time remaining to complete simulation: 1 hours, 58 minutes, 33 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 938/1000: t=93700.0 yr, dE/E0=4.98e-09, N=1001
  Estimated time remaining to complete simulation: 1 hours, 56 minutes, 40 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 939/1000: t=93800.0 yr, dE/E0=5.10e-09, N=1001
  Estimated time remaining to complete simulation: 1 hours, 54 minutes, 49 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 940/1000: t=93900.0 yr, dE/E0=5.21e-09, N=1001
  Estimated time remaining to complete simulation: 1 hours, 52 minutes, 57 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 941/1000: t=94000.0 yr, dE/E0=5.40e-09, N=1001
  Estimated time remaining to complete simulation: 1 hours, 51 minutes, 3 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 942/1000: t=94100.0 yr, dE/E0=5.47e-09, N=1001
  Estimated time remaining to complete simulation: 1 hours, 49 minutes, 9 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 943/1000: t=94200.0 yr, dE/E0=5.54e-09, N=1001
  Estimated time remaining to complete simulation: 1 hours, 47 minutes, 16 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 944/1000: t=94300.0 yr, dE/E0=5.30e-09, N=1001
  Estimated time remaining to complete simulation: 1 hours, 45 minutes, 22 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 945/1000: t=94400.0 yr, dE/E0=5.15e-09, N=1001
  Estimated time remaining to complete simulation: 1 hours, 43 minutes, 28 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 946/1000: t=94500.0 yr, dE/E0=5.12e-09, N=1001
  Estimated time remaining to complete simulation: 1 hours, 41 minutes, 34 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 947/1000: t=94600.0 yr, dE/E0=5.26e-09, N=1001
  Estimated time remaining to complete simulation: 1 hours, 39 minutes, 40 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 948/1000: t=94700.0 yr, dE/E0=5.34e-09, N=1001
  Estimated time remaining to complete simulation: 1 hours, 37 minutes, 47 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 949/1000: t=94800.0 yr, dE/E0=5.36e-09, N=1001
  Estimated time remaining to complete simulation: 1 hours, 35 minutes, 55 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 950/1000: t=94900.0 yr, dE/E0=5.35e-09, N=1001
  Estimated time remaining to complete simulation: 1 hours, 34 minutes, 2 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 951/1000: t=95000.0 yr, dE/E0=5.34e-09, N=1001
  Estimated time remaining to complete simulation: 1 hours, 32 minutes, 8 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 952/1000: t=95100.0 yr, dE/E0=5.14e-09, N=1001
  Estimated time remaining to complete simulation: 1 hours, 30 minutes, 14 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 953/1000: t=95200.0 yr, dE/E0=5.07e-09, N=1001
  Estimated time remaining to complete simulation: 1 hours, 28 minutes, 20 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 954/1000: t=95300.0 yr, dE/E0=5.18e-09, N=1001
  Estimated time remaining to complete simulation: 1 hours, 26 minutes, 26 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 955/1000: t=95400.0 yr, dE/E0=5.14e-09, N=1001
  Estimated time remaining to complete simulation: 1 hours, 24 minutes, 32 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 956/1000: t=95500.0 yr, dE/E0=5.20e-09, N=1001
  Estimated time remaining to complete simulation: 1 hours, 22 minutes, 39 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 957/1000: t=95600.0 yr, dE/E0=5.22e-09, N=1001
  Estimated time remaining to complete simulation: 1 hours, 20 minutes, 45 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 958/1000: t=95700.0 yr, dE/E0=5.29e-09, N=1001
  Estimated time remaining to complete simulation: 1 hours, 18 minutes, 52 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 959/1000: t=95800.0 yr, dE/E0=5.33e-09, N=1001
  Estimated time remaining to complete simulation: 1 hours, 17 minutes
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 960/1000: t=95900.0 yr, dE/E0=5.39e-09, N=1001
  Estimated time remaining to complete simulation: 1 hours, 15 minutes, 8 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 961/1000: t=96000.0 yr, dE/E0=5.47e-09, N=1001
  Estimated time remaining to complete simulation: 1 hours, 13 minutes, 15 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 962/1000: t=96100.0 yr, dE/E0=5.53e-09, N=1001
  Estimated time remaining to complete simulation: 1 hours, 11 minutes, 21 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 963/1000: t=96200.0 yr, dE/E0=5.37e-09, N=1001
  Estimated time remaining to complete simulation: 1 hours, 9 minutes, 27 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 964/1000: t=96300.0 yr, dE/E0=5.16e-09, N=1001
  Estimated time remaining to complete simulation: 1 hours, 7 minutes, 35 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 965/1000: t=96400.0 yr, dE/E0=5.22e-09, N=1001
  Estimated time remaining to complete simulation: 1 hours, 5 minutes, 41 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 966/1000: t=96500.0 yr, dE/E0=5.36e-09, N=1001
  Estimated time remaining to complete simulation: 1 hours, 3 minutes, 47 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 967/1000: t=96600.0 yr, dE/E0=5.63e-09, N=1001
  Estimated time remaining to complete simulation: 1 hours, 1 minutes, 54 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 968/1000: t=96700.0 yr, dE/E0=5.55e-09, N=1001
  Estimated time remaining to complete simulation: 1 hours
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 969/1000: t=96800.0 yr, dE/E0=5.35e-09, N=1001
  Estimated time remaining to complete simulation: 58 minutes, 7 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 970/1000: t=96900.0 yr, dE/E0=5.25e-09, N=1001
  Estimated time remaining to complete simulation: 56 minutes, 14 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 971/1000: t=97000.0 yr, dE/E0=5.25e-09, N=1001
  Estimated time remaining to complete simulation: 54 minutes, 21 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 972/1000: t=97100.0 yr, dE/E0=4.99e-09, N=1001
  Estimated time remaining to complete simulation: 52 minutes, 28 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 973/1000: t=97200.0 yr, dE/E0=4.86e-09, N=1001
  Estimated time remaining to complete simulation: 50 minutes, 35 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 974/1000: t=97300.0 yr, dE/E0=4.95e-09, N=1001
  Estimated time remaining to complete simulation: 48 minutes, 42 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 975/1000: t=97400.0 yr, dE/E0=5.30e-09, N=1001
  Estimated time remaining to complete simulation: 46 minutes, 49 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 976/1000: t=97500.0 yr, dE/E0=5.44e-09, N=1001
  Estimated time remaining to complete simulation: 44 minutes, 55 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 977/1000: t=97600.0 yr, dE/E0=5.50e-09, N=1001
  Estimated time remaining to complete simulation: 43 minutes, 2 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 978/1000: t=97700.0 yr, dE/E0=5.28e-09, N=1001
  Estimated time remaining to complete simulation: 41 minutes, 9 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 979/1000: t=97800.0 yr, dE/E0=5.29e-09, N=1001
  Estimated time remaining to complete simulation: 39 minutes, 17 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 980/1000: t=97900.0 yr, dE/E0=5.25e-09, N=1001
  Estimated time remaining to complete simulation: 37 minutes, 24 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 981/1000: t=98000.0 yr, dE/E0=5.15e-09, N=1001
  Estimated time remaining to complete simulation: 35 minutes, 31 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 982/1000: t=98100.0 yr, dE/E0=5.13e-09, N=1001
  Estimated time remaining to complete simulation: 33 minutes, 38 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 983/1000: t=98200.0 yr, dE/E0=5.38e-09, N=1001
  Estimated time remaining to complete simulation: 31 minutes, 45 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 984/1000: t=98300.0 yr, dE/E0=5.36e-09, N=1001
  Estimated time remaining to complete simulation: 29 minutes, 53 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 985/1000: t=98400.0 yr, dE/E0=5.30e-09, N=1001
  Estimated time remaining to complete simulation: 28 minutes
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 986/1000: t=98500.0 yr, dE/E0=5.23e-09, N=1001
  Estimated time remaining to complete simulation: 26 minutes, 8 seconds
  Estimated time remaining to next output: 1 minutes, 52 seconds
Output 987/1000: t=98600.0 yr, dE/E0=5.18e-09, N=1001
  Estimated time remaining to complete simulation: 24 minutes, 15 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 988/1000: t=98700.0 yr, dE/E0=5.33e-09, N=1001
  Estimated time remaining to complete simulation: 22 minutes, 23 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 989/1000: t=98800.0 yr, dE/E0=5.45e-09, N=1001
  Estimated time remaining to complete simulation: 20 minutes, 31 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 990/1000: t=98900.0 yr, dE/E0=5.52e-09, N=1001
  Estimated time remaining to complete simulation: 18 minutes, 38 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 991/1000: t=99000.0 yr, dE/E0=5.58e-09, N=1001
  Estimated time remaining to complete simulation: 16 minutes, 46 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 992/1000: t=99100.0 yr, dE/E0=5.47e-09, N=1001
  Estimated time remaining to complete simulation: 14 minutes, 54 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 993/1000: t=99200.0 yr, dE/E0=5.23e-09, N=1001
  Estimated time remaining to complete simulation: 13 minutes, 2 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 994/1000: t=99300.0 yr, dE/E0=4.77e-09, N=1001
  Estimated time remaining to complete simulation: 11 minutes, 10 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 995/1000: t=99400.0 yr, dE/E0=4.92e-09, N=1001
  Estimated time remaining to complete simulation: 9 minutes, 18 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 996/1000: t=99500.0 yr, dE/E0=4.93e-09, N=1001
  Estimated time remaining to complete simulation: 7 minutes, 26 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 997/1000: t=99600.0 yr, dE/E0=5.20e-09, N=1001
  Estimated time remaining to complete simulation: 5 minutes, 34 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 998/1000: t=99700.0 yr, dE/E0=5.62e-09, N=1001
  Estimated time remaining to complete simulation: 3 minutes, 43 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 999/1000: t=99800.0 yr, dE/E0=5.32e-09, N=1001
  Estimated time remaining to complete simulation: 1 minutes, 51 seconds
  Estimated time remaining to next output: 1 minutes, 51 seconds
Output 1000/1000: t=99900.0 yr, dE/E0=5.27e-09, N=1001
  Estimated time remaining to complete simulation: 0 seconds
Output 1001/1000: t=100000.0 yr, dE/E0=5.13e-09, N=1001
  Estimated time remaining to complete simulation: -1 months, 4 weeks, 1 days, 23 hours, 58 minutes, 9 seconds

Simulation complete.
Total runtime: 1 days, 7 hours, 56 seconds
Saved archive: outputs/Sim_1000MP_100thouyr_dohnanyi/Sim_1000MP_100thouyr_dohnanyi.bin
Number of snapshots saved: 1001
Archive time range: 0.000e+00 yr to 1.000e+05 yr
Loaded snapshot table from archive.
role
massive_planetesimal    1000
star                       1
Name: count, dtype: int64
Saved: outputs/Sim_1000MP_100thouyr_dohnanyi/figures/survival_fraction_vs_time.png
Saved: outputs/Sim_1000MP_100thouyr_dohnanyi/figures/mean_semimajor_axis_vs_time.png
Saved: outputs/Sim_1000MP_100thouyr_dohnanyi/figures/mean_eccentricity_vs_time.png
Saved: outputs/Sim_1000MP_100thouyr_dohnanyi/figures/rms_eccentricity_vs_time.png
Saved: outputs/Sim_1000MP_100thouyr_dohnanyi/figures/rms_inclination_vs_time.png
Saved: outputs/Sim_1000MP_100thouyr_dohnanyi/figures/a_vs_e_initial_final.png
Saved: outputs/Sim_1000MP_100thouyr_dohnanyi/figures/a_vs_i_initial_final.png
Inner plotted edge = 95.00 AU
Outer plotted edge = 104.99 AU
Saved: outputs/Sim_1000MP_100thouyr_dohnanyi/figures/xy_initial_final.png
All summary figures saved.
```
