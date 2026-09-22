# SmokeTest_800MP_slopeq3 — Simulation Report

Config file: `/Users/elainenieves/debris-disk-pipeline/config/SmokeTest_800MP_slopeq3.yaml`
Archive file: `outputs/SmokeTest_800MP_slopeq3/SmokeTest_800MP_slopeq3.bin`

## Provenance

- Run UUID: `7e394075-ee8f-4f98-ab78-5e1391acc74a`
- Created: 2026-09-21T15:59:41-03:00
- Finished: 2026-09-21T16:04:19-03:00
- Wall runtime: 274.4 s
- Outcome: completed
- Command: `/Users/elainenieves/debris-disk-pipeline/src/simulation/run_simulation.py /Users/elainenieves/debris-disk-pipeline/config/SmokeTest_800MP_slopeq3.yaml`
- Git commit: `fbf3a28891c78796dcee8dd82829bfac5990cfda` (branch `main`) **(DIRTY — uncommitted tracked changes)**
    - modified: `README.md`
    - modified: `src/simulation/run_simulation.py`
    - modified: `tests/test_dohnanyi_mode.py`
- Software: python 3.12.11, rebound 5.0.0, numpy 2.4.6, pandas 3.0.3, matplotlib 3.10.9, pyyaml 6.0.3
- Frozen config: `config.yaml` (this directory)
- Full environment: `environment.txt` (this directory)

## Simulation
- Name: SmokeTest_800MP_slopeq3
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
- Mass-assignment method (config): power_law distribution (mode=csv): variable=radius, [None, None] km, slope=3.0, seed=None (total_disk_mass_earth = unset, split across N by the power law)
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
Saving SimulationArchive to: outputs/SmokeTest_800MP_slopeq3/SmokeTest_800MP_slopeq3.bin
No existing dump_data.json found; starting fresh run.

No giant planet: integrating the disk around the star alone.
  Timestep: 9.259630e+01 (0.1 x circular period at a=95 (disk inner edge) = 9.259630e+02)

Massive planetesimal mass setup:
  Mode: distribution/csv  (planetesimal radii loaded from CSV; disk mass computed from file)
  Number of planetesimals: 800
  Mass spectrum: loaded from CSV (/Users/elainenieves/debris-disk-pipeline/src/mass_models/cascade_selection_200km_800keep/slope_q3/selected.csv), slope=3, realized radius range [67.870, 139.120] km
  Per-MP mass (Earth masses): min=2.192228e-07 / median=4.224303e-07 / max=1.888060e-06
  Per-MP diameter (km, uniform sphere, rho = 1 g/cm**3): min=135.741 / median=168.914 / max=278.240
  Total disk mass: 4.799052e-04 Earth masses (1.441390e-09 Msun)
Saved: outputs/SmokeTest_800MP_slopeq3/distribution.csv
Saved: outputs/SmokeTest_800MP_slopeq3/figures/dohnanyi_per_particle.png
Saved: outputs/SmokeTest_800MP_slopeq3/figures/dohnanyi_differential_histogram.png
Saved: outputs/SmokeTest_800MP_slopeq3/figures/count_vs_mass_histogram.png
Saved: outputs/SmokeTest_800MP_slopeq3/figures/count_vs_radius_histogram.png

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
  Estimated time remaining to complete simulation: 2 minutes
  Estimated time remaining to next output: 15 seconds
Output 3/10: t=4000.0 yr, dE/E0=1.24e-13, N=801
  Estimated time remaining to complete simulation: 2 minutes, 19 seconds
  Estimated time remaining to next output: 19 seconds
Output 4/10: t=6000.0 yr, dE/E0=1.25e-13, N=801
  Estimated time remaining to complete simulation: 2 minutes, 7 seconds
  Estimated time remaining to next output: 21 seconds
Output 5/10: t=8000.0 yr, dE/E0=1.49e-13, N=801
  Estimated time remaining to complete simulation: 1 minutes, 51 seconds
  Estimated time remaining to next output: 22 seconds
Output 6/10: t=10000.0 yr, dE/E0=5.15e-14, N=801
  Estimated time remaining to complete simulation: 1 minutes, 32 seconds
  Estimated time remaining to next output: 23 seconds
Output 7/10: t=12000.0 yr, dE/E0=1.13e-14, N=801
  Estimated time remaining to complete simulation: 1 minutes, 11 seconds
  Estimated time remaining to next output: 23 seconds
Output 8/10: t=14000.0 yr, dE/E0=1.18e-14, N=801
  Estimated time remaining to complete simulation: 48 seconds
  Estimated time remaining to next output: 24 seconds
Output 9/10: t=16000.0 yr, dE/E0=7.11e-14, N=801
  Estimated time remaining to complete simulation: 24 seconds
  Estimated time remaining to next output: 24 seconds
Output 10/10: t=18000.0 yr, dE/E0=1.25e-13, N=801
  Estimated time remaining to complete simulation: 0 seconds
Output 11/10: t=20000.0 yr, dE/E0=7.53e-14, N=801
  Estimated time remaining to complete simulation: -1 months, 4 weeks, 1 days, 23 hours, 59 minutes, 36 seconds

Simulation complete.
Total runtime: 4 minutes, 34 seconds

Krivov & Booth (2018) self-stirring check (Eqs. 9-10):
  Final time:                 t = 2.000000e+04 yr
  RMS eccentricity (800 MPs):   2.367946e-05
  Belt geometry:              a = 100, da = 10, a/da = 10
  Masses:                     M_indiv = 1.801738e-12 Msun, M_disc = 1.441390e-09 Msun
  Implied stirring timescale: T = 1.272252e+23 yr
  Effective stirring factor:  C_e = 0.3027
Saved archive: outputs/SmokeTest_800MP_slopeq3/SmokeTest_800MP_slopeq3.bin
Number of snapshots saved: 11
Archive time range: 0.000e+00 yr to 2.000e+04 yr
Loaded snapshot table from archive.
role
massive_planetesimal    800
star                      1
Name: count, dtype: int64
Saved: outputs/SmokeTest_800MP_slopeq3/figures/survival_fraction_vs_time.png
Saved: outputs/SmokeTest_800MP_slopeq3/figures/mean_semimajor_axis_vs_time.png
Saved: outputs/SmokeTest_800MP_slopeq3/figures/mean_eccentricity_vs_time.png
Saved: outputs/SmokeTest_800MP_slopeq3/figures/rms_eccentricity_vs_time.png
Saved: outputs/SmokeTest_800MP_slopeq3/figures/rms_inclination_vs_time.png
Saved: outputs/SmokeTest_800MP_slopeq3/figures/a_vs_e_initial_final.png
Saved: outputs/SmokeTest_800MP_slopeq3/figures/a_vs_i_initial_final.png
Inner plotted edge = 95.00 AU
Outer plotted edge = 104.99 AU
Saved: outputs/SmokeTest_800MP_slopeq3/figures/xy_initial_final.png
All summary figures saved.
```
