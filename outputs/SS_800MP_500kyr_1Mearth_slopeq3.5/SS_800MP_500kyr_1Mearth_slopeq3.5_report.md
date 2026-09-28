# SS_800MP_500kyr_1Mearth_slopeq3.5 — Simulation Report

Config file: `config/SS_800MP_500kyr_1Mearth_slopeq3.5.yaml`
Archive file: `outputs/SS_800MP_500kyr_1Mearth_slopeq3.5/SS_800MP_500kyr_1Mearth_slopeq3.5.bin`

## Provenance

- Run UUID: `08503ec3-93a1-42cd-893f-39e17878f074`
- Created: 2026-09-25T15:16:44+00:00
- Finished: 2026-09-27T14:05:14+00:00
- Wall runtime: 168505.7 s
- Outcome: completed
- Command: `src/simulation/run_simulation.py config/SS_800MP_500kyr_1Mearth_slopeq3.5.yaml`
- Git: not available (run from a non-repo checkout)
- Software: python 3.12.14, rebound 5.0.0, numpy 2.4.6, pandas 3.0.3, matplotlib 3.10.9, pyyaml 6.0.3
- Frozen config: `config.yaml` (this directory)
- Full environment: `environment.txt` (this directory)

## Simulation
- Name: SS_800MP_500kyr_1Mearth_slopeq3.5
- Output directory: outputs
- Dump/checkpoint enabled: True

## Units
- time = yr, length = AU, mass = Msun

## Integration
- Integrator: mercurius
- maxtime: 500000
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
- Mass-assignment method (config): loaded from CSV (mode=csv): variable=radius, path=src/mass_models/cascade_selection_1000km_drop100_800keep_1Mearth/slope_q3.5/selected.csv, slope=3.5 (radii/masses read verbatim from file; disk mass computed from file, not split by a power law)
- **Mass is NOT uniform** across the 800 massive planetesimals:
  - min / median / max: 7.435746e-10 / 1.857488e-09 / 2.585122e-08 Msun
  - min / median / max: 2.475702e-04 / 6.184434e-04 / 8.607061e-03 Earth masses
  - total disk mass: 1.000000e+00 Earth masses

## Test Particles
- N: 0
- Distribution: uniform

## Run Summary (from archive)
- Initial particle count: 801
- Final particle count: 801
- Particles lost (escaped / unbound / other removal): 0
- Archive time range: 0.000000e+00 to 5.000000e+05
- Number of snapshots: 51

## Terminal Output

```
Saving SimulationArchive to: outputs/SS_800MP_500kyr_1Mearth_slopeq3.5/SS_800MP_500kyr_1Mearth_slopeq3.5.bin
No existing dump_data.json found; starting fresh run.

No giant planet: integrating the disk around the star alone.
  Timestep: 9.259630e+01 (0.1 x circular period at a=95 (disk inner edge) = 9.259630e+02)

Massive planetesimal mass setup:
  Mode: distribution/csv  (planetesimal radii loaded from CSV; disk mass computed from file)
  Number of planetesimals: 800
  Mass spectrum: loaded from CSV (/hadoop_data/home/elaine.nieves/debris-disk-pipeline/src/mass_models/cascade_selection_1000km_drop100_800keep_1Mearth/slope_q3.5/selected.csv), slope=3.5, realized radius range [31.794, 77.230] km
  Per-MP mass (Earth masses): min=2.475702e-04 / median=6.184434e-04 / max=8.607061e-03
  Per-MP diameter (km, uniform sphere, rho = 1 g/cm**3): min=63.588 / median=79.944 / max=154.461
  Total disk mass: 1.000000e+00 Earth masses (3.003490e-06 Msun)
Saved: outputs/SS_800MP_500kyr_1Mearth_slopeq3.5/distribution.csv
Saved: outputs/SS_800MP_500kyr_1Mearth_slopeq3.5/figures/dohnanyi_per_particle.png
Saved: outputs/SS_800MP_500kyr_1Mearth_slopeq3.5/figures/dohnanyi_differential_histogram.png
Saved: outputs/SS_800MP_500kyr_1Mearth_slopeq3.5/figures/count_vs_mass_histogram.png
Saved: outputs/SS_800MP_500kyr_1Mearth_slopeq3.5/figures/count_vs_radius_histogram.png

Stirrer-coverage check (Krivov & Booth 2018: N x delta_af >= delta_a):
  Stirrers inside the belt [95, 105]: N = 800
  delta_af = 8 sqrt(3) h_M a_M:  mean = 1.334670e+00, sum over stirrers = 1.067736e+03
  Belt width delta_a = 1.000000e+01
  Coverage ratio (sum delta_af / delta_a) = 106.774
  OK: stirrer feeding zones span the belt.

Beginning the main integration
Output 1/50: t=0.0 yr, dE/E0=0.00e+00, N=801
  Estimated time remaining to complete simulation: 4 seconds
  Estimated time remaining to next output: 0 seconds
Output 2/50: t=10000.0 yr, dE/E0=1.34e-04, N=801
  Estimated time remaining to complete simulation: 4 days, 14 hours, 45 minutes, 40 seconds
  Estimated time remaining to next output: 2 hours, 18 minutes, 27 seconds
Output 3/50: t=20000.0 yr, dE/E0=1.34e-04, N=801
  Estimated time remaining to complete simulation: 4 days, 22 hours, 39 minutes
  Estimated time remaining to next output: 2 hours, 31 minutes, 28 seconds
Output 4/50: t=30000.0 yr, dE/E0=1.34e-04, N=801
  Estimated time remaining to complete simulation: 4 days, 5 hours, 50 minutes, 2 seconds
  Estimated time remaining to next output: 2 hours, 12 minutes, 49 seconds
Output 5/50: t=40000.0 yr, dE/E0=1.34e-04, N=801
  Estimated time remaining to complete simulation: 4 days, 1 hours, 18 minutes, 51 seconds
  Estimated time remaining to next output: 2 hours, 9 minutes, 45 seconds
Output 6/50: t=50000.0 yr, dE/E0=1.34e-04, N=801
  Estimated time remaining to complete simulation: 3 days, 23 hours, 31 minutes, 13 seconds
  Estimated time remaining to next output: 2 hours, 10 minutes, 15 seconds
Output 7/50: t=60000.0 yr, dE/E0=1.34e-04, N=801
  Estimated time remaining to complete simulation: 3 days, 21 hours, 34 minutes, 13 seconds
  Estimated time remaining to next output: 2 hours, 10 minutes, 33 seconds
Output 8/50: t=70000.0 yr, dE/E0=1.34e-04, N=801
  Estimated time remaining to complete simulation: 3 days, 19 hours, 48 minutes, 42 seconds
  Estimated time remaining to next output: 2 hours, 11 minutes, 9 seconds
Output 9/50: t=80000.0 yr, dE/E0=1.34e-04, N=801
  Estimated time remaining to complete simulation: 3 days, 18 hours, 5 minutes, 21 seconds
  Estimated time remaining to next output: 2 hours, 11 minutes, 50 seconds
Output 10/50: t=90000.0 yr, dE/E0=1.34e-04, N=801
  Estimated time remaining to complete simulation: 3 days, 16 hours, 56 minutes, 29 seconds
  Estimated time remaining to next output: 2 hours, 13 minutes, 24 seconds
Output 11/50: t=100000.0 yr, dE/E0=1.34e-04, N=801
  Estimated time remaining to complete simulation: 3 days, 15 hours, 6 minutes, 38 seconds
  Estimated time remaining to next output: 2 hours, 14 minutes
Output 12/50: t=110000.0 yr, dE/E0=1.34e-04, N=801
  Estimated time remaining to complete simulation: 3 days, 11 hours, 57 minutes, 13 seconds
  Estimated time remaining to next output: 2 hours, 12 minutes, 33 seconds
Output 13/50: t=120000.0 yr, dE/E0=1.34e-04, N=801
  Estimated time remaining to complete simulation: 3 days, 11 hours, 58 minutes, 25 seconds
  Estimated time remaining to next output: 2 hours, 16 minutes, 10 seconds
Output 14/50: t=130000.0 yr, dE/E0=1.34e-04, N=801
  Estimated time remaining to complete simulation: 3 days, 9 hours, 48 minutes, 24 seconds
  Estimated time remaining to next output: 2 hours, 16 minutes, 20 seconds
Output 15/50: t=140000.0 yr, dE/E0=1.34e-04, N=801
  Estimated time remaining to complete simulation: 3 days, 7 hours, 35 minutes, 8 seconds
  Estimated time remaining to next output: 2 hours, 16 minutes, 25 seconds
Output 16/50: t=150000.0 yr, dE/E0=1.34e-04, N=801
  Estimated time remaining to complete simulation: 3 days, 4 hours, 8 minutes, 51 seconds
  Estimated time remaining to next output: 2 hours, 14 minutes, 22 seconds
Output 17/50: t=160000.0 yr, dE/E0=1.34e-04, N=801
  Estimated time remaining to complete simulation: 2 days, 23 hours, 54 minutes, 25 seconds
  Estimated time remaining to next output: 2 hours, 10 minutes, 44 seconds
Output 18/50: t=170000.0 yr, dE/E0=1.34e-04, N=801
  Estimated time remaining to complete simulation: 2 days, 20 hours, 2 minutes, 43 seconds
  Estimated time remaining to next output: 2 hours, 7 minutes, 35 seconds
Output 19/50: t=180000.0 yr, dE/E0=1.34e-04, N=801
  Estimated time remaining to complete simulation: 2 days, 17 hours, 15 minutes, 51 seconds
  Estimated time remaining to next output: 2 hours, 6 minutes, 19 seconds
Output 20/50: t=190000.0 yr, dE/E0=1.34e-04, N=801
  Estimated time remaining to complete simulation: 2 days, 14 hours, 50 minutes, 2 seconds
  Estimated time remaining to next output: 2 hours, 5 minutes, 40 seconds
Output 21/50: t=200000.0 yr, dE/E0=1.34e-04, N=801
  Estimated time remaining to complete simulation: 2 days, 11 hours, 43 minutes, 41 seconds
  Estimated time remaining to next output: 2 hours, 3 minutes, 34 seconds
Output 22/50: t=210000.0 yr, dE/E0=1.34e-04, N=801
  Estimated time remaining to complete simulation: 2 days, 7 hours, 12 minutes, 2 seconds
  Estimated time remaining to next output: 1 hours, 58 minutes, 17 seconds
Output 23/50: t=220000.0 yr, dE/E0=1.34e-04, N=801
  Estimated time remaining to complete simulation: 2 days, 3 hours, 3 minutes, 59 seconds
  Estimated time remaining to next output: 1 hours, 53 minutes, 28 seconds
Output 24/50: t=230000.0 yr, dE/E0=1.34e-04, N=801
  Estimated time remaining to complete simulation: 1 days, 23 hours, 16 minutes, 29 seconds
  Estimated time remaining to next output: 1 hours, 49 minutes, 5 seconds
Output 25/50: t=240000.0 yr, dE/E0=1.34e-04, N=801
  Estimated time remaining to complete simulation: 1 days, 19 hours, 45 minutes, 49 seconds
  Estimated time remaining to next output: 1 hours, 45 minutes, 1 seconds
Output 26/50: t=250000.0 yr, dE/E0=1.34e-04, N=801
  Estimated time remaining to complete simulation: 1 days, 16 hours, 31 minutes, 4 seconds
  Estimated time remaining to next output: 1 hours, 41 minutes, 17 seconds
Output 27/50: t=260000.0 yr, dE/E0=1.34e-04, N=801
  Estimated time remaining to complete simulation: 1 days, 13 hours, 29 minutes, 18 seconds
  Estimated time remaining to next output: 1 hours, 37 minutes, 47 seconds
Output 28/50: t=270000.0 yr, dE/E0=1.34e-04, N=801
  Estimated time remaining to complete simulation: 1 days, 10 hours, 39 minutes, 58 seconds
  Estimated time remaining to next output: 1 hours, 34 minutes, 32 seconds
Output 29/50: t=280000.0 yr, dE/E0=1.34e-04, N=801
  Estimated time remaining to complete simulation: 1 days, 8 hours, 1 minutes, 46 seconds
  Estimated time remaining to next output: 1 hours, 31 minutes, 30 seconds
Output 30/50: t=290000.0 yr, dE/E0=1.34e-04, N=801
  Estimated time remaining to complete simulation: 1 days, 5 hours, 33 minutes, 50 seconds
  Estimated time remaining to next output: 1 hours, 28 minutes, 41 seconds
Output 31/50: t=300000.0 yr, dE/E0=1.34e-04, N=801
  Estimated time remaining to complete simulation: 1 days, 3 hours, 14 minutes, 51 seconds
  Estimated time remaining to next output: 1 hours, 26 minutes, 2 seconds
Output 32/50: t=310000.0 yr, dE/E0=1.34e-04, N=801
  Estimated time remaining to complete simulation: 1 days, 1 hours, 4 minutes, 11 seconds
  Estimated time remaining to next output: 1 hours, 23 minutes, 33 seconds
Output 33/50: t=320000.0 yr, dE/E0=1.34e-04, N=801
  Estimated time remaining to complete simulation: 23 hours, 1 minutes, 1 seconds
  Estimated time remaining to next output: 1 hours, 21 minutes, 14 seconds
Output 34/50: t=330000.0 yr, dE/E0=1.34e-04, N=801
  Estimated time remaining to complete simulation: 21 hours, 4 minutes, 36 seconds
  Estimated time remaining to next output: 1 hours, 19 minutes, 2 seconds
Output 35/50: t=340000.0 yr, dE/E0=1.34e-04, N=801
  Estimated time remaining to complete simulation: 19 hours, 14 minutes, 38 seconds
  Estimated time remaining to next output: 1 hours, 16 minutes, 58 seconds
Output 36/50: t=350000.0 yr, dE/E0=1.34e-04, N=801
  Estimated time remaining to complete simulation: 17 hours, 30 minutes, 17 seconds
  Estimated time remaining to next output: 1 hours, 15 minutes, 1 seconds
Output 37/50: t=360000.0 yr, dE/E0=1.34e-04, N=801
  Estimated time remaining to complete simulation: 15 hours, 51 minutes, 9 seconds
  Estimated time remaining to next output: 1 hours, 13 minutes, 9 seconds
Output 38/50: t=370000.0 yr, dE/E0=1.34e-04, N=801
  Estimated time remaining to complete simulation: 14 hours, 16 minutes, 48 seconds
  Estimated time remaining to next output: 1 hours, 11 minutes, 24 seconds
Output 39/50: t=380000.0 yr, dE/E0=1.34e-04, N=801
  Estimated time remaining to complete simulation: 12 hours, 46 minutes, 46 seconds
  Estimated time remaining to next output: 1 hours, 9 minutes, 42 seconds
Output 40/50: t=390000.0 yr, dE/E0=1.34e-04, N=801
  Estimated time remaining to complete simulation: 11 hours, 21 minutes, 10 seconds
  Estimated time remaining to next output: 1 hours, 8 minutes, 7 seconds
Output 41/50: t=400000.0 yr, dE/E0=1.34e-04, N=801
  Estimated time remaining to complete simulation: 9 hours, 59 minutes, 27 seconds
  Estimated time remaining to next output: 1 hours, 6 minutes, 36 seconds
Output 42/50: t=410000.0 yr, dE/E0=1.34e-04, N=801
  Estimated time remaining to complete simulation: 8 hours, 41 minutes, 12 seconds
  Estimated time remaining to next output: 1 hours, 5 minutes, 9 seconds
Output 43/50: t=420000.0 yr, dE/E0=1.34e-04, N=801
  Estimated time remaining to complete simulation: 7 hours, 26 minutes, 20 seconds
  Estimated time remaining to next output: 1 hours, 3 minutes, 45 seconds
Output 44/50: t=430000.0 yr, dE/E0=1.34e-04, N=801
  Estimated time remaining to complete simulation: 6 hours, 14 minutes, 41 seconds
  Estimated time remaining to next output: 1 hours, 2 minutes, 26 seconds
Output 45/50: t=440000.0 yr, dE/E0=1.34e-04, N=801
  Estimated time remaining to complete simulation: 5 hours, 5 minutes, 56 seconds
  Estimated time remaining to next output: 1 hours, 1 minutes, 11 seconds
Output 46/50: t=450000.0 yr, dE/E0=1.34e-04, N=801
  Estimated time remaining to complete simulation: 4 hours
  Estimated time remaining to next output: 1 hours
Output 47/50: t=460000.0 yr, dE/E0=1.34e-04, N=801
  Estimated time remaining to complete simulation: 2 hours, 56 minutes, 32 seconds
  Estimated time remaining to next output: 58 minutes, 50 seconds
Output 48/50: t=470000.0 yr, dE/E0=1.34e-04, N=801
  Estimated time remaining to complete simulation: 1 hours, 55 minutes, 40 seconds
  Estimated time remaining to next output: 57 minutes, 50 seconds
Output 49/50: t=480000.0 yr, dE/E0=1.34e-04, N=801
  Estimated time remaining to complete simulation: 56 minutes, 51 seconds
  Estimated time remaining to next output: 56 minutes, 51 seconds
Output 50/50: t=490000.0 yr, dE/E0=1.34e-04, N=801
  Estimated time remaining to complete simulation: 0 seconds
Output 51/50: t=500000.0 yr, dE/E0=1.34e-04, N=801
  Estimated time remaining to complete simulation: -1 months, 4 weeks, 1 days, 23 hours, 4 minutes, 56 seconds

Simulation complete.
Total runtime: 1 days, 22 hours, 48 minutes, 25 seconds

Krivov & Booth (2018) self-stirring check (Eqs. 9-10):
  Final time:                 t = 5.000000e+05 yr
  RMS eccentricity (800 MPs):   1.870710e-02
  Belt geometry:              a = 100, da = 10, a/da = 10
  Masses:                     M_indiv = 3.754362e-09 Msun, M_disc = 3.003490e-06 Msun
  Implied stirring timescale: T = 8.165332e+12 yr
  Effective stirring factor:  C_e = 1086.1056
  WARNING: C_e = 1086.1056 >= 40 (Ida & Makino 1993 canonical value) -- this run stirs at or above the analytic self-stirring rate.
Saved archive: outputs/SS_800MP_500kyr_1Mearth_slopeq3.5/SS_800MP_500kyr_1Mearth_slopeq3.5.bin
Number of snapshots saved: 51
Archive time range: 0.000e+00 yr to 5.000e+05 yr
Loaded snapshot table from archive.
role
massive_planetesimal    800
star                      1
Name: count, dtype: int64
Saved: outputs/SS_800MP_500kyr_1Mearth_slopeq3.5/figures/survival_fraction_vs_time.png
Saved: outputs/SS_800MP_500kyr_1Mearth_slopeq3.5/figures/mean_semimajor_axis_vs_time.png
Saved: outputs/SS_800MP_500kyr_1Mearth_slopeq3.5/figures/mean_eccentricity_vs_time.png
Saved: outputs/SS_800MP_500kyr_1Mearth_slopeq3.5/figures/rms_eccentricity_vs_time.png
Saved: outputs/SS_800MP_500kyr_1Mearth_slopeq3.5/figures/rms_inclination_vs_time.png
Saved: outputs/SS_800MP_500kyr_1Mearth_slopeq3.5/figures/a_vs_e_initial_final.png
Saved: outputs/SS_800MP_500kyr_1Mearth_slopeq3.5/figures/a_vs_i_initial_final.png
Inner plotted edge = 95.00 AU
Outer plotted edge = 104.99 AU
Saved: outputs/SS_800MP_500kyr_1Mearth_slopeq3.5/figures/xy_initial_final.png
All summary figures saved.
```
