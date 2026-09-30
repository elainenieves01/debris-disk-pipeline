# SS_800MP_10Myr_1Mearth_slopeq4.5 — Simulation Report

Config file: `config/SS_800MP_10Myr_1Mearth_slopeq4.5.yaml`
Archive file: `outputs/SS_800MP_10Myr_1Mearth_slopeq4.5/SS_800MP_10Myr_1Mearth_slopeq4.5.bin`

## Provenance

- Run UUID: `351e0400-aafa-41bb-b829-5a1cc2003e04`
- Created: 2026-09-25T15:16:17+00:00
- Finished: 2026-09-30T13:14:04+00:00
- Wall runtime: 424664.4 s
- Outcome: completed
- Command: `src/simulation/run_simulation.py config/SS_800MP_10Myr_1Mearth_slopeq4.5.yaml`
- Git: not available (run from a non-repo checkout)
- Software: python 3.12.14, rebound 5.0.0, numpy 2.4.6, pandas 3.0.3, matplotlib 3.10.9, pyyaml 6.0.3
- Frozen config: `config.yaml` (this directory)
- Full environment: `environment.txt` (this directory)

## Simulation
- Name: SS_800MP_10Myr_1Mearth_slopeq4.5
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
- Mass-assignment method (config): loaded from CSV (mode=csv): variable=radius, path=src/mass_models/cascade_selection_1000km_drop100_800keep_1Mearth/slope_q4.5/selected.csv, slope=4.5 (radii/masses read verbatim from file; disk mass computed from file, not split by a power law)
- **Mass is NOT uniform** across the 800 massive planetesimals:
  - min / median / max: 1.149457e-09 / 2.323641e-09 / 1.638534e-08 Msun
  - min / median / max: 3.827071e-04 / 7.736471e-04 / 5.455433e-03 Earth masses
  - total disk mass: 1.000000e+00 Earth masses

## Test Particles
- N: 0
- Distribution: uniform

## Run Summary (from archive)
- Initial particle count: 801
- Final particle count: 801
- Particles lost (escaped / unbound / other removal): 0
- Archive time range: 0.000000e+00 to 1.000000e+07
- Number of snapshots: 1001

## Terminal Output

```
Saving SimulationArchive to: outputs/SS_800MP_10Myr_1Mearth_slopeq4.5/SS_800MP_10Myr_1Mearth_slopeq4.5.bin
No existing dump_data.json found; starting fresh run.

No giant planet: integrating the disk around the star alone.
  Timestep: 9.259630e+01 (0.1 x circular period at a=95 (disk inner edge) = 9.259630e+02)

Massive planetesimal mass setup:
  Mode: distribution/csv  (planetesimal radii loaded from CSV; disk mass computed from file)
  Number of planetesimals: 800
  Mass spectrum: loaded from CSV (/hadoop_data/home/elaine.nieves/debris-disk-pipeline/src/mass_models/cascade_selection_1000km_drop100_800keep_1Mearth/slope_q4.5/selected.csv), slope=4.5, realized radius range [11.690, 22.715] km
  Per-MP mass (Earth masses): min=3.827071e-04 / median=7.736471e-04 / max=5.455433e-03
  Per-MP diameter (km, uniform sphere, rho = 1 g/cm**3): min=23.380 / median=27.878 / max=45.429
  Total disk mass: 1.000000e+00 Earth masses (3.003490e-06 Msun)
Saved: outputs/SS_800MP_10Myr_1Mearth_slopeq4.5/distribution.csv
Saved: outputs/SS_800MP_10Myr_1Mearth_slopeq4.5/figures/dohnanyi_per_particle.png
Saved: outputs/SS_800MP_10Myr_1Mearth_slopeq4.5/figures/dohnanyi_differential_histogram.png
Saved: outputs/SS_800MP_10Myr_1Mearth_slopeq4.5/figures/count_vs_mass_histogram.png
Saved: outputs/SS_800MP_10Myr_1Mearth_slopeq4.5/figures/count_vs_radius_histogram.png

Stirrer-coverage check (Krivov & Booth 2018: N x delta_af >= delta_a):
  Stirrers inside the belt [95, 105]: N = 800
  delta_af = 8 sqrt(3) h_M a_M:  mean = 1.393839e+00, sum over stirrers = 1.115071e+03
  Belt width delta_a = 1.000000e+01
  Coverage ratio (sum delta_af / delta_a) = 111.507
  OK: stirrer feeding zones span the belt.

Beginning the main integration
Output 1/1000: t=0.0 yr, dE/E0=0.00e+00, N=801
  Estimated time remaining to complete simulation: 1 minutes, 6 seconds
  Estimated time remaining to next output: 0 seconds
Output 2/1000: t=10000.0 yr, dE/E0=1.53e-05, N=801
  Estimated time remaining to complete simulation: 5 months, 1 weeks, 2 days, 4 hours, 22 minutes, 36 seconds
  Estimated time remaining to next output: 3 hours, 49 minutes, 40 seconds
Output 3/1000: t=20000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 7 months, 2 days, 4 hours, 35 minutes, 16 seconds
  Estimated time remaining to next output: 5 hours, 6 minutes, 28 seconds
Output 4/1000: t=30000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 5 months, 2 weeks, 2 days, 21 hours, 15 minutes, 24 seconds
  Estimated time remaining to next output: 4 hours, 1 minutes, 16 seconds
Output 5/1000: t=40000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 4 months, 2 weeks, 2 days, 6 hours, 45 minutes, 5 seconds
  Estimated time remaining to next output: 3 hours, 17 minutes, 13 seconds
Output 6/1000: t=50000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 months, 3 weeks, 4 days, 10 hours, 32 minutes, 11 seconds
  Estimated time remaining to next output: 2 hours, 47 minutes, 14 seconds
Output 7/1000: t=60000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 months, 1 weeks, 3 days, 3 minutes, 44 seconds
  Estimated time remaining to next output: 2 hours, 25 minutes, 1 seconds
Output 8/1000: t=70000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 months, 4 weeks, 9 hours, 36 minutes, 51 seconds
  Estimated time remaining to next output: 2 hours, 8 minutes, 19 seconds
Output 9/1000: t=80000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 months, 2 weeks, 5 days, 2 hours, 26 minutes, 23 seconds
  Estimated time remaining to next output: 1 hours, 54 minutes, 56 seconds
Output 10/1000: t=90000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 months, 1 weeks, 4 days, 18 hours, 6 minutes, 18 seconds
  Estimated time remaining to next output: 1 hours, 44 minutes, 22 seconds
Output 11/1000: t=100000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 months, 5 days, 16 hours, 56 minutes, 11 seconds
  Estimated time remaining to next output: 1 hours, 35 minutes, 40 seconds
Output 12/1000: t=110000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 months, 1 days, 1 hours, 5 minutes, 43 seconds
  Estimated time remaining to next output: 1 hours, 28 minutes, 58 seconds
Output 13/1000: t=120000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 months, 3 weeks, 6 days, 6 hours, 25 minutes, 54 seconds
  Estimated time remaining to next output: 1 hours, 23 minutes, 33 seconds
Output 14/1000: t=130000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 months, 3 weeks, 2 days, 16 hours, 8 minutes, 41 seconds
  Estimated time remaining to next output: 1 hours, 18 minutes, 23 seconds
Output 15/1000: t=140000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 months, 2 weeks, 6 days, 13 hours, 17 minutes, 14 seconds
  Estimated time remaining to next output: 1 hours, 13 minutes, 54 seconds
Output 16/1000: t=150000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 months, 2 weeks, 3 days, 16 hours, 45 minutes, 57 seconds
  Estimated time remaining to next output: 1 hours, 9 minutes, 48 seconds
Output 17/1000: t=160000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 months, 2 weeks, 1 days, 2 hours, 27 minutes, 17 seconds
  Estimated time remaining to next output: 1 hours, 6 minutes, 4 seconds
Output 18/1000: t=170000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 months, 1 weeks, 5 days, 19 hours, 4 minutes, 34 seconds
  Estimated time remaining to next output: 1 hours, 2 minutes, 45 seconds
Output 19/1000: t=180000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 months, 1 weeks, 3 days, 17 hours, 3 minutes, 15 seconds
  Estimated time remaining to next output: 59 minutes, 45 seconds
Output 20/1000: t=190000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 months, 1 weeks, 1 days, 19 hours, 56 minutes, 58 seconds
  Estimated time remaining to next output: 57 minutes, 3 seconds
Output 21/1000: t=200000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 months, 1 weeks, 2 hours, 49 minutes, 44 seconds
  Estimated time remaining to next output: 54 minutes, 35 seconds
Output 22/1000: t=210000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 months, 5 days, 13 hours, 57 minutes, 17 seconds
  Estimated time remaining to next output: 52 minutes, 23 seconds
Output 23/1000: t=220000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 months, 4 days, 3 hours, 52 minutes, 5 seconds
  Estimated time remaining to next output: 50 minutes, 21 seconds
Output 24/1000: t=230000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 months, 2 days, 20 hours, 31 minutes, 9 seconds
  Estimated time remaining to next output: 48 minutes, 28 seconds
Output 25/1000: t=240000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 months, 1 days, 16 hours, 14 minutes, 46 seconds
  Estimated time remaining to next output: 46 minutes, 47 seconds
Output 26/1000: t=250000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 months, 14 hours, 19 minutes, 27 seconds
  Estimated time remaining to next output: 45 minutes, 14 seconds
Output 27/1000: t=260000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 4 weeks, 1 days, 15 hours, 10 minutes, 46 seconds
  Estimated time remaining to next output: 43 minutes, 51 seconds
Output 28/1000: t=270000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 4 weeks, 16 hours, 23 minutes, 20 seconds
  Estimated time remaining to next output: 42 minutes, 29 seconds
Output 29/1000: t=280000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 weeks, 6 days, 19 hours, 20 minutes, 20 seconds
  Estimated time remaining to next output: 41 minutes, 14 seconds
Output 30/1000: t=290000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 weeks, 5 days, 23 hours, 35 minutes, 15 seconds
  Estimated time remaining to next output: 40 minutes, 3 seconds
Output 31/1000: t=300000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 weeks, 5 days, 5 hours, 21 minutes, 56 seconds
  Estimated time remaining to next output: 38 minutes, 58 seconds
Output 32/1000: t=310000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 weeks, 4 days, 11 hours, 50 minutes, 7 seconds
  Estimated time remaining to next output: 37 minutes, 55 seconds
Output 33/1000: t=320000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 weeks, 3 days, 19 hours, 28 minutes, 3 seconds
  Estimated time remaining to next output: 36 minutes, 56 seconds
Output 34/1000: t=330000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 weeks, 3 days, 3 hours, 52 minutes, 50 seconds
  Estimated time remaining to next output: 36 minutes, 1 seconds
Output 35/1000: t=340000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 weeks, 2 days, 13 hours, 22 minutes, 37 seconds
  Estimated time remaining to next output: 35 minutes, 9 seconds
Output 36/1000: t=350000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 weeks, 1 days, 23 hours, 57 minutes, 55 seconds
  Estimated time remaining to next output: 34 minutes, 21 seconds
Output 37/1000: t=360000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 weeks, 1 days, 11 hours, 15 minutes, 4 seconds
  Estimated time remaining to next output: 33 minutes, 35 seconds
Output 38/1000: t=370000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 weeks, 22 hours, 42 minutes, 21 seconds
  Estimated time remaining to next output: 32 minutes, 51 seconds
Output 39/1000: t=380000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 weeks, 10 hours, 59 minutes, 12 seconds
  Estimated time remaining to next output: 32 minutes, 9 seconds
Output 40/1000: t=390000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 weeks, 6 days, 23 hours, 42 minutes, 59 seconds
  Estimated time remaining to next output: 31 minutes, 28 seconds
Output 41/1000: t=400000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 weeks, 6 days, 13 hours, 2 minutes, 56 seconds
  Estimated time remaining to next output: 30 minutes, 50 seconds
Output 42/1000: t=410000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 weeks, 6 days, 2 hours, 59 minutes, 37 seconds
  Estimated time remaining to next output: 30 minutes, 15 seconds
Output 43/1000: t=420000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 weeks, 5 days, 17 hours, 32 minutes, 15 seconds
  Estimated time remaining to next output: 29 minutes, 41 seconds
Output 44/1000: t=430000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 weeks, 5 days, 8 hours, 27 minutes, 36 seconds
  Estimated time remaining to next output: 29 minutes, 9 seconds
Output 45/1000: t=440000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 weeks, 4 days, 23 hours, 39 minutes, 38 seconds
  Estimated time remaining to next output: 28 minutes, 37 seconds
Output 46/1000: t=450000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 weeks, 4 days, 15 hours, 11 minutes, 35 seconds
  Estimated time remaining to next output: 28 minutes, 7 seconds
Output 47/1000: t=460000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 weeks, 4 days, 7 hours, 11 minutes, 59 seconds
  Estimated time remaining to next output: 27 minutes, 39 seconds
Output 48/1000: t=470000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 weeks, 3 days, 23 hours, 22 minutes, 5 seconds
  Estimated time remaining to next output: 27 minutes, 11 seconds
Output 49/1000: t=480000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 weeks, 3 days, 16 hours, 36 seconds
  Estimated time remaining to next output: 26 minutes, 45 seconds
Output 50/1000: t=490000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 weeks, 3 days, 8 hours, 46 minutes, 43 seconds
  Estimated time remaining to next output: 26 minutes, 19 seconds
Output 51/1000: t=500000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 weeks, 3 days, 1 hours, 58 minutes, 22 seconds
  Estimated time remaining to next output: 25 minutes, 55 seconds
Output 52/1000: t=510000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 weeks, 2 days, 19 hours, 16 minutes, 20 seconds
  Estimated time remaining to next output: 25 minutes, 31 seconds
Output 53/1000: t=520000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 weeks, 2 days, 12 hours, 52 minutes, 12 seconds
  Estimated time remaining to next output: 25 minutes, 8 seconds
Output 54/1000: t=530000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 weeks, 2 days, 6 hours, 43 minutes, 42 seconds
  Estimated time remaining to next output: 24 minutes, 46 seconds
Output 55/1000: t=540000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 weeks, 2 days, 50 minutes, 24 seconds
  Estimated time remaining to next output: 24 minutes, 26 seconds
Output 56/1000: t=550000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 weeks, 1 days, 18 hours, 58 minutes, 31 seconds
  Estimated time remaining to next output: 24 minutes, 5 seconds
Output 57/1000: t=560000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 weeks, 1 days, 13 hours, 25 minutes, 8 seconds
  Estimated time remaining to next output: 23 minutes, 45 seconds
Output 58/1000: t=570000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 weeks, 1 days, 8 hours, 13 minutes, 43 seconds
  Estimated time remaining to next output: 23 minutes, 27 seconds
Output 59/1000: t=580000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 weeks, 1 days, 3 hours, 51 minutes, 38 seconds
  Estimated time remaining to next output: 23 minutes, 12 seconds
Output 60/1000: t=590000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 weeks, 23 hours, 3 minutes, 5 seconds
  Estimated time remaining to next output: 22 minutes, 55 seconds
Output 61/1000: t=600000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 weeks, 18 hours, 17 minutes, 7 seconds
  Estimated time remaining to next output: 22 minutes, 38 seconds
Output 62/1000: t=610000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 weeks, 13 hours, 36 minutes, 39 seconds
  Estimated time remaining to next output: 22 minutes, 21 seconds
Output 63/1000: t=620000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 weeks, 9 hours, 3 minutes, 10 seconds
  Estimated time remaining to next output: 22 minutes, 5 seconds
Output 64/1000: t=630000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 weeks, 4 hours, 36 minutes, 51 seconds
  Estimated time remaining to next output: 21 minutes, 50 seconds
Output 65/1000: t=640000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 weeks, 21 minutes, 27 seconds
  Estimated time remaining to next output: 21 minutes, 35 seconds
Output 66/1000: t=650000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 6 days, 20 hours, 6 minutes, 55 seconds
  Estimated time remaining to next output: 21 minutes, 20 seconds
Output 67/1000: t=660000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 6 days, 16 hours, 9 minutes, 27 seconds
  Estimated time remaining to next output: 21 minutes, 6 seconds
Output 68/1000: t=670000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 6 days, 12 hours, 20 minutes, 12 seconds
  Estimated time remaining to next output: 20 minutes, 52 seconds
Output 69/1000: t=680000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 6 days, 8 hours, 35 minutes, 53 seconds
  Estimated time remaining to next output: 20 minutes, 39 seconds
Output 70/1000: t=690000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 6 days, 4 hours, 55 minutes, 12 seconds
  Estimated time remaining to next output: 20 minutes, 26 seconds
Output 71/1000: t=700000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 6 days, 1 hours, 39 minutes, 8 seconds
  Estimated time remaining to next output: 20 minutes, 15 seconds
Output 72/1000: t=710000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 5 days, 22 hours, 32 minutes, 31 seconds
  Estimated time remaining to next output: 20 minutes, 4 seconds
Output 73/1000: t=720000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 5 days, 19 hours, 2 minutes, 3 seconds
  Estimated time remaining to next output: 19 minutes, 52 seconds
Output 74/1000: t=730000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 5 days, 15 hours, 37 minutes, 18 seconds
  Estimated time remaining to next output: 19 minutes, 40 seconds
Output 75/1000: t=740000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 5 days, 12 hours, 31 minutes, 17 seconds
  Estimated time remaining to next output: 19 minutes, 29 seconds
Output 76/1000: t=750000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 5 days, 9 hours, 22 minutes, 56 seconds
  Estimated time remaining to next output: 19 minutes, 18 seconds
Output 77/1000: t=760000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 5 days, 6 hours, 13 minutes, 43 seconds
  Estimated time remaining to next output: 19 minutes, 7 seconds
Output 78/1000: t=770000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 5 days, 3 hours, 11 minutes, 38 seconds
  Estimated time remaining to next output: 18 minutes, 56 seconds
Output 79/1000: t=780000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 5 days, 15 minutes, 1 seconds
  Estimated time remaining to next output: 18 minutes, 46 seconds
Output 80/1000: t=790000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 4 days, 21 hours, 23 minutes, 6 seconds
  Estimated time remaining to next output: 18 minutes, 36 seconds
Output 81/1000: t=800000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 4 days, 18 hours, 30 minutes, 27 seconds
  Estimated time remaining to next output: 18 minutes, 26 seconds
Output 82/1000: t=810000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 4 days, 15 hours, 44 minutes, 23 seconds
  Estimated time remaining to next output: 18 minutes, 17 seconds
Output 83/1000: t=820000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 4 days, 12 hours, 58 minutes, 14 seconds
  Estimated time remaining to next output: 18 minutes, 7 seconds
Output 84/1000: t=830000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 4 days, 10 hours, 19 minutes, 44 seconds
  Estimated time remaining to next output: 17 minutes, 58 seconds
Output 85/1000: t=840000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 4 days, 8 hours, 15 minutes, 28 seconds
  Estimated time remaining to next output: 17 minutes, 51 seconds
Output 86/1000: t=850000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 4 days, 6 hours, 51 minutes, 39 seconds
  Estimated time remaining to next output: 17 minutes, 46 seconds
Output 87/1000: t=860000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 4 days, 5 hours, 37 minutes, 41 seconds
  Estimated time remaining to next output: 17 minutes, 43 seconds
Output 88/1000: t=870000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 4 days, 3 hours, 22 minutes, 52 seconds
  Estimated time remaining to next output: 17 minutes, 35 seconds
Output 89/1000: t=880000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 4 days, 56 minutes, 46 seconds
  Estimated time remaining to next output: 17 minutes, 26 seconds
Output 90/1000: t=890000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 3 days, 22 hours, 56 minutes, 17 seconds
  Estimated time remaining to next output: 17 minutes, 20 seconds
Output 91/1000: t=900000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 3 days, 21 hours, 59 minutes, 5 seconds
  Estimated time remaining to next output: 17 minutes, 17 seconds
Output 92/1000: t=910000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 3 days, 21 hours, 6 minutes, 47 seconds
  Estimated time remaining to next output: 17 minutes, 15 seconds
Output 93/1000: t=920000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 3 days, 20 hours, 17 minutes, 24 seconds
  Estimated time remaining to next output: 17 minutes, 13 seconds
Output 94/1000: t=930000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 3 days, 19 hours, 31 minutes, 15 seconds
  Estimated time remaining to next output: 17 minutes, 11 seconds
Output 95/1000: t=940000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 3 days, 18 hours, 43 minutes, 36 seconds
  Estimated time remaining to next output: 17 minutes, 9 seconds
Output 96/1000: t=950000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 3 days, 17 hours, 48 minutes, 13 seconds
  Estimated time remaining to next output: 17 minutes, 6 seconds
Output 97/1000: t=960000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 3 days, 17 hours, 2 minutes, 52 seconds
  Estimated time remaining to next output: 17 minutes, 4 seconds
Output 98/1000: t=970000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 3 days, 15 hours, 59 minutes, 25 seconds
  Estimated time remaining to next output: 17 minutes, 1 seconds
Output 99/1000: t=980000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 3 days, 15 hours, 7 minutes, 22 seconds
  Estimated time remaining to next output: 16 minutes, 59 seconds
Output 100/1000: t=990000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 3 days, 14 hours, 14 minutes, 45 seconds
  Estimated time remaining to next output: 16 minutes, 56 seconds
Output 101/1000: t=1000000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 3 days, 13 hours, 25 minutes, 19 seconds
  Estimated time remaining to next output: 16 minutes, 54 seconds
Output 102/1000: t=1010000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 3 days, 12 hours, 51 minutes, 12 seconds
  Estimated time remaining to next output: 16 minutes, 53 seconds
Output 103/1000: t=1020000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 3 days, 11 hours, 56 minutes, 2 seconds
  Estimated time remaining to next output: 16 minutes, 51 seconds
Output 104/1000: t=1030000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 3 days, 11 hours, 23 minutes, 30 seconds
  Estimated time remaining to next output: 16 minutes, 50 seconds
Output 105/1000: t=1040000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 3 days, 9 hours, 29 minutes, 40 seconds
  Estimated time remaining to next output: 16 minutes, 43 seconds
Output 106/1000: t=1050000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 3 days, 7 hours, 34 minutes, 24 seconds
  Estimated time remaining to next output: 16 minutes, 36 seconds
Output 107/1000: t=1060000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 3 days, 5 hours, 45 minutes, 42 seconds
  Estimated time remaining to next output: 16 minutes, 30 seconds
Output 108/1000: t=1070000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 3 days, 3 hours, 53 minutes, 45 seconds
  Estimated time remaining to next output: 16 minutes, 24 seconds
Output 109/1000: t=1080000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 3 days, 2 hours, 7 minutes, 13 seconds
  Estimated time remaining to next output: 16 minutes, 18 seconds
Output 110/1000: t=1090000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 3 days, 20 minutes, 24 seconds
  Estimated time remaining to next output: 16 minutes, 12 seconds
Output 111/1000: t=1100000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 2 days, 22 hours, 32 minutes, 52 seconds
  Estimated time remaining to next output: 16 minutes, 5 seconds
Output 112/1000: t=1110000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 2 days, 20 hours, 47 minutes, 35 seconds
  Estimated time remaining to next output: 15 minutes, 59 seconds
Output 113/1000: t=1120000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 2 days, 19 hours, 5 minutes, 13 seconds
  Estimated time remaining to next output: 15 minutes, 54 seconds
Output 114/1000: t=1130000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 2 days, 17 hours, 30 minutes, 34 seconds
  Estimated time remaining to next output: 15 minutes, 48 seconds
Output 115/1000: t=1140000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 2 days, 15 hours, 54 minutes, 49 seconds
  Estimated time remaining to next output: 15 minutes, 43 seconds
Output 116/1000: t=1150000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 2 days, 14 hours, 19 minutes, 6 seconds
  Estimated time remaining to next output: 15 minutes, 37 seconds
Output 117/1000: t=1160000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 2 days, 12 hours, 46 minutes, 58 seconds
  Estimated time remaining to next output: 15 minutes, 32 seconds
Output 118/1000: t=1170000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 2 days, 11 hours, 17 minutes, 41 seconds
  Estimated time remaining to next output: 15 minutes, 27 seconds
Output 119/1000: t=1180000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 2 days, 9 hours, 45 minutes, 9 seconds
  Estimated time remaining to next output: 15 minutes, 22 seconds
Output 120/1000: t=1190000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 2 days, 8 hours, 15 minutes, 41 seconds
  Estimated time remaining to next output: 15 minutes, 17 seconds
Output 121/1000: t=1200000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 2 days, 6 hours, 48 minutes, 34 seconds
  Estimated time remaining to next output: 15 minutes, 12 seconds
Output 122/1000: t=1210000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 2 days, 5 hours, 22 minutes, 3 seconds
  Estimated time remaining to next output: 15 minutes, 7 seconds
Output 123/1000: t=1220000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 2 days, 3 hours, 58 minutes, 43 seconds
  Estimated time remaining to next output: 15 minutes, 2 seconds
Output 124/1000: t=1230000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 2 days, 2 hours, 31 minutes, 42 seconds
  Estimated time remaining to next output: 14 minutes, 58 seconds
Output 125/1000: t=1240000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 2 days, 1 hours, 7 minutes, 47 seconds
  Estimated time remaining to next output: 14 minutes, 53 seconds
Output 126/1000: t=1250000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 1 days, 23 hours, 45 minutes, 8 seconds
  Estimated time remaining to next output: 14 minutes, 48 seconds
Output 127/1000: t=1260000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 1 days, 22 hours, 25 minutes, 14 seconds
  Estimated time remaining to next output: 14 minutes, 44 seconds
Output 128/1000: t=1270000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 1 days, 21 hours, 6 minutes, 53 seconds
  Estimated time remaining to next output: 14 minutes, 39 seconds
Output 129/1000: t=1280000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 1 days, 19 hours, 52 minutes, 18 seconds
  Estimated time remaining to next output: 14 minutes, 35 seconds
Output 130/1000: t=1290000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 1 days, 18 hours, 38 minutes
  Estimated time remaining to next output: 14 minutes, 31 seconds
Output 131/1000: t=1300000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 1 days, 17 hours, 22 minutes, 27 seconds
  Estimated time remaining to next output: 14 minutes, 27 seconds
Output 132/1000: t=1310000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 1 days, 16 hours, 8 minutes, 26 seconds
  Estimated time remaining to next output: 14 minutes, 23 seconds
Output 133/1000: t=1320000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 1 days, 14 hours, 56 minutes, 49 seconds
  Estimated time remaining to next output: 14 minutes, 19 seconds
Output 134/1000: t=1330000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 1 days, 13 hours, 44 minutes, 36 seconds
  Estimated time remaining to next output: 14 minutes, 15 seconds
Output 135/1000: t=1340000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 1 days, 12 hours, 34 minutes, 17 seconds
  Estimated time remaining to next output: 14 minutes, 11 seconds
Output 136/1000: t=1350000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 1 days, 11 hours, 23 minutes, 9 seconds
  Estimated time remaining to next output: 14 minutes, 7 seconds
Output 137/1000: t=1360000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 1 days, 10 hours, 13 minutes, 6 seconds
  Estimated time remaining to next output: 14 minutes, 3 seconds
Output 138/1000: t=1370000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 1 days, 9 hours, 10 minutes, 58 seconds
  Estimated time remaining to next output: 14 minutes
Output 139/1000: t=1380000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 1 days, 8 hours, 1 minutes, 21 seconds
  Estimated time remaining to next output: 13 minutes, 56 seconds
Output 140/1000: t=1390000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 1 days, 6 hours, 54 minutes, 31 seconds
  Estimated time remaining to next output: 13 minutes, 52 seconds
Output 141/1000: t=1400000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 1 days, 5 hours, 49 minutes, 19 seconds
  Estimated time remaining to next output: 13 minutes, 49 seconds
Output 142/1000: t=1410000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 1 days, 4 hours, 49 minutes, 13 seconds
  Estimated time remaining to next output: 13 minutes, 45 seconds
Output 143/1000: t=1420000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 1 days, 3 hours, 45 minutes, 49 seconds
  Estimated time remaining to next output: 13 minutes, 42 seconds
Output 144/1000: t=1430000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 1 days, 2 hours, 41 minutes, 46 seconds
  Estimated time remaining to next output: 13 minutes, 38 seconds
Output 145/1000: t=1440000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 1 days, 1 hours, 41 minutes, 22 seconds
  Estimated time remaining to next output: 13 minutes, 35 seconds
Output 146/1000: t=1450000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 1 days, 41 minutes, 36 seconds
  Estimated time remaining to next output: 13 minutes, 32 seconds
Output 147/1000: t=1460000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 23 hours, 39 minutes
  Estimated time remaining to next output: 13 minutes, 28 seconds
Output 148/1000: t=1470000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 22 hours, 36 minutes, 22 seconds
  Estimated time remaining to next output: 13 minutes, 25 seconds
Output 149/1000: t=1480000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 21 hours, 36 minutes, 22 seconds
  Estimated time remaining to next output: 13 minutes, 22 seconds
Output 150/1000: t=1490000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 20 hours, 34 minutes, 34 seconds
  Estimated time remaining to next output: 13 minutes, 18 seconds
Output 151/1000: t=1500000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 19 hours, 35 minutes, 23 seconds
  Estimated time remaining to next output: 13 minutes, 15 seconds
Output 152/1000: t=1510000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 18 hours, 41 minutes, 48 seconds
  Estimated time remaining to next output: 13 minutes, 12 seconds
Output 153/1000: t=1520000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 17 hours, 43 minutes, 48 seconds
  Estimated time remaining to next output: 13 minutes, 9 seconds
Output 154/1000: t=1530000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 16 hours, 49 minutes, 6 seconds
  Estimated time remaining to next output: 13 minutes, 6 seconds
Output 155/1000: t=1540000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 15 hours, 53 minutes, 56 seconds
  Estimated time remaining to next output: 13 minutes, 3 seconds
Output 156/1000: t=1550000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 14 hours, 57 minutes, 19 seconds
  Estimated time remaining to next output: 13 minutes
Output 157/1000: t=1560000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 14 hours, 4 minutes, 6 seconds
  Estimated time remaining to next output: 12 minutes, 57 seconds
Output 158/1000: t=1570000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 13 hours, 12 minutes, 41 seconds
  Estimated time remaining to next output: 12 minutes, 54 seconds
Output 159/1000: t=1580000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 12 hours, 17 minutes, 41 seconds
  Estimated time remaining to next output: 12 minutes, 51 seconds
Output 160/1000: t=1590000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 11 hours, 24 minutes, 58 seconds
  Estimated time remaining to next output: 12 minutes, 48 seconds
Output 161/1000: t=1600000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 10 hours, 31 minutes, 32 seconds
  Estimated time remaining to next output: 12 minutes, 46 seconds
Output 162/1000: t=1610000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 9 hours, 40 minutes, 18 seconds
  Estimated time remaining to next output: 12 minutes, 43 seconds
Output 163/1000: t=1620000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 9 hours, 14 minutes, 32 seconds
  Estimated time remaining to next output: 12 minutes, 42 seconds
Output 164/1000: t=1630000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 8 hours, 51 minutes, 50 seconds
  Estimated time remaining to next output: 12 minutes, 41 seconds
Output 165/1000: t=1640000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 8 hours, 27 minutes, 49 seconds
  Estimated time remaining to next output: 12 minutes, 40 seconds
Output 166/1000: t=1650000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 7 hours, 58 minutes, 39 seconds
  Estimated time remaining to next output: 12 minutes, 39 seconds
Output 167/1000: t=1660000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 7 hours, 13 minutes, 8 seconds
  Estimated time remaining to next output: 12 minutes, 37 seconds
Output 168/1000: t=1670000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 6 hours, 25 minutes, 21 seconds
  Estimated time remaining to next output: 12 minutes, 34 seconds
Output 169/1000: t=1680000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 5 hours, 49 minutes, 24 seconds
  Estimated time remaining to next output: 12 minutes, 33 seconds
Output 170/1000: t=1690000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 5 hours, 14 minutes, 38 seconds
  Estimated time remaining to next output: 12 minutes, 31 seconds
Output 171/1000: t=1700000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 4 hours, 41 minutes, 27 seconds
  Estimated time remaining to next output: 12 minutes, 29 seconds
Output 172/1000: t=1710000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 4 hours, 7 minutes, 19 seconds
  Estimated time remaining to next output: 12 minutes, 28 seconds
Output 173/1000: t=1720000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 3 hours, 36 minutes, 50 seconds
  Estimated time remaining to next output: 12 minutes, 27 seconds
Output 174/1000: t=1730000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 3 hours, 7 minutes, 1 seconds
  Estimated time remaining to next output: 12 minutes, 25 seconds
Output 175/1000: t=1740000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 2 hours, 31 minutes, 26 seconds
  Estimated time remaining to next output: 12 minutes, 24 seconds
Output 176/1000: t=1750000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 2 hours, 2 minutes, 48 seconds
  Estimated time remaining to next output: 12 minutes, 22 seconds
Output 177/1000: t=1760000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 1 hours, 32 minutes, 3 seconds
  Estimated time remaining to next output: 12 minutes, 21 seconds
Output 178/1000: t=1770000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 1 hours, 22 seconds
  Estimated time remaining to next output: 12 minutes, 20 seconds
Output 179/1000: t=1780000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 28 minutes, 56 seconds
  Estimated time remaining to next output: 12 minutes, 18 seconds
Output 180/1000: t=1790000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 weeks, 37 seconds
  Estimated time remaining to next output: 12 minutes, 17 seconds
Output 181/1000: t=1800000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 6 days, 23 hours, 35 minutes, 45 seconds
  Estimated time remaining to next output: 12 minutes, 16 seconds
Output 182/1000: t=1810000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 6 days, 23 hours, 11 minutes, 57 seconds
  Estimated time remaining to next output: 12 minutes, 15 seconds
Output 183/1000: t=1820000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 6 days, 22 hours, 46 minutes, 20 seconds
  Estimated time remaining to next output: 12 minutes, 14 seconds
Output 184/1000: t=1830000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 6 days, 22 hours, 20 minutes, 3 seconds
  Estimated time remaining to next output: 12 minutes, 13 seconds
Output 185/1000: t=1840000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 6 days, 21 hours, 57 minutes, 22 seconds
  Estimated time remaining to next output: 12 minutes, 13 seconds
Output 186/1000: t=1850000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 6 days, 21 hours, 37 minutes, 3 seconds
  Estimated time remaining to next output: 12 minutes, 12 seconds
Output 187/1000: t=1860000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 6 days, 21 hours, 13 minutes, 48 seconds
  Estimated time remaining to next output: 12 minutes, 11 seconds
Output 188/1000: t=1870000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 6 days, 20 hours, 53 minutes, 20 seconds
  Estimated time remaining to next output: 12 minutes, 11 seconds
Output 189/1000: t=1880000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 6 days, 20 hours, 30 minutes, 3 seconds
  Estimated time remaining to next output: 12 minutes, 10 seconds
Output 190/1000: t=1890000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 6 days, 20 hours, 4 minutes, 43 seconds
  Estimated time remaining to next output: 12 minutes, 9 seconds
Output 191/1000: t=1900000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 6 days, 19 hours, 46 minutes, 48 seconds
  Estimated time remaining to next output: 12 minutes, 8 seconds
Output 192/1000: t=1910000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 6 days, 19 hours, 24 minutes, 5 seconds
  Estimated time remaining to next output: 12 minutes, 8 seconds
Output 193/1000: t=1920000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 6 days, 19 hours, 2 minutes, 14 seconds
  Estimated time remaining to next output: 12 minutes, 7 seconds
Output 194/1000: t=1930000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 6 days, 18 hours, 42 minutes, 57 seconds
  Estimated time remaining to next output: 12 minutes, 6 seconds
Output 195/1000: t=1940000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 6 days, 18 hours, 20 minutes, 17 seconds
  Estimated time remaining to next output: 12 minutes, 5 seconds
Output 196/1000: t=1950000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 6 days, 17 hours, 57 minutes, 14 seconds
  Estimated time remaining to next output: 12 minutes, 5 seconds
Output 197/1000: t=1960000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 6 days, 17 hours, 34 minutes, 36 seconds
  Estimated time remaining to next output: 12 minutes, 4 seconds
Output 198/1000: t=1970000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 6 days, 17 hours, 15 minutes, 33 seconds
  Estimated time remaining to next output: 12 minutes, 3 seconds
Output 199/1000: t=1980000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 6 days, 16 hours, 56 minutes, 7 seconds
  Estimated time remaining to next output: 12 minutes, 3 seconds
Output 200/1000: t=1990000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 6 days, 16 hours, 35 minutes, 56 seconds
  Estimated time remaining to next output: 12 minutes, 2 seconds
Output 201/1000: t=2000000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 6 days, 16 hours, 16 minutes, 28 seconds
  Estimated time remaining to next output: 12 minutes, 2 seconds
Output 202/1000: t=2010000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 6 days, 15 hours, 58 minutes, 6 seconds
  Estimated time remaining to next output: 12 minutes, 1 seconds
Output 203/1000: t=2020000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 6 days, 15 hours, 36 minutes, 5 seconds
  Estimated time remaining to next output: 12 minutes
Output 204/1000: t=2030000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 6 days, 15 hours, 9 minutes, 3 seconds
  Estimated time remaining to next output: 11 minutes, 59 seconds
Output 205/1000: t=2040000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 6 days, 14 hours, 41 minutes, 51 seconds
  Estimated time remaining to next output: 11 minutes, 58 seconds
Output 206/1000: t=2050000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 6 days, 14 hours, 14 minutes, 52 seconds
  Estimated time remaining to next output: 11 minutes, 57 seconds
Output 207/1000: t=2060000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 6 days, 13 hours, 47 minutes, 41 seconds
  Estimated time remaining to next output: 11 minutes, 56 seconds
Output 208/1000: t=2070000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 6 days, 13 hours, 22 minutes, 41 seconds
  Estimated time remaining to next output: 11 minutes, 55 seconds
Output 209/1000: t=2080000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 6 days, 12 hours, 55 minutes, 19 seconds
  Estimated time remaining to next output: 11 minutes, 54 seconds
Output 210/1000: t=2090000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 6 days, 12 hours, 29 minutes, 10 seconds
  Estimated time remaining to next output: 11 minutes, 53 seconds
Output 211/1000: t=2100000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 6 days, 12 hours, 1 minutes, 21 seconds
  Estimated time remaining to next output: 11 minutes, 51 seconds
Output 212/1000: t=2110000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 6 days, 11 hours, 35 minutes, 22 seconds
  Estimated time remaining to next output: 11 minutes, 50 seconds
Output 213/1000: t=2120000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 6 days, 11 hours, 6 minutes, 47 seconds
  Estimated time remaining to next output: 11 minutes, 49 seconds
Output 214/1000: t=2130000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 6 days, 10 hours, 40 minutes, 18 seconds
  Estimated time remaining to next output: 11 minutes, 48 seconds
Output 215/1000: t=2140000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 6 days, 10 hours, 6 minutes, 54 seconds
  Estimated time remaining to next output: 11 minutes, 46 seconds
Output 216/1000: t=2150000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 6 days, 9 hours, 30 minutes, 27 seconds
  Estimated time remaining to next output: 11 minutes, 44 seconds
Output 217/1000: t=2160000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 6 days, 8 hours, 57 minutes, 23 seconds
  Estimated time remaining to next output: 11 minutes, 43 seconds
Output 218/1000: t=2170000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 6 days, 8 hours, 21 minutes, 27 seconds
  Estimated time remaining to next output: 11 minutes, 41 seconds
Output 219/1000: t=2180000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 6 days, 7 hours, 46 minutes, 30 seconds
  Estimated time remaining to next output: 11 minutes, 39 seconds
Output 220/1000: t=2190000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 6 days, 7 hours, 15 minutes, 23 seconds
  Estimated time remaining to next output: 11 minutes, 38 seconds
Output 221/1000: t=2200000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 6 days, 6 hours, 41 minutes, 59 seconds
  Estimated time remaining to next output: 11 minutes, 36 seconds
Output 222/1000: t=2210000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 6 days, 6 hours, 7 minutes, 53 seconds
  Estimated time remaining to next output: 11 minutes, 34 seconds
Output 223/1000: t=2220000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 6 days, 5 hours, 35 minutes, 49 seconds
  Estimated time remaining to next output: 11 minutes, 33 seconds
Output 224/1000: t=2230000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 6 days, 5 hours, 3 minutes, 56 seconds
  Estimated time remaining to next output: 11 minutes, 31 seconds
Output 225/1000: t=2240000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 6 days, 4 hours, 30 minutes, 42 seconds
  Estimated time remaining to next output: 11 minutes, 29 seconds
Output 226/1000: t=2250000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 6 days, 3 hours, 58 minutes, 57 seconds
  Estimated time remaining to next output: 11 minutes, 28 seconds
Output 227/1000: t=2260000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 6 days, 3 hours, 26 minutes, 39 seconds
  Estimated time remaining to next output: 11 minutes, 26 seconds
Output 228/1000: t=2270000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 6 days, 2 hours, 54 minutes, 59 seconds
  Estimated time remaining to next output: 11 minutes, 25 seconds
Output 229/1000: t=2280000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 6 days, 2 hours, 22 minutes, 13 seconds
  Estimated time remaining to next output: 11 minutes, 23 seconds
Output 230/1000: t=2290000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 6 days, 1 hours, 50 minutes, 34 seconds
  Estimated time remaining to next output: 11 minutes, 21 seconds
Output 231/1000: t=2300000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 6 days, 1 hours, 18 minutes, 12 seconds
  Estimated time remaining to next output: 11 minutes, 20 seconds
Output 232/1000: t=2310000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 6 days, 46 minutes, 37 seconds
  Estimated time remaining to next output: 11 minutes, 18 seconds
Output 233/1000: t=2320000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 6 days, 15 minutes, 44 seconds
  Estimated time remaining to next output: 11 minutes, 17 seconds
Output 234/1000: t=2330000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 5 days, 23 hours, 44 minutes, 33 seconds
  Estimated time remaining to next output: 11 minutes, 15 seconds
Output 235/1000: t=2340000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 5 days, 23 hours, 13 minutes, 42 seconds
  Estimated time remaining to next output: 11 minutes, 14 seconds
Output 236/1000: t=2350000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 5 days, 22 hours, 42 minutes, 54 seconds
  Estimated time remaining to next output: 11 minutes, 12 seconds
Output 237/1000: t=2360000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 5 days, 22 hours, 12 minutes, 44 seconds
  Estimated time remaining to next output: 11 minutes, 10 seconds
Output 238/1000: t=2370000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 5 days, 21 hours, 42 minutes, 14 seconds
  Estimated time remaining to next output: 11 minutes, 9 seconds
Output 239/1000: t=2380000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 5 days, 21 hours, 12 minutes, 48 seconds
  Estimated time remaining to next output: 11 minutes, 8 seconds
Output 240/1000: t=2390000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 5 days, 20 hours, 43 minutes, 33 seconds
  Estimated time remaining to next output: 11 minutes, 6 seconds
Output 241/1000: t=2400000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 5 days, 20 hours, 13 minutes, 43 seconds
  Estimated time remaining to next output: 11 minutes, 5 seconds
Output 242/1000: t=2410000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 5 days, 19 hours, 44 minutes, 29 seconds
  Estimated time remaining to next output: 11 minutes, 3 seconds
Output 243/1000: t=2420000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 5 days, 19 hours, 16 minutes, 1 seconds
  Estimated time remaining to next output: 11 minutes, 2 seconds
Output 244/1000: t=2430000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 5 days, 18 hours, 47 minutes, 45 seconds
  Estimated time remaining to next output: 11 minutes
Output 245/1000: t=2440000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 5 days, 18 hours, 18 minutes, 5 seconds
  Estimated time remaining to next output: 10 minutes, 59 seconds
Output 246/1000: t=2450000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 5 days, 17 hours, 51 minutes, 6 seconds
  Estimated time remaining to next output: 10 minutes, 58 seconds
Output 247/1000: t=2460000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 5 days, 17 hours, 22 minutes, 35 seconds
  Estimated time remaining to next output: 10 minutes, 56 seconds
Output 248/1000: t=2470000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 5 days, 16 hours, 55 minutes, 6 seconds
  Estimated time remaining to next output: 10 minutes, 55 seconds
Output 249/1000: t=2480000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 5 days, 16 hours, 27 minutes, 27 seconds
  Estimated time remaining to next output: 10 minutes, 54 seconds
Output 250/1000: t=2490000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 5 days, 16 hours, 1 minutes, 37 seconds
  Estimated time remaining to next output: 10 minutes, 52 seconds
Output 251/1000: t=2500000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 5 days, 15 hours, 34 minutes, 12 seconds
  Estimated time remaining to next output: 10 minutes, 51 seconds
Output 252/1000: t=2510000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 5 days, 15 hours, 6 minutes, 51 seconds
  Estimated time remaining to next output: 10 minutes, 50 seconds
Output 253/1000: t=2520000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 5 days, 14 hours, 39 minutes, 18 seconds
  Estimated time remaining to next output: 10 minutes, 48 seconds
Output 254/1000: t=2530000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 5 days, 14 hours, 11 minutes, 27 seconds
  Estimated time remaining to next output: 10 minutes, 47 seconds
Output 255/1000: t=2540000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 5 days, 13 hours, 45 minutes, 33 seconds
  Estimated time remaining to next output: 10 minutes, 46 seconds
Output 256/1000: t=2550000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 5 days, 13 hours, 19 minutes, 6 seconds
  Estimated time remaining to next output: 10 minutes, 45 seconds
Output 257/1000: t=2560000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 5 days, 12 hours, 51 minutes, 25 seconds
  Estimated time remaining to next output: 10 minutes, 43 seconds
Output 258/1000: t=2570000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 5 days, 12 hours, 24 minutes, 46 seconds
  Estimated time remaining to next output: 10 minutes, 42 seconds
Output 259/1000: t=2580000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 5 days, 11 hours, 59 minutes, 16 seconds
  Estimated time remaining to next output: 10 minutes, 41 seconds
Output 260/1000: t=2590000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 5 days, 11 hours, 47 minutes, 13 seconds
  Estimated time remaining to next output: 10 minutes, 41 seconds
Output 261/1000: t=2600000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 5 days, 11 hours, 32 minutes, 45 seconds
  Estimated time remaining to next output: 10 minutes, 40 seconds
Output 262/1000: t=2610000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 5 days, 11 hours, 22 minutes, 35 seconds
  Estimated time remaining to next output: 10 minutes, 40 seconds
Output 263/1000: t=2620000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 5 days, 11 hours, 10 minutes, 46 seconds
  Estimated time remaining to next output: 10 minutes, 40 seconds
Output 264/1000: t=2630000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 5 days, 10 hours, 56 minutes, 52 seconds
  Estimated time remaining to next output: 10 minutes, 40 seconds
Output 265/1000: t=2640000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 5 days, 10 hours, 42 minutes, 42 seconds
  Estimated time remaining to next output: 10 minutes, 40 seconds
Output 266/1000: t=2650000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 5 days, 10 hours, 31 minutes, 10 seconds
  Estimated time remaining to next output: 10 minutes, 40 seconds
Output 267/1000: t=2660000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 5 days, 10 hours, 18 minutes, 55 seconds
  Estimated time remaining to next output: 10 minutes, 40 seconds
Output 268/1000: t=2670000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 5 days, 10 hours, 7 minutes, 12 seconds
  Estimated time remaining to next output: 10 minutes, 39 seconds
Output 269/1000: t=2680000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 5 days, 9 hours, 53 minutes, 29 seconds
  Estimated time remaining to next output: 10 minutes, 39 seconds
Output 270/1000: t=2690000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 5 days, 9 hours, 43 minutes, 46 seconds
  Estimated time remaining to next output: 10 minutes, 39 seconds
Output 271/1000: t=2700000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 5 days, 9 hours, 34 minutes, 21 seconds
  Estimated time remaining to next output: 10 minutes, 39 seconds
Output 272/1000: t=2710000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 5 days, 9 hours, 27 minutes, 7 seconds
  Estimated time remaining to next output: 10 minutes, 40 seconds
Output 273/1000: t=2720000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 5 days, 9 hours, 14 minutes, 59 seconds
  Estimated time remaining to next output: 10 minutes, 40 seconds
Output 274/1000: t=2730000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 5 days, 9 hours, 1 minutes, 56 seconds
  Estimated time remaining to next output: 10 minutes, 39 seconds
Output 275/1000: t=2740000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 5 days, 8 hours, 48 minutes, 16 seconds
  Estimated time remaining to next output: 10 minutes, 39 seconds
Output 276/1000: t=2750000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 5 days, 8 hours, 36 minutes, 43 seconds
  Estimated time remaining to next output: 10 minutes, 39 seconds
Output 277/1000: t=2760000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 5 days, 8 hours, 23 minutes, 49 seconds
  Estimated time remaining to next output: 10 minutes, 39 seconds
Output 278/1000: t=2770000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 5 days, 8 hours, 11 minutes, 16 seconds
  Estimated time remaining to next output: 10 minutes, 39 seconds
Output 279/1000: t=2780000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 5 days, 8 hours, 50 seconds
  Estimated time remaining to next output: 10 minutes, 39 seconds
Output 280/1000: t=2790000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 5 days, 7 hours, 51 minutes, 33 seconds
  Estimated time remaining to next output: 10 minutes, 39 seconds
Output 281/1000: t=2800000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 5 days, 7 hours, 38 minutes, 32 seconds
  Estimated time remaining to next output: 10 minutes, 39 seconds
Output 282/1000: t=2810000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 5 days, 7 hours, 26 minutes, 56 seconds
  Estimated time remaining to next output: 10 minutes, 39 seconds
Output 283/1000: t=2820000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 5 days, 7 hours, 7 minutes, 13 seconds
  Estimated time remaining to next output: 10 minutes, 38 seconds
Output 284/1000: t=2830000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 5 days, 6 hours, 42 minutes, 52 seconds
  Estimated time remaining to next output: 10 minutes, 37 seconds
Output 285/1000: t=2840000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 5 days, 6 hours, 18 minutes, 51 seconds
  Estimated time remaining to next output: 10 minutes, 35 seconds
Output 286/1000: t=2850000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 5 days, 5 hours, 54 minutes, 24 seconds
  Estimated time remaining to next output: 10 minutes, 34 seconds
Output 287/1000: t=2860000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 5 days, 5 hours, 31 minutes, 16 seconds
  Estimated time remaining to next output: 10 minutes, 33 seconds
Output 288/1000: t=2870000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 5 days, 5 hours, 7 minutes, 12 seconds
  Estimated time remaining to next output: 10 minutes, 32 seconds
Output 289/1000: t=2880000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 5 days, 4 hours, 43 minutes, 36 seconds
  Estimated time remaining to next output: 10 minutes, 31 seconds
Output 290/1000: t=2890000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 5 days, 4 hours, 20 minutes, 49 seconds
  Estimated time remaining to next output: 10 minutes, 30 seconds
Output 291/1000: t=2900000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 5 days, 3 hours, 57 minutes, 41 seconds
  Estimated time remaining to next output: 10 minutes, 29 seconds
Output 292/1000: t=2910000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 5 days, 3 hours, 33 minutes, 9 seconds
  Estimated time remaining to next output: 10 minutes, 28 seconds
Output 293/1000: t=2920000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 5 days, 3 hours, 10 minutes, 4 seconds
  Estimated time remaining to next output: 10 minutes, 27 seconds
Output 294/1000: t=2930000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 5 days, 2 hours, 46 minutes, 38 seconds
  Estimated time remaining to next output: 10 minutes, 26 seconds
Output 295/1000: t=2940000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 5 days, 2 hours, 23 minutes, 38 seconds
  Estimated time remaining to next output: 10 minutes, 24 seconds
Output 296/1000: t=2950000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 5 days, 2 hours, 2 minutes, 33 seconds
  Estimated time remaining to next output: 10 minutes, 24 seconds
Output 297/1000: t=2960000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 5 days, 1 hours, 40 minutes, 25 seconds
  Estimated time remaining to next output: 10 minutes, 23 seconds
Output 298/1000: t=2970000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 5 days, 1 hours, 18 minutes, 12 seconds
  Estimated time remaining to next output: 10 minutes, 22 seconds
Output 299/1000: t=2980000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 5 days, 57 minutes, 40 seconds
  Estimated time remaining to next output: 10 minutes, 21 seconds
Output 300/1000: t=2990000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 5 days, 35 minutes, 16 seconds
  Estimated time remaining to next output: 10 minutes, 20 seconds
Output 301/1000: t=3000000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 5 days, 13 minutes, 37 seconds
  Estimated time remaining to next output: 10 minutes, 19 seconds
Output 302/1000: t=3010000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 4 days, 23 hours, 52 minutes, 35 seconds
  Estimated time remaining to next output: 10 minutes, 18 seconds
Output 303/1000: t=3020000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 4 days, 23 hours, 30 minutes, 14 seconds
  Estimated time remaining to next output: 10 minutes, 17 seconds
Output 304/1000: t=3030000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 4 days, 23 hours, 8 minutes, 9 seconds
  Estimated time remaining to next output: 10 minutes, 16 seconds
Output 305/1000: t=3040000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 4 days, 22 hours, 46 minutes, 42 seconds
  Estimated time remaining to next output: 10 minutes, 15 seconds
Output 306/1000: t=3050000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 4 days, 22 hours, 25 minutes, 1 seconds
  Estimated time remaining to next output: 10 minutes, 14 seconds
Output 307/1000: t=3060000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 4 days, 22 hours, 3 minutes, 7 seconds
  Estimated time remaining to next output: 10 minutes, 13 seconds
Output 308/1000: t=3070000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 4 days, 21 hours, 41 minutes, 54 seconds
  Estimated time remaining to next output: 10 minutes, 12 seconds
Output 309/1000: t=3080000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 4 days, 21 hours, 20 minutes, 46 seconds
  Estimated time remaining to next output: 10 minutes, 11 seconds
Output 310/1000: t=3090000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 4 days, 20 hours, 59 minutes, 53 seconds
  Estimated time remaining to next output: 10 minutes, 10 seconds
Output 311/1000: t=3100000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 4 days, 20 hours, 38 minutes, 27 seconds
  Estimated time remaining to next output: 10 minutes, 9 seconds
Output 312/1000: t=3110000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 4 days, 20 hours, 19 minutes, 2 seconds
  Estimated time remaining to next output: 10 minutes, 8 seconds
Output 313/1000: t=3120000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 4 days, 19 hours, 58 minutes, 15 seconds
  Estimated time remaining to next output: 10 minutes, 7 seconds
Output 314/1000: t=3130000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 4 days, 19 hours, 37 minutes, 18 seconds
  Estimated time remaining to next output: 10 minutes, 6 seconds
Output 315/1000: t=3140000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 4 days, 19 hours, 16 minutes, 23 seconds
  Estimated time remaining to next output: 10 minutes, 5 seconds
Output 316/1000: t=3150000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 4 days, 18 hours, 57 minutes, 19 seconds
  Estimated time remaining to next output: 10 minutes, 5 seconds
Output 317/1000: t=3160000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 4 days, 18 hours, 36 minutes, 45 seconds
  Estimated time remaining to next output: 10 minutes, 4 seconds
Output 318/1000: t=3170000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 4 days, 18 hours, 17 minutes, 59 seconds
  Estimated time remaining to next output: 10 minutes, 3 seconds
Output 319/1000: t=3180000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 4 days, 17 hours, 57 minutes, 45 seconds
  Estimated time remaining to next output: 10 minutes, 2 seconds
Output 320/1000: t=3190000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 4 days, 17 hours, 37 minutes, 36 seconds
  Estimated time remaining to next output: 10 minutes, 1 seconds
Output 321/1000: t=3200000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 4 days, 17 hours, 17 minutes, 39 seconds
  Estimated time remaining to next output: 10 minutes
Output 322/1000: t=3210000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 4 days, 16 hours, 56 minutes, 50 seconds
  Estimated time remaining to next output: 9 minutes, 59 seconds
Output 323/1000: t=3220000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 4 days, 16 hours, 37 minutes, 21 seconds
  Estimated time remaining to next output: 9 minutes, 58 seconds
Output 324/1000: t=3230000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 4 days, 16 hours, 18 minutes, 33 seconds
  Estimated time remaining to next output: 9 minutes, 58 seconds
Output 325/1000: t=3240000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 4 days, 15 hours, 59 minutes, 35 seconds
  Estimated time remaining to next output: 9 minutes, 57 seconds
Output 326/1000: t=3250000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 4 days, 15 hours, 41 minutes, 25 seconds
  Estimated time remaining to next output: 9 minutes, 56 seconds
Output 327/1000: t=3260000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 4 days, 15 hours, 21 minutes, 48 seconds
  Estimated time remaining to next output: 9 minutes, 55 seconds
Output 328/1000: t=3270000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 4 days, 15 hours, 3 minutes, 21 seconds
  Estimated time remaining to next output: 9 minutes, 54 seconds
Output 329/1000: t=3280000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 4 days, 14 hours, 44 minutes, 21 seconds
  Estimated time remaining to next output: 9 minutes, 54 seconds
Output 330/1000: t=3290000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 4 days, 14 hours, 25 minutes, 7 seconds
  Estimated time remaining to next output: 9 minutes, 53 seconds
Output 331/1000: t=3300000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 4 days, 14 hours, 5 minutes, 19 seconds
  Estimated time remaining to next output: 9 minutes, 52 seconds
Output 332/1000: t=3310000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 4 days, 13 hours, 46 minutes, 32 seconds
  Estimated time remaining to next output: 9 minutes, 51 seconds
Output 333/1000: t=3320000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 4 days, 13 hours, 27 minutes, 7 seconds
  Estimated time remaining to next output: 9 minutes, 50 seconds
Output 334/1000: t=3330000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 4 days, 13 hours, 7 minutes, 23 seconds
  Estimated time remaining to next output: 9 minutes, 49 seconds
Output 335/1000: t=3340000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 4 days, 12 hours, 47 minutes, 55 seconds
  Estimated time remaining to next output: 9 minutes, 48 seconds
Output 336/1000: t=3350000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 4 days, 12 hours, 28 minutes, 45 seconds
  Estimated time remaining to next output: 9 minutes, 48 seconds
Output 337/1000: t=3360000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 4 days, 12 hours, 9 minutes, 53 seconds
  Estimated time remaining to next output: 9 minutes, 47 seconds
Output 338/1000: t=3370000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 4 days, 11 hours, 51 minutes, 13 seconds
  Estimated time remaining to next output: 9 minutes, 46 seconds
Output 339/1000: t=3380000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 4 days, 11 hours, 39 minutes, 40 seconds
  Estimated time remaining to next output: 9 minutes, 46 seconds
Output 340/1000: t=3390000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 4 days, 11 hours, 29 minutes, 21 seconds
  Estimated time remaining to next output: 9 minutes, 46 seconds
Output 341/1000: t=3400000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 4 days, 11 hours, 20 minutes, 15 seconds
  Estimated time remaining to next output: 9 minutes, 46 seconds
Output 342/1000: t=3410000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 4 days, 11 hours, 10 minutes, 39 seconds
  Estimated time remaining to next output: 9 minutes, 46 seconds
Output 343/1000: t=3420000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 4 days, 10 hours, 51 minutes, 29 seconds
  Estimated time remaining to next output: 9 minutes, 45 seconds
Output 344/1000: t=3430000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 4 days, 10 hours, 32 minutes, 38 seconds
  Estimated time remaining to next output: 9 minutes, 44 seconds
Output 345/1000: t=3440000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 4 days, 10 hours, 14 minutes, 51 seconds
  Estimated time remaining to next output: 9 minutes, 43 seconds
Output 346/1000: t=3450000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 4 days, 9 hours, 56 minutes, 35 seconds
  Estimated time remaining to next output: 9 minutes, 43 seconds
Output 347/1000: t=3460000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 4 days, 9 hours, 38 minutes, 39 seconds
  Estimated time remaining to next output: 9 minutes, 42 seconds
Output 348/1000: t=3470000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 4 days, 9 hours, 20 minutes, 16 seconds
  Estimated time remaining to next output: 9 minutes, 41 seconds
Output 349/1000: t=3480000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 4 days, 9 hours, 2 minutes, 51 seconds
  Estimated time remaining to next output: 9 minutes, 40 seconds
Output 350/1000: t=3490000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 4 days, 8 hours, 44 minutes, 22 seconds
  Estimated time remaining to next output: 9 minutes, 40 seconds
Output 351/1000: t=3500000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 4 days, 8 hours, 26 minutes, 32 seconds
  Estimated time remaining to next output: 9 minutes, 39 seconds
Output 352/1000: t=3510000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 4 days, 8 hours, 9 minutes, 24 seconds
  Estimated time remaining to next output: 9 minutes, 38 seconds
Output 353/1000: t=3520000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 4 days, 7 hours, 51 minutes, 33 seconds
  Estimated time remaining to next output: 9 minutes, 37 seconds
Output 354/1000: t=3530000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 4 days, 7 hours, 33 minutes, 16 seconds
  Estimated time remaining to next output: 9 minutes, 37 seconds
Output 355/1000: t=3540000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 4 days, 7 hours, 15 minutes, 48 seconds
  Estimated time remaining to next output: 9 minutes, 36 seconds
Output 356/1000: t=3550000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 4 days, 6 hours, 59 minutes, 23 seconds
  Estimated time remaining to next output: 9 minutes, 35 seconds
Output 357/1000: t=3560000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 4 days, 6 hours, 42 minutes, 14 seconds
  Estimated time remaining to next output: 9 minutes, 35 seconds
Output 358/1000: t=3570000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 4 days, 6 hours, 25 minutes, 13 seconds
  Estimated time remaining to next output: 9 minutes, 34 seconds
Output 359/1000: t=3580000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 4 days, 6 hours, 7 minutes, 48 seconds
  Estimated time remaining to next output: 9 minutes, 33 seconds
Output 360/1000: t=3590000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 4 days, 5 hours, 50 minutes, 6 seconds
  Estimated time remaining to next output: 9 minutes, 32 seconds
Output 361/1000: t=3600000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 4 days, 5 hours, 33 minutes, 2 seconds
  Estimated time remaining to next output: 9 minutes, 32 seconds
Output 362/1000: t=3610000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 4 days, 5 hours, 15 minutes, 47 seconds
  Estimated time remaining to next output: 9 minutes, 31 seconds
Output 363/1000: t=3620000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 4 days, 4 hours, 58 minutes, 41 seconds
  Estimated time remaining to next output: 9 minutes, 30 seconds
Output 364/1000: t=3630000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 4 days, 4 hours, 42 minutes, 4 seconds
  Estimated time remaining to next output: 9 minutes, 30 seconds
Output 365/1000: t=3640000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 4 days, 4 hours, 24 minutes, 42 seconds
  Estimated time remaining to next output: 9 minutes, 29 seconds
Output 366/1000: t=3650000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 4 days, 4 hours, 8 minutes, 4 seconds
  Estimated time remaining to next output: 9 minutes, 28 seconds
Output 367/1000: t=3660000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 4 days, 3 hours, 51 minutes, 8 seconds
  Estimated time remaining to next output: 9 minutes, 27 seconds
Output 368/1000: t=3670000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 4 days, 3 hours, 35 minutes, 30 seconds
  Estimated time remaining to next output: 9 minutes, 27 seconds
Output 369/1000: t=3680000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 4 days, 3 hours, 19 minutes, 17 seconds
  Estimated time remaining to next output: 9 minutes, 26 seconds
Output 370/1000: t=3690000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 4 days, 3 hours, 2 minutes, 23 seconds
  Estimated time remaining to next output: 9 minutes, 25 seconds
Output 371/1000: t=3700000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 4 days, 2 hours, 45 minutes, 40 seconds
  Estimated time remaining to next output: 9 minutes, 25 seconds
Output 372/1000: t=3710000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 4 days, 2 hours, 29 minutes, 3 seconds
  Estimated time remaining to next output: 9 minutes, 24 seconds
Output 373/1000: t=3720000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 4 days, 2 hours, 12 minutes, 39 seconds
  Estimated time remaining to next output: 9 minutes, 23 seconds
Output 374/1000: t=3730000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 4 days, 1 hours, 55 minutes, 57 seconds
  Estimated time remaining to next output: 9 minutes, 23 seconds
Output 375/1000: t=3740000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 4 days, 1 hours, 39 minutes, 17 seconds
  Estimated time remaining to next output: 9 minutes, 22 seconds
Output 376/1000: t=3750000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 4 days, 1 hours, 23 minutes, 23 seconds
  Estimated time remaining to next output: 9 minutes, 21 seconds
Output 377/1000: t=3760000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 4 days, 1 hours, 6 minutes, 59 seconds
  Estimated time remaining to next output: 9 minutes, 21 seconds
Output 378/1000: t=3770000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 4 days, 51 minutes, 16 seconds
  Estimated time remaining to next output: 9 minutes, 20 seconds
Output 379/1000: t=3780000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 4 days, 35 minutes, 4 seconds
  Estimated time remaining to next output: 9 minutes, 19 seconds
Output 380/1000: t=3790000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 4 days, 18 minutes, 45 seconds
  Estimated time remaining to next output: 9 minutes, 19 seconds
Output 381/1000: t=3800000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 4 days, 2 minutes, 44 seconds
  Estimated time remaining to next output: 9 minutes, 18 seconds
Output 382/1000: t=3810000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 23 hours, 46 minutes, 40 seconds
  Estimated time remaining to next output: 9 minutes, 17 seconds
Output 383/1000: t=3820000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 23 hours, 31 minutes, 29 seconds
  Estimated time remaining to next output: 9 minutes, 17 seconds
Output 384/1000: t=3830000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 23 hours, 16 minutes, 28 seconds
  Estimated time remaining to next output: 9 minutes, 16 seconds
Output 385/1000: t=3840000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 23 hours, 1 minutes, 6 seconds
  Estimated time remaining to next output: 9 minutes, 16 seconds
Output 386/1000: t=3850000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 22 hours, 45 minutes, 48 seconds
  Estimated time remaining to next output: 9 minutes, 15 seconds
Output 387/1000: t=3860000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 22 hours, 30 minutes, 2 seconds
  Estimated time remaining to next output: 9 minutes, 14 seconds
Output 388/1000: t=3870000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 22 hours, 14 minutes, 50 seconds
  Estimated time remaining to next output: 9 minutes, 14 seconds
Output 389/1000: t=3880000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 21 hours, 59 minutes, 35 seconds
  Estimated time remaining to next output: 9 minutes, 13 seconds
Output 390/1000: t=3890000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 21 hours, 43 minutes, 40 seconds
  Estimated time remaining to next output: 9 minutes, 13 seconds
Output 391/1000: t=3900000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 21 hours, 28 minutes, 12 seconds
  Estimated time remaining to next output: 9 minutes, 12 seconds
Output 392/1000: t=3910000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 21 hours, 13 minutes, 28 seconds
  Estimated time remaining to next output: 9 minutes, 11 seconds
Output 393/1000: t=3920000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 20 hours, 58 minutes, 14 seconds
  Estimated time remaining to next output: 9 minutes, 11 seconds
Output 394/1000: t=3930000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 20 hours, 42 minutes, 51 seconds
  Estimated time remaining to next output: 9 minutes, 10 seconds
Output 395/1000: t=3940000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 20 hours, 28 minutes, 37 seconds
  Estimated time remaining to next output: 9 minutes, 10 seconds
Output 396/1000: t=3950000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 20 hours, 13 minutes, 14 seconds
  Estimated time remaining to next output: 9 minutes, 9 seconds
Output 397/1000: t=3960000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 19 hours, 58 minutes, 8 seconds
  Estimated time remaining to next output: 9 minutes, 9 seconds
Output 398/1000: t=3970000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 19 hours, 43 minutes, 17 seconds
  Estimated time remaining to next output: 9 minutes, 8 seconds
Output 399/1000: t=3980000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 19 hours, 29 minutes, 31 seconds
  Estimated time remaining to next output: 9 minutes, 8 seconds
Output 400/1000: t=3990000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 19 hours, 15 minutes, 1 seconds
  Estimated time remaining to next output: 9 minutes, 7 seconds
Output 401/1000: t=4000000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 18 hours, 59 minutes, 24 seconds
  Estimated time remaining to next output: 9 minutes, 6 seconds
Output 402/1000: t=4010000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 18 hours, 44 minutes, 6 seconds
  Estimated time remaining to next output: 9 minutes, 6 seconds
Output 403/1000: t=4020000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 18 hours, 29 minutes, 25 seconds
  Estimated time remaining to next output: 9 minutes, 5 seconds
Output 404/1000: t=4030000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 18 hours, 14 minutes, 27 seconds
  Estimated time remaining to next output: 9 minutes, 5 seconds
Output 405/1000: t=4040000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 17 hours, 59 minutes, 42 seconds
  Estimated time remaining to next output: 9 minutes, 4 seconds
Output 406/1000: t=4050000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 17 hours, 45 minutes, 56 seconds
  Estimated time remaining to next output: 9 minutes, 4 seconds
Output 407/1000: t=4060000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 17 hours, 31 minutes, 7 seconds
  Estimated time remaining to next output: 9 minutes, 3 seconds
Output 408/1000: t=4070000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 17 hours, 16 minutes, 56 seconds
  Estimated time remaining to next output: 9 minutes, 2 seconds
Output 409/1000: t=4080000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 17 hours, 1 minutes, 53 seconds
  Estimated time remaining to next output: 9 minutes, 2 seconds
Output 410/1000: t=4090000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 16 hours, 47 minutes, 40 seconds
  Estimated time remaining to next output: 9 minutes, 1 seconds
Output 411/1000: t=4100000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 16 hours, 33 minutes, 41 seconds
  Estimated time remaining to next output: 9 minutes, 1 seconds
Output 412/1000: t=4110000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 16 hours, 19 minutes, 7 seconds
  Estimated time remaining to next output: 9 minutes
Output 413/1000: t=4120000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 16 hours, 4 minutes, 53 seconds
  Estimated time remaining to next output: 9 minutes
Output 414/1000: t=4130000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 15 hours, 50 minutes, 43 seconds
  Estimated time remaining to next output: 8 minutes, 59 seconds
Output 415/1000: t=4140000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 15 hours, 36 minutes, 56 seconds
  Estimated time remaining to next output: 8 minutes, 59 seconds
Output 416/1000: t=4150000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 15 hours, 23 minutes, 4 seconds
  Estimated time remaining to next output: 8 minutes, 58 seconds
Output 417/1000: t=4160000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 15 hours, 8 minutes, 46 seconds
  Estimated time remaining to next output: 8 minutes, 58 seconds
Output 418/1000: t=4170000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 14 hours, 54 minutes, 19 seconds
  Estimated time remaining to next output: 8 minutes, 57 seconds
Output 419/1000: t=4180000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 14 hours, 40 minutes, 27 seconds
  Estimated time remaining to next output: 8 minutes, 57 seconds
Output 420/1000: t=4190000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 14 hours, 26 minutes, 36 seconds
  Estimated time remaining to next output: 8 minutes, 56 seconds
Output 421/1000: t=4200000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 14 hours, 11 minutes, 57 seconds
  Estimated time remaining to next output: 8 minutes, 55 seconds
Output 422/1000: t=4210000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 13 hours, 57 minutes, 34 seconds
  Estimated time remaining to next output: 8 minutes, 55 seconds
Output 423/1000: t=4220000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 13 hours, 43 minutes, 48 seconds
  Estimated time remaining to next output: 8 minutes, 54 seconds
Output 424/1000: t=4230000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 13 hours, 30 minutes, 35 seconds
  Estimated time remaining to next output: 8 minutes, 54 seconds
Output 425/1000: t=4240000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 13 hours, 16 minutes, 25 seconds
  Estimated time remaining to next output: 8 minutes, 53 seconds
Output 426/1000: t=4250000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 13 hours, 2 minutes, 47 seconds
  Estimated time remaining to next output: 8 minutes, 53 seconds
Output 427/1000: t=4260000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 12 hours, 48 minutes, 44 seconds
  Estimated time remaining to next output: 8 minutes, 52 seconds
Output 428/1000: t=4270000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 12 hours, 35 minutes, 12 seconds
  Estimated time remaining to next output: 8 minutes, 52 seconds
Output 429/1000: t=4280000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 12 hours, 21 minutes, 7 seconds
  Estimated time remaining to next output: 8 minutes, 51 seconds
Output 430/1000: t=4290000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 12 hours, 7 minutes, 35 seconds
  Estimated time remaining to next output: 8 minutes, 51 seconds
Output 431/1000: t=4300000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 11 hours, 53 minutes, 47 seconds
  Estimated time remaining to next output: 8 minutes, 50 seconds
Output 432/1000: t=4310000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 11 hours, 40 minutes, 26 seconds
  Estimated time remaining to next output: 8 minutes, 50 seconds
Output 433/1000: t=4320000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 11 hours, 27 minutes, 2 seconds
  Estimated time remaining to next output: 8 minutes, 49 seconds
Output 434/1000: t=4330000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 11 hours, 13 minutes, 30 seconds
  Estimated time remaining to next output: 8 minutes, 49 seconds
Output 435/1000: t=4340000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 10 hours, 59 minutes, 38 seconds
  Estimated time remaining to next output: 8 minutes, 48 seconds
Output 436/1000: t=4350000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 10 hours, 46 minutes, 45 seconds
  Estimated time remaining to next output: 8 minutes, 48 seconds
Output 437/1000: t=4360000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 10 hours, 33 minutes, 17 seconds
  Estimated time remaining to next output: 8 minutes, 47 seconds
Output 438/1000: t=4370000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 10 hours, 20 minutes, 12 seconds
  Estimated time remaining to next output: 8 minutes, 47 seconds
Output 439/1000: t=4380000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 10 hours, 7 minutes, 26 seconds
  Estimated time remaining to next output: 8 minutes, 46 seconds
Output 440/1000: t=4390000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 9 hours, 54 minutes, 37 seconds
  Estimated time remaining to next output: 8 minutes, 46 seconds
Output 441/1000: t=4400000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 9 hours, 41 minutes, 22 seconds
  Estimated time remaining to next output: 8 minutes, 46 seconds
Output 442/1000: t=4410000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 9 hours, 27 minutes, 54 seconds
  Estimated time remaining to next output: 8 minutes, 45 seconds
Output 443/1000: t=4420000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 9 hours, 14 minutes, 47 seconds
  Estimated time remaining to next output: 8 minutes, 45 seconds
Output 444/1000: t=4430000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 9 hours, 2 minutes, 7 seconds
  Estimated time remaining to next output: 8 minutes, 44 seconds
Output 445/1000: t=4440000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 8 hours, 49 minutes, 13 seconds
  Estimated time remaining to next output: 8 minutes, 44 seconds
Output 446/1000: t=4450000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 8 hours, 36 minutes, 43 seconds
  Estimated time remaining to next output: 8 minutes, 43 seconds
Output 447/1000: t=4460000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 8 hours, 23 minutes, 32 seconds
  Estimated time remaining to next output: 8 minutes, 43 seconds
Output 448/1000: t=4470000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 8 hours, 10 minutes, 49 seconds
  Estimated time remaining to next output: 8 minutes, 42 seconds
Output 449/1000: t=4480000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 7 hours, 57 minutes, 40 seconds
  Estimated time remaining to next output: 8 minutes, 42 seconds
Output 450/1000: t=4490000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 7 hours, 44 minutes, 31 seconds
  Estimated time remaining to next output: 8 minutes, 41 seconds
Output 451/1000: t=4500000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 7 hours, 32 minutes, 19 seconds
  Estimated time remaining to next output: 8 minutes, 41 seconds
Output 452/1000: t=4510000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 7 hours, 19 minutes, 42 seconds
  Estimated time remaining to next output: 8 minutes, 41 seconds
Output 453/1000: t=4520000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 7 hours, 6 minutes, 39 seconds
  Estimated time remaining to next output: 8 minutes, 40 seconds
Output 454/1000: t=4530000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 6 hours, 53 minutes, 49 seconds
  Estimated time remaining to next output: 8 minutes, 40 seconds
Output 455/1000: t=4540000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 6 hours, 41 minutes, 5 seconds
  Estimated time remaining to next output: 8 minutes, 39 seconds
Output 456/1000: t=4550000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 6 hours, 28 minutes, 39 seconds
  Estimated time remaining to next output: 8 minutes, 39 seconds
Output 457/1000: t=4560000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 6 hours, 16 minutes, 13 seconds
  Estimated time remaining to next output: 8 minutes, 38 seconds
Output 458/1000: t=4570000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 6 hours, 3 minutes, 38 seconds
  Estimated time remaining to next output: 8 minutes, 38 seconds
Output 459/1000: t=4580000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 5 hours, 51 minutes, 8 seconds
  Estimated time remaining to next output: 8 minutes, 38 seconds
Output 460/1000: t=4590000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 5 hours, 38 minutes, 12 seconds
  Estimated time remaining to next output: 8 minutes, 37 seconds
Output 461/1000: t=4600000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 5 hours, 24 minutes, 58 seconds
  Estimated time remaining to next output: 8 minutes, 37 seconds
Output 462/1000: t=4610000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 5 hours, 12 minutes, 49 seconds
  Estimated time remaining to next output: 8 minutes, 36 seconds
Output 463/1000: t=4620000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 5 hours, 1 seconds
  Estimated time remaining to next output: 8 minutes, 36 seconds
Output 464/1000: t=4630000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 4 hours, 47 minutes, 33 seconds
  Estimated time remaining to next output: 8 minutes, 35 seconds
Output 465/1000: t=4640000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 4 hours, 35 minutes, 21 seconds
  Estimated time remaining to next output: 8 minutes, 35 seconds
Output 466/1000: t=4650000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 4 hours, 22 minutes, 48 seconds
  Estimated time remaining to next output: 8 minutes, 34 seconds
Output 467/1000: t=4660000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 4 hours, 10 minutes, 19 seconds
  Estimated time remaining to next output: 8 minutes, 34 seconds
Output 468/1000: t=4670000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 3 hours, 57 minutes, 52 seconds
  Estimated time remaining to next output: 8 minutes, 34 seconds
Output 469/1000: t=4680000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 3 hours, 45 minutes, 17 seconds
  Estimated time remaining to next output: 8 minutes, 33 seconds
Output 470/1000: t=4690000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 3 hours, 33 minutes, 23 seconds
  Estimated time remaining to next output: 8 minutes, 33 seconds
Output 471/1000: t=4700000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 3 hours, 21 minutes, 15 seconds
  Estimated time remaining to next output: 8 minutes, 32 seconds
Output 472/1000: t=4710000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 3 hours, 9 minutes, 36 seconds
  Estimated time remaining to next output: 8 minutes, 32 seconds
Output 473/1000: t=4720000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 2 hours, 57 minutes, 47 seconds
  Estimated time remaining to next output: 8 minutes, 32 seconds
Output 474/1000: t=4730000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 2 hours, 45 minutes, 18 seconds
  Estimated time remaining to next output: 8 minutes, 31 seconds
Output 475/1000: t=4740000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 2 hours, 32 minutes, 50 seconds
  Estimated time remaining to next output: 8 minutes, 31 seconds
Output 476/1000: t=4750000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 2 hours, 21 minutes, 6 seconds
  Estimated time remaining to next output: 8 minutes, 30 seconds
Output 477/1000: t=4760000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 2 hours, 9 minutes, 15 seconds
  Estimated time remaining to next output: 8 minutes, 30 seconds
Output 478/1000: t=4770000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 1 hours, 57 minutes, 45 seconds
  Estimated time remaining to next output: 8 minutes, 30 seconds
Output 479/1000: t=4780000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 1 hours, 45 minutes, 21 seconds
  Estimated time remaining to next output: 8 minutes, 29 seconds
Output 480/1000: t=4790000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 1 hours, 33 minutes, 17 seconds
  Estimated time remaining to next output: 8 minutes, 29 seconds
Output 481/1000: t=4800000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 1 hours, 21 minutes, 36 seconds
  Estimated time remaining to next output: 8 minutes, 28 seconds
Output 482/1000: t=4810000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 1 hours, 9 minutes, 46 seconds
  Estimated time remaining to next output: 8 minutes, 28 seconds
Output 483/1000: t=4820000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 58 minutes, 32 seconds
  Estimated time remaining to next output: 8 minutes, 28 seconds
Output 484/1000: t=4830000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 47 minutes, 14 seconds
  Estimated time remaining to next output: 8 minutes, 27 seconds
Output 485/1000: t=4840000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 35 minutes, 17 seconds
  Estimated time remaining to next output: 8 minutes, 27 seconds
Output 486/1000: t=4850000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 23 minutes, 18 seconds
  Estimated time remaining to next output: 8 minutes, 27 seconds
Output 487/1000: t=4860000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 days, 11 minutes, 13 seconds
  Estimated time remaining to next output: 8 minutes, 26 seconds
Output 488/1000: t=4870000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 23 hours, 59 minutes, 14 seconds
  Estimated time remaining to next output: 8 minutes, 26 seconds
Output 489/1000: t=4880000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 23 hours, 47 minutes, 38 seconds
  Estimated time remaining to next output: 8 minutes, 25 seconds
Output 490/1000: t=4890000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 23 hours, 35 minutes, 56 seconds
  Estimated time remaining to next output: 8 minutes, 25 seconds
Output 491/1000: t=4900000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 23 hours, 24 minutes, 18 seconds
  Estimated time remaining to next output: 8 minutes, 25 seconds
Output 492/1000: t=4910000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 23 hours, 12 minutes, 32 seconds
  Estimated time remaining to next output: 8 minutes, 24 seconds
Output 493/1000: t=4920000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 23 hours, 35 seconds
  Estimated time remaining to next output: 8 minutes, 24 seconds
Output 494/1000: t=4930000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 22 hours, 48 minutes, 50 seconds
  Estimated time remaining to next output: 8 minutes, 23 seconds
Output 495/1000: t=4940000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 22 hours, 37 minutes, 34 seconds
  Estimated time remaining to next output: 8 minutes, 23 seconds
Output 496/1000: t=4950000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 22 hours, 26 minutes, 26 seconds
  Estimated time remaining to next output: 8 minutes, 23 seconds
Output 497/1000: t=4960000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 22 hours, 15 minutes, 4 seconds
  Estimated time remaining to next output: 8 minutes, 22 seconds
Output 498/1000: t=4970000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 22 hours, 3 minutes, 11 seconds
  Estimated time remaining to next output: 8 minutes, 22 seconds
Output 499/1000: t=4980000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 21 hours, 51 minutes, 25 seconds
  Estimated time remaining to next output: 8 minutes, 21 seconds
Output 500/1000: t=4990000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 21 hours, 40 minutes
  Estimated time remaining to next output: 8 minutes, 21 seconds
Output 501/1000: t=5000000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 21 hours, 28 minutes, 35 seconds
  Estimated time remaining to next output: 8 minutes, 21 seconds
Output 502/1000: t=5010000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 21 hours, 17 minutes, 13 seconds
  Estimated time remaining to next output: 8 minutes, 20 seconds
Output 503/1000: t=5020000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 21 hours, 5 minutes, 28 seconds
  Estimated time remaining to next output: 8 minutes, 20 seconds
Output 504/1000: t=5030000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 20 hours, 54 minutes, 12 seconds
  Estimated time remaining to next output: 8 minutes, 20 seconds
Output 505/1000: t=5040000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 20 hours, 42 minutes, 48 seconds
  Estimated time remaining to next output: 8 minutes, 19 seconds
Output 506/1000: t=5050000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 20 hours, 31 minutes, 38 seconds
  Estimated time remaining to next output: 8 minutes, 19 seconds
Output 507/1000: t=5060000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 20 hours, 20 minutes, 37 seconds
  Estimated time remaining to next output: 8 minutes, 19 seconds
Output 508/1000: t=5070000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 20 hours, 9 minutes, 12 seconds
  Estimated time remaining to next output: 8 minutes, 18 seconds
Output 509/1000: t=5080000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 19 hours, 58 minutes, 3 seconds
  Estimated time remaining to next output: 8 minutes, 18 seconds
Output 510/1000: t=5090000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 19 hours, 46 minutes, 53 seconds
  Estimated time remaining to next output: 8 minutes, 17 seconds
Output 511/1000: t=5100000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 19 hours, 35 minutes, 31 seconds
  Estimated time remaining to next output: 8 minutes, 17 seconds
Output 512/1000: t=5110000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 19 hours, 24 minutes, 41 seconds
  Estimated time remaining to next output: 8 minutes, 17 seconds
Output 513/1000: t=5120000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 19 hours, 13 minutes, 21 seconds
  Estimated time remaining to next output: 8 minutes, 16 seconds
Output 514/1000: t=5130000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 19 hours, 2 minutes, 42 seconds
  Estimated time remaining to next output: 8 minutes, 16 seconds
Output 515/1000: t=5140000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 18 hours, 51 minutes, 57 seconds
  Estimated time remaining to next output: 8 minutes, 16 seconds
Output 516/1000: t=5150000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 18 hours, 40 minutes, 45 seconds
  Estimated time remaining to next output: 8 minutes, 15 seconds
Output 517/1000: t=5160000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 18 hours, 29 minutes, 43 seconds
  Estimated time remaining to next output: 8 minutes, 15 seconds
Output 518/1000: t=5170000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 18 hours, 18 minutes, 34 seconds
  Estimated time remaining to next output: 8 minutes, 15 seconds
Output 519/1000: t=5180000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 18 hours, 7 minutes, 46 seconds
  Estimated time remaining to next output: 8 minutes, 14 seconds
Output 520/1000: t=5190000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 17 hours, 56 minutes, 23 seconds
  Estimated time remaining to next output: 8 minutes, 14 seconds
Output 521/1000: t=5200000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 17 hours, 45 minutes, 18 seconds
  Estimated time remaining to next output: 8 minutes, 14 seconds
Output 522/1000: t=5210000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 17 hours, 34 minutes, 23 seconds
  Estimated time remaining to next output: 8 minutes, 13 seconds
Output 523/1000: t=5220000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 17 hours, 23 minutes, 58 seconds
  Estimated time remaining to next output: 8 minutes, 13 seconds
Output 524/1000: t=5230000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 17 hours, 12 minutes, 59 seconds
  Estimated time remaining to next output: 8 minutes, 13 seconds
Output 525/1000: t=5240000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 17 hours, 2 minutes, 30 seconds
  Estimated time remaining to next output: 8 minutes, 12 seconds
Output 526/1000: t=5250000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 16 hours, 51 minutes, 25 seconds
  Estimated time remaining to next output: 8 minutes, 12 seconds
Output 527/1000: t=5260000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 16 hours, 40 minutes, 20 seconds
  Estimated time remaining to next output: 8 minutes, 12 seconds
Output 528/1000: t=5270000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 16 hours, 29 minutes, 26 seconds
  Estimated time remaining to next output: 8 minutes, 11 seconds
Output 529/1000: t=5280000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 16 hours, 18 minutes, 38 seconds
  Estimated time remaining to next output: 8 minutes, 11 seconds
Output 530/1000: t=5290000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 16 hours, 7 minutes, 35 seconds
  Estimated time remaining to next output: 8 minutes, 11 seconds
Output 531/1000: t=5300000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 15 hours, 57 minutes, 1 seconds
  Estimated time remaining to next output: 8 minutes, 10 seconds
Output 532/1000: t=5310000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 15 hours, 46 minutes, 26 seconds
  Estimated time remaining to next output: 8 minutes, 10 seconds
Output 533/1000: t=5320000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 15 hours, 35 minutes, 39 seconds
  Estimated time remaining to next output: 8 minutes, 10 seconds
Output 534/1000: t=5330000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 15 hours, 24 minutes, 50 seconds
  Estimated time remaining to next output: 8 minutes, 9 seconds
Output 535/1000: t=5340000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 15 hours, 14 minutes, 1 seconds
  Estimated time remaining to next output: 8 minutes, 9 seconds
Output 536/1000: t=5350000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 15 hours, 3 minutes, 32 seconds
  Estimated time remaining to next output: 8 minutes, 9 seconds
Output 537/1000: t=5360000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 14 hours, 52 minutes, 45 seconds
  Estimated time remaining to next output: 8 minutes, 8 seconds
Output 538/1000: t=5370000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 14 hours, 42 minutes, 4 seconds
  Estimated time remaining to next output: 8 minutes, 8 seconds
Output 539/1000: t=5380000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 14 hours, 31 minutes, 31 seconds
  Estimated time remaining to next output: 8 minutes, 8 seconds
Output 540/1000: t=5390000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 14 hours, 20 minutes, 43 seconds
  Estimated time remaining to next output: 8 minutes, 7 seconds
Output 541/1000: t=5400000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 14 hours, 10 minutes, 18 seconds
  Estimated time remaining to next output: 8 minutes, 7 seconds
Output 542/1000: t=5410000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 13 hours, 59 minutes, 33 seconds
  Estimated time remaining to next output: 8 minutes, 7 seconds
Output 543/1000: t=5420000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 13 hours, 49 minutes, 2 seconds
  Estimated time remaining to next output: 8 minutes, 6 seconds
Output 544/1000: t=5430000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 13 hours, 38 minutes, 39 seconds
  Estimated time remaining to next output: 8 minutes, 6 seconds
Output 545/1000: t=5440000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 13 hours, 28 minutes, 30 seconds
  Estimated time remaining to next output: 8 minutes, 6 seconds
Output 546/1000: t=5450000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 13 hours, 19 minutes, 31 seconds
  Estimated time remaining to next output: 8 minutes, 6 seconds
Output 547/1000: t=5460000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 13 hours, 10 minutes, 5 seconds
  Estimated time remaining to next output: 8 minutes, 6 seconds
Output 548/1000: t=5470000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 13 hours, 1 seconds
  Estimated time remaining to next output: 8 minutes, 5 seconds
Output 549/1000: t=5480000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 12 hours, 49 minutes, 38 seconds
  Estimated time remaining to next output: 8 minutes, 5 seconds
Output 550/1000: t=5490000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 12 hours, 39 minutes, 21 seconds
  Estimated time remaining to next output: 8 minutes, 5 seconds
Output 551/1000: t=5500000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 12 hours, 29 minutes, 22 seconds
  Estimated time remaining to next output: 8 minutes, 4 seconds
Output 552/1000: t=5510000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 12 hours, 19 minutes, 1 seconds
  Estimated time remaining to next output: 8 minutes, 4 seconds
Output 553/1000: t=5520000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 12 hours, 8 minutes, 50 seconds
  Estimated time remaining to next output: 8 minutes, 4 seconds
Output 554/1000: t=5530000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 11 hours, 58 minutes, 19 seconds
  Estimated time remaining to next output: 8 minutes, 4 seconds
Output 555/1000: t=5540000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 11 hours, 48 minutes, 3 seconds
  Estimated time remaining to next output: 8 minutes, 3 seconds
Output 556/1000: t=5550000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 11 hours, 37 minutes, 42 seconds
  Estimated time remaining to next output: 8 minutes, 3 seconds
Output 557/1000: t=5560000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 11 hours, 27 minutes, 28 seconds
  Estimated time remaining to next output: 8 minutes, 3 seconds
Output 558/1000: t=5570000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 11 hours, 17 minutes, 12 seconds
  Estimated time remaining to next output: 8 minutes, 2 seconds
Output 559/1000: t=5580000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 11 hours, 6 minutes, 45 seconds
  Estimated time remaining to next output: 8 minutes, 2 seconds
Output 560/1000: t=5590000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 10 hours, 56 minutes, 23 seconds
  Estimated time remaining to next output: 8 minutes, 2 seconds
Output 561/1000: t=5600000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 10 hours, 46 minutes, 8 seconds
  Estimated time remaining to next output: 8 minutes, 1 seconds
Output 562/1000: t=5610000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 10 hours, 36 minutes, 19 seconds
  Estimated time remaining to next output: 8 minutes, 1 seconds
Output 563/1000: t=5620000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 10 hours, 26 minutes, 16 seconds
  Estimated time remaining to next output: 8 minutes, 1 seconds
Output 564/1000: t=5630000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 10 hours, 16 minutes, 3 seconds
  Estimated time remaining to next output: 8 minutes, 1 seconds
Output 565/1000: t=5640000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 10 hours, 6 minutes, 1 seconds
  Estimated time remaining to next output: 8 minutes
Output 566/1000: t=5650000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 9 hours, 56 minutes, 7 seconds
  Estimated time remaining to next output: 8 minutes
Output 567/1000: t=5660000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 9 hours, 45 minutes, 58 seconds
  Estimated time remaining to next output: 8 minutes
Output 568/1000: t=5670000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 9 hours, 35 minutes, 41 seconds
  Estimated time remaining to next output: 7 minutes, 59 seconds
Output 569/1000: t=5680000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 9 hours, 25 minutes, 37 seconds
  Estimated time remaining to next output: 7 minutes, 59 seconds
Output 570/1000: t=5690000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 9 hours, 15 minutes, 16 seconds
  Estimated time remaining to next output: 7 minutes, 59 seconds
Output 571/1000: t=5700000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 9 hours, 5 minutes, 20 seconds
  Estimated time remaining to next output: 7 minutes, 59 seconds
Output 572/1000: t=5710000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 8 hours, 55 minutes, 7 seconds
  Estimated time remaining to next output: 7 minutes, 58 seconds
Output 573/1000: t=5720000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 8 hours, 45 minutes, 7 seconds
  Estimated time remaining to next output: 7 minutes, 58 seconds
Output 574/1000: t=5730000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 8 hours, 35 minutes, 21 seconds
  Estimated time remaining to next output: 7 minutes, 58 seconds
Output 575/1000: t=5740000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 8 hours, 25 minutes, 12 seconds
  Estimated time remaining to next output: 7 minutes, 57 seconds
Output 576/1000: t=5750000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 8 hours, 15 minutes, 34 seconds
  Estimated time remaining to next output: 7 minutes, 57 seconds
Output 577/1000: t=5760000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 8 hours, 5 minutes, 50 seconds
  Estimated time remaining to next output: 7 minutes, 57 seconds
Output 578/1000: t=5770000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 7 hours, 56 minutes, 3 seconds
  Estimated time remaining to next output: 7 minutes, 57 seconds
Output 579/1000: t=5780000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 7 hours, 46 minutes, 34 seconds
  Estimated time remaining to next output: 7 minutes, 56 seconds
Output 580/1000: t=5790000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 7 hours, 36 minutes, 33 seconds
  Estimated time remaining to next output: 7 minutes, 56 seconds
Output 581/1000: t=5800000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 7 hours, 26 minutes, 37 seconds
  Estimated time remaining to next output: 7 minutes, 56 seconds
Output 582/1000: t=5810000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 7 hours, 16 minutes, 41 seconds
  Estimated time remaining to next output: 7 minutes, 56 seconds
Output 583/1000: t=5820000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 7 hours, 7 minutes, 8 seconds
  Estimated time remaining to next output: 7 minutes, 55 seconds
Output 584/1000: t=5830000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 6 hours, 57 minutes, 12 seconds
  Estimated time remaining to next output: 7 minutes, 55 seconds
Output 585/1000: t=5840000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 6 hours, 47 minutes, 23 seconds
  Estimated time remaining to next output: 7 minutes, 55 seconds
Output 586/1000: t=5850000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 6 hours, 37 minutes, 53 seconds
  Estimated time remaining to next output: 7 minutes, 55 seconds
Output 587/1000: t=5860000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 6 hours, 28 minutes, 10 seconds
  Estimated time remaining to next output: 7 minutes, 54 seconds
Output 588/1000: t=5870000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 6 hours, 18 minutes, 20 seconds
  Estimated time remaining to next output: 7 minutes, 54 seconds
Output 589/1000: t=5880000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 6 hours, 8 minutes, 42 seconds
  Estimated time remaining to next output: 7 minutes, 54 seconds
Output 590/1000: t=5890000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 5 hours, 58 minutes, 54 seconds
  Estimated time remaining to next output: 7 minutes, 53 seconds
Output 591/1000: t=5900000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 5 hours, 49 minutes, 15 seconds
  Estimated time remaining to next output: 7 minutes, 53 seconds
Output 592/1000: t=5910000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 5 hours, 39 minutes, 23 seconds
  Estimated time remaining to next output: 7 minutes, 53 seconds
Output 593/1000: t=5920000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 5 hours, 29 minutes, 53 seconds
  Estimated time remaining to next output: 7 minutes, 53 seconds
Output 594/1000: t=5930000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 5 hours, 20 minutes, 16 seconds
  Estimated time remaining to next output: 7 minutes, 52 seconds
Output 595/1000: t=5940000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 5 hours, 10 minutes, 39 seconds
  Estimated time remaining to next output: 7 minutes, 52 seconds
Output 596/1000: t=5950000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 5 hours, 1 minutes, 4 seconds
  Estimated time remaining to next output: 7 minutes, 52 seconds
Output 597/1000: t=5960000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 4 hours, 51 minutes, 35 seconds
  Estimated time remaining to next output: 7 minutes, 52 seconds
Output 598/1000: t=5970000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 4 hours, 42 minutes, 18 seconds
  Estimated time remaining to next output: 7 minutes, 51 seconds
Output 599/1000: t=5980000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 4 hours, 32 minutes, 54 seconds
  Estimated time remaining to next output: 7 minutes, 51 seconds
Output 600/1000: t=5990000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 4 hours, 23 minutes, 32 seconds
  Estimated time remaining to next output: 7 minutes, 51 seconds
Output 601/1000: t=6000000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 4 hours, 14 minutes, 7 seconds
  Estimated time remaining to next output: 7 minutes, 51 seconds
Output 602/1000: t=6010000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 4 hours, 4 minutes, 28 seconds
  Estimated time remaining to next output: 7 minutes, 51 seconds
Output 603/1000: t=6020000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 3 hours, 55 minutes
  Estimated time remaining to next output: 7 minutes, 50 seconds
Output 604/1000: t=6030000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 3 hours, 45 minutes, 20 seconds
  Estimated time remaining to next output: 7 minutes, 50 seconds
Output 605/1000: t=6040000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 3 hours, 35 minutes, 54 seconds
  Estimated time remaining to next output: 7 minutes, 50 seconds
Output 606/1000: t=6050000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 3 hours, 26 minutes, 9 seconds
  Estimated time remaining to next output: 7 minutes, 49 seconds
Output 607/1000: t=6060000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 3 hours, 16 minutes, 37 seconds
  Estimated time remaining to next output: 7 minutes, 49 seconds
Output 608/1000: t=6070000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 3 hours, 7 minutes, 11 seconds
  Estimated time remaining to next output: 7 minutes, 49 seconds
Output 609/1000: t=6080000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 2 hours, 57 minutes, 36 seconds
  Estimated time remaining to next output: 7 minutes, 49 seconds
Output 610/1000: t=6090000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 2 hours, 48 minutes, 26 seconds
  Estimated time remaining to next output: 7 minutes, 48 seconds
Output 611/1000: t=6100000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 2 hours, 38 minutes, 58 seconds
  Estimated time remaining to next output: 7 minutes, 48 seconds
Output 612/1000: t=6110000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 2 hours, 29 minutes, 21 seconds
  Estimated time remaining to next output: 7 minutes, 48 seconds
Output 613/1000: t=6120000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 2 hours, 20 minutes, 8 seconds
  Estimated time remaining to next output: 7 minutes, 48 seconds
Output 614/1000: t=6130000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 2 hours, 10 minutes, 57 seconds
  Estimated time remaining to next output: 7 minutes, 48 seconds
Output 615/1000: t=6140000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 2 hours, 1 minutes, 44 seconds
  Estimated time remaining to next output: 7 minutes, 47 seconds
Output 616/1000: t=6150000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 1 hours, 52 minutes, 23 seconds
  Estimated time remaining to next output: 7 minutes, 47 seconds
Output 617/1000: t=6160000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 1 hours, 42 minutes, 42 seconds
  Estimated time remaining to next output: 7 minutes, 47 seconds
Output 618/1000: t=6170000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 1 hours, 33 minutes, 19 seconds
  Estimated time remaining to next output: 7 minutes, 47 seconds
Output 619/1000: t=6180000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 1 hours, 23 minutes, 55 seconds
  Estimated time remaining to next output: 7 minutes, 46 seconds
Output 620/1000: t=6190000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 1 hours, 14 minutes, 33 seconds
  Estimated time remaining to next output: 7 minutes, 46 seconds
Output 621/1000: t=6200000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 1 hours, 5 minutes, 19 seconds
  Estimated time remaining to next output: 7 minutes, 46 seconds
Output 622/1000: t=6210000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 55 minutes, 53 seconds
  Estimated time remaining to next output: 7 minutes, 46 seconds
Output 623/1000: t=6220000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 46 minutes, 33 seconds
  Estimated time remaining to next output: 7 minutes, 45 seconds
Output 624/1000: t=6230000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 37 minutes, 10 seconds
  Estimated time remaining to next output: 7 minutes, 45 seconds
Output 625/1000: t=6240000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 27 minutes, 52 seconds
  Estimated time remaining to next output: 7 minutes, 45 seconds
Output 626/1000: t=6250000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 18 minutes, 31 seconds
  Estimated time remaining to next output: 7 minutes, 45 seconds
Output 627/1000: t=6260000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 days, 9 minutes, 11 seconds
  Estimated time remaining to next output: 7 minutes, 44 seconds
Output 628/1000: t=6270000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 23 hours, 59 minutes, 57 seconds
  Estimated time remaining to next output: 7 minutes, 44 seconds
Output 629/1000: t=6280000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 23 hours, 50 minutes, 40 seconds
  Estimated time remaining to next output: 7 minutes, 44 seconds
Output 630/1000: t=6290000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 23 hours, 41 minutes, 35 seconds
  Estimated time remaining to next output: 7 minutes, 44 seconds
Output 631/1000: t=6300000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 23 hours, 32 minutes, 43 seconds
  Estimated time remaining to next output: 7 minutes, 43 seconds
Output 632/1000: t=6310000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 23 hours, 23 minutes, 41 seconds
  Estimated time remaining to next output: 7 minutes, 43 seconds
Output 633/1000: t=6320000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 23 hours, 14 minutes, 32 seconds
  Estimated time remaining to next output: 7 minutes, 43 seconds
Output 634/1000: t=6330000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 23 hours, 5 minutes, 10 seconds
  Estimated time remaining to next output: 7 minutes, 43 seconds
Output 635/1000: t=6340000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 22 hours, 56 minutes, 5 seconds
  Estimated time remaining to next output: 7 minutes, 42 seconds
Output 636/1000: t=6350000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 22 hours, 47 minutes, 2 seconds
  Estimated time remaining to next output: 7 minutes, 42 seconds
Output 637/1000: t=6360000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 22 hours, 38 minutes, 3 seconds
  Estimated time remaining to next output: 7 minutes, 42 seconds
Output 638/1000: t=6370000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 22 hours, 28 minutes, 53 seconds
  Estimated time remaining to next output: 7 minutes, 42 seconds
Output 639/1000: t=6380000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 22 hours, 19 minutes, 43 seconds
  Estimated time remaining to next output: 7 minutes, 42 seconds
Output 640/1000: t=6390000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 22 hours, 10 minutes, 29 seconds
  Estimated time remaining to next output: 7 minutes, 41 seconds
Output 641/1000: t=6400000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 22 hours, 1 minutes, 30 seconds
  Estimated time remaining to next output: 7 minutes, 41 seconds
Output 642/1000: t=6410000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 21 hours, 52 minutes, 26 seconds
  Estimated time remaining to next output: 7 minutes, 41 seconds
Output 643/1000: t=6420000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 21 hours, 43 minutes, 13 seconds
  Estimated time remaining to next output: 7 minutes, 41 seconds
Output 644/1000: t=6430000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 21 hours, 34 minutes, 19 seconds
  Estimated time remaining to next output: 7 minutes, 40 seconds
Output 645/1000: t=6440000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 21 hours, 25 minutes, 19 seconds
  Estimated time remaining to next output: 7 minutes, 40 seconds
Output 646/1000: t=6450000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 21 hours, 16 minutes, 25 seconds
  Estimated time remaining to next output: 7 minutes, 40 seconds
Output 647/1000: t=6460000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 21 hours, 7 minutes, 18 seconds
  Estimated time remaining to next output: 7 minutes, 40 seconds
Output 648/1000: t=6470000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 20 hours, 58 minutes, 7 seconds
  Estimated time remaining to next output: 7 minutes, 39 seconds
Output 649/1000: t=6480000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 20 hours, 49 minutes, 9 seconds
  Estimated time remaining to next output: 7 minutes, 39 seconds
Output 650/1000: t=6490000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 20 hours, 40 minutes, 21 seconds
  Estimated time remaining to next output: 7 minutes, 39 seconds
Output 651/1000: t=6500000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 20 hours, 31 minutes, 18 seconds
  Estimated time remaining to next output: 7 minutes, 39 seconds
Output 652/1000: t=6510000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 20 hours, 22 minutes, 14 seconds
  Estimated time remaining to next output: 7 minutes, 39 seconds
Output 653/1000: t=6520000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 20 hours, 13 minutes, 10 seconds
  Estimated time remaining to next output: 7 minutes, 38 seconds
Output 654/1000: t=6530000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 20 hours, 4 minutes, 10 seconds
  Estimated time remaining to next output: 7 minutes, 38 seconds
Output 655/1000: t=6540000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 19 hours, 55 minutes, 19 seconds
  Estimated time remaining to next output: 7 minutes, 38 seconds
Output 656/1000: t=6550000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 19 hours, 46 minutes, 12 seconds
  Estimated time remaining to next output: 7 minutes, 38 seconds
Output 657/1000: t=6560000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 19 hours, 37 minutes, 19 seconds
  Estimated time remaining to next output: 7 minutes, 37 seconds
Output 658/1000: t=6570000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 19 hours, 28 minutes, 33 seconds
  Estimated time remaining to next output: 7 minutes, 37 seconds
Output 659/1000: t=6580000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 19 hours, 19 minutes, 45 seconds
  Estimated time remaining to next output: 7 minutes, 37 seconds
Output 660/1000: t=6590000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 19 hours, 10 minutes, 56 seconds
  Estimated time remaining to next output: 7 minutes, 37 seconds
Output 661/1000: t=6600000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 19 hours, 2 minutes, 13 seconds
  Estimated time remaining to next output: 7 minutes, 37 seconds
Output 662/1000: t=6610000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 18 hours, 53 minutes, 16 seconds
  Estimated time remaining to next output: 7 minutes, 36 seconds
Output 663/1000: t=6620000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 18 hours, 44 minutes, 25 seconds
  Estimated time remaining to next output: 7 minutes, 36 seconds
Output 664/1000: t=6630000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 18 hours, 35 minutes, 33 seconds
  Estimated time remaining to next output: 7 minutes, 36 seconds
Output 665/1000: t=6640000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 18 hours, 27 minutes, 1 seconds
  Estimated time remaining to next output: 7 minutes, 36 seconds
Output 666/1000: t=6650000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 18 hours, 18 minutes, 27 seconds
  Estimated time remaining to next output: 7 minutes, 36 seconds
Output 667/1000: t=6660000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 18 hours, 9 minutes, 29 seconds
  Estimated time remaining to next output: 7 minutes, 35 seconds
Output 668/1000: t=6670000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 18 hours, 49 seconds
  Estimated time remaining to next output: 7 minutes, 35 seconds
Output 669/1000: t=6680000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 17 hours, 52 minutes, 13 seconds
  Estimated time remaining to next output: 7 minutes, 35 seconds
Output 670/1000: t=6690000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 17 hours, 43 minutes, 51 seconds
  Estimated time remaining to next output: 7 minutes, 35 seconds
Output 671/1000: t=6700000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 17 hours, 35 minutes, 16 seconds
  Estimated time remaining to next output: 7 minutes, 35 seconds
Output 672/1000: t=6710000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 17 hours, 26 minutes, 52 seconds
  Estimated time remaining to next output: 7 minutes, 34 seconds
Output 673/1000: t=6720000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 17 hours, 18 minutes, 13 seconds
  Estimated time remaining to next output: 7 minutes, 34 seconds
Output 674/1000: t=6730000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 17 hours, 9 minutes, 49 seconds
  Estimated time remaining to next output: 7 minutes, 34 seconds
Output 675/1000: t=6740000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 17 hours, 1 minutes, 47 seconds
  Estimated time remaining to next output: 7 minutes, 34 seconds
Output 676/1000: t=6750000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 16 hours, 53 minutes, 17 seconds
  Estimated time remaining to next output: 7 minutes, 34 seconds
Output 677/1000: t=6760000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 16 hours, 44 minutes, 43 seconds
  Estimated time remaining to next output: 7 minutes, 34 seconds
Output 678/1000: t=6770000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 16 hours, 35 minutes, 53 seconds
  Estimated time remaining to next output: 7 minutes, 33 seconds
Output 679/1000: t=6780000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 16 hours, 27 minutes, 12 seconds
  Estimated time remaining to next output: 7 minutes, 33 seconds
Output 680/1000: t=6790000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 16 hours, 18 minutes, 30 seconds
  Estimated time remaining to next output: 7 minutes, 33 seconds
Output 681/1000: t=6800000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 16 hours, 9 minutes, 46 seconds
  Estimated time remaining to next output: 7 minutes, 33 seconds
Output 682/1000: t=6810000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 16 hours, 1 minutes, 13 seconds
  Estimated time remaining to next output: 7 minutes, 33 seconds
Output 683/1000: t=6820000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 15 hours, 52 minutes, 37 seconds
  Estimated time remaining to next output: 7 minutes, 32 seconds
Output 684/1000: t=6830000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 15 hours, 44 minutes, 4 seconds
  Estimated time remaining to next output: 7 minutes, 32 seconds
Output 685/1000: t=6840000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 15 hours, 35 minutes, 30 seconds
  Estimated time remaining to next output: 7 minutes, 32 seconds
Output 686/1000: t=6850000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 15 hours, 26 minutes, 54 seconds
  Estimated time remaining to next output: 7 minutes, 32 seconds
Output 687/1000: t=6860000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 15 hours, 18 minutes, 7 seconds
  Estimated time remaining to next output: 7 minutes, 32 seconds
Output 688/1000: t=6870000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 15 hours, 9 minutes, 38 seconds
  Estimated time remaining to next output: 7 minutes, 31 seconds
Output 689/1000: t=6880000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 15 hours, 1 minutes, 7 seconds
  Estimated time remaining to next output: 7 minutes, 31 seconds
Output 690/1000: t=6890000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 14 hours, 52 minutes, 25 seconds
  Estimated time remaining to next output: 7 minutes, 31 seconds
Output 691/1000: t=6900000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 14 hours, 43 minutes, 52 seconds
  Estimated time remaining to next output: 7 minutes, 31 seconds
Output 692/1000: t=6910000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 14 hours, 35 minutes, 26 seconds
  Estimated time remaining to next output: 7 minutes, 31 seconds
Output 693/1000: t=6920000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 14 hours, 27 minutes, 3 seconds
  Estimated time remaining to next output: 7 minutes, 30 seconds
Output 694/1000: t=6930000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 14 hours, 18 minutes, 32 seconds
  Estimated time remaining to next output: 7 minutes, 30 seconds
Output 695/1000: t=6940000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 14 hours, 9 minutes, 56 seconds
  Estimated time remaining to next output: 7 minutes, 30 seconds
Output 696/1000: t=6950000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 14 hours, 1 minutes, 21 seconds
  Estimated time remaining to next output: 7 minutes, 30 seconds
Output 697/1000: t=6960000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 13 hours, 52 minutes, 55 seconds
  Estimated time remaining to next output: 7 minutes, 30 seconds
Output 698/1000: t=6970000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 13 hours, 44 minutes, 24 seconds
  Estimated time remaining to next output: 7 minutes, 29 seconds
Output 699/1000: t=6980000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 13 hours, 36 minutes, 3 seconds
  Estimated time remaining to next output: 7 minutes, 29 seconds
Output 700/1000: t=6990000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 13 hours, 27 minutes, 50 seconds
  Estimated time remaining to next output: 7 minutes, 29 seconds
Output 701/1000: t=7000000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 13 hours, 19 minutes, 39 seconds
  Estimated time remaining to next output: 7 minutes, 29 seconds
Output 702/1000: t=7010000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 13 hours, 11 minutes, 28 seconds
  Estimated time remaining to next output: 7 minutes, 29 seconds
Output 703/1000: t=7020000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 13 hours, 3 minutes
  Estimated time remaining to next output: 7 minutes, 29 seconds
Output 704/1000: t=7030000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 12 hours, 55 minutes, 7 seconds
  Estimated time remaining to next output: 7 minutes, 29 seconds
Output 705/1000: t=7040000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 12 hours, 47 minutes, 22 seconds
  Estimated time remaining to next output: 7 minutes, 28 seconds
Output 706/1000: t=7050000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 12 hours, 39 minutes, 14 seconds
  Estimated time remaining to next output: 7 minutes, 28 seconds
Output 707/1000: t=7060000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 12 hours, 30 minutes, 46 seconds
  Estimated time remaining to next output: 7 minutes, 28 seconds
Output 708/1000: t=7070000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 12 hours, 22 minutes, 25 seconds
  Estimated time remaining to next output: 7 minutes, 28 seconds
Output 709/1000: t=7080000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 12 hours, 14 minutes, 12 seconds
  Estimated time remaining to next output: 7 minutes, 28 seconds
Output 710/1000: t=7090000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 12 hours, 6 minutes, 2 seconds
  Estimated time remaining to next output: 7 minutes, 28 seconds
Output 711/1000: t=7100000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 11 hours, 57 minutes, 54 seconds
  Estimated time remaining to next output: 7 minutes, 28 seconds
Output 712/1000: t=7110000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 11 hours, 49 minutes, 30 seconds
  Estimated time remaining to next output: 7 minutes, 27 seconds
Output 713/1000: t=7120000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 11 hours, 41 minutes, 5 seconds
  Estimated time remaining to next output: 7 minutes, 27 seconds
Output 714/1000: t=7130000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 11 hours, 32 minutes, 32 seconds
  Estimated time remaining to next output: 7 minutes, 27 seconds
Output 715/1000: t=7140000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 11 hours, 24 minutes, 14 seconds
  Estimated time remaining to next output: 7 minutes, 27 seconds
Output 716/1000: t=7150000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 11 hours, 16 minutes, 7 seconds
  Estimated time remaining to next output: 7 minutes, 27 seconds
Output 717/1000: t=7160000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 11 hours, 7 minutes, 47 seconds
  Estimated time remaining to next output: 7 minutes, 26 seconds
Output 718/1000: t=7170000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 10 hours, 59 minutes, 35 seconds
  Estimated time remaining to next output: 7 minutes, 26 seconds
Output 719/1000: t=7180000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 10 hours, 51 minutes, 28 seconds
  Estimated time remaining to next output: 7 minutes, 26 seconds
Output 720/1000: t=7190000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 10 hours, 43 minutes, 32 seconds
  Estimated time remaining to next output: 7 minutes, 26 seconds
Output 721/1000: t=7200000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 10 hours, 35 minutes, 28 seconds
  Estimated time remaining to next output: 7 minutes, 26 seconds
Output 722/1000: t=7210000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 10 hours, 27 minutes, 12 seconds
  Estimated time remaining to next output: 7 minutes, 26 seconds
Output 723/1000: t=7220000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 10 hours, 19 minutes, 2 seconds
  Estimated time remaining to next output: 7 minutes, 26 seconds
Output 724/1000: t=7230000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 10 hours, 10 minutes, 46 seconds
  Estimated time remaining to next output: 7 minutes, 25 seconds
Output 725/1000: t=7240000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 10 hours, 2 minutes, 27 seconds
  Estimated time remaining to next output: 7 minutes, 25 seconds
Output 726/1000: t=7250000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 9 hours, 54 minutes, 15 seconds
  Estimated time remaining to next output: 7 minutes, 25 seconds
Output 727/1000: t=7260000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 9 hours, 45 minutes, 55 seconds
  Estimated time remaining to next output: 7 minutes, 25 seconds
Output 728/1000: t=7270000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 9 hours, 37 minutes, 34 seconds
  Estimated time remaining to next output: 7 minutes, 25 seconds
Output 729/1000: t=7280000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 9 hours, 29 minutes, 12 seconds
  Estimated time remaining to next output: 7 minutes, 24 seconds
Output 730/1000: t=7290000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 9 hours, 21 minutes, 8 seconds
  Estimated time remaining to next output: 7 minutes, 24 seconds
Output 731/1000: t=7300000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 9 hours, 13 minutes, 1 seconds
  Estimated time remaining to next output: 7 minutes, 24 seconds
Output 732/1000: t=7310000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 9 hours, 4 minutes, 43 seconds
  Estimated time remaining to next output: 7 minutes, 24 seconds
Output 733/1000: t=7320000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 8 hours, 56 minutes, 25 seconds
  Estimated time remaining to next output: 7 minutes, 24 seconds
Output 734/1000: t=7330000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 8 hours, 48 minutes, 10 seconds
  Estimated time remaining to next output: 7 minutes, 23 seconds
Output 735/1000: t=7340000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 8 hours, 40 minutes
  Estimated time remaining to next output: 7 minutes, 23 seconds
Output 736/1000: t=7350000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 8 hours, 31 minutes, 53 seconds
  Estimated time remaining to next output: 7 minutes, 23 seconds
Output 737/1000: t=7360000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 8 hours, 23 minutes, 42 seconds
  Estimated time remaining to next output: 7 minutes, 23 seconds
Output 738/1000: t=7370000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 8 hours, 15 minutes, 31 seconds
  Estimated time remaining to next output: 7 minutes, 23 seconds
Output 739/1000: t=7380000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 8 hours, 7 minutes, 23 seconds
  Estimated time remaining to next output: 7 minutes, 23 seconds
Output 740/1000: t=7390000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 7 hours, 59 minutes, 12 seconds
  Estimated time remaining to next output: 7 minutes, 22 seconds
Output 741/1000: t=7400000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 7 hours, 51 minutes, 21 seconds
  Estimated time remaining to next output: 7 minutes, 22 seconds
Output 742/1000: t=7410000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 7 hours, 43 minutes, 15 seconds
  Estimated time remaining to next output: 7 minutes, 22 seconds
Output 743/1000: t=7420000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 7 hours, 35 minutes, 7 seconds
  Estimated time remaining to next output: 7 minutes, 22 seconds
Output 744/1000: t=7430000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 7 hours, 27 minutes, 8 seconds
  Estimated time remaining to next output: 7 minutes, 22 seconds
Output 745/1000: t=7440000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 7 hours, 19 minutes, 1 seconds
  Estimated time remaining to next output: 7 minutes, 22 seconds
Output 746/1000: t=7450000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 7 hours, 10 minutes, 53 seconds
  Estimated time remaining to next output: 7 minutes, 21 seconds
Output 747/1000: t=7460000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 7 hours, 2 minutes, 42 seconds
  Estimated time remaining to next output: 7 minutes, 21 seconds
Output 748/1000: t=7470000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 6 hours, 54 minutes, 43 seconds
  Estimated time remaining to next output: 7 minutes, 21 seconds
Output 749/1000: t=7480000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 6 hours, 46 minutes, 42 seconds
  Estimated time remaining to next output: 7 minutes, 21 seconds
Output 750/1000: t=7490000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 6 hours, 38 minutes, 33 seconds
  Estimated time remaining to next output: 7 minutes, 21 seconds
Output 751/1000: t=7500000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 6 hours, 30 minutes, 34 seconds
  Estimated time remaining to next output: 7 minutes, 21 seconds
Output 752/1000: t=7510000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 6 hours, 22 minutes, 36 seconds
  Estimated time remaining to next output: 7 minutes, 20 seconds
Output 753/1000: t=7520000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 6 hours, 14 minutes, 36 seconds
  Estimated time remaining to next output: 7 minutes, 20 seconds
Output 754/1000: t=7530000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 6 hours, 6 minutes, 29 seconds
  Estimated time remaining to next output: 7 minutes, 20 seconds
Output 755/1000: t=7540000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 5 hours, 58 minutes, 24 seconds
  Estimated time remaining to next output: 7 minutes, 20 seconds
Output 756/1000: t=7550000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 5 hours, 50 minutes, 18 seconds
  Estimated time remaining to next output: 7 minutes, 20 seconds
Output 757/1000: t=7560000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 5 hours, 42 minutes, 18 seconds
  Estimated time remaining to next output: 7 minutes, 20 seconds
Output 758/1000: t=7570000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 5 hours, 34 minutes, 22 seconds
  Estimated time remaining to next output: 7 minutes, 19 seconds
Output 759/1000: t=7580000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 5 hours, 26 minutes, 23 seconds
  Estimated time remaining to next output: 7 minutes, 19 seconds
Output 760/1000: t=7590000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 5 hours, 18 minutes, 24 seconds
  Estimated time remaining to next output: 7 minutes, 19 seconds
Output 761/1000: t=7600000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 5 hours, 10 minutes, 21 seconds
  Estimated time remaining to next output: 7 minutes, 19 seconds
Output 762/1000: t=7610000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 5 hours, 2 minutes, 25 seconds
  Estimated time remaining to next output: 7 minutes, 19 seconds
Output 763/1000: t=7620000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 4 hours, 54 minutes, 31 seconds
  Estimated time remaining to next output: 7 minutes, 19 seconds
Output 764/1000: t=7630000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 4 hours, 46 minutes, 30 seconds
  Estimated time remaining to next output: 7 minutes, 18 seconds
Output 765/1000: t=7640000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 4 hours, 38 minutes, 25 seconds
  Estimated time remaining to next output: 7 minutes, 18 seconds
Output 766/1000: t=7650000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 4 hours, 30 minutes, 32 seconds
  Estimated time remaining to next output: 7 minutes, 18 seconds
Output 767/1000: t=7660000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 4 hours, 22 minutes, 31 seconds
  Estimated time remaining to next output: 7 minutes, 18 seconds
Output 768/1000: t=7670000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 4 hours, 14 minutes, 31 seconds
  Estimated time remaining to next output: 7 minutes, 18 seconds
Output 769/1000: t=7680000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 4 hours, 6 minutes, 41 seconds
  Estimated time remaining to next output: 7 minutes, 18 seconds
Output 770/1000: t=7690000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 3 hours, 58 minutes, 49 seconds
  Estimated time remaining to next output: 7 minutes, 17 seconds
Output 771/1000: t=7700000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 3 hours, 50 minutes, 59 seconds
  Estimated time remaining to next output: 7 minutes, 17 seconds
Output 772/1000: t=7710000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 3 hours, 42 minutes, 57 seconds
  Estimated time remaining to next output: 7 minutes, 17 seconds
Output 773/1000: t=7720000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 3 hours, 35 minutes, 2 seconds
  Estimated time remaining to next output: 7 minutes, 17 seconds
Output 774/1000: t=7730000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 3 hours, 27 minutes, 7 seconds
  Estimated time remaining to next output: 7 minutes, 17 seconds
Output 775/1000: t=7740000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 3 hours, 19 minutes, 18 seconds
  Estimated time remaining to next output: 7 minutes, 17 seconds
Output 776/1000: t=7750000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 3 hours, 11 minutes, 26 seconds
  Estimated time remaining to next output: 7 minutes, 16 seconds
Output 777/1000: t=7760000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 3 hours, 3 minutes, 30 seconds
  Estimated time remaining to next output: 7 minutes, 16 seconds
Output 778/1000: t=7770000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 2 hours, 55 minutes, 36 seconds
  Estimated time remaining to next output: 7 minutes, 16 seconds
Output 779/1000: t=7780000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 2 hours, 47 minutes, 44 seconds
  Estimated time remaining to next output: 7 minutes, 16 seconds
Output 780/1000: t=7790000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 2 hours, 39 minutes, 58 seconds
  Estimated time remaining to next output: 7 minutes, 16 seconds
Output 781/1000: t=7800000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 2 hours, 32 minutes, 9 seconds
  Estimated time remaining to next output: 7 minutes, 16 seconds
Output 782/1000: t=7810000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 2 hours, 24 minutes, 18 seconds
  Estimated time remaining to next output: 7 minutes, 16 seconds
Output 783/1000: t=7820000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 2 hours, 16 minutes, 32 seconds
  Estimated time remaining to next output: 7 minutes, 15 seconds
Output 784/1000: t=7830000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 2 hours, 8 minutes, 41 seconds
  Estimated time remaining to next output: 7 minutes, 15 seconds
Output 785/1000: t=7840000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 2 hours, 49 seconds
  Estimated time remaining to next output: 7 minutes, 15 seconds
Output 786/1000: t=7850000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 1 hours, 53 minutes, 1 seconds
  Estimated time remaining to next output: 7 minutes, 15 seconds
Output 787/1000: t=7860000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 1 hours, 45 minutes, 9 seconds
  Estimated time remaining to next output: 7 minutes, 15 seconds
Output 788/1000: t=7870000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 1 hours, 37 minutes, 20 seconds
  Estimated time remaining to next output: 7 minutes, 15 seconds
Output 789/1000: t=7880000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 1 hours, 29 minutes, 33 seconds
  Estimated time remaining to next output: 7 minutes, 14 seconds
Output 790/1000: t=7890000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 1 hours, 21 minutes, 43 seconds
  Estimated time remaining to next output: 7 minutes, 14 seconds
Output 791/1000: t=7900000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 1 hours, 14 minutes, 1 seconds
  Estimated time remaining to next output: 7 minutes, 14 seconds
Output 792/1000: t=7910000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 1 hours, 6 minutes, 17 seconds
  Estimated time remaining to next output: 7 minutes, 14 seconds
Output 793/1000: t=7920000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 58 minutes, 25 seconds
  Estimated time remaining to next output: 7 minutes, 14 seconds
Output 794/1000: t=7930000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 50 minutes, 38 seconds
  Estimated time remaining to next output: 7 minutes, 14 seconds
Output 795/1000: t=7940000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 42 minutes, 51 seconds
  Estimated time remaining to next output: 7 minutes, 14 seconds
Output 796/1000: t=7950000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 35 minutes, 9 seconds
  Estimated time remaining to next output: 7 minutes, 13 seconds
Output 797/1000: t=7960000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 27 minutes, 19 seconds
  Estimated time remaining to next output: 7 minutes, 13 seconds
Output 798/1000: t=7970000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 19 minutes, 29 seconds
  Estimated time remaining to next output: 7 minutes, 13 seconds
Output 799/1000: t=7980000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 11 minutes, 41 seconds
  Estimated time remaining to next output: 7 minutes, 13 seconds
Output 800/1000: t=7990000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 days, 3 minutes, 59 seconds
  Estimated time remaining to next output: 7 minutes, 13 seconds
Output 801/1000: t=8000000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 23 hours, 56 minutes, 20 seconds
  Estimated time remaining to next output: 7 minutes, 13 seconds
Output 802/1000: t=8010000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 23 hours, 48 minutes, 32 seconds
  Estimated time remaining to next output: 7 minutes, 12 seconds
Output 803/1000: t=8020000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 23 hours, 40 minutes, 49 seconds
  Estimated time remaining to next output: 7 minutes, 12 seconds
Output 804/1000: t=8030000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 23 hours, 33 minutes, 9 seconds
  Estimated time remaining to next output: 7 minutes, 12 seconds
Output 805/1000: t=8040000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 23 hours, 25 minutes, 32 seconds
  Estimated time remaining to next output: 7 minutes, 12 seconds
Output 806/1000: t=8050000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 23 hours, 17 minutes, 54 seconds
  Estimated time remaining to next output: 7 minutes, 12 seconds
Output 807/1000: t=8060000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 23 hours, 10 minutes, 11 seconds
  Estimated time remaining to next output: 7 minutes, 12 seconds
Output 808/1000: t=8070000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 23 hours, 2 minutes, 30 seconds
  Estimated time remaining to next output: 7 minutes, 12 seconds
Output 809/1000: t=8080000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 22 hours, 54 minutes, 50 seconds
  Estimated time remaining to next output: 7 minutes, 11 seconds
Output 810/1000: t=8090000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 22 hours, 47 minutes, 47 seconds
  Estimated time remaining to next output: 7 minutes, 11 seconds
Output 811/1000: t=8100000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 22 hours, 40 minutes, 44 seconds
  Estimated time remaining to next output: 7 minutes, 11 seconds
Output 812/1000: t=8110000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 22 hours, 33 minutes, 41 seconds
  Estimated time remaining to next output: 7 minutes, 12 seconds
Output 813/1000: t=8120000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 22 hours, 26 minutes, 15 seconds
  Estimated time remaining to next output: 7 minutes, 11 seconds
Output 814/1000: t=8130000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 22 hours, 19 minutes, 21 seconds
  Estimated time remaining to next output: 7 minutes, 12 seconds
Output 815/1000: t=8140000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 22 hours, 12 minutes, 38 seconds
  Estimated time remaining to next output: 7 minutes, 12 seconds
Output 816/1000: t=8150000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 22 hours, 5 minutes, 8 seconds
  Estimated time remaining to next output: 7 minutes, 12 seconds
Output 817/1000: t=8160000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 21 hours, 58 minutes, 25 seconds
  Estimated time remaining to next output: 7 minutes, 12 seconds
Output 818/1000: t=8170000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 21 hours, 51 minutes, 28 seconds
  Estimated time remaining to next output: 7 minutes, 12 seconds
Output 819/1000: t=8180000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 21 hours, 44 minutes, 34 seconds
  Estimated time remaining to next output: 7 minutes, 12 seconds
Output 820/1000: t=8190000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 21 hours, 37 minutes, 41 seconds
  Estimated time remaining to next output: 7 minutes, 12 seconds
Output 821/1000: t=8200000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 21 hours, 30 minutes, 39 seconds
  Estimated time remaining to next output: 7 minutes, 12 seconds
Output 822/1000: t=8210000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 21 hours, 23 minutes, 12 seconds
  Estimated time remaining to next output: 7 minutes, 12 seconds
Output 823/1000: t=8220000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 21 hours, 16 minutes, 16 seconds
  Estimated time remaining to next output: 7 minutes, 12 seconds
Output 824/1000: t=8230000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 21 hours, 9 minutes, 24 seconds
  Estimated time remaining to next output: 7 minutes, 12 seconds
Output 825/1000: t=8240000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 21 hours, 2 minutes, 36 seconds
  Estimated time remaining to next output: 7 minutes, 12 seconds
Output 826/1000: t=8250000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 20 hours, 55 minutes, 48 seconds
  Estimated time remaining to next output: 7 minutes, 13 seconds
Output 827/1000: t=8260000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 20 hours, 48 minutes, 48 seconds
  Estimated time remaining to next output: 7 minutes, 13 seconds
Output 828/1000: t=8270000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 20 hours, 42 minutes, 3 seconds
  Estimated time remaining to next output: 7 minutes, 13 seconds
Output 829/1000: t=8280000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 20 hours, 35 minutes, 2 seconds
  Estimated time remaining to next output: 7 minutes, 13 seconds
Output 830/1000: t=8290000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 20 hours, 28 minutes, 15 seconds
  Estimated time remaining to next output: 7 minutes, 13 seconds
Output 831/1000: t=8300000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 20 hours, 21 minutes, 13 seconds
  Estimated time remaining to next output: 7 minutes, 13 seconds
Output 832/1000: t=8310000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 20 hours, 13 minutes, 58 seconds
  Estimated time remaining to next output: 7 minutes, 13 seconds
Output 833/1000: t=8320000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 20 hours, 7 minutes, 11 seconds
  Estimated time remaining to next output: 7 minutes, 13 seconds
Output 834/1000: t=8330000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 19 hours, 59 minutes, 59 seconds
  Estimated time remaining to next output: 7 minutes, 13 seconds
Output 835/1000: t=8340000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 19 hours, 53 minutes, 9 seconds
  Estimated time remaining to next output: 7 minutes, 13 seconds
Output 836/1000: t=8350000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 19 hours, 46 minutes, 25 seconds
  Estimated time remaining to next output: 7 minutes, 14 seconds
Output 837/1000: t=8360000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 19 hours, 39 minutes, 28 seconds
  Estimated time remaining to next output: 7 minutes, 14 seconds
Output 838/1000: t=8370000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 19 hours, 32 minutes, 33 seconds
  Estimated time remaining to next output: 7 minutes, 14 seconds
Output 839/1000: t=8380000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 19 hours, 25 minutes, 34 seconds
  Estimated time remaining to next output: 7 minutes, 14 seconds
Output 840/1000: t=8390000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 19 hours, 18 minutes, 35 seconds
  Estimated time remaining to next output: 7 minutes, 14 seconds
Output 841/1000: t=8400000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 19 hours, 12 minutes, 2 seconds
  Estimated time remaining to next output: 7 minutes, 14 seconds
Output 842/1000: t=8410000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 19 hours, 5 minutes, 13 seconds
  Estimated time remaining to next output: 7 minutes, 14 seconds
Output 843/1000: t=8420000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 18 hours, 58 minutes, 29 seconds
  Estimated time remaining to next output: 7 minutes, 15 seconds
Output 844/1000: t=8430000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 18 hours, 51 minutes, 25 seconds
  Estimated time remaining to next output: 7 minutes, 15 seconds
Output 845/1000: t=8440000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 18 hours, 44 minutes, 23 seconds
  Estimated time remaining to next output: 7 minutes, 15 seconds
Output 846/1000: t=8450000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 18 hours, 37 minutes, 26 seconds
  Estimated time remaining to next output: 7 minutes, 15 seconds
Output 847/1000: t=8460000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 18 hours, 30 minutes, 30 seconds
  Estimated time remaining to next output: 7 minutes, 15 seconds
Output 848/1000: t=8470000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 18 hours, 23 minutes, 15 seconds
  Estimated time remaining to next output: 7 minutes, 15 seconds
Output 849/1000: t=8480000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 18 hours, 15 minutes, 46 seconds
  Estimated time remaining to next output: 7 minutes, 15 seconds
Output 850/1000: t=8490000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 18 hours, 8 minutes, 56 seconds
  Estimated time remaining to next output: 7 minutes, 15 seconds
Output 851/1000: t=8500000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 18 hours, 2 minutes, 7 seconds
  Estimated time remaining to next output: 7 minutes, 15 seconds
Output 852/1000: t=8510000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 17 hours, 55 minutes, 8 seconds
  Estimated time remaining to next output: 7 minutes, 15 seconds
Output 853/1000: t=8520000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 17 hours, 48 minutes, 4 seconds
  Estimated time remaining to next output: 7 minutes, 15 seconds
Output 854/1000: t=8530000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 17 hours, 40 minutes, 26 seconds
  Estimated time remaining to next output: 7 minutes, 15 seconds
Output 855/1000: t=8540000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 17 hours, 32 minutes, 49 seconds
  Estimated time remaining to next output: 7 minutes, 15 seconds
Output 856/1000: t=8550000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 17 hours, 25 minutes, 10 seconds
  Estimated time remaining to next output: 7 minutes, 15 seconds
Output 857/1000: t=8560000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 17 hours, 17 minutes, 35 seconds
  Estimated time remaining to next output: 7 minutes, 15 seconds
Output 858/1000: t=8570000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 17 hours, 9 minutes, 57 seconds
  Estimated time remaining to next output: 7 minutes, 15 seconds
Output 859/1000: t=8580000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 17 hours, 2 minutes, 22 seconds
  Estimated time remaining to next output: 7 minutes, 15 seconds
Output 860/1000: t=8590000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 16 hours, 54 minutes, 45 seconds
  Estimated time remaining to next output: 7 minutes, 14 seconds
Output 861/1000: t=8600000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 16 hours, 47 minutes, 9 seconds
  Estimated time remaining to next output: 7 minutes, 14 seconds
Output 862/1000: t=8610000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 16 hours, 39 minutes, 42 seconds
  Estimated time remaining to next output: 7 minutes, 14 seconds
Output 863/1000: t=8620000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 16 hours, 32 minutes, 22 seconds
  Estimated time remaining to next output: 7 minutes, 14 seconds
Output 864/1000: t=8630000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 16 hours, 25 minutes, 27 seconds
  Estimated time remaining to next output: 7 minutes, 14 seconds
Output 865/1000: t=8640000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 16 hours, 18 minutes, 31 seconds
  Estimated time remaining to next output: 7 minutes, 14 seconds
Output 866/1000: t=8650000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 16 hours, 11 minutes, 38 seconds
  Estimated time remaining to next output: 7 minutes, 15 seconds
Output 867/1000: t=8660000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 16 hours, 4 minutes, 43 seconds
  Estimated time remaining to next output: 7 minutes, 15 seconds
Output 868/1000: t=8670000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 15 hours, 57 minutes, 52 seconds
  Estimated time remaining to next output: 7 minutes, 15 seconds
Output 869/1000: t=8680000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 15 hours, 50 minutes, 53 seconds
  Estimated time remaining to next output: 7 minutes, 15 seconds
Output 870/1000: t=8690000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 15 hours, 43 minutes, 52 seconds
  Estimated time remaining to next output: 7 minutes, 15 seconds
Output 871/1000: t=8700000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 15 hours, 36 minutes, 48 seconds
  Estimated time remaining to next output: 7 minutes, 15 seconds
Output 872/1000: t=8710000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 15 hours, 29 minutes, 48 seconds
  Estimated time remaining to next output: 7 minutes, 15 seconds
Output 873/1000: t=8720000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 15 hours, 22 minutes, 44 seconds
  Estimated time remaining to next output: 7 minutes, 15 seconds
Output 874/1000: t=8730000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 15 hours, 15 minutes, 45 seconds
  Estimated time remaining to next output: 7 minutes, 16 seconds
Output 875/1000: t=8740000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 15 hours, 8 minutes, 49 seconds
  Estimated time remaining to next output: 7 minutes, 16 seconds
Output 876/1000: t=8750000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 15 hours, 1 minutes, 48 seconds
  Estimated time remaining to next output: 7 minutes, 16 seconds
Output 877/1000: t=8760000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 14 hours, 54 minutes, 49 seconds
  Estimated time remaining to next output: 7 minutes, 16 seconds
Output 878/1000: t=8770000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 14 hours, 47 minutes, 57 seconds
  Estimated time remaining to next output: 7 minutes, 16 seconds
Output 879/1000: t=8780000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 14 hours, 40 minutes, 59 seconds
  Estimated time remaining to next output: 7 minutes, 16 seconds
Output 880/1000: t=8790000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 14 hours, 34 minutes, 6 seconds
  Estimated time remaining to next output: 7 minutes, 17 seconds
Output 881/1000: t=8800000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 14 hours, 27 minutes, 7 seconds
  Estimated time remaining to next output: 7 minutes, 17 seconds
Output 882/1000: t=8810000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 14 hours, 20 minutes, 4 seconds
  Estimated time remaining to next output: 7 minutes, 17 seconds
Output 883/1000: t=8820000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 14 hours, 13 minutes, 4 seconds
  Estimated time remaining to next output: 7 minutes, 17 seconds
Output 884/1000: t=8830000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 14 hours, 6 minutes, 2 seconds
  Estimated time remaining to next output: 7 minutes, 17 seconds
Output 885/1000: t=8840000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 13 hours, 59 minutes, 1 seconds
  Estimated time remaining to next output: 7 minutes, 17 seconds
Output 886/1000: t=8850000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 13 hours, 52 minutes, 3 seconds
  Estimated time remaining to next output: 7 minutes, 17 seconds
Output 887/1000: t=8860000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 13 hours, 44 minutes, 58 seconds
  Estimated time remaining to next output: 7 minutes, 18 seconds
Output 888/1000: t=8870000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 13 hours, 37 minutes, 27 seconds
  Estimated time remaining to next output: 7 minutes, 17 seconds
Output 889/1000: t=8880000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 13 hours, 29 minutes, 58 seconds
  Estimated time remaining to next output: 7 minutes, 17 seconds
Output 890/1000: t=8890000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 13 hours, 22 minutes, 24 seconds
  Estimated time remaining to next output: 7 minutes, 17 seconds
Output 891/1000: t=8900000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 13 hours, 14 minutes, 50 seconds
  Estimated time remaining to next output: 7 minutes, 17 seconds
Output 892/1000: t=8910000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 13 hours, 7 minutes, 17 seconds
  Estimated time remaining to next output: 7 minutes, 17 seconds
Output 893/1000: t=8920000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 12 hours, 59 minutes, 49 seconds
  Estimated time remaining to next output: 7 minutes, 17 seconds
Output 894/1000: t=8930000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 12 hours, 52 minutes, 19 seconds
  Estimated time remaining to next output: 7 minutes, 17 seconds
Output 895/1000: t=8940000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 12 hours, 44 minutes, 46 seconds
  Estimated time remaining to next output: 7 minutes, 17 seconds
Output 896/1000: t=8950000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 12 hours, 37 minutes, 14 seconds
  Estimated time remaining to next output: 7 minutes, 16 seconds
Output 897/1000: t=8960000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 12 hours, 29 minutes, 45 seconds
  Estimated time remaining to next output: 7 minutes, 16 seconds
Output 898/1000: t=8970000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 12 hours, 22 minutes, 17 seconds
  Estimated time remaining to next output: 7 minutes, 16 seconds
Output 899/1000: t=8980000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 12 hours, 14 minutes, 46 seconds
  Estimated time remaining to next output: 7 minutes, 16 seconds
Output 900/1000: t=8990000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 12 hours, 7 minutes, 15 seconds
  Estimated time remaining to next output: 7 minutes, 16 seconds
Output 901/1000: t=9000000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 11 hours, 59 minutes, 44 seconds
  Estimated time remaining to next output: 7 minutes, 16 seconds
Output 902/1000: t=9010000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 11 hours, 52 minutes, 15 seconds
  Estimated time remaining to next output: 7 minutes, 16 seconds
Output 903/1000: t=9020000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 11 hours, 44 minutes, 47 seconds
  Estimated time remaining to next output: 7 minutes, 15 seconds
Output 904/1000: t=9030000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 11 hours, 37 minutes, 18 seconds
  Estimated time remaining to next output: 7 minutes, 15 seconds
Output 905/1000: t=9040000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 11 hours, 29 minutes, 48 seconds
  Estimated time remaining to next output: 7 minutes, 15 seconds
Output 906/1000: t=9050000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 11 hours, 22 minutes, 21 seconds
  Estimated time remaining to next output: 7 minutes, 15 seconds
Output 907/1000: t=9060000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 11 hours, 14 minutes, 53 seconds
  Estimated time remaining to next output: 7 minutes, 15 seconds
Output 908/1000: t=9070000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 11 hours, 7 minutes, 24 seconds
  Estimated time remaining to next output: 7 minutes, 15 seconds
Output 909/1000: t=9080000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 10 hours, 59 minutes, 59 seconds
  Estimated time remaining to next output: 7 minutes, 15 seconds
Output 910/1000: t=9090000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 10 hours, 52 minutes, 33 seconds
  Estimated time remaining to next output: 7 minutes, 15 seconds
Output 911/1000: t=9100000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 10 hours, 45 minutes, 5 seconds
  Estimated time remaining to next output: 7 minutes, 14 seconds
Output 912/1000: t=9110000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 10 hours, 37 minutes, 42 seconds
  Estimated time remaining to next output: 7 minutes, 14 seconds
Output 913/1000: t=9120000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 10 hours, 30 minutes, 16 seconds
  Estimated time remaining to next output: 7 minutes, 14 seconds
Output 914/1000: t=9130000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 10 hours, 22 minutes, 48 seconds
  Estimated time remaining to next output: 7 minutes, 14 seconds
Output 915/1000: t=9140000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 10 hours, 15 minutes, 22 seconds
  Estimated time remaining to next output: 7 minutes, 14 seconds
Output 916/1000: t=9150000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 10 hours, 7 minutes, 57 seconds
  Estimated time remaining to next output: 7 minutes, 14 seconds
Output 917/1000: t=9160000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 10 hours, 31 seconds
  Estimated time remaining to next output: 7 minutes, 14 seconds
Output 918/1000: t=9170000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 9 hours, 53 minutes, 6 seconds
  Estimated time remaining to next output: 7 minutes, 13 seconds
Output 919/1000: t=9180000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 9 hours, 45 minutes, 42 seconds
  Estimated time remaining to next output: 7 minutes, 13 seconds
Output 920/1000: t=9190000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 9 hours, 38 minutes, 18 seconds
  Estimated time remaining to next output: 7 minutes, 13 seconds
Output 921/1000: t=9200000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 9 hours, 30 minutes, 55 seconds
  Estimated time remaining to next output: 7 minutes, 13 seconds
Output 922/1000: t=9210000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 9 hours, 23 minutes, 32 seconds
  Estimated time remaining to next output: 7 minutes, 13 seconds
Output 923/1000: t=9220000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 9 hours, 16 minutes, 10 seconds
  Estimated time remaining to next output: 7 minutes, 13 seconds
Output 924/1000: t=9230000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 9 hours, 8 minutes, 46 seconds
  Estimated time remaining to next output: 7 minutes, 13 seconds
Output 925/1000: t=9240000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 9 hours, 1 minutes, 22 seconds
  Estimated time remaining to next output: 7 minutes, 13 seconds
Output 926/1000: t=9250000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 8 hours, 54 minutes, 1 seconds
  Estimated time remaining to next output: 7 minutes, 12 seconds
Output 927/1000: t=9260000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 8 hours, 46 minutes, 40 seconds
  Estimated time remaining to next output: 7 minutes, 12 seconds
Output 928/1000: t=9270000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 8 hours, 39 minutes, 17 seconds
  Estimated time remaining to next output: 7 minutes, 12 seconds
Output 929/1000: t=9280000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 8 hours, 31 minutes, 56 seconds
  Estimated time remaining to next output: 7 minutes, 12 seconds
Output 930/1000: t=9290000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 8 hours, 24 minutes, 33 seconds
  Estimated time remaining to next output: 7 minutes, 12 seconds
Output 931/1000: t=9300000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 8 hours, 17 minutes, 10 seconds
  Estimated time remaining to next output: 7 minutes, 12 seconds
Output 932/1000: t=9310000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 8 hours, 9 minutes, 50 seconds
  Estimated time remaining to next output: 7 minutes, 12 seconds
Output 933/1000: t=9320000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 8 hours, 2 minutes, 29 seconds
  Estimated time remaining to next output: 7 minutes, 12 seconds
Output 934/1000: t=9330000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 7 hours, 55 minutes, 10 seconds
  Estimated time remaining to next output: 7 minutes, 11 seconds
Output 935/1000: t=9340000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 7 hours, 47 minutes, 49 seconds
  Estimated time remaining to next output: 7 minutes, 11 seconds
Output 936/1000: t=9350000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 7 hours, 40 minutes, 29 seconds
  Estimated time remaining to next output: 7 minutes, 11 seconds
Output 937/1000: t=9360000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 7 hours, 33 minutes, 9 seconds
  Estimated time remaining to next output: 7 minutes, 11 seconds
Output 938/1000: t=9370000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 7 hours, 25 minutes, 51 seconds
  Estimated time remaining to next output: 7 minutes, 11 seconds
Output 939/1000: t=9380000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 7 hours, 18 minutes, 34 seconds
  Estimated time remaining to next output: 7 minutes, 11 seconds
Output 940/1000: t=9390000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 7 hours, 11 minutes, 15 seconds
  Estimated time remaining to next output: 7 minutes, 11 seconds
Output 941/1000: t=9400000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 7 hours, 3 minutes, 57 seconds
  Estimated time remaining to next output: 7 minutes, 11 seconds
Output 942/1000: t=9410000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 6 hours, 56 minutes, 37 seconds
  Estimated time remaining to next output: 7 minutes, 10 seconds
Output 943/1000: t=9420000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 6 hours, 49 minutes, 19 seconds
  Estimated time remaining to next output: 7 minutes, 10 seconds
Output 944/1000: t=9430000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 6 hours, 42 minutes, 1 seconds
  Estimated time remaining to next output: 7 minutes, 10 seconds
Output 945/1000: t=9440000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 6 hours, 34 minutes, 44 seconds
  Estimated time remaining to next output: 7 minutes, 10 seconds
Output 946/1000: t=9450000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 6 hours, 27 minutes, 27 seconds
  Estimated time remaining to next output: 7 minutes, 10 seconds
Output 947/1000: t=9460000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 6 hours, 20 minutes, 10 seconds
  Estimated time remaining to next output: 7 minutes, 10 seconds
Output 948/1000: t=9470000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 6 hours, 12 minutes, 54 seconds
  Estimated time remaining to next output: 7 minutes, 10 seconds
Output 949/1000: t=9480000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 6 hours, 5 minutes, 37 seconds
  Estimated time remaining to next output: 7 minutes, 10 seconds
Output 950/1000: t=9490000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 5 hours, 58 minutes, 20 seconds
  Estimated time remaining to next output: 7 minutes, 10 seconds
Output 951/1000: t=9500000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 5 hours, 51 minutes, 5 seconds
  Estimated time remaining to next output: 7 minutes, 9 seconds
Output 952/1000: t=9510000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 5 hours, 43 minutes, 49 seconds
  Estimated time remaining to next output: 7 minutes, 9 seconds
Output 953/1000: t=9520000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 5 hours, 36 minutes, 33 seconds
  Estimated time remaining to next output: 7 minutes, 9 seconds
Output 954/1000: t=9530000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 5 hours, 29 minutes, 18 seconds
  Estimated time remaining to next output: 7 minutes, 9 seconds
Output 955/1000: t=9540000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 5 hours, 22 minutes, 4 seconds
  Estimated time remaining to next output: 7 minutes, 9 seconds
Output 956/1000: t=9550000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 5 hours, 14 minutes, 50 seconds
  Estimated time remaining to next output: 7 minutes, 9 seconds
Output 957/1000: t=9560000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 5 hours, 7 minutes, 35 seconds
  Estimated time remaining to next output: 7 minutes, 9 seconds
Output 958/1000: t=9570000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 5 hours, 21 seconds
  Estimated time remaining to next output: 7 minutes, 9 seconds
Output 959/1000: t=9580000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 4 hours, 53 minutes, 7 seconds
  Estimated time remaining to next output: 7 minutes, 8 seconds
Output 960/1000: t=9590000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 4 hours, 45 minutes, 53 seconds
  Estimated time remaining to next output: 7 minutes, 8 seconds
Output 961/1000: t=9600000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 4 hours, 38 minutes, 40 seconds
  Estimated time remaining to next output: 7 minutes, 8 seconds
Output 962/1000: t=9610000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 4 hours, 31 minutes, 26 seconds
  Estimated time remaining to next output: 7 minutes, 8 seconds
Output 963/1000: t=9620000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 4 hours, 24 minutes, 14 seconds
  Estimated time remaining to next output: 7 minutes, 8 seconds
Output 964/1000: t=9630000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 4 hours, 17 minutes, 1 seconds
  Estimated time remaining to next output: 7 minutes, 8 seconds
Output 965/1000: t=9640000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 4 hours, 9 minutes, 49 seconds
  Estimated time remaining to next output: 7 minutes, 8 seconds
Output 966/1000: t=9650000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 4 hours, 2 minutes, 37 seconds
  Estimated time remaining to next output: 7 minutes, 8 seconds
Output 967/1000: t=9660000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 hours, 55 minutes, 26 seconds
  Estimated time remaining to next output: 7 minutes, 8 seconds
Output 968/1000: t=9670000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 hours, 48 minutes, 14 seconds
  Estimated time remaining to next output: 7 minutes, 7 seconds
Output 969/1000: t=9680000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 hours, 41 minutes, 3 seconds
  Estimated time remaining to next output: 7 minutes, 7 seconds
Output 970/1000: t=9690000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 hours, 33 minutes, 51 seconds
  Estimated time remaining to next output: 7 minutes, 7 seconds
Output 971/1000: t=9700000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 hours, 26 minutes, 40 seconds
  Estimated time remaining to next output: 7 minutes, 7 seconds
Output 972/1000: t=9710000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 hours, 19 minutes, 29 seconds
  Estimated time remaining to next output: 7 minutes, 7 seconds
Output 973/1000: t=9720000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 hours, 12 minutes, 18 seconds
  Estimated time remaining to next output: 7 minutes, 7 seconds
Output 974/1000: t=9730000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 3 hours, 5 minutes, 8 seconds
  Estimated time remaining to next output: 7 minutes, 7 seconds
Output 975/1000: t=9740000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 hours, 57 minutes, 58 seconds
  Estimated time remaining to next output: 7 minutes, 7 seconds
Output 976/1000: t=9750000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 hours, 50 minutes, 48 seconds
  Estimated time remaining to next output: 7 minutes, 7 seconds
Output 977/1000: t=9760000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 hours, 43 minutes, 39 seconds
  Estimated time remaining to next output: 7 minutes, 6 seconds
Output 978/1000: t=9770000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 hours, 36 minutes, 29 seconds
  Estimated time remaining to next output: 7 minutes, 6 seconds
Output 979/1000: t=9780000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 hours, 29 minutes, 20 seconds
  Estimated time remaining to next output: 7 minutes, 6 seconds
Output 980/1000: t=9790000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 hours, 22 minutes, 11 seconds
  Estimated time remaining to next output: 7 minutes, 6 seconds
Output 981/1000: t=9800000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 hours, 15 minutes, 2 seconds
  Estimated time remaining to next output: 7 minutes, 6 seconds
Output 982/1000: t=9810000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 hours, 7 minutes, 54 seconds
  Estimated time remaining to next output: 7 minutes, 6 seconds
Output 983/1000: t=9820000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 2 hours, 45 seconds
  Estimated time remaining to next output: 7 minutes, 6 seconds
Output 984/1000: t=9830000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 hours, 53 minutes, 37 seconds
  Estimated time remaining to next output: 7 minutes, 6 seconds
Output 985/1000: t=9840000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 hours, 46 minutes, 29 seconds
  Estimated time remaining to next output: 7 minutes, 5 seconds
Output 986/1000: t=9850000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 hours, 39 minutes, 22 seconds
  Estimated time remaining to next output: 7 minutes, 5 seconds
Output 987/1000: t=9860000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 hours, 32 minutes, 15 seconds
  Estimated time remaining to next output: 7 minutes, 5 seconds
Output 988/1000: t=9870000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 hours, 25 minutes, 8 seconds
  Estimated time remaining to next output: 7 minutes, 5 seconds
Output 989/1000: t=9880000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 hours, 18 minutes
  Estimated time remaining to next output: 7 minutes, 5 seconds
Output 990/1000: t=9890000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 hours, 10 minutes, 54 seconds
  Estimated time remaining to next output: 7 minutes, 5 seconds
Output 991/1000: t=9900000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 1 hours, 3 minutes, 47 seconds
  Estimated time remaining to next output: 7 minutes, 5 seconds
Output 992/1000: t=9910000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 56 minutes, 41 seconds
  Estimated time remaining to next output: 7 minutes, 5 seconds
Output 993/1000: t=9920000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 49 minutes, 35 seconds
  Estimated time remaining to next output: 7 minutes, 5 seconds
Output 994/1000: t=9930000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 42 minutes, 30 seconds
  Estimated time remaining to next output: 7 minutes, 5 seconds
Output 995/1000: t=9940000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 35 minutes, 24 seconds
  Estimated time remaining to next output: 7 minutes, 4 seconds
Output 996/1000: t=9950000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 28 minutes, 19 seconds
  Estimated time remaining to next output: 7 minutes, 4 seconds
Output 997/1000: t=9960000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 21 minutes, 14 seconds
  Estimated time remaining to next output: 7 minutes, 4 seconds
Output 998/1000: t=9970000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 14 minutes, 9 seconds
  Estimated time remaining to next output: 7 minutes, 4 seconds
Output 999/1000: t=9980000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 7 minutes, 4 seconds
  Estimated time remaining to next output: 7 minutes, 4 seconds
Output 1000/1000: t=9990000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: 0 seconds
Output 1001/1000: t=10000000.0 yr, dE/E0=1.59e-05, N=801
  Estimated time remaining to complete simulation: -1 months, 4 weeks, 1 days, 23 hours, 52 minutes, 56 seconds

Simulation complete.
Total runtime: 4 days, 21 hours, 57 minutes, 44 seconds

Krivov & Booth (2018) self-stirring check (Eqs. 9-10):
  Final time:                 t = 1.000000e+07 yr
  RMS eccentricity (800 MPs):   2.212155e-02
  Belt geometry:              a = 100, da = 10, a/da = 10
  Masses:                     M_indiv = 3.754362e-09 Msun, M_disc = 3.003490e-06 Msun
  Implied stirring timescale: T = 8.351567e+13 yr
  Effective stirring factor:  C_e = 106.1886
  WARNING: C_e = 106.1886 >= 40 (Ida & Makino 1993 canonical value) -- this run stirs at or above the analytic self-stirring rate.
Saved archive: outputs/SS_800MP_10Myr_1Mearth_slopeq4.5/SS_800MP_10Myr_1Mearth_slopeq4.5.bin
Number of snapshots saved: 1001
Archive time range: 0.000e+00 yr to 1.000e+07 yr
Loaded snapshot table from archive.
role
massive_planetesimal    800
star                      1
Name: count, dtype: int64
Saved: outputs/SS_800MP_10Myr_1Mearth_slopeq4.5/figures/survival_fraction_vs_time.png
Saved: outputs/SS_800MP_10Myr_1Mearth_slopeq4.5/figures/mean_semimajor_axis_vs_time.png
Saved: outputs/SS_800MP_10Myr_1Mearth_slopeq4.5/figures/mean_eccentricity_vs_time.png
Saved: outputs/SS_800MP_10Myr_1Mearth_slopeq4.5/figures/rms_eccentricity_vs_time.png
Saved: outputs/SS_800MP_10Myr_1Mearth_slopeq4.5/figures/rms_inclination_vs_time.png
Saved: outputs/SS_800MP_10Myr_1Mearth_slopeq4.5/figures/a_vs_e_initial_final.png
Saved: outputs/SS_800MP_10Myr_1Mearth_slopeq4.5/figures/a_vs_i_initial_final.png
Inner plotted edge = 95.00 AU
Outer plotted edge = 104.99 AU
Saved: outputs/SS_800MP_10Myr_1Mearth_slopeq4.5/figures/xy_initial_final.png
All summary figures saved.
```
