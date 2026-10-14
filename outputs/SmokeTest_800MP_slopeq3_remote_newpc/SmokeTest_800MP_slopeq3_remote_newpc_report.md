# SmokeTest_800MP_slopeq3_remote_newpc — Simulation Report

Config file: `config/SmokeTest_800MP_slopeq3_remote_newpc.yaml`
Archive file: `outputs/SmokeTest_800MP_slopeq3_remote_newpc/SmokeTest_800MP_slopeq3_remote_newpc.bin`

## Provenance

- Run UUID: `d3432ac3-bb66-4d28-8dd3-9f970df61184`
- Created: 2026-09-28T16:40:11+00:00
- Finished: 2026-09-28T16:51:54+00:00
- Wall runtime: 698.3 s
- Outcome: completed
- Command: `src/simulation/run_simulation.py config/SmokeTest_800MP_slopeq3_remote_newpc.yaml`
- Git: not available (run from a non-repo checkout)
- Software: python 3.12.14, rebound 5.0.0, numpy 2.4.6, pandas 3.0.3, matplotlib 3.10.9, pyyaml 6.0.3
- Frozen config: `config.yaml` (this directory)
- Full environment: `environment.txt` (this directory)

## Simulation
- Name: SmokeTest_800MP_slopeq3_remote_newpc
- Output directory: outputs
- Dump/checkpoint enabled: True

## Units
- time = yr, length = AU, mass = Msun

## Integration
- Integrator: mercurius
- maxtime: 20000
- time_step: 2000
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
- Mass-assignment method (config): loaded from CSV (mode=csv): variable=radius, path=src/mass_models/cascade_selection_200km_800keep/slope_q3/selected.csv, slope=3.0 (radii/masses read verbatim from file; disk mass computed from file, not split by a power law)
- **Mass is NOT uniform** across the 800 massive planetesimals:
  - min / median / max: 6.584335e-13 / 1.268765e-12 / 5.670767e-12 Msun
  - min / median / max: 2.192228e-07 / 4.224303e-07 / 1.888060e-06 Earth masses
  - total disk mass: 4.799052e-04 Earth masses

## Test Particles
- N: 0
- Distribution: uniform

## Run Summary (from archive)
- Initial particle count: 801
- Final particle count: 801
- Particles lost (escaped / unbound / other removal): 0
- Archive time range: 0.000000e+00 to 2.000000e+04
- Number of snapshots: 11

## Terminal Output

```
Saving SimulationArchive to: outputs/SmokeTest_800MP_slopeq3_remote_newpc/SmokeTest_800MP_slopeq3_remote_newpc.bin
No existing dump_data.json found; starting fresh run.

No giant planet: integrating the disk around the star alone.
  Timestep: 9.259630e+01 (0.1 x circular period at a=95 (disk inner edge) = 9.259630e+02)

Massive planetesimal mass setup:
  Mode: distribution/csv  (planetesimal radii loaded from CSV; disk mass computed from file)
  Number of planetesimals: 800
  Mass spectrum: loaded from CSV (/hadoop_data/home/elaine.nieves/debris-disk-pipeline/src/mass_models/cascade_selection_200km_800keep/slope_q3/selected.csv), slope=3, realized radius range [67.870, 139.120] km
  Per-MP mass (Earth masses): min=2.192228e-07 / median=4.224303e-07 / max=1.888060e-06
  Per-MP diameter (km, uniform sphere, rho = 1 g/cm**3): min=135.741 / median=168.914 / max=278.240
  Total disk mass: 4.799052e-04 Earth masses (1.441390e-09 Msun)
Saved: outputs/SmokeTest_800MP_slopeq3_remote_newpc/distribution.csv
Saved: outputs/SmokeTest_800MP_slopeq3_remote_newpc/figures/dohnanyi_per_particle.png
Saved: outputs/SmokeTest_800MP_slopeq3_remote_newpc/figures/dohnanyi_differential_histogram.png
Saved: outputs/SmokeTest_800MP_slopeq3_remote_newpc/figures/count_vs_mass_histogram.png
Saved: outputs/SmokeTest_800MP_slopeq3_remote_newpc/figures/count_vs_radius_histogram.png

Stirrer-coverage check (Krivov & Booth 2018: N x delta_af >= delta_a):
  Stirrers inside the belt [95, 105]: N = 800
  delta_af = 8 sqrt(3) h_M a_M:  mean = 1.116331e-01, sum over stirrers = 8.930645e+01
  Belt width delta_a = 1.000000e+01
  Coverage ratio (sum delta_af / delta_a) = 8.931
  OK: stirrer feeding zones span the belt.

Beginning the main integration
Output 1/10: t=0.0 yr, dE/E0=0.00e+00, N=801
  Estimated time remaining to complete simulation: 0 seconds
  Estimated time remaining to next output: 0 seconds
Output 2/10: t=2000.0 yr, dE/E0=1.06e-13, N=801
  Estimated time remaining to complete simulation: 6 minutes, 4 seconds
  Estimated time remaining to next output: 45 seconds
Output 3/10: t=4000.0 yr, dE/E0=1.24e-13, N=801
  Estimated time remaining to complete simulation: 7 minutes, 5 seconds
  Estimated time remaining to next output: 1 minutes
Output 4/10: t=6000.0 yr, dE/E0=1.25e-13, N=801
  Estimated time remaining to complete simulation: 6 minutes, 26 seconds
  Estimated time remaining to next output: 1 minutes, 4 seconds
Output 5/10: t=8000.0 yr, dE/E0=1.48e-13, N=801
  Estimated time remaining to complete simulation: 5 minutes, 32 seconds
  Estimated time remaining to next output: 1 minutes, 6 seconds
Output 6/10: t=10000.0 yr, dE/E0=5.10e-14, N=801
  Estimated time remaining to complete simulation: 4 minutes, 31 seconds
  Estimated time remaining to next output: 1 minutes, 7 seconds
Output 7/10: t=12000.0 yr, dE/E0=1.13e-14, N=801
  Estimated time remaining to complete simulation: 3 minutes, 27 seconds
  Estimated time remaining to next output: 1 minutes, 9 seconds
Output 8/10: t=14000.0 yr, dE/E0=1.31e-14, N=801
  Estimated time remaining to complete simulation: 2 minutes, 19 seconds
  Estimated time remaining to next output: 1 minutes, 9 seconds
Output 9/10: t=16000.0 yr, dE/E0=7.15e-14, N=801
  Estimated time remaining to complete simulation: 1 minutes, 8 seconds
  Estimated time remaining to next output: 1 minutes, 8 seconds
Output 10/10: t=18000.0 yr, dE/E0=1.22e-13, N=801
  Estimated time remaining to complete simulation: 0 seconds
Output 11/10: t=20000.0 yr, dE/E0=7.48e-14, N=801
  Estimated time remaining to complete simulation: -1 months, 4 weeks, 1 days, 23 hours, 58 minutes, 57 seconds

Simulation complete.
Total runtime: 11 minutes, 38 seconds

Krivov & Booth (2018) self-stirring check (Eqs. 9-10):
  Final time:                 t = 2.000000e+04 yr
  RMS eccentricity (800 MPs):   2.367946e-05
  Belt geometry:              a = 100, da = 10, a/da = 10
  Masses:                     M_indiv = 1.801738e-12 Msun, M_disc = 1.441390e-09 Msun
  Implied stirring timescale: T = 1.272252e+23 yr
  Effective stirring factor:  C_e = 0.3027
Saved archive: outputs/SmokeTest_800MP_slopeq3_remote_newpc/SmokeTest_800MP_slopeq3_remote_newpc.bin
Number of snapshots saved: 11
Archive time range: 0.000e+00 yr to 2.000e+04 yr
Loaded snapshot table from archive.
role
massive_planetesimal    800
star                      1
Name: count, dtype: int64
Saved: outputs/SmokeTest_800MP_slopeq3_remote_newpc/figures/survival_fraction_vs_time.png
Saved: outputs/SmokeTest_800MP_slopeq3_remote_newpc/figures/mean_semimajor_axis_vs_time.png
Saved: outputs/SmokeTest_800MP_slopeq3_remote_newpc/figures/mean_eccentricity_vs_time.png
Saved: outputs/SmokeTest_800MP_slopeq3_remote_newpc/figures/rms_eccentricity_vs_time.png
Saved: outputs/SmokeTest_800MP_slopeq3_remote_newpc/figures/rms_inclination_vs_time.png
Saved: outputs/SmokeTest_800MP_slopeq3_remote_newpc/figures/a_vs_e_initial_final.png
Saved: outputs/SmokeTest_800MP_slopeq3_remote_newpc/figures/a_vs_i_initial_final.png
Inner plotted edge = 95.00 AU
Outer plotted edge = 104.99 AU
Saved: outputs/SmokeTest_800MP_slopeq3_remote_newpc/figures/xy_initial_final.png
All summary figures saved.
```
