# SS_800MP_1000TP_500kyr_1Mearth_slopeq3.5 — Simulation Report

Config file: `config/SS_800MP_1000TP_500kyr_1Mearth_slopeq3.5.yaml`
Archive file: `outputs/SS_800MP_1000TP_500kyr_1Mearth_slopeq3.5/SS_800MP_1000TP_500kyr_1Mearth_slopeq3.5.bin`

## Provenance

- Run UUID: `29a9efa4-d7fe-470f-9d35-acecf8a99eae`
- Created: 2026-09-25T15:16:50+00:00
- Finished: 2026-09-28T08:28:49+00:00
- Wall runtime: 234716.6 s
- Outcome: completed
- Command: `src/simulation/run_simulation.py config/SS_800MP_1000TP_500kyr_1Mearth_slopeq3.5.yaml`
- Git: not available (run from a non-repo checkout)
- Software: python 3.12.14, rebound 5.0.0, numpy 2.4.6, pandas 3.0.3, matplotlib 3.10.9, pyyaml 6.0.3
- Frozen config: `config.yaml` (this directory)
- Full environment: `environment.txt` (this directory)

## Simulation
- Name: SS_800MP_1000TP_500kyr_1Mearth_slopeq3.5
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
- N: 1000
- Distribution: uniform

## Run Summary (from archive)
- Initial particle count: 1801
- Final particle count: 1801
- Particles lost (escaped / unbound / other removal): 0
- Archive time range: 0.000000e+00 to 5.000000e+05
- Number of snapshots: 51

## Terminal Output

```
Saving SimulationArchive to: outputs/SS_800MP_1000TP_500kyr_1Mearth_slopeq3.5/SS_800MP_1000TP_500kyr_1Mearth_slopeq3.5.bin
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
Saved: outputs/SS_800MP_1000TP_500kyr_1Mearth_slopeq3.5/distribution.csv
Saved: outputs/SS_800MP_1000TP_500kyr_1Mearth_slopeq3.5/figures/dohnanyi_per_particle.png
Saved: outputs/SS_800MP_1000TP_500kyr_1Mearth_slopeq3.5/figures/dohnanyi_differential_histogram.png
Saved: outputs/SS_800MP_1000TP_500kyr_1Mearth_slopeq3.5/figures/count_vs_mass_histogram.png
Saved: outputs/SS_800MP_1000TP_500kyr_1Mearth_slopeq3.5/figures/count_vs_radius_histogram.png

Stirrer-coverage check (Krivov & Booth 2018: N x delta_af >= delta_a):
  Stirrers inside the belt [95, 105]: N = 800
  delta_af = 8 sqrt(3) h_M a_M:  mean = 1.334670e+00, sum over stirrers = 1.067736e+03
  Belt width delta_a = 1.000000e+01
  Coverage ratio (sum delta_af / delta_a) = 106.774
  OK: stirrer feeding zones span the belt.

Beginning the main integration
Output 1/50: t=0.0 yr, dE/E0=0.00e+00, N=1801
  Estimated time remaining to complete simulation: 11 seconds
  Estimated time remaining to next output: 0 seconds
Output 2/50: t=10000.0 yr, dE/E0=2.34e-05, N=1801
  Estimated time remaining to complete simulation: 1 weeks, 5 days, 11 hours, 17 minutes, 44 seconds
  Estimated time remaining to next output: 6 hours, 14 minutes, 7 seconds
Output 3/50: t=20000.0 yr, dE/E0=2.34e-05, N=1801
  Estimated time remaining to complete simulation: 2 weeks, 12 hours, 7 minutes, 24 seconds
  Estimated time remaining to next output: 7 hours, 24 minutes, 24 seconds
Output 4/50: t=30000.0 yr, dE/E0=2.34e-05, N=1801
  Estimated time remaining to complete simulation: 1 weeks, 6 days, 19 hours, 34 minutes, 31 seconds
  Estimated time remaining to next output: 7 hours, 12 minutes, 29 seconds
Output 5/50: t=40000.0 yr, dE/E0=2.34e-05, N=1801
  Estimated time remaining to complete simulation: 1 weeks, 5 days, 5 hours, 31 minutes, 35 seconds
  Estimated time remaining to next output: 6 hours, 31 minutes, 22 seconds
Output 6/50: t=50000.0 yr, dE/E0=2.34e-05, N=1801
  Estimated time remaining to complete simulation: 1 weeks, 3 days, 16 hours, 5 minutes, 39 seconds
  Estimated time remaining to next output: 5 hours, 49 minutes, 13 seconds
Output 7/50: t=60000.0 yr, dE/E0=2.34e-05, N=1801
  Estimated time remaining to complete simulation: 1 weeks, 2 days, 12 hours, 21 minutes, 10 seconds
  Estimated time remaining to next output: 5 hours, 18 minutes, 37 seconds
Output 8/50: t=70000.0 yr, dE/E0=2.34e-05, N=1801
  Estimated time remaining to complete simulation: 1 weeks, 1 days, 17 hours, 2 minutes, 15 seconds
  Estimated time remaining to next output: 4 hours, 58 minutes, 37 seconds
Output 9/50: t=80000.0 yr, dE/E0=2.34e-05, N=1801
  Estimated time remaining to complete simulation: 1 weeks, 22 hours, 28 minutes, 45 seconds
  Estimated time remaining to next output: 4 hours, 38 minutes, 45 seconds
Output 10/50: t=90000.0 yr, dE/E0=2.34e-05, N=1801
  Estimated time remaining to complete simulation: 1 weeks, 6 hours, 14 minutes, 39 seconds
  Estimated time remaining to next output: 4 hours, 21 minutes, 21 seconds
Output 11/50: t=100000.0 yr, dE/E0=2.34e-05, N=1801
  Estimated time remaining to complete simulation: 6 days, 13 hours, 45 minutes, 13 seconds
  Estimated time remaining to next output: 4 hours, 2 minutes, 41 seconds
Output 12/50: t=110000.0 yr, dE/E0=2.34e-05, N=1801
  Estimated time remaining to complete simulation: 5 days, 22 hours, 36 minutes, 15 seconds
  Estimated time remaining to next output: 3 hours, 45 minutes, 9 seconds
Output 13/50: t=120000.0 yr, dE/E0=2.34e-05, N=1801
  Estimated time remaining to complete simulation: 5 days, 9 hours, 42 minutes, 44 seconds
  Estimated time remaining to next output: 3 hours, 30 minutes, 20 seconds
Output 14/50: t=130000.0 yr, dE/E0=2.34e-05, N=1801
  Estimated time remaining to complete simulation: 4 days, 22 hours, 41 minutes, 53 seconds
  Estimated time remaining to next output: 3 hours, 17 minutes, 49 seconds
Output 15/50: t=140000.0 yr, dE/E0=2.34e-05, N=1801
  Estimated time remaining to complete simulation: 4 days, 14 hours, 12 minutes, 57 seconds
  Estimated time remaining to next output: 3 hours, 8 minutes, 56 seconds
Output 16/50: t=150000.0 yr, dE/E0=2.34e-05, N=1801
  Estimated time remaining to complete simulation: 4 days, 6 hours, 15 minutes, 11 seconds
  Estimated time remaining to next output: 3 hours, 26 seconds
Output 17/50: t=160000.0 yr, dE/E0=2.34e-05, N=1801
  Estimated time remaining to complete simulation: 3 days, 23 hours, 3 minutes, 38 seconds
  Estimated time remaining to next output: 2 hours, 52 minutes, 50 seconds
Output 18/50: t=170000.0 yr, dE/E0=2.34e-05, N=1801
  Estimated time remaining to complete simulation: 3 days, 16 hours, 30 minutes, 55 seconds
  Estimated time remaining to next output: 2 hours, 45 minutes, 57 seconds
Output 19/50: t=180000.0 yr, dE/E0=2.34e-05, N=1801
  Estimated time remaining to complete simulation: 3 days, 10 hours, 19 minutes, 4 seconds
  Estimated time remaining to next output: 2 hours, 39 minutes, 19 seconds
Output 20/50: t=190000.0 yr, dE/E0=2.34e-05, N=1801
  Estimated time remaining to complete simulation: 3 days, 4 hours, 18 minutes, 31 seconds
  Estimated time remaining to next output: 2 hours, 32 minutes, 37 seconds
Output 21/50: t=200000.0 yr, dE/E0=2.34e-05, N=1801
  Estimated time remaining to complete simulation: 2 days, 22 hours, 57 minutes, 44 seconds
  Estimated time remaining to next output: 2 hours, 26 minutes, 49 seconds
Output 22/50: t=210000.0 yr, dE/E0=2.34e-05, N=1801
  Estimated time remaining to complete simulation: 2 days, 18 hours, 1 minutes
  Estimated time remaining to next output: 2 hours, 21 minutes, 27 seconds
Output 23/50: t=220000.0 yr, dE/E0=2.34e-05, N=1801
  Estimated time remaining to complete simulation: 2 days, 13 hours, 24 minutes, 7 seconds
  Estimated time remaining to next output: 2 hours, 16 minutes, 26 seconds
Output 24/50: t=230000.0 yr, dE/E0=2.34e-05, N=1801
  Estimated time remaining to complete simulation: 2 days, 9 hours, 12 minutes, 25 seconds
  Estimated time remaining to next output: 2 hours, 12 minutes
Output 25/50: t=240000.0 yr, dE/E0=2.34e-05, N=1801
  Estimated time remaining to complete simulation: 2 days, 5 hours, 12 minutes, 4 seconds
  Estimated time remaining to next output: 2 hours, 7 minutes, 40 seconds
Output 26/50: t=250000.0 yr, dE/E0=2.34e-05, N=1801
  Estimated time remaining to complete simulation: 2 days, 1 hours, 27 minutes, 40 seconds
  Estimated time remaining to next output: 2 hours, 3 minutes, 39 seconds
Output 27/50: t=260000.0 yr, dE/E0=2.34e-05, N=1801
  Estimated time remaining to complete simulation: 1 days, 22 hours, 2 minutes, 11 seconds
  Estimated time remaining to next output: 2 hours, 5 seconds
Output 28/50: t=270000.0 yr, dE/E0=2.34e-05, N=1801
  Estimated time remaining to complete simulation: 1 days, 18 hours, 49 minutes, 32 seconds
  Estimated time remaining to next output: 1 hours, 56 minutes, 47 seconds
Output 29/50: t=280000.0 yr, dE/E0=2.34e-05, N=1801
  Estimated time remaining to complete simulation: 1 days, 15 hours, 47 minutes, 13 seconds
  Estimated time remaining to next output: 1 hours, 53 minutes, 40 seconds
Output 30/50: t=290000.0 yr, dE/E0=2.34e-05, N=1801
  Estimated time remaining to complete simulation: 1 days, 12 hours, 54 minutes, 19 seconds
  Estimated time remaining to next output: 1 hours, 50 minutes, 42 seconds
Output 31/50: t=300000.0 yr, dE/E0=2.34e-05, N=1801
  Estimated time remaining to complete simulation: 1 days, 10 hours, 13 minutes, 40 seconds
  Estimated time remaining to next output: 1 hours, 48 minutes, 5 seconds
Output 32/50: t=310000.0 yr, dE/E0=2.34e-05, N=1801
  Estimated time remaining to complete simulation: 1 days, 7 hours, 40 minutes, 39 seconds
  Estimated time remaining to next output: 1 hours, 45 minutes, 35 seconds
Output 33/50: t=320000.0 yr, dE/E0=2.34e-05, N=1801
  Estimated time remaining to complete simulation: 1 days, 5 hours, 14 minutes, 12 seconds
  Estimated time remaining to next output: 1 hours, 43 minutes, 11 seconds
Output 34/50: t=330000.0 yr, dE/E0=2.34e-05, N=1801
  Estimated time remaining to complete simulation: 1 days, 2 hours, 55 minutes, 1 seconds
  Estimated time remaining to next output: 1 hours, 40 minutes, 56 seconds
Output 35/50: t=340000.0 yr, dE/E0=2.34e-05, N=1801
  Estimated time remaining to complete simulation: 1 days, 42 minutes, 44 seconds
  Estimated time remaining to next output: 1 hours, 38 minutes, 50 seconds
Output 36/50: t=350000.0 yr, dE/E0=2.34e-05, N=1801
  Estimated time remaining to complete simulation: 22 hours, 34 minutes, 29 seconds
  Estimated time remaining to next output: 1 hours, 36 minutes, 44 seconds
Output 37/50: t=360000.0 yr, dE/E0=2.34e-05, N=1801
  Estimated time remaining to complete simulation: 20 hours, 32 minutes, 48 seconds
  Estimated time remaining to next output: 1 hours, 34 minutes, 49 seconds
Output 38/50: t=370000.0 yr, dE/E0=2.34e-05, N=1801
  Estimated time remaining to complete simulation: 18 hours, 35 minutes, 52 seconds
  Estimated time remaining to next output: 1 hours, 32 minutes, 59 seconds
Output 39/50: t=380000.0 yr, dE/E0=2.34e-05, N=1801
  Estimated time remaining to complete simulation: 16 hours, 44 minutes, 14 seconds
  Estimated time remaining to next output: 1 hours, 31 minutes, 17 seconds
Output 40/50: t=390000.0 yr, dE/E0=2.34e-05, N=1801
  Estimated time remaining to complete simulation: 14 hours, 56 minutes, 44 seconds
  Estimated time remaining to next output: 1 hours, 29 minutes, 40 seconds
Output 41/50: t=400000.0 yr, dE/E0=2.34e-05, N=1801
  Estimated time remaining to complete simulation: 13 hours, 12 minutes, 54 seconds
  Estimated time remaining to next output: 1 hours, 28 minutes, 6 seconds
Output 42/50: t=410000.0 yr, dE/E0=2.34e-05, N=1801
  Estimated time remaining to complete simulation: 11 hours, 32 minutes, 48 seconds
  Estimated time remaining to next output: 1 hours, 26 minutes, 36 seconds
Output 43/50: t=420000.0 yr, dE/E0=2.34e-05, N=1801
  Estimated time remaining to complete simulation: 9 hours, 56 minutes, 43 seconds
  Estimated time remaining to next output: 1 hours, 25 minutes, 14 seconds
Output 44/50: t=430000.0 yr, dE/E0=2.34e-05, N=1801
  Estimated time remaining to complete simulation: 8 hours, 22 minutes, 51 seconds
  Estimated time remaining to next output: 1 hours, 23 minutes, 48 seconds
Output 45/50: t=440000.0 yr, dE/E0=2.34e-05, N=1801
  Estimated time remaining to complete simulation: 6 hours, 52 minutes, 49 seconds
  Estimated time remaining to next output: 1 hours, 22 minutes, 33 seconds
Output 46/50: t=450000.0 yr, dE/E0=2.34e-05, N=1801
  Estimated time remaining to complete simulation: 5 hours, 26 minutes, 13 seconds
  Estimated time remaining to next output: 1 hours, 21 minutes, 33 seconds
Output 47/50: t=460000.0 yr, dE/E0=2.34e-05, N=1801
  Estimated time remaining to complete simulation: 4 hours, 1 minutes, 49 seconds
  Estimated time remaining to next output: 1 hours, 20 minutes, 36 seconds
Output 48/50: t=470000.0 yr, dE/E0=2.34e-05, N=1801
  Estimated time remaining to complete simulation: 2 hours, 39 minutes, 19 seconds
  Estimated time remaining to next output: 1 hours, 19 minutes, 39 seconds
Output 49/50: t=480000.0 yr, dE/E0=2.34e-05, N=1801
  Estimated time remaining to complete simulation: 1 hours, 18 minutes, 48 seconds
  Estimated time remaining to next output: 1 hours, 18 minutes, 48 seconds
Output 50/50: t=490000.0 yr, dE/E0=2.34e-05, N=1801
  Estimated time remaining to complete simulation: 0 seconds
Output 51/50: t=500000.0 yr, dE/E0=2.34e-05, N=1801
  Estimated time remaining to complete simulation: -1 months, 4 weeks, 1 days, 22 hours, 43 minutes, 18 seconds

Simulation complete.
Total runtime: 2 days, 17 hours, 11 minutes, 56 seconds

Krivov & Booth (2018) self-stirring check (Eqs. 9-10):
  Final time:                 t = 5.000000e+05 yr
  Rayleigh outlier cut:       e > 5 sigma = 4.0131e-02 (sigma = median(e)/sqrt(2 ln 2) = 8.0262e-03)
  Stirred-disk check:         median(e) = 9.4501e-03 vs 30 x disk.emax = 9.6000e-04 -> stirred, cut applied
  Excluded MPs:               2 -- MP_335 (e = 0.1647), MP_107 (e = 0.0446)
  KS test of kept e vs Rayleigh: D = 0.0339, p = 0.312
  RMS eccentricity (798 of 800 MPs): 1.149475e-02  (all MPs: 1.296967e-02)
  Belt geometry:              a = 100, da = 10, a/da = 10
  Masses:                     M_max = 2.585122e-08 Msun, M_disc = 3.003490e-06 Msun
  Implied stirring timescale: T = 5.727994e+13 yr
  Effective stirring factor:  C_e = 22.4853  (all MPs, no cut: 36.4433)
  NOTE: C_e revised 2026-09-30; the values above were recomputed from the final snapshot of the archive: (1) `compute_effective_stirring_C_e` in `src/simulation/run_simulation.py` previously used the *mean* massive-planetesimal mass (M_disc / N) as the individual stirrer mass M in Krivov & Booth Eq. 9; it now uses the *maximum* massive-planetesimal mass of the sample. (2) RMS(e) now excludes Rayleigh outliers, e > 5 sigma with sigma = median(e)/sqrt(2 ln 2) (bodies scattered by a single strong encounter, e.g. an initially Hill-overlapping pair), applied only once the disk is stirred (median(e) >= 30 x disk.emax); a KS test against a Rayleigh distribution is reported as a diagnostic but does not switch the cut. M and M_disc still use every massive planetesimal. History: C_e = 250.9356 (mean M, all MPs) -> 36.4433 (max M, all MPs) -> 22.4853 (max M, Rayleigh cut; current).
Saved archive: outputs/SS_800MP_1000TP_500kyr_1Mearth_slopeq3.5/SS_800MP_1000TP_500kyr_1Mearth_slopeq3.5.bin
Number of snapshots saved: 51
Archive time range: 0.000e+00 yr to 5.000e+05 yr
Loaded snapshot table from archive.
role
test_particle           1000
massive_planetesimal     800
star                       1
Name: count, dtype: int64
Saved: outputs/SS_800MP_1000TP_500kyr_1Mearth_slopeq3.5/figures/survival_fraction_vs_time.png
Saved: outputs/SS_800MP_1000TP_500kyr_1Mearth_slopeq3.5/figures/mean_semimajor_axis_vs_time.png
Saved: outputs/SS_800MP_1000TP_500kyr_1Mearth_slopeq3.5/figures/mean_eccentricity_vs_time.png
Saved: outputs/SS_800MP_1000TP_500kyr_1Mearth_slopeq3.5/figures/rms_eccentricity_vs_time.png
Saved: outputs/SS_800MP_1000TP_500kyr_1Mearth_slopeq3.5/figures/rms_inclination_vs_time.png
Saved: outputs/SS_800MP_1000TP_500kyr_1Mearth_slopeq3.5/figures/a_vs_e_initial_final.png
Saved: outputs/SS_800MP_1000TP_500kyr_1Mearth_slopeq3.5/figures/a_vs_i_initial_final.png
Inner plotted edge = 95.00 AU
Outer plotted edge = 104.99 AU
Saved: outputs/SS_800MP_1000TP_500kyr_1Mearth_slopeq3.5/figures/xy_initial_final.png
All summary figures saved.
```
