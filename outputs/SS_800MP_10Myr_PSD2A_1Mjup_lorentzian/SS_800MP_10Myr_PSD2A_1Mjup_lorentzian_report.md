# SS_800MP_10Myr_PSD2A_1Mjup_lorentzian — Simulation Report

Config file: `config/SS_800MP_10Myr_PSD2A_1Mjup_lorentzian.yaml`
Archive file: `outputs/SS_800MP_10Myr_PSD2A_1Mjup_lorentzian/SS_800MP_10Myr_PSD2A_1Mjup_lorentzian.bin`

## Provenance

- Run UUID: `3303b4c3-9437-41b5-bc91-a180306c4980`
- Created: 2026-10-14T17:55:45-03:00
- Finished: 2026-10-23T17:16:46-03:00
- Wall runtime: 355922.0 s
- Outcome: completed
- Command: `src/simulation/run_simulation.py config/SS_800MP_10Myr_PSD2A_1Mjup_lorentzian.yaml`
- Git commit: `9e8790c32d4476a63517560b2cb1c9a16a917270` (branch `main`) **(DIRTY — uncommitted tracked changes)**
    - modified: `notebooks/mass_model_playground.ipynb`
- Software: python 3.12.14, rebound 5.0.0, numpy 2.4.6, pandas 3.0.3, matplotlib 3.10.9, pyyaml 6.0.3
- Resumed 1 time(s) after the first run
- Frozen config: `config.yaml` (this directory)
- Full environment: `environment.txt` (this directory)

## Simulation
- Name: SS_800MP_10Myr_PSD2A_1Mjup_lorentzian
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
- Mass: 1.0 Mjup
- a: 70.852725 au, e: 0.0, inc: 0.0 deg
- omega: 0.0 deg, Omega random: True
- t_peri_jd: 2451545.0, orbital_period_days: 217833.698, epoch_jd: 2451545.0

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
- Final particle count: 802
- Particles lost (escaped / unbound / other removal): 0
- Archive time range: 0.000000e+00 to 1.000000e+07
- Number of snapshots: 1002

## Terminal Output

```
Saving SimulationArchive to: outputs/SS_800MP_10Myr_PSD2A_1Mjup_lorentzian/SS_800MP_10Myr_PSD2A_1Mjup_lorentzian.bin
Resuming from t=1.110000e+06 yr: times=array([ 1110000.,  1120000.,  1130000.,  1140000.,  1150000.,  1160000.,
        1170000.,  1180000.,  1190000.,  1200000.,  1210000.,  1220000.,
        1230000.,  1240000.,  1250000.,  1260000.,  1270000.,  1280000.,
        1290000.,  1300000.,  1310000.,  1320000.,  1330000.,  1340000.,
        1350000.,  1360000.,  1370000.,  1380000.,  1390000.,  1400000.,
        1410000.,  1420000.,  1430000.,  1440000.,  1450000.,  1460000.,
        1470000.,  1480000.,  1490000.,  1500000.,  1510000.,  1520000.,
        1530000.,  1540000.,  1550000.,  1560000.,  1570000.,  1580000.,
        1590000.,  1600000.,  1610000.,  1620000.,  1630000.,  1640000.,
        1650000.,  1660000.,  1670000.,  1680000.,  1690000.,  1700000.,
        1710000.,  1720000.,  1730000.,  1740000.,  1750000.,  1760000.,
        1770000.,  1780000.,  1790000.,  1800000.,  1810000.,  1820000.,
        1830000.,  1840000.,  1850000.,  1860000.,  1870000.,  1880000.,
        1890000.,  1900000.,  1910000.,  1920000.,  1930000.,  1940000.,
        1950000.,  1960000.,  1970000.,  1980000.,  1990000.,  2000000.,
        2010000.,  2020000.,  2030000.,  2040000.,  2050000.,  2060000.,
        2070000.,  2080000.,  2090000.,  2100000.,  2110000.,  2120000.,
        2130000.,  2140000.,  2150000.,  2160000.,  2170000.,  2180000.,
        2190000.,  2200000.,  2210000.,  2220000.,  2230000.,  2240000.,
        2250000.,  2260000.,  2270000.,  2280000.,  2290000.,  2300000.,
        2310000.,  2320000.,  2330000.,  2340000.,  2350000.,  2360000.,
        2370000.,  2380000.,  2390000.,  2400000.,  2410000.,  2420000.,
        2430000.,  2440000.,  2450000.,  2460000.,  2470000.,  2480000.,
        2490000.,  2500000.,  2510000.,  2520000.,  2530000.,  2540000.,
        2550000.,  2560000.,  2570000.,  2580000.,  2590000.,  2600000.,
        2610000.,  2620000.,  2630000.,  2640000.,  2650000.,  2660000.,
        2670000.,  2680000.,  2690000.,  2700000.,  2710000.,  2720000.,
        2730000.,  2740000.,  2750000.,  2760000.,  2770000.,  2780000.,
        2790000.,  2800000.,  2810000.,  2820000.,  2830000.,  2840000.,
        2850000.,  2860000.,  2870000.,  2880000.,  2890000.,  2900000.,
        2910000.,  2920000.,  2930000.,  2940000.,  2950000.,  2960000.,
        2970000.,  2980000.,  2990000.,  3000000.,  3010000.,  3020000.,
        3030000.,  3040000.,  3050000.,  3060000.,  3070000.,  3080000.,
        3090000.,  3100000.,  3110000.,  3120000.,  3130000.,  3140000.,
        3150000.,  3160000.,  3170000.,  3180000.,  3190000.,  3200000.,
        3210000.,  3220000.,  3230000.,  3240000.,  3250000.,  3260000.,
        3270000.,  3280000.,  3290000.,  3300000.,  3310000.,  3320000.,
        3330000.,  3340000.,  3350000.,  3360000.,  3370000.,  3380000.,
        3390000.,  3400000.,  3410000.,  3420000.,  3430000.,  3440000.,
        3450000.,  3460000.,  3470000.,  3480000.,  3490000.,  3500000.,
        3510000.,  3520000.,  3530000.,  3540000.,  3550000.,  3560000.,
        3570000.,  3580000.,  3590000.,  3600000.,  3610000.,  3620000.,
        3630000.,  3640000.,  3650000.,  3660000.,  3670000.,  3680000.,
        3690000.,  3700000.,  3710000.,  3720000.,  3730000.,  3740000.,
        3750000.,  3760000.,  3770000.,  3780000.,  3790000.,  3800000.,
        3810000.,  3820000.,  3830000.,  3840000.,  3850000.,  3860000.,
        3870000.,  3880000.,  3890000.,  3900000.,  3910000.,  3920000.,
        3930000.,  3940000.,  3950000.,  3960000.,  3970000.,  3980000.,
        3990000.,  4000000.,  4010000.,  4020000.,  4030000.,  4040000.,
        4050000.,  4060000.,  4070000.,  4080000.,  4090000.,  4100000.,
        4110000.,  4120000.,  4130000.,  4140000.,  4150000.,  4160000.,
        4170000.,  4180000.,  4190000.,  4200000.,  4210000.,  4220000.,
        4230000.,  4240000.,  4250000.,  4260000.,  4270000.,  4280000.,
        4290000.,  4300000.,  4310000.,  4320000.,  4330000.,  4340000.,
        4350000.,  4360000.,  4370000.,  4380000.,  4390000.,  4400000.,
        4410000.,  4420000.,  4430000.,  4440000.,  4450000.,  4460000.,
        4470000.,  4480000.,  4490000.,  4500000.,  4510000.,  4520000.,
        4530000.,  4540000.,  4550000.,  4560000.,  4570000.,  4580000.,
        4590000.,  4600000.,  4610000.,  4620000.,  4630000.,  4640000.,
        4650000.,  4660000.,  4670000.,  4680000.,  4690000.,  4700000.,
        4710000.,  4720000.,  4730000.,  4740000.,  4750000.,  4760000.,
        4770000.,  4780000.,  4790000.,  4800000.,  4810000.,  4820000.,
        4830000.,  4840000.,  4850000.,  4860000.,  4870000.,  4880000.,
        4890000.,  4900000.,  4910000.,  4920000.,  4930000.,  4940000.,
        4950000.,  4960000.,  4970000.,  4980000.,  4990000.,  5000000.,
        5010000.,  5020000.,  5030000.,  5040000.,  5050000.,  5060000.,
        5070000.,  5080000.,  5090000.,  5100000.,  5110000.,  5120000.,
        5130000.,  5140000.,  5150000.,  5160000.,  5170000.,  5180000.,
        5190000.,  5200000.,  5210000.,  5220000.,  5230000.,  5240000.,
        5250000.,  5260000.,  5270000.,  5280000.,  5290000.,  5300000.,
        5310000.,  5320000.,  5330000.,  5340000.,  5350000.,  5360000.,
        5370000.,  5380000.,  5390000.,  5400000.,  5410000.,  5420000.,
        5430000.,  5440000.,  5450000.,  5460000.,  5470000.,  5480000.,
        5490000.,  5500000.,  5510000.,  5520000.,  5530000.,  5540000.,
        5550000.,  5560000.,  5570000.,  5580000.,  5590000.,  5600000.,
        5610000.,  5620000.,  5630000.,  5640000.,  5650000.,  5660000.,
        5670000.,  5680000.,  5690000.,  5700000.,  5710000.,  5720000.,
        5730000.,  5740000.,  5750000.,  5760000.,  5770000.,  5780000.,
        5790000.,  5800000.,  5810000.,  5820000.,  5830000.,  5840000.,
        5850000.,  5860000.,  5870000.,  5880000.,  5890000.,  5900000.,
        5910000.,  5920000.,  5930000.,  5940000.,  5950000.,  5960000.,
        5970000.,  5980000.,  5990000.,  6000000.,  6010000.,  6020000.,
        6030000.,  6040000.,  6050000.,  6060000.,  6070000.,  6080000.,
        6090000.,  6100000.,  6110000.,  6120000.,  6130000.,  6140000.,
        6150000.,  6160000.,  6170000.,  6180000.,  6190000.,  6200000.,
        6210000.,  6220000.,  6230000.,  6240000.,  6250000.,  6260000.,
        6270000.,  6280000.,  6290000.,  6300000.,  6310000.,  6320000.,
        6330000.,  6340000.,  6350000.,  6360000.,  6370000.,  6380000.,
        6390000.,  6400000.,  6410000.,  6420000.,  6430000.,  6440000.,
        6450000.,  6460000.,  6470000.,  6480000.,  6490000.,  6500000.,
        6510000.,  6520000.,  6530000.,  6540000.,  6550000.,  6560000.,
        6570000.,  6580000.,  6590000.,  6600000.,  6610000.,  6620000.,
        6630000.,  6640000.,  6650000.,  6660000.,  6670000.,  6680000.,
        6690000.,  6700000.,  6710000.,  6720000.,  6730000.,  6740000.,
        6750000.,  6760000.,  6770000.,  6780000.,  6790000.,  6800000.,
        6810000.,  6820000.,  6830000.,  6840000.,  6850000.,  6860000.,
        6870000.,  6880000.,  6890000.,  6900000.,  6910000.,  6920000.,
        6930000.,  6940000.,  6950000.,  6960000.,  6970000.,  6980000.,
        6990000.,  7000000.,  7010000.,  7020000.,  7030000.,  7040000.,
        7050000.,  7060000.,  7070000.,  7080000.,  7090000.,  7100000.,
        7110000.,  7120000.,  7130000.,  7140000.,  7150000.,  7160000.,
        7170000.,  7180000.,  7190000.,  7200000.,  7210000.,  7220000.,
        7230000.,  7240000.,  7250000.,  7260000.,  7270000.,  7280000.,
        7290000.,  7300000.,  7310000.,  7320000.,  7330000.,  7340000.,
        7350000.,  7360000.,  7370000.,  7380000.,  7390000.,  7400000.,
        7410000.,  7420000.,  7430000.,  7440000.,  7450000.,  7460000.,
        7470000.,  7480000.,  7490000.,  7500000.,  7510000.,  7520000.,
        7530000.,  7540000.,  7550000.,  7560000.,  7570000.,  7580000.,
        7590000.,  7600000.,  7610000.,  7620000.,  7630000.,  7640000.,
        7650000.,  7660000.,  7670000.,  7680000.,  7690000.,  7700000.,
        7710000.,  7720000.,  7730000.,  7740000.,  7750000.,  7760000.,
        7770000.,  7780000.,  7790000.,  7800000.,  7810000.,  7820000.,
        7830000.,  7840000.,  7850000.,  7860000.,  7870000.,  7880000.,
        7890000.,  7900000.,  7910000.,  7920000.,  7930000.,  7940000.,
        7950000.,  7960000.,  7970000.,  7980000.,  7990000.,  8000000.,
        8010000.,  8020000.,  8030000.,  8040000.,  8050000.,  8060000.,
        8070000.,  8080000.,  8090000.,  8100000.,  8110000.,  8120000.,
        8130000.,  8140000.,  8150000.,  8160000.,  8170000.,  8180000.,
        8190000.,  8200000.,  8210000.,  8220000.,  8230000.,  8240000.,
        8250000.,  8260000.,  8270000.,  8280000.,  8290000.,  8300000.,
        8310000.,  8320000.,  8330000.,  8340000.,  8350000.,  8360000.,
        8370000.,  8380000.,  8390000.,  8400000.,  8410000.,  8420000.,
        8430000.,  8440000.,  8450000.,  8460000.,  8470000.,  8480000.,
        8490000.,  8500000.,  8510000.,  8520000.,  8530000.,  8540000.,
        8550000.,  8560000.,  8570000.,  8580000.,  8590000.,  8600000.,
        8610000.,  8620000.,  8630000.,  8640000.,  8650000.,  8660000.,
        8670000.,  8680000.,  8690000.,  8700000.,  8710000.,  8720000.,
        8730000.,  8740000.,  8750000.,  8760000.,  8770000.,  8780000.,
        8790000.,  8800000.,  8810000.,  8820000.,  8830000.,  8840000.,
        8850000.,  8860000.,  8870000.,  8880000.,  8890000.,  8900000.,
        8910000.,  8920000.,  8930000.,  8940000.,  8950000.,  8960000.,
        8970000.,  8980000.,  8990000.,  9000000.,  9010000.,  9020000.,
        9030000.,  9040000.,  9050000.,  9060000.,  9070000.,  9080000.,
        9090000.,  9100000.,  9110000.,  9120000.,  9130000.,  9140000.,
        9150000.,  9160000.,  9170000.,  9180000.,  9190000.,  9200000.,
        9210000.,  9220000.,  9230000.,  9240000.,  9250000.,  9260000.,
        9270000.,  9280000.,  9290000.,  9300000.,  9310000.,  9320000.,
        9330000.,  9340000.,  9350000.,  9360000.,  9370000.,  9380000.,
        9390000.,  9400000.,  9410000.,  9420000.,  9430000.,  9440000.,
        9450000.,  9460000.,  9470000.,  9480000.,  9490000.,  9500000.,
        9510000.,  9520000.,  9530000.,  9540000.,  9550000.,  9560000.,
        9570000.,  9580000.,  9590000.,  9600000.,  9610000.,  9620000.,
        9630000.,  9640000.,  9650000.,  9660000.,  9670000.,  9680000.,
        9690000.,  9700000.,  9710000.,  9720000.,  9730000.,  9740000.,
        9750000.,  9760000.,  9770000.,  9780000.,  9790000.,  9800000.,
        9810000.,  9820000.,  9830000.,  9840000.,  9850000.,  9860000.,
        9870000.,  9880000.,  9890000.,  9900000.,  9910000.,  9920000.,
        9930000.,  9940000.,  9950000.,  9960000.,  9970000.,  9980000.,
        9990000., 10000000.])
Found dump file. Restoring simulation from snapshot...
  Timestep: 5.961178e+01 (0.1 x giant planet orbital period = 5.961178e+02)
Restored simulation from snapshot number at t=1.110000e+06 yr with N=802 particles.

Stirrer-coverage check (Krivov & Booth 2018: N x delta_af >= delta_a):
  Stirrers inside the belt [95, 105]: N = 792
  delta_af = 8 sqrt(3) h_M a_M:  mean = 1.481959e+00, sum over stirrers = 1.173712e+03
  Belt width delta_a = 1.000000e+01
  Coverage ratio (sum delta_af / delta_a) = 117.371
  OK: stirrer feeding zones span the belt.

Beginning the main integration
Output 1/889: t=1110000.0 yr, dE/E0=0.00e+00, N=802
  Estimated time remaining to complete simulation: 1 minutes, 16 seconds
  Estimated time remaining to next output: 0 seconds
Output 2/889: t=1120000.0 yr, dE/E0=5.28e-09, N=802
  Estimated time remaining to complete simulation: 4 days, 1 hours, 27 minutes, 15 seconds
  Estimated time remaining to next output: 6 minutes, 35 seconds
Output 3/889: t=1130000.0 yr, dE/E0=4.82e-10, N=802
  Estimated time remaining to complete simulation: 5 days, 10 hours, 24 minutes, 22 seconds
  Estimated time remaining to next output: 8 minutes, 49 seconds
Output 4/889: t=1140000.0 yr, dE/E0=7.95e-09, N=802
  Estimated time remaining to complete simulation: 6 days, 2 hours, 39 minutes, 34 seconds
  Estimated time remaining to next output: 9 minutes, 56 seconds
Output 5/889: t=1150000.0 yr, dE/E0=1.77e-08, N=802
  Estimated time remaining to complete simulation: 6 days, 14 hours, 50 minutes, 41 seconds
  Estimated time remaining to next output: 10 minutes, 46 seconds
Output 6/889: t=1160000.0 yr, dE/E0=2.46e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 2 hours, 58 minutes, 15 seconds
  Estimated time remaining to next output: 11 minutes, 37 seconds
Output 7/889: t=1170000.0 yr, dE/E0=2.01e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 13 hours, 25 minutes, 5 seconds
  Estimated time remaining to next output: 12 minutes, 20 seconds
Output 8/889: t=1180000.0 yr, dE/E0=2.23e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 20 hours, 49 minutes, 10 seconds
  Estimated time remaining to next output: 12 minutes, 51 seconds
Output 9/889: t=1190000.0 yr, dE/E0=2.99e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 1 days, 2 hours, 17 minutes, 47 seconds
  Estimated time remaining to next output: 13 minutes, 14 seconds
Output 10/889: t=1200000.0 yr, dE/E0=3.34e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 1 days, 7 hours, 39 minutes, 26 seconds
  Estimated time remaining to next output: 13 minutes, 37 seconds
Output 11/889: t=1210000.0 yr, dE/E0=3.77e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 1 days, 10 hours, 51 minutes, 49 seconds
  Estimated time remaining to next output: 13 minutes, 51 seconds
Output 12/889: t=1220000.0 yr, dE/E0=3.57e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 1 days, 14 hours, 6 minutes, 28 seconds
  Estimated time remaining to next output: 14 minutes, 6 seconds
Output 13/889: t=1230000.0 yr, dE/E0=3.42e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 1 days, 16 hours, 55 minutes, 24 seconds
  Estimated time remaining to next output: 14 minutes, 18 seconds
Output 14/889: t=1240000.0 yr, dE/E0=3.49e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 1 days, 17 hours, 57 minutes, 21 seconds
  Estimated time remaining to next output: 14 minutes, 23 seconds
Output 15/889: t=1250000.0 yr, dE/E0=4.90e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 1 days, 13 hours, 18 seconds
  Estimated time remaining to next output: 14 minutes, 4 seconds
Output 16/889: t=1260000.0 yr, dE/E0=3.73e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 1 days, 7 hours, 21 minutes, 6 seconds
  Estimated time remaining to next output: 13 minutes, 42 seconds
Output 17/889: t=1270000.0 yr, dE/E0=3.87e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 1 days, 2 hours, 18 minutes, 31 seconds
  Estimated time remaining to next output: 13 minutes, 22 seconds
Output 18/889: t=1280000.0 yr, dE/E0=3.47e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 21 hours, 55 minutes, 38 seconds
  Estimated time remaining to next output: 13 minutes, 5 seconds
Output 19/889: t=1290000.0 yr, dE/E0=3.10e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 17 hours, 50 minutes, 3 seconds
  Estimated time remaining to next output: 12 minutes, 48 seconds
Output 20/889: t=1300000.0 yr, dE/E0=3.89e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 14 hours, 11 minutes, 57 seconds
  Estimated time remaining to next output: 12 minutes, 34 seconds
Output 21/889: t=1310000.0 yr, dE/E0=3.72e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 11 hours, 3 minutes, 25 seconds
  Estimated time remaining to next output: 12 minutes, 22 seconds
Output 22/889: t=1320000.0 yr, dE/E0=4.44e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 8 hours, 39 minutes, 19 seconds
  Estimated time remaining to next output: 12 minutes, 13 seconds
Output 23/889: t=1330000.0 yr, dE/E0=4.30e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 6 hours, 9 minutes, 58 seconds
  Estimated time remaining to next output: 12 minutes, 4 seconds
Output 24/889: t=1340000.0 yr, dE/E0=4.57e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 3 hours, 58 minutes, 6 seconds
  Estimated time remaining to next output: 11 minutes, 55 seconds
Output 25/889: t=1350000.0 yr, dE/E0=3.91e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 1 hours, 43 minutes, 32 seconds
  Estimated time remaining to next output: 11 minutes, 47 seconds
Output 26/889: t=1360000.0 yr, dE/E0=3.69e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 4 minutes, 44 seconds
  Estimated time remaining to next output: 11 minutes, 41 seconds
Output 27/889: t=1370000.0 yr, dE/E0=3.88e-08, N=802
  Estimated time remaining to complete simulation: 6 days, 22 hours, 52 minutes, 31 seconds
  Estimated time remaining to next output: 11 minutes, 36 seconds
Output 28/889: t=1380000.0 yr, dE/E0=4.27e-08, N=802
  Estimated time remaining to complete simulation: 6 days, 21 hours, 31 minutes, 16 seconds
  Estimated time remaining to next output: 11 minutes, 32 seconds
Output 29/889: t=1390000.0 yr, dE/E0=4.36e-08, N=802
  Estimated time remaining to complete simulation: 6 days, 20 hours, 6 minutes, 26 seconds
  Estimated time remaining to next output: 11 minutes, 26 seconds
Output 30/889: t=1400000.0 yr, dE/E0=3.74e-08, N=802
  Estimated time remaining to complete simulation: 6 days, 19 hours, 26 minutes, 43 seconds
  Estimated time remaining to next output: 11 minutes, 24 seconds
Output 31/889: t=1410000.0 yr, dE/E0=3.52e-08, N=802
  Estimated time remaining to complete simulation: 6 days, 18 hours, 30 minutes, 27 seconds
  Estimated time remaining to next output: 11 minutes, 21 seconds
Output 32/889: t=1420000.0 yr, dE/E0=3.39e-08, N=802
  Estimated time remaining to complete simulation: 6 days, 17 hours, 16 minutes, 20 seconds
  Estimated time remaining to next output: 11 minutes, 17 seconds
Output 33/889: t=1430000.0 yr, dE/E0=3.26e-08, N=802
  Estimated time remaining to complete simulation: 6 days, 15 hours, 57 minutes, 52 seconds
  Estimated time remaining to next output: 11 minutes, 12 seconds
Output 34/889: t=1440000.0 yr, dE/E0=3.10e-08, N=802
  Estimated time remaining to complete simulation: 6 days, 15 hours, 6 minutes, 56 seconds
  Estimated time remaining to next output: 11 minutes, 9 seconds
Output 35/889: t=1450000.0 yr, dE/E0=2.51e-08, N=802
  Estimated time remaining to complete simulation: 6 days, 14 hours, 21 minutes, 59 seconds
  Estimated time remaining to next output: 11 minutes, 7 seconds
Output 36/889: t=1460000.0 yr, dE/E0=3.11e-08, N=802
  Estimated time remaining to complete simulation: 6 days, 13 hours, 43 minutes, 57 seconds
  Estimated time remaining to next output: 11 minutes, 5 seconds
Output 37/889: t=1470000.0 yr, dE/E0=2.88e-08, N=802
  Estimated time remaining to complete simulation: 6 days, 13 hours, 46 minutes, 33 seconds
  Estimated time remaining to next output: 11 minutes, 6 seconds
Output 38/889: t=1480000.0 yr, dE/E0=3.52e-08, N=802
  Estimated time remaining to complete simulation: 6 days, 13 hours, 14 minutes, 13 seconds
  Estimated time remaining to next output: 11 minutes, 5 seconds
Output 39/889: t=1490000.0 yr, dE/E0=3.50e-08, N=802
  Estimated time remaining to complete simulation: 6 days, 12 hours, 49 minutes, 39 seconds
  Estimated time remaining to next output: 11 minutes, 4 seconds
Output 40/889: t=1500000.0 yr, dE/E0=3.49e-08, N=802
  Estimated time remaining to complete simulation: 6 days, 12 hours, 17 minutes, 13 seconds
  Estimated time remaining to next output: 11 minutes, 2 seconds
Output 41/889: t=1510000.0 yr, dE/E0=3.57e-08, N=802
  Estimated time remaining to complete simulation: 6 days, 11 hours, 47 minutes, 33 seconds
  Estimated time remaining to next output: 11 minutes, 1 seconds
Output 42/889: t=1520000.0 yr, dE/E0=3.29e-08, N=802
  Estimated time remaining to complete simulation: 6 days, 11 hours, 23 minutes, 6 seconds
  Estimated time remaining to next output: 11 minutes
Output 43/889: t=1530000.0 yr, dE/E0=3.22e-08, N=802
  Estimated time remaining to complete simulation: 6 days, 10 hours, 25 minutes, 54 seconds
  Estimated time remaining to next output: 10 minutes, 57 seconds
Output 44/889: t=1540000.0 yr, dE/E0=2.91e-08, N=802
  Estimated time remaining to complete simulation: 6 days, 8 hours, 42 minutes, 47 seconds
  Estimated time remaining to next output: 10 minutes, 50 seconds
Output 45/889: t=1550000.0 yr, dE/E0=3.33e-08, N=802
  Estimated time remaining to complete simulation: 6 days, 7 hours, 13 minutes, 9 seconds
  Estimated time remaining to next output: 10 minutes, 45 seconds
Output 46/889: t=1560000.0 yr, dE/E0=4.08e-08, N=802
  Estimated time remaining to complete simulation: 6 days, 5 hours, 44 minutes, 52 seconds
  Estimated time remaining to next output: 10 minutes, 39 seconds
Output 47/889: t=1570000.0 yr, dE/E0=3.15e-08, N=802
  Estimated time remaining to complete simulation: 6 days, 4 hours, 9 minutes, 8 seconds
  Estimated time remaining to next output: 10 minutes, 33 seconds
Output 48/889: t=1580000.0 yr, dE/E0=2.38e-08, N=802
  Estimated time remaining to complete simulation: 6 days, 2 hours, 41 minutes, 9 seconds
  Estimated time remaining to next output: 10 minutes, 27 seconds
Output 49/889: t=1590000.0 yr, dE/E0=3.82e-08, N=802
  Estimated time remaining to complete simulation: 6 days, 1 hours, 14 minutes, 28 seconds
  Estimated time remaining to next output: 10 minutes, 22 seconds
Output 50/889: t=1600000.0 yr, dE/E0=3.27e-08, N=802
  Estimated time remaining to complete simulation: 5 days, 23 hours, 57 minutes, 7 seconds
  Estimated time remaining to next output: 10 minutes, 17 seconds
Output 51/889: t=1610000.0 yr, dE/E0=3.05e-08, N=802
  Estimated time remaining to complete simulation: 5 days, 22 hours, 39 minutes, 3 seconds
  Estimated time remaining to next output: 10 minutes, 12 seconds
Output 52/889: t=1620000.0 yr, dE/E0=2.13e-08, N=802
  Estimated time remaining to complete simulation: 5 days, 21 hours, 30 minutes, 55 seconds
  Estimated time remaining to next output: 10 minutes, 8 seconds
Output 53/889: t=1630000.0 yr, dE/E0=2.22e-08, N=802
  Estimated time remaining to complete simulation: 5 days, 20 hours, 25 minutes, 4 seconds
  Estimated time remaining to next output: 10 minutes, 4 seconds
Output 54/889: t=1640000.0 yr, dE/E0=4.22e-08, N=802
  Estimated time remaining to complete simulation: 5 days, 19 hours, 15 minutes
  Estimated time remaining to next output: 10 minutes
Output 55/889: t=1650000.0 yr, dE/E0=5.10e-08, N=802
  Estimated time remaining to complete simulation: 5 days, 18 hours, 5 minutes, 4 seconds
  Estimated time remaining to next output: 9 minutes, 56 seconds
Output 56/889: t=1660000.0 yr, dE/E0=4.05e-08, N=802
  Estimated time remaining to complete simulation: 5 days, 17 hours, 6 minutes, 46 seconds
  Estimated time remaining to next output: 9 minutes, 52 seconds
Output 57/889: t=1670000.0 yr, dE/E0=3.84e-08, N=802
  Estimated time remaining to complete simulation: 5 days, 16 hours, 1 minutes, 36 seconds
  Estimated time remaining to next output: 9 minutes, 48 seconds
Output 58/889: t=1680000.0 yr, dE/E0=4.78e-08, N=802
  Estimated time remaining to complete simulation: 5 days, 15 hours, 2 minutes, 51 seconds
  Estimated time remaining to next output: 9 minutes, 45 seconds
Output 59/889: t=1690000.0 yr, dE/E0=4.43e-08, N=802
  Estimated time remaining to complete simulation: 5 days, 14 hours, 13 minutes, 17 seconds
  Estimated time remaining to next output: 9 minutes, 42 seconds
Output 60/889: t=1700000.0 yr, dE/E0=4.91e-08, N=802
  Estimated time remaining to complete simulation: 5 days, 13 hours, 17 minutes, 26 seconds
  Estimated time remaining to next output: 9 minutes, 38 seconds
Output 61/889: t=1710000.0 yr, dE/E0=4.39e-08, N=802
  Estimated time remaining to complete simulation: 5 days, 12 hours, 20 minutes, 38 seconds
  Estimated time remaining to next output: 9 minutes, 35 seconds
Output 62/889: t=1720000.0 yr, dE/E0=4.63e-08, N=802
  Estimated time remaining to complete simulation: 5 days, 11 hours, 23 minutes, 28 seconds
  Estimated time remaining to next output: 9 minutes, 31 seconds
Output 63/889: t=1730000.0 yr, dE/E0=5.01e-08, N=802
  Estimated time remaining to complete simulation: 5 days, 10 hours, 36 minutes, 36 seconds
  Estimated time remaining to next output: 9 minutes, 29 seconds
Output 64/889: t=1740000.0 yr, dE/E0=4.24e-08, N=802
  Estimated time remaining to complete simulation: 5 days, 9 hours, 42 minutes, 58 seconds
  Estimated time remaining to next output: 9 minutes, 26 seconds
Output 65/889: t=1750000.0 yr, dE/E0=4.43e-08, N=802
  Estimated time remaining to complete simulation: 5 days, 8 hours, 49 minutes, 48 seconds
  Estimated time remaining to next output: 9 minutes, 22 seconds
Output 66/889: t=1760000.0 yr, dE/E0=4.81e-08, N=802
  Estimated time remaining to complete simulation: 5 days, 8 hours, 2 seconds
  Estimated time remaining to next output: 9 minutes, 19 seconds
Output 67/889: t=1770000.0 yr, dE/E0=4.64e-08, N=802
  Estimated time remaining to complete simulation: 5 days, 7 hours, 15 minutes, 14 seconds
  Estimated time remaining to next output: 9 minutes, 17 seconds
Output 68/889: t=1780000.0 yr, dE/E0=5.38e-08, N=802
  Estimated time remaining to complete simulation: 5 days, 6 hours, 26 minutes, 48 seconds
  Estimated time remaining to next output: 9 minutes, 14 seconds
Output 69/889: t=1790000.0 yr, dE/E0=3.57e-08, N=802
  Estimated time remaining to complete simulation: 5 days, 5 hours, 43 minutes, 5 seconds
  Estimated time remaining to next output: 9 minutes, 11 seconds
Output 70/889: t=1800000.0 yr, dE/E0=3.49e-08, N=802
  Estimated time remaining to complete simulation: 5 days, 4 hours, 55 minutes, 44 seconds
  Estimated time remaining to next output: 9 minutes, 9 seconds
Output 71/889: t=1810000.0 yr, dE/E0=4.01e-08, N=802
  Estimated time remaining to complete simulation: 5 days, 4 hours, 17 minutes, 12 seconds
  Estimated time remaining to next output: 9 minutes, 6 seconds
Output 72/889: t=1820000.0 yr, dE/E0=3.94e-08, N=802
  Estimated time remaining to complete simulation: 5 days, 3 hours, 37 minutes, 17 seconds
  Estimated time remaining to next output: 9 minutes, 4 seconds
Output 73/889: t=1830000.0 yr, dE/E0=4.52e-08, N=802
  Estimated time remaining to complete simulation: 5 days, 2 hours, 57 minutes, 30 seconds
  Estimated time remaining to next output: 9 minutes, 2 seconds
Output 74/889: t=1840000.0 yr, dE/E0=4.08e-08, N=802
  Estimated time remaining to complete simulation: 5 days, 2 hours, 20 minutes, 19 seconds
  Estimated time remaining to next output: 9 minutes
Output 75/889: t=1850000.0 yr, dE/E0=4.50e-08, N=802
  Estimated time remaining to complete simulation: 5 days, 1 hours, 41 minutes, 32 seconds
  Estimated time remaining to next output: 8 minutes, 58 seconds
Output 76/889: t=1860000.0 yr, dE/E0=4.16e-08, N=802
  Estimated time remaining to complete simulation: 5 days, 58 minutes, 15 seconds
  Estimated time remaining to next output: 8 minutes, 55 seconds
Output 77/889: t=1870000.0 yr, dE/E0=5.22e-08, N=802
  Estimated time remaining to complete simulation: 5 days, 25 minutes, 43 seconds
  Estimated time remaining to next output: 8 minutes, 53 seconds
Output 78/889: t=1880000.0 yr, dE/E0=4.74e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 23 hours, 51 minutes, 39 seconds
  Estimated time remaining to next output: 8 minutes, 52 seconds
Output 79/889: t=1890000.0 yr, dE/E0=3.63e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 23 hours, 15 minutes, 4 seconds
  Estimated time remaining to next output: 8 minutes, 50 seconds
Output 80/889: t=1900000.0 yr, dE/E0=4.38e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 22 hours, 38 minutes, 3 seconds
  Estimated time remaining to next output: 8 minutes, 47 seconds
Output 81/889: t=1910000.0 yr, dE/E0=3.82e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 22 hours, 4 minutes, 28 seconds
  Estimated time remaining to next output: 8 minutes, 46 seconds
Output 82/889: t=1920000.0 yr, dE/E0=2.26e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 21 hours, 31 minutes, 41 seconds
  Estimated time remaining to next output: 8 minutes, 44 seconds
Output 83/889: t=1930000.0 yr, dE/E0=3.20e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 20 hours, 57 minutes, 1 seconds
  Estimated time remaining to next output: 8 minutes, 42 seconds
Output 84/889: t=1940000.0 yr, dE/E0=2.59e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 20 hours, 25 minutes, 1 seconds
  Estimated time remaining to next output: 8 minutes, 40 seconds
Output 85/889: t=1950000.0 yr, dE/E0=3.13e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 19 hours, 52 minutes, 34 seconds
  Estimated time remaining to next output: 8 minutes, 38 seconds
Output 86/889: t=1960000.0 yr, dE/E0=3.78e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 19 hours, 28 minutes, 49 seconds
  Estimated time remaining to next output: 8 minutes, 37 seconds
Output 87/889: t=1970000.0 yr, dE/E0=2.12e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 19 hours, 36 minutes, 51 seconds
  Estimated time remaining to next output: 8 minutes, 38 seconds
Output 88/889: t=1980000.0 yr, dE/E0=1.38e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 19 hours, 40 minutes, 43 seconds
  Estimated time remaining to next output: 8 minutes, 39 seconds
Output 89/889: t=1990000.0 yr, dE/E0=2.19e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 19 hours, 47 minutes, 36 seconds
  Estimated time remaining to next output: 8 minutes, 41 seconds
Output 90/889: t=2000000.0 yr, dE/E0=2.05e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 19 hours, 46 minutes, 1 seconds
  Estimated time remaining to next output: 8 minutes, 41 seconds
Output 91/889: t=2010000.0 yr, dE/E0=2.10e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 19 hours, 47 minutes, 33 seconds
  Estimated time remaining to next output: 8 minutes, 42 seconds
Output 92/889: t=2020000.0 yr, dE/E0=1.36e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 19 hours, 51 minutes, 26 seconds
  Estimated time remaining to next output: 8 minutes, 43 seconds
Output 93/889: t=2030000.0 yr, dE/E0=1.62e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 19 hours, 52 minutes, 56 seconds
  Estimated time remaining to next output: 8 minutes, 44 seconds
Output 94/889: t=2040000.0 yr, dE/E0=2.25e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 19 hours, 52 minutes, 2 seconds
  Estimated time remaining to next output: 8 minutes, 44 seconds
Output 95/889: t=2050000.0 yr, dE/E0=2.26e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 19 hours, 52 minutes, 7 seconds
  Estimated time remaining to next output: 8 minutes, 45 seconds
Output 96/889: t=2060000.0 yr, dE/E0=2.39e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 19 hours, 59 minutes, 51 seconds
  Estimated time remaining to next output: 8 minutes, 46 seconds
Output 97/889: t=2070000.0 yr, dE/E0=2.79e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 20 hours, 2 minutes, 53 seconds
  Estimated time remaining to next output: 8 minutes, 47 seconds
Output 98/889: t=2080000.0 yr, dE/E0=1.53e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 20 hours, 2 minutes, 47 seconds
  Estimated time remaining to next output: 8 minutes, 48 seconds
Output 99/889: t=2090000.0 yr, dE/E0=2.45e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 19 hours, 37 minutes, 54 seconds
  Estimated time remaining to next output: 8 minutes, 46 seconds
Output 100/889: t=2100000.0 yr, dE/E0=2.86e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 19 hours, 8 minutes, 40 seconds
  Estimated time remaining to next output: 8 minutes, 45 seconds
Output 101/889: t=2110000.0 yr, dE/E0=2.16e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 18 hours, 39 minutes, 49 seconds
  Estimated time remaining to next output: 8 minutes, 43 seconds
Output 102/889: t=2120000.0 yr, dE/E0=2.71e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 18 hours, 9 minutes, 45 seconds
  Estimated time remaining to next output: 8 minutes, 42 seconds
Output 103/889: t=2130000.0 yr, dE/E0=3.02e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 17 hours, 41 minutes, 16 seconds
  Estimated time remaining to next output: 8 minutes, 40 seconds
Output 104/889: t=2140000.0 yr, dE/E0=2.86e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 17 hours, 12 minutes, 43 seconds
  Estimated time remaining to next output: 8 minutes, 39 seconds
Output 105/889: t=2150000.0 yr, dE/E0=2.51e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 16 hours, 43 minutes, 24 seconds
  Estimated time remaining to next output: 8 minutes, 37 seconds
Output 106/889: t=2160000.0 yr, dE/E0=3.24e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 16 hours, 15 minutes, 10 seconds
  Estimated time remaining to next output: 8 minutes, 36 seconds
Output 107/889: t=2170000.0 yr, dE/E0=3.73e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 15 hours, 48 minutes, 51 seconds
  Estimated time remaining to next output: 8 minutes, 34 seconds
Output 108/889: t=2180000.0 yr, dE/E0=4.10e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 15 hours, 20 minutes, 43 seconds
  Estimated time remaining to next output: 8 minutes, 33 seconds
Output 109/889: t=2190000.0 yr, dE/E0=3.91e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 14 hours, 53 minutes, 30 seconds
  Estimated time remaining to next output: 8 minutes, 31 seconds
Output 110/889: t=2200000.0 yr, dE/E0=3.13e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 14 hours, 25 minutes, 42 seconds
  Estimated time remaining to next output: 8 minutes, 30 seconds
Output 111/889: t=2210000.0 yr, dE/E0=2.25e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 14 hours, 4 minutes, 52 seconds
  Estimated time remaining to next output: 8 minutes, 29 seconds
Output 112/889: t=2220000.0 yr, dE/E0=3.05e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 13 hours, 42 minutes, 57 seconds
  Estimated time remaining to next output: 8 minutes, 28 seconds
Output 113/889: t=2230000.0 yr, dE/E0=3.82e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 13 hours, 18 minutes, 8 seconds
  Estimated time remaining to next output: 8 minutes, 27 seconds
Output 114/889: t=2240000.0 yr, dE/E0=2.89e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 12 hours, 55 minutes, 31 seconds
  Estimated time remaining to next output: 8 minutes, 25 seconds
Output 115/889: t=2250000.0 yr, dE/E0=2.33e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 12 hours, 31 minutes, 7 seconds
  Estimated time remaining to next output: 8 minutes, 24 seconds
Output 116/889: t=2260000.0 yr, dE/E0=2.66e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 12 hours, 8 minutes, 59 seconds
  Estimated time remaining to next output: 8 minutes, 23 seconds
Output 117/889: t=2270000.0 yr, dE/E0=2.00e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 11 hours, 46 minutes, 4 seconds
  Estimated time remaining to next output: 8 minutes, 22 seconds
Output 118/889: t=2280000.0 yr, dE/E0=1.29e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 11 hours, 20 minutes, 48 seconds
  Estimated time remaining to next output: 8 minutes, 21 seconds
Output 119/889: t=2290000.0 yr, dE/E0=1.64e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 10 hours, 57 minutes, 29 seconds
  Estimated time remaining to next output: 8 minutes, 20 seconds
Output 120/889: t=2300000.0 yr, dE/E0=1.03e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 10 hours, 36 minutes, 3 seconds
  Estimated time remaining to next output: 8 minutes, 19 seconds
Output 121/889: t=2310000.0 yr, dE/E0=1.07e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 10 hours, 14 minutes, 12 seconds
  Estimated time remaining to next output: 8 minutes, 17 seconds
Output 122/889: t=2320000.0 yr, dE/E0=1.03e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 9 hours, 54 minutes, 2 seconds
  Estimated time remaining to next output: 8 minutes, 17 seconds
Output 123/889: t=2330000.0 yr, dE/E0=2.53e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 9 hours, 32 minutes, 41 seconds
  Estimated time remaining to next output: 8 minutes, 16 seconds
Output 124/889: t=2340000.0 yr, dE/E0=1.36e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 9 hours, 10 minutes, 24 seconds
  Estimated time remaining to next output: 8 minutes, 14 seconds
Output 125/889: t=2350000.0 yr, dE/E0=1.99e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 8 hours, 52 minutes, 19 seconds
  Estimated time remaining to next output: 8 minutes, 14 seconds
Output 126/889: t=2360000.0 yr, dE/E0=2.62e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 8 hours, 32 minutes, 53 seconds
  Estimated time remaining to next output: 8 minutes, 13 seconds
Output 127/889: t=2370000.0 yr, dE/E0=2.70e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 8 hours, 10 minutes, 1 seconds
  Estimated time remaining to next output: 8 minutes, 12 seconds
Output 128/889: t=2380000.0 yr, dE/E0=2.81e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 7 hours, 50 minutes, 2 seconds
  Estimated time remaining to next output: 8 minutes, 11 seconds
Output 129/889: t=2390000.0 yr, dE/E0=3.60e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 7 hours, 29 minutes, 6 seconds
  Estimated time remaining to next output: 8 minutes, 10 seconds
Output 130/889: t=2400000.0 yr, dE/E0=3.04e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 7 hours, 10 minutes, 37 seconds
  Estimated time remaining to next output: 8 minutes, 9 seconds
Output 131/889: t=2410000.0 yr, dE/E0=3.04e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 7 hours, 8 minutes, 23 seconds
  Estimated time remaining to next output: 8 minutes, 9 seconds
Output 132/889: t=2420000.0 yr, dE/E0=2.31e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 7 hours, 11 minutes, 36 seconds
  Estimated time remaining to next output: 8 minutes, 10 seconds
Output 133/889: t=2430000.0 yr, dE/E0=2.73e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 7 hours, 11 minutes, 12 seconds
  Estimated time remaining to next output: 8 minutes, 11 seconds
Output 134/889: t=2440000.0 yr, dE/E0=2.89e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 7 hours, 16 minutes, 9 seconds
  Estimated time remaining to next output: 8 minutes, 12 seconds
Output 135/889: t=2450000.0 yr, dE/E0=2.99e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 7 hours, 16 minutes, 58 seconds
  Estimated time remaining to next output: 8 minutes, 13 seconds
Output 136/889: t=2460000.0 yr, dE/E0=2.46e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 7 hours, 18 minutes, 44 seconds
  Estimated time remaining to next output: 8 minutes, 13 seconds
Output 137/889: t=2470000.0 yr, dE/E0=1.85e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 7 hours, 18 minutes, 14 seconds
  Estimated time remaining to next output: 8 minutes, 14 seconds
Output 138/889: t=2480000.0 yr, dE/E0=2.76e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 7 hours, 21 minutes, 35 seconds
  Estimated time remaining to next output: 8 minutes, 15 seconds
Output 139/889: t=2490000.0 yr, dE/E0=2.44e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 7 hours, 26 minutes, 10 seconds
  Estimated time remaining to next output: 8 minutes, 16 seconds
Output 140/889: t=2500000.0 yr, dE/E0=2.14e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 7 hours, 29 minutes, 2 seconds
  Estimated time remaining to next output: 8 minutes, 17 seconds
Output 141/889: t=2510000.0 yr, dE/E0=1.40e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 7 hours, 27 minutes, 37 seconds
  Estimated time remaining to next output: 8 minutes, 17 seconds
Output 142/889: t=2520000.0 yr, dE/E0=7.40e-09, N=802
  Estimated time remaining to complete simulation: 4 days, 7 hours, 27 minutes, 1 seconds
  Estimated time remaining to next output: 8 minutes, 18 seconds
Output 143/889: t=2530000.0 yr, dE/E0=4.29e-09, N=802
  Estimated time remaining to complete simulation: 4 days, 7 hours, 29 minutes, 26 seconds
  Estimated time remaining to next output: 8 minutes, 19 seconds
Output 144/889: t=2540000.0 yr, dE/E0=2.14e-09, N=802
  Estimated time remaining to complete simulation: 4 days, 7 hours, 29 minutes, 55 seconds
  Estimated time remaining to next output: 8 minutes, 20 seconds
Output 145/889: t=2550000.0 yr, dE/E0=5.21e-09, N=802
  Estimated time remaining to complete simulation: 4 days, 7 hours, 36 minutes, 21 seconds
  Estimated time remaining to next output: 8 minutes, 21 seconds
Output 146/889: t=2560000.0 yr, dE/E0=7.81e-09, N=802
  Estimated time remaining to complete simulation: 4 days, 7 hours, 38 minutes, 19 seconds
  Estimated time remaining to next output: 8 minutes, 22 seconds
Output 147/889: t=2570000.0 yr, dE/E0=4.77e-09, N=802
  Estimated time remaining to complete simulation: 4 days, 7 hours, 40 minutes, 8 seconds
  Estimated time remaining to next output: 8 minutes, 22 seconds
Output 148/889: t=2580000.0 yr, dE/E0=7.70e-10, N=802
  Estimated time remaining to complete simulation: 4 days, 7 hours, 42 minutes, 45 seconds
  Estimated time remaining to next output: 8 minutes, 23 seconds
Output 149/889: t=2590000.0 yr, dE/E0=1.42e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 7 hours, 43 minutes, 34 seconds
  Estimated time remaining to next output: 8 minutes, 24 seconds
Output 150/889: t=2600000.0 yr, dE/E0=1.39e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 7 hours, 41 minutes, 28 seconds
  Estimated time remaining to next output: 8 minutes, 25 seconds
Output 151/889: t=2610000.0 yr, dE/E0=8.35e-09, N=802
  Estimated time remaining to complete simulation: 4 days, 7 hours, 38 minutes, 17 seconds
  Estimated time remaining to next output: 8 minutes, 25 seconds
Output 152/889: t=2620000.0 yr, dE/E0=1.45e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 7 hours, 36 minutes, 25 seconds
  Estimated time remaining to next output: 8 minutes, 26 seconds
Output 153/889: t=2630000.0 yr, dE/E0=8.07e-09, N=802
  Estimated time remaining to complete simulation: 4 days, 7 hours, 36 minutes, 22 seconds
  Estimated time remaining to next output: 8 minutes, 26 seconds
Output 154/889: t=2640000.0 yr, dE/E0=1.64e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 7 hours, 35 minutes, 13 seconds
  Estimated time remaining to next output: 8 minutes, 27 seconds
Output 155/889: t=2650000.0 yr, dE/E0=2.23e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 7 hours, 36 minutes, 2 seconds
  Estimated time remaining to next output: 8 minutes, 28 seconds
Output 156/889: t=2660000.0 yr, dE/E0=1.79e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 7 hours, 34 minutes, 15 seconds
  Estimated time remaining to next output: 8 minutes, 28 seconds
Output 157/889: t=2670000.0 yr, dE/E0=2.23e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 7 hours, 32 minutes, 37 seconds
  Estimated time remaining to next output: 8 minutes, 29 seconds
Output 158/889: t=2680000.0 yr, dE/E0=2.26e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 7 hours, 28 minutes, 15 seconds
  Estimated time remaining to next output: 8 minutes, 29 seconds
Output 159/889: t=2690000.0 yr, dE/E0=3.22e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 7 hours, 29 minutes
  Estimated time remaining to next output: 8 minutes, 30 seconds
Output 160/889: t=2700000.0 yr, dE/E0=1.70e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 7 hours, 26 minutes, 30 seconds
  Estimated time remaining to next output: 8 minutes, 30 seconds
Output 161/889: t=2710000.0 yr, dE/E0=1.96e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 7 hours, 26 minutes, 16 seconds
  Estimated time remaining to next output: 8 minutes, 31 seconds
Output 162/889: t=2720000.0 yr, dE/E0=1.77e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 7 hours, 25 minutes, 30 seconds
  Estimated time remaining to next output: 8 minutes, 32 seconds
Output 163/889: t=2730000.0 yr, dE/E0=2.31e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 7 hours, 25 minutes, 24 seconds
  Estimated time remaining to next output: 8 minutes, 32 seconds
Output 164/889: t=2740000.0 yr, dE/E0=1.74e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 7 hours, 22 minutes, 2 seconds
  Estimated time remaining to next output: 8 minutes, 33 seconds
Output 165/889: t=2750000.0 yr, dE/E0=6.03e-09, N=802
  Estimated time remaining to complete simulation: 4 days, 7 hours, 18 minutes, 53 seconds
  Estimated time remaining to next output: 8 minutes, 33 seconds
Output 166/889: t=2760000.0 yr, dE/E0=1.24e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 7 hours, 15 minutes, 27 seconds
  Estimated time remaining to next output: 8 minutes, 34 seconds
Output 167/889: t=2770000.0 yr, dE/E0=2.69e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 7 hours, 15 minutes, 5 seconds
  Estimated time remaining to next output: 8 minutes, 34 seconds
Output 168/889: t=2780000.0 yr, dE/E0=2.80e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 7 hours, 16 minutes, 5 seconds
  Estimated time remaining to next output: 8 minutes, 35 seconds
Output 169/889: t=2790000.0 yr, dE/E0=1.80e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 7 hours, 2 minutes, 49 seconds
  Estimated time remaining to next output: 8 minutes, 35 seconds
Output 170/889: t=2800000.0 yr, dE/E0=8.43e-09, N=802
  Estimated time remaining to complete simulation: 4 days, 6 hours, 45 minutes, 43 seconds
  Estimated time remaining to next output: 8 minutes, 34 seconds
Output 171/889: t=2810000.0 yr, dE/E0=2.38e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 6 hours, 28 minutes, 36 seconds
  Estimated time remaining to next output: 8 minutes, 33 seconds
Output 172/889: t=2820000.0 yr, dE/E0=2.33e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 6 hours, 22 minutes, 25 seconds
  Estimated time remaining to next output: 8 minutes, 34 seconds
Output 173/889: t=2830000.0 yr, dE/E0=2.58e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 6 hours, 6 minutes, 29 seconds
  Estimated time remaining to next output: 8 minutes, 33 seconds
Output 174/889: t=2840000.0 yr, dE/E0=9.60e-09, N=802
  Estimated time remaining to complete simulation: 4 days, 5 hours, 47 minutes, 30 seconds
  Estimated time remaining to next output: 8 minutes, 32 seconds
Output 175/889: t=2850000.0 yr, dE/E0=8.99e-09, N=802
  Estimated time remaining to complete simulation: 4 days, 5 hours, 29 minutes, 36 seconds
  Estimated time remaining to next output: 8 minutes, 31 seconds
Output 176/889: t=2860000.0 yr, dE/E0=7.09e-09, N=802
  Estimated time remaining to complete simulation: 4 days, 5 hours, 14 minutes, 20 seconds
  Estimated time remaining to next output: 8 minutes, 31 seconds
Output 177/889: t=2870000.0 yr, dE/E0=1.27e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 4 hours, 56 minutes, 31 seconds
  Estimated time remaining to next output: 8 minutes, 30 seconds
Output 178/889: t=2880000.0 yr, dE/E0=1.54e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 4 hours, 53 minutes, 45 seconds
  Estimated time remaining to next output: 8 minutes, 30 seconds
Output 179/889: t=2890000.0 yr, dE/E0=9.52e-09, N=802
  Estimated time remaining to complete simulation: 4 days, 4 hours, 48 minutes, 4 seconds
  Estimated time remaining to next output: 8 minutes, 31 seconds
Output 180/889: t=2900000.0 yr, dE/E0=4.07e-09, N=802
  Estimated time remaining to complete simulation: 4 days, 4 hours, 36 minutes, 59 seconds
  Estimated time remaining to next output: 8 minutes, 30 seconds
Output 181/889: t=2910000.0 yr, dE/E0=7.62e-09, N=802
  Estimated time remaining to complete simulation: 4 days, 4 hours, 19 minutes, 58 seconds
  Estimated time remaining to next output: 8 minutes, 30 seconds
Output 182/889: t=2920000.0 yr, dE/E0=6.78e-10, N=802
  Estimated time remaining to complete simulation: 4 days, 4 hours, 3 minutes, 37 seconds
  Estimated time remaining to next output: 8 minutes, 29 seconds
Output 183/889: t=2930000.0 yr, dE/E0=5.94e-09, N=802
  Estimated time remaining to complete simulation: 4 days, 3 hours, 58 minutes, 40 seconds
  Estimated time remaining to next output: 8 minutes, 29 seconds
Output 184/889: t=2940000.0 yr, dE/E0=9.06e-09, N=802
  Estimated time remaining to complete simulation: 4 days, 3 hours, 52 minutes, 22 seconds
  Estimated time remaining to next output: 8 minutes, 29 seconds
Output 185/889: t=2950000.0 yr, dE/E0=8.35e-09, N=802
  Estimated time remaining to complete simulation: 4 days, 3 hours, 46 minutes, 31 seconds
  Estimated time remaining to next output: 8 minutes, 30 seconds
Output 186/889: t=2960000.0 yr, dE/E0=1.50e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 3 hours, 44 minutes, 45 seconds
  Estimated time remaining to next output: 8 minutes, 30 seconds
Output 187/889: t=2970000.0 yr, dE/E0=4.44e-09, N=802
  Estimated time remaining to complete simulation: 4 days, 3 hours, 41 minutes, 41 seconds
  Estimated time remaining to next output: 8 minutes, 31 seconds
Output 188/889: t=2980000.0 yr, dE/E0=4.45e-09, N=802
  Estimated time remaining to complete simulation: 4 days, 3 hours, 39 minutes, 29 seconds
  Estimated time remaining to next output: 8 minutes, 31 seconds
Output 189/889: t=2990000.0 yr, dE/E0=8.77e-09, N=802
  Estimated time remaining to complete simulation: 4 days, 3 hours, 27 minutes, 53 seconds
  Estimated time remaining to next output: 8 minutes, 31 seconds
Output 190/889: t=3000000.0 yr, dE/E0=1.60e-09, N=802
  Estimated time remaining to complete simulation: 4 days, 3 hours, 9 minutes, 32 seconds
  Estimated time remaining to next output: 8 minutes, 30 seconds
Output 191/889: t=3010000.0 yr, dE/E0=3.21e-09, N=802
  Estimated time remaining to complete simulation: 4 days, 2 hours, 52 minutes, 36 seconds
  Estimated time remaining to next output: 8 minutes, 29 seconds
Output 192/889: t=3020000.0 yr, dE/E0=5.44e-10, N=802
  Estimated time remaining to complete simulation: 4 days, 2 hours, 34 minutes, 54 seconds
  Estimated time remaining to next output: 8 minutes, 29 seconds
Output 193/889: t=3030000.0 yr, dE/E0=1.24e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 2 hours, 18 minutes, 49 seconds
  Estimated time remaining to next output: 8 minutes, 28 seconds
Output 194/889: t=3040000.0 yr, dE/E0=1.43e-09, N=802
  Estimated time remaining to complete simulation: 4 days, 2 hours, 1 minutes, 20 seconds
  Estimated time remaining to next output: 8 minutes, 27 seconds
Output 195/889: t=3050000.0 yr, dE/E0=3.73e-09, N=802
  Estimated time remaining to complete simulation: 4 days, 1 hours, 43 minutes, 1 seconds
  Estimated time remaining to next output: 8 minutes, 26 seconds
Output 196/889: t=3060000.0 yr, dE/E0=6.50e-10, N=802
  Estimated time remaining to complete simulation: 4 days, 1 hours, 26 minutes, 33 seconds
  Estimated time remaining to next output: 8 minutes, 26 seconds
Output 197/889: t=3070000.0 yr, dE/E0=1.08e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 1 hours, 15 minutes, 23 seconds
  Estimated time remaining to next output: 8 minutes, 25 seconds
Output 198/889: t=3080000.0 yr, dE/E0=9.36e-10, N=802
  Estimated time remaining to complete simulation: 4 days, 1 hours, 9 minutes, 40 seconds
  Estimated time remaining to next output: 8 minutes, 26 seconds
Output 199/889: t=3090000.0 yr, dE/E0=2.36e-09, N=802
  Estimated time remaining to complete simulation: 4 days, 1 hours, 6 minutes, 51 seconds
  Estimated time remaining to next output: 8 minutes, 26 seconds
Output 200/889: t=3100000.0 yr, dE/E0=3.20e-09, N=802
  Estimated time remaining to complete simulation: 4 days, 1 hours, 1 minutes, 28 seconds
  Estimated time remaining to next output: 8 minutes, 26 seconds
Output 201/889: t=3110000.0 yr, dE/E0=8.29e-09, N=802
  Estimated time remaining to complete simulation: 4 days, 56 minutes, 46 seconds
  Estimated time remaining to next output: 8 minutes, 27 seconds
Output 202/889: t=3120000.0 yr, dE/E0=2.91e-09, N=802
  Estimated time remaining to complete simulation: 4 days, 54 minutes, 3 seconds
  Estimated time remaining to next output: 8 minutes, 27 seconds
Output 203/889: t=3130000.0 yr, dE/E0=5.27e-09, N=802
  Estimated time remaining to complete simulation: 4 days, 49 minutes, 5 seconds
  Estimated time remaining to next output: 8 minutes, 28 seconds
Output 204/889: t=3140000.0 yr, dE/E0=7.72e-09, N=802
  Estimated time remaining to complete simulation: 4 days, 45 minutes, 14 seconds
  Estimated time remaining to next output: 8 minutes, 28 seconds
Output 205/889: t=3150000.0 yr, dE/E0=1.47e-09, N=802
  Estimated time remaining to complete simulation: 4 days, 41 minutes, 4 seconds
  Estimated time remaining to next output: 8 minutes, 28 seconds
Output 206/889: t=3160000.0 yr, dE/E0=1.67e-09, N=802
  Estimated time remaining to complete simulation: 4 days, 37 minutes, 22 seconds
  Estimated time remaining to next output: 8 minutes, 29 seconds
Output 207/889: t=3170000.0 yr, dE/E0=3.70e-09, N=802
  Estimated time remaining to complete simulation: 4 days, 34 minutes, 18 seconds
  Estimated time remaining to next output: 8 minutes, 29 seconds
Output 208/889: t=3180000.0 yr, dE/E0=2.16e-09, N=802
  Estimated time remaining to complete simulation: 4 days, 33 minutes, 19 seconds
  Estimated time remaining to next output: 8 minutes, 30 seconds
Output 209/889: t=3190000.0 yr, dE/E0=9.19e-10, N=802
  Estimated time remaining to complete simulation: 4 days, 31 minutes, 28 seconds
  Estimated time remaining to next output: 8 minutes, 31 seconds
Output 210/889: t=3200000.0 yr, dE/E0=1.89e-09, N=802
  Estimated time remaining to complete simulation: 4 days, 26 minutes, 28 seconds
  Estimated time remaining to next output: 8 minutes, 31 seconds
Output 211/889: t=3210000.0 yr, dE/E0=1.36e-09, N=802
  Estimated time remaining to complete simulation: 4 days, 22 minutes, 57 seconds
  Estimated time remaining to next output: 8 minutes, 31 seconds
Output 212/889: t=3220000.0 yr, dE/E0=4.21e-09, N=802
  Estimated time remaining to complete simulation: 4 days, 17 minutes, 4 seconds
  Estimated time remaining to next output: 8 minutes, 32 seconds
Output 213/889: t=3230000.0 yr, dE/E0=3.04e-09, N=802
  Estimated time remaining to complete simulation: 4 days, 3 minutes, 41 seconds
  Estimated time remaining to next output: 8 minutes, 31 seconds
Output 214/889: t=3240000.0 yr, dE/E0=4.45e-09, N=802
  Estimated time remaining to complete simulation: 3 days, 23 hours, 47 minutes, 27 seconds
  Estimated time remaining to next output: 8 minutes, 30 seconds
Output 215/889: t=3250000.0 yr, dE/E0=5.43e-09, N=802
  Estimated time remaining to complete simulation: 3 days, 23 hours, 32 minutes, 45 seconds
  Estimated time remaining to next output: 8 minutes, 30 seconds
Output 216/889: t=3260000.0 yr, dE/E0=1.53e-09, N=802
  Estimated time remaining to complete simulation: 3 days, 23 hours, 16 minutes, 36 seconds
  Estimated time remaining to next output: 8 minutes, 29 seconds
Output 217/889: t=3270000.0 yr, dE/E0=3.09e-09, N=802
  Estimated time remaining to complete simulation: 3 days, 22 hours, 59 minutes, 55 seconds
  Estimated time remaining to next output: 8 minutes, 28 seconds
Output 218/889: t=3280000.0 yr, dE/E0=9.23e-10, N=802
  Estimated time remaining to complete simulation: 3 days, 22 hours, 44 minutes, 18 seconds
  Estimated time remaining to next output: 8 minutes, 28 seconds
Output 219/889: t=3290000.0 yr, dE/E0=2.26e-09, N=802
  Estimated time remaining to complete simulation: 3 days, 22 hours, 28 minutes, 56 seconds
  Estimated time remaining to next output: 8 minutes, 27 seconds
Output 220/889: t=3300000.0 yr, dE/E0=6.35e-09, N=802
  Estimated time remaining to complete simulation: 3 days, 22 hours, 12 minutes, 57 seconds
  Estimated time remaining to next output: 8 minutes, 26 seconds
Output 221/889: t=3310000.0 yr, dE/E0=1.30e-09, N=802
  Estimated time remaining to complete simulation: 3 days, 21 hours, 57 minutes, 24 seconds
  Estimated time remaining to next output: 8 minutes, 26 seconds
Output 222/889: t=3320000.0 yr, dE/E0=3.37e-09, N=802
  Estimated time remaining to complete simulation: 3 days, 21 hours, 41 minutes, 53 seconds
  Estimated time remaining to next output: 8 minutes, 25 seconds
Output 223/889: t=3330000.0 yr, dE/E0=5.76e-09, N=802
  Estimated time remaining to complete simulation: 3 days, 21 hours, 27 minutes, 11 seconds
  Estimated time remaining to next output: 8 minutes, 25 seconds
Output 224/889: t=3340000.0 yr, dE/E0=1.22e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 21 hours, 11 minutes, 28 seconds
  Estimated time remaining to next output: 8 minutes, 24 seconds
Output 225/889: t=3350000.0 yr, dE/E0=7.57e-09, N=802
  Estimated time remaining to complete simulation: 3 days, 20 hours, 56 minutes, 22 seconds
  Estimated time remaining to next output: 8 minutes, 23 seconds
Output 226/889: t=3360000.0 yr, dE/E0=6.56e-09, N=802
  Estimated time remaining to complete simulation: 3 days, 20 hours, 40 minutes, 41 seconds
  Estimated time remaining to next output: 8 minutes, 23 seconds
Output 227/889: t=3370000.0 yr, dE/E0=3.95e-09, N=802
  Estimated time remaining to complete simulation: 3 days, 20 hours, 26 minutes, 15 seconds
  Estimated time remaining to next output: 8 minutes, 22 seconds
Output 228/889: t=3380000.0 yr, dE/E0=6.66e-10, N=802
  Estimated time remaining to complete simulation: 3 days, 20 hours, 10 minutes, 43 seconds
  Estimated time remaining to next output: 8 minutes, 22 seconds
Output 229/889: t=3390000.0 yr, dE/E0=2.28e-09, N=802
  Estimated time remaining to complete simulation: 3 days, 19 hours, 55 minutes, 8 seconds
  Estimated time remaining to next output: 8 minutes, 21 seconds
Output 230/889: t=3400000.0 yr, dE/E0=4.41e-09, N=802
  Estimated time remaining to complete simulation: 3 days, 19 hours, 40 minutes, 11 seconds
  Estimated time remaining to next output: 8 minutes, 20 seconds
Output 231/889: t=3410000.0 yr, dE/E0=1.41e-09, N=802
  Estimated time remaining to complete simulation: 3 days, 19 hours, 25 minutes, 39 seconds
  Estimated time remaining to next output: 8 minutes, 20 seconds
Output 232/889: t=3420000.0 yr, dE/E0=4.98e-09, N=802
  Estimated time remaining to complete simulation: 3 days, 19 hours, 10 minutes, 29 seconds
  Estimated time remaining to next output: 8 minutes, 19 seconds
Output 233/889: t=3430000.0 yr, dE/E0=1.58e-09, N=802
  Estimated time remaining to complete simulation: 3 days, 18 hours, 56 minutes, 9 seconds
  Estimated time remaining to next output: 8 minutes, 19 seconds
Output 234/889: t=3440000.0 yr, dE/E0=1.85e-09, N=802
  Estimated time remaining to complete simulation: 3 days, 18 hours, 42 minutes, 27 seconds
  Estimated time remaining to next output: 8 minutes, 18 seconds
Output 235/889: t=3450000.0 yr, dE/E0=1.53e-09, N=802
  Estimated time remaining to complete simulation: 3 days, 18 hours, 27 minutes, 16 seconds
  Estimated time remaining to next output: 8 minutes, 17 seconds
Output 236/889: t=3460000.0 yr, dE/E0=8.64e-09, N=802
  Estimated time remaining to complete simulation: 3 days, 18 hours, 13 minutes
  Estimated time remaining to next output: 8 minutes, 17 seconds
Output 237/889: t=3470000.0 yr, dE/E0=9.72e-09, N=802
  Estimated time remaining to complete simulation: 3 days, 17 hours, 59 minutes, 9 seconds
  Estimated time remaining to next output: 8 minutes, 16 seconds
Output 238/889: t=3480000.0 yr, dE/E0=4.10e-09, N=802
  Estimated time remaining to complete simulation: 3 days, 17 hours, 43 minutes, 52 seconds
  Estimated time remaining to next output: 8 minutes, 16 seconds
Output 239/889: t=3490000.0 yr, dE/E0=3.35e-09, N=802
  Estimated time remaining to complete simulation: 3 days, 17 hours, 29 minutes, 15 seconds
  Estimated time remaining to next output: 8 minutes, 15 seconds
Output 240/889: t=3500000.0 yr, dE/E0=1.48e-09, N=802
  Estimated time remaining to complete simulation: 3 days, 17 hours, 15 minutes, 39 seconds
  Estimated time remaining to next output: 8 minutes, 15 seconds
Output 241/889: t=3510000.0 yr, dE/E0=1.51e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 17 hours, 1 minutes, 23 seconds
  Estimated time remaining to next output: 8 minutes, 14 seconds
Output 242/889: t=3520000.0 yr, dE/E0=6.22e-10, N=802
  Estimated time remaining to complete simulation: 3 days, 16 hours, 48 minutes, 40 seconds
  Estimated time remaining to next output: 8 minutes, 14 seconds
Output 243/889: t=3530000.0 yr, dE/E0=7.70e-09, N=802
  Estimated time remaining to complete simulation: 3 days, 16 hours, 34 minutes, 11 seconds
  Estimated time remaining to next output: 8 minutes, 13 seconds
Output 244/889: t=3540000.0 yr, dE/E0=1.83e-09, N=802
  Estimated time remaining to complete simulation: 3 days, 16 hours, 20 minutes, 5 seconds
  Estimated time remaining to next output: 8 minutes, 13 seconds
Output 245/889: t=3550000.0 yr, dE/E0=2.71e-09, N=802
  Estimated time remaining to complete simulation: 3 days, 16 hours, 6 minutes, 26 seconds
  Estimated time remaining to next output: 8 minutes, 12 seconds
Output 246/889: t=3560000.0 yr, dE/E0=3.91e-09, N=802
  Estimated time remaining to complete simulation: 3 days, 15 hours, 52 minutes, 41 seconds
  Estimated time remaining to next output: 8 minutes, 12 seconds
Output 247/889: t=3570000.0 yr, dE/E0=7.09e-09, N=802
  Estimated time remaining to complete simulation: 3 days, 15 hours, 38 minutes, 35 seconds
  Estimated time remaining to next output: 8 minutes, 11 seconds
Output 248/889: t=3580000.0 yr, dE/E0=1.14e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 15 hours, 25 minutes, 36 seconds
  Estimated time remaining to next output: 8 minutes, 11 seconds
Output 249/889: t=3590000.0 yr, dE/E0=6.52e-09, N=802
  Estimated time remaining to complete simulation: 3 days, 15 hours, 12 minutes, 17 seconds
  Estimated time remaining to next output: 8 minutes, 10 seconds
Output 250/889: t=3600000.0 yr, dE/E0=3.51e-09, N=802
  Estimated time remaining to complete simulation: 3 days, 14 hours, 59 minutes, 28 seconds
  Estimated time remaining to next output: 8 minutes, 10 seconds
Output 251/889: t=3610000.0 yr, dE/E0=2.11e-09, N=802
  Estimated time remaining to complete simulation: 3 days, 14 hours, 46 minutes, 27 seconds
  Estimated time remaining to next output: 8 minutes, 9 seconds
Output 252/889: t=3620000.0 yr, dE/E0=1.27e-09, N=802
  Estimated time remaining to complete simulation: 3 days, 14 hours, 32 minutes, 59 seconds
  Estimated time remaining to next output: 8 minutes, 9 seconds
Output 253/889: t=3630000.0 yr, dE/E0=8.98e-10, N=802
  Estimated time remaining to complete simulation: 3 days, 14 hours, 19 minutes, 13 seconds
  Estimated time remaining to next output: 8 minutes, 8 seconds
Output 254/889: t=3640000.0 yr, dE/E0=1.15e-09, N=802
  Estimated time remaining to complete simulation: 3 days, 14 hours, 5 minutes, 59 seconds
  Estimated time remaining to next output: 8 minutes, 8 seconds
Output 255/889: t=3650000.0 yr, dE/E0=4.50e-09, N=802
  Estimated time remaining to complete simulation: 3 days, 13 hours, 52 minutes, 34 seconds
  Estimated time remaining to next output: 8 minutes, 7 seconds
Output 256/889: t=3660000.0 yr, dE/E0=1.32e-09, N=802
  Estimated time remaining to complete simulation: 3 days, 13 hours, 39 minutes, 5 seconds
  Estimated time remaining to next output: 8 minutes, 7 seconds
Output 257/889: t=3670000.0 yr, dE/E0=1.19e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 13 hours, 25 minutes, 19 seconds
  Estimated time remaining to next output: 8 minutes, 6 seconds
Output 258/889: t=3680000.0 yr, dE/E0=1.09e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 13 hours, 12 minutes, 33 seconds
  Estimated time remaining to next output: 8 minutes, 6 seconds
Output 259/889: t=3690000.0 yr, dE/E0=8.36e-09, N=802
  Estimated time remaining to complete simulation: 3 days, 12 hours, 59 minutes, 46 seconds
  Estimated time remaining to next output: 8 minutes, 5 seconds
Output 260/889: t=3700000.0 yr, dE/E0=1.17e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 12 hours, 46 minutes, 53 seconds
  Estimated time remaining to next output: 8 minutes, 5 seconds
Output 261/889: t=3710000.0 yr, dE/E0=1.46e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 12 hours, 34 minutes, 33 seconds
  Estimated time remaining to next output: 8 minutes, 4 seconds
Output 262/889: t=3720000.0 yr, dE/E0=2.29e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 12 hours, 21 minutes, 52 seconds
  Estimated time remaining to next output: 8 minutes, 4 seconds
Output 263/889: t=3730000.0 yr, dE/E0=1.85e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 12 hours, 9 minutes, 18 seconds
  Estimated time remaining to next output: 8 minutes, 3 seconds
Output 264/889: t=3740000.0 yr, dE/E0=2.15e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 11 hours, 57 minutes, 3 seconds
  Estimated time remaining to next output: 8 minutes, 3 seconds
Output 265/889: t=3750000.0 yr, dE/E0=2.53e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 11 hours, 44 minutes, 42 seconds
  Estimated time remaining to next output: 8 minutes, 3 seconds
Output 266/889: t=3760000.0 yr, dE/E0=1.99e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 11 hours, 38 minutes, 16 seconds
  Estimated time remaining to next output: 8 minutes, 3 seconds
Output 267/889: t=3770000.0 yr, dE/E0=2.28e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 11 hours, 34 minutes, 27 seconds
  Estimated time remaining to next output: 8 minutes, 3 seconds
Output 268/889: t=3780000.0 yr, dE/E0=3.25e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 11 hours, 30 minutes, 36 seconds
  Estimated time remaining to next output: 8 minutes, 4 seconds
Output 269/889: t=3790000.0 yr, dE/E0=2.04e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 11 hours, 27 minutes, 18 seconds
  Estimated time remaining to next output: 8 minutes, 4 seconds
Output 270/889: t=3800000.0 yr, dE/E0=2.84e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 11 hours, 23 minutes, 23 seconds
  Estimated time remaining to next output: 8 minutes, 4 seconds
Output 271/889: t=3810000.0 yr, dE/E0=2.35e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 11 hours, 19 minutes, 48 seconds
  Estimated time remaining to next output: 8 minutes, 5 seconds
Output 272/889: t=3820000.0 yr, dE/E0=2.29e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 11 hours, 14 minutes, 42 seconds
  Estimated time remaining to next output: 8 minutes, 5 seconds
Output 273/889: t=3830000.0 yr, dE/E0=2.15e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 11 hours, 9 minutes, 49 seconds
  Estimated time remaining to next output: 8 minutes, 6 seconds
Output 274/889: t=3840000.0 yr, dE/E0=2.08e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 11 hours, 5 minutes, 57 seconds
  Estimated time remaining to next output: 8 minutes, 6 seconds
Output 275/889: t=3850000.0 yr, dE/E0=2.82e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 11 hours, 1 minutes, 42 seconds
  Estimated time remaining to next output: 8 minutes, 6 seconds
Output 276/889: t=3860000.0 yr, dE/E0=2.60e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 10 hours, 57 minutes, 56 seconds
  Estimated time remaining to next output: 8 minutes, 7 seconds
Output 277/889: t=3870000.0 yr, dE/E0=2.25e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 10 hours, 56 minutes, 15 seconds
  Estimated time remaining to next output: 8 minutes, 7 seconds
Output 278/889: t=3880000.0 yr, dE/E0=3.03e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 10 hours, 51 minutes, 26 seconds
  Estimated time remaining to next output: 8 minutes, 8 seconds
Output 279/889: t=3890000.0 yr, dE/E0=2.11e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 10 hours, 46 minutes, 13 seconds
  Estimated time remaining to next output: 8 minutes, 8 seconds
Output 280/889: t=3900000.0 yr, dE/E0=2.87e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 10 hours, 41 minutes, 21 seconds
  Estimated time remaining to next output: 8 minutes, 8 seconds
Output 281/889: t=3910000.0 yr, dE/E0=2.90e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 10 hours, 36 minutes, 48 seconds
  Estimated time remaining to next output: 8 minutes, 9 seconds
Output 282/889: t=3920000.0 yr, dE/E0=2.47e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 10 hours, 32 minutes, 42 seconds
  Estimated time remaining to next output: 8 minutes, 9 seconds
Output 283/889: t=3930000.0 yr, dE/E0=3.54e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 10 hours, 28 minutes, 58 seconds
  Estimated time remaining to next output: 8 minutes, 9 seconds
Output 284/889: t=3940000.0 yr, dE/E0=3.49e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 10 hours, 24 minutes, 7 seconds
  Estimated time remaining to next output: 8 minutes, 10 seconds
Output 285/889: t=3950000.0 yr, dE/E0=3.04e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 10 hours, 19 minutes, 35 seconds
  Estimated time remaining to next output: 8 minutes, 10 seconds
Output 286/889: t=3960000.0 yr, dE/E0=3.23e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 10 hours, 14 minutes, 35 seconds
  Estimated time remaining to next output: 8 minutes, 11 seconds
Output 287/889: t=3970000.0 yr, dE/E0=3.97e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 10 hours, 10 minutes, 28 seconds
  Estimated time remaining to next output: 8 minutes, 11 seconds
Output 288/889: t=3980000.0 yr, dE/E0=3.97e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 10 hours, 6 minutes, 56 seconds
  Estimated time remaining to next output: 8 minutes, 11 seconds
Output 289/889: t=3990000.0 yr, dE/E0=3.39e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 10 hours, 3 minutes, 31 seconds
  Estimated time remaining to next output: 8 minutes, 12 seconds
Output 290/889: t=4000000.0 yr, dE/E0=2.44e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 9 hours, 58 minutes, 36 seconds
  Estimated time remaining to next output: 8 minutes, 12 seconds
Output 291/889: t=4010000.0 yr, dE/E0=3.00e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 9 hours, 53 minutes, 50 seconds
  Estimated time remaining to next output: 8 minutes, 13 seconds
Output 292/889: t=4020000.0 yr, dE/E0=3.84e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 9 hours, 49 minutes, 22 seconds
  Estimated time remaining to next output: 8 minutes, 13 seconds
Output 293/889: t=4030000.0 yr, dE/E0=5.20e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 9 hours, 44 minutes, 54 seconds
  Estimated time remaining to next output: 8 minutes, 13 seconds
Output 294/889: t=4040000.0 yr, dE/E0=4.64e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 9 hours, 40 minutes, 18 seconds
  Estimated time remaining to next output: 8 minutes, 14 seconds
Output 295/889: t=4050000.0 yr, dE/E0=5.11e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 9 hours, 35 minutes, 39 seconds
  Estimated time remaining to next output: 8 minutes, 14 seconds
Output 296/889: t=4060000.0 yr, dE/E0=5.23e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 9 hours, 31 minutes, 14 seconds
  Estimated time remaining to next output: 8 minutes, 14 seconds
Output 297/889: t=4070000.0 yr, dE/E0=5.25e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 9 hours, 25 minutes, 46 seconds
  Estimated time remaining to next output: 8 minutes, 15 seconds
Output 298/889: t=4080000.0 yr, dE/E0=5.21e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 9 hours, 21 minutes, 28 seconds
  Estimated time remaining to next output: 8 minutes, 15 seconds
Output 299/889: t=4090000.0 yr, dE/E0=4.53e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 9 hours, 16 minutes, 43 seconds
  Estimated time remaining to next output: 8 minutes, 15 seconds
Output 300/889: t=4100000.0 yr, dE/E0=4.79e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 9 hours, 11 minutes, 54 seconds
  Estimated time remaining to next output: 8 minutes, 16 seconds
Output 301/889: t=4110000.0 yr, dE/E0=5.07e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 9 hours, 6 minutes, 39 seconds
  Estimated time remaining to next output: 8 minutes, 16 seconds
Output 302/889: t=4120000.0 yr, dE/E0=5.33e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 9 hours, 2 minutes, 3 seconds
  Estimated time remaining to next output: 8 minutes, 16 seconds
Output 303/889: t=4130000.0 yr, dE/E0=5.33e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 8 hours, 56 minutes, 34 seconds
  Estimated time remaining to next output: 8 minutes, 17 seconds
Output 304/889: t=4140000.0 yr, dE/E0=6.20e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 8 hours, 51 minutes, 28 seconds
  Estimated time remaining to next output: 8 minutes, 17 seconds
Output 305/889: t=4150000.0 yr, dE/E0=5.48e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 8 hours, 46 minutes, 22 seconds
  Estimated time remaining to next output: 8 minutes, 17 seconds
Output 306/889: t=4160000.0 yr, dE/E0=5.34e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 8 hours, 41 minutes, 45 seconds
  Estimated time remaining to next output: 8 minutes, 18 seconds
Output 307/889: t=4170000.0 yr, dE/E0=5.76e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 8 hours, 37 minutes, 3 seconds
  Estimated time remaining to next output: 8 minutes, 18 seconds
Output 308/889: t=4180000.0 yr, dE/E0=5.43e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 8 hours, 32 minutes, 46 seconds
  Estimated time remaining to next output: 8 minutes, 19 seconds
Output 309/889: t=4190000.0 yr, dE/E0=4.87e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 8 hours, 26 minutes, 9 seconds
  Estimated time remaining to next output: 8 minutes, 19 seconds
Output 310/889: t=4200000.0 yr, dE/E0=4.82e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 8 hours, 20 minutes, 31 seconds
  Estimated time remaining to next output: 8 minutes, 19 seconds
Output 311/889: t=4210000.0 yr, dE/E0=5.86e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 8 hours, 14 minutes, 56 seconds
  Estimated time remaining to next output: 8 minutes, 19 seconds
Output 312/889: t=4220000.0 yr, dE/E0=5.13e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 8 hours, 9 minutes, 36 seconds
  Estimated time remaining to next output: 8 minutes, 20 seconds
Output 313/889: t=4230000.0 yr, dE/E0=4.34e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 8 hours, 3 minutes, 54 seconds
  Estimated time remaining to next output: 8 minutes, 20 seconds
Output 314/889: t=4240000.0 yr, dE/E0=5.57e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 7 hours, 58 minutes, 2 seconds
  Estimated time remaining to next output: 8 minutes, 20 seconds
Output 315/889: t=4250000.0 yr, dE/E0=5.28e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 7 hours, 52 minutes, 15 seconds
  Estimated time remaining to next output: 8 minutes, 20 seconds
Output 316/889: t=4260000.0 yr, dE/E0=4.48e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 7 hours, 45 minutes, 20 seconds
  Estimated time remaining to next output: 8 minutes, 21 seconds
Output 317/889: t=4270000.0 yr, dE/E0=4.97e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 7 hours, 40 minutes, 28 seconds
  Estimated time remaining to next output: 8 minutes, 21 seconds
Output 318/889: t=4280000.0 yr, dE/E0=4.19e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 7 hours, 30 minutes, 41 seconds
  Estimated time remaining to next output: 8 minutes, 21 seconds
Output 319/889: t=4290000.0 yr, dE/E0=4.60e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 7 hours, 17 minutes, 46 seconds
  Estimated time remaining to next output: 8 minutes, 20 seconds
Output 320/889: t=4300000.0 yr, dE/E0=4.98e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 7 hours, 5 minutes, 44 seconds
  Estimated time remaining to next output: 8 minutes, 20 seconds
Output 321/889: t=4310000.0 yr, dE/E0=3.98e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 6 hours, 53 minutes, 40 seconds
  Estimated time remaining to next output: 8 minutes, 20 seconds
Output 322/889: t=4320000.0 yr, dE/E0=3.59e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 6 hours, 41 minutes, 58 seconds
  Estimated time remaining to next output: 8 minutes, 19 seconds
Output 323/889: t=4330000.0 yr, dE/E0=5.07e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 6 hours, 29 minutes, 56 seconds
  Estimated time remaining to next output: 8 minutes, 19 seconds
Output 324/889: t=4340000.0 yr, dE/E0=4.87e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 6 hours, 18 minutes, 3 seconds
  Estimated time remaining to next output: 8 minutes, 18 seconds
Output 325/889: t=4350000.0 yr, dE/E0=5.06e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 6 hours, 5 minutes, 50 seconds
  Estimated time remaining to next output: 8 minutes, 18 seconds
Output 326/889: t=4360000.0 yr, dE/E0=5.31e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 5 hours, 53 minutes, 51 seconds
  Estimated time remaining to next output: 8 minutes, 18 seconds
Output 327/889: t=4370000.0 yr, dE/E0=5.27e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 5 hours, 41 minutes, 27 seconds
  Estimated time remaining to next output: 8 minutes, 17 seconds
Output 328/889: t=4380000.0 yr, dE/E0=6.34e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 5 hours, 29 minutes, 12 seconds
  Estimated time remaining to next output: 8 minutes, 17 seconds
Output 329/889: t=4390000.0 yr, dE/E0=6.96e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 5 hours, 18 minutes, 6 seconds
  Estimated time remaining to next output: 8 minutes, 16 seconds
Output 330/889: t=4400000.0 yr, dE/E0=6.21e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 5 hours, 6 minutes, 19 seconds
  Estimated time remaining to next output: 8 minutes, 16 seconds
Output 331/889: t=4410000.0 yr, dE/E0=5.85e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 4 hours, 53 minutes, 16 seconds
  Estimated time remaining to next output: 8 minutes, 16 seconds
Output 332/889: t=4420000.0 yr, dE/E0=6.46e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 4 hours, 44 minutes, 11 seconds
  Estimated time remaining to next output: 8 minutes, 15 seconds
Output 333/889: t=4430000.0 yr, dE/E0=7.48e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 4 hours, 39 minutes, 4 seconds
  Estimated time remaining to next output: 8 minutes, 16 seconds
Output 334/889: t=4440000.0 yr, dE/E0=8.22e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 4 hours, 33 minutes, 45 seconds
  Estimated time remaining to next output: 8 minutes, 16 seconds
Output 335/889: t=4450000.0 yr, dE/E0=6.39e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 4 hours, 29 minutes, 21 seconds
  Estimated time remaining to next output: 8 minutes, 17 seconds
Output 336/889: t=4460000.0 yr, dE/E0=6.32e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 4 hours, 23 minutes, 8 seconds
  Estimated time remaining to next output: 8 minutes, 17 seconds
Output 337/889: t=4470000.0 yr, dE/E0=6.56e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 4 hours, 18 minutes, 17 seconds
  Estimated time remaining to next output: 8 minutes, 17 seconds
Output 338/889: t=4480000.0 yr, dE/E0=6.78e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 4 hours, 12 minutes, 41 seconds
  Estimated time remaining to next output: 8 minutes, 17 seconds
Output 339/889: t=4490000.0 yr, dE/E0=5.95e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 4 hours, 7 minutes, 28 seconds
  Estimated time remaining to next output: 8 minutes, 18 seconds
Output 340/889: t=4500000.0 yr, dE/E0=5.79e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 4 hours, 2 minutes, 3 seconds
  Estimated time remaining to next output: 8 minutes, 18 seconds
Output 341/889: t=4510000.0 yr, dE/E0=7.00e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 3 hours, 57 minutes, 5 seconds
  Estimated time remaining to next output: 8 minutes, 18 seconds
Output 342/889: t=4520000.0 yr, dE/E0=6.40e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 3 hours, 52 minutes, 10 seconds
  Estimated time remaining to next output: 8 minutes, 19 seconds
Output 343/889: t=4530000.0 yr, dE/E0=5.70e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 3 hours, 41 minutes, 57 seconds
  Estimated time remaining to next output: 8 minutes, 19 seconds
Output 344/889: t=4540000.0 yr, dE/E0=5.39e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 3 hours, 30 minutes, 27 seconds
  Estimated time remaining to next output: 8 minutes, 18 seconds
Output 345/889: t=4550000.0 yr, dE/E0=5.72e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 3 hours, 18 minutes, 47 seconds
  Estimated time remaining to next output: 8 minutes, 18 seconds
Output 346/889: t=4560000.0 yr, dE/E0=6.62e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 3 hours, 6 minutes, 53 seconds
  Estimated time remaining to next output: 8 minutes, 17 seconds
Output 347/889: t=4570000.0 yr, dE/E0=5.58e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 2 hours, 54 minutes, 34 seconds
  Estimated time remaining to next output: 8 minutes, 17 seconds
Output 348/889: t=4580000.0 yr, dE/E0=5.74e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 2 hours, 42 minutes, 48 seconds
  Estimated time remaining to next output: 8 minutes, 17 seconds
Output 349/889: t=4590000.0 yr, dE/E0=5.53e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 2 hours, 31 minutes, 2 seconds
  Estimated time remaining to next output: 8 minutes, 16 seconds
Output 350/889: t=4600000.0 yr, dE/E0=5.66e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 2 hours, 19 minutes, 6 seconds
  Estimated time remaining to next output: 8 minutes, 16 seconds
Output 351/889: t=4610000.0 yr, dE/E0=5.36e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 2 hours, 7 minutes, 39 seconds
  Estimated time remaining to next output: 8 minutes, 16 seconds
Output 352/889: t=4620000.0 yr, dE/E0=5.78e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 1 hours, 56 minutes, 4 seconds
  Estimated time remaining to next output: 8 minutes, 15 seconds
Output 353/889: t=4630000.0 yr, dE/E0=5.71e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 1 hours, 44 minutes, 16 seconds
  Estimated time remaining to next output: 8 minutes, 15 seconds
Output 354/889: t=4640000.0 yr, dE/E0=6.20e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 1 hours, 32 minutes, 54 seconds
  Estimated time remaining to next output: 8 minutes, 14 seconds
Output 355/889: t=4650000.0 yr, dE/E0=7.05e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 1 hours, 21 minutes, 54 seconds
  Estimated time remaining to next output: 8 minutes, 14 seconds
Output 356/889: t=4660000.0 yr, dE/E0=6.59e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 1 hours, 10 minutes, 18 seconds
  Estimated time remaining to next output: 8 minutes, 14 seconds
Output 357/889: t=4670000.0 yr, dE/E0=5.96e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 58 minutes, 48 seconds
  Estimated time remaining to next output: 8 minutes, 13 seconds
Output 358/889: t=4680000.0 yr, dE/E0=6.34e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 47 minutes, 51 seconds
  Estimated time remaining to next output: 8 minutes, 13 seconds
Output 359/889: t=4690000.0 yr, dE/E0=6.60e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 36 minutes, 18 seconds
  Estimated time remaining to next output: 8 minutes, 13 seconds
Output 360/889: t=4700000.0 yr, dE/E0=6.30e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 24 minutes, 58 seconds
  Estimated time remaining to next output: 8 minutes, 12 seconds
Output 361/889: t=4710000.0 yr, dE/E0=6.67e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 13 minutes, 42 seconds
  Estimated time remaining to next output: 8 minutes, 12 seconds
Output 362/889: t=4720000.0 yr, dE/E0=6.19e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 1 minutes, 48 seconds
  Estimated time remaining to next output: 8 minutes, 12 seconds
Output 363/889: t=4730000.0 yr, dE/E0=5.48e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 23 hours, 50 minutes, 42 seconds
  Estimated time remaining to next output: 8 minutes, 11 seconds
Output 364/889: t=4740000.0 yr, dE/E0=5.89e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 23 hours, 40 minutes, 15 seconds
  Estimated time remaining to next output: 8 minutes, 11 seconds
Output 365/889: t=4750000.0 yr, dE/E0=5.52e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 23 hours, 29 minutes, 38 seconds
  Estimated time remaining to next output: 8 minutes, 11 seconds
Output 366/889: t=4760000.0 yr, dE/E0=5.79e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 23 hours, 18 minutes, 55 seconds
  Estimated time remaining to next output: 8 minutes, 10 seconds
Output 367/889: t=4770000.0 yr, dE/E0=4.63e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 23 hours, 8 minutes, 34 seconds
  Estimated time remaining to next output: 8 minutes, 10 seconds
Output 368/889: t=4780000.0 yr, dE/E0=5.65e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 22 hours, 57 minutes, 34 seconds
  Estimated time remaining to next output: 8 minutes, 10 seconds
Output 369/889: t=4790000.0 yr, dE/E0=5.60e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 22 hours, 46 minutes, 43 seconds
  Estimated time remaining to next output: 8 minutes, 10 seconds
Output 370/889: t=4800000.0 yr, dE/E0=5.53e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 22 hours, 36 minutes, 2 seconds
  Estimated time remaining to next output: 8 minutes, 9 seconds
Output 371/889: t=4810000.0 yr, dE/E0=6.01e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 22 hours, 24 minutes, 52 seconds
  Estimated time remaining to next output: 8 minutes, 9 seconds
Output 372/889: t=4820000.0 yr, dE/E0=6.59e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 22 hours, 14 minutes, 28 seconds
  Estimated time remaining to next output: 8 minutes, 9 seconds
Output 373/889: t=4830000.0 yr, dE/E0=5.59e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 22 hours, 3 minutes, 49 seconds
  Estimated time remaining to next output: 8 minutes, 8 seconds
Output 374/889: t=4840000.0 yr, dE/E0=6.20e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 21 hours, 54 minutes
  Estimated time remaining to next output: 8 minutes, 8 seconds
Output 375/889: t=4850000.0 yr, dE/E0=4.80e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 21 hours, 47 minutes, 28 seconds
  Estimated time remaining to next output: 8 minutes, 8 seconds
Output 376/889: t=4860000.0 yr, dE/E0=5.62e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 21 hours, 40 minutes, 58 seconds
  Estimated time remaining to next output: 8 minutes, 9 seconds
Output 377/889: t=4870000.0 yr, dE/E0=5.59e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 21 hours, 34 minutes, 29 seconds
  Estimated time remaining to next output: 8 minutes, 9 seconds
Output 378/889: t=4880000.0 yr, dE/E0=6.14e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 21 hours, 28 minutes, 5 seconds
  Estimated time remaining to next output: 8 minutes, 9 seconds
Output 379/889: t=4890000.0 yr, dE/E0=5.32e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 21 hours, 16 minutes, 27 seconds
  Estimated time remaining to next output: 8 minutes, 8 seconds
Output 380/889: t=4900000.0 yr, dE/E0=4.70e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 21 hours, 5 minutes, 5 seconds
  Estimated time remaining to next output: 8 minutes, 8 seconds
Output 381/889: t=4910000.0 yr, dE/E0=4.39e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 20 hours, 54 minutes, 7 seconds
  Estimated time remaining to next output: 8 minutes, 8 seconds
Output 382/889: t=4920000.0 yr, dE/E0=4.78e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 20 hours, 43 minutes, 19 seconds
  Estimated time remaining to next output: 8 minutes, 7 seconds
Output 383/889: t=4930000.0 yr, dE/E0=5.35e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 20 hours, 31 minutes, 44 seconds
  Estimated time remaining to next output: 8 minutes, 7 seconds
Output 384/889: t=4940000.0 yr, dE/E0=4.95e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 20 hours, 20 minutes, 50 seconds
  Estimated time remaining to next output: 8 minutes, 7 seconds
Output 385/889: t=4950000.0 yr, dE/E0=5.02e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 20 hours, 9 minutes, 51 seconds
  Estimated time remaining to next output: 8 minutes, 6 seconds
Output 386/889: t=4960000.0 yr, dE/E0=6.30e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 19 hours, 58 minutes, 36 seconds
  Estimated time remaining to next output: 8 minutes, 6 seconds
Output 387/889: t=4970000.0 yr, dE/E0=5.53e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 19 hours, 47 minutes, 47 seconds
  Estimated time remaining to next output: 8 minutes, 6 seconds
Output 388/889: t=4980000.0 yr, dE/E0=5.07e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 19 hours, 36 minutes, 45 seconds
  Estimated time remaining to next output: 8 minutes, 5 seconds
Output 389/889: t=4990000.0 yr, dE/E0=3.91e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 19 hours, 26 minutes, 5 seconds
  Estimated time remaining to next output: 8 minutes, 5 seconds
Output 390/889: t=5000000.0 yr, dE/E0=3.30e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 19 hours, 15 minutes, 13 seconds
  Estimated time remaining to next output: 8 minutes, 5 seconds
Output 391/889: t=5010000.0 yr, dE/E0=3.84e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 19 hours, 4 minutes, 25 seconds
  Estimated time remaining to next output: 8 minutes, 4 seconds
Output 392/889: t=5020000.0 yr, dE/E0=3.19e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 18 hours, 53 minutes, 54 seconds
  Estimated time remaining to next output: 8 minutes, 4 seconds
Output 393/889: t=5030000.0 yr, dE/E0=3.66e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 18 hours, 43 minutes, 34 seconds
  Estimated time remaining to next output: 8 minutes, 4 seconds
Output 394/889: t=5040000.0 yr, dE/E0=4.27e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 18 hours, 32 minutes, 54 seconds
  Estimated time remaining to next output: 8 minutes, 3 seconds
Output 395/889: t=5050000.0 yr, dE/E0=4.53e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 18 hours, 22 minutes, 2 seconds
  Estimated time remaining to next output: 8 minutes, 3 seconds
Output 396/889: t=5060000.0 yr, dE/E0=3.21e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 18 hours, 11 minutes, 10 seconds
  Estimated time remaining to next output: 8 minutes, 3 seconds
Output 397/889: t=5070000.0 yr, dE/E0=2.37e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 18 hours, 11 seconds
  Estimated time remaining to next output: 8 minutes, 2 seconds
Output 398/889: t=5080000.0 yr, dE/E0=2.37e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 17 hours, 48 minutes, 58 seconds
  Estimated time remaining to next output: 8 minutes, 2 seconds
Output 399/889: t=5090000.0 yr, dE/E0=3.41e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 17 hours, 38 minutes, 51 seconds
  Estimated time remaining to next output: 8 minutes, 2 seconds
Output 400/889: t=5100000.0 yr, dE/E0=3.59e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 17 hours, 27 minutes, 57 seconds
  Estimated time remaining to next output: 8 minutes, 1 seconds
Output 401/889: t=5110000.0 yr, dE/E0=3.27e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 17 hours, 17 minutes, 4 seconds
  Estimated time remaining to next output: 8 minutes, 1 seconds
Output 402/889: t=5120000.0 yr, dE/E0=3.19e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 17 hours, 6 minutes, 31 seconds
  Estimated time remaining to next output: 8 minutes, 1 seconds
Output 403/889: t=5130000.0 yr, dE/E0=3.99e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 16 hours, 56 minutes, 31 seconds
  Estimated time remaining to next output: 8 minutes, 1 seconds
Output 404/889: t=5140000.0 yr, dE/E0=4.34e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 16 hours, 46 minutes, 23 seconds
  Estimated time remaining to next output: 8 minutes
Output 405/889: t=5150000.0 yr, dE/E0=3.87e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 16 hours, 35 minutes, 31 seconds
  Estimated time remaining to next output: 8 minutes
Output 406/889: t=5160000.0 yr, dE/E0=3.58e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 16 hours, 25 minutes, 8 seconds
  Estimated time remaining to next output: 8 minutes
Output 407/889: t=5170000.0 yr, dE/E0=3.50e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 16 hours, 14 minutes, 15 seconds
  Estimated time remaining to next output: 7 minutes, 59 seconds
Output 408/889: t=5180000.0 yr, dE/E0=3.19e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 16 hours, 3 minutes, 49 seconds
  Estimated time remaining to next output: 7 minutes, 59 seconds
Output 409/889: t=5190000.0 yr, dE/E0=3.14e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 15 hours, 53 minutes, 12 seconds
  Estimated time remaining to next output: 7 minutes, 59 seconds
Output 410/889: t=5200000.0 yr, dE/E0=2.09e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 15 hours, 42 minutes, 43 seconds
  Estimated time remaining to next output: 7 minutes, 58 seconds
Output 411/889: t=5210000.0 yr, dE/E0=2.31e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 15 hours, 32 minutes, 6 seconds
  Estimated time remaining to next output: 7 minutes, 58 seconds
Output 412/889: t=5220000.0 yr, dE/E0=2.34e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 15 hours, 21 minutes, 46 seconds
  Estimated time remaining to next output: 7 minutes, 58 seconds
Output 413/889: t=5230000.0 yr, dE/E0=3.96e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 15 hours, 11 minutes, 46 seconds
  Estimated time remaining to next output: 7 minutes, 57 seconds
Output 414/889: t=5240000.0 yr, dE/E0=5.00e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 15 hours, 1 minutes, 26 seconds
  Estimated time remaining to next output: 7 minutes, 57 seconds
Output 415/889: t=5250000.0 yr, dE/E0=4.47e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 14 hours, 51 minutes, 22 seconds
  Estimated time remaining to next output: 7 minutes, 57 seconds
Output 416/889: t=5260000.0 yr, dE/E0=4.45e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 14 hours, 41 minutes, 16 seconds
  Estimated time remaining to next output: 7 minutes, 57 seconds
Output 417/889: t=5270000.0 yr, dE/E0=3.93e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 14 hours, 31 minutes, 10 seconds
  Estimated time remaining to next output: 7 minutes, 56 seconds
Output 418/889: t=5280000.0 yr, dE/E0=4.39e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 14 hours, 21 minutes, 6 seconds
  Estimated time remaining to next output: 7 minutes, 56 seconds
Output 419/889: t=5290000.0 yr, dE/E0=5.24e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 14 hours, 10 minutes, 59 seconds
  Estimated time remaining to next output: 7 minutes, 56 seconds
Output 420/889: t=5300000.0 yr, dE/E0=4.44e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 14 hours, 47 seconds
  Estimated time remaining to next output: 7 minutes, 56 seconds
Output 421/889: t=5310000.0 yr, dE/E0=4.30e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 13 hours, 50 minutes, 23 seconds
  Estimated time remaining to next output: 7 minutes, 55 seconds
Output 422/889: t=5320000.0 yr, dE/E0=4.42e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 13 hours, 40 minutes, 13 seconds
  Estimated time remaining to next output: 7 minutes, 55 seconds
Output 423/889: t=5330000.0 yr, dE/E0=2.63e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 13 hours, 30 minutes, 25 seconds
  Estimated time remaining to next output: 7 minutes, 55 seconds
Output 424/889: t=5340000.0 yr, dE/E0=3.09e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 13 hours, 20 minutes, 23 seconds
  Estimated time remaining to next output: 7 minutes, 54 seconds
Output 425/889: t=5350000.0 yr, dE/E0=4.65e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 13 hours, 10 minutes, 6 seconds
  Estimated time remaining to next output: 7 minutes, 54 seconds
Output 426/889: t=5360000.0 yr, dE/E0=3.36e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 12 hours, 59 minutes, 57 seconds
  Estimated time remaining to next output: 7 minutes, 54 seconds
Output 427/889: t=5370000.0 yr, dE/E0=3.56e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 12 hours, 49 minutes, 33 seconds
  Estimated time remaining to next output: 7 minutes, 53 seconds
Output 428/889: t=5380000.0 yr, dE/E0=3.74e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 12 hours, 39 minutes, 47 seconds
  Estimated time remaining to next output: 7 minutes, 53 seconds
Output 429/889: t=5390000.0 yr, dE/E0=3.15e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 12 hours, 30 minutes
  Estimated time remaining to next output: 7 minutes, 53 seconds
Output 430/889: t=5400000.0 yr, dE/E0=4.27e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 12 hours, 20 minutes, 13 seconds
  Estimated time remaining to next output: 7 minutes, 53 seconds
Output 431/889: t=5410000.0 yr, dE/E0=3.47e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 12 hours, 10 minutes, 21 seconds
  Estimated time remaining to next output: 7 minutes, 52 seconds
Output 432/889: t=5420000.0 yr, dE/E0=3.87e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 12 hours, 27 seconds
  Estimated time remaining to next output: 7 minutes, 52 seconds
Output 433/889: t=5430000.0 yr, dE/E0=4.23e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 11 hours, 50 minutes, 50 seconds
  Estimated time remaining to next output: 7 minutes, 52 seconds
Output 434/889: t=5440000.0 yr, dE/E0=3.43e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 11 hours, 40 minutes, 29 seconds
  Estimated time remaining to next output: 7 minutes, 52 seconds
Output 435/889: t=5450000.0 yr, dE/E0=4.82e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 11 hours, 30 minutes, 40 seconds
  Estimated time remaining to next output: 7 minutes, 51 seconds
Output 436/889: t=5460000.0 yr, dE/E0=3.89e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 11 hours, 20 minutes, 50 seconds
  Estimated time remaining to next output: 7 minutes, 51 seconds
Output 437/889: t=5470000.0 yr, dE/E0=3.96e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 11 hours, 11 minutes, 22 seconds
  Estimated time remaining to next output: 7 minutes, 51 seconds
Output 438/889: t=5480000.0 yr, dE/E0=3.39e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 11 hours, 1 minutes, 36 seconds
  Estimated time remaining to next output: 7 minutes, 51 seconds
Output 439/889: t=5490000.0 yr, dE/E0=2.94e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 10 hours, 52 minutes, 10 seconds
  Estimated time remaining to next output: 7 minutes, 50 seconds
Output 440/889: t=5500000.0 yr, dE/E0=3.45e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 10 hours, 42 minutes, 33 seconds
  Estimated time remaining to next output: 7 minutes, 50 seconds
Output 441/889: t=5510000.0 yr, dE/E0=2.96e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 10 hours, 33 minutes, 1 seconds
  Estimated time remaining to next output: 7 minutes, 50 seconds
Output 442/889: t=5520000.0 yr, dE/E0=3.00e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 10 hours, 23 minutes, 17 seconds
  Estimated time remaining to next output: 7 minutes, 50 seconds
Output 443/889: t=5530000.0 yr, dE/E0=3.34e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 10 hours, 13 minutes, 42 seconds
  Estimated time remaining to next output: 7 minutes, 50 seconds
Output 444/889: t=5540000.0 yr, dE/E0=3.61e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 10 hours, 4 minutes, 17 seconds
  Estimated time remaining to next output: 7 minutes, 49 seconds
Output 445/889: t=5550000.0 yr, dE/E0=3.22e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 9 hours, 54 minutes, 31 seconds
  Estimated time remaining to next output: 7 minutes, 49 seconds
Output 446/889: t=5560000.0 yr, dE/E0=2.70e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 9 hours, 45 minutes, 14 seconds
  Estimated time remaining to next output: 7 minutes, 49 seconds
Output 447/889: t=5570000.0 yr, dE/E0=3.93e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 9 hours, 35 minutes, 19 seconds
  Estimated time remaining to next output: 7 minutes, 49 seconds
Output 448/889: t=5580000.0 yr, dE/E0=2.85e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 9 hours, 25 minutes, 43 seconds
  Estimated time remaining to next output: 7 minutes, 48 seconds
Output 449/889: t=5590000.0 yr, dE/E0=3.02e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 9 hours, 16 minutes, 20 seconds
  Estimated time remaining to next output: 7 minutes, 48 seconds
Output 450/889: t=5600000.0 yr, dE/E0=3.32e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 9 hours, 6 minutes, 43 seconds
  Estimated time remaining to next output: 7 minutes, 48 seconds
Output 451/889: t=5610000.0 yr, dE/E0=3.31e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 8 hours, 57 minutes, 25 seconds
  Estimated time remaining to next output: 7 minutes, 48 seconds
Output 452/889: t=5620000.0 yr, dE/E0=3.68e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 8 hours, 48 minutes, 4 seconds
  Estimated time remaining to next output: 7 minutes, 47 seconds
Output 453/889: t=5630000.0 yr, dE/E0=3.27e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 8 hours, 38 minutes, 21 seconds
  Estimated time remaining to next output: 7 minutes, 47 seconds
Output 454/889: t=5640000.0 yr, dE/E0=2.85e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 8 hours, 28 minutes, 46 seconds
  Estimated time remaining to next output: 7 minutes, 47 seconds
Output 455/889: t=5650000.0 yr, dE/E0=2.98e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 8 hours, 19 minutes, 23 seconds
  Estimated time remaining to next output: 7 minutes, 47 seconds
Output 456/889: t=5660000.0 yr, dE/E0=2.44e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 8 hours, 9 minutes, 44 seconds
  Estimated time remaining to next output: 7 minutes, 46 seconds
Output 457/889: t=5670000.0 yr, dE/E0=3.21e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 8 hours, 38 seconds
  Estimated time remaining to next output: 7 minutes, 46 seconds
Output 458/889: t=5680000.0 yr, dE/E0=3.18e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 7 hours, 51 minutes, 6 seconds
  Estimated time remaining to next output: 7 minutes, 46 seconds
Output 459/889: t=5690000.0 yr, dE/E0=1.73e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 7 hours, 41 minutes, 48 seconds
  Estimated time remaining to next output: 7 minutes, 46 seconds
Output 460/889: t=5700000.0 yr, dE/E0=1.98e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 7 hours, 32 minutes, 52 seconds
  Estimated time remaining to next output: 7 minutes, 46 seconds
Output 461/889: t=5710000.0 yr, dE/E0=2.74e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 7 hours, 23 minutes, 42 seconds
  Estimated time remaining to next output: 7 minutes, 45 seconds
Output 462/889: t=5720000.0 yr, dE/E0=3.30e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 7 hours, 14 minutes, 14 seconds
  Estimated time remaining to next output: 7 minutes, 45 seconds
Output 463/889: t=5730000.0 yr, dE/E0=3.23e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 7 hours, 4 minutes, 40 seconds
  Estimated time remaining to next output: 7 minutes, 45 seconds
Output 464/889: t=5740000.0 yr, dE/E0=3.17e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 6 hours, 55 minutes, 18 seconds
  Estimated time remaining to next output: 7 minutes, 45 seconds
Output 465/889: t=5750000.0 yr, dE/E0=3.59e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 6 hours, 45 minutes, 53 seconds
  Estimated time remaining to next output: 7 minutes, 44 seconds
Output 466/889: t=5760000.0 yr, dE/E0=3.92e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 6 hours, 36 minutes, 40 seconds
  Estimated time remaining to next output: 7 minutes, 44 seconds
Output 467/889: t=5770000.0 yr, dE/E0=4.17e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 6 hours, 27 minutes, 12 seconds
  Estimated time remaining to next output: 7 minutes, 44 seconds
Output 468/889: t=5780000.0 yr, dE/E0=4.77e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 6 hours, 17 minutes, 45 seconds
  Estimated time remaining to next output: 7 minutes, 44 seconds
Output 469/889: t=5790000.0 yr, dE/E0=4.78e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 6 hours, 8 minutes, 4 seconds
  Estimated time remaining to next output: 7 minutes, 44 seconds
Output 470/889: t=5800000.0 yr, dE/E0=5.37e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 5 hours, 59 minutes, 5 seconds
  Estimated time remaining to next output: 7 minutes, 43 seconds
Output 471/889: t=5810000.0 yr, dE/E0=4.62e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 5 hours, 49 minutes, 42 seconds
  Estimated time remaining to next output: 7 minutes, 43 seconds
Output 472/889: t=5820000.0 yr, dE/E0=4.57e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 5 hours, 40 minutes, 32 seconds
  Estimated time remaining to next output: 7 minutes, 43 seconds
Output 473/889: t=5830000.0 yr, dE/E0=4.64e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 5 hours, 31 minutes, 33 seconds
  Estimated time remaining to next output: 7 minutes, 43 seconds
Output 474/889: t=5840000.0 yr, dE/E0=5.26e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 5 hours, 22 minutes, 16 seconds
  Estimated time remaining to next output: 7 minutes, 42 seconds
Output 475/889: t=5850000.0 yr, dE/E0=5.02e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 5 hours, 13 minutes, 2 seconds
  Estimated time remaining to next output: 7 minutes, 42 seconds
Output 476/889: t=5860000.0 yr, dE/E0=4.78e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 5 hours, 4 minutes, 2 seconds
  Estimated time remaining to next output: 7 minutes, 42 seconds
Output 477/889: t=5870000.0 yr, dE/E0=4.32e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 4 hours, 54 minutes, 44 seconds
  Estimated time remaining to next output: 7 minutes, 42 seconds
Output 478/889: t=5880000.0 yr, dE/E0=4.69e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 4 hours, 45 minutes, 44 seconds
  Estimated time remaining to next output: 7 minutes, 42 seconds
Output 479/889: t=5890000.0 yr, dE/E0=4.79e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 4 hours, 36 minutes, 43 seconds
  Estimated time remaining to next output: 7 minutes, 41 seconds
Output 480/889: t=5900000.0 yr, dE/E0=4.46e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 4 hours, 27 minutes, 56 seconds
  Estimated time remaining to next output: 7 minutes, 41 seconds
Output 481/889: t=5910000.0 yr, dE/E0=4.03e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 4 hours, 18 minutes, 24 seconds
  Estimated time remaining to next output: 7 minutes, 41 seconds
Output 482/889: t=5920000.0 yr, dE/E0=3.21e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 4 hours, 9 minutes, 22 seconds
  Estimated time remaining to next output: 7 minutes, 41 seconds
Output 483/889: t=5930000.0 yr, dE/E0=3.98e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 4 hours, 3 seconds
  Estimated time remaining to next output: 7 minutes, 41 seconds
Output 484/889: t=5940000.0 yr, dE/E0=4.56e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 3 hours, 50 minutes, 39 seconds
  Estimated time remaining to next output: 7 minutes, 40 seconds
Output 485/889: t=5950000.0 yr, dE/E0=3.92e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 3 hours, 41 minutes, 46 seconds
  Estimated time remaining to next output: 7 minutes, 40 seconds
Output 486/889: t=5960000.0 yr, dE/E0=3.43e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 3 hours, 32 minutes, 48 seconds
  Estimated time remaining to next output: 7 minutes, 40 seconds
Output 487/889: t=5970000.0 yr, dE/E0=3.59e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 3 hours, 24 minutes, 6 seconds
  Estimated time remaining to next output: 7 minutes, 40 seconds
Output 488/889: t=5980000.0 yr, dE/E0=3.86e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 3 hours, 14 minutes, 53 seconds
  Estimated time remaining to next output: 7 minutes, 40 seconds
Output 489/889: t=5990000.0 yr, dE/E0=3.75e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 3 hours, 5 minutes, 47 seconds
  Estimated time remaining to next output: 7 minutes, 39 seconds
Output 490/889: t=6000000.0 yr, dE/E0=4.01e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 2 hours, 56 minutes, 49 seconds
  Estimated time remaining to next output: 7 minutes, 39 seconds
Output 491/889: t=6010000.0 yr, dE/E0=3.62e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 2 hours, 47 minutes, 27 seconds
  Estimated time remaining to next output: 7 minutes, 39 seconds
Output 492/889: t=6020000.0 yr, dE/E0=4.40e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 2 hours, 38 minutes, 31 seconds
  Estimated time remaining to next output: 7 minutes, 39 seconds
Output 493/889: t=6030000.0 yr, dE/E0=4.52e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 2 hours, 29 minutes, 29 seconds
  Estimated time remaining to next output: 7 minutes, 39 seconds
Output 494/889: t=6040000.0 yr, dE/E0=3.84e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 2 hours, 20 minutes, 30 seconds
  Estimated time remaining to next output: 7 minutes, 38 seconds
Output 495/889: t=6050000.0 yr, dE/E0=3.44e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 2 hours, 11 minutes, 23 seconds
  Estimated time remaining to next output: 7 minutes, 38 seconds
Output 496/889: t=6060000.0 yr, dE/E0=3.37e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 2 hours, 2 minutes, 18 seconds
  Estimated time remaining to next output: 7 minutes, 38 seconds
Output 497/889: t=6070000.0 yr, dE/E0=4.50e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 1 hours, 53 minutes, 26 seconds
  Estimated time remaining to next output: 7 minutes, 38 seconds
Output 498/889: t=6080000.0 yr, dE/E0=4.37e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 1 hours, 44 minutes, 36 seconds
  Estimated time remaining to next output: 7 minutes, 37 seconds
Output 499/889: t=6090000.0 yr, dE/E0=3.98e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 1 hours, 35 minutes, 30 seconds
  Estimated time remaining to next output: 7 minutes, 37 seconds
Output 500/889: t=6100000.0 yr, dE/E0=4.58e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 1 hours, 26 minutes, 24 seconds
  Estimated time remaining to next output: 7 minutes, 37 seconds
Output 501/889: t=6110000.0 yr, dE/E0=5.04e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 1 hours, 17 minutes, 30 seconds
  Estimated time remaining to next output: 7 minutes, 37 seconds
Output 502/889: t=6120000.0 yr, dE/E0=5.28e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 1 hours, 8 minutes, 43 seconds
  Estimated time remaining to next output: 7 minutes, 37 seconds
Output 503/889: t=6130000.0 yr, dE/E0=4.87e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 59 minutes, 35 seconds
  Estimated time remaining to next output: 7 minutes, 36 seconds
Output 504/889: t=6140000.0 yr, dE/E0=4.43e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 51 minutes, 4 seconds
  Estimated time remaining to next output: 7 minutes, 36 seconds
Output 505/889: t=6150000.0 yr, dE/E0=4.16e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 42 minutes, 14 seconds
  Estimated time remaining to next output: 7 minutes, 36 seconds
Output 506/889: t=6160000.0 yr, dE/E0=4.75e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 33 minutes, 9 seconds
  Estimated time remaining to next output: 7 minutes, 36 seconds
Output 507/889: t=6170000.0 yr, dE/E0=4.21e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 24 minutes, 8 seconds
  Estimated time remaining to next output: 7 minutes, 36 seconds
Output 508/889: t=6180000.0 yr, dE/E0=4.34e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 15 minutes, 11 seconds
  Estimated time remaining to next output: 7 minutes, 35 seconds
Output 509/889: t=6190000.0 yr, dE/E0=3.89e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 6 minutes, 12 seconds
  Estimated time remaining to next output: 7 minutes, 35 seconds
Output 510/889: t=6200000.0 yr, dE/E0=3.55e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 23 hours, 57 minutes, 39 seconds
  Estimated time remaining to next output: 7 minutes, 35 seconds
Output 511/889: t=6210000.0 yr, dE/E0=3.69e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 23 hours, 49 minutes, 7 seconds
  Estimated time remaining to next output: 7 minutes, 35 seconds
Output 512/889: t=6220000.0 yr, dE/E0=3.75e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 23 hours, 40 minutes, 25 seconds
  Estimated time remaining to next output: 7 minutes, 35 seconds
Output 513/889: t=6230000.0 yr, dE/E0=3.13e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 23 hours, 31 minutes, 42 seconds
  Estimated time remaining to next output: 7 minutes, 35 seconds
Output 514/889: t=6240000.0 yr, dE/E0=3.85e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 23 hours, 23 minutes, 4 seconds
  Estimated time remaining to next output: 7 minutes, 34 seconds
Output 515/889: t=6250000.0 yr, dE/E0=4.33e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 23 hours, 14 minutes, 11 seconds
  Estimated time remaining to next output: 7 minutes, 34 seconds
Output 516/889: t=6260000.0 yr, dE/E0=3.92e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 23 hours, 5 minutes, 38 seconds
  Estimated time remaining to next output: 7 minutes, 34 seconds
Output 517/889: t=6270000.0 yr, dE/E0=2.14e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 22 hours, 56 minutes, 37 seconds
  Estimated time remaining to next output: 7 minutes, 34 seconds
Output 518/889: t=6280000.0 yr, dE/E0=2.02e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 22 hours, 48 minutes, 3 seconds
  Estimated time remaining to next output: 7 minutes, 34 seconds
Output 519/889: t=6290000.0 yr, dE/E0=3.00e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 22 hours, 39 minutes, 24 seconds
  Estimated time remaining to next output: 7 minutes, 33 seconds
Output 520/889: t=6300000.0 yr, dE/E0=2.54e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 22 hours, 30 minutes, 35 seconds
  Estimated time remaining to next output: 7 minutes, 33 seconds
Output 521/889: t=6310000.0 yr, dE/E0=1.90e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 22 hours, 21 minutes, 44 seconds
  Estimated time remaining to next output: 7 minutes, 33 seconds
Output 522/889: t=6320000.0 yr, dE/E0=1.93e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 22 hours, 12 minutes, 56 seconds
  Estimated time remaining to next output: 7 minutes, 33 seconds
Output 523/889: t=6330000.0 yr, dE/E0=1.85e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 22 hours, 4 minutes, 24 seconds
  Estimated time remaining to next output: 7 minutes, 33 seconds
Output 524/889: t=6340000.0 yr, dE/E0=1.85e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 21 hours, 55 minutes, 52 seconds
  Estimated time remaining to next output: 7 minutes, 33 seconds
Output 525/889: t=6350000.0 yr, dE/E0=2.08e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 21 hours, 47 minutes, 9 seconds
  Estimated time remaining to next output: 7 minutes, 32 seconds
Output 526/889: t=6360000.0 yr, dE/E0=1.99e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 21 hours, 38 minutes, 26 seconds
  Estimated time remaining to next output: 7 minutes, 32 seconds
Output 527/889: t=6370000.0 yr, dE/E0=1.61e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 21 hours, 29 minutes, 39 seconds
  Estimated time remaining to next output: 7 minutes, 32 seconds
Output 528/889: t=6380000.0 yr, dE/E0=2.19e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 21 hours, 21 minutes, 4 seconds
  Estimated time remaining to next output: 7 minutes, 32 seconds
Output 529/889: t=6390000.0 yr, dE/E0=1.58e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 21 hours, 12 minutes, 11 seconds
  Estimated time remaining to next output: 7 minutes, 32 seconds
Output 530/889: t=6400000.0 yr, dE/E0=8.48e-09, N=802
  Estimated time remaining to complete simulation: 1 days, 21 hours, 3 minutes, 41 seconds
  Estimated time remaining to next output: 7 minutes, 31 seconds
Output 531/889: t=6410000.0 yr, dE/E0=7.45e-09, N=802
  Estimated time remaining to complete simulation: 1 days, 20 hours, 54 minutes, 58 seconds
  Estimated time remaining to next output: 7 minutes, 31 seconds
Output 532/889: t=6420000.0 yr, dE/E0=1.37e-09, N=802
  Estimated time remaining to complete simulation: 1 days, 20 hours, 46 minutes, 27 seconds
  Estimated time remaining to next output: 7 minutes, 31 seconds
Output 533/889: t=6430000.0 yr, dE/E0=6.73e-09, N=802
  Estimated time remaining to complete simulation: 1 days, 20 hours, 37 minutes, 38 seconds
  Estimated time remaining to next output: 7 minutes, 31 seconds
Output 534/889: t=6440000.0 yr, dE/E0=5.62e-09, N=802
  Estimated time remaining to complete simulation: 1 days, 20 hours, 29 minutes, 8 seconds
  Estimated time remaining to next output: 7 minutes, 31 seconds
Output 535/889: t=6450000.0 yr, dE/E0=1.06e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 20 hours, 20 minutes, 50 seconds
  Estimated time remaining to next output: 7 minutes, 30 seconds
Output 536/889: t=6460000.0 yr, dE/E0=5.42e-10, N=802
  Estimated time remaining to complete simulation: 1 days, 20 hours, 12 minutes, 10 seconds
  Estimated time remaining to next output: 7 minutes, 30 seconds
Output 537/889: t=6470000.0 yr, dE/E0=4.15e-09, N=802
  Estimated time remaining to complete simulation: 1 days, 20 hours, 3 minutes, 30 seconds
  Estimated time remaining to next output: 7 minutes, 30 seconds
Output 538/889: t=6480000.0 yr, dE/E0=2.74e-09, N=802
  Estimated time remaining to complete simulation: 1 days, 19 hours, 55 minutes, 8 seconds
  Estimated time remaining to next output: 7 minutes, 30 seconds
Output 539/889: t=6490000.0 yr, dE/E0=4.24e-09, N=802
  Estimated time remaining to complete simulation: 1 days, 19 hours, 46 minutes, 36 seconds
  Estimated time remaining to next output: 7 minutes, 30 seconds
Output 540/889: t=6500000.0 yr, dE/E0=2.18e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 19 hours, 38 minutes, 1 seconds
  Estimated time remaining to next output: 7 minutes, 30 seconds
Output 541/889: t=6510000.0 yr, dE/E0=5.56e-09, N=802
  Estimated time remaining to complete simulation: 1 days, 19 hours, 29 minutes, 25 seconds
  Estimated time remaining to next output: 7 minutes, 29 seconds
Output 542/889: t=6520000.0 yr, dE/E0=7.87e-09, N=802
  Estimated time remaining to complete simulation: 1 days, 19 hours, 20 minutes, 53 seconds
  Estimated time remaining to next output: 7 minutes, 29 seconds
Output 543/889: t=6530000.0 yr, dE/E0=1.91e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 19 hours, 12 minutes, 39 seconds
  Estimated time remaining to next output: 7 minutes, 29 seconds
Output 544/889: t=6540000.0 yr, dE/E0=1.61e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 19 hours, 4 minutes, 22 seconds
  Estimated time remaining to next output: 7 minutes, 29 seconds
Output 545/889: t=6550000.0 yr, dE/E0=1.15e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 18 hours, 55 minutes, 58 seconds
  Estimated time remaining to next output: 7 minutes, 29 seconds
Output 546/889: t=6560000.0 yr, dE/E0=7.13e-09, N=802
  Estimated time remaining to complete simulation: 1 days, 18 hours, 47 minutes, 50 seconds
  Estimated time remaining to next output: 7 minutes, 29 seconds
Output 547/889: t=6570000.0 yr, dE/E0=2.22e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 18 hours, 39 minutes, 31 seconds
  Estimated time remaining to next output: 7 minutes, 29 seconds
Output 548/889: t=6580000.0 yr, dE/E0=1.63e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 18 hours, 31 minutes
  Estimated time remaining to next output: 7 minutes, 28 seconds
Output 549/889: t=6590000.0 yr, dE/E0=2.42e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 18 hours, 22 minutes, 42 seconds
  Estimated time remaining to next output: 7 minutes, 28 seconds
Output 550/889: t=6600000.0 yr, dE/E0=1.27e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 18 hours, 14 minutes, 17 seconds
  Estimated time remaining to next output: 7 minutes, 28 seconds
Output 551/889: t=6610000.0 yr, dE/E0=2.16e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 18 hours, 5 minutes, 49 seconds
  Estimated time remaining to next output: 7 minutes, 28 seconds
Output 552/889: t=6620000.0 yr, dE/E0=1.38e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 17 hours, 57 minutes, 27 seconds
  Estimated time remaining to next output: 7 minutes, 28 seconds
Output 553/889: t=6630000.0 yr, dE/E0=1.03e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 17 hours, 49 minutes, 14 seconds
  Estimated time remaining to next output: 7 minutes, 28 seconds
Output 554/889: t=6640000.0 yr, dE/E0=7.38e-09, N=802
  Estimated time remaining to complete simulation: 1 days, 17 hours, 40 minutes, 53 seconds
  Estimated time remaining to next output: 7 minutes, 27 seconds
Output 555/889: t=6650000.0 yr, dE/E0=1.71e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 17 hours, 32 minutes, 31 seconds
  Estimated time remaining to next output: 7 minutes, 27 seconds
Output 556/889: t=6660000.0 yr, dE/E0=1.21e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 17 hours, 24 minutes, 17 seconds
  Estimated time remaining to next output: 7 minutes, 27 seconds
Output 557/889: t=6670000.0 yr, dE/E0=1.54e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 17 hours, 15 minutes, 53 seconds
  Estimated time remaining to next output: 7 minutes, 27 seconds
Output 558/889: t=6680000.0 yr, dE/E0=1.30e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 17 hours, 7 minutes, 29 seconds
  Estimated time remaining to next output: 7 minutes, 27 seconds
Output 559/889: t=6690000.0 yr, dE/E0=1.93e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 16 hours, 59 minutes, 7 seconds
  Estimated time remaining to next output: 7 minutes, 27 seconds
Output 560/889: t=6700000.0 yr, dE/E0=1.36e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 16 hours, 50 minutes, 42 seconds
  Estimated time remaining to next output: 7 minutes, 26 seconds
Output 561/889: t=6710000.0 yr, dE/E0=1.82e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 16 hours, 42 minutes, 37 seconds
  Estimated time remaining to next output: 7 minutes, 26 seconds
Output 562/889: t=6720000.0 yr, dE/E0=1.73e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 16 hours, 34 minutes, 28 seconds
  Estimated time remaining to next output: 7 minutes, 26 seconds
Output 563/889: t=6730000.0 yr, dE/E0=1.24e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 16 hours, 26 minutes, 20 seconds
  Estimated time remaining to next output: 7 minutes, 26 seconds
Output 564/889: t=6740000.0 yr, dE/E0=1.54e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 16 hours, 17 minutes, 59 seconds
  Estimated time remaining to next output: 7 minutes, 26 seconds
Output 565/889: t=6750000.0 yr, dE/E0=1.59e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 16 hours, 9 minutes, 39 seconds
  Estimated time remaining to next output: 7 minutes, 26 seconds
Output 566/889: t=6760000.0 yr, dE/E0=2.26e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 16 hours, 1 minutes, 40 seconds
  Estimated time remaining to next output: 7 minutes, 26 seconds
Output 567/889: t=6770000.0 yr, dE/E0=2.37e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 15 hours, 53 minutes, 29 seconds
  Estimated time remaining to next output: 7 minutes, 25 seconds
Output 568/889: t=6780000.0 yr, dE/E0=2.44e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 15 hours, 45 minutes, 2 seconds
  Estimated time remaining to next output: 7 minutes, 25 seconds
Output 569/889: t=6790000.0 yr, dE/E0=2.50e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 15 hours, 36 minutes, 51 seconds
  Estimated time remaining to next output: 7 minutes, 25 seconds
Output 570/889: t=6800000.0 yr, dE/E0=2.85e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 15 hours, 28 minutes, 28 seconds
  Estimated time remaining to next output: 7 minutes, 25 seconds
Output 571/889: t=6810000.0 yr, dE/E0=2.46e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 15 hours, 20 minutes, 13 seconds
  Estimated time remaining to next output: 7 minutes, 25 seconds
Output 572/889: t=6820000.0 yr, dE/E0=2.33e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 15 hours, 11 minutes, 56 seconds
  Estimated time remaining to next output: 7 minutes, 25 seconds
Output 573/889: t=6830000.0 yr, dE/E0=1.74e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 15 hours, 3 minutes, 48 seconds
  Estimated time remaining to next output: 7 minutes, 25 seconds
Output 574/889: t=6840000.0 yr, dE/E0=1.77e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 14 hours, 55 minutes, 32 seconds
  Estimated time remaining to next output: 7 minutes, 24 seconds
Output 575/889: t=6850000.0 yr, dE/E0=2.62e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 14 hours, 47 minutes, 21 seconds
  Estimated time remaining to next output: 7 minutes, 24 seconds
Output 576/889: t=6860000.0 yr, dE/E0=1.53e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 14 hours, 39 minutes, 3 seconds
  Estimated time remaining to next output: 7 minutes, 24 seconds
Output 577/889: t=6870000.0 yr, dE/E0=1.21e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 14 hours, 30 minutes, 58 seconds
  Estimated time remaining to next output: 7 minutes, 24 seconds
Output 578/889: t=6880000.0 yr, dE/E0=1.10e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 14 hours, 22 minutes, 35 seconds
  Estimated time remaining to next output: 7 minutes, 24 seconds
Output 579/889: t=6890000.0 yr, dE/E0=1.44e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 14 hours, 14 minutes, 14 seconds
  Estimated time remaining to next output: 7 minutes, 24 seconds
Output 580/889: t=6900000.0 yr, dE/E0=1.40e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 14 hours, 6 minutes, 12 seconds
  Estimated time remaining to next output: 7 minutes, 23 seconds
Output 581/889: t=6910000.0 yr, dE/E0=1.47e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 13 hours, 58 minutes, 7 seconds
  Estimated time remaining to next output: 7 minutes, 23 seconds
Output 582/889: t=6920000.0 yr, dE/E0=7.43e-09, N=802
  Estimated time remaining to complete simulation: 1 days, 13 hours, 49 minutes, 55 seconds
  Estimated time remaining to next output: 7 minutes, 23 seconds
Output 583/889: t=6930000.0 yr, dE/E0=1.70e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 13 hours, 41 minutes, 37 seconds
  Estimated time remaining to next output: 7 minutes, 23 seconds
Output 584/889: t=6940000.0 yr, dE/E0=2.05e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 13 hours, 33 minutes, 17 seconds
  Estimated time remaining to next output: 7 minutes, 23 seconds
Output 585/889: t=6950000.0 yr, dE/E0=4.95e-09, N=802
  Estimated time remaining to complete simulation: 1 days, 13 hours, 25 minutes, 16 seconds
  Estimated time remaining to next output: 7 minutes, 23 seconds
Output 586/889: t=6960000.0 yr, dE/E0=2.73e-09, N=802
  Estimated time remaining to complete simulation: 1 days, 13 hours, 16 minutes, 59 seconds
  Estimated time remaining to next output: 7 minutes, 22 seconds
Output 587/889: t=6970000.0 yr, dE/E0=4.80e-09, N=802
  Estimated time remaining to complete simulation: 1 days, 13 hours, 8 minutes, 54 seconds
  Estimated time remaining to next output: 7 minutes, 22 seconds
Output 588/889: t=6980000.0 yr, dE/E0=1.01e-11, N=802
  Estimated time remaining to complete simulation: 1 days, 13 hours, 47 seconds
  Estimated time remaining to next output: 7 minutes, 22 seconds
Output 589/889: t=6990000.0 yr, dE/E0=2.86e-09, N=802
  Estimated time remaining to complete simulation: 1 days, 12 hours, 52 minutes, 41 seconds
  Estimated time remaining to next output: 7 minutes, 22 seconds
Output 590/889: t=7000000.0 yr, dE/E0=1.04e-09, N=802
  Estimated time remaining to complete simulation: 1 days, 12 hours, 44 minutes, 29 seconds
  Estimated time remaining to next output: 7 minutes, 22 seconds
Output 591/889: t=7010000.0 yr, dE/E0=1.05e-09, N=802
  Estimated time remaining to complete simulation: 1 days, 12 hours, 36 minutes, 10 seconds
  Estimated time remaining to next output: 7 minutes, 22 seconds
Output 592/889: t=7020000.0 yr, dE/E0=4.82e-09, N=802
  Estimated time remaining to complete simulation: 1 days, 12 hours, 27 minutes, 53 seconds
  Estimated time remaining to next output: 7 minutes, 21 seconds
Output 593/889: t=7030000.0 yr, dE/E0=5.97e-09, N=802
  Estimated time remaining to complete simulation: 1 days, 12 hours, 19 minutes, 31 seconds
  Estimated time remaining to next output: 7 minutes, 21 seconds
Output 594/889: t=7040000.0 yr, dE/E0=2.13e-09, N=802
  Estimated time remaining to complete simulation: 1 days, 12 hours, 11 minutes, 24 seconds
  Estimated time remaining to next output: 7 minutes, 21 seconds
Output 595/889: t=7050000.0 yr, dE/E0=1.79e-09, N=802
  Estimated time remaining to complete simulation: 1 days, 12 hours, 3 minutes, 7 seconds
  Estimated time remaining to next output: 7 minutes, 21 seconds
Output 596/889: t=7060000.0 yr, dE/E0=2.12e-09, N=802
  Estimated time remaining to complete simulation: 1 days, 11 hours, 54 minutes, 51 seconds
  Estimated time remaining to next output: 7 minutes, 21 seconds
Output 597/889: t=7070000.0 yr, dE/E0=7.49e-09, N=802
  Estimated time remaining to complete simulation: 1 days, 11 hours, 46 minutes, 33 seconds
  Estimated time remaining to next output: 7 minutes, 21 seconds
Output 598/889: t=7080000.0 yr, dE/E0=2.91e-09, N=802
  Estimated time remaining to complete simulation: 1 days, 11 hours, 38 minutes, 30 seconds
  Estimated time remaining to next output: 7 minutes, 20 seconds
Output 599/889: t=7090000.0 yr, dE/E0=6.00e-09, N=802
  Estimated time remaining to complete simulation: 1 days, 11 hours, 30 minutes, 16 seconds
  Estimated time remaining to next output: 7 minutes, 20 seconds
Output 600/889: t=7100000.0 yr, dE/E0=3.72e-09, N=802
  Estimated time remaining to complete simulation: 1 days, 11 hours, 22 minutes, 6 seconds
  Estimated time remaining to next output: 7 minutes, 20 seconds
Output 601/889: t=7110000.0 yr, dE/E0=8.37e-09, N=802
  Estimated time remaining to complete simulation: 1 days, 11 hours, 14 minutes, 12 seconds
  Estimated time remaining to next output: 7 minutes, 20 seconds
Output 602/889: t=7120000.0 yr, dE/E0=3.25e-09, N=802
  Estimated time remaining to complete simulation: 1 days, 11 hours, 5 minutes, 58 seconds
  Estimated time remaining to next output: 7 minutes, 20 seconds
Output 603/889: t=7130000.0 yr, dE/E0=1.64e-09, N=802
  Estimated time remaining to complete simulation: 1 days, 10 hours, 57 minutes, 49 seconds
  Estimated time remaining to next output: 7 minutes, 20 seconds
Output 604/889: t=7140000.0 yr, dE/E0=7.99e-09, N=802
  Estimated time remaining to complete simulation: 1 days, 10 hours, 49 minutes, 40 seconds
  Estimated time remaining to next output: 7 minutes, 19 seconds
Output 605/889: t=7150000.0 yr, dE/E0=1.13e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 10 hours, 41 minutes, 25 seconds
  Estimated time remaining to next output: 7 minutes, 19 seconds
Output 606/889: t=7160000.0 yr, dE/E0=4.33e-09, N=802
  Estimated time remaining to complete simulation: 1 days, 10 hours, 33 minutes, 15 seconds
  Estimated time remaining to next output: 7 minutes, 19 seconds
Output 607/889: t=7170000.0 yr, dE/E0=3.22e-09, N=802
  Estimated time remaining to complete simulation: 1 days, 10 hours, 25 minutes, 3 seconds
  Estimated time remaining to next output: 7 minutes, 19 seconds
Output 608/889: t=7180000.0 yr, dE/E0=4.77e-10, N=802
  Estimated time remaining to complete simulation: 1 days, 10 hours, 16 minutes, 49 seconds
  Estimated time remaining to next output: 7 minutes, 19 seconds
Output 609/889: t=7190000.0 yr, dE/E0=2.95e-09, N=802
  Estimated time remaining to complete simulation: 1 days, 10 hours, 8 minutes, 42 seconds
  Estimated time remaining to next output: 7 minutes, 19 seconds
Output 610/889: t=7200000.0 yr, dE/E0=2.34e-09, N=802
  Estimated time remaining to complete simulation: 1 days, 10 hours, 31 seconds
  Estimated time remaining to next output: 7 minutes, 18 seconds
Output 611/889: t=7210000.0 yr, dE/E0=7.19e-09, N=802
  Estimated time remaining to complete simulation: 1 days, 9 hours, 52 minutes, 31 seconds
  Estimated time remaining to next output: 7 minutes, 18 seconds
Output 612/889: t=7220000.0 yr, dE/E0=9.08e-09, N=802
  Estimated time remaining to complete simulation: 1 days, 9 hours, 44 minutes, 33 seconds
  Estimated time remaining to next output: 7 minutes, 18 seconds
Output 613/889: t=7230000.0 yr, dE/E0=6.61e-09, N=802
  Estimated time remaining to complete simulation: 1 days, 9 hours, 36 minutes, 28 seconds
  Estimated time remaining to next output: 7 minutes, 18 seconds
Output 614/889: t=7240000.0 yr, dE/E0=1.17e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 9 hours, 28 minutes, 29 seconds
  Estimated time remaining to next output: 7 minutes, 18 seconds
Output 615/889: t=7250000.0 yr, dE/E0=7.53e-09, N=802
  Estimated time remaining to complete simulation: 1 days, 9 hours, 20 minutes, 25 seconds
  Estimated time remaining to next output: 7 minutes, 18 seconds
Output 616/889: t=7260000.0 yr, dE/E0=1.06e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 9 hours, 12 minutes, 15 seconds
  Estimated time remaining to next output: 7 minutes, 17 seconds
Output 617/889: t=7270000.0 yr, dE/E0=1.29e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 9 hours, 4 minutes, 15 seconds
  Estimated time remaining to next output: 7 minutes, 17 seconds
Output 618/889: t=7280000.0 yr, dE/E0=1.79e-09, N=802
  Estimated time remaining to complete simulation: 1 days, 8 hours, 56 minutes, 14 seconds
  Estimated time remaining to next output: 7 minutes, 17 seconds
Output 619/889: t=7290000.0 yr, dE/E0=1.03e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 8 hours, 48 minutes, 9 seconds
  Estimated time remaining to next output: 7 minutes, 17 seconds
Output 620/889: t=7300000.0 yr, dE/E0=5.08e-09, N=802
  Estimated time remaining to complete simulation: 1 days, 8 hours, 40 minutes, 7 seconds
  Estimated time remaining to next output: 7 minutes, 17 seconds
Output 621/889: t=7310000.0 yr, dE/E0=1.23e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 8 hours, 32 minutes, 5 seconds
  Estimated time remaining to next output: 7 minutes, 17 seconds
Output 622/889: t=7320000.0 yr, dE/E0=6.98e-09, N=802
  Estimated time remaining to complete simulation: 1 days, 8 hours, 24 minutes, 1 seconds
  Estimated time remaining to next output: 7 minutes, 16 seconds
Output 623/889: t=7330000.0 yr, dE/E0=1.95e-09, N=802
  Estimated time remaining to complete simulation: 1 days, 8 hours, 16 minutes, 5 seconds
  Estimated time remaining to next output: 7 minutes, 16 seconds
Output 624/889: t=7340000.0 yr, dE/E0=6.03e-09, N=802
  Estimated time remaining to complete simulation: 1 days, 8 hours, 8 minutes, 7 seconds
  Estimated time remaining to next output: 7 minutes, 16 seconds
Output 625/889: t=7350000.0 yr, dE/E0=7.51e-09, N=802
  Estimated time remaining to complete simulation: 1 days, 8 hours, 7 seconds
  Estimated time remaining to next output: 7 minutes, 16 seconds
Output 626/889: t=7360000.0 yr, dE/E0=1.19e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 7 hours, 52 minutes, 2 seconds
  Estimated time remaining to next output: 7 minutes, 16 seconds
Output 627/889: t=7370000.0 yr, dE/E0=1.58e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 7 hours, 44 minutes, 12 seconds
  Estimated time remaining to next output: 7 minutes, 16 seconds
Output 628/889: t=7380000.0 yr, dE/E0=9.31e-09, N=802
  Estimated time remaining to complete simulation: 1 days, 7 hours, 36 minutes, 17 seconds
  Estimated time remaining to next output: 7 minutes, 15 seconds
Output 629/889: t=7390000.0 yr, dE/E0=5.92e-09, N=802
  Estimated time remaining to complete simulation: 1 days, 7 hours, 28 minutes, 17 seconds
  Estimated time remaining to next output: 7 minutes, 15 seconds
Output 630/889: t=7400000.0 yr, dE/E0=1.67e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 7 hours, 20 minutes, 11 seconds
  Estimated time remaining to next output: 7 minutes, 15 seconds
Output 631/889: t=7410000.0 yr, dE/E0=5.40e-09, N=802
  Estimated time remaining to complete simulation: 1 days, 7 hours, 12 minutes, 14 seconds
  Estimated time remaining to next output: 7 minutes, 15 seconds
Output 632/889: t=7420000.0 yr, dE/E0=1.01e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 7 hours, 4 minutes, 15 seconds
  Estimated time remaining to next output: 7 minutes, 15 seconds
Output 633/889: t=7430000.0 yr, dE/E0=1.02e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 6 hours, 56 minutes, 26 seconds
  Estimated time remaining to next output: 7 minutes, 15 seconds
Output 634/889: t=7440000.0 yr, dE/E0=1.79e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 6 hours, 48 minutes, 42 seconds
  Estimated time remaining to next output: 7 minutes, 14 seconds
Output 635/889: t=7450000.0 yr, dE/E0=8.37e-09, N=802
  Estimated time remaining to complete simulation: 1 days, 6 hours, 40 minutes, 50 seconds
  Estimated time remaining to next output: 7 minutes, 14 seconds
Output 636/889: t=7460000.0 yr, dE/E0=4.98e-09, N=802
  Estimated time remaining to complete simulation: 1 days, 6 hours, 32 minutes, 54 seconds
  Estimated time remaining to next output: 7 minutes, 14 seconds
Output 637/889: t=7470000.0 yr, dE/E0=2.37e-09, N=802
  Estimated time remaining to complete simulation: 1 days, 6 hours, 24 minutes, 58 seconds
  Estimated time remaining to next output: 7 minutes, 14 seconds
Output 638/889: t=7480000.0 yr, dE/E0=5.22e-09, N=802
  Estimated time remaining to complete simulation: 1 days, 6 hours, 17 minutes, 1 seconds
  Estimated time remaining to next output: 7 minutes, 14 seconds
Output 639/889: t=7490000.0 yr, dE/E0=8.16e-09, N=802
  Estimated time remaining to complete simulation: 1 days, 6 hours, 9 minutes, 3 seconds
  Estimated time remaining to next output: 7 minutes, 14 seconds
Output 640/889: t=7500000.0 yr, dE/E0=1.15e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 6 hours, 1 minutes, 7 seconds
  Estimated time remaining to next output: 7 minutes, 14 seconds
Output 641/889: t=7510000.0 yr, dE/E0=8.10e-09, N=802
  Estimated time remaining to complete simulation: 1 days, 5 hours, 53 minutes, 4 seconds
  Estimated time remaining to next output: 7 minutes, 13 seconds
Output 642/889: t=7520000.0 yr, dE/E0=6.23e-09, N=802
  Estimated time remaining to complete simulation: 1 days, 5 hours, 45 minutes, 7 seconds
  Estimated time remaining to next output: 7 minutes, 13 seconds
Output 643/889: t=7530000.0 yr, dE/E0=1.13e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 5 hours, 36 minutes, 59 seconds
  Estimated time remaining to next output: 7 minutes, 13 seconds
Output 644/889: t=7540000.0 yr, dE/E0=2.24e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 5 hours, 28 minutes, 59 seconds
  Estimated time remaining to next output: 7 minutes, 13 seconds
Output 645/889: t=7550000.0 yr, dE/E0=1.65e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 5 hours, 21 minutes, 5 seconds
  Estimated time remaining to next output: 7 minutes, 13 seconds
Output 646/889: t=7560000.0 yr, dE/E0=8.47e-09, N=802
  Estimated time remaining to complete simulation: 1 days, 5 hours, 13 minutes, 7 seconds
  Estimated time remaining to next output: 7 minutes, 12 seconds
Output 647/889: t=7570000.0 yr, dE/E0=1.27e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 5 hours, 5 minutes, 12 seconds
  Estimated time remaining to next output: 7 minutes, 12 seconds
Output 648/889: t=7580000.0 yr, dE/E0=6.22e-09, N=802
  Estimated time remaining to complete simulation: 1 days, 4 hours, 57 minutes, 20 seconds
  Estimated time remaining to next output: 7 minutes, 12 seconds
Output 649/889: t=7590000.0 yr, dE/E0=8.86e-09, N=802
  Estimated time remaining to complete simulation: 1 days, 4 hours, 49 minutes, 21 seconds
  Estimated time remaining to next output: 7 minutes, 12 seconds
Output 650/889: t=7600000.0 yr, dE/E0=4.58e-09, N=802
  Estimated time remaining to complete simulation: 1 days, 4 hours, 41 minutes, 27 seconds
  Estimated time remaining to next output: 7 minutes, 12 seconds
Output 651/889: t=7610000.0 yr, dE/E0=1.35e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 4 hours, 33 minutes, 31 seconds
  Estimated time remaining to next output: 7 minutes, 11 seconds
Output 652/889: t=7620000.0 yr, dE/E0=1.92e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 4 hours, 25 minutes, 39 seconds
  Estimated time remaining to next output: 7 minutes, 11 seconds
Output 653/889: t=7630000.0 yr, dE/E0=2.42e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 4 hours, 17 minutes, 51 seconds
  Estimated time remaining to next output: 7 minutes, 11 seconds
Output 654/889: t=7640000.0 yr, dE/E0=1.30e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 4 hours, 9 minutes, 54 seconds
  Estimated time remaining to next output: 7 minutes, 11 seconds
Output 655/889: t=7650000.0 yr, dE/E0=1.45e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 4 hours, 2 minutes, 2 seconds
  Estimated time remaining to next output: 7 minutes, 11 seconds
Output 656/889: t=7660000.0 yr, dE/E0=9.72e-09, N=802
  Estimated time remaining to complete simulation: 1 days, 3 hours, 54 minutes, 6 seconds
  Estimated time remaining to next output: 7 minutes, 11 seconds
Output 657/889: t=7670000.0 yr, dE/E0=1.45e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 3 hours, 46 minutes, 13 seconds
  Estimated time remaining to next output: 7 minutes, 10 seconds
Output 658/889: t=7680000.0 yr, dE/E0=1.18e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 3 hours, 38 minutes, 21 seconds
  Estimated time remaining to next output: 7 minutes, 10 seconds
Output 659/889: t=7690000.0 yr, dE/E0=1.68e-09, N=802
  Estimated time remaining to complete simulation: 1 days, 3 hours, 30 minutes, 23 seconds
  Estimated time remaining to next output: 7 minutes, 10 seconds
Output 660/889: t=7700000.0 yr, dE/E0=5.42e-09, N=802
  Estimated time remaining to complete simulation: 1 days, 3 hours, 22 minutes, 46 seconds
  Estimated time remaining to next output: 7 minutes, 10 seconds
Output 661/889: t=7710000.0 yr, dE/E0=9.48e-09, N=802
  Estimated time remaining to complete simulation: 1 days, 3 hours, 14 minutes, 52 seconds
  Estimated time remaining to next output: 7 minutes, 10 seconds
Output 662/889: t=7720000.0 yr, dE/E0=1.78e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 3 hours, 7 minutes, 7 seconds
  Estimated time remaining to next output: 7 minutes, 10 seconds
Output 663/889: t=7730000.0 yr, dE/E0=1.87e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 2 hours, 59 minutes, 26 seconds
  Estimated time remaining to next output: 7 minutes, 9 seconds
Output 664/889: t=7740000.0 yr, dE/E0=5.76e-09, N=802
  Estimated time remaining to complete simulation: 1 days, 2 hours, 51 minutes, 37 seconds
  Estimated time remaining to next output: 7 minutes, 9 seconds
Output 665/889: t=7750000.0 yr, dE/E0=1.26e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 2 hours, 43 minutes, 52 seconds
  Estimated time remaining to next output: 7 minutes, 9 seconds
Output 666/889: t=7760000.0 yr, dE/E0=1.44e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 2 hours, 36 minutes, 5 seconds
  Estimated time remaining to next output: 7 minutes, 9 seconds
Output 667/889: t=7770000.0 yr, dE/E0=9.62e-09, N=802
  Estimated time remaining to complete simulation: 1 days, 2 hours, 28 minutes, 15 seconds
  Estimated time remaining to next output: 7 minutes, 9 seconds
Output 668/889: t=7780000.0 yr, dE/E0=1.05e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 2 hours, 20 minutes, 26 seconds
  Estimated time remaining to next output: 7 minutes, 9 seconds
Output 669/889: t=7790000.0 yr, dE/E0=9.78e-10, N=802
  Estimated time remaining to complete simulation: 1 days, 2 hours, 12 minutes, 45 seconds
  Estimated time remaining to next output: 7 minutes, 8 seconds
Output 670/889: t=7800000.0 yr, dE/E0=1.80e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 2 hours, 4 minutes, 58 seconds
  Estimated time remaining to next output: 7 minutes, 8 seconds
Output 671/889: t=7810000.0 yr, dE/E0=1.47e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 1 hours, 57 minutes, 13 seconds
  Estimated time remaining to next output: 7 minutes, 8 seconds
Output 672/889: t=7820000.0 yr, dE/E0=1.77e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 1 hours, 49 minutes, 32 seconds
  Estimated time remaining to next output: 7 minutes, 8 seconds
Output 673/889: t=7830000.0 yr, dE/E0=1.74e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 1 hours, 41 minutes, 49 seconds
  Estimated time remaining to next output: 7 minutes, 8 seconds
Output 674/889: t=7840000.0 yr, dE/E0=2.50e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 1 hours, 34 minutes
  Estimated time remaining to next output: 7 minutes, 8 seconds
Output 675/889: t=7850000.0 yr, dE/E0=2.16e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 1 hours, 26 minutes, 14 seconds
  Estimated time remaining to next output: 7 minutes, 7 seconds
Output 676/889: t=7860000.0 yr, dE/E0=2.35e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 1 hours, 18 minutes, 27 seconds
  Estimated time remaining to next output: 7 minutes, 7 seconds
Output 677/889: t=7870000.0 yr, dE/E0=1.02e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 1 hours, 10 minutes, 48 seconds
  Estimated time remaining to next output: 7 minutes, 7 seconds
Output 678/889: t=7880000.0 yr, dE/E0=1.15e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 1 hours, 3 minutes, 13 seconds
  Estimated time remaining to next output: 7 minutes, 7 seconds
Output 679/889: t=7890000.0 yr, dE/E0=1.84e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 55 minutes, 28 seconds
  Estimated time remaining to next output: 7 minutes, 7 seconds
Output 680/889: t=7900000.0 yr, dE/E0=1.49e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 47 minutes, 45 seconds
  Estimated time remaining to next output: 7 minutes, 7 seconds
Output 681/889: t=7910000.0 yr, dE/E0=1.96e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 40 minutes
  Estimated time remaining to next output: 7 minutes, 6 seconds
Output 682/889: t=7920000.0 yr, dE/E0=2.34e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 32 minutes, 14 seconds
  Estimated time remaining to next output: 7 minutes, 6 seconds
Output 683/889: t=7930000.0 yr, dE/E0=2.40e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 24 minutes, 31 seconds
  Estimated time remaining to next output: 7 minutes, 6 seconds
Output 684/889: t=7940000.0 yr, dE/E0=3.51e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 16 minutes, 49 seconds
  Estimated time remaining to next output: 7 minutes, 6 seconds
Output 685/889: t=7950000.0 yr, dE/E0=4.11e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 9 minutes, 13 seconds
  Estimated time remaining to next output: 7 minutes, 6 seconds
Output 686/889: t=7960000.0 yr, dE/E0=2.55e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 1 minutes, 29 seconds
  Estimated time remaining to next output: 7 minutes, 6 seconds
Output 687/889: t=7970000.0 yr, dE/E0=2.97e-08, N=802
  Estimated time remaining to complete simulation: 23 hours, 53 minutes, 56 seconds
  Estimated time remaining to next output: 7 minutes, 5 seconds
Output 688/889: t=7980000.0 yr, dE/E0=2.89e-08, N=802
  Estimated time remaining to complete simulation: 23 hours, 46 minutes, 18 seconds
  Estimated time remaining to next output: 7 minutes, 5 seconds
Output 689/889: t=7990000.0 yr, dE/E0=3.45e-08, N=802
  Estimated time remaining to complete simulation: 23 hours, 38 minutes, 40 seconds
  Estimated time remaining to next output: 7 minutes, 5 seconds
Output 690/889: t=8000000.0 yr, dE/E0=3.03e-08, N=802
  Estimated time remaining to complete simulation: 23 hours, 31 minutes, 5 seconds
  Estimated time remaining to next output: 7 minutes, 5 seconds
Output 691/889: t=8010000.0 yr, dE/E0=2.27e-08, N=802
  Estimated time remaining to complete simulation: 23 hours, 23 minutes, 33 seconds
  Estimated time remaining to next output: 7 minutes, 5 seconds
Output 692/889: t=8020000.0 yr, dE/E0=3.57e-08, N=802
  Estimated time remaining to complete simulation: 23 hours, 15 minutes, 57 seconds
  Estimated time remaining to next output: 7 minutes, 5 seconds
Output 693/889: t=8030000.0 yr, dE/E0=3.85e-08, N=802
  Estimated time remaining to complete simulation: 23 hours, 8 minutes, 21 seconds
  Estimated time remaining to next output: 7 minutes, 5 seconds
Output 694/889: t=8040000.0 yr, dE/E0=4.00e-08, N=802
  Estimated time remaining to complete simulation: 23 hours, 40 seconds
  Estimated time remaining to next output: 7 minutes, 4 seconds
Output 695/889: t=8050000.0 yr, dE/E0=3.39e-08, N=802
  Estimated time remaining to complete simulation: 22 hours, 53 minutes
  Estimated time remaining to next output: 7 minutes, 4 seconds
Output 696/889: t=8060000.0 yr, dE/E0=3.81e-08, N=802
  Estimated time remaining to complete simulation: 22 hours, 45 minutes, 21 seconds
  Estimated time remaining to next output: 7 minutes, 4 seconds
Output 697/889: t=8070000.0 yr, dE/E0=3.69e-08, N=802
  Estimated time remaining to complete simulation: 22 hours, 37 minutes, 45 seconds
  Estimated time remaining to next output: 7 minutes, 4 seconds
Output 698/889: t=8080000.0 yr, dE/E0=4.11e-08, N=802
  Estimated time remaining to complete simulation: 22 hours, 30 minutes, 13 seconds
  Estimated time remaining to next output: 7 minutes, 4 seconds
Output 699/889: t=8090000.0 yr, dE/E0=3.50e-08, N=802
  Estimated time remaining to complete simulation: 22 hours, 22 minutes, 38 seconds
  Estimated time remaining to next output: 7 minutes, 3 seconds
Output 700/889: t=8100000.0 yr, dE/E0=3.38e-08, N=802
  Estimated time remaining to complete simulation: 22 hours, 15 minutes, 8 seconds
  Estimated time remaining to next output: 7 minutes, 3 seconds
Output 701/889: t=8110000.0 yr, dE/E0=2.80e-08, N=802
  Estimated time remaining to complete simulation: 22 hours, 7 minutes, 33 seconds
  Estimated time remaining to next output: 7 minutes, 3 seconds
Output 702/889: t=8120000.0 yr, dE/E0=3.25e-08, N=802
  Estimated time remaining to complete simulation: 22 hours
  Estimated time remaining to next output: 7 minutes, 3 seconds
Output 703/889: t=8130000.0 yr, dE/E0=3.15e-08, N=802
  Estimated time remaining to complete simulation: 21 hours, 52 minutes, 23 seconds
  Estimated time remaining to next output: 7 minutes, 3 seconds
Output 704/889: t=8140000.0 yr, dE/E0=2.54e-08, N=802
  Estimated time remaining to complete simulation: 21 hours, 44 minutes, 55 seconds
  Estimated time remaining to next output: 7 minutes, 3 seconds
Output 705/889: t=8150000.0 yr, dE/E0=3.30e-08, N=802
  Estimated time remaining to complete simulation: 21 hours, 37 minutes, 22 seconds
  Estimated time remaining to next output: 7 minutes, 3 seconds
Output 706/889: t=8160000.0 yr, dE/E0=3.76e-08, N=802
  Estimated time remaining to complete simulation: 21 hours, 29 minutes, 52 seconds
  Estimated time remaining to next output: 7 minutes, 2 seconds
Output 707/889: t=8170000.0 yr, dE/E0=2.72e-08, N=802
  Estimated time remaining to complete simulation: 21 hours, 22 minutes, 19 seconds
  Estimated time remaining to next output: 7 minutes, 2 seconds
Output 708/889: t=8180000.0 yr, dE/E0=3.26e-08, N=802
  Estimated time remaining to complete simulation: 21 hours, 14 minutes, 47 seconds
  Estimated time remaining to next output: 7 minutes, 2 seconds
Output 709/889: t=8190000.0 yr, dE/E0=2.76e-08, N=802
  Estimated time remaining to complete simulation: 21 hours, 7 minutes, 19 seconds
  Estimated time remaining to next output: 7 minutes, 2 seconds
Output 710/889: t=8200000.0 yr, dE/E0=3.58e-08, N=802
  Estimated time remaining to complete simulation: 20 hours, 59 minutes, 50 seconds
  Estimated time remaining to next output: 7 minutes, 2 seconds
Output 711/889: t=8210000.0 yr, dE/E0=3.62e-08, N=802
  Estimated time remaining to complete simulation: 20 hours, 52 minutes, 24 seconds
  Estimated time remaining to next output: 7 minutes, 2 seconds
Output 712/889: t=8220000.0 yr, dE/E0=3.51e-08, N=802
  Estimated time remaining to complete simulation: 20 hours, 44 minutes, 50 seconds
  Estimated time remaining to next output: 7 minutes, 1 seconds
Output 713/889: t=8230000.0 yr, dE/E0=3.40e-08, N=802
  Estimated time remaining to complete simulation: 20 hours, 37 minutes, 19 seconds
  Estimated time remaining to next output: 7 minutes, 1 seconds
Output 714/889: t=8240000.0 yr, dE/E0=3.07e-08, N=802
  Estimated time remaining to complete simulation: 20 hours, 29 minutes, 58 seconds
  Estimated time remaining to next output: 7 minutes, 1 seconds
Output 715/889: t=8250000.0 yr, dE/E0=3.73e-08, N=802
  Estimated time remaining to complete simulation: 20 hours, 22 minutes, 31 seconds
  Estimated time remaining to next output: 7 minutes, 1 seconds
Output 716/889: t=8260000.0 yr, dE/E0=3.61e-08, N=802
  Estimated time remaining to complete simulation: 20 hours, 14 minutes, 59 seconds
  Estimated time remaining to next output: 7 minutes, 1 seconds
Output 717/889: t=8270000.0 yr, dE/E0=3.69e-08, N=802
  Estimated time remaining to complete simulation: 20 hours, 7 minutes, 29 seconds
  Estimated time remaining to next output: 7 minutes, 1 seconds
Output 718/889: t=8280000.0 yr, dE/E0=3.81e-08, N=802
  Estimated time remaining to complete simulation: 20 hours, 7 seconds
  Estimated time remaining to next output: 7 minutes, 1 seconds
Output 719/889: t=8290000.0 yr, dE/E0=4.10e-08, N=802
  Estimated time remaining to complete simulation: 19 hours, 52 minutes, 41 seconds
  Estimated time remaining to next output: 7 minutes
Output 720/889: t=8300000.0 yr, dE/E0=4.69e-08, N=802
  Estimated time remaining to complete simulation: 19 hours, 45 minutes, 13 seconds
  Estimated time remaining to next output: 7 minutes
Output 721/889: t=8310000.0 yr, dE/E0=3.37e-08, N=802
  Estimated time remaining to complete simulation: 19 hours, 37 minutes, 46 seconds
  Estimated time remaining to next output: 7 minutes
Output 722/889: t=8320000.0 yr, dE/E0=4.58e-08, N=802
  Estimated time remaining to complete simulation: 19 hours, 30 minutes, 19 seconds
  Estimated time remaining to next output: 7 minutes
Output 723/889: t=8330000.0 yr, dE/E0=4.26e-08, N=802
  Estimated time remaining to complete simulation: 19 hours, 22 minutes, 50 seconds
  Estimated time remaining to next output: 7 minutes
Output 724/889: t=8340000.0 yr, dE/E0=4.20e-08, N=802
  Estimated time remaining to complete simulation: 19 hours, 15 minutes, 29 seconds
  Estimated time remaining to next output: 7 minutes
Output 725/889: t=8350000.0 yr, dE/E0=3.49e-08, N=802
  Estimated time remaining to complete simulation: 19 hours, 8 minutes, 11 seconds
  Estimated time remaining to next output: 7 minutes
Output 726/889: t=8360000.0 yr, dE/E0=4.43e-08, N=802
  Estimated time remaining to complete simulation: 19 hours, 51 seconds
  Estimated time remaining to next output: 6 minutes, 59 seconds
Output 727/889: t=8370000.0 yr, dE/E0=4.68e-08, N=802
  Estimated time remaining to complete simulation: 18 hours, 53 minutes, 27 seconds
  Estimated time remaining to next output: 6 minutes, 59 seconds
Output 728/889: t=8380000.0 yr, dE/E0=4.70e-08, N=802
  Estimated time remaining to complete simulation: 18 hours, 46 minutes, 3 seconds
  Estimated time remaining to next output: 6 minutes, 59 seconds
Output 729/889: t=8390000.0 yr, dE/E0=5.44e-08, N=802
  Estimated time remaining to complete simulation: 18 hours, 38 minutes, 40 seconds
  Estimated time remaining to next output: 6 minutes, 59 seconds
Output 730/889: t=8400000.0 yr, dE/E0=4.71e-08, N=802
  Estimated time remaining to complete simulation: 18 hours, 31 minutes, 19 seconds
  Estimated time remaining to next output: 6 minutes, 59 seconds
Output 731/889: t=8410000.0 yr, dE/E0=4.61e-08, N=802
  Estimated time remaining to complete simulation: 18 hours, 23 minutes, 59 seconds
  Estimated time remaining to next output: 6 minutes, 59 seconds
Output 732/889: t=8420000.0 yr, dE/E0=4.07e-08, N=802
  Estimated time remaining to complete simulation: 18 hours, 16 minutes, 38 seconds
  Estimated time remaining to next output: 6 minutes, 59 seconds
Output 733/889: t=8430000.0 yr, dE/E0=5.20e-08, N=802
  Estimated time remaining to complete simulation: 18 hours, 9 minutes, 18 seconds
  Estimated time remaining to next output: 6 minutes, 58 seconds
Output 734/889: t=8440000.0 yr, dE/E0=5.35e-08, N=802
  Estimated time remaining to complete simulation: 18 hours, 1 minutes, 57 seconds
  Estimated time remaining to next output: 6 minutes, 58 seconds
Output 735/889: t=8450000.0 yr, dE/E0=4.25e-08, N=802
  Estimated time remaining to complete simulation: 17 hours, 54 minutes, 38 seconds
  Estimated time remaining to next output: 6 minutes, 58 seconds
Output 736/889: t=8460000.0 yr, dE/E0=3.93e-08, N=802
  Estimated time remaining to complete simulation: 17 hours, 47 minutes, 20 seconds
  Estimated time remaining to next output: 6 minutes, 58 seconds
Output 737/889: t=8470000.0 yr, dE/E0=4.19e-08, N=802
  Estimated time remaining to complete simulation: 17 hours, 40 minutes, 1 seconds
  Estimated time remaining to next output: 6 minutes, 58 seconds
Output 738/889: t=8480000.0 yr, dE/E0=4.88e-08, N=802
  Estimated time remaining to complete simulation: 17 hours, 32 minutes, 43 seconds
  Estimated time remaining to next output: 6 minutes, 58 seconds
Output 739/889: t=8490000.0 yr, dE/E0=4.21e-08, N=802
  Estimated time remaining to complete simulation: 17 hours, 25 minutes, 25 seconds
  Estimated time remaining to next output: 6 minutes, 58 seconds
Output 740/889: t=8500000.0 yr, dE/E0=4.35e-08, N=802
  Estimated time remaining to complete simulation: 17 hours, 18 minutes, 5 seconds
  Estimated time remaining to next output: 6 minutes, 58 seconds
Output 741/889: t=8510000.0 yr, dE/E0=4.12e-08, N=802
  Estimated time remaining to complete simulation: 17 hours, 10 minutes, 48 seconds
  Estimated time remaining to next output: 6 minutes, 57 seconds
Output 742/889: t=8520000.0 yr, dE/E0=5.13e-08, N=802
  Estimated time remaining to complete simulation: 17 hours, 3 minutes, 28 seconds
  Estimated time remaining to next output: 6 minutes, 57 seconds
Output 743/889: t=8530000.0 yr, dE/E0=5.33e-08, N=802
  Estimated time remaining to complete simulation: 16 hours, 56 minutes, 12 seconds
  Estimated time remaining to next output: 6 minutes, 57 seconds
Output 744/889: t=8540000.0 yr, dE/E0=5.18e-08, N=802
  Estimated time remaining to complete simulation: 16 hours, 48 minutes, 55 seconds
  Estimated time remaining to next output: 6 minutes, 57 seconds
Output 745/889: t=8550000.0 yr, dE/E0=4.86e-08, N=802
  Estimated time remaining to complete simulation: 16 hours, 41 minutes, 36 seconds
  Estimated time remaining to next output: 6 minutes, 57 seconds
Output 746/889: t=8560000.0 yr, dE/E0=4.46e-08, N=802
  Estimated time remaining to complete simulation: 16 hours, 34 minutes, 17 seconds
  Estimated time remaining to next output: 6 minutes, 57 seconds
Output 747/889: t=8570000.0 yr, dE/E0=4.95e-08, N=802
  Estimated time remaining to complete simulation: 16 hours, 27 minutes, 1 seconds
  Estimated time remaining to next output: 6 minutes, 57 seconds
Output 748/889: t=8580000.0 yr, dE/E0=4.58e-08, N=802
  Estimated time remaining to complete simulation: 16 hours, 19 minutes, 44 seconds
  Estimated time remaining to next output: 6 minutes, 56 seconds
Output 749/889: t=8590000.0 yr, dE/E0=5.18e-08, N=802
  Estimated time remaining to complete simulation: 16 hours, 12 minutes, 25 seconds
  Estimated time remaining to next output: 6 minutes, 56 seconds
Output 750/889: t=8600000.0 yr, dE/E0=4.32e-08, N=802
  Estimated time remaining to complete simulation: 16 hours, 5 minutes, 11 seconds
  Estimated time remaining to next output: 6 minutes, 56 seconds
Output 751/889: t=8610000.0 yr, dE/E0=4.91e-08, N=802
  Estimated time remaining to complete simulation: 15 hours, 57 minutes, 57 seconds
  Estimated time remaining to next output: 6 minutes, 56 seconds
Output 752/889: t=8620000.0 yr, dE/E0=5.26e-08, N=802
  Estimated time remaining to complete simulation: 15 hours, 50 minutes, 42 seconds
  Estimated time remaining to next output: 6 minutes, 56 seconds
Output 753/889: t=8630000.0 yr, dE/E0=5.60e-08, N=802
  Estimated time remaining to complete simulation: 15 hours, 43 minutes, 28 seconds
  Estimated time remaining to next output: 6 minutes, 56 seconds
Output 754/889: t=8640000.0 yr, dE/E0=5.49e-08, N=802
  Estimated time remaining to complete simulation: 15 hours, 36 minutes, 18 seconds
  Estimated time remaining to next output: 6 minutes, 56 seconds
Output 755/889: t=8650000.0 yr, dE/E0=4.99e-08, N=802
  Estimated time remaining to complete simulation: 15 hours, 29 minutes, 3 seconds
  Estimated time remaining to next output: 6 minutes, 55 seconds
Output 756/889: t=8660000.0 yr, dE/E0=5.14e-08, N=802
  Estimated time remaining to complete simulation: 15 hours, 21 minutes, 48 seconds
  Estimated time remaining to next output: 6 minutes, 55 seconds
Output 757/889: t=8670000.0 yr, dE/E0=4.44e-08, N=802
  Estimated time remaining to complete simulation: 15 hours, 14 minutes, 36 seconds
  Estimated time remaining to next output: 6 minutes, 55 seconds
Output 758/889: t=8680000.0 yr, dE/E0=5.87e-08, N=802
  Estimated time remaining to complete simulation: 15 hours, 7 minutes, 23 seconds
  Estimated time remaining to next output: 6 minutes, 55 seconds
Output 759/889: t=8690000.0 yr, dE/E0=6.40e-08, N=802
  Estimated time remaining to complete simulation: 15 hours, 11 seconds
  Estimated time remaining to next output: 6 minutes, 55 seconds
Output 760/889: t=8700000.0 yr, dE/E0=6.90e-08, N=802
  Estimated time remaining to complete simulation: 14 hours, 52 minutes, 55 seconds
  Estimated time remaining to next output: 6 minutes, 55 seconds
Output 761/889: t=8710000.0 yr, dE/E0=6.12e-08, N=802
  Estimated time remaining to complete simulation: 14 hours, 45 minutes, 43 seconds
  Estimated time remaining to next output: 6 minutes, 55 seconds
Output 762/889: t=8720000.0 yr, dE/E0=6.44e-08, N=802
  Estimated time remaining to complete simulation: 14 hours, 38 minutes, 32 seconds
  Estimated time remaining to next output: 6 minutes, 55 seconds
Output 763/889: t=8730000.0 yr, dE/E0=5.48e-08, N=802
  Estimated time remaining to complete simulation: 14 hours, 31 minutes, 19 seconds
  Estimated time remaining to next output: 6 minutes, 54 seconds
Output 764/889: t=8740000.0 yr, dE/E0=5.93e-08, N=802
  Estimated time remaining to complete simulation: 14 hours, 24 minutes, 9 seconds
  Estimated time remaining to next output: 6 minutes, 54 seconds
Output 765/889: t=8750000.0 yr, dE/E0=5.52e-08, N=802
  Estimated time remaining to complete simulation: 14 hours, 17 minutes
  Estimated time remaining to next output: 6 minutes, 54 seconds
Output 766/889: t=8760000.0 yr, dE/E0=6.66e-08, N=802
  Estimated time remaining to complete simulation: 14 hours, 9 minutes, 50 seconds
  Estimated time remaining to next output: 6 minutes, 54 seconds
Output 767/889: t=8770000.0 yr, dE/E0=5.65e-08, N=802
  Estimated time remaining to complete simulation: 14 hours, 2 minutes, 37 seconds
  Estimated time remaining to next output: 6 minutes, 54 seconds
Output 768/889: t=8780000.0 yr, dE/E0=5.86e-08, N=802
  Estimated time remaining to complete simulation: 13 hours, 55 minutes, 27 seconds
  Estimated time remaining to next output: 6 minutes, 54 seconds
Output 769/889: t=8790000.0 yr, dE/E0=7.53e-08, N=802
  Estimated time remaining to complete simulation: 13 hours, 48 minutes, 17 seconds
  Estimated time remaining to next output: 6 minutes, 54 seconds
Output 770/889: t=8800000.0 yr, dE/E0=6.21e-08, N=802
  Estimated time remaining to complete simulation: 13 hours, 41 minutes, 10 seconds
  Estimated time remaining to next output: 6 minutes, 54 seconds
Output 771/889: t=8810000.0 yr, dE/E0=5.92e-08, N=802
  Estimated time remaining to complete simulation: 13 hours, 34 minutes, 2 seconds
  Estimated time remaining to next output: 6 minutes, 53 seconds
Output 772/889: t=8820000.0 yr, dE/E0=6.30e-08, N=802
  Estimated time remaining to complete simulation: 13 hours, 26 minutes, 55 seconds
  Estimated time remaining to next output: 6 minutes, 53 seconds
Output 773/889: t=8830000.0 yr, dE/E0=7.23e-08, N=802
  Estimated time remaining to complete simulation: 13 hours, 19 minutes, 46 seconds
  Estimated time remaining to next output: 6 minutes, 53 seconds
Output 774/889: t=8840000.0 yr, dE/E0=7.28e-08, N=802
  Estimated time remaining to complete simulation: 13 hours, 12 minutes, 37 seconds
  Estimated time remaining to next output: 6 minutes, 53 seconds
Output 775/889: t=8850000.0 yr, dE/E0=6.84e-08, N=802
  Estimated time remaining to complete simulation: 13 hours, 5 minutes, 30 seconds
  Estimated time remaining to next output: 6 minutes, 53 seconds
Output 776/889: t=8860000.0 yr, dE/E0=6.06e-08, N=802
  Estimated time remaining to complete simulation: 12 hours, 58 minutes, 21 seconds
  Estimated time remaining to next output: 6 minutes, 53 seconds
Output 777/889: t=8870000.0 yr, dE/E0=6.75e-08, N=802
  Estimated time remaining to complete simulation: 12 hours, 51 minutes, 15 seconds
  Estimated time remaining to next output: 6 minutes, 53 seconds
Output 778/889: t=8880000.0 yr, dE/E0=6.88e-08, N=802
  Estimated time remaining to complete simulation: 12 hours, 44 minutes, 8 seconds
  Estimated time remaining to next output: 6 minutes, 53 seconds
Output 779/889: t=8890000.0 yr, dE/E0=6.00e-08, N=802
  Estimated time remaining to complete simulation: 12 hours, 37 minutes, 3 seconds
  Estimated time remaining to next output: 6 minutes, 52 seconds
Output 780/889: t=8900000.0 yr, dE/E0=5.72e-08, N=802
  Estimated time remaining to complete simulation: 12 hours, 29 minutes, 57 seconds
  Estimated time remaining to next output: 6 minutes, 52 seconds
Output 781/889: t=8910000.0 yr, dE/E0=5.17e-08, N=802
  Estimated time remaining to complete simulation: 12 hours, 22 minutes, 49 seconds
  Estimated time remaining to next output: 6 minutes, 52 seconds
Output 782/889: t=8920000.0 yr, dE/E0=6.06e-08, N=802
  Estimated time remaining to complete simulation: 12 hours, 15 minutes, 42 seconds
  Estimated time remaining to next output: 6 minutes, 52 seconds
Output 783/889: t=8930000.0 yr, dE/E0=5.28e-08, N=802
  Estimated time remaining to complete simulation: 12 hours, 8 minutes, 35 seconds
  Estimated time remaining to next output: 6 minutes, 52 seconds
Output 784/889: t=8940000.0 yr, dE/E0=3.93e-08, N=802
  Estimated time remaining to complete simulation: 12 hours, 1 minutes, 28 seconds
  Estimated time remaining to next output: 6 minutes, 52 seconds
Output 785/889: t=8950000.0 yr, dE/E0=4.98e-08, N=802
  Estimated time remaining to complete simulation: 11 hours, 54 minutes, 22 seconds
  Estimated time remaining to next output: 6 minutes, 52 seconds
Output 786/889: t=8960000.0 yr, dE/E0=4.30e-08, N=802
  Estimated time remaining to complete simulation: 11 hours, 47 minutes, 18 seconds
  Estimated time remaining to next output: 6 minutes, 52 seconds
Output 787/889: t=8970000.0 yr, dE/E0=5.04e-08, N=802
  Estimated time remaining to complete simulation: 11 hours, 40 minutes, 15 seconds
  Estimated time remaining to next output: 6 minutes, 51 seconds
Output 788/889: t=8980000.0 yr, dE/E0=4.84e-08, N=802
  Estimated time remaining to complete simulation: 11 hours, 33 minutes, 10 seconds
  Estimated time remaining to next output: 6 minutes, 51 seconds
Output 789/889: t=8990000.0 yr, dE/E0=5.24e-08, N=802
  Estimated time remaining to complete simulation: 11 hours, 26 minutes, 9 seconds
  Estimated time remaining to next output: 6 minutes, 51 seconds
Output 790/889: t=9000000.0 yr, dE/E0=5.77e-08, N=802
  Estimated time remaining to complete simulation: 11 hours, 19 minutes, 3 seconds
  Estimated time remaining to next output: 6 minutes, 51 seconds
Output 791/889: t=9010000.0 yr, dE/E0=5.54e-08, N=802
  Estimated time remaining to complete simulation: 11 hours, 12 minutes
  Estimated time remaining to next output: 6 minutes, 51 seconds
Output 792/889: t=9020000.0 yr, dE/E0=4.63e-08, N=802
  Estimated time remaining to complete simulation: 11 hours, 4 minutes, 57 seconds
  Estimated time remaining to next output: 6 minutes, 51 seconds
Output 793/889: t=9030000.0 yr, dE/E0=4.57e-08, N=802
  Estimated time remaining to complete simulation: 10 hours, 57 minutes, 54 seconds
  Estimated time remaining to next output: 6 minutes, 51 seconds
Output 794/889: t=9040000.0 yr, dE/E0=4.76e-08, N=802
  Estimated time remaining to complete simulation: 10 hours, 50 minutes, 49 seconds
  Estimated time remaining to next output: 6 minutes, 51 seconds
Output 795/889: t=9050000.0 yr, dE/E0=4.87e-08, N=802
  Estimated time remaining to complete simulation: 10 hours, 43 minutes, 47 seconds
  Estimated time remaining to next output: 6 minutes, 50 seconds
Output 796/889: t=9060000.0 yr, dE/E0=6.41e-08, N=802
  Estimated time remaining to complete simulation: 10 hours, 36 minutes, 45 seconds
  Estimated time remaining to next output: 6 minutes, 50 seconds
Output 797/889: t=9070000.0 yr, dE/E0=5.05e-08, N=802
  Estimated time remaining to complete simulation: 10 hours, 29 minutes, 47 seconds
  Estimated time remaining to next output: 6 minutes, 50 seconds
Output 798/889: t=9080000.0 yr, dE/E0=4.88e-08, N=802
  Estimated time remaining to complete simulation: 10 hours, 22 minutes, 43 seconds
  Estimated time remaining to next output: 6 minutes, 50 seconds
Output 799/889: t=9090000.0 yr, dE/E0=5.06e-08, N=802
  Estimated time remaining to complete simulation: 10 hours, 15 minutes, 42 seconds
  Estimated time remaining to next output: 6 minutes, 50 seconds
Output 800/889: t=9100000.0 yr, dE/E0=5.88e-08, N=802
  Estimated time remaining to complete simulation: 10 hours, 8 minutes, 42 seconds
  Estimated time remaining to next output: 6 minutes, 50 seconds
Output 801/889: t=9110000.0 yr, dE/E0=4.80e-08, N=802
  Estimated time remaining to complete simulation: 10 hours, 1 minutes, 39 seconds
  Estimated time remaining to next output: 6 minutes, 50 seconds
Output 802/889: t=9120000.0 yr, dE/E0=4.89e-08, N=802
  Estimated time remaining to complete simulation: 9 hours, 54 minutes, 38 seconds
  Estimated time remaining to next output: 6 minutes, 50 seconds
Output 803/889: t=9130000.0 yr, dE/E0=6.16e-08, N=802
  Estimated time remaining to complete simulation: 9 hours, 47 minutes, 37 seconds
  Estimated time remaining to next output: 6 minutes, 49 seconds
Output 804/889: t=9140000.0 yr, dE/E0=6.23e-08, N=802
  Estimated time remaining to complete simulation: 9 hours, 40 minutes, 36 seconds
  Estimated time remaining to next output: 6 minutes, 49 seconds
Output 805/889: t=9150000.0 yr, dE/E0=6.50e-08, N=802
  Estimated time remaining to complete simulation: 9 hours, 33 minutes, 34 seconds
  Estimated time remaining to next output: 6 minutes, 49 seconds
Output 806/889: t=9160000.0 yr, dE/E0=5.13e-08, N=802
  Estimated time remaining to complete simulation: 9 hours, 26 minutes, 34 seconds
  Estimated time remaining to next output: 6 minutes, 49 seconds
Output 807/889: t=9170000.0 yr, dE/E0=5.69e-08, N=802
  Estimated time remaining to complete simulation: 9 hours, 19 minutes, 34 seconds
  Estimated time remaining to next output: 6 minutes, 49 seconds
Output 808/889: t=9180000.0 yr, dE/E0=6.11e-08, N=802
  Estimated time remaining to complete simulation: 9 hours, 12 minutes, 32 seconds
  Estimated time remaining to next output: 6 minutes, 49 seconds
Output 809/889: t=9190000.0 yr, dE/E0=6.56e-08, N=802
  Estimated time remaining to complete simulation: 9 hours, 5 minutes, 35 seconds
  Estimated time remaining to next output: 6 minutes, 49 seconds
Output 810/889: t=9200000.0 yr, dE/E0=6.07e-08, N=802
  Estimated time remaining to complete simulation: 8 hours, 58 minutes, 35 seconds
  Estimated time remaining to next output: 6 minutes, 49 seconds
Output 811/889: t=9210000.0 yr, dE/E0=5.50e-08, N=802
  Estimated time remaining to complete simulation: 8 hours, 51 minutes, 38 seconds
  Estimated time remaining to next output: 6 minutes, 48 seconds
Output 812/889: t=9220000.0 yr, dE/E0=6.18e-08, N=802
  Estimated time remaining to complete simulation: 8 hours, 44 minutes, 40 seconds
  Estimated time remaining to next output: 6 minutes, 48 seconds
Output 813/889: t=9230000.0 yr, dE/E0=6.51e-08, N=802
  Estimated time remaining to complete simulation: 8 hours, 37 minutes, 42 seconds
  Estimated time remaining to next output: 6 minutes, 48 seconds
Output 814/889: t=9240000.0 yr, dE/E0=6.58e-08, N=802
  Estimated time remaining to complete simulation: 8 hours, 30 minutes, 43 seconds
  Estimated time remaining to next output: 6 minutes, 48 seconds
Output 815/889: t=9250000.0 yr, dE/E0=6.60e-08, N=802
  Estimated time remaining to complete simulation: 8 hours, 23 minutes, 47 seconds
  Estimated time remaining to next output: 6 minutes, 48 seconds
Output 816/889: t=9260000.0 yr, dE/E0=6.96e-08, N=802
  Estimated time remaining to complete simulation: 8 hours, 16 minutes, 51 seconds
  Estimated time remaining to next output: 6 minutes, 48 seconds
Output 817/889: t=9270000.0 yr, dE/E0=7.35e-08, N=802
  Estimated time remaining to complete simulation: 8 hours, 9 minutes, 53 seconds
  Estimated time remaining to next output: 6 minutes, 48 seconds
Output 818/889: t=9280000.0 yr, dE/E0=6.97e-08, N=802
  Estimated time remaining to complete simulation: 8 hours, 2 minutes, 57 seconds
  Estimated time remaining to next output: 6 minutes, 48 seconds
Output 819/889: t=9290000.0 yr, dE/E0=7.05e-08, N=802
  Estimated time remaining to complete simulation: 7 hours, 56 minutes, 1 seconds
  Estimated time remaining to next output: 6 minutes, 48 seconds
Output 820/889: t=9300000.0 yr, dE/E0=6.03e-08, N=802
  Estimated time remaining to complete simulation: 7 hours, 49 minutes, 6 seconds
  Estimated time remaining to next output: 6 minutes, 47 seconds
Output 821/889: t=9310000.0 yr, dE/E0=6.46e-08, N=802
  Estimated time remaining to complete simulation: 7 hours, 42 minutes, 10 seconds
  Estimated time remaining to next output: 6 minutes, 47 seconds
Output 822/889: t=9320000.0 yr, dE/E0=6.73e-08, N=802
  Estimated time remaining to complete simulation: 7 hours, 35 minutes, 15 seconds
  Estimated time remaining to next output: 6 minutes, 47 seconds
Output 823/889: t=9330000.0 yr, dE/E0=7.58e-08, N=802
  Estimated time remaining to complete simulation: 7 hours, 28 minutes, 21 seconds
  Estimated time remaining to next output: 6 minutes, 47 seconds
Output 824/889: t=9340000.0 yr, dE/E0=4.87e-08, N=802
  Estimated time remaining to complete simulation: 7 hours, 21 minutes, 26 seconds
  Estimated time remaining to next output: 6 minutes, 47 seconds
Output 825/889: t=9350000.0 yr, dE/E0=6.20e-08, N=802
  Estimated time remaining to complete simulation: 7 hours, 14 minutes, 32 seconds
  Estimated time remaining to next output: 6 minutes, 47 seconds
Output 826/889: t=9360000.0 yr, dE/E0=6.97e-08, N=802
  Estimated time remaining to complete simulation: 7 hours, 7 minutes, 38 seconds
  Estimated time remaining to next output: 6 minutes, 47 seconds
Output 827/889: t=9370000.0 yr, dE/E0=7.44e-08, N=802
  Estimated time remaining to complete simulation: 7 hours, 44 seconds
  Estimated time remaining to next output: 6 minutes, 47 seconds
Output 828/889: t=9380000.0 yr, dE/E0=6.60e-08, N=802
  Estimated time remaining to complete simulation: 6 hours, 53 minutes, 51 seconds
  Estimated time remaining to next output: 6 minutes, 47 seconds
Output 829/889: t=9390000.0 yr, dE/E0=6.74e-08, N=802
  Estimated time remaining to complete simulation: 6 hours, 46 minutes, 56 seconds
  Estimated time remaining to next output: 6 minutes, 46 seconds
Output 830/889: t=9400000.0 yr, dE/E0=6.38e-08, N=802
  Estimated time remaining to complete simulation: 6 hours, 40 minutes, 2 seconds
  Estimated time remaining to next output: 6 minutes, 46 seconds
Output 831/889: t=9410000.0 yr, dE/E0=6.34e-08, N=802
  Estimated time remaining to complete simulation: 6 hours, 33 minutes, 10 seconds
  Estimated time remaining to next output: 6 minutes, 46 seconds
Output 832/889: t=9420000.0 yr, dE/E0=5.68e-08, N=802
  Estimated time remaining to complete simulation: 6 hours, 26 minutes, 17 seconds
  Estimated time remaining to next output: 6 minutes, 46 seconds
Output 833/889: t=9430000.0 yr, dE/E0=5.20e-08, N=802
  Estimated time remaining to complete simulation: 6 hours, 19 minutes, 24 seconds
  Estimated time remaining to next output: 6 minutes, 46 seconds
Output 834/889: t=9440000.0 yr, dE/E0=5.19e-08, N=802
  Estimated time remaining to complete simulation: 6 hours, 12 minutes, 29 seconds
  Estimated time remaining to next output: 6 minutes, 46 seconds
Output 835/889: t=9450000.0 yr, dE/E0=6.01e-08, N=802
  Estimated time remaining to complete simulation: 6 hours, 5 minutes, 37 seconds
  Estimated time remaining to next output: 6 minutes, 46 seconds
Output 836/889: t=9460000.0 yr, dE/E0=6.85e-08, N=802
  Estimated time remaining to complete simulation: 5 hours, 58 minutes, 45 seconds
  Estimated time remaining to next output: 6 minutes, 46 seconds
Output 837/889: t=9470000.0 yr, dE/E0=6.61e-08, N=802
  Estimated time remaining to complete simulation: 5 hours, 51 minutes, 54 seconds
  Estimated time remaining to next output: 6 minutes, 46 seconds
Output 838/889: t=9480000.0 yr, dE/E0=5.49e-08, N=802
  Estimated time remaining to complete simulation: 5 hours, 45 minutes, 1 seconds
  Estimated time remaining to next output: 6 minutes, 45 seconds
Output 839/889: t=9490000.0 yr, dE/E0=6.92e-08, N=802
  Estimated time remaining to complete simulation: 5 hours, 38 minutes, 11 seconds
  Estimated time remaining to next output: 6 minutes, 45 seconds
Output 840/889: t=9500000.0 yr, dE/E0=6.53e-08, N=802
  Estimated time remaining to complete simulation: 5 hours, 31 minutes, 20 seconds
  Estimated time remaining to next output: 6 minutes, 45 seconds
Output 841/889: t=9510000.0 yr, dE/E0=6.57e-08, N=802
  Estimated time remaining to complete simulation: 5 hours, 24 minutes, 30 seconds
  Estimated time remaining to next output: 6 minutes, 45 seconds
Output 842/889: t=9520000.0 yr, dE/E0=6.19e-08, N=802
  Estimated time remaining to complete simulation: 5 hours, 17 minutes, 40 seconds
  Estimated time remaining to next output: 6 minutes, 45 seconds
Output 843/889: t=9530000.0 yr, dE/E0=6.40e-08, N=802
  Estimated time remaining to complete simulation: 5 hours, 10 minutes, 50 seconds
  Estimated time remaining to next output: 6 minutes, 45 seconds
Output 844/889: t=9540000.0 yr, dE/E0=6.60e-08, N=802
  Estimated time remaining to complete simulation: 5 hours, 3 minutes, 59 seconds
  Estimated time remaining to next output: 6 minutes, 45 seconds
Output 845/889: t=9550000.0 yr, dE/E0=6.64e-08, N=802
  Estimated time remaining to complete simulation: 4 hours, 57 minutes, 9 seconds
  Estimated time remaining to next output: 6 minutes, 45 seconds
Output 846/889: t=9560000.0 yr, dE/E0=5.99e-08, N=802
  Estimated time remaining to complete simulation: 4 hours, 50 minutes, 19 seconds
  Estimated time remaining to next output: 6 minutes, 45 seconds
Output 847/889: t=9570000.0 yr, dE/E0=6.33e-08, N=802
  Estimated time remaining to complete simulation: 4 hours, 43 minutes, 29 seconds
  Estimated time remaining to next output: 6 minutes, 44 seconds
Output 848/889: t=9580000.0 yr, dE/E0=5.71e-08, N=802
  Estimated time remaining to complete simulation: 4 hours, 36 minutes, 40 seconds
  Estimated time remaining to next output: 6 minutes, 44 seconds
Output 849/889: t=9590000.0 yr, dE/E0=4.64e-08, N=802
  Estimated time remaining to complete simulation: 4 hours, 29 minutes, 51 seconds
  Estimated time remaining to next output: 6 minutes, 44 seconds
Output 850/889: t=9600000.0 yr, dE/E0=5.74e-08, N=802
  Estimated time remaining to complete simulation: 4 hours, 23 minutes, 2 seconds
  Estimated time remaining to next output: 6 minutes, 44 seconds
Output 851/889: t=9610000.0 yr, dE/E0=6.00e-08, N=802
  Estimated time remaining to complete simulation: 4 hours, 16 minutes, 13 seconds
  Estimated time remaining to next output: 6 minutes, 44 seconds
Output 852/889: t=9620000.0 yr, dE/E0=6.03e-08, N=802
  Estimated time remaining to complete simulation: 4 hours, 9 minutes, 24 seconds
  Estimated time remaining to next output: 6 minutes, 44 seconds
Output 853/889: t=9630000.0 yr, dE/E0=5.94e-08, N=802
  Estimated time remaining to complete simulation: 4 hours, 2 minutes, 35 seconds
  Estimated time remaining to next output: 6 minutes, 44 seconds
Output 854/889: t=9640000.0 yr, dE/E0=5.49e-08, N=802
  Estimated time remaining to complete simulation: 3 hours, 55 minutes, 46 seconds
  Estimated time remaining to next output: 6 minutes, 44 seconds
Output 855/889: t=9650000.0 yr, dE/E0=5.34e-08, N=802
  Estimated time remaining to complete simulation: 3 hours, 48 minutes, 57 seconds
  Estimated time remaining to next output: 6 minutes, 44 seconds
Output 856/889: t=9660000.0 yr, dE/E0=5.71e-08, N=802
  Estimated time remaining to complete simulation: 3 hours, 42 minutes, 9 seconds
  Estimated time remaining to next output: 6 minutes, 43 seconds
Output 857/889: t=9670000.0 yr, dE/E0=5.72e-08, N=802
  Estimated time remaining to complete simulation: 3 hours, 35 minutes, 21 seconds
  Estimated time remaining to next output: 6 minutes, 43 seconds
Output 858/889: t=9680000.0 yr, dE/E0=6.76e-08, N=802
  Estimated time remaining to complete simulation: 3 hours, 28 minutes, 33 seconds
  Estimated time remaining to next output: 6 minutes, 43 seconds
Output 859/889: t=9690000.0 yr, dE/E0=6.61e-08, N=802
  Estimated time remaining to complete simulation: 3 hours, 21 minutes, 47 seconds
  Estimated time remaining to next output: 6 minutes, 43 seconds
Output 860/889: t=9700000.0 yr, dE/E0=6.82e-08, N=802
  Estimated time remaining to complete simulation: 3 hours, 15 minutes
  Estimated time remaining to next output: 6 minutes, 43 seconds
Output 861/889: t=9710000.0 yr, dE/E0=7.22e-08, N=802
  Estimated time remaining to complete simulation: 3 hours, 8 minutes, 14 seconds
  Estimated time remaining to next output: 6 minutes, 43 seconds
Output 862/889: t=9720000.0 yr, dE/E0=7.79e-08, N=802
  Estimated time remaining to complete simulation: 3 hours, 1 minutes, 27 seconds
  Estimated time remaining to next output: 6 minutes, 43 seconds
Output 863/889: t=9730000.0 yr, dE/E0=7.49e-08, N=802
  Estimated time remaining to complete simulation: 2 hours, 54 minutes, 41 seconds
  Estimated time remaining to next output: 6 minutes, 43 seconds
Output 864/889: t=9740000.0 yr, dE/E0=6.70e-08, N=802
  Estimated time remaining to complete simulation: 2 hours, 47 minutes, 55 seconds
  Estimated time remaining to next output: 6 minutes, 43 seconds
Output 865/889: t=9750000.0 yr, dE/E0=6.85e-08, N=802
  Estimated time remaining to complete simulation: 2 hours, 41 minutes, 9 seconds
  Estimated time remaining to next output: 6 minutes, 42 seconds
Output 866/889: t=9760000.0 yr, dE/E0=6.52e-08, N=802
  Estimated time remaining to complete simulation: 2 hours, 34 minutes, 24 seconds
  Estimated time remaining to next output: 6 minutes, 42 seconds
Output 867/889: t=9770000.0 yr, dE/E0=7.32e-08, N=802
  Estimated time remaining to complete simulation: 2 hours, 27 minutes, 39 seconds
  Estimated time remaining to next output: 6 minutes, 42 seconds
Output 868/889: t=9780000.0 yr, dE/E0=6.42e-08, N=802
  Estimated time remaining to complete simulation: 2 hours, 20 minutes, 53 seconds
  Estimated time remaining to next output: 6 minutes, 42 seconds
Output 869/889: t=9790000.0 yr, dE/E0=6.20e-08, N=802
  Estimated time remaining to complete simulation: 2 hours, 14 minutes, 8 seconds
  Estimated time remaining to next output: 6 minutes, 42 seconds
Output 870/889: t=9800000.0 yr, dE/E0=6.09e-08, N=802
  Estimated time remaining to complete simulation: 2 hours, 7 minutes, 23 seconds
  Estimated time remaining to next output: 6 minutes, 42 seconds
Output 871/889: t=9810000.0 yr, dE/E0=5.19e-08, N=802
  Estimated time remaining to complete simulation: 2 hours, 39 seconds
  Estimated time remaining to next output: 6 minutes, 42 seconds
Output 872/889: t=9820000.0 yr, dE/E0=6.78e-08, N=802
  Estimated time remaining to complete simulation: 1 hours, 53 minutes, 54 seconds
  Estimated time remaining to next output: 6 minutes, 42 seconds
Output 873/889: t=9830000.0 yr, dE/E0=6.55e-08, N=802
  Estimated time remaining to complete simulation: 1 hours, 47 minutes, 10 seconds
  Estimated time remaining to next output: 6 minutes, 41 seconds
Output 874/889: t=9840000.0 yr, dE/E0=5.10e-08, N=802
  Estimated time remaining to complete simulation: 1 hours, 40 minutes, 26 seconds
  Estimated time remaining to next output: 6 minutes, 41 seconds
Output 875/889: t=9850000.0 yr, dE/E0=6.80e-08, N=802
  Estimated time remaining to complete simulation: 1 hours, 33 minutes, 43 seconds
  Estimated time remaining to next output: 6 minutes, 41 seconds
Output 876/889: t=9860000.0 yr, dE/E0=6.21e-08, N=802
  Estimated time remaining to complete simulation: 1 hours, 27 minutes
  Estimated time remaining to next output: 6 minutes, 41 seconds
Output 877/889: t=9870000.0 yr, dE/E0=5.75e-08, N=802
  Estimated time remaining to complete simulation: 1 hours, 20 minutes, 17 seconds
  Estimated time remaining to next output: 6 minutes, 41 seconds
Output 878/889: t=9880000.0 yr, dE/E0=5.75e-08, N=802
  Estimated time remaining to complete simulation: 1 hours, 13 minutes, 34 seconds
  Estimated time remaining to next output: 6 minutes, 41 seconds
Output 879/889: t=9890000.0 yr, dE/E0=5.84e-08, N=802
  Estimated time remaining to complete simulation: 1 hours, 6 minutes, 52 seconds
  Estimated time remaining to next output: 6 minutes, 41 seconds
Output 880/889: t=9900000.0 yr, dE/E0=6.95e-08, N=802
  Estimated time remaining to complete simulation: 1 hours, 9 seconds
  Estimated time remaining to next output: 6 minutes, 41 seconds
Output 881/889: t=9910000.0 yr, dE/E0=7.24e-08, N=802
  Estimated time remaining to complete simulation: 53 minutes, 28 seconds
  Estimated time remaining to next output: 6 minutes, 41 seconds
Output 882/889: t=9920000.0 yr, dE/E0=5.52e-08, N=802
  Estimated time remaining to complete simulation: 46 minutes, 46 seconds
  Estimated time remaining to next output: 6 minutes, 40 seconds
Output 883/889: t=9930000.0 yr, dE/E0=6.83e-08, N=802
  Estimated time remaining to complete simulation: 40 minutes, 4 seconds
  Estimated time remaining to next output: 6 minutes, 40 seconds
Output 884/889: t=9940000.0 yr, dE/E0=6.86e-08, N=802
  Estimated time remaining to complete simulation: 33 minutes, 23 seconds
  Estimated time remaining to next output: 6 minutes, 40 seconds
Output 885/889: t=9950000.0 yr, dE/E0=7.80e-08, N=802
  Estimated time remaining to complete simulation: 26 minutes, 42 seconds
  Estimated time remaining to next output: 6 minutes, 40 seconds
Output 886/889: t=9960000.0 yr, dE/E0=6.53e-08, N=802
  Estimated time remaining to complete simulation: 20 minutes, 1 seconds
  Estimated time remaining to next output: 6 minutes, 40 seconds
Output 887/889: t=9970000.0 yr, dE/E0=6.64e-08, N=802
  Estimated time remaining to complete simulation: 13 minutes, 20 seconds
  Estimated time remaining to next output: 6 minutes, 40 seconds
Output 888/889: t=9980000.0 yr, dE/E0=7.02e-08, N=802
  Estimated time remaining to complete simulation: 6 minutes, 40 seconds
  Estimated time remaining to next output: 6 minutes, 40 seconds
Output 889/889: t=9990000.0 yr, dE/E0=6.35e-08, N=802
  Estimated time remaining to complete simulation: 0 seconds
Output 890/889: t=10000000.0 yr, dE/E0=6.85e-08, N=802
  Estimated time remaining to complete simulation: -1 months, 4 weeks, 1 days, 23 hours, 53 minutes, 21 seconds

Simulation complete.
Total runtime: 4 days, 2 hours, 52 minutes, 2 seconds

Krivov & Booth (2018) self-stirring check (Eqs. 9-10):
  NOTE: a giant planet is present; the two-population self-stirring model assumes no external perturber, so C_e below is only indicative.
  Final time:                 t = 1.000000e+07 yr
  Rayleigh outlier cut:       e > 5 sigma = 1.7099e-01 (sigma = median(e)/sqrt(2 ln 2) = 3.4199e-02)
  Stirred-disk check:         median(e) = 4.0266e-02 vs 30 x disk.emax = 9.6000e-04 -> stirred, cut applied
  Excluded MPs:               1 -- MP_448 (e = 0.7334)
  KS test of kept e vs Rayleigh: D = 0.0787, p = 9.36e-05  (WARNING: p < 0.05, kept e deviates from a Rayleigh distribution)
  RMS eccentricity (799 of 800 MPs): 5.311474e-02  (all MPs: 5.907570e-02)
  Belt geometry:              a = 100, da = 10, a/da = 10
  Masses:                     M_max = 6.368760e-09 Msun, M_disc = 3.003490e-06 Msun
  Implied stirring timescale: T = 2.512869e+12 yr
  Effective stirring factor:  C_e = 2080.4499  (all MPs, no cut: 3183.7051)
  WARNING: C_e = 2080.4499 >= 40 (Ida & Makino 1993 canonical value) -- this run stirs at or above the analytic self-stirring rate.
Saved archive: outputs/SS_800MP_10Myr_PSD2A_1Mjup_lorentzian/SS_800MP_10Myr_PSD2A_1Mjup_lorentzian.bin
Number of snapshots saved: 1002
Archive time range: 0.000e+00 yr to 1.000e+07 yr
Particle-name check: OK (1002 snapshots)
Loaded snapshot table from archive.
role
massive_planetesimal    800
star                      1
giant_planet              1
Name: count, dtype: int64
Saved: outputs/SS_800MP_10Myr_PSD2A_1Mjup_lorentzian/figures/survival_fraction_vs_time.png
Saved: outputs/SS_800MP_10Myr_PSD2A_1Mjup_lorentzian/figures/mean_semimajor_axis_vs_time.png
Saved: outputs/SS_800MP_10Myr_PSD2A_1Mjup_lorentzian/figures/mean_eccentricity_vs_time.png
Saved: outputs/SS_800MP_10Myr_PSD2A_1Mjup_lorentzian/figures/rms_eccentricity_vs_time.png
Saved: outputs/SS_800MP_10Myr_PSD2A_1Mjup_lorentzian/figures/rms_inclination_vs_time.png
Saved: outputs/SS_800MP_10Myr_PSD2A_1Mjup_lorentzian/figures/data/orbits_initial_final.csv
Saved: outputs/SS_800MP_10Myr_PSD2A_1Mjup_lorentzian/figures/a_vs_e_initial_final.png
Saved: outputs/SS_800MP_10Myr_PSD2A_1Mjup_lorentzian/figures/a_vs_i_initial_final.png
Inner plotted edge = 95.04 AU
Outer plotted edge = 104.92 AU
Saved: outputs/SS_800MP_10Myr_PSD2A_1Mjup_lorentzian/figures/xy_initial_final.png
All summary figures saved.
```
