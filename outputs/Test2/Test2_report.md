# Test2 — Simulation Report

Config file: `config/Test.yaml`
Archive file: `outputs/Test2/Test2.bin`

## Simulation
- Name: Test2
- Output directory: outputs
- Dump/checkpoint enabled: True

## Units
- time = yr, length = AU, mass = Msun

## Integration
- Integrator: mercurius
- maxtime: 200.0
- time_step: 5
- timestep_fraction_of_planet_period: 0.1
- exit_max_distance: 100.0 au

## Star
- Mass: 1.28 Msun

## Giant Planet
- Mass: 1.26 Mjup
- a: 2.56 au, e: 0.07, inc: 0.01 deg
- omega: 100.0 deg, Omega random: True
- t_peri_jd: 2450870.0, orbital_period_days: 1311.0, epoch_jd: 2451545.0

## Disk
- a: [30.0, 50.0] au
- e: [0.0, 3.5e-06]
- inc: [0.0, 3.5e-06] deg

## Massive Planetesimals
- N: 4
- Mass-assignment method (config): mass_fraction_of_giant_planet = 5.000000e-04
- Individual mass (uniform across all 4): 6.015177e-07 Msun (0.200273 Earth masses)

## Test Particles
- N: 10
- Distribution: uniform

## Run Summary (from archive)
- Initial particle count: 16
- Final particle count: 16
- Particles lost (escaped / unbound / other removal): 0
- Archive time range: 1.950000e+02 to 2.000000e+02
- Number of snapshots: 2

## Terminal Output

```
Saving SimulationArchive to: outputs/Test2/Test2.bin
Resuming from t=1.950000e+02 yr: times=array([195., 200.])
Found dump file. Restoring simulation from snapshot...
Restored simulation from snapshot number at t=1.950000e+02 yr with N=16 particles.

Beginning the main integration
Output 1/1: t=195.0 yr, dE/E0=0.00e+00, N=16
  Estimated time remaining to complete simulation: 0 seconds
Output 2/1: t=200.0 yr, dE/E0=2.13e-06, N=16
  Estimated time remaining to complete simulation: 0 seconds

Simulation complete.
Total runtime: 0 seconds
Saved archive: outputs/Test2/Test2.bin
Number of snapshots saved: 2
Archive time range: 1.950e+02 yr to 2.000e+02 yr
Loaded snapshot table from archive.
role
test_particle           10
massive_planetesimal     4
star                     1
giant_planet             1
Name: count, dtype: int64
Saved: outputs/Test2/figures/survival_fraction_vs_time.png
Saved: outputs/Test2/figures/mean_semimajor_axis_vs_time.png
Saved: outputs/Test2/figures/mean_eccentricity_vs_time.png
Saved: outputs/Test2/figures/rms_eccentricity_vs_time.png
Saved: outputs/Test2/figures/rms_inclination_vs_time.png
Saved: outputs/Test2/figures/a_vs_e_initial_final.png
Saved: outputs/Test2/figures/a_vs_i_initial_final.png
Inner plotted edge = 32.90 AU
Outer plotted edge = 48.83 AU
Saved: outputs/Test2/figures/xy_initial_final.png
All summary figures saved.
```
