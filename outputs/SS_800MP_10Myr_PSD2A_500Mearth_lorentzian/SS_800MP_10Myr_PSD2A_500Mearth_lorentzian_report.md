# SS_800MP_10Myr_PSD2A_500Mearth_lorentzian — Simulation Report

Config file: `config/SS_800MP_10Myr_PSD2A_500Mearth_lorentzian.yaml`
Archive file: `outputs/SS_800MP_10Myr_PSD2A_500Mearth_lorentzian/SS_800MP_10Myr_PSD2A_500Mearth_lorentzian.bin`

## Provenance

- Run UUID: `54e9d070-1adf-4b55-8436-1459100476e0`
- Created: 2026-10-14T17:55:54-03:00
- Finished: 2026-10-21T21:20:43-03:00
- Wall runtime: 197752.7 s
- Outcome: completed
- Command: `src/simulation/run_simulation.py config/SS_800MP_10Myr_PSD2A_500Mearth_lorentzian.yaml`
- Git commit: `c51684a1af3fc9db2ba4446455a2f524e91594de` (branch `main`) **(DIRTY — uncommitted tracked changes)**
    - modified: `notebooks/mass_model_playground.ipynb`
- Software: python 3.12.14, rebound 5.0.0, numpy 2.4.6, pandas 3.0.3, matplotlib 3.10.9, pyyaml 6.0.3
- Resumed 1 time(s) after the first run
- Frozen config: `config.yaml` (this directory)
- Full environment: `environment.txt` (this directory)

## Simulation
- Name: SS_800MP_10Myr_PSD2A_500Mearth_lorentzian
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
- Mass: 1.57285351 Mjup
- a: 68.031371 au, e: 0.0, inc: 0.0 deg
- omega: 0.0 deg, Omega random: True
- t_peri_jd: 2451545.0, orbital_period_days: 204952.894, epoch_jd: 2451545.0

## Disk
- a: [95, 105] au
- a distribution: Lorentzian in ln a, mu_0 = 100 au, sigma = 1 au
- e: [0.0, 3.2e-05]
- inc: [0.0, 3.2e-05] deg

## Massive Planetesimals
- N: 800
- Mass-assignment method (config): loaded from CSV (mode=csv): variable=radius, path=src/mass_models/Plantesimal_Size_Dist_2_1Mearth/model_A/selected.csv, slope=2.5 (radii/masses read verbatim from file; disk mass computed from file, not split by a power law)
- **Mass is NOT uniform** across the 800 massive planetesimals:
  - min / median / max: 2.201214e-09 / 3.539820e-09 / 6.368760e-09 Msun
  - min / median / max: 7.328854e-04 / 1.178569e-03 / 2.120454e-03 Earth masses
  - total disk mass: 1.000000e+00 Earth masses

## Test Particles
- N: 0
- Distribution: uniform

## Run Summary (from archive)
- Initial particle count: 802
- Final particle count: 798
- Particles lost (escaped / unbound / other removal): 4
- Archive time range: 0.000000e+00 to 1.000000e+07
- Number of snapshots: 1002

## Terminal Output

```
Saving SimulationArchive to: outputs/SS_800MP_10Myr_PSD2A_500Mearth_lorentzian/SS_800MP_10Myr_PSD2A_500Mearth_lorentzian.bin
Resuming from t=4.580000e+06 yr: times=array([ 4580000.,  4590000.,  4600000.,  4610000.,  4620000.,  4630000.,
        4640000.,  4650000.,  4660000.,  4670000.,  4680000.,  4690000.,
        4700000.,  4710000.,  4720000.,  4730000.,  4740000.,  4750000.,
        4760000.,  4770000.,  4780000.,  4790000.,  4800000.,  4810000.,
        4820000.,  4830000.,  4840000.,  4850000.,  4860000.,  4870000.,
        4880000.,  4890000.,  4900000.,  4910000.,  4920000.,  4930000.,
        4940000.,  4950000.,  4960000.,  4970000.,  4980000.,  4990000.,
        5000000.,  5010000.,  5020000.,  5030000.,  5040000.,  5050000.,
        5060000.,  5070000.,  5080000.,  5090000.,  5100000.,  5110000.,
        5120000.,  5130000.,  5140000.,  5150000.,  5160000.,  5170000.,
        5180000.,  5190000.,  5200000.,  5210000.,  5220000.,  5230000.,
        5240000.,  5250000.,  5260000.,  5270000.,  5280000.,  5290000.,
        5300000.,  5310000.,  5320000.,  5330000.,  5340000.,  5350000.,
        5360000.,  5370000.,  5380000.,  5390000.,  5400000.,  5410000.,
        5420000.,  5430000.,  5440000.,  5450000.,  5460000.,  5470000.,
        5480000.,  5490000.,  5500000.,  5510000.,  5520000.,  5530000.,
        5540000.,  5550000.,  5560000.,  5570000.,  5580000.,  5590000.,
        5600000.,  5610000.,  5620000.,  5630000.,  5640000.,  5650000.,
        5660000.,  5670000.,  5680000.,  5690000.,  5700000.,  5710000.,
        5720000.,  5730000.,  5740000.,  5750000.,  5760000.,  5770000.,
        5780000.,  5790000.,  5800000.,  5810000.,  5820000.,  5830000.,
        5840000.,  5850000.,  5860000.,  5870000.,  5880000.,  5890000.,
        5900000.,  5910000.,  5920000.,  5930000.,  5940000.,  5950000.,
        5960000.,  5970000.,  5980000.,  5990000.,  6000000.,  6010000.,
        6020000.,  6030000.,  6040000.,  6050000.,  6060000.,  6070000.,
        6080000.,  6090000.,  6100000.,  6110000.,  6120000.,  6130000.,
        6140000.,  6150000.,  6160000.,  6170000.,  6180000.,  6190000.,
        6200000.,  6210000.,  6220000.,  6230000.,  6240000.,  6250000.,
        6260000.,  6270000.,  6280000.,  6290000.,  6300000.,  6310000.,
        6320000.,  6330000.,  6340000.,  6350000.,  6360000.,  6370000.,
        6380000.,  6390000.,  6400000.,  6410000.,  6420000.,  6430000.,
        6440000.,  6450000.,  6460000.,  6470000.,  6480000.,  6490000.,
        6500000.,  6510000.,  6520000.,  6530000.,  6540000.,  6550000.,
        6560000.,  6570000.,  6580000.,  6590000.,  6600000.,  6610000.,
        6620000.,  6630000.,  6640000.,  6650000.,  6660000.,  6670000.,
        6680000.,  6690000.,  6700000.,  6710000.,  6720000.,  6730000.,
        6740000.,  6750000.,  6760000.,  6770000.,  6780000.,  6790000.,
        6800000.,  6810000.,  6820000.,  6830000.,  6840000.,  6850000.,
        6860000.,  6870000.,  6880000.,  6890000.,  6900000.,  6910000.,
        6920000.,  6930000.,  6940000.,  6950000.,  6960000.,  6970000.,
        6980000.,  6990000.,  7000000.,  7010000.,  7020000.,  7030000.,
        7040000.,  7050000.,  7060000.,  7070000.,  7080000.,  7090000.,
        7100000.,  7110000.,  7120000.,  7130000.,  7140000.,  7150000.,
        7160000.,  7170000.,  7180000.,  7190000.,  7200000.,  7210000.,
        7220000.,  7230000.,  7240000.,  7250000.,  7260000.,  7270000.,
        7280000.,  7290000.,  7300000.,  7310000.,  7320000.,  7330000.,
        7340000.,  7350000.,  7360000.,  7370000.,  7380000.,  7390000.,
        7400000.,  7410000.,  7420000.,  7430000.,  7440000.,  7450000.,
        7460000.,  7470000.,  7480000.,  7490000.,  7500000.,  7510000.,
        7520000.,  7530000.,  7540000.,  7550000.,  7560000.,  7570000.,
        7580000.,  7590000.,  7600000.,  7610000.,  7620000.,  7630000.,
        7640000.,  7650000.,  7660000.,  7670000.,  7680000.,  7690000.,
        7700000.,  7710000.,  7720000.,  7730000.,  7740000.,  7750000.,
        7760000.,  7770000.,  7780000.,  7790000.,  7800000.,  7810000.,
        7820000.,  7830000.,  7840000.,  7850000.,  7860000.,  7870000.,
        7880000.,  7890000.,  7900000.,  7910000.,  7920000.,  7930000.,
        7940000.,  7950000.,  7960000.,  7970000.,  7980000.,  7990000.,
        8000000.,  8010000.,  8020000.,  8030000.,  8040000.,  8050000.,
        8060000.,  8070000.,  8080000.,  8090000.,  8100000.,  8110000.,
        8120000.,  8130000.,  8140000.,  8150000.,  8160000.,  8170000.,
        8180000.,  8190000.,  8200000.,  8210000.,  8220000.,  8230000.,
        8240000.,  8250000.,  8260000.,  8270000.,  8280000.,  8290000.,
        8300000.,  8310000.,  8320000.,  8330000.,  8340000.,  8350000.,
        8360000.,  8370000.,  8380000.,  8390000.,  8400000.,  8410000.,
        8420000.,  8430000.,  8440000.,  8450000.,  8460000.,  8470000.,
        8480000.,  8490000.,  8500000.,  8510000.,  8520000.,  8530000.,
        8540000.,  8550000.,  8560000.,  8570000.,  8580000.,  8590000.,
        8600000.,  8610000.,  8620000.,  8630000.,  8640000.,  8650000.,
        8660000.,  8670000.,  8680000.,  8690000.,  8700000.,  8710000.,
        8720000.,  8730000.,  8740000.,  8750000.,  8760000.,  8770000.,
        8780000.,  8790000.,  8800000.,  8810000.,  8820000.,  8830000.,
        8840000.,  8850000.,  8860000.,  8870000.,  8880000.,  8890000.,
        8900000.,  8910000.,  8920000.,  8930000.,  8940000.,  8950000.,
        8960000.,  8970000.,  8980000.,  8990000.,  9000000.,  9010000.,
        9020000.,  9030000.,  9040000.,  9050000.,  9060000.,  9070000.,
        9080000.,  9090000.,  9100000.,  9110000.,  9120000.,  9130000.,
        9140000.,  9150000.,  9160000.,  9170000.,  9180000.,  9190000.,
        9200000.,  9210000.,  9220000.,  9230000.,  9240000.,  9250000.,
        9260000.,  9270000.,  9280000.,  9290000.,  9300000.,  9310000.,
        9320000.,  9330000.,  9340000.,  9350000.,  9360000.,  9370000.,
        9380000.,  9390000.,  9400000.,  9410000.,  9420000.,  9430000.,
        9440000.,  9450000.,  9460000.,  9470000.,  9480000.,  9490000.,
        9500000.,  9510000.,  9520000.,  9530000.,  9540000.,  9550000.,
        9560000.,  9570000.,  9580000.,  9590000.,  9600000.,  9610000.,
        9620000.,  9630000.,  9640000.,  9650000.,  9660000.,  9670000.,
        9680000.,  9690000.,  9700000.,  9710000.,  9720000.,  9730000.,
        9740000.,  9750000.,  9760000.,  9770000.,  9780000.,  9790000.,
        9800000.,  9810000.,  9820000.,  9830000.,  9840000.,  9850000.,
        9860000.,  9870000.,  9880000.,  9890000.,  9900000.,  9910000.,
        9920000.,  9930000.,  9940000.,  9950000.,  9960000.,  9970000.,
        9980000.,  9990000., 10000000.])
Found dump file. Restoring simulation from snapshot...
  Timestep: 5.607169e+01 (0.1 x giant planet orbital period = 5.607169e+02)
Restored simulation from snapshot number at t=4.580000e+06 yr with N=801 particles.

Stirrer-coverage check (Krivov & Booth 2018: N x delta_af >= delta_a):
  Stirrers inside the belt [95, 105]: N = 774
  delta_af = 8 sqrt(3) h_M a_M:  mean = 1.479485e+00, sum over stirrers = 1.145122e+03
  Belt width delta_a = 1.000000e+01
  Coverage ratio (sum delta_af / delta_a) = 114.512
  OK: stirrer feeding zones span the belt.

Beginning the main integration
Output 1/542: t=4580000.0 yr, dE/E0=0.00e+00, N=801
  Estimated time remaining to complete simulation: 52 seconds
  Estimated time remaining to next output: 0 seconds
Output 2/542: t=4590000.0 yr, dE/E0=3.20e-09, N=801
  Estimated time remaining to complete simulation: 22 hours, 40 minutes, 12 seconds
  Estimated time remaining to next output: 2 minutes, 31 seconds
Output 3/542: t=4600000.0 yr, dE/E0=1.38e-08, N=801
  Estimated time remaining to complete simulation: 1 days, 5 hours, 54 minutes, 21 seconds
  Estimated time remaining to next output: 3 minutes, 19 seconds
Output 4/542: t=4610000.0 yr, dE/E0=2.24e-08, N=801
  Estimated time remaining to complete simulation: 1 days, 9 hours, 32 minutes, 25 seconds
  Estimated time remaining to next output: 3 minutes, 44 seconds
Output 5/542: t=4620000.0 yr, dE/E0=3.02e-08, N=801
  Estimated time remaining to complete simulation: 1 days, 11 hours, 47 minutes, 20 seconds
  Estimated time remaining to next output: 3 minutes, 59 seconds
Output 6/542: t=4630000.0 yr, dE/E0=1.96e-08, N=801
  Estimated time remaining to complete simulation: 1 days, 13 hours, 25 minutes, 7 seconds
  Estimated time remaining to next output: 4 minutes, 11 seconds
Output 7/542: t=4640000.0 yr, dE/E0=2.41e-08, N=801
  Estimated time remaining to complete simulation: 1 days, 14 hours, 36 minutes, 33 seconds
  Estimated time remaining to next output: 4 minutes, 19 seconds
Output 8/542: t=4650000.0 yr, dE/E0=1.78e-08, N=801
  Estimated time remaining to complete simulation: 1 days, 15 hours, 23 minutes, 34 seconds
  Estimated time remaining to next output: 4 minutes, 25 seconds
Output 9/542: t=4660000.0 yr, dE/E0=1.56e-08, N=801
  Estimated time remaining to complete simulation: 1 days, 15 hours, 54 minutes, 47 seconds
  Estimated time remaining to next output: 4 minutes, 29 seconds
Output 10/542: t=4670000.0 yr, dE/E0=2.66e-08, N=801
  Estimated time remaining to complete simulation: 1 days, 16 hours, 48 minutes
  Estimated time remaining to next output: 4 minutes, 36 seconds
Output 11/542: t=4680000.0 yr, dE/E0=2.95e-08, N=801
  Estimated time remaining to complete simulation: 1 days, 16 hours, 52 minutes, 59 seconds
  Estimated time remaining to next output: 4 minutes, 37 seconds
Output 12/542: t=4690000.0 yr, dE/E0=1.52e-08, N=801
  Estimated time remaining to complete simulation: 1 days, 17 hours, 8 minutes, 7 seconds
  Estimated time remaining to next output: 4 minutes, 39 seconds
Output 13/542: t=4700000.0 yr, dE/E0=1.99e-08, N=801
  Estimated time remaining to complete simulation: 1 days, 17 hours, 36 minutes, 58 seconds
  Estimated time remaining to next output: 4 minutes, 43 seconds
Output 14/542: t=4710000.0 yr, dE/E0=2.04e-08, N=801
  Estimated time remaining to complete simulation: 1 days, 17 hours, 58 minutes, 9 seconds
  Estimated time remaining to next output: 4 minutes, 46 seconds
Output 15/542: t=4720000.0 yr, dE/E0=2.07e-08, N=801
  Estimated time remaining to complete simulation: 1 days, 17 hours, 55 minutes, 50 seconds
  Estimated time remaining to next output: 4 minutes, 46 seconds
Output 16/542: t=4730000.0 yr, dE/E0=3.67e-08, N=801
  Estimated time remaining to complete simulation: 1 days, 18 hours, 6 minutes, 28 seconds
  Estimated time remaining to next output: 4 minutes, 48 seconds
A particle escaped (r>exit_max_distance).
Removing escaped particle at index 385
Remaining particles: 800
Output 17/542: t=4736896.8 yr, dE/E0=3.30e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 17 hours, 23 minutes, 42 seconds
  Estimated time remaining to next output: 4 minutes, 43 seconds
Output 18/542: t=4750000.0 yr, dE/E0=3.26e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 18 hours, 11 minutes, 1 seconds
  Estimated time remaining to next output: 4 minutes, 49 seconds
Output 19/542: t=4760000.0 yr, dE/E0=3.24e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 18 hours, 20 minutes, 25 seconds
  Estimated time remaining to next output: 4 minutes, 51 seconds
Output 20/542: t=4770000.0 yr, dE/E0=3.21e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 18 hours, 21 minutes, 43 seconds
  Estimated time remaining to next output: 4 minutes, 52 seconds
Output 21/542: t=4780000.0 yr, dE/E0=3.28e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 18 hours, 29 minutes, 34 seconds
  Estimated time remaining to next output: 4 minutes, 53 seconds
Output 22/542: t=4790000.0 yr, dE/E0=3.46e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 18 hours, 34 minutes, 7 seconds
  Estimated time remaining to next output: 4 minutes, 54 seconds
Output 23/542: t=4800000.0 yr, dE/E0=3.46e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 18 hours, 39 minutes, 48 seconds
  Estimated time remaining to next output: 4 minutes, 55 seconds
Output 24/542: t=4810000.0 yr, dE/E0=3.34e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 18 hours, 34 minutes, 50 seconds
  Estimated time remaining to next output: 4 minutes, 55 seconds
Output 25/542: t=4820000.0 yr, dE/E0=3.36e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 18 hours, 32 minutes, 59 seconds
  Estimated time remaining to next output: 4 minutes, 56 seconds
Output 26/542: t=4830000.0 yr, dE/E0=3.35e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 18 hours, 33 minutes, 41 seconds
  Estimated time remaining to next output: 4 minutes, 56 seconds
Output 27/542: t=4840000.0 yr, dE/E0=3.37e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 18 hours, 31 minutes, 52 seconds
  Estimated time remaining to next output: 4 minutes, 57 seconds
Output 28/542: t=4850000.0 yr, dE/E0=3.44e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 18 hours, 33 minutes, 40 seconds
  Estimated time remaining to next output: 4 minutes, 58 seconds
Output 29/542: t=4860000.0 yr, dE/E0=3.51e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 18 hours, 27 minutes, 35 seconds
  Estimated time remaining to next output: 4 minutes, 57 seconds
Output 30/542: t=4870000.0 yr, dE/E0=3.42e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 18 hours, 29 minutes, 42 seconds
  Estimated time remaining to next output: 4 minutes, 58 seconds
Output 31/542: t=4880000.0 yr, dE/E0=3.37e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 18 hours, 27 minutes, 19 seconds
  Estimated time remaining to next output: 4 minutes, 59 seconds
Output 32/542: t=4890000.0 yr, dE/E0=3.33e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 18 hours, 22 minutes, 58 seconds
  Estimated time remaining to next output: 4 minutes, 59 seconds
Output 33/542: t=4900000.0 yr, dE/E0=3.49e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 18 hours, 21 minutes, 2 seconds
  Estimated time remaining to next output: 4 minutes, 59 seconds
Output 34/542: t=4910000.0 yr, dE/E0=3.49e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 18 hours, 21 minutes, 44 seconds
  Estimated time remaining to next output: 5 minutes
Output 35/542: t=4920000.0 yr, dE/E0=3.55e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 18 hours, 27 minutes, 8 seconds
  Estimated time remaining to next output: 5 minutes, 1 seconds
Output 36/542: t=4930000.0 yr, dE/E0=3.41e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 18 hours, 26 minutes, 27 seconds
  Estimated time remaining to next output: 5 minutes, 1 seconds
Output 37/542: t=4940000.0 yr, dE/E0=3.43e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 18 hours, 29 minutes, 54 seconds
  Estimated time remaining to next output: 5 minutes, 2 seconds
Output 38/542: t=4950000.0 yr, dE/E0=3.35e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 18 hours, 26 minutes, 57 seconds
  Estimated time remaining to next output: 5 minutes, 3 seconds
Output 39/542: t=4960000.0 yr, dE/E0=3.41e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 18 hours, 26 minutes, 14 seconds
  Estimated time remaining to next output: 5 minutes, 3 seconds
Output 40/542: t=4970000.0 yr, dE/E0=3.63e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 18 hours, 22 minutes, 48 seconds
  Estimated time remaining to next output: 5 minutes, 3 seconds
Output 41/542: t=4980000.0 yr, dE/E0=3.55e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 18 hours, 18 minutes, 49 seconds
  Estimated time remaining to next output: 5 minutes, 4 seconds
Output 42/542: t=4990000.0 yr, dE/E0=3.45e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 18 hours, 19 minutes, 48 seconds
  Estimated time remaining to next output: 5 minutes, 4 seconds
Output 43/542: t=5000000.0 yr, dE/E0=3.40e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 18 hours, 13 minutes, 22 seconds
  Estimated time remaining to next output: 5 minutes, 4 seconds
Output 44/542: t=5010000.0 yr, dE/E0=3.37e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 18 hours, 11 minutes, 28 seconds
  Estimated time remaining to next output: 5 minutes, 4 seconds
Output 45/542: t=5020000.0 yr, dE/E0=3.37e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 18 hours, 11 minutes, 57 seconds
  Estimated time remaining to next output: 5 minutes, 5 seconds
Output 46/542: t=5030000.0 yr, dE/E0=3.58e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 18 hours, 7 minutes, 5 seconds
  Estimated time remaining to next output: 5 minutes, 5 seconds
Output 47/542: t=5040000.0 yr, dE/E0=3.63e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 18 hours, 2 minutes, 44 seconds
  Estimated time remaining to next output: 5 minutes, 5 seconds
Output 48/542: t=5050000.0 yr, dE/E0=3.55e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 17 hours, 59 minutes, 53 seconds
  Estimated time remaining to next output: 5 minutes, 6 seconds
Output 49/542: t=5060000.0 yr, dE/E0=3.53e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 18 hours, 23 seconds
  Estimated time remaining to next output: 5 minutes, 6 seconds
Output 50/542: t=5070000.0 yr, dE/E0=3.49e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 17 hours, 57 minutes, 28 seconds
  Estimated time remaining to next output: 5 minutes, 7 seconds
Output 51/542: t=5080000.0 yr, dE/E0=3.57e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 17 hours, 51 minutes, 52 seconds
  Estimated time remaining to next output: 5 minutes, 6 seconds
Output 52/542: t=5090000.0 yr, dE/E0=3.71e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 17 hours, 48 minutes, 16 seconds
  Estimated time remaining to next output: 5 minutes, 7 seconds
Output 53/542: t=5100000.0 yr, dE/E0=3.69e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 17 hours, 46 minutes, 55 seconds
  Estimated time remaining to next output: 5 minutes, 7 seconds
Output 54/542: t=5110000.0 yr, dE/E0=3.52e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 17 hours, 43 minutes, 47 seconds
  Estimated time remaining to next output: 5 minutes, 7 seconds
Output 55/542: t=5120000.0 yr, dE/E0=3.55e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 17 hours, 42 minutes, 30 seconds
  Estimated time remaining to next output: 5 minutes, 8 seconds
Output 56/542: t=5130000.0 yr, dE/E0=3.54e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 17 hours, 40 minutes, 1 seconds
  Estimated time remaining to next output: 5 minutes, 8 seconds
Output 57/542: t=5140000.0 yr, dE/E0=3.48e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 17 hours, 34 minutes, 58 seconds
  Estimated time remaining to next output: 5 minutes, 8 seconds
Output 58/542: t=5150000.0 yr, dE/E0=3.56e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 17 hours, 29 minutes, 21 seconds
  Estimated time remaining to next output: 5 minutes, 8 seconds
Output 59/542: t=5160000.0 yr, dE/E0=3.57e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 17 hours, 28 minutes, 1 seconds
  Estimated time remaining to next output: 5 minutes, 9 seconds
Output 60/542: t=5170000.0 yr, dE/E0=3.57e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 17 hours, 22 minutes, 8 seconds
  Estimated time remaining to next output: 5 minutes, 8 seconds
Output 61/542: t=5180000.0 yr, dE/E0=3.52e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 17 hours, 16 minutes, 36 seconds
  Estimated time remaining to next output: 5 minutes, 8 seconds
Output 62/542: t=5190000.0 yr, dE/E0=3.54e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 17 hours, 12 minutes, 14 seconds
  Estimated time remaining to next output: 5 minutes, 9 seconds
Output 63/542: t=5200000.0 yr, dE/E0=3.60e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 17 hours, 8 minutes, 12 seconds
  Estimated time remaining to next output: 5 minutes, 9 seconds
Output 64/542: t=5210000.0 yr, dE/E0=3.67e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 17 hours, 5 minutes, 40 seconds
  Estimated time remaining to next output: 5 minutes, 9 seconds
Output 65/542: t=5220000.0 yr, dE/E0=3.71e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 17 hours, 2 minutes, 6 seconds
  Estimated time remaining to next output: 5 minutes, 9 seconds
Output 66/542: t=5230000.0 yr, dE/E0=3.68e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 16 hours, 59 minutes, 2 seconds
  Estimated time remaining to next output: 5 minutes, 9 seconds
Output 67/542: t=5240000.0 yr, dE/E0=3.60e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 16 hours, 54 minutes, 30 seconds
  Estimated time remaining to next output: 5 minutes, 10 seconds
Output 68/542: t=5250000.0 yr, dE/E0=3.60e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 16 hours, 49 minutes, 57 seconds
  Estimated time remaining to next output: 5 minutes, 10 seconds
Output 69/542: t=5260000.0 yr, dE/E0=3.67e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 16 hours, 44 minutes, 39 seconds
  Estimated time remaining to next output: 5 minutes, 10 seconds
Output 70/542: t=5270000.0 yr, dE/E0=3.71e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 16 hours, 37 minutes, 44 seconds
  Estimated time remaining to next output: 5 minutes, 9 seconds
Output 71/542: t=5280000.0 yr, dE/E0=3.73e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 16 hours, 36 minutes, 9 seconds
  Estimated time remaining to next output: 5 minutes, 10 seconds
Output 72/542: t=5290000.0 yr, dE/E0=3.75e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 16 hours, 33 minutes, 39 seconds
  Estimated time remaining to next output: 5 minutes, 10 seconds
Output 73/542: t=5300000.0 yr, dE/E0=3.64e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 16 hours, 27 minutes, 41 seconds
  Estimated time remaining to next output: 5 minutes, 10 seconds
Output 74/542: t=5310000.0 yr, dE/E0=3.66e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 16 hours, 24 minutes, 33 seconds
  Estimated time remaining to next output: 5 minutes, 10 seconds
Output 75/542: t=5320000.0 yr, dE/E0=3.65e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 16 hours, 19 minutes, 16 seconds
  Estimated time remaining to next output: 5 minutes, 10 seconds
Output 76/542: t=5330000.0 yr, dE/E0=3.75e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 16 hours, 14 minutes, 49 seconds
  Estimated time remaining to next output: 5 minutes, 10 seconds
Output 77/542: t=5340000.0 yr, dE/E0=3.72e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 16 hours, 10 minutes, 56 seconds
  Estimated time remaining to next output: 5 minutes, 11 seconds
Output 78/542: t=5350000.0 yr, dE/E0=3.80e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 16 hours, 7 minutes, 26 seconds
  Estimated time remaining to next output: 5 minutes, 11 seconds
Output 79/542: t=5360000.0 yr, dE/E0=3.76e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 16 hours, 2 minutes, 43 seconds
  Estimated time remaining to next output: 5 minutes, 11 seconds
Output 80/542: t=5370000.0 yr, dE/E0=3.69e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 15 hours, 56 minutes, 51 seconds
  Estimated time remaining to next output: 5 minutes, 11 seconds
Output 81/542: t=5380000.0 yr, dE/E0=3.81e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 15 hours, 52 minutes, 20 seconds
  Estimated time remaining to next output: 5 minutes, 11 seconds
Output 82/542: t=5390000.0 yr, dE/E0=3.81e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 15 hours, 48 minutes, 18 seconds
  Estimated time remaining to next output: 5 minutes, 11 seconds
Output 83/542: t=5400000.0 yr, dE/E0=3.86e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 15 hours, 43 minutes, 49 seconds
  Estimated time remaining to next output: 5 minutes, 11 seconds
Output 84/542: t=5410000.0 yr, dE/E0=3.80e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 15 hours, 39 minutes, 44 seconds
  Estimated time remaining to next output: 5 minutes, 11 seconds
Output 85/542: t=5420000.0 yr, dE/E0=3.68e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 15 hours, 35 minutes, 20 seconds
  Estimated time remaining to next output: 5 minutes, 11 seconds
Output 86/542: t=5430000.0 yr, dE/E0=3.70e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 15 hours, 30 minutes, 10 seconds
  Estimated time remaining to next output: 5 minutes, 11 seconds
Output 87/542: t=5440000.0 yr, dE/E0=3.74e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 15 hours, 25 minutes, 39 seconds
  Estimated time remaining to next output: 5 minutes, 11 seconds
Output 88/542: t=5450000.0 yr, dE/E0=3.81e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 15 hours, 21 minutes, 16 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 89/542: t=5460000.0 yr, dE/E0=3.85e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 15 hours, 16 minutes, 25 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 90/542: t=5470000.0 yr, dE/E0=3.71e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 15 hours, 11 minutes, 44 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 91/542: t=5480000.0 yr, dE/E0=3.70e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 15 hours, 8 minutes, 43 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 92/542: t=5490000.0 yr, dE/E0=3.64e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 15 hours, 3 minutes, 45 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 93/542: t=5500000.0 yr, dE/E0=3.68e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 14 hours, 57 minutes, 24 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 94/542: t=5510000.0 yr, dE/E0=3.74e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 14 hours, 51 minutes, 34 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 95/542: t=5520000.0 yr, dE/E0=3.79e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 14 hours, 46 minutes, 4 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 96/542: t=5530000.0 yr, dE/E0=3.77e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 14 hours, 40 minutes, 55 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 97/542: t=5540000.0 yr, dE/E0=3.68e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 14 hours, 36 minutes, 29 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 98/542: t=5550000.0 yr, dE/E0=3.75e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 14 hours, 30 minutes, 51 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 99/542: t=5560000.0 yr, dE/E0=3.73e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 14 hours, 25 minutes, 50 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 100/542: t=5570000.0 yr, dE/E0=3.77e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 14 hours, 20 minutes, 17 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 101/542: t=5580000.0 yr, dE/E0=3.80e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 14 hours, 16 minutes, 38 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 102/542: t=5590000.0 yr, dE/E0=3.74e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 14 hours, 11 minutes, 59 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 103/542: t=5600000.0 yr, dE/E0=3.67e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 14 hours, 8 minutes, 1 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 104/542: t=5610000.0 yr, dE/E0=3.69e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 14 hours, 3 minutes, 51 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 105/542: t=5620000.0 yr, dE/E0=3.65e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 13 hours, 57 minutes, 51 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 106/542: t=5630000.0 yr, dE/E0=3.83e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 13 hours, 51 minutes, 6 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 107/542: t=5640000.0 yr, dE/E0=3.76e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 13 hours, 47 minutes, 57 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 108/542: t=5650000.0 yr, dE/E0=3.66e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 13 hours, 42 minutes, 33 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 109/542: t=5660000.0 yr, dE/E0=3.68e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 13 hours, 38 minutes, 46 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 110/542: t=5670000.0 yr, dE/E0=3.55e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 13 hours, 34 minutes, 6 seconds
  Estimated time remaining to next output: 5 minutes, 13 seconds
Output 111/542: t=5680000.0 yr, dE/E0=3.66e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 13 hours, 27 minutes, 55 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 112/542: t=5690000.0 yr, dE/E0=3.75e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 13 hours, 21 minutes, 47 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 113/542: t=5700000.0 yr, dE/E0=3.83e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 13 hours, 17 minutes, 45 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 114/542: t=5710000.0 yr, dE/E0=3.81e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 13 hours, 12 minutes, 5 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 115/542: t=5720000.0 yr, dE/E0=3.84e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 13 hours, 6 minutes, 11 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 116/542: t=5730000.0 yr, dE/E0=3.85e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 13 hours, 1 minutes, 16 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 117/542: t=5740000.0 yr, dE/E0=3.90e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 12 hours, 56 minutes, 38 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 118/542: t=5750000.0 yr, dE/E0=3.93e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 12 hours, 52 minutes, 4 seconds
  Estimated time remaining to next output: 5 minutes, 13 seconds
Output 119/542: t=5760000.0 yr, dE/E0=3.98e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 12 hours, 46 minutes, 23 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 120/542: t=5770000.0 yr, dE/E0=4.02e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 12 hours, 41 minutes, 54 seconds
  Estimated time remaining to next output: 5 minutes, 13 seconds
Output 121/542: t=5780000.0 yr, dE/E0=3.94e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 12 hours, 36 minutes, 54 seconds
  Estimated time remaining to next output: 5 minutes, 13 seconds
Output 122/542: t=5790000.0 yr, dE/E0=3.91e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 12 hours, 32 minutes, 8 seconds
  Estimated time remaining to next output: 5 minutes, 13 seconds
Output 123/542: t=5800000.0 yr, dE/E0=3.98e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 12 hours, 26 minutes, 32 seconds
  Estimated time remaining to next output: 5 minutes, 13 seconds
Output 124/542: t=5810000.0 yr, dE/E0=4.01e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 12 hours, 21 minutes, 16 seconds
  Estimated time remaining to next output: 5 minutes, 13 seconds
Output 125/542: t=5820000.0 yr, dE/E0=4.11e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 12 hours, 16 minutes, 14 seconds
  Estimated time remaining to next output: 5 minutes, 13 seconds
Output 126/542: t=5830000.0 yr, dE/E0=4.01e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 12 hours, 10 minutes, 26 seconds
  Estimated time remaining to next output: 5 minutes, 13 seconds
Output 127/542: t=5840000.0 yr, dE/E0=4.01e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 12 hours, 6 minutes, 8 seconds
  Estimated time remaining to next output: 5 minutes, 13 seconds
Output 128/542: t=5850000.0 yr, dE/E0=3.91e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 12 hours, 33 seconds
  Estimated time remaining to next output: 5 minutes, 13 seconds
Output 129/542: t=5860000.0 yr, dE/E0=3.91e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 11 hours, 55 minutes, 29 seconds
  Estimated time remaining to next output: 5 minutes, 13 seconds
Output 130/542: t=5870000.0 yr, dE/E0=3.98e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 11 hours, 50 minutes, 12 seconds
  Estimated time remaining to next output: 5 minutes, 13 seconds
Output 131/542: t=5880000.0 yr, dE/E0=4.11e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 11 hours, 45 minutes, 29 seconds
  Estimated time remaining to next output: 5 minutes, 13 seconds
Output 132/542: t=5890000.0 yr, dE/E0=4.12e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 11 hours, 40 minutes, 42 seconds
  Estimated time remaining to next output: 5 minutes, 13 seconds
Output 133/542: t=5900000.0 yr, dE/E0=4.02e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 11 hours, 35 minutes, 3 seconds
  Estimated time remaining to next output: 5 minutes, 13 seconds
Output 134/542: t=5910000.0 yr, dE/E0=4.01e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 11 hours, 30 minutes, 15 seconds
  Estimated time remaining to next output: 5 minutes, 13 seconds
Output 135/542: t=5920000.0 yr, dE/E0=4.16e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 11 hours, 25 minutes, 40 seconds
  Estimated time remaining to next output: 5 minutes, 13 seconds
Output 136/542: t=5930000.0 yr, dE/E0=4.23e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 11 hours, 19 minutes, 15 seconds
  Estimated time remaining to next output: 5 minutes, 13 seconds
Output 137/542: t=5940000.0 yr, dE/E0=4.30e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 11 hours, 13 minutes, 43 seconds
  Estimated time remaining to next output: 5 minutes, 13 seconds
Output 138/542: t=5950000.0 yr, dE/E0=4.24e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 11 hours, 8 minutes, 27 seconds
  Estimated time remaining to next output: 5 minutes, 13 seconds
Output 139/542: t=5960000.0 yr, dE/E0=4.19e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 11 hours, 2 minutes, 27 seconds
  Estimated time remaining to next output: 5 minutes, 13 seconds
Output 140/542: t=5970000.0 yr, dE/E0=4.07e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 10 hours, 56 minutes, 11 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 141/542: t=5980000.0 yr, dE/E0=4.10e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 10 hours, 51 minutes, 44 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 142/542: t=5990000.0 yr, dE/E0=4.27e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 10 hours, 45 minutes, 18 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 143/542: t=6000000.0 yr, dE/E0=4.37e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 10 hours, 39 minutes, 55 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 144/542: t=6010000.0 yr, dE/E0=4.34e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 10 hours, 35 minutes
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 145/542: t=6020000.0 yr, dE/E0=4.27e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 10 hours, 29 minutes, 32 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 146/542: t=6030000.0 yr, dE/E0=4.24e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 10 hours, 25 minutes, 18 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 147/542: t=6040000.0 yr, dE/E0=4.17e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 10 hours, 19 minutes, 47 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 148/542: t=6050000.0 yr, dE/E0=4.31e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 10 hours, 14 minutes, 26 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 149/542: t=6060000.0 yr, dE/E0=4.35e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 10 hours, 9 minutes, 19 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 150/542: t=6070000.0 yr, dE/E0=4.30e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 10 hours, 3 minutes, 57 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 151/542: t=6080000.0 yr, dE/E0=4.31e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 9 hours, 58 minutes, 25 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 152/542: t=6090000.0 yr, dE/E0=4.26e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 9 hours, 52 minutes, 28 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 153/542: t=6100000.0 yr, dE/E0=4.38e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 9 hours, 46 minutes, 51 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 154/542: t=6110000.0 yr, dE/E0=4.41e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 9 hours, 41 minutes, 30 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 155/542: t=6120000.0 yr, dE/E0=4.47e-07, N=800
  Estimated time remaining to complete simulation: 1 days, 9 hours, 37 minutes, 19 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
A particle escaped (r>exit_max_distance).
Removing escaped particle at index 456
Remaining particles: 799
Output 156/542: t=6121570.0 yr, dE/E0=7.02e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 9 hours, 21 minutes, 16 seconds
  Estimated time remaining to next output: 5 minutes, 11 seconds
Output 157/542: t=6140000.0 yr, dE/E0=7.00e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 9 hours, 27 minutes, 9 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 158/542: t=6150000.0 yr, dE/E0=6.96e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 9 hours, 21 minutes, 19 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 159/542: t=6160000.0 yr, dE/E0=7.03e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 9 hours, 16 minutes, 6 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 160/542: t=6170000.0 yr, dE/E0=7.08e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 9 hours, 11 minutes, 2 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 161/542: t=6180000.0 yr, dE/E0=7.04e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 9 hours, 5 minutes, 56 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 162/542: t=6190000.0 yr, dE/E0=7.08e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 9 hours, 58 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 163/542: t=6200000.0 yr, dE/E0=7.03e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 8 hours, 55 minutes, 36 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 164/542: t=6210000.0 yr, dE/E0=6.93e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 8 hours, 50 minutes, 10 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 165/542: t=6220000.0 yr, dE/E0=6.93e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 8 hours, 45 minutes, 54 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 166/542: t=6230000.0 yr, dE/E0=7.05e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 8 hours, 40 minutes, 55 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 167/542: t=6240000.0 yr, dE/E0=7.14e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 8 hours, 35 minutes, 21 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 168/542: t=6250000.0 yr, dE/E0=7.13e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 8 hours, 30 minutes
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 169/542: t=6260000.0 yr, dE/E0=7.09e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 8 hours, 24 minutes, 55 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 170/542: t=6270000.0 yr, dE/E0=7.02e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 8 hours, 19 minutes, 59 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 171/542: t=6280000.0 yr, dE/E0=7.05e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 8 hours, 14 minutes, 40 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 172/542: t=6290000.0 yr, dE/E0=7.18e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 8 hours, 9 minutes, 14 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 173/542: t=6300000.0 yr, dE/E0=7.19e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 8 hours, 3 minutes, 51 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 174/542: t=6310000.0 yr, dE/E0=7.14e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 7 hours, 58 minutes, 50 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 175/542: t=6320000.0 yr, dE/E0=7.01e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 7 hours, 53 minutes, 45 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 176/542: t=6330000.0 yr, dE/E0=6.92e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 7 hours, 48 minutes, 10 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 177/542: t=6340000.0 yr, dE/E0=7.01e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 7 hours, 43 minutes, 23 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 178/542: t=6350000.0 yr, dE/E0=7.08e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 7 hours, 37 minutes, 56 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 179/542: t=6360000.0 yr, dE/E0=7.14e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 7 hours, 32 minutes, 44 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 180/542: t=6370000.0 yr, dE/E0=7.22e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 7 hours, 27 minutes, 10 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 181/542: t=6380000.0 yr, dE/E0=7.21e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 7 hours, 22 minutes, 28 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 182/542: t=6390000.0 yr, dE/E0=7.04e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 7 hours, 16 minutes, 32 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 183/542: t=6400000.0 yr, dE/E0=7.05e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 7 hours, 10 minutes, 50 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 184/542: t=6410000.0 yr, dE/E0=7.01e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 7 hours, 5 minutes, 8 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 185/542: t=6420000.0 yr, dE/E0=7.15e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 6 hours, 59 minutes, 56 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 186/542: t=6430000.0 yr, dE/E0=7.13e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 6 hours, 54 minutes, 39 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 187/542: t=6440000.0 yr, dE/E0=7.10e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 6 hours, 49 minutes, 46 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 188/542: t=6450000.0 yr, dE/E0=7.04e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 6 hours, 44 minutes, 40 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 189/542: t=6460000.0 yr, dE/E0=7.02e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 6 hours, 39 minutes, 18 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 190/542: t=6470000.0 yr, dE/E0=7.02e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 6 hours, 34 minutes, 38 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 191/542: t=6480000.0 yr, dE/E0=7.19e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 6 hours, 29 minutes, 19 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 192/542: t=6490000.0 yr, dE/E0=7.24e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 6 hours, 23 minutes, 37 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 193/542: t=6500000.0 yr, dE/E0=7.04e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 6 hours, 18 minutes, 8 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 194/542: t=6510000.0 yr, dE/E0=7.05e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 6 hours, 12 minutes, 56 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 195/542: t=6520000.0 yr, dE/E0=6.99e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 6 hours, 7 minutes, 13 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 196/542: t=6530000.0 yr, dE/E0=7.03e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 6 hours, 1 minutes, 51 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 197/542: t=6540000.0 yr, dE/E0=7.10e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 5 hours, 56 minutes, 45 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 198/542: t=6550000.0 yr, dE/E0=7.04e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 5 hours, 51 minutes, 38 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 199/542: t=6560000.0 yr, dE/E0=7.02e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 5 hours, 46 minutes, 34 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 200/542: t=6570000.0 yr, dE/E0=6.91e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 5 hours, 40 minutes, 40 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 201/542: t=6580000.0 yr, dE/E0=6.84e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 5 hours, 35 minutes, 32 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 202/542: t=6590000.0 yr, dE/E0=6.88e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 5 hours, 31 minutes, 5 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 203/542: t=6600000.0 yr, dE/E0=6.99e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 5 hours, 25 minutes, 52 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 204/542: t=6610000.0 yr, dE/E0=7.00e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 5 hours, 20 minutes, 44 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 205/542: t=6620000.0 yr, dE/E0=6.92e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 5 hours, 15 minutes, 32 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 206/542: t=6630000.0 yr, dE/E0=6.83e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 5 hours, 10 minutes, 29 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 207/542: t=6640000.0 yr, dE/E0=6.89e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 5 hours, 5 minutes, 50 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 208/542: t=6650000.0 yr, dE/E0=6.91e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 5 hours, 34 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 209/542: t=6660000.0 yr, dE/E0=7.05e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 4 hours, 55 minutes, 33 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 210/542: t=6670000.0 yr, dE/E0=7.04e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 4 hours, 50 minutes, 25 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 211/542: t=6680000.0 yr, dE/E0=6.90e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 4 hours, 44 minutes, 56 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 212/542: t=6690000.0 yr, dE/E0=6.83e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 4 hours, 39 minutes, 46 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 213/542: t=6700000.0 yr, dE/E0=6.84e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 4 hours, 34 minutes, 36 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 214/542: t=6710000.0 yr, dE/E0=6.92e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 4 hours, 29 minutes, 43 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 215/542: t=6720000.0 yr, dE/E0=7.04e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 4 hours, 24 minutes, 20 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 216/542: t=6730000.0 yr, dE/E0=7.07e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 4 hours, 19 minutes
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 217/542: t=6740000.0 yr, dE/E0=6.91e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 4 hours, 13 minutes, 25 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 218/542: t=6750000.0 yr, dE/E0=6.88e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 4 hours, 8 minutes, 7 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 219/542: t=6760000.0 yr, dE/E0=6.94e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 4 hours, 3 minutes, 16 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 220/542: t=6770000.0 yr, dE/E0=7.05e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 3 hours, 58 minutes, 41 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 221/542: t=6780000.0 yr, dE/E0=7.06e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 3 hours, 54 minutes, 1 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 222/542: t=6790000.0 yr, dE/E0=7.00e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 3 hours, 48 minutes, 33 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 223/542: t=6800000.0 yr, dE/E0=6.95e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 3 hours, 43 minutes, 51 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 224/542: t=6810000.0 yr, dE/E0=6.87e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 3 hours, 38 minutes, 30 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 225/542: t=6820000.0 yr, dE/E0=6.81e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 3 hours, 33 minutes, 23 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 226/542: t=6830000.0 yr, dE/E0=6.98e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 3 hours, 28 minutes, 6 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 227/542: t=6840000.0 yr, dE/E0=6.99e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 3 hours, 22 minutes, 45 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 228/542: t=6850000.0 yr, dE/E0=6.96e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 3 hours, 17 minutes, 33 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 229/542: t=6860000.0 yr, dE/E0=6.87e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 3 hours, 12 minutes, 51 seconds
  Estimated time remaining to next output: 5 minutes, 13 seconds
Output 230/542: t=6870000.0 yr, dE/E0=6.82e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 3 hours, 7 minutes, 51 seconds
  Estimated time remaining to next output: 5 minutes, 13 seconds
Output 231/542: t=6880000.0 yr, dE/E0=6.80e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 3 hours, 2 minutes, 29 seconds
  Estimated time remaining to next output: 5 minutes, 13 seconds
Output 232/542: t=6890000.0 yr, dE/E0=6.87e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 2 hours, 57 minutes, 36 seconds
  Estimated time remaining to next output: 5 minutes, 13 seconds
Output 233/542: t=6900000.0 yr, dE/E0=6.91e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 2 hours, 52 minutes, 11 seconds
  Estimated time remaining to next output: 5 minutes, 13 seconds
Output 234/542: t=6910000.0 yr, dE/E0=7.01e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 2 hours, 46 minutes, 43 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 235/542: t=6920000.0 yr, dE/E0=6.87e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 2 hours, 41 minutes, 40 seconds
  Estimated time remaining to next output: 5 minutes, 13 seconds
Output 236/542: t=6930000.0 yr, dE/E0=6.74e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 2 hours, 36 minutes, 48 seconds
  Estimated time remaining to next output: 5 minutes, 13 seconds
Output 237/542: t=6940000.0 yr, dE/E0=6.77e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 2 hours, 31 minutes, 19 seconds
  Estimated time remaining to next output: 5 minutes, 13 seconds
Output 238/542: t=6950000.0 yr, dE/E0=6.94e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 2 hours, 26 minutes, 24 seconds
  Estimated time remaining to next output: 5 minutes, 13 seconds
Output 239/542: t=6960000.0 yr, dE/E0=6.93e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 2 hours, 20 minutes, 51 seconds
  Estimated time remaining to next output: 5 minutes, 13 seconds
Output 240/542: t=6970000.0 yr, dE/E0=6.94e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 2 hours, 15 minutes, 25 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 241/542: t=6980000.0 yr, dE/E0=6.85e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 2 hours, 10 minutes, 12 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 242/542: t=6990000.0 yr, dE/E0=6.70e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 2 hours, 4 minutes, 46 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 243/542: t=7000000.0 yr, dE/E0=6.74e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 1 hours, 59 minutes, 54 seconds
  Estimated time remaining to next output: 5 minutes, 13 seconds
Output 244/542: t=7010000.0 yr, dE/E0=6.89e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 1 hours, 54 minutes, 40 seconds
  Estimated time remaining to next output: 5 minutes, 13 seconds
Output 245/542: t=7020000.0 yr, dE/E0=6.87e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 1 hours, 49 minutes, 3 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 246/542: t=7030000.0 yr, dE/E0=6.85e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 1 hours, 43 minutes, 47 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 247/542: t=7040000.0 yr, dE/E0=6.82e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 1 hours, 38 minutes, 42 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 248/542: t=7050000.0 yr, dE/E0=6.74e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 1 hours, 33 minutes, 28 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 249/542: t=7060000.0 yr, dE/E0=6.76e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 1 hours, 28 minutes, 27 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 250/542: t=7070000.0 yr, dE/E0=6.80e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 1 hours, 23 minutes, 20 seconds
  Estimated time remaining to next output: 5 minutes, 13 seconds
Output 251/542: t=7080000.0 yr, dE/E0=6.90e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 1 hours, 18 minutes, 20 seconds
  Estimated time remaining to next output: 5 minutes, 13 seconds
Output 252/542: t=7090000.0 yr, dE/E0=6.91e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 1 hours, 13 minutes, 23 seconds
  Estimated time remaining to next output: 5 minutes, 13 seconds
Output 253/542: t=7100000.0 yr, dE/E0=6.77e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 1 hours, 8 minutes, 28 seconds
  Estimated time remaining to next output: 5 minutes, 13 seconds
Output 254/542: t=7110000.0 yr, dE/E0=6.76e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 1 hours, 3 minutes, 37 seconds
  Estimated time remaining to next output: 5 minutes, 13 seconds
Output 255/542: t=7120000.0 yr, dE/E0=6.70e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 58 minutes, 41 seconds
  Estimated time remaining to next output: 5 minutes, 13 seconds
Output 256/542: t=7130000.0 yr, dE/E0=6.75e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 53 minutes, 22 seconds
  Estimated time remaining to next output: 5 minutes, 13 seconds
Output 257/542: t=7140000.0 yr, dE/E0=6.79e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 47 minutes, 51 seconds
  Estimated time remaining to next output: 5 minutes, 13 seconds
Output 258/542: t=7150000.0 yr, dE/E0=6.90e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 42 minutes, 40 seconds
  Estimated time remaining to next output: 5 minutes, 13 seconds
Output 259/542: t=7160000.0 yr, dE/E0=6.72e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 37 minutes, 24 seconds
  Estimated time remaining to next output: 5 minutes, 13 seconds
Output 260/542: t=7170000.0 yr, dE/E0=6.79e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 32 minutes, 6 seconds
  Estimated time remaining to next output: 5 minutes, 13 seconds
Output 261/542: t=7180000.0 yr, dE/E0=6.77e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 26 minutes, 52 seconds
  Estimated time remaining to next output: 5 minutes, 13 seconds
Output 262/542: t=7190000.0 yr, dE/E0=6.83e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 21 minutes, 51 seconds
  Estimated time remaining to next output: 5 minutes, 13 seconds
Output 263/542: t=7200000.0 yr, dE/E0=6.86e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 17 minutes, 5 seconds
  Estimated time remaining to next output: 5 minutes, 13 seconds
Output 264/542: t=7210000.0 yr, dE/E0=6.97e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 12 minutes, 4 seconds
  Estimated time remaining to next output: 5 minutes, 13 seconds
Output 265/542: t=7220000.0 yr, dE/E0=6.91e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 6 minutes, 58 seconds
  Estimated time remaining to next output: 5 minutes, 13 seconds
Output 266/542: t=7230000.0 yr, dE/E0=6.72e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 1 minutes, 49 seconds
  Estimated time remaining to next output: 5 minutes, 13 seconds
Output 267/542: t=7240000.0 yr, dE/E0=6.76e-07, N=799
  Estimated time remaining to complete simulation: 23 hours, 56 minutes, 25 seconds
  Estimated time remaining to next output: 5 minutes, 13 seconds
Output 268/542: t=7250000.0 yr, dE/E0=6.71e-07, N=799
  Estimated time remaining to complete simulation: 23 hours, 51 minutes, 18 seconds
  Estimated time remaining to next output: 5 minutes, 13 seconds
Output 269/542: t=7260000.0 yr, dE/E0=6.82e-07, N=799
  Estimated time remaining to complete simulation: 23 hours, 46 minutes, 13 seconds
  Estimated time remaining to next output: 5 minutes, 13 seconds
Output 270/542: t=7270000.0 yr, dE/E0=6.83e-07, N=799
  Estimated time remaining to complete simulation: 23 hours, 41 minutes, 5 seconds
  Estimated time remaining to next output: 5 minutes, 13 seconds
Output 271/542: t=7280000.0 yr, dE/E0=6.75e-07, N=799
  Estimated time remaining to complete simulation: 23 hours, 35 minutes, 48 seconds
  Estimated time remaining to next output: 5 minutes, 13 seconds
Output 272/542: t=7290000.0 yr, dE/E0=6.69e-07, N=799
  Estimated time remaining to complete simulation: 23 hours, 32 minutes, 44 seconds
  Estimated time remaining to next output: 5 minutes, 13 seconds
Output 273/542: t=7300000.0 yr, dE/E0=6.60e-07, N=799
  Estimated time remaining to complete simulation: 23 hours, 27 minutes, 16 seconds
  Estimated time remaining to next output: 5 minutes, 13 seconds
Output 274/542: t=7310000.0 yr, dE/E0=6.67e-07, N=799
  Estimated time remaining to complete simulation: 23 hours, 22 minutes, 12 seconds
  Estimated time remaining to next output: 5 minutes, 13 seconds
Output 275/542: t=7320000.0 yr, dE/E0=6.75e-07, N=799
  Estimated time remaining to complete simulation: 23 hours, 17 minutes, 18 seconds
  Estimated time remaining to next output: 5 minutes, 14 seconds
Output 276/542: t=7330000.0 yr, dE/E0=6.86e-07, N=799
  Estimated time remaining to complete simulation: 23 hours, 11 minutes, 51 seconds
  Estimated time remaining to next output: 5 minutes, 13 seconds
Output 277/542: t=7340000.0 yr, dE/E0=6.74e-07, N=799
  Estimated time remaining to complete simulation: 23 hours, 7 minutes, 52 seconds
  Estimated time remaining to next output: 5 minutes, 14 seconds
Output 278/542: t=7350000.0 yr, dE/E0=6.74e-07, N=799
  Estimated time remaining to complete simulation: 23 hours, 4 minutes, 50 seconds
  Estimated time remaining to next output: 5 minutes, 14 seconds
Output 279/542: t=7360000.0 yr, dE/E0=6.59e-07, N=799
  Estimated time remaining to complete simulation: 23 hours, 21 seconds
  Estimated time remaining to next output: 5 minutes, 14 seconds
Output 280/542: t=7370000.0 yr, dE/E0=6.71e-07, N=799
  Estimated time remaining to complete simulation: 22 hours, 55 minutes, 13 seconds
  Estimated time remaining to next output: 5 minutes, 14 seconds
Output 281/542: t=7380000.0 yr, dE/E0=6.82e-07, N=799
  Estimated time remaining to complete simulation: 22 hours, 50 minutes, 7 seconds
  Estimated time remaining to next output: 5 minutes, 14 seconds
Output 282/542: t=7390000.0 yr, dE/E0=6.81e-07, N=799
  Estimated time remaining to complete simulation: 22 hours, 45 minutes, 5 seconds
  Estimated time remaining to next output: 5 minutes, 15 seconds
Output 283/542: t=7400000.0 yr, dE/E0=6.86e-07, N=799
  Estimated time remaining to complete simulation: 22 hours, 39 minutes, 35 seconds
  Estimated time remaining to next output: 5 minutes, 14 seconds
Output 284/542: t=7410000.0 yr, dE/E0=6.79e-07, N=799
  Estimated time remaining to complete simulation: 22 hours, 34 minutes, 47 seconds
  Estimated time remaining to next output: 5 minutes, 15 seconds
Output 285/542: t=7420000.0 yr, dE/E0=6.74e-07, N=799
  Estimated time remaining to complete simulation: 22 hours, 30 minutes, 30 seconds
  Estimated time remaining to next output: 5 minutes, 15 seconds
Output 286/542: t=7430000.0 yr, dE/E0=6.84e-07, N=799
  Estimated time remaining to complete simulation: 22 hours, 26 minutes, 39 seconds
  Estimated time remaining to next output: 5 minutes, 15 seconds
Output 287/542: t=7440000.0 yr, dE/E0=6.88e-07, N=799
  Estimated time remaining to complete simulation: 22 hours, 22 minutes, 12 seconds
  Estimated time remaining to next output: 5 minutes, 15 seconds
Output 288/542: t=7450000.0 yr, dE/E0=6.93e-07, N=799
  Estimated time remaining to complete simulation: 22 hours, 17 minutes, 31 seconds
  Estimated time remaining to next output: 5 minutes, 15 seconds
Output 289/542: t=7460000.0 yr, dE/E0=6.88e-07, N=799
  Estimated time remaining to complete simulation: 22 hours, 12 minutes, 15 seconds
  Estimated time remaining to next output: 5 minutes, 15 seconds
Output 290/542: t=7470000.0 yr, dE/E0=6.69e-07, N=799
  Estimated time remaining to complete simulation: 22 hours, 6 minutes, 50 seconds
  Estimated time remaining to next output: 5 minutes, 15 seconds
Output 291/542: t=7480000.0 yr, dE/E0=6.72e-07, N=799
  Estimated time remaining to complete simulation: 22 hours, 3 minutes, 27 seconds
  Estimated time remaining to next output: 5 minutes, 16 seconds
Output 292/542: t=7490000.0 yr, dE/E0=6.71e-07, N=799
  Estimated time remaining to complete simulation: 22 hours, 35 seconds
  Estimated time remaining to next output: 5 minutes, 16 seconds
Output 293/542: t=7500000.0 yr, dE/E0=6.78e-07, N=799
  Estimated time remaining to complete simulation: 21 hours, 56 minutes, 28 seconds
  Estimated time remaining to next output: 5 minutes, 17 seconds
Output 294/542: t=7510000.0 yr, dE/E0=6.75e-07, N=799
  Estimated time remaining to complete simulation: 21 hours, 54 minutes, 1 seconds
  Estimated time remaining to next output: 5 minutes, 17 seconds
Output 295/542: t=7520000.0 yr, dE/E0=6.80e-07, N=799
  Estimated time remaining to complete simulation: 21 hours, 51 minutes, 9 seconds
  Estimated time remaining to next output: 5 minutes, 18 seconds
Output 296/542: t=7530000.0 yr, dE/E0=6.61e-07, N=799
  Estimated time remaining to complete simulation: 21 hours, 45 minutes, 57 seconds
  Estimated time remaining to next output: 5 minutes, 18 seconds
Output 297/542: t=7540000.0 yr, dE/E0=6.68e-07, N=799
  Estimated time remaining to complete simulation: 21 hours, 40 minutes, 43 seconds
  Estimated time remaining to next output: 5 minutes, 18 seconds
Output 298/542: t=7550000.0 yr, dE/E0=6.66e-07, N=799
  Estimated time remaining to complete simulation: 21 hours, 36 minutes, 8 seconds
  Estimated time remaining to next output: 5 minutes, 18 seconds
Output 299/542: t=7560000.0 yr, dE/E0=6.82e-07, N=799
  Estimated time remaining to complete simulation: 21 hours, 32 minutes, 44 seconds
  Estimated time remaining to next output: 5 minutes, 19 seconds
Output 300/542: t=7570000.0 yr, dE/E0=6.85e-07, N=799
  Estimated time remaining to complete simulation: 21 hours, 27 minutes, 23 seconds
  Estimated time remaining to next output: 5 minutes, 19 seconds
Output 301/542: t=7580000.0 yr, dE/E0=6.82e-07, N=799
  Estimated time remaining to complete simulation: 21 hours, 23 minutes, 37 seconds
  Estimated time remaining to next output: 5 minutes, 19 seconds
Output 302/542: t=7590000.0 yr, dE/E0=6.71e-07, N=799
  Estimated time remaining to complete simulation: 21 hours, 19 minutes, 52 seconds
  Estimated time remaining to next output: 5 minutes, 19 seconds
Output 303/542: t=7600000.0 yr, dE/E0=6.66e-07, N=799
  Estimated time remaining to complete simulation: 21 hours, 14 minutes, 28 seconds
  Estimated time remaining to next output: 5 minutes, 19 seconds
Output 304/542: t=7610000.0 yr, dE/E0=6.72e-07, N=799
  Estimated time remaining to complete simulation: 21 hours, 9 minutes, 9 seconds
  Estimated time remaining to next output: 5 minutes, 19 seconds
Output 305/542: t=7620000.0 yr, dE/E0=6.81e-07, N=799
  Estimated time remaining to complete simulation: 21 hours, 3 minutes, 40 seconds
  Estimated time remaining to next output: 5 minutes, 19 seconds
Output 306/542: t=7630000.0 yr, dE/E0=6.83e-07, N=799
  Estimated time remaining to complete simulation: 20 hours, 58 minutes, 20 seconds
  Estimated time remaining to next output: 5 minutes, 19 seconds
Output 307/542: t=7640000.0 yr, dE/E0=6.75e-07, N=799
  Estimated time remaining to complete simulation: 20 hours, 52 minutes, 54 seconds
  Estimated time remaining to next output: 5 minutes, 19 seconds
Output 308/542: t=7650000.0 yr, dE/E0=6.72e-07, N=799
  Estimated time remaining to complete simulation: 20 hours, 47 minutes, 24 seconds
  Estimated time remaining to next output: 5 minutes, 19 seconds
Output 309/542: t=7660000.0 yr, dE/E0=6.62e-07, N=799
  Estimated time remaining to complete simulation: 20 hours, 42 minutes, 10 seconds
  Estimated time remaining to next output: 5 minutes, 19 seconds
Output 310/542: t=7670000.0 yr, dE/E0=6.76e-07, N=799
  Estimated time remaining to complete simulation: 20 hours, 36 minutes, 46 seconds
  Estimated time remaining to next output: 5 minutes, 19 seconds
Output 311/542: t=7680000.0 yr, dE/E0=6.88e-07, N=799
  Estimated time remaining to complete simulation: 20 hours, 31 minutes, 20 seconds
  Estimated time remaining to next output: 5 minutes, 19 seconds
Output 312/542: t=7690000.0 yr, dE/E0=6.71e-07, N=799
  Estimated time remaining to complete simulation: 20 hours, 28 minutes, 8 seconds
  Estimated time remaining to next output: 5 minutes, 20 seconds
Output 313/542: t=7700000.0 yr, dE/E0=6.74e-07, N=799
  Estimated time remaining to complete simulation: 20 hours, 25 minutes, 18 seconds
  Estimated time remaining to next output: 5 minutes, 21 seconds
Output 314/542: t=7710000.0 yr, dE/E0=6.62e-07, N=799
  Estimated time remaining to complete simulation: 20 hours, 22 minutes, 5 seconds
  Estimated time remaining to next output: 5 minutes, 21 seconds
Output 315/542: t=7720000.0 yr, dE/E0=6.51e-07, N=799
  Estimated time remaining to complete simulation: 20 hours, 19 minutes, 17 seconds
  Estimated time remaining to next output: 5 minutes, 22 seconds
Output 316/542: t=7730000.0 yr, dE/E0=6.62e-07, N=799
  Estimated time remaining to complete simulation: 20 hours, 16 minutes, 26 seconds
  Estimated time remaining to next output: 5 minutes, 22 seconds
Output 317/542: t=7740000.0 yr, dE/E0=6.68e-07, N=799
  Estimated time remaining to complete simulation: 20 hours, 12 minutes, 55 seconds
  Estimated time remaining to next output: 5 minutes, 23 seconds
Output 318/542: t=7750000.0 yr, dE/E0=6.75e-07, N=799
  Estimated time remaining to complete simulation: 20 hours, 9 minutes, 33 seconds
  Estimated time remaining to next output: 5 minutes, 23 seconds
Output 319/542: t=7760000.0 yr, dE/E0=6.67e-07, N=799
  Estimated time remaining to complete simulation: 20 hours, 5 minutes, 59 seconds
  Estimated time remaining to next output: 5 minutes, 24 seconds
Output 320/542: t=7770000.0 yr, dE/E0=6.63e-07, N=799
  Estimated time remaining to complete simulation: 20 hours, 2 minutes, 40 seconds
  Estimated time remaining to next output: 5 minutes, 25 seconds
Output 321/542: t=7780000.0 yr, dE/E0=6.53e-07, N=799
  Estimated time remaining to complete simulation: 19 hours, 59 minutes, 20 seconds
  Estimated time remaining to next output: 5 minutes, 25 seconds
Output 322/542: t=7790000.0 yr, dE/E0=6.55e-07, N=799
  Estimated time remaining to complete simulation: 19 hours, 56 minutes, 15 seconds
  Estimated time remaining to next output: 5 minutes, 26 seconds
Output 323/542: t=7800000.0 yr, dE/E0=6.62e-07, N=799
  Estimated time remaining to complete simulation: 19 hours, 52 minutes, 55 seconds
  Estimated time remaining to next output: 5 minutes, 26 seconds
Output 324/542: t=7810000.0 yr, dE/E0=6.71e-07, N=799
  Estimated time remaining to complete simulation: 19 hours, 49 minutes, 41 seconds
  Estimated time remaining to next output: 5 minutes, 27 seconds
Output 325/542: t=7820000.0 yr, dE/E0=6.71e-07, N=799
  Estimated time remaining to complete simulation: 19 hours, 45 minutes, 54 seconds
  Estimated time remaining to next output: 5 minutes, 27 seconds
Output 326/542: t=7830000.0 yr, dE/E0=6.58e-07, N=799
  Estimated time remaining to complete simulation: 19 hours, 42 minutes, 25 seconds
  Estimated time remaining to next output: 5 minutes, 28 seconds
Output 327/542: t=7840000.0 yr, dE/E0=6.60e-07, N=799
  Estimated time remaining to complete simulation: 19 hours, 38 minutes, 55 seconds
  Estimated time remaining to next output: 5 minutes, 29 seconds
Output 328/542: t=7850000.0 yr, dE/E0=6.60e-07, N=799
  Estimated time remaining to complete simulation: 19 hours, 35 minutes, 35 seconds
  Estimated time remaining to next output: 5 minutes, 29 seconds
Output 329/542: t=7860000.0 yr, dE/E0=6.62e-07, N=799
  Estimated time remaining to complete simulation: 19 hours, 32 minutes, 20 seconds
  Estimated time remaining to next output: 5 minutes, 30 seconds
Output 330/542: t=7870000.0 yr, dE/E0=6.78e-07, N=799
  Estimated time remaining to complete simulation: 19 hours, 26 minutes, 55 seconds
  Estimated time remaining to next output: 5 minutes, 30 seconds
Output 331/542: t=7880000.0 yr, dE/E0=6.62e-07, N=799
  Estimated time remaining to complete simulation: 19 hours, 21 minutes, 21 seconds
  Estimated time remaining to next output: 5 minutes, 30 seconds
Output 332/542: t=7890000.0 yr, dE/E0=6.69e-07, N=799
  Estimated time remaining to complete simulation: 19 hours, 15 minutes, 45 seconds
  Estimated time remaining to next output: 5 minutes, 30 seconds
Output 333/542: t=7900000.0 yr, dE/E0=6.63e-07, N=799
  Estimated time remaining to complete simulation: 19 hours, 10 minutes, 8 seconds
  Estimated time remaining to next output: 5 minutes, 30 seconds
Output 334/542: t=7910000.0 yr, dE/E0=6.65e-07, N=799
  Estimated time remaining to complete simulation: 19 hours, 4 minutes, 37 seconds
  Estimated time remaining to next output: 5 minutes, 30 seconds
Output 335/542: t=7920000.0 yr, dE/E0=6.68e-07, N=799
  Estimated time remaining to complete simulation: 18 hours, 59 minutes, 3 seconds
  Estimated time remaining to next output: 5 minutes, 30 seconds
Output 336/542: t=7930000.0 yr, dE/E0=6.84e-07, N=799
  Estimated time remaining to complete simulation: 18 hours, 53 minutes, 21 seconds
  Estimated time remaining to next output: 5 minutes, 30 seconds
Output 337/542: t=7940000.0 yr, dE/E0=6.79e-07, N=799
  Estimated time remaining to complete simulation: 18 hours, 47 minutes, 42 seconds
  Estimated time remaining to next output: 5 minutes, 30 seconds
Output 338/542: t=7950000.0 yr, dE/E0=6.67e-07, N=799
  Estimated time remaining to complete simulation: 18 hours, 42 minutes, 8 seconds
  Estimated time remaining to next output: 5 minutes, 30 seconds
Output 339/542: t=7960000.0 yr, dE/E0=6.57e-07, N=799
  Estimated time remaining to complete simulation: 18 hours, 36 minutes, 28 seconds
  Estimated time remaining to next output: 5 minutes, 29 seconds
Output 340/542: t=7970000.0 yr, dE/E0=6.68e-07, N=799
  Estimated time remaining to complete simulation: 18 hours, 30 minutes, 47 seconds
  Estimated time remaining to next output: 5 minutes, 29 seconds
Output 341/542: t=7980000.0 yr, dE/E0=6.78e-07, N=799
  Estimated time remaining to complete simulation: 18 hours, 25 minutes, 9 seconds
  Estimated time remaining to next output: 5 minutes, 29 seconds
Output 342/542: t=7990000.0 yr, dE/E0=6.74e-07, N=799
  Estimated time remaining to complete simulation: 18 hours, 19 minutes, 35 seconds
  Estimated time remaining to next output: 5 minutes, 29 seconds
Output 343/542: t=8000000.0 yr, dE/E0=6.73e-07, N=799
  Estimated time remaining to complete simulation: 18 hours, 14 minutes, 1 seconds
  Estimated time remaining to next output: 5 minutes, 29 seconds
Output 344/542: t=8010000.0 yr, dE/E0=6.71e-07, N=799
  Estimated time remaining to complete simulation: 18 hours, 8 minutes, 24 seconds
  Estimated time remaining to next output: 5 minutes, 29 seconds
Output 345/542: t=8020000.0 yr, dE/E0=6.62e-07, N=799
  Estimated time remaining to complete simulation: 18 hours, 2 minutes, 56 seconds
  Estimated time remaining to next output: 5 minutes, 29 seconds
Output 346/542: t=8030000.0 yr, dE/E0=6.75e-07, N=799
  Estimated time remaining to complete simulation: 17 hours, 57 minutes, 14 seconds
  Estimated time remaining to next output: 5 minutes, 29 seconds
Output 347/542: t=8040000.0 yr, dE/E0=6.70e-07, N=799
  Estimated time remaining to complete simulation: 17 hours, 51 minutes, 40 seconds
  Estimated time remaining to next output: 5 minutes, 29 seconds
Output 348/542: t=8050000.0 yr, dE/E0=6.81e-07, N=799
  Estimated time remaining to complete simulation: 17 hours, 46 minutes, 1 seconds
  Estimated time remaining to next output: 5 minutes, 29 seconds
Output 349/542: t=8060000.0 yr, dE/E0=6.76e-07, N=799
  Estimated time remaining to complete simulation: 17 hours, 40 minutes, 34 seconds
  Estimated time remaining to next output: 5 minutes, 29 seconds
Output 350/542: t=8070000.0 yr, dE/E0=6.63e-07, N=799
  Estimated time remaining to complete simulation: 17 hours, 35 minutes, 4 seconds
  Estimated time remaining to next output: 5 minutes, 29 seconds
Output 351/542: t=8080000.0 yr, dE/E0=6.70e-07, N=799
  Estimated time remaining to complete simulation: 17 hours, 29 minutes, 22 seconds
  Estimated time remaining to next output: 5 minutes, 29 seconds
Output 352/542: t=8090000.0 yr, dE/E0=6.65e-07, N=799
  Estimated time remaining to complete simulation: 17 hours, 23 minutes, 51 seconds
  Estimated time remaining to next output: 5 minutes, 29 seconds
Output 353/542: t=8100000.0 yr, dE/E0=6.64e-07, N=799
  Estimated time remaining to complete simulation: 17 hours, 18 minutes, 11 seconds
  Estimated time remaining to next output: 5 minutes, 29 seconds
Output 354/542: t=8110000.0 yr, dE/E0=6.75e-07, N=799
  Estimated time remaining to complete simulation: 17 hours, 12 minutes, 47 seconds
  Estimated time remaining to next output: 5 minutes, 29 seconds
Output 355/542: t=8120000.0 yr, dE/E0=6.69e-07, N=799
  Estimated time remaining to complete simulation: 17 hours, 7 minutes, 15 seconds
  Estimated time remaining to next output: 5 minutes, 29 seconds
Output 356/542: t=8130000.0 yr, dE/E0=6.66e-07, N=799
  Estimated time remaining to complete simulation: 17 hours, 1 minutes, 43 seconds
  Estimated time remaining to next output: 5 minutes, 29 seconds
Output 357/542: t=8140000.0 yr, dE/E0=6.72e-07, N=799
  Estimated time remaining to complete simulation: 16 hours, 56 minutes, 7 seconds
  Estimated time remaining to next output: 5 minutes, 29 seconds
Output 358/542: t=8150000.0 yr, dE/E0=6.64e-07, N=799
  Estimated time remaining to complete simulation: 16 hours, 50 minutes, 30 seconds
  Estimated time remaining to next output: 5 minutes, 29 seconds
Output 359/542: t=8160000.0 yr, dE/E0=6.79e-07, N=799
  Estimated time remaining to complete simulation: 16 hours, 44 minutes, 57 seconds
  Estimated time remaining to next output: 5 minutes, 29 seconds
Output 360/542: t=8170000.0 yr, dE/E0=6.83e-07, N=799
  Estimated time remaining to complete simulation: 16 hours, 39 minutes, 18 seconds
  Estimated time remaining to next output: 5 minutes, 29 seconds
Output 361/542: t=8180000.0 yr, dE/E0=6.85e-07, N=799
  Estimated time remaining to complete simulation: 16 hours, 34 minutes, 6 seconds
  Estimated time remaining to next output: 5 minutes, 29 seconds
Output 362/542: t=8190000.0 yr, dE/E0=6.79e-07, N=799
  Estimated time remaining to complete simulation: 16 hours, 28 minutes, 37 seconds
  Estimated time remaining to next output: 5 minutes, 29 seconds
Output 363/542: t=8200000.0 yr, dE/E0=6.76e-07, N=799
  Estimated time remaining to complete simulation: 16 hours, 23 minutes
  Estimated time remaining to next output: 5 minutes, 29 seconds
Output 364/542: t=8210000.0 yr, dE/E0=6.75e-07, N=799
  Estimated time remaining to complete simulation: 16 hours, 17 minutes, 22 seconds
  Estimated time remaining to next output: 5 minutes, 29 seconds
Output 365/542: t=8220000.0 yr, dE/E0=6.84e-07, N=799
  Estimated time remaining to complete simulation: 16 hours, 11 minutes, 40 seconds
  Estimated time remaining to next output: 5 minutes, 29 seconds
Output 366/542: t=8230000.0 yr, dE/E0=6.94e-07, N=799
  Estimated time remaining to complete simulation: 16 hours, 6 minutes, 16 seconds
  Estimated time remaining to next output: 5 minutes, 29 seconds
Output 367/542: t=8240000.0 yr, dE/E0=6.96e-07, N=799
  Estimated time remaining to complete simulation: 16 hours, 35 seconds
  Estimated time remaining to next output: 5 minutes, 29 seconds
Output 368/542: t=8250000.0 yr, dE/E0=6.88e-07, N=799
  Estimated time remaining to complete simulation: 15 hours, 55 minutes, 5 seconds
  Estimated time remaining to next output: 5 minutes, 29 seconds
A particle escaped (r>exit_max_distance).
Removing escaped particle at index 645
Remaining particles: 798
Output 369/542: t=8256784.7 yr, dE/E0=8.93e-07, N=798
  Estimated time remaining to complete simulation: 15 hours, 48 minutes, 41 seconds
  Estimated time remaining to next output: 5 minutes, 29 seconds
Output 370/542: t=8270000.0 yr, dE/E0=8.84e-07, N=798
  Estimated time remaining to complete simulation: 15 hours, 43 minutes, 46 seconds
  Estimated time remaining to next output: 5 minutes, 29 seconds
Output 371/542: t=8280000.0 yr, dE/E0=8.84e-07, N=798
  Estimated time remaining to complete simulation: 15 hours, 38 minutes, 11 seconds
  Estimated time remaining to next output: 5 minutes, 29 seconds
Output 372/542: t=8290000.0 yr, dE/E0=9.08e-07, N=798
  Estimated time remaining to complete simulation: 15 hours, 32 minutes, 51 seconds
  Estimated time remaining to next output: 5 minutes, 29 seconds
Output 373/542: t=8300000.0 yr, dE/E0=9.03e-07, N=798
  Estimated time remaining to complete simulation: 15 hours, 27 minutes, 20 seconds
  Estimated time remaining to next output: 5 minutes, 29 seconds
Output 374/542: t=8310000.0 yr, dE/E0=8.85e-07, N=798
  Estimated time remaining to complete simulation: 15 hours, 21 minutes, 45 seconds
  Estimated time remaining to next output: 5 minutes, 29 seconds
Output 375/542: t=8320000.0 yr, dE/E0=8.84e-07, N=798
  Estimated time remaining to complete simulation: 15 hours, 16 minutes, 16 seconds
  Estimated time remaining to next output: 5 minutes, 29 seconds
Output 376/542: t=8330000.0 yr, dE/E0=8.89e-07, N=798
  Estimated time remaining to complete simulation: 15 hours, 10 minutes, 32 seconds
  Estimated time remaining to next output: 5 minutes, 29 seconds
Output 377/542: t=8340000.0 yr, dE/E0=8.96e-07, N=798
  Estimated time remaining to complete simulation: 15 hours, 4 minutes, 52 seconds
  Estimated time remaining to next output: 5 minutes, 29 seconds
Output 378/542: t=8350000.0 yr, dE/E0=8.94e-07, N=798
  Estimated time remaining to complete simulation: 14 hours, 59 minutes, 20 seconds
  Estimated time remaining to next output: 5 minutes, 29 seconds
Output 379/542: t=8360000.0 yr, dE/E0=9.04e-07, N=798
  Estimated time remaining to complete simulation: 14 hours, 53 minutes, 52 seconds
  Estimated time remaining to next output: 5 minutes, 29 seconds
Output 380/542: t=8370000.0 yr, dE/E0=8.99e-07, N=798
  Estimated time remaining to complete simulation: 14 hours, 48 minutes, 17 seconds
  Estimated time remaining to next output: 5 minutes, 28 seconds
Output 381/542: t=8380000.0 yr, dE/E0=8.90e-07, N=798
  Estimated time remaining to complete simulation: 14 hours, 42 minutes, 43 seconds
  Estimated time remaining to next output: 5 minutes, 28 seconds
Output 382/542: t=8390000.0 yr, dE/E0=8.92e-07, N=798
  Estimated time remaining to complete simulation: 14 hours, 37 minutes, 8 seconds
  Estimated time remaining to next output: 5 minutes, 28 seconds
Output 383/542: t=8400000.0 yr, dE/E0=8.92e-07, N=798
  Estimated time remaining to complete simulation: 14 hours, 31 minutes, 35 seconds
  Estimated time remaining to next output: 5 minutes, 28 seconds
Output 384/542: t=8410000.0 yr, dE/E0=9.02e-07, N=798
  Estimated time remaining to complete simulation: 14 hours, 25 minutes, 58 seconds
  Estimated time remaining to next output: 5 minutes, 28 seconds
Output 385/542: t=8420000.0 yr, dE/E0=9.07e-07, N=798
  Estimated time remaining to complete simulation: 14 hours, 20 minutes, 22 seconds
  Estimated time remaining to next output: 5 minutes, 28 seconds
Output 386/542: t=8430000.0 yr, dE/E0=8.95e-07, N=798
  Estimated time remaining to complete simulation: 14 hours, 14 minutes, 48 seconds
  Estimated time remaining to next output: 5 minutes, 28 seconds
Output 387/542: t=8440000.0 yr, dE/E0=8.91e-07, N=798
  Estimated time remaining to complete simulation: 14 hours, 9 minutes, 20 seconds
  Estimated time remaining to next output: 5 minutes, 28 seconds
Output 388/542: t=8450000.0 yr, dE/E0=8.88e-07, N=798
  Estimated time remaining to complete simulation: 14 hours, 3 minutes, 41 seconds
  Estimated time remaining to next output: 5 minutes, 28 seconds
Output 389/542: t=8460000.0 yr, dE/E0=9.00e-07, N=798
  Estimated time remaining to complete simulation: 13 hours, 58 minutes, 18 seconds
  Estimated time remaining to next output: 5 minutes, 28 seconds
Output 390/542: t=8470000.0 yr, dE/E0=9.19e-07, N=798
  Estimated time remaining to complete simulation: 13 hours, 52 minutes, 38 seconds
  Estimated time remaining to next output: 5 minutes, 28 seconds
Output 391/542: t=8480000.0 yr, dE/E0=9.15e-07, N=798
  Estimated time remaining to complete simulation: 13 hours, 47 minutes, 7 seconds
  Estimated time remaining to next output: 5 minutes, 28 seconds
Output 392/542: t=8490000.0 yr, dE/E0=9.11e-07, N=798
  Estimated time remaining to complete simulation: 13 hours, 41 minutes, 30 seconds
  Estimated time remaining to next output: 5 minutes, 28 seconds
Output 393/542: t=8500000.0 yr, dE/E0=9.04e-07, N=798
  Estimated time remaining to complete simulation: 13 hours, 36 minutes, 4 seconds
  Estimated time remaining to next output: 5 minutes, 28 seconds
Output 394/542: t=8510000.0 yr, dE/E0=9.00e-07, N=798
  Estimated time remaining to complete simulation: 13 hours, 30 minutes, 28 seconds
  Estimated time remaining to next output: 5 minutes, 28 seconds
Output 395/542: t=8520000.0 yr, dE/E0=8.97e-07, N=798
  Estimated time remaining to complete simulation: 13 hours, 24 minutes, 56 seconds
  Estimated time remaining to next output: 5 minutes, 28 seconds
Output 396/542: t=8530000.0 yr, dE/E0=9.09e-07, N=798
  Estimated time remaining to complete simulation: 13 hours, 19 minutes, 49 seconds
  Estimated time remaining to next output: 5 minutes, 28 seconds
Output 397/542: t=8540000.0 yr, dE/E0=9.02e-07, N=798
  Estimated time remaining to complete simulation: 13 hours, 15 minutes, 46 seconds
  Estimated time remaining to next output: 5 minutes, 29 seconds
Output 398/542: t=8550000.0 yr, dE/E0=9.07e-07, N=798
  Estimated time remaining to complete simulation: 13 hours, 11 minutes, 14 seconds
  Estimated time remaining to next output: 5 minutes, 29 seconds
Output 399/542: t=8560000.0 yr, dE/E0=9.06e-07, N=798
  Estimated time remaining to complete simulation: 13 hours, 7 minutes, 4 seconds
  Estimated time remaining to next output: 5 minutes, 30 seconds
Output 400/542: t=8570000.0 yr, dE/E0=8.94e-07, N=798
  Estimated time remaining to complete simulation: 13 hours, 2 minutes, 44 seconds
  Estimated time remaining to next output: 5 minutes, 30 seconds
Output 401/542: t=8580000.0 yr, dE/E0=8.98e-07, N=798
  Estimated time remaining to complete simulation: 12 hours, 58 minutes, 30 seconds
  Estimated time remaining to next output: 5 minutes, 31 seconds
Output 402/542: t=8590000.0 yr, dE/E0=9.13e-07, N=798
  Estimated time remaining to complete simulation: 12 hours, 53 minutes, 56 seconds
  Estimated time remaining to next output: 5 minutes, 31 seconds
Output 403/542: t=8600000.0 yr, dE/E0=9.13e-07, N=798
  Estimated time remaining to complete simulation: 12 hours, 49 minutes, 37 seconds
  Estimated time remaining to next output: 5 minutes, 32 seconds
Output 404/542: t=8610000.0 yr, dE/E0=9.06e-07, N=798
  Estimated time remaining to complete simulation: 12 hours, 45 minutes, 12 seconds
  Estimated time remaining to next output: 5 minutes, 32 seconds
Output 405/542: t=8620000.0 yr, dE/E0=9.05e-07, N=798
  Estimated time remaining to complete simulation: 12 hours, 40 minutes, 44 seconds
  Estimated time remaining to next output: 5 minutes, 33 seconds
Output 406/542: t=8630000.0 yr, dE/E0=9.07e-07, N=798
  Estimated time remaining to complete simulation: 12 hours, 36 minutes, 24 seconds
  Estimated time remaining to next output: 5 minutes, 33 seconds
Output 407/542: t=8640000.0 yr, dE/E0=9.06e-07, N=798
  Estimated time remaining to complete simulation: 12 hours, 31 minutes, 44 seconds
  Estimated time remaining to next output: 5 minutes, 34 seconds
Output 408/542: t=8650000.0 yr, dE/E0=9.21e-07, N=798
  Estimated time remaining to complete simulation: 12 hours, 27 minutes, 15 seconds
  Estimated time remaining to next output: 5 minutes, 34 seconds
Output 409/542: t=8660000.0 yr, dE/E0=9.22e-07, N=798
  Estimated time remaining to complete simulation: 12 hours, 22 minutes, 53 seconds
  Estimated time remaining to next output: 5 minutes, 35 seconds
Output 410/542: t=8670000.0 yr, dE/E0=9.17e-07, N=798
  Estimated time remaining to complete simulation: 12 hours, 18 minutes, 10 seconds
  Estimated time remaining to next output: 5 minutes, 35 seconds
Output 411/542: t=8680000.0 yr, dE/E0=9.00e-07, N=798
  Estimated time remaining to complete simulation: 12 hours, 13 minutes, 47 seconds
  Estimated time remaining to next output: 5 minutes, 36 seconds
Output 412/542: t=8690000.0 yr, dE/E0=8.98e-07, N=798
  Estimated time remaining to complete simulation: 12 hours, 9 minutes, 8 seconds
  Estimated time remaining to next output: 5 minutes, 36 seconds
Output 413/542: t=8700000.0 yr, dE/E0=8.98e-07, N=798
  Estimated time remaining to complete simulation: 12 hours, 4 minutes, 28 seconds
  Estimated time remaining to next output: 5 minutes, 36 seconds
Output 414/542: t=8710000.0 yr, dE/E0=9.14e-07, N=798
  Estimated time remaining to complete simulation: 11 hours, 59 minutes, 43 seconds
  Estimated time remaining to next output: 5 minutes, 37 seconds
Output 415/542: t=8720000.0 yr, dE/E0=9.12e-07, N=798
  Estimated time remaining to complete simulation: 11 hours, 55 minutes, 5 seconds
  Estimated time remaining to next output: 5 minutes, 37 seconds
Output 416/542: t=8730000.0 yr, dE/E0=9.20e-07, N=798
  Estimated time remaining to complete simulation: 11 hours, 50 minutes, 30 seconds
  Estimated time remaining to next output: 5 minutes, 38 seconds
Output 417/542: t=8740000.0 yr, dE/E0=9.10e-07, N=798
  Estimated time remaining to complete simulation: 11 hours, 45 minutes, 45 seconds
  Estimated time remaining to next output: 5 minutes, 38 seconds
Output 418/542: t=8750000.0 yr, dE/E0=9.11e-07, N=798
  Estimated time remaining to complete simulation: 11 hours, 40 minutes, 57 seconds
  Estimated time remaining to next output: 5 minutes, 39 seconds
Output 419/542: t=8760000.0 yr, dE/E0=9.16e-07, N=798
  Estimated time remaining to complete simulation: 11 hours, 36 minutes, 6 seconds
  Estimated time remaining to next output: 5 minutes, 39 seconds
Output 420/542: t=8770000.0 yr, dE/E0=9.25e-07, N=798
  Estimated time remaining to complete simulation: 11 hours, 31 minutes, 25 seconds
  Estimated time remaining to next output: 5 minutes, 40 seconds
Output 421/542: t=8780000.0 yr, dE/E0=9.30e-07, N=798
  Estimated time remaining to complete simulation: 11 hours, 26 minutes, 31 seconds
  Estimated time remaining to next output: 5 minutes, 40 seconds
Output 422/542: t=8790000.0 yr, dE/E0=9.34e-07, N=798
  Estimated time remaining to complete simulation: 11 hours, 21 minutes, 45 seconds
  Estimated time remaining to next output: 5 minutes, 40 seconds
Output 423/542: t=8800000.0 yr, dE/E0=9.28e-07, N=798
  Estimated time remaining to complete simulation: 11 hours, 16 minutes, 48 seconds
  Estimated time remaining to next output: 5 minutes, 41 seconds
Output 424/542: t=8810000.0 yr, dE/E0=9.26e-07, N=798
  Estimated time remaining to complete simulation: 11 hours, 12 minutes, 9 seconds
  Estimated time remaining to next output: 5 minutes, 41 seconds
Output 425/542: t=8820000.0 yr, dE/E0=9.30e-07, N=798
  Estimated time remaining to complete simulation: 11 hours, 7 minutes, 15 seconds
  Estimated time remaining to next output: 5 minutes, 42 seconds
Output 426/542: t=8830000.0 yr, dE/E0=9.36e-07, N=798
  Estimated time remaining to complete simulation: 11 hours, 2 minutes, 16 seconds
  Estimated time remaining to next output: 5 minutes, 42 seconds
Output 427/542: t=8840000.0 yr, dE/E0=9.39e-07, N=798
  Estimated time remaining to complete simulation: 10 hours, 57 minutes, 22 seconds
  Estimated time remaining to next output: 5 minutes, 42 seconds
Output 428/542: t=8850000.0 yr, dE/E0=9.40e-07, N=798
  Estimated time remaining to complete simulation: 10 hours, 52 minutes, 21 seconds
  Estimated time remaining to next output: 5 minutes, 43 seconds
Output 429/542: t=8860000.0 yr, dE/E0=9.32e-07, N=798
  Estimated time remaining to complete simulation: 10 hours, 47 minutes, 26 seconds
  Estimated time remaining to next output: 5 minutes, 43 seconds
Output 430/542: t=8870000.0 yr, dE/E0=9.31e-07, N=798
  Estimated time remaining to complete simulation: 10 hours, 42 minutes, 28 seconds
  Estimated time remaining to next output: 5 minutes, 44 seconds
Output 431/542: t=8880000.0 yr, dE/E0=9.35e-07, N=798
  Estimated time remaining to complete simulation: 10 hours, 37 minutes, 29 seconds
  Estimated time remaining to next output: 5 minutes, 44 seconds
Output 432/542: t=8890000.0 yr, dE/E0=9.45e-07, N=798
  Estimated time remaining to complete simulation: 10 hours, 32 minutes, 32 seconds
  Estimated time remaining to next output: 5 minutes, 45 seconds
Output 433/542: t=8900000.0 yr, dE/E0=9.57e-07, N=798
  Estimated time remaining to complete simulation: 10 hours, 27 minutes, 27 seconds
  Estimated time remaining to next output: 5 minutes, 45 seconds
Output 434/542: t=8910000.0 yr, dE/E0=9.45e-07, N=798
  Estimated time remaining to complete simulation: 10 hours, 22 minutes, 21 seconds
  Estimated time remaining to next output: 5 minutes, 45 seconds
Output 435/542: t=8920000.0 yr, dE/E0=9.38e-07, N=798
  Estimated time remaining to complete simulation: 10 hours, 17 minutes, 26 seconds
  Estimated time remaining to next output: 5 minutes, 46 seconds
Output 436/542: t=8930000.0 yr, dE/E0=9.46e-07, N=798
  Estimated time remaining to complete simulation: 10 hours, 12 minutes, 32 seconds
  Estimated time remaining to next output: 5 minutes, 46 seconds
Output 437/542: t=8940000.0 yr, dE/E0=9.48e-07, N=798
  Estimated time remaining to complete simulation: 10 hours, 7 minutes, 32 seconds
  Estimated time remaining to next output: 5 minutes, 47 seconds
Output 438/542: t=8950000.0 yr, dE/E0=9.49e-07, N=798
  Estimated time remaining to complete simulation: 10 hours, 2 minutes, 28 seconds
  Estimated time remaining to next output: 5 minutes, 47 seconds
Output 439/542: t=8960000.0 yr, dE/E0=9.53e-07, N=798
  Estimated time remaining to complete simulation: 9 hours, 57 minutes, 17 seconds
  Estimated time remaining to next output: 5 minutes, 47 seconds
Output 440/542: t=8970000.0 yr, dE/E0=9.56e-07, N=798
  Estimated time remaining to complete simulation: 9 hours, 52 minutes, 8 seconds
  Estimated time remaining to next output: 5 minutes, 48 seconds
Output 441/542: t=8980000.0 yr, dE/E0=9.39e-07, N=798
  Estimated time remaining to complete simulation: 9 hours, 47 minutes, 9 seconds
  Estimated time remaining to next output: 5 minutes, 48 seconds
Output 442/542: t=8990000.0 yr, dE/E0=9.43e-07, N=798
  Estimated time remaining to complete simulation: 9 hours, 42 minutes, 2 seconds
  Estimated time remaining to next output: 5 minutes, 49 seconds
Output 443/542: t=9000000.0 yr, dE/E0=9.52e-07, N=798
  Estimated time remaining to complete simulation: 9 hours, 36 minutes, 54 seconds
  Estimated time remaining to next output: 5 minutes, 49 seconds
Output 444/542: t=9010000.0 yr, dE/E0=9.58e-07, N=798
  Estimated time remaining to complete simulation: 9 hours, 31 minutes, 47 seconds
  Estimated time remaining to next output: 5 minutes, 50 seconds
Output 445/542: t=9020000.0 yr, dE/E0=9.66e-07, N=798
  Estimated time remaining to complete simulation: 9 hours, 26 minutes, 31 seconds
  Estimated time remaining to next output: 5 minutes, 50 seconds
Output 446/542: t=9030000.0 yr, dE/E0=9.63e-07, N=798
  Estimated time remaining to complete simulation: 9 hours, 21 minutes, 16 seconds
  Estimated time remaining to next output: 5 minutes, 50 seconds
Output 447/542: t=9040000.0 yr, dE/E0=9.52e-07, N=798
  Estimated time remaining to complete simulation: 9 hours, 16 minutes, 1 seconds
  Estimated time remaining to next output: 5 minutes, 51 seconds
Output 448/542: t=9050000.0 yr, dE/E0=9.47e-07, N=798
  Estimated time remaining to complete simulation: 9 hours, 10 minutes, 44 seconds
  Estimated time remaining to next output: 5 minutes, 51 seconds
Output 449/542: t=9060000.0 yr, dE/E0=9.61e-07, N=798
  Estimated time remaining to complete simulation: 9 hours, 5 minutes, 28 seconds
  Estimated time remaining to next output: 5 minutes, 51 seconds
Output 450/542: t=9070000.0 yr, dE/E0=9.59e-07, N=798
  Estimated time remaining to complete simulation: 9 hours, 8 seconds
  Estimated time remaining to next output: 5 minutes, 52 seconds
Output 451/542: t=9080000.0 yr, dE/E0=9.69e-07, N=798
  Estimated time remaining to complete simulation: 8 hours, 54 minutes, 54 seconds
  Estimated time remaining to next output: 5 minutes, 52 seconds
Output 452/542: t=9090000.0 yr, dE/E0=9.61e-07, N=798
  Estimated time remaining to complete simulation: 8 hours, 49 minutes, 35 seconds
  Estimated time remaining to next output: 5 minutes, 53 seconds
Output 453/542: t=9100000.0 yr, dE/E0=9.54e-07, N=798
  Estimated time remaining to complete simulation: 8 hours, 44 minutes, 12 seconds
  Estimated time remaining to next output: 5 minutes, 53 seconds
Output 454/542: t=9110000.0 yr, dE/E0=9.60e-07, N=798
  Estimated time remaining to complete simulation: 8 hours, 38 minutes, 47 seconds
  Estimated time remaining to next output: 5 minutes, 53 seconds
Output 455/542: t=9120000.0 yr, dE/E0=9.54e-07, N=798
  Estimated time remaining to complete simulation: 8 hours, 33 minutes, 25 seconds
  Estimated time remaining to next output: 5 minutes, 54 seconds
Output 456/542: t=9130000.0 yr, dE/E0=9.58e-07, N=798
  Estimated time remaining to complete simulation: 8 hours, 28 minutes
  Estimated time remaining to next output: 5 minutes, 54 seconds
Output 457/542: t=9140000.0 yr, dE/E0=9.66e-07, N=798
  Estimated time remaining to complete simulation: 8 hours, 22 minutes, 43 seconds
  Estimated time remaining to next output: 5 minutes, 54 seconds
Output 458/542: t=9150000.0 yr, dE/E0=9.72e-07, N=798
  Estimated time remaining to complete simulation: 8 hours, 17 minutes, 21 seconds
  Estimated time remaining to next output: 5 minutes, 55 seconds
Output 459/542: t=9160000.0 yr, dE/E0=9.52e-07, N=798
  Estimated time remaining to complete simulation: 8 hours, 11 minutes, 55 seconds
  Estimated time remaining to next output: 5 minutes, 55 seconds
Output 460/542: t=9170000.0 yr, dE/E0=9.52e-07, N=798
  Estimated time remaining to complete simulation: 8 hours, 6 minutes, 26 seconds
  Estimated time remaining to next output: 5 minutes, 55 seconds
Output 461/542: t=9180000.0 yr, dE/E0=9.57e-07, N=798
  Estimated time remaining to complete simulation: 8 hours, 1 minutes
  Estimated time remaining to next output: 5 minutes, 56 seconds
Output 462/542: t=9190000.0 yr, dE/E0=9.76e-07, N=798
  Estimated time remaining to complete simulation: 7 hours, 55 minutes, 8 seconds
  Estimated time remaining to next output: 5 minutes, 56 seconds
Output 463/542: t=9200000.0 yr, dE/E0=9.79e-07, N=798
  Estimated time remaining to complete simulation: 7 hours, 49 minutes, 8 seconds
  Estimated time remaining to next output: 5 minutes, 56 seconds
Output 464/542: t=9210000.0 yr, dE/E0=9.71e-07, N=798
  Estimated time remaining to complete simulation: 7 hours, 43 minutes, 4 seconds
  Estimated time remaining to next output: 5 minutes, 56 seconds
Output 465/542: t=9220000.0 yr, dE/E0=9.62e-07, N=798
  Estimated time remaining to complete simulation: 7 hours, 37 minutes, 13 seconds
  Estimated time remaining to next output: 5 minutes, 56 seconds
Output 466/542: t=9230000.0 yr, dE/E0=9.53e-07, N=798
  Estimated time remaining to complete simulation: 7 hours, 31 minutes, 45 seconds
  Estimated time remaining to next output: 5 minutes, 56 seconds
Output 467/542: t=9240000.0 yr, dE/E0=9.48e-07, N=798
  Estimated time remaining to complete simulation: 7 hours, 26 minutes, 18 seconds
  Estimated time remaining to next output: 5 minutes, 57 seconds
Output 468/542: t=9250000.0 yr, dE/E0=9.58e-07, N=798
  Estimated time remaining to complete simulation: 7 hours, 20 minutes, 47 seconds
  Estimated time remaining to next output: 5 minutes, 57 seconds
Output 469/542: t=9260000.0 yr, dE/E0=9.68e-07, N=798
  Estimated time remaining to complete simulation: 7 hours, 15 minutes, 15 seconds
  Estimated time remaining to next output: 5 minutes, 57 seconds
Output 470/542: t=9270000.0 yr, dE/E0=9.74e-07, N=798
  Estimated time remaining to complete simulation: 7 hours, 9 minutes, 40 seconds
  Estimated time remaining to next output: 5 minutes, 58 seconds
Output 471/542: t=9280000.0 yr, dE/E0=9.64e-07, N=798
  Estimated time remaining to complete simulation: 7 hours, 4 minutes, 3 seconds
  Estimated time remaining to next output: 5 minutes, 58 seconds
Output 472/542: t=9290000.0 yr, dE/E0=9.54e-07, N=798
  Estimated time remaining to complete simulation: 6 hours, 58 minutes, 30 seconds
  Estimated time remaining to next output: 5 minutes, 58 seconds
Output 473/542: t=9300000.0 yr, dE/E0=9.62e-07, N=798
  Estimated time remaining to complete simulation: 6 hours, 52 minutes, 53 seconds
  Estimated time remaining to next output: 5 minutes, 59 seconds
Output 474/542: t=9310000.0 yr, dE/E0=9.72e-07, N=798
  Estimated time remaining to complete simulation: 6 hours, 47 minutes, 15 seconds
  Estimated time remaining to next output: 5 minutes, 59 seconds
Output 475/542: t=9320000.0 yr, dE/E0=9.71e-07, N=798
  Estimated time remaining to complete simulation: 6 hours, 41 minutes, 42 seconds
  Estimated time remaining to next output: 5 minutes, 59 seconds
Output 476/542: t=9330000.0 yr, dE/E0=9.72e-07, N=798
  Estimated time remaining to complete simulation: 6 hours, 36 minutes, 6 seconds
  Estimated time remaining to next output: 6 minutes
Output 477/542: t=9340000.0 yr, dE/E0=9.66e-07, N=798
  Estimated time remaining to complete simulation: 6 hours, 30 minutes, 27 seconds
  Estimated time remaining to next output: 6 minutes
Output 478/542: t=9350000.0 yr, dE/E0=9.60e-07, N=798
  Estimated time remaining to complete simulation: 6 hours, 24 minutes, 44 seconds
  Estimated time remaining to next output: 6 minutes
Output 479/542: t=9360000.0 yr, dE/E0=9.63e-07, N=798
  Estimated time remaining to complete simulation: 6 hours, 19 minutes, 7 seconds
  Estimated time remaining to next output: 6 minutes, 1 seconds
Output 480/542: t=9370000.0 yr, dE/E0=9.73e-07, N=798
  Estimated time remaining to complete simulation: 6 hours, 13 minutes, 26 seconds
  Estimated time remaining to next output: 6 minutes, 1 seconds
Output 481/542: t=9380000.0 yr, dE/E0=9.68e-07, N=798
  Estimated time remaining to complete simulation: 6 hours, 7 minutes, 46 seconds
  Estimated time remaining to next output: 6 minutes, 1 seconds
Output 482/542: t=9390000.0 yr, dE/E0=9.68e-07, N=798
  Estimated time remaining to complete simulation: 6 hours, 2 minutes, 3 seconds
  Estimated time remaining to next output: 6 minutes, 2 seconds
Output 483/542: t=9400000.0 yr, dE/E0=9.65e-07, N=798
  Estimated time remaining to complete simulation: 5 hours, 56 minutes, 19 seconds
  Estimated time remaining to next output: 6 minutes, 2 seconds
Output 484/542: t=9410000.0 yr, dE/E0=9.60e-07, N=798
  Estimated time remaining to complete simulation: 5 hours, 50 minutes, 32 seconds
  Estimated time remaining to next output: 6 minutes, 2 seconds
Output 485/542: t=9420000.0 yr, dE/E0=9.63e-07, N=798
  Estimated time remaining to complete simulation: 5 hours, 44 minutes, 52 seconds
  Estimated time remaining to next output: 6 minutes, 3 seconds
Output 486/542: t=9430000.0 yr, dE/E0=9.65e-07, N=798
  Estimated time remaining to complete simulation: 5 hours, 39 minutes, 7 seconds
  Estimated time remaining to next output: 6 minutes, 3 seconds
Output 487/542: t=9440000.0 yr, dE/E0=9.69e-07, N=798
  Estimated time remaining to complete simulation: 5 hours, 33 minutes, 24 seconds
  Estimated time remaining to next output: 6 minutes, 3 seconds
Output 488/542: t=9450000.0 yr, dE/E0=9.75e-07, N=798
  Estimated time remaining to complete simulation: 5 hours, 27 minutes, 37 seconds
  Estimated time remaining to next output: 6 minutes, 4 seconds
Output 489/542: t=9460000.0 yr, dE/E0=9.66e-07, N=798
  Estimated time remaining to complete simulation: 5 hours, 21 minutes, 51 seconds
  Estimated time remaining to next output: 6 minutes, 4 seconds
Output 490/542: t=9470000.0 yr, dE/E0=9.53e-07, N=798
  Estimated time remaining to complete simulation: 5 hours, 16 minutes, 1 seconds
  Estimated time remaining to next output: 6 minutes, 4 seconds
Output 491/542: t=9480000.0 yr, dE/E0=9.60e-07, N=798
  Estimated time remaining to complete simulation: 5 hours, 9 minutes, 52 seconds
  Estimated time remaining to next output: 6 minutes, 4 seconds
Output 492/542: t=9490000.0 yr, dE/E0=9.67e-07, N=798
  Estimated time remaining to complete simulation: 5 hours, 3 minutes, 49 seconds
  Estimated time remaining to next output: 6 minutes, 4 seconds
Output 493/542: t=9500000.0 yr, dE/E0=9.86e-07, N=798
  Estimated time remaining to complete simulation: 4 hours, 57 minutes, 59 seconds
  Estimated time remaining to next output: 6 minutes, 4 seconds
Output 494/542: t=9510000.0 yr, dE/E0=9.79e-07, N=798
  Estimated time remaining to complete simulation: 4 hours, 51 minutes, 54 seconds
  Estimated time remaining to next output: 6 minutes, 4 seconds
Output 495/542: t=9520000.0 yr, dE/E0=9.65e-07, N=798
  Estimated time remaining to complete simulation: 4 hours, 45 minutes, 46 seconds
  Estimated time remaining to next output: 6 minutes, 4 seconds
Output 496/542: t=9530000.0 yr, dE/E0=9.64e-07, N=798
  Estimated time remaining to complete simulation: 4 hours, 39 minutes, 37 seconds
  Estimated time remaining to next output: 6 minutes, 4 seconds
Output 497/542: t=9540000.0 yr, dE/E0=9.69e-07, N=798
  Estimated time remaining to complete simulation: 4 hours, 33 minutes, 31 seconds
  Estimated time remaining to next output: 6 minutes, 4 seconds
Output 498/542: t=9550000.0 yr, dE/E0=9.69e-07, N=798
  Estimated time remaining to complete simulation: 4 hours, 27 minutes, 23 seconds
  Estimated time remaining to next output: 6 minutes, 4 seconds
Output 499/542: t=9560000.0 yr, dE/E0=9.76e-07, N=798
  Estimated time remaining to complete simulation: 4 hours, 21 minutes, 18 seconds
  Estimated time remaining to next output: 6 minutes, 4 seconds
Output 500/542: t=9570000.0 yr, dE/E0=9.63e-07, N=798
  Estimated time remaining to complete simulation: 4 hours, 15 minutes, 31 seconds
  Estimated time remaining to next output: 6 minutes, 5 seconds
Output 501/542: t=9580000.0 yr, dE/E0=9.65e-07, N=798
  Estimated time remaining to complete simulation: 4 hours, 9 minutes, 38 seconds
  Estimated time remaining to next output: 6 minutes, 5 seconds
Output 502/542: t=9590000.0 yr, dE/E0=9.53e-07, N=798
  Estimated time remaining to complete simulation: 4 hours, 3 minutes, 44 seconds
  Estimated time remaining to next output: 6 minutes, 5 seconds
Output 503/542: t=9600000.0 yr, dE/E0=9.63e-07, N=798
  Estimated time remaining to complete simulation: 3 hours, 57 minutes, 52 seconds
  Estimated time remaining to next output: 6 minutes, 5 seconds
Output 504/542: t=9610000.0 yr, dE/E0=9.66e-07, N=798
  Estimated time remaining to complete simulation: 3 hours, 51 minutes, 57 seconds
  Estimated time remaining to next output: 6 minutes, 6 seconds
Output 505/542: t=9620000.0 yr, dE/E0=9.75e-07, N=798
  Estimated time remaining to complete simulation: 3 hours, 45 minutes, 57 seconds
  Estimated time remaining to next output: 6 minutes, 6 seconds
Output 506/542: t=9630000.0 yr, dE/E0=9.70e-07, N=798
  Estimated time remaining to complete simulation: 3 hours, 39 minutes, 55 seconds
  Estimated time remaining to next output: 6 minutes, 6 seconds
Output 507/542: t=9640000.0 yr, dE/E0=9.70e-07, N=798
  Estimated time remaining to complete simulation: 3 hours, 33 minutes, 59 seconds
  Estimated time remaining to next output: 6 minutes, 6 seconds
Output 508/542: t=9650000.0 yr, dE/E0=9.60e-07, N=798
  Estimated time remaining to complete simulation: 3 hours, 28 minutes, 2 seconds
  Estimated time remaining to next output: 6 minutes, 7 seconds
Output 509/542: t=9660000.0 yr, dE/E0=9.73e-07, N=798
  Estimated time remaining to complete simulation: 3 hours, 21 minutes, 53 seconds
  Estimated time remaining to next output: 6 minutes, 7 seconds
Output 510/542: t=9670000.0 yr, dE/E0=9.83e-07, N=798
  Estimated time remaining to complete simulation: 3 hours, 15 minutes, 43 seconds
  Estimated time remaining to next output: 6 minutes, 6 seconds
Output 511/542: t=9680000.0 yr, dE/E0=9.83e-07, N=798
  Estimated time remaining to complete simulation: 3 hours, 9 minutes, 33 seconds
  Estimated time remaining to next output: 6 minutes, 6 seconds
Output 512/542: t=9690000.0 yr, dE/E0=9.71e-07, N=798
  Estimated time remaining to complete simulation: 3 hours, 3 minutes, 24 seconds
  Estimated time remaining to next output: 6 minutes, 6 seconds
Output 513/542: t=9700000.0 yr, dE/E0=9.60e-07, N=798
  Estimated time remaining to complete simulation: 2 hours, 57 minutes, 15 seconds
  Estimated time remaining to next output: 6 minutes, 6 seconds
Output 514/542: t=9710000.0 yr, dE/E0=9.69e-07, N=798
  Estimated time remaining to complete simulation: 2 hours, 51 minutes, 5 seconds
  Estimated time remaining to next output: 6 minutes, 6 seconds
Output 515/542: t=9720000.0 yr, dE/E0=9.63e-07, N=798
  Estimated time remaining to complete simulation: 2 hours, 44 minutes, 56 seconds
  Estimated time remaining to next output: 6 minutes, 6 seconds
Output 516/542: t=9730000.0 yr, dE/E0=9.74e-07, N=798
  Estimated time remaining to complete simulation: 2 hours, 38 minutes, 47 seconds
  Estimated time remaining to next output: 6 minutes, 6 seconds
Output 517/542: t=9740000.0 yr, dE/E0=9.79e-07, N=798
  Estimated time remaining to complete simulation: 2 hours, 32 minutes, 38 seconds
  Estimated time remaining to next output: 6 minutes, 6 seconds
Output 518/542: t=9750000.0 yr, dE/E0=9.75e-07, N=798
  Estimated time remaining to complete simulation: 2 hours, 26 minutes, 29 seconds
  Estimated time remaining to next output: 6 minutes, 6 seconds
Output 519/542: t=9760000.0 yr, dE/E0=9.70e-07, N=798
  Estimated time remaining to complete simulation: 2 hours, 20 minutes, 20 seconds
  Estimated time remaining to next output: 6 minutes, 6 seconds
Output 520/542: t=9770000.0 yr, dE/E0=9.65e-07, N=798
  Estimated time remaining to complete simulation: 2 hours, 14 minutes, 12 seconds
  Estimated time remaining to next output: 6 minutes, 6 seconds
Output 521/542: t=9780000.0 yr, dE/E0=9.67e-07, N=798
  Estimated time remaining to complete simulation: 2 hours, 8 minutes, 5 seconds
  Estimated time remaining to next output: 6 minutes, 5 seconds
Output 522/542: t=9790000.0 yr, dE/E0=9.66e-07, N=798
  Estimated time remaining to complete simulation: 2 hours, 1 minutes, 57 seconds
  Estimated time remaining to next output: 6 minutes, 5 seconds
Output 523/542: t=9800000.0 yr, dE/E0=9.76e-07, N=798
  Estimated time remaining to complete simulation: 1 hours, 55 minutes, 49 seconds
  Estimated time remaining to next output: 6 minutes, 5 seconds
Output 524/542: t=9810000.0 yr, dE/E0=9.74e-07, N=798
  Estimated time remaining to complete simulation: 1 hours, 49 minutes, 42 seconds
  Estimated time remaining to next output: 6 minutes, 5 seconds
Output 525/542: t=9820000.0 yr, dE/E0=9.62e-07, N=798
  Estimated time remaining to complete simulation: 1 hours, 43 minutes, 34 seconds
  Estimated time remaining to next output: 6 minutes, 5 seconds
Output 526/542: t=9830000.0 yr, dE/E0=9.65e-07, N=798
  Estimated time remaining to complete simulation: 1 hours, 37 minutes, 27 seconds
  Estimated time remaining to next output: 6 minutes, 5 seconds
Output 527/542: t=9840000.0 yr, dE/E0=9.58e-07, N=798
  Estimated time remaining to complete simulation: 1 hours, 31 minutes, 20 seconds
  Estimated time remaining to next output: 6 minutes, 5 seconds
Output 528/542: t=9850000.0 yr, dE/E0=9.59e-07, N=798
  Estimated time remaining to complete simulation: 1 hours, 25 minutes, 14 seconds
  Estimated time remaining to next output: 6 minutes, 5 seconds
Output 529/542: t=9860000.0 yr, dE/E0=9.71e-07, N=798
  Estimated time remaining to complete simulation: 1 hours, 19 minutes, 8 seconds
  Estimated time remaining to next output: 6 minutes, 5 seconds
Output 530/542: t=9870000.0 yr, dE/E0=9.70e-07, N=798
  Estimated time remaining to complete simulation: 1 hours, 13 minutes, 2 seconds
  Estimated time remaining to next output: 6 minutes, 5 seconds
Output 531/542: t=9880000.0 yr, dE/E0=9.57e-07, N=798
  Estimated time remaining to complete simulation: 1 hours, 6 minutes, 56 seconds
  Estimated time remaining to next output: 6 minutes, 5 seconds
Output 532/542: t=9890000.0 yr, dE/E0=9.47e-07, N=798
  Estimated time remaining to complete simulation: 1 hours, 50 seconds
  Estimated time remaining to next output: 6 minutes, 5 seconds
Output 533/542: t=9900000.0 yr, dE/E0=9.59e-07, N=798
  Estimated time remaining to complete simulation: 54 minutes, 45 seconds
  Estimated time remaining to next output: 6 minutes, 5 seconds
Output 534/542: t=9910000.0 yr, dE/E0=9.65e-07, N=798
  Estimated time remaining to complete simulation: 48 minutes, 39 seconds
  Estimated time remaining to next output: 6 minutes, 4 seconds
Output 535/542: t=9920000.0 yr, dE/E0=9.70e-07, N=798
  Estimated time remaining to complete simulation: 42 minutes, 34 seconds
  Estimated time remaining to next output: 6 minutes, 4 seconds
Output 536/542: t=9930000.0 yr, dE/E0=9.77e-07, N=798
  Estimated time remaining to complete simulation: 36 minutes, 28 seconds
  Estimated time remaining to next output: 6 minutes, 4 seconds
Output 537/542: t=9940000.0 yr, dE/E0=9.71e-07, N=798
  Estimated time remaining to complete simulation: 30 minutes, 23 seconds
  Estimated time remaining to next output: 6 minutes, 4 seconds
Output 538/542: t=9950000.0 yr, dE/E0=9.76e-07, N=798
  Estimated time remaining to complete simulation: 24 minutes, 18 seconds
  Estimated time remaining to next output: 6 minutes, 4 seconds
Output 539/542: t=9960000.0 yr, dE/E0=9.58e-07, N=798
  Estimated time remaining to complete simulation: 18 minutes, 13 seconds
  Estimated time remaining to next output: 6 minutes, 4 seconds
Output 540/542: t=9970000.0 yr, dE/E0=9.75e-07, N=798
  Estimated time remaining to complete simulation: 12 minutes, 8 seconds
  Estimated time remaining to next output: 6 minutes, 4 seconds
Output 541/542: t=9980000.0 yr, dE/E0=9.83e-07, N=798
  Estimated time remaining to complete simulation: 6 minutes, 4 seconds
  Estimated time remaining to next output: 6 minutes, 4 seconds
Output 542/542: t=9990000.0 yr, dE/E0=9.74e-07, N=798
  Estimated time remaining to complete simulation: 0 seconds
Output 543/542: t=10000000.0 yr, dE/E0=9.79e-07, N=798
  Estimated time remaining to complete simulation: -1 months, 4 weeks, 1 days, 23 hours, 53 minutes, 56 seconds

Simulation complete.
Total runtime: 2 days, 6 hours, 55 minutes, 52 seconds

Krivov & Booth (2018) self-stirring check (Eqs. 9-10):
  NOTE: a giant planet is present; the two-population self-stirring model assumes no external perturber, so C_e below is only indicative.
  Final time:                 t = 1.000000e+07 yr
  Rayleigh outlier cut:       e > 5 sigma = 1.0841e-01 (sigma = median(e)/sqrt(2 ln 2) = 2.1683e-02)
  Stirred-disk check:         median(e) = 2.5529e-02 vs 30 x disk.emax = 9.6000e-04 -> stirred, cut applied
  Excluded MPs:               8 -- MP_525 (e = 0.7546), MP_521 (e = 0.3683), MP_522 (e = 0.1365), MP_416 (e = 0.1300), MP_206 (e = 0.1284), MP_135 (e = 0.1196), MP_213 (e = 0.1132), MP_551 (e = 0.1128)
  KS test of kept e vs Rayleigh: D = 0.1236, p = 5.95e-11  (WARNING: p < 0.05, kept e deviates from a Rayleigh distribution)
  RMS eccentricity (788 of 796 MPs): 3.638487e-02  (all MPs: 4.807995e-02)
  Belt geometry:              a = 100, da = 10, a/da = 10
  Masses:                     M_max = 6.368760e-09 Msun, M_disc = 2.991158e-06 Msun
  Implied stirring timescale: T = 1.141161e+13 yr
  Effective stirring factor:  C_e = 460.0098  (all MPs, no cut: 1402.6203)
  WARNING: C_e = 460.0098 >= 40 (Ida & Makino 1993 canonical value) -- this run stirs at or above the analytic self-stirring rate.
Saved archive: outputs/SS_800MP_10Myr_PSD2A_500Mearth_lorentzian/SS_800MP_10Myr_PSD2A_500Mearth_lorentzian.bin
Number of snapshots saved: 1002
Archive time range: 0.000e+00 yr to 1.000e+07 yr
Particle-name check: OK (1002 snapshots)
Loaded snapshot table from archive.
role
massive_planetesimal    800
star                      1
giant_planet              1
Name: count, dtype: int64
Saved: outputs/SS_800MP_10Myr_PSD2A_500Mearth_lorentzian/figures/survival_fraction_vs_time.png
Saved: outputs/SS_800MP_10Myr_PSD2A_500Mearth_lorentzian/figures/mean_semimajor_axis_vs_time.png
Saved: outputs/SS_800MP_10Myr_PSD2A_500Mearth_lorentzian/figures/mean_eccentricity_vs_time.png
Saved: outputs/SS_800MP_10Myr_PSD2A_500Mearth_lorentzian/figures/rms_eccentricity_vs_time.png
Saved: outputs/SS_800MP_10Myr_PSD2A_500Mearth_lorentzian/figures/rms_inclination_vs_time.png
Saved: outputs/SS_800MP_10Myr_PSD2A_500Mearth_lorentzian/figures/data/orbits_initial_final.csv
Saved: outputs/SS_800MP_10Myr_PSD2A_500Mearth_lorentzian/figures/a_vs_e_initial_final.png
Saved: outputs/SS_800MP_10Myr_PSD2A_500Mearth_lorentzian/figures/a_vs_i_initial_final.png
Inner plotted edge = 95.04 AU
Outer plotted edge = 104.92 AU
Saved: outputs/SS_800MP_10Myr_PSD2A_500Mearth_lorentzian/figures/xy_initial_final.png
All summary figures saved.
```
