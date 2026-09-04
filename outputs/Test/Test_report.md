# Test2 — Simulation Report

Config file: `config/Test.yaml`
Archive file: `outputs/Test/Test.bin`

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
- Number of snapshots: 4
