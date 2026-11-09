# SS_800MP_10Myr_PSD2B_100Mearth_lorentzian — Simulation Report

Config file: `config/SS_800MP_10Myr_PSD2B_100Mearth_lorentzian.yaml`
Archive file: `outputs/SS_800MP_10Myr_PSD2B_100Mearth_lorentzian/SS_800MP_10Myr_PSD2B_100Mearth_lorentzian.bin`

## Provenance

- Run UUID: `74ce6c25-435b-41de-8f13-3c785d404f89`
- Created: 2026-10-14T17:56:04-03:00
- Finished: 2026-10-25T17:01:22-03:00
- Wall runtime: 527797.4 s
- Outcome: completed
- Command: `src/simulation/run_simulation.py config/SS_800MP_10Myr_PSD2B_100Mearth_lorentzian.yaml`
- Git commit: `e2f4500c1dff6271650542698ba60951c8d5f7ff` (branch `main`) **(DIRTY — uncommitted tracked changes)**
    - modified: `notebooks/mass_model_playground.ipynb`
- Software: python 3.12.14, rebound 5.0.0, numpy 2.4.6, pandas 3.0.3, matplotlib 3.10.9, pyyaml 6.0.3
- Resumed 1 time(s) after the first run
- Frozen config: `config.yaml` (this directory)
- Full environment: `environment.txt` (this directory)

## Simulation
- Name: SS_800MP_10Myr_PSD2B_100Mearth_lorentzian
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
- Mass: 0.3145707 Mjup
- a: 77.132335 au, e: 0.0, inc: 0.0 deg
- omega: 0.0 deg, Omega random: True
- t_peri_jd: 2451545.0, orbital_period_days: 247425.776, epoch_jd: 2451545.0

## Disk
- a: [95, 105] au
- a distribution: Lorentzian in ln a, mu_0 = 100 au, sigma = 1 au
- e: [0.0, 3.2e-05]
- inc: [0.0, 3.2e-05] deg

## Massive Planetesimals
- N: 800
- Mass-assignment method (config): loaded from CSV (mode=csv): variable=radius, path=src/mass_models/Plantesimal_Size_Dist_2_1Mearth/model_B/selected.csv, slope=3.5 (radii/masses read verbatim from file; disk mass computed from file, not split by a power law)
- **Mass is NOT uniform** across the 800 massive planetesimals:
  - min / median / max: 1.003434e-09 / 2.194171e-09 / 2.152034e-08 Msun
  - min / median / max: 3.340893e-04 / 7.305407e-04 / 7.165112e-03 Earth masses
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
Saving SimulationArchive to: outputs/SS_800MP_10Myr_PSD2B_100Mearth_lorentzian/SS_800MP_10Myr_PSD2B_100Mearth_lorentzian.bin
Resuming from t=2.300000e+05 yr: times=array([  230000.,   240000.,   250000.,   260000.,   270000.,   280000.,
         290000.,   300000.,   310000.,   320000.,   330000.,   340000.,
         350000.,   360000.,   370000.,   380000.,   390000.,   400000.,
         410000.,   420000.,   430000.,   440000.,   450000.,   460000.,
         470000.,   480000.,   490000.,   500000.,   510000.,   520000.,
         530000.,   540000.,   550000.,   560000.,   570000.,   580000.,
         590000.,   600000.,   610000.,   620000.,   630000.,   640000.,
         650000.,   660000.,   670000.,   680000.,   690000.,   700000.,
         710000.,   720000.,   730000.,   740000.,   750000.,   760000.,
         770000.,   780000.,   790000.,   800000.,   810000.,   820000.,
         830000.,   840000.,   850000.,   860000.,   870000.,   880000.,
         890000.,   900000.,   910000.,   920000.,   930000.,   940000.,
         950000.,   960000.,   970000.,   980000.,   990000.,  1000000.,
        1010000.,  1020000.,  1030000.,  1040000.,  1050000.,  1060000.,
        1070000.,  1080000.,  1090000.,  1100000.,  1110000.,  1120000.,
        1130000.,  1140000.,  1150000.,  1160000.,  1170000.,  1180000.,
        1190000.,  1200000.,  1210000.,  1220000.,  1230000.,  1240000.,
        1250000.,  1260000.,  1270000.,  1280000.,  1290000.,  1300000.,
        1310000.,  1320000.,  1330000.,  1340000.,  1350000.,  1360000.,
        1370000.,  1380000.,  1390000.,  1400000.,  1410000.,  1420000.,
        1430000.,  1440000.,  1450000.,  1460000.,  1470000.,  1480000.,
        1490000.,  1500000.,  1510000.,  1520000.,  1530000.,  1540000.,
        1550000.,  1560000.,  1570000.,  1580000.,  1590000.,  1600000.,
        1610000.,  1620000.,  1630000.,  1640000.,  1650000.,  1660000.,
        1670000.,  1680000.,  1690000.,  1700000.,  1710000.,  1720000.,
        1730000.,  1740000.,  1750000.,  1760000.,  1770000.,  1780000.,
        1790000.,  1800000.,  1810000.,  1820000.,  1830000.,  1840000.,
        1850000.,  1860000.,  1870000.,  1880000.,  1890000.,  1900000.,
        1910000.,  1920000.,  1930000.,  1940000.,  1950000.,  1960000.,
        1970000.,  1980000.,  1990000.,  2000000.,  2010000.,  2020000.,
        2030000.,  2040000.,  2050000.,  2060000.,  2070000.,  2080000.,
        2090000.,  2100000.,  2110000.,  2120000.,  2130000.,  2140000.,
        2150000.,  2160000.,  2170000.,  2180000.,  2190000.,  2200000.,
        2210000.,  2220000.,  2230000.,  2240000.,  2250000.,  2260000.,
        2270000.,  2280000.,  2290000.,  2300000.,  2310000.,  2320000.,
        2330000.,  2340000.,  2350000.,  2360000.,  2370000.,  2380000.,
        2390000.,  2400000.,  2410000.,  2420000.,  2430000.,  2440000.,
        2450000.,  2460000.,  2470000.,  2480000.,  2490000.,  2500000.,
        2510000.,  2520000.,  2530000.,  2540000.,  2550000.,  2560000.,
        2570000.,  2580000.,  2590000.,  2600000.,  2610000.,  2620000.,
        2630000.,  2640000.,  2650000.,  2660000.,  2670000.,  2680000.,
        2690000.,  2700000.,  2710000.,  2720000.,  2730000.,  2740000.,
        2750000.,  2760000.,  2770000.,  2780000.,  2790000.,  2800000.,
        2810000.,  2820000.,  2830000.,  2840000.,  2850000.,  2860000.,
        2870000.,  2880000.,  2890000.,  2900000.,  2910000.,  2920000.,
        2930000.,  2940000.,  2950000.,  2960000.,  2970000.,  2980000.,
        2990000.,  3000000.,  3010000.,  3020000.,  3030000.,  3040000.,
        3050000.,  3060000.,  3070000.,  3080000.,  3090000.,  3100000.,
        3110000.,  3120000.,  3130000.,  3140000.,  3150000.,  3160000.,
        3170000.,  3180000.,  3190000.,  3200000.,  3210000.,  3220000.,
        3230000.,  3240000.,  3250000.,  3260000.,  3270000.,  3280000.,
        3290000.,  3300000.,  3310000.,  3320000.,  3330000.,  3340000.,
        3350000.,  3360000.,  3370000.,  3380000.,  3390000.,  3400000.,
        3410000.,  3420000.,  3430000.,  3440000.,  3450000.,  3460000.,
        3470000.,  3480000.,  3490000.,  3500000.,  3510000.,  3520000.,
        3530000.,  3540000.,  3550000.,  3560000.,  3570000.,  3580000.,
        3590000.,  3600000.,  3610000.,  3620000.,  3630000.,  3640000.,
        3650000.,  3660000.,  3670000.,  3680000.,  3690000.,  3700000.,
        3710000.,  3720000.,  3730000.,  3740000.,  3750000.,  3760000.,
        3770000.,  3780000.,  3790000.,  3800000.,  3810000.,  3820000.,
        3830000.,  3840000.,  3850000.,  3860000.,  3870000.,  3880000.,
        3890000.,  3900000.,  3910000.,  3920000.,  3930000.,  3940000.,
        3950000.,  3960000.,  3970000.,  3980000.,  3990000.,  4000000.,
        4010000.,  4020000.,  4030000.,  4040000.,  4050000.,  4060000.,
        4070000.,  4080000.,  4090000.,  4100000.,  4110000.,  4120000.,
        4130000.,  4140000.,  4150000.,  4160000.,  4170000.,  4180000.,
        4190000.,  4200000.,  4210000.,  4220000.,  4230000.,  4240000.,
        4250000.,  4260000.,  4270000.,  4280000.,  4290000.,  4300000.,
        4310000.,  4320000.,  4330000.,  4340000.,  4350000.,  4360000.,
        4370000.,  4380000.,  4390000.,  4400000.,  4410000.,  4420000.,
        4430000.,  4440000.,  4450000.,  4460000.,  4470000.,  4480000.,
        4490000.,  4500000.,  4510000.,  4520000.,  4530000.,  4540000.,
        4550000.,  4560000.,  4570000.,  4580000.,  4590000.,  4600000.,
        4610000.,  4620000.,  4630000.,  4640000.,  4650000.,  4660000.,
        4670000.,  4680000.,  4690000.,  4700000.,  4710000.,  4720000.,
        4730000.,  4740000.,  4750000.,  4760000.,  4770000.,  4780000.,
        4790000.,  4800000.,  4810000.,  4820000.,  4830000.,  4840000.,
        4850000.,  4860000.,  4870000.,  4880000.,  4890000.,  4900000.,
        4910000.,  4920000.,  4930000.,  4940000.,  4950000.,  4960000.,
        4970000.,  4980000.,  4990000.,  5000000.,  5010000.,  5020000.,
        5030000.,  5040000.,  5050000.,  5060000.,  5070000.,  5080000.,
        5090000.,  5100000.,  5110000.,  5120000.,  5130000.,  5140000.,
        5150000.,  5160000.,  5170000.,  5180000.,  5190000.,  5200000.,
        5210000.,  5220000.,  5230000.,  5240000.,  5250000.,  5260000.,
        5270000.,  5280000.,  5290000.,  5300000.,  5310000.,  5320000.,
        5330000.,  5340000.,  5350000.,  5360000.,  5370000.,  5380000.,
        5390000.,  5400000.,  5410000.,  5420000.,  5430000.,  5440000.,
        5450000.,  5460000.,  5470000.,  5480000.,  5490000.,  5500000.,
        5510000.,  5520000.,  5530000.,  5540000.,  5550000.,  5560000.,
        5570000.,  5580000.,  5590000.,  5600000.,  5610000.,  5620000.,
        5630000.,  5640000.,  5650000.,  5660000.,  5670000.,  5680000.,
        5690000.,  5700000.,  5710000.,  5720000.,  5730000.,  5740000.,
        5750000.,  5760000.,  5770000.,  5780000.,  5790000.,  5800000.,
        5810000.,  5820000.,  5830000.,  5840000.,  5850000.,  5860000.,
        5870000.,  5880000.,  5890000.,  5900000.,  5910000.,  5920000.,
        5930000.,  5940000.,  5950000.,  5960000.,  5970000.,  5980000.,
        5990000.,  6000000.,  6010000.,  6020000.,  6030000.,  6040000.,
        6050000.,  6060000.,  6070000.,  6080000.,  6090000.,  6100000.,
        6110000.,  6120000.,  6130000.,  6140000.,  6150000.,  6160000.,
        6170000.,  6180000.,  6190000.,  6200000.,  6210000.,  6220000.,
        6230000.,  6240000.,  6250000.,  6260000.,  6270000.,  6280000.,
        6290000.,  6300000.,  6310000.,  6320000.,  6330000.,  6340000.,
        6350000.,  6360000.,  6370000.,  6380000.,  6390000.,  6400000.,
        6410000.,  6420000.,  6430000.,  6440000.,  6450000.,  6460000.,
        6470000.,  6480000.,  6490000.,  6500000.,  6510000.,  6520000.,
        6530000.,  6540000.,  6550000.,  6560000.,  6570000.,  6580000.,
        6590000.,  6600000.,  6610000.,  6620000.,  6630000.,  6640000.,
        6650000.,  6660000.,  6670000.,  6680000.,  6690000.,  6700000.,
        6710000.,  6720000.,  6730000.,  6740000.,  6750000.,  6760000.,
        6770000.,  6780000.,  6790000.,  6800000.,  6810000.,  6820000.,
        6830000.,  6840000.,  6850000.,  6860000.,  6870000.,  6880000.,
        6890000.,  6900000.,  6910000.,  6920000.,  6930000.,  6940000.,
        6950000.,  6960000.,  6970000.,  6980000.,  6990000.,  7000000.,
        7010000.,  7020000.,  7030000.,  7040000.,  7050000.,  7060000.,
        7070000.,  7080000.,  7090000.,  7100000.,  7110000.,  7120000.,
        7130000.,  7140000.,  7150000.,  7160000.,  7170000.,  7180000.,
        7190000.,  7200000.,  7210000.,  7220000.,  7230000.,  7240000.,
        7250000.,  7260000.,  7270000.,  7280000.,  7290000.,  7300000.,
        7310000.,  7320000.,  7330000.,  7340000.,  7350000.,  7360000.,
        7370000.,  7380000.,  7390000.,  7400000.,  7410000.,  7420000.,
        7430000.,  7440000.,  7450000.,  7460000.,  7470000.,  7480000.,
        7490000.,  7500000.,  7510000.,  7520000.,  7530000.,  7540000.,
        7550000.,  7560000.,  7570000.,  7580000.,  7590000.,  7600000.,
        7610000.,  7620000.,  7630000.,  7640000.,  7650000.,  7660000.,
        7670000.,  7680000.,  7690000.,  7700000.,  7710000.,  7720000.,
        7730000.,  7740000.,  7750000.,  7760000.,  7770000.,  7780000.,
        7790000.,  7800000.,  7810000.,  7820000.,  7830000.,  7840000.,
        7850000.,  7860000.,  7870000.,  7880000.,  7890000.,  7900000.,
        7910000.,  7920000.,  7930000.,  7940000.,  7950000.,  7960000.,
        7970000.,  7980000.,  7990000.,  8000000.,  8010000.,  8020000.,
        8030000.,  8040000.,  8050000.,  8060000.,  8070000.,  8080000.,
        8090000.,  8100000.,  8110000.,  8120000.,  8130000.,  8140000.,
        8150000.,  8160000.,  8170000.,  8180000.,  8190000.,  8200000.,
        8210000.,  8220000.,  8230000.,  8240000.,  8250000.,  8260000.,
        8270000.,  8280000.,  8290000.,  8300000.,  8310000.,  8320000.,
        8330000.,  8340000.,  8350000.,  8360000.,  8370000.,  8380000.,
        8390000.,  8400000.,  8410000.,  8420000.,  8430000.,  8440000.,
        8450000.,  8460000.,  8470000.,  8480000.,  8490000.,  8500000.,
        8510000.,  8520000.,  8530000.,  8540000.,  8550000.,  8560000.,
        8570000.,  8580000.,  8590000.,  8600000.,  8610000.,  8620000.,
        8630000.,  8640000.,  8650000.,  8660000.,  8670000.,  8680000.,
        8690000.,  8700000.,  8710000.,  8720000.,  8730000.,  8740000.,
        8750000.,  8760000.,  8770000.,  8780000.,  8790000.,  8800000.,
        8810000.,  8820000.,  8830000.,  8840000.,  8850000.,  8860000.,
        8870000.,  8880000.,  8890000.,  8900000.,  8910000.,  8920000.,
        8930000.,  8940000.,  8950000.,  8960000.,  8970000.,  8980000.,
        8990000.,  9000000.,  9010000.,  9020000.,  9030000.,  9040000.,
        9050000.,  9060000.,  9070000.,  9080000.,  9090000.,  9100000.,
        9110000.,  9120000.,  9130000.,  9140000.,  9150000.,  9160000.,
        9170000.,  9180000.,  9190000.,  9200000.,  9210000.,  9220000.,
        9230000.,  9240000.,  9250000.,  9260000.,  9270000.,  9280000.,
        9290000.,  9300000.,  9310000.,  9320000.,  9330000.,  9340000.,
        9350000.,  9360000.,  9370000.,  9380000.,  9390000.,  9400000.,
        9410000.,  9420000.,  9430000.,  9440000.,  9450000.,  9460000.,
        9470000.,  9480000.,  9490000.,  9500000.,  9510000.,  9520000.,
        9530000.,  9540000.,  9550000.,  9560000.,  9570000.,  9580000.,
        9590000.,  9600000.,  9610000.,  9620000.,  9630000.,  9640000.,
        9650000.,  9660000.,  9670000.,  9680000.,  9690000.,  9700000.,
        9710000.,  9720000.,  9730000.,  9740000.,  9750000.,  9760000.,
        9770000.,  9780000.,  9790000.,  9800000.,  9810000.,  9820000.,
        9830000.,  9840000.,  9850000.,  9860000.,  9870000.,  9880000.,
        9890000.,  9900000.,  9910000.,  9920000.,  9930000.,  9940000.,
        9950000.,  9960000.,  9970000.,  9980000.,  9990000., 10000000.])
Found dump file. Restoring simulation from snapshot...
  Timestep: 6.772840e+01 (0.1 x giant planet orbital period = 6.772840e+02)
Restored simulation from snapshot number at t=2.300000e+05 yr with N=802 particles.

Stirrer-coverage check (Krivov & Booth 2018: N x delta_af >= delta_a):
  Stirrers inside the belt [95, 105]: N = 795
  delta_af = 8 sqrt(3) h_M a_M:  mean = 1.379922e+00, sum over stirrers = 1.097038e+03
  Belt width delta_a = 1.000000e+01
  Coverage ratio (sum delta_af / delta_a) = 109.704
  OK: stirrer feeding zones span the belt.

Beginning the main integration
Output 1/977: t=230000.0 yr, dE/E0=0.00e+00, N=802
  Estimated time remaining to complete simulation: 1 minutes, 4 seconds
  Estimated time remaining to next output: 0 seconds
Output 2/977: t=240000.0 yr, dE/E0=8.72e-09, N=802
  Estimated time remaining to complete simulation: 1 months, 1 days, 7 hours, 30 minutes, 1 seconds
  Estimated time remaining to next output: 46 minutes, 14 seconds
Output 3/977: t=250000.0 yr, dE/E0=2.56e-10, N=802
  Estimated time remaining to complete simulation: 1 months, 1 weeks, 6 days, 22 hours, 44 minutes, 33 seconds
  Estimated time remaining to next output: 1 hours, 4 minutes, 58 seconds
Output 4/977: t=260000.0 yr, dE/E0=6.19e-09, N=802
  Estimated time remaining to complete simulation: 1 months, 2 weeks, 6 days, 1 hours, 7 minutes, 18 seconds
  Estimated time remaining to next output: 1 hours, 14 minutes, 4 seconds
Output 5/977: t=270000.0 yr, dE/E0=3.28e-08, N=802
  Estimated time remaining to complete simulation: 1 months, 3 weeks, 2 days, 14 hours, 7 minutes, 30 seconds
  Estimated time remaining to next output: 1 hours, 19 minutes, 23 seconds
Output 6/977: t=280000.0 yr, dE/E0=4.81e-08, N=802
  Estimated time remaining to complete simulation: 1 months, 3 weeks, 3 days, 1 hours, 44 minutes, 23 seconds
  Estimated time remaining to next output: 1 hours, 20 minutes, 11 seconds
Output 7/977: t=290000.0 yr, dE/E0=1.01e-08, N=802
  Estimated time remaining to complete simulation: 1 months, 3 weeks, 3 days, 12 hours, 22 minutes, 55 seconds
  Estimated time remaining to next output: 1 hours, 20 minutes, 55 seconds
Output 8/977: t=300000.0 yr, dE/E0=2.77e-08, N=802
  Estimated time remaining to complete simulation: 1 months, 3 weeks, 3 days, 20 hours, 49 minutes, 46 seconds
  Estimated time remaining to next output: 1 hours, 21 minutes, 32 seconds
Output 9/977: t=310000.0 yr, dE/E0=8.99e-09, N=802
  Estimated time remaining to complete simulation: 1 months, 3 weeks, 4 days, 1 hours, 40 minutes, 42 seconds
  Estimated time remaining to next output: 1 hours, 21 minutes, 55 seconds
Output 10/977: t=320000.0 yr, dE/E0=2.14e-08, N=802
  Estimated time remaining to complete simulation: 1 months, 3 weeks, 2 days, 3 hours, 3 minutes, 30 seconds
  Estimated time remaining to next output: 1 hours, 19 minutes, 6 seconds
Output 11/977: t=330000.0 yr, dE/E0=1.78e-08, N=802
  Estimated time remaining to complete simulation: 1 months, 3 weeks, 13 hours, 32 minutes, 14 seconds
  Estimated time remaining to next output: 1 hours, 16 minutes, 51 seconds
Output 12/977: t=340000.0 yr, dE/E0=2.34e-08, N=802
  Estimated time remaining to complete simulation: 1 months, 2 weeks, 6 days, 3 hours, 50 minutes, 24 seconds
  Estimated time remaining to next output: 1 hours, 14 minutes, 51 seconds
Output 13/977: t=350000.0 yr, dE/E0=3.76e-08, N=802
  Estimated time remaining to complete simulation: 1 months, 2 weeks, 4 days, 20 hours, 38 minutes, 48 seconds
  Estimated time remaining to next output: 1 hours, 12 minutes, 59 seconds
Output 14/977: t=360000.0 yr, dE/E0=3.02e-08, N=802
  Estimated time remaining to complete simulation: 1 months, 2 weeks, 3 days, 18 hours, 11 minutes, 7 seconds
  Estimated time remaining to next output: 1 hours, 11 minutes, 24 seconds
Output 15/977: t=370000.0 yr, dE/E0=2.83e-08, N=802
  Estimated time remaining to complete simulation: 1 months, 2 weeks, 2 days, 21 hours, 9 minutes, 27 seconds
  Estimated time remaining to next output: 1 hours, 10 minutes, 10 seconds
Output 16/977: t=380000.0 yr, dE/E0=3.96e-08, N=802
  Estimated time remaining to complete simulation: 1 months, 2 weeks, 2 days, 2 hours, 6 minutes, 16 seconds
  Estimated time remaining to next output: 1 hours, 9 minutes, 3 seconds
Output 17/977: t=390000.0 yr, dE/E0=3.28e-08, N=802
  Estimated time remaining to complete simulation: 1 months, 2 weeks, 1 days, 7 hours, 37 minutes, 38 seconds
  Estimated time remaining to next output: 1 hours, 7 minutes, 58 seconds
Output 18/977: t=400000.0 yr, dE/E0=3.65e-08, N=802
  Estimated time remaining to complete simulation: 1 months, 2 weeks, 22 hours, 37 minutes, 3 seconds
  Estimated time remaining to next output: 1 hours, 7 minutes, 29 seconds
Output 19/977: t=410000.0 yr, dE/E0=5.36e-08, N=802
  Estimated time remaining to complete simulation: 1 months, 2 weeks, 18 hours, 3 minutes, 10 seconds
  Estimated time remaining to next output: 1 hours, 7 minutes, 16 seconds
Output 20/977: t=420000.0 yr, dE/E0=6.36e-08, N=802
  Estimated time remaining to complete simulation: 1 months, 2 weeks, 12 hours, 54 minutes, 8 seconds
  Estimated time remaining to next output: 1 hours, 7 minutes
Output 21/977: t=430000.0 yr, dE/E0=6.62e-08, N=802
  Estimated time remaining to complete simulation: 1 months, 2 weeks, 8 hours, 30 minutes, 53 seconds
  Estimated time remaining to next output: 1 hours, 6 minutes, 48 seconds
Output 22/977: t=440000.0 yr, dE/E0=6.56e-08, N=802
  Estimated time remaining to complete simulation: 1 months, 2 weeks, 16 hours, 15 minutes, 21 seconds
  Estimated time remaining to next output: 1 hours, 7 minutes, 22 seconds
Output 23/977: t=450000.0 yr, dE/E0=5.96e-08, N=802
  Estimated time remaining to complete simulation: 1 months, 2 weeks, 1 days, 25 minutes, 22 seconds
  Estimated time remaining to next output: 1 hours, 7 minutes, 57 seconds
Output 24/977: t=460000.0 yr, dE/E0=8.51e-08, N=802
  Estimated time remaining to complete simulation: 1 months, 2 weeks, 1 days, 3 hours, 56 minutes, 7 seconds
  Estimated time remaining to next output: 1 hours, 8 minutes, 14 seconds
Output 25/977: t=470000.0 yr, dE/E0=7.21e-08, N=802
  Estimated time remaining to complete simulation: 1 months, 2 weeks, 1 days, 20 hours, 18 minutes, 9 seconds
  Estimated time remaining to next output: 1 hours, 9 minutes, 20 seconds
Output 26/977: t=480000.0 yr, dE/E0=8.38e-08, N=802
  Estimated time remaining to complete simulation: 1 months, 2 weeks, 3 days, 10 hours, 51 minutes, 35 seconds
  Estimated time remaining to next output: 1 hours, 11 minutes, 51 seconds
Output 27/977: t=490000.0 yr, dE/E0=8.14e-08, N=802
  Estimated time remaining to complete simulation: 1 months, 2 weeks, 4 days, 18 hours, 20 minutes
  Estimated time remaining to next output: 1 hours, 13 minutes, 54 seconds
Output 28/977: t=500000.0 yr, dE/E0=6.96e-08, N=802
  Estimated time remaining to complete simulation: 1 months, 2 weeks, 5 days, 21 hours, 48 minutes, 34 seconds
  Estimated time remaining to next output: 1 hours, 15 minutes, 43 seconds
Output 29/977: t=510000.0 yr, dE/E0=5.66e-08, N=802
  Estimated time remaining to complete simulation: 1 months, 2 weeks, 6 days, 1 hours, 41 minutes, 46 seconds
  Estimated time remaining to next output: 1 hours, 16 minutes, 3 seconds
Output 30/977: t=520000.0 yr, dE/E0=5.79e-08, N=802
  Estimated time remaining to complete simulation: 1 months, 2 weeks, 6 days, 4 hours, 27 minutes
  Estimated time remaining to next output: 1 hours, 16 minutes, 18 seconds
Output 31/977: t=530000.0 yr, dE/E0=6.39e-08, N=802
  Estimated time remaining to complete simulation: 1 months, 2 weeks, 6 days, 7 hours, 48 minutes, 6 seconds
  Estimated time remaining to next output: 1 hours, 16 minutes, 36 seconds
Output 32/977: t=540000.0 yr, dE/E0=7.02e-08, N=802
  Estimated time remaining to complete simulation: 1 months, 2 weeks, 6 days, 10 hours, 17 minutes
  Estimated time remaining to next output: 1 hours, 16 minutes, 50 seconds
Output 33/977: t=550000.0 yr, dE/E0=6.09e-08, N=802
  Estimated time remaining to complete simulation: 1 months, 2 weeks, 6 days, 12 hours, 48 minutes, 36 seconds
  Estimated time remaining to next output: 1 hours, 17 minutes, 5 seconds
Output 34/977: t=560000.0 yr, dE/E0=7.18e-08, N=802
  Estimated time remaining to complete simulation: 1 months, 2 weeks, 6 days, 16 hours, 59 minutes, 57 seconds
  Estimated time remaining to next output: 1 hours, 17 minutes, 26 seconds
Output 35/977: t=570000.0 yr, dE/E0=5.46e-08, N=802
  Estimated time remaining to complete simulation: 1 months, 2 weeks, 6 days, 3 hours, 57 minutes, 46 seconds
  Estimated time remaining to next output: 1 hours, 16 minutes, 41 seconds
Output 36/977: t=580000.0 yr, dE/E0=4.60e-08, N=802
  Estimated time remaining to complete simulation: 1 months, 2 weeks, 5 days, 8 hours, 33 minutes, 9 seconds
  Estimated time remaining to next output: 1 hours, 15 minutes, 31 seconds
Output 37/977: t=590000.0 yr, dE/E0=6.05e-08, N=802
  Estimated time remaining to complete simulation: 1 months, 2 weeks, 4 days, 9 hours, 56 minutes, 50 seconds
  Estimated time remaining to next output: 1 hours, 14 minutes, 10 seconds
Output 38/977: t=600000.0 yr, dE/E0=6.05e-08, N=802
  Estimated time remaining to complete simulation: 1 months, 2 weeks, 3 days, 11 hours, 40 seconds
  Estimated time remaining to next output: 1 hours, 12 minutes, 46 seconds
Output 39/977: t=610000.0 yr, dE/E0=7.31e-08, N=802
  Estimated time remaining to complete simulation: 1 months, 2 weeks, 2 days, 10 hours, 42 minutes, 13 seconds
  Estimated time remaining to next output: 1 hours, 11 minutes, 18 seconds
Output 40/977: t=620000.0 yr, dE/E0=8.84e-08, N=802
  Estimated time remaining to complete simulation: 1 months, 2 weeks, 1 days, 11 hours, 38 minutes, 26 seconds
  Estimated time remaining to next output: 1 hours, 9 minutes, 54 seconds
Output 41/977: t=630000.0 yr, dE/E0=8.09e-08, N=802
  Estimated time remaining to complete simulation: 1 months, 2 weeks, 13 hours, 40 minutes, 9 seconds
  Estimated time remaining to next output: 1 hours, 8 minutes, 34 seconds
Output 42/977: t=640000.0 yr, dE/E0=1.09e-07, N=802
  Estimated time remaining to complete simulation: 1 months, 1 weeks, 6 days, 16 hours, 54 minutes, 50 seconds
  Estimated time remaining to next output: 1 hours, 7 minutes, 18 seconds
Output 43/977: t=650000.0 yr, dE/E0=1.18e-07, N=802
  Estimated time remaining to complete simulation: 1 months, 1 weeks, 5 days, 21 hours, 10 minutes, 31 seconds
  Estimated time remaining to next output: 1 hours, 6 minutes, 6 seconds
Output 44/977: t=660000.0 yr, dE/E0=1.25e-07, N=802
  Estimated time remaining to complete simulation: 1 months, 1 weeks, 5 days, 2 hours, 29 minutes, 38 seconds
  Estimated time remaining to next output: 1 hours, 4 minutes, 59 seconds
Output 45/977: t=670000.0 yr, dE/E0=1.14e-07, N=802
  Estimated time remaining to complete simulation: 1 months, 1 weeks, 4 days, 8 hours, 43 minutes, 45 seconds
  Estimated time remaining to next output: 1 hours, 3 minutes, 54 seconds
Output 46/977: t=680000.0 yr, dE/E0=1.06e-07, N=802
  Estimated time remaining to complete simulation: 1 months, 1 weeks, 3 days, 15 hours, 52 minutes, 5 seconds
  Estimated time remaining to next output: 1 hours, 2 minutes, 53 seconds
Output 47/977: t=690000.0 yr, dE/E0=9.16e-08, N=802
  Estimated time remaining to complete simulation: 1 months, 1 weeks, 3 days, 4 minutes, 4 seconds
  Estimated time remaining to next output: 1 hours, 1 minutes, 56 seconds
Output 48/977: t=700000.0 yr, dE/E0=1.06e-07, N=802
  Estimated time remaining to complete simulation: 1 months, 1 weeks, 2 days, 9 hours, 13 minutes, 24 seconds
  Estimated time remaining to next output: 1 hours, 1 minutes, 2 seconds
Output 49/977: t=710000.0 yr, dE/E0=9.26e-08, N=802
  Estimated time remaining to complete simulation: 1 months, 1 weeks, 1 days, 18 hours, 47 minutes, 20 seconds
  Estimated time remaining to next output: 1 hours, 10 seconds
Output 50/977: t=720000.0 yr, dE/E0=9.11e-08, N=802
  Estimated time remaining to complete simulation: 1 months, 1 weeks, 1 days, 4 hours, 56 minutes, 11 seconds
  Estimated time remaining to next output: 59 minutes, 20 seconds
Output 51/977: t=730000.0 yr, dE/E0=9.48e-08, N=802
  Estimated time remaining to complete simulation: 1 months, 1 weeks, 15 hours, 24 minutes, 58 seconds
  Estimated time remaining to next output: 58 minutes, 32 seconds
Output 52/977: t=740000.0 yr, dE/E0=7.40e-08, N=802
  Estimated time remaining to complete simulation: 1 months, 1 weeks, 2 hours, 19 minutes, 11 seconds
  Estimated time remaining to next output: 57 minutes, 45 seconds
Output 53/977: t=750000.0 yr, dE/E0=9.08e-08, N=802
  Estimated time remaining to complete simulation: 1 months, 6 days, 13 hours, 35 minutes, 59 seconds
  Estimated time remaining to next output: 56 minutes, 59 seconds
Output 54/977: t=760000.0 yr, dE/E0=8.52e-08, N=802
  Estimated time remaining to complete simulation: 1 months, 6 days, 3 hours, 25 minutes, 49 seconds
  Estimated time remaining to next output: 56 minutes, 23 seconds
Output 55/977: t=770000.0 yr, dE/E0=9.36e-08, N=802
  Estimated time remaining to complete simulation: 1 months, 5 days, 15 hours, 48 minutes, 40 seconds
  Estimated time remaining to next output: 55 minutes, 41 seconds
Output 56/977: t=780000.0 yr, dE/E0=7.96e-08, N=802
  Estimated time remaining to complete simulation: 1 months, 5 days, 4 hours, 34 minutes, 19 seconds
  Estimated time remaining to next output: 55 minutes, 1 seconds
Output 57/977: t=790000.0 yr, dE/E0=7.27e-08, N=802
  Estimated time remaining to complete simulation: 1 months, 4 days, 18 hours, 4 minutes, 42 seconds
  Estimated time remaining to next output: 54 minutes, 23 seconds
Output 58/977: t=800000.0 yr, dE/E0=6.24e-08, N=802
  Estimated time remaining to complete simulation: 1 months, 4 days, 7 hours, 48 minutes, 1 seconds
  Estimated time remaining to next output: 53 minutes, 47 seconds
Output 59/977: t=810000.0 yr, dE/E0=4.89e-08, N=802
  Estimated time remaining to complete simulation: 1 months, 3 days, 21 hours, 38 minutes, 17 seconds
  Estimated time remaining to next output: 53 minutes, 10 seconds
Output 60/977: t=820000.0 yr, dE/E0=5.30e-08, N=802
  Estimated time remaining to complete simulation: 1 months, 3 days, 12 hours, 3 minutes, 33 seconds
  Estimated time remaining to next output: 52 minutes, 36 seconds
Output 61/977: t=830000.0 yr, dE/E0=4.94e-08, N=802
  Estimated time remaining to complete simulation: 1 months, 3 days, 2 hours, 37 minutes, 54 seconds
  Estimated time remaining to next output: 52 minutes, 3 seconds
Output 62/977: t=840000.0 yr, dE/E0=4.08e-08, N=802
  Estimated time remaining to complete simulation: 1 months, 2 days, 18 hours, 16 minutes, 24 seconds
  Estimated time remaining to next output: 51 minutes, 33 seconds
Output 63/977: t=850000.0 yr, dE/E0=2.22e-08, N=802
  Estimated time remaining to complete simulation: 1 months, 2 days, 10 hours, 9 minutes, 38 seconds
  Estimated time remaining to next output: 51 minutes, 4 seconds
Output 64/977: t=860000.0 yr, dE/E0=3.70e-08, N=802
  Estimated time remaining to complete simulation: 1 months, 2 days, 2 hours, 43 minutes, 3 seconds
  Estimated time remaining to next output: 50 minutes, 38 seconds
Output 65/977: t=870000.0 yr, dE/E0=4.85e-08, N=802
  Estimated time remaining to complete simulation: 1 months, 1 days, 21 hours, 29 minutes, 3 seconds
  Estimated time remaining to next output: 50 minutes, 21 seconds
Output 66/977: t=880000.0 yr, dE/E0=4.25e-08, N=802
  Estimated time remaining to complete simulation: 1 months, 1 days, 17 hours, 39 minutes, 27 seconds
  Estimated time remaining to next output: 50 minutes, 9 seconds
Output 67/977: t=890000.0 yr, dE/E0=2.84e-08, N=802
  Estimated time remaining to complete simulation: 1 months, 1 days, 13 hours, 25 minutes, 26 seconds
  Estimated time remaining to next output: 49 minutes, 56 seconds
Output 68/977: t=900000.0 yr, dE/E0=4.95e-08, N=802
  Estimated time remaining to complete simulation: 1 months, 1 days, 9 hours, 18 minutes, 53 seconds
  Estimated time remaining to next output: 49 minutes, 43 seconds
Output 69/977: t=910000.0 yr, dE/E0=5.75e-08, N=802
  Estimated time remaining to complete simulation: 1 months, 1 days, 6 hours, 15 minutes, 13 seconds
  Estimated time remaining to next output: 49 minutes, 34 seconds
Output 70/977: t=920000.0 yr, dE/E0=8.08e-08, N=802
  Estimated time remaining to complete simulation: 1 months, 1 days, 3 hours, 15 minutes, 16 seconds
  Estimated time remaining to next output: 49 minutes, 25 seconds
Output 71/977: t=930000.0 yr, dE/E0=8.51e-08, N=802
  Estimated time remaining to complete simulation: 1 months, 23 hours, 19 minutes, 56 seconds
  Estimated time remaining to next output: 49 minutes, 13 seconds
Output 72/977: t=940000.0 yr, dE/E0=1.07e-07, N=802
  Estimated time remaining to complete simulation: 1 months, 19 hours, 38 minutes, 47 seconds
  Estimated time remaining to next output: 49 minutes, 2 seconds
Output 73/977: t=950000.0 yr, dE/E0=1.12e-07, N=802
  Estimated time remaining to complete simulation: 1 months, 15 hours, 32 minutes, 47 seconds
  Estimated time remaining to next output: 48 minutes, 49 seconds
Output 74/977: t=960000.0 yr, dE/E0=8.87e-08, N=802
  Estimated time remaining to complete simulation: 1 months, 10 hours, 57 minutes, 28 seconds
  Estimated time remaining to next output: 48 minutes, 34 seconds
Output 75/977: t=970000.0 yr, dE/E0=7.72e-08, N=802
  Estimated time remaining to complete simulation: 1 months, 6 hours, 14 minutes, 23 seconds
  Estimated time remaining to next output: 48 minutes, 18 seconds
Output 76/977: t=980000.0 yr, dE/E0=6.25e-08, N=802
  Estimated time remaining to complete simulation: 1 months, 1 hours, 17 minutes, 41 seconds
  Estimated time remaining to next output: 48 minutes, 1 seconds
Output 77/977: t=990000.0 yr, dE/E0=6.28e-08, N=802
  Estimated time remaining to complete simulation: 4 weeks, 1 days, 20 hours, 34 minutes, 30 seconds
  Estimated time remaining to next output: 47 minutes, 46 seconds
Output 78/977: t=1000000.0 yr, dE/E0=7.78e-08, N=802
  Estimated time remaining to complete simulation: 4 weeks, 1 days, 14 hours, 29 minutes, 19 seconds
  Estimated time remaining to next output: 47 minutes, 25 seconds
Output 79/977: t=1010000.0 yr, dE/E0=8.61e-08, N=802
  Estimated time remaining to complete simulation: 4 weeks, 1 days, 7 hours, 57 minutes, 10 seconds
  Estimated time remaining to next output: 47 minutes, 2 seconds
Output 80/977: t=1020000.0 yr, dE/E0=7.03e-08, N=802
  Estimated time remaining to complete simulation: 4 weeks, 1 days, 1 hours, 34 minutes, 26 seconds
  Estimated time remaining to next output: 46 minutes, 39 seconds
Output 81/977: t=1030000.0 yr, dE/E0=7.37e-08, N=802
  Estimated time remaining to complete simulation: 4 weeks, 19 hours, 21 minutes, 38 seconds
  Estimated time remaining to next output: 46 minutes, 17 seconds
Output 82/977: t=1040000.0 yr, dE/E0=7.88e-08, N=802
  Estimated time remaining to complete simulation: 4 weeks, 13 hours, 9 minutes, 3 seconds
  Estimated time remaining to next output: 45 minutes, 55 seconds
Output 83/977: t=1050000.0 yr, dE/E0=9.54e-08, N=802
  Estimated time remaining to complete simulation: 4 weeks, 6 hours, 10 minutes
  Estimated time remaining to next output: 45 minutes, 30 seconds
Output 84/977: t=1060000.0 yr, dE/E0=8.41e-08, N=802
  Estimated time remaining to complete simulation: 3 weeks, 6 days, 23 hours, 18 minutes, 35 seconds
  Estimated time remaining to next output: 45 minutes, 6 seconds
Output 85/977: t=1070000.0 yr, dE/E0=8.29e-08, N=802
  Estimated time remaining to complete simulation: 3 weeks, 6 days, 16 hours, 51 minutes, 43 seconds
  Estimated time remaining to next output: 44 minutes, 43 seconds
Output 86/977: t=1080000.0 yr, dE/E0=8.38e-08, N=802
  Estimated time remaining to complete simulation: 3 weeks, 6 days, 10 hours, 38 minutes, 38 seconds
  Estimated time remaining to next output: 44 minutes, 21 seconds
Output 87/977: t=1090000.0 yr, dE/E0=8.54e-08, N=802
  Estimated time remaining to complete simulation: 3 weeks, 6 days, 4 hours, 32 minutes, 37 seconds
  Estimated time remaining to next output: 43 minutes, 59 seconds
Output 88/977: t=1100000.0 yr, dE/E0=6.89e-08, N=802
  Estimated time remaining to complete simulation: 3 weeks, 5 days, 22 hours, 49 minutes, 16 seconds
  Estimated time remaining to next output: 43 minutes, 39 seconds
Output 89/977: t=1110000.0 yr, dE/E0=8.44e-08, N=802
  Estimated time remaining to complete simulation: 3 weeks, 5 days, 17 hours, 1 minutes, 10 seconds
  Estimated time remaining to next output: 43 minutes, 18 seconds
Output 90/977: t=1120000.0 yr, dE/E0=7.55e-08, N=802
  Estimated time remaining to complete simulation: 3 weeks, 5 days, 11 hours, 24 minutes
  Estimated time remaining to next output: 42 minutes, 58 seconds
Output 91/977: t=1130000.0 yr, dE/E0=8.31e-08, N=802
  Estimated time remaining to complete simulation: 3 weeks, 5 days, 5 hours, 48 minutes, 21 seconds
  Estimated time remaining to next output: 42 minutes, 39 seconds
Output 92/977: t=1140000.0 yr, dE/E0=7.96e-08, N=802
  Estimated time remaining to complete simulation: 3 weeks, 5 days, 17 minutes, 36 seconds
  Estimated time remaining to next output: 42 minutes, 19 seconds
Output 93/977: t=1150000.0 yr, dE/E0=8.23e-08, N=802
  Estimated time remaining to complete simulation: 3 weeks, 4 days, 18 hours, 45 minutes, 18 seconds
  Estimated time remaining to next output: 41 minutes, 59 seconds
Output 94/977: t=1160000.0 yr, dE/E0=8.38e-08, N=802
  Estimated time remaining to complete simulation: 3 weeks, 4 days, 13 hours, 27 minutes, 50 seconds
  Estimated time remaining to next output: 41 minutes, 41 seconds
Output 95/977: t=1170000.0 yr, dE/E0=9.09e-08, N=802
  Estimated time remaining to complete simulation: 3 weeks, 4 days, 8 hours, 16 minutes, 36 seconds
  Estimated time remaining to next output: 41 minutes, 22 seconds
Output 96/977: t=1180000.0 yr, dE/E0=9.98e-08, N=802
  Estimated time remaining to complete simulation: 3 weeks, 4 days, 3 hours, 40 minutes, 31 seconds
  Estimated time remaining to next output: 41 minutes, 6 seconds
Output 97/977: t=1190000.0 yr, dE/E0=8.92e-08, N=802
  Estimated time remaining to complete simulation: 3 weeks, 3 days, 23 hours, 13 minutes, 28 seconds
  Estimated time remaining to next output: 40 minutes, 51 seconds
Output 98/977: t=1200000.0 yr, dE/E0=7.91e-08, N=802
  Estimated time remaining to complete simulation: 3 weeks, 3 days, 18 hours, 59 minutes, 56 seconds
  Estimated time remaining to next output: 40 minutes, 36 seconds
Output 99/977: t=1210000.0 yr, dE/E0=9.03e-08, N=802
  Estimated time remaining to complete simulation: 3 weeks, 3 days, 14 hours, 59 minutes, 43 seconds
  Estimated time remaining to next output: 40 minutes, 23 seconds
Output 100/977: t=1220000.0 yr, dE/E0=9.06e-08, N=802
  Estimated time remaining to complete simulation: 3 weeks, 3 days, 11 hours, 8 minutes, 16 seconds
  Estimated time remaining to next output: 40 minutes, 10 seconds
Output 101/977: t=1230000.0 yr, dE/E0=7.09e-08, N=802
  Estimated time remaining to complete simulation: 3 weeks, 3 days, 7 hours, 18 minutes, 44 seconds
  Estimated time remaining to next output: 39 minutes, 57 seconds
Output 102/977: t=1240000.0 yr, dE/E0=8.42e-08, N=802
  Estimated time remaining to complete simulation: 3 weeks, 3 days, 3 hours, 9 minutes, 34 seconds
  Estimated time remaining to next output: 39 minutes, 42 seconds
Output 103/977: t=1250000.0 yr, dE/E0=7.10e-08, N=802
  Estimated time remaining to complete simulation: 3 weeks, 2 days, 22 hours, 52 minutes, 26 seconds
  Estimated time remaining to next output: 39 minutes, 27 seconds
Output 104/977: t=1260000.0 yr, dE/E0=8.09e-08, N=802
  Estimated time remaining to complete simulation: 3 weeks, 2 days, 18 hours, 31 minutes, 26 seconds
  Estimated time remaining to next output: 39 minutes, 12 seconds
Output 105/977: t=1270000.0 yr, dE/E0=8.93e-08, N=802
  Estimated time remaining to complete simulation: 3 weeks, 2 days, 14 hours, 18 minutes, 5 seconds
  Estimated time remaining to next output: 38 minutes, 57 seconds
Output 106/977: t=1280000.0 yr, dE/E0=1.15e-07, N=802
  Estimated time remaining to complete simulation: 3 weeks, 2 days, 10 hours, 19 minutes, 28 seconds
  Estimated time remaining to next output: 38 minutes, 44 seconds
Output 107/977: t=1290000.0 yr, dE/E0=1.09e-07, N=802
  Estimated time remaining to complete simulation: 3 weeks, 2 days, 6 hours, 11 minutes, 46 seconds
  Estimated time remaining to next output: 38 minutes, 29 seconds
Output 108/977: t=1300000.0 yr, dE/E0=1.05e-07, N=802
  Estimated time remaining to complete simulation: 3 weeks, 2 days, 1 hours, 32 minutes, 42 seconds
  Estimated time remaining to next output: 38 minutes, 13 seconds
Output 109/977: t=1310000.0 yr, dE/E0=1.07e-07, N=802
  Estimated time remaining to complete simulation: 3 weeks, 1 days, 20 hours, 59 minutes, 12 seconds
  Estimated time remaining to next output: 37 minutes, 56 seconds
Output 110/977: t=1320000.0 yr, dE/E0=7.86e-08, N=802
  Estimated time remaining to complete simulation: 3 weeks, 1 days, 16 hours, 26 minutes, 28 seconds
  Estimated time remaining to next output: 37 minutes, 40 seconds
Output 111/977: t=1330000.0 yr, dE/E0=8.78e-08, N=802
  Estimated time remaining to complete simulation: 3 weeks, 1 days, 11 hours, 53 minutes, 14 seconds
  Estimated time remaining to next output: 37 minutes, 24 seconds
Output 112/977: t=1340000.0 yr, dE/E0=7.73e-08, N=802
  Estimated time remaining to complete simulation: 3 weeks, 1 days, 7 hours, 22 minutes, 15 seconds
  Estimated time remaining to next output: 37 minutes, 8 seconds
Output 113/977: t=1350000.0 yr, dE/E0=6.92e-08, N=802
  Estimated time remaining to complete simulation: 3 weeks, 1 days, 3 hours
  Estimated time remaining to next output: 36 minutes, 52 seconds
Output 114/977: t=1360000.0 yr, dE/E0=8.20e-08, N=802
  Estimated time remaining to complete simulation: 3 weeks, 22 hours, 40 minutes, 37 seconds
  Estimated time remaining to next output: 36 minutes, 37 seconds
Output 115/977: t=1370000.0 yr, dE/E0=7.43e-08, N=802
  Estimated time remaining to complete simulation: 3 weeks, 18 hours, 25 minutes, 46 seconds
  Estimated time remaining to next output: 36 minutes, 21 seconds
Output 116/977: t=1380000.0 yr, dE/E0=6.20e-08, N=802
  Estimated time remaining to complete simulation: 3 weeks, 14 hours, 14 minutes, 29 seconds
  Estimated time remaining to next output: 36 minutes, 6 seconds
Output 117/977: t=1390000.0 yr, dE/E0=9.12e-08, N=802
  Estimated time remaining to complete simulation: 3 weeks, 10 hours, 8 minutes, 1 seconds
  Estimated time remaining to next output: 35 minutes, 52 seconds
Output 118/977: t=1400000.0 yr, dE/E0=7.72e-08, N=802
  Estimated time remaining to complete simulation: 3 weeks, 6 hours, 4 minutes
  Estimated time remaining to next output: 35 minutes, 37 seconds
Output 119/977: t=1410000.0 yr, dE/E0=8.43e-08, N=802
  Estimated time remaining to complete simulation: 3 weeks, 2 hours, 6 minutes, 18 seconds
  Estimated time remaining to next output: 35 minutes, 23 seconds
Output 120/977: t=1420000.0 yr, dE/E0=8.57e-08, N=802
  Estimated time remaining to complete simulation: 2 weeks, 6 days, 22 hours, 12 minutes, 12 seconds
  Estimated time remaining to next output: 35 minutes, 9 seconds
Output 121/977: t=1430000.0 yr, dE/E0=9.92e-08, N=802
  Estimated time remaining to complete simulation: 2 weeks, 6 days, 18 hours, 21 minutes, 31 seconds
  Estimated time remaining to next output: 34 minutes, 55 seconds
Output 122/977: t=1440000.0 yr, dE/E0=9.13e-08, N=802
  Estimated time remaining to complete simulation: 2 weeks, 6 days, 14 hours, 33 minutes, 37 seconds
  Estimated time remaining to next output: 34 minutes, 42 seconds
Output 123/977: t=1450000.0 yr, dE/E0=8.94e-08, N=802
  Estimated time remaining to complete simulation: 2 weeks, 6 days, 10 hours, 49 minutes, 10 seconds
  Estimated time remaining to next output: 34 minutes, 29 seconds
Output 124/977: t=1460000.0 yr, dE/E0=8.84e-08, N=802
  Estimated time remaining to complete simulation: 2 weeks, 6 days, 7 hours, 7 minutes, 5 seconds
  Estimated time remaining to next output: 34 minutes, 15 seconds
Output 125/977: t=1470000.0 yr, dE/E0=9.58e-08, N=802
  Estimated time remaining to complete simulation: 2 weeks, 6 days, 3 hours, 27 minutes, 42 seconds
  Estimated time remaining to next output: 34 minutes, 2 seconds
Output 126/977: t=1480000.0 yr, dE/E0=9.92e-08, N=802
  Estimated time remaining to complete simulation: 2 weeks, 5 days, 23 hours, 54 minutes, 45 seconds
  Estimated time remaining to next output: 33 minutes, 50 seconds
Output 127/977: t=1490000.0 yr, dE/E0=1.07e-07, N=802
  Estimated time remaining to complete simulation: 2 weeks, 5 days, 20 hours, 21 minutes, 57 seconds
  Estimated time remaining to next output: 33 minutes, 37 seconds
Output 128/977: t=1500000.0 yr, dE/E0=1.30e-07, N=802
  Estimated time remaining to complete simulation: 2 weeks, 5 days, 16 hours, 53 minutes, 29 seconds
  Estimated time remaining to next output: 33 minutes, 25 seconds
Output 129/977: t=1510000.0 yr, dE/E0=1.37e-07, N=802
  Estimated time remaining to complete simulation: 2 weeks, 5 days, 13 hours, 27 minutes, 43 seconds
  Estimated time remaining to next output: 33 minutes, 12 seconds
Output 130/977: t=1520000.0 yr, dE/E0=1.47e-07, N=802
  Estimated time remaining to complete simulation: 2 weeks, 5 days, 10 hours, 7 minutes, 51 seconds
  Estimated time remaining to next output: 33 minutes, 1 seconds
Output 131/977: t=1530000.0 yr, dE/E0=1.45e-07, N=802
  Estimated time remaining to complete simulation: 2 weeks, 5 days, 6 hours, 47 minutes, 57 seconds
  Estimated time remaining to next output: 32 minutes, 49 seconds
Output 132/977: t=1540000.0 yr, dE/E0=1.21e-07, N=802
  Estimated time remaining to complete simulation: 2 weeks, 5 days, 3 hours, 29 minutes, 13 seconds
  Estimated time remaining to next output: 32 minutes, 37 seconds
Output 133/977: t=1550000.0 yr, dE/E0=1.37e-07, N=802
  Estimated time remaining to complete simulation: 2 weeks, 5 days, 18 minutes, 10 seconds
  Estimated time remaining to next output: 32 minutes, 26 seconds
Output 134/977: t=1560000.0 yr, dE/E0=1.30e-07, N=802
  Estimated time remaining to complete simulation: 2 weeks, 4 days, 21 hours, 8 minutes, 12 seconds
  Estimated time remaining to next output: 32 minutes, 15 seconds
Output 135/977: t=1570000.0 yr, dE/E0=1.40e-07, N=802
  Estimated time remaining to complete simulation: 2 weeks, 4 days, 17 hours, 59 minutes, 21 seconds
  Estimated time remaining to next output: 32 minutes, 3 seconds
Output 136/977: t=1580000.0 yr, dE/E0=1.60e-07, N=802
  Estimated time remaining to complete simulation: 2 weeks, 4 days, 14 hours, 51 minutes, 10 seconds
  Estimated time remaining to next output: 31 minutes, 52 seconds
Output 137/977: t=1590000.0 yr, dE/E0=1.55e-07, N=802
  Estimated time remaining to complete simulation: 2 weeks, 4 days, 11 hours, 47 minutes, 34 seconds
  Estimated time remaining to next output: 31 minutes, 41 seconds
Output 138/977: t=1600000.0 yr, dE/E0=1.58e-07, N=802
  Estimated time remaining to complete simulation: 2 weeks, 4 days, 8 hours, 47 minutes, 44 seconds
  Estimated time remaining to next output: 31 minutes, 31 seconds
Output 139/977: t=1610000.0 yr, dE/E0=1.75e-07, N=802
  Estimated time remaining to complete simulation: 2 weeks, 4 days, 5 hours, 48 minutes, 35 seconds
  Estimated time remaining to next output: 31 minutes, 20 seconds
Output 140/977: t=1620000.0 yr, dE/E0=1.54e-07, N=802
  Estimated time remaining to complete simulation: 2 weeks, 4 days, 2 hours, 50 minutes, 18 seconds
  Estimated time remaining to next output: 31 minutes, 10 seconds
Output 141/977: t=1630000.0 yr, dE/E0=1.42e-07, N=802
  Estimated time remaining to complete simulation: 2 weeks, 3 days, 23 hours, 54 minutes, 49 seconds
  Estimated time remaining to next output: 30 minutes, 59 seconds
Output 142/977: t=1640000.0 yr, dE/E0=1.25e-07, N=802
  Estimated time remaining to complete simulation: 2 weeks, 3 days, 20 hours, 59 minutes, 56 seconds
  Estimated time remaining to next output: 30 minutes, 49 seconds
Output 143/977: t=1650000.0 yr, dE/E0=1.42e-07, N=802
  Estimated time remaining to complete simulation: 2 weeks, 3 days, 18 hours, 12 minutes, 25 seconds
  Estimated time remaining to next output: 30 minutes, 39 seconds
Output 144/977: t=1660000.0 yr, dE/E0=1.45e-07, N=802
  Estimated time remaining to complete simulation: 2 weeks, 3 days, 15 hours, 26 minutes, 50 seconds
  Estimated time remaining to next output: 30 minutes, 30 seconds
Output 145/977: t=1670000.0 yr, dE/E0=1.75e-07, N=802
  Estimated time remaining to complete simulation: 2 weeks, 3 days, 12 hours, 44 minutes, 45 seconds
  Estimated time remaining to next output: 30 minutes, 20 seconds
Output 146/977: t=1680000.0 yr, dE/E0=1.52e-07, N=802
  Estimated time remaining to complete simulation: 2 weeks, 3 days, 10 hours, 6 minutes, 16 seconds
  Estimated time remaining to next output: 30 minutes, 11 seconds
Output 147/977: t=1690000.0 yr, dE/E0=1.65e-07, N=802
  Estimated time remaining to complete simulation: 2 weeks, 3 days, 7 hours, 28 minutes, 39 seconds
  Estimated time remaining to next output: 30 minutes, 2 seconds
Output 148/977: t=1700000.0 yr, dE/E0=1.67e-07, N=802
  Estimated time remaining to complete simulation: 2 weeks, 3 days, 4 hours, 49 minutes, 44 seconds
  Estimated time remaining to next output: 29 minutes, 52 seconds
Output 149/977: t=1710000.0 yr, dE/E0=1.65e-07, N=802
  Estimated time remaining to complete simulation: 2 weeks, 3 days, 2 hours, 10 minutes, 2 seconds
  Estimated time remaining to next output: 29 minutes, 43 seconds
Output 150/977: t=1720000.0 yr, dE/E0=1.64e-07, N=802
  Estimated time remaining to complete simulation: 2 weeks, 2 days, 23 hours, 32 minutes, 14 seconds
  Estimated time remaining to next output: 29 minutes, 34 seconds
Output 151/977: t=1730000.0 yr, dE/E0=1.57e-07, N=802
  Estimated time remaining to complete simulation: 2 weeks, 2 days, 20 hours, 56 minutes, 54 seconds
  Estimated time remaining to next output: 29 minutes, 24 seconds
Output 152/977: t=1740000.0 yr, dE/E0=1.60e-07, N=802
  Estimated time remaining to complete simulation: 2 weeks, 2 days, 18 hours, 23 minutes, 12 seconds
  Estimated time remaining to next output: 29 minutes, 15 seconds
Output 153/977: t=1750000.0 yr, dE/E0=1.47e-07, N=802
  Estimated time remaining to complete simulation: 2 weeks, 2 days, 15 hours, 50 minutes, 47 seconds
  Estimated time remaining to next output: 29 minutes, 6 seconds
Output 154/977: t=1760000.0 yr, dE/E0=1.44e-07, N=802
  Estimated time remaining to complete simulation: 2 weeks, 2 days, 13 hours, 18 minutes, 53 seconds
  Estimated time remaining to next output: 28 minutes, 57 seconds
Output 155/977: t=1770000.0 yr, dE/E0=1.42e-07, N=802
  Estimated time remaining to complete simulation: 2 weeks, 2 days, 10 hours, 49 minutes, 39 seconds
  Estimated time remaining to next output: 28 minutes, 49 seconds
Output 156/977: t=1780000.0 yr, dE/E0=1.57e-07, N=802
  Estimated time remaining to complete simulation: 2 weeks, 2 days, 8 hours, 23 minutes, 23 seconds
  Estimated time remaining to next output: 28 minutes, 40 seconds
Output 157/977: t=1790000.0 yr, dE/E0=1.40e-07, N=802
  Estimated time remaining to complete simulation: 2 weeks, 2 days, 5 hours, 59 minutes, 34 seconds
  Estimated time remaining to next output: 28 minutes, 32 seconds
Output 158/977: t=1800000.0 yr, dE/E0=1.62e-07, N=802
  Estimated time remaining to complete simulation: 2 weeks, 2 days, 3 hours, 37 minutes, 34 seconds
  Estimated time remaining to next output: 28 minutes, 23 seconds
Output 159/977: t=1810000.0 yr, dE/E0=1.53e-07, N=802
  Estimated time remaining to complete simulation: 2 weeks, 2 days, 1 hours, 17 minutes, 39 seconds
  Estimated time remaining to next output: 28 minutes, 15 seconds
Output 160/977: t=1820000.0 yr, dE/E0=1.30e-07, N=802
  Estimated time remaining to complete simulation: 2 weeks, 1 days, 23 hours, 19 seconds
  Estimated time remaining to next output: 28 minutes, 7 seconds
Output 161/977: t=1830000.0 yr, dE/E0=1.42e-07, N=802
  Estimated time remaining to complete simulation: 2 weeks, 1 days, 20 hours, 44 minutes, 39 seconds
  Estimated time remaining to next output: 27 minutes, 59 seconds
Output 162/977: t=1840000.0 yr, dE/E0=1.55e-07, N=802
  Estimated time remaining to complete simulation: 2 weeks, 1 days, 18 hours, 29 minutes, 55 seconds
  Estimated time remaining to next output: 27 minutes, 51 seconds
Output 163/977: t=1850000.0 yr, dE/E0=1.44e-07, N=802
  Estimated time remaining to complete simulation: 2 weeks, 1 days, 16 hours, 13 minutes, 43 seconds
  Estimated time remaining to next output: 27 minutes, 43 seconds
Output 164/977: t=1860000.0 yr, dE/E0=1.48e-07, N=802
  Estimated time remaining to complete simulation: 2 weeks, 1 days, 14 hours, 1 minutes, 24 seconds
  Estimated time remaining to next output: 27 minutes, 36 seconds
Output 165/977: t=1870000.0 yr, dE/E0=1.21e-07, N=802
  Estimated time remaining to complete simulation: 2 weeks, 1 days, 11 hours, 47 minutes, 57 seconds
  Estimated time remaining to next output: 27 minutes, 28 seconds
Output 166/977: t=1880000.0 yr, dE/E0=1.09e-07, N=802
  Estimated time remaining to complete simulation: 2 weeks, 1 days, 9 hours, 36 minutes, 58 seconds
  Estimated time remaining to next output: 27 minutes, 20 seconds
Output 167/977: t=1890000.0 yr, dE/E0=1.15e-07, N=802
  Estimated time remaining to complete simulation: 2 weeks, 1 days, 7 hours, 27 minutes, 12 seconds
  Estimated time remaining to next output: 27 minutes, 13 seconds
Output 168/977: t=1900000.0 yr, dE/E0=1.08e-07, N=802
  Estimated time remaining to complete simulation: 2 weeks, 1 days, 5 hours, 19 minutes, 55 seconds
  Estimated time remaining to next output: 27 minutes, 5 seconds
Output 169/977: t=1910000.0 yr, dE/E0=1.01e-07, N=802
  Estimated time remaining to complete simulation: 2 weeks, 1 days, 3 hours, 14 minutes, 3 seconds
  Estimated time remaining to next output: 26 minutes, 58 seconds
Output 170/977: t=1920000.0 yr, dE/E0=1.18e-07, N=802
  Estimated time remaining to complete simulation: 2 weeks, 1 days, 1 hours, 11 minutes, 16 seconds
  Estimated time remaining to next output: 26 minutes, 51 seconds
Output 171/977: t=1930000.0 yr, dE/E0=1.16e-07, N=802
  Estimated time remaining to complete simulation: 2 weeks, 23 hours, 5 minutes, 36 seconds
  Estimated time remaining to next output: 26 minutes, 43 seconds
Output 172/977: t=1940000.0 yr, dE/E0=1.09e-07, N=802
  Estimated time remaining to complete simulation: 2 weeks, 21 hours, 3 minutes, 22 seconds
  Estimated time remaining to next output: 26 minutes, 36 seconds
Output 173/977: t=1950000.0 yr, dE/E0=1.18e-07, N=802
  Estimated time remaining to complete simulation: 2 weeks, 19 hours, 1 minutes, 41 seconds
  Estimated time remaining to next output: 26 minutes, 29 seconds
Output 174/977: t=1960000.0 yr, dE/E0=1.22e-07, N=802
  Estimated time remaining to complete simulation: 2 weeks, 17 hours, 2 minutes, 21 seconds
  Estimated time remaining to next output: 26 minutes, 22 seconds
Output 175/977: t=1970000.0 yr, dE/E0=1.08e-07, N=802
  Estimated time remaining to complete simulation: 2 weeks, 15 hours, 3 minutes, 7 seconds
  Estimated time remaining to next output: 26 minutes, 15 seconds
Output 176/977: t=1980000.0 yr, dE/E0=1.05e-07, N=802
  Estimated time remaining to complete simulation: 2 weeks, 13 hours, 6 minutes, 56 seconds
  Estimated time remaining to next output: 26 minutes, 9 seconds
Output 177/977: t=1990000.0 yr, dE/E0=1.20e-07, N=802
  Estimated time remaining to complete simulation: 2 weeks, 11 hours, 11 minutes, 27 seconds
  Estimated time remaining to next output: 26 minutes, 2 seconds
Output 178/977: t=2000000.0 yr, dE/E0=1.13e-07, N=802
  Estimated time remaining to complete simulation: 2 weeks, 9 hours, 16 minutes, 11 seconds
  Estimated time remaining to next output: 25 minutes, 55 seconds
Output 179/977: t=2010000.0 yr, dE/E0=1.15e-07, N=802
  Estimated time remaining to complete simulation: 2 weeks, 7 hours, 22 minutes, 35 seconds
  Estimated time remaining to next output: 25 minutes, 49 seconds
Output 180/977: t=2020000.0 yr, dE/E0=1.03e-07, N=802
  Estimated time remaining to complete simulation: 2 weeks, 5 hours, 30 minutes, 21 seconds
  Estimated time remaining to next output: 25 minutes, 42 seconds
Output 181/977: t=2030000.0 yr, dE/E0=9.40e-08, N=802
  Estimated time remaining to complete simulation: 2 weeks, 3 hours, 38 minutes, 20 seconds
  Estimated time remaining to next output: 25 minutes, 36 seconds
Output 182/977: t=2040000.0 yr, dE/E0=6.67e-08, N=802
  Estimated time remaining to complete simulation: 2 weeks, 1 hours, 45 minutes, 20 seconds
  Estimated time remaining to next output: 25 minutes, 29 seconds
Output 183/977: t=2050000.0 yr, dE/E0=5.81e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 6 days, 23 hours, 56 minutes, 21 seconds
  Estimated time remaining to next output: 25 minutes, 23 seconds
Output 184/977: t=2060000.0 yr, dE/E0=6.43e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 6 days, 22 hours, 6 minutes, 22 seconds
  Estimated time remaining to next output: 25 minutes, 16 seconds
Output 185/977: t=2070000.0 yr, dE/E0=7.17e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 6 days, 20 hours, 19 minutes, 10 seconds
  Estimated time remaining to next output: 25 minutes, 10 seconds
Output 186/977: t=2080000.0 yr, dE/E0=8.94e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 6 days, 18 hours, 31 minutes, 9 seconds
  Estimated time remaining to next output: 25 minutes, 4 seconds
Output 187/977: t=2090000.0 yr, dE/E0=9.34e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 6 days, 16 hours, 46 minutes, 31 seconds
  Estimated time remaining to next output: 24 minutes, 58 seconds
Output 188/977: t=2100000.0 yr, dE/E0=9.40e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 6 days, 15 hours, 1 minutes, 6 seconds
  Estimated time remaining to next output: 24 minutes, 52 seconds
Output 189/977: t=2110000.0 yr, dE/E0=1.00e-07, N=802
  Estimated time remaining to complete simulation: 1 weeks, 6 days, 13 hours, 16 minutes, 8 seconds
  Estimated time remaining to next output: 24 minutes, 46 seconds
Output 190/977: t=2120000.0 yr, dE/E0=9.20e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 6 days, 11 hours, 36 minutes, 29 seconds
  Estimated time remaining to next output: 24 minutes, 40 seconds
Output 191/977: t=2130000.0 yr, dE/E0=8.78e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 6 days, 9 hours, 55 minutes, 58 seconds
  Estimated time remaining to next output: 24 minutes, 34 seconds
Output 192/977: t=2140000.0 yr, dE/E0=1.04e-07, N=802
  Estimated time remaining to complete simulation: 1 weeks, 6 days, 8 hours, 15 minutes, 2 seconds
  Estimated time remaining to next output: 24 minutes, 28 seconds
Output 193/977: t=2150000.0 yr, dE/E0=9.83e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 6 days, 6 hours, 34 minutes, 52 seconds
  Estimated time remaining to next output: 24 minutes, 22 seconds
Output 194/977: t=2160000.0 yr, dE/E0=1.05e-07, N=802
  Estimated time remaining to complete simulation: 1 weeks, 6 days, 4 hours, 54 minutes, 40 seconds
  Estimated time remaining to next output: 24 minutes, 17 seconds
Output 195/977: t=2170000.0 yr, dE/E0=8.08e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 6 days, 3 hours, 17 minutes, 26 seconds
  Estimated time remaining to next output: 24 minutes, 11 seconds
Output 196/977: t=2180000.0 yr, dE/E0=6.72e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 6 days, 1 hours, 40 minutes, 2 seconds
  Estimated time remaining to next output: 24 minutes, 5 seconds
Output 197/977: t=2190000.0 yr, dE/E0=8.62e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 6 days, 3 minutes, 26 seconds
  Estimated time remaining to next output: 24 minutes
Output 198/977: t=2200000.0 yr, dE/E0=1.03e-07, N=802
  Estimated time remaining to complete simulation: 1 weeks, 5 days, 22 hours, 27 minutes, 58 seconds
  Estimated time remaining to next output: 23 minutes, 54 seconds
Output 199/977: t=2210000.0 yr, dE/E0=1.14e-07, N=802
  Estimated time remaining to complete simulation: 1 weeks, 5 days, 20 hours, 56 minutes, 7 seconds
  Estimated time remaining to next output: 23 minutes, 49 seconds
Output 200/977: t=2220000.0 yr, dE/E0=1.01e-07, N=802
  Estimated time remaining to complete simulation: 1 weeks, 5 days, 19 hours, 23 minutes, 4 seconds
  Estimated time remaining to next output: 23 minutes, 44 seconds
Output 201/977: t=2230000.0 yr, dE/E0=9.76e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 5 days, 17 hours, 50 minutes, 2 seconds
  Estimated time remaining to next output: 23 minutes, 38 seconds
Output 202/977: t=2240000.0 yr, dE/E0=1.02e-07, N=802
  Estimated time remaining to complete simulation: 1 weeks, 5 days, 16 hours, 19 minutes, 19 seconds
  Estimated time remaining to next output: 23 minutes, 33 seconds
Output 203/977: t=2250000.0 yr, dE/E0=8.54e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 5 days, 14 hours, 48 minutes, 31 seconds
  Estimated time remaining to next output: 23 minutes, 28 seconds
Output 204/977: t=2260000.0 yr, dE/E0=8.90e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 5 days, 13 hours, 18 minutes, 22 seconds
  Estimated time remaining to next output: 23 minutes, 23 seconds
Output 205/977: t=2270000.0 yr, dE/E0=9.76e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 5 days, 11 hours, 50 minutes, 23 seconds
  Estimated time remaining to next output: 23 minutes, 18 seconds
Output 206/977: t=2280000.0 yr, dE/E0=8.06e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 5 days, 10 hours, 22 minutes, 34 seconds
  Estimated time remaining to next output: 23 minutes, 13 seconds
Output 207/977: t=2290000.0 yr, dE/E0=6.66e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 5 days, 8 hours, 54 minutes, 57 seconds
  Estimated time remaining to next output: 23 minutes, 8 seconds
Output 208/977: t=2300000.0 yr, dE/E0=6.71e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 5 days, 7 hours, 27 minutes, 40 seconds
  Estimated time remaining to next output: 23 minutes, 3 seconds
Output 209/977: t=2310000.0 yr, dE/E0=6.37e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 5 days, 6 hours, 11 seconds
  Estimated time remaining to next output: 22 minutes, 58 seconds
Output 210/977: t=2320000.0 yr, dE/E0=6.01e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 5 days, 4 hours, 35 minutes, 3 seconds
  Estimated time remaining to next output: 22 minutes, 53 seconds
Output 211/977: t=2330000.0 yr, dE/E0=6.64e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 5 days, 3 hours, 10 minutes, 56 seconds
  Estimated time remaining to next output: 22 minutes, 48 seconds
Output 212/977: t=2340000.0 yr, dE/E0=4.99e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 5 days, 1 hours, 49 minutes, 30 seconds
  Estimated time remaining to next output: 22 minutes, 43 seconds
Output 213/977: t=2350000.0 yr, dE/E0=4.97e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 5 days, 27 minutes, 33 seconds
  Estimated time remaining to next output: 22 minutes, 39 seconds
Output 214/977: t=2360000.0 yr, dE/E0=6.63e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 4 days, 23 hours, 6 minutes, 47 seconds
  Estimated time remaining to next output: 22 minutes, 34 seconds
Output 215/977: t=2370000.0 yr, dE/E0=5.71e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 4 days, 21 hours, 43 minutes, 30 seconds
  Estimated time remaining to next output: 22 minutes, 29 seconds
Output 216/977: t=2380000.0 yr, dE/E0=5.69e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 4 days, 20 hours, 22 minutes, 33 seconds
  Estimated time remaining to next output: 22 minutes, 25 seconds
Output 217/977: t=2390000.0 yr, dE/E0=6.04e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 4 days, 19 hours, 2 minutes, 19 seconds
  Estimated time remaining to next output: 22 minutes, 20 seconds
Output 218/977: t=2400000.0 yr, dE/E0=5.15e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 4 days, 17 hours, 42 minutes, 21 seconds
  Estimated time remaining to next output: 22 minutes, 16 seconds
Output 219/977: t=2410000.0 yr, dE/E0=5.47e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 4 days, 16 hours, 24 minutes, 21 seconds
  Estimated time remaining to next output: 22 minutes, 11 seconds
Output 220/977: t=2420000.0 yr, dE/E0=3.24e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 4 days, 15 hours, 6 minutes, 44 seconds
  Estimated time remaining to next output: 22 minutes, 7 seconds
Output 221/977: t=2430000.0 yr, dE/E0=2.88e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 4 days, 13 hours, 49 minutes, 57 seconds
  Estimated time remaining to next output: 22 minutes, 3 seconds
Output 222/977: t=2440000.0 yr, dE/E0=2.37e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 4 days, 12 hours, 32 minutes, 30 seconds
  Estimated time remaining to next output: 21 minutes, 58 seconds
Output 223/977: t=2450000.0 yr, dE/E0=4.70e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 4 days, 11 hours, 16 minutes, 23 seconds
  Estimated time remaining to next output: 21 minutes, 54 seconds
Output 224/977: t=2460000.0 yr, dE/E0=3.45e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 4 days, 10 hours, 1 minutes, 9 seconds
  Estimated time remaining to next output: 21 minutes, 50 seconds
Output 225/977: t=2470000.0 yr, dE/E0=2.87e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 4 days, 8 hours, 46 minutes, 35 seconds
  Estimated time remaining to next output: 21 minutes, 45 seconds
Output 226/977: t=2480000.0 yr, dE/E0=3.28e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 4 days, 7 hours, 32 minutes, 1 seconds
  Estimated time remaining to next output: 21 minutes, 41 seconds
Output 227/977: t=2490000.0 yr, dE/E0=3.32e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 4 days, 6 hours, 18 minutes, 53 seconds
  Estimated time remaining to next output: 21 minutes, 37 seconds
Output 228/977: t=2500000.0 yr, dE/E0=4.56e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 4 days, 5 hours, 6 minutes, 49 seconds
  Estimated time remaining to next output: 21 minutes, 33 seconds
Output 229/977: t=2510000.0 yr, dE/E0=6.53e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 4 days, 3 hours, 54 minutes, 2 seconds
  Estimated time remaining to next output: 21 minutes, 29 seconds
Output 230/977: t=2520000.0 yr, dE/E0=4.90e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 4 days, 2 hours, 42 minutes, 22 seconds
  Estimated time remaining to next output: 21 minutes, 25 seconds
Output 231/977: t=2530000.0 yr, dE/E0=1.65e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 4 days, 1 hours, 31 minutes, 43 seconds
  Estimated time remaining to next output: 21 minutes, 21 seconds
Output 232/977: t=2540000.0 yr, dE/E0=3.01e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 4 days, 20 minutes, 54 seconds
  Estimated time remaining to next output: 21 minutes, 17 seconds
Output 233/977: t=2550000.0 yr, dE/E0=2.07e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 3 days, 23 hours, 10 minutes, 26 seconds
  Estimated time remaining to next output: 21 minutes, 13 seconds
Output 234/977: t=2560000.0 yr, dE/E0=2.59e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 3 days, 22 hours, 43 seconds
  Estimated time remaining to next output: 21 minutes, 9 seconds
Output 235/977: t=2570000.0 yr, dE/E0=2.16e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 3 days, 20 hours, 51 minutes, 35 seconds
  Estimated time remaining to next output: 21 minutes, 5 seconds
Output 236/977: t=2580000.0 yr, dE/E0=5.23e-09, N=802
  Estimated time remaining to complete simulation: 1 weeks, 3 days, 19 hours, 42 minutes, 30 seconds
  Estimated time remaining to next output: 21 minutes, 1 seconds
Output 237/977: t=2590000.0 yr, dE/E0=1.23e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 3 days, 18 hours, 34 minutes, 3 seconds
  Estimated time remaining to next output: 20 minutes, 57 seconds
Output 238/977: t=2600000.0 yr, dE/E0=7.33e-09, N=802
  Estimated time remaining to complete simulation: 1 weeks, 3 days, 17 hours, 25 minutes, 34 seconds
  Estimated time remaining to next output: 20 minutes, 54 seconds
Output 239/977: t=2610000.0 yr, dE/E0=1.22e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 3 days, 16 hours, 19 minutes, 19 seconds
  Estimated time remaining to next output: 20 minutes, 50 seconds
Output 240/977: t=2620000.0 yr, dE/E0=6.13e-09, N=802
  Estimated time remaining to complete simulation: 1 weeks, 3 days, 15 hours, 12 minutes, 31 seconds
  Estimated time remaining to next output: 20 minutes, 46 seconds
Output 241/977: t=2630000.0 yr, dE/E0=2.73e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 3 days, 14 hours, 6 minutes, 16 seconds
  Estimated time remaining to next output: 20 minutes, 42 seconds
Output 242/977: t=2640000.0 yr, dE/E0=3.75e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 3 days, 13 hours, 28 seconds
  Estimated time remaining to next output: 20 minutes, 39 seconds
Output 243/977: t=2650000.0 yr, dE/E0=3.73e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 3 days, 11 hours, 55 minutes, 30 seconds
  Estimated time remaining to next output: 20 minutes, 35 seconds
Output 244/977: t=2660000.0 yr, dE/E0=1.80e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 3 days, 10 hours, 51 minutes
  Estimated time remaining to next output: 20 minutes, 32 seconds
Output 245/977: t=2670000.0 yr, dE/E0=3.26e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 3 days, 9 hours, 46 minutes, 9 seconds
  Estimated time remaining to next output: 20 minutes, 28 seconds
Output 246/977: t=2680000.0 yr, dE/E0=1.87e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 3 days, 8 hours, 42 minutes, 9 seconds
  Estimated time remaining to next output: 20 minutes, 24 seconds
Output 247/977: t=2690000.0 yr, dE/E0=3.95e-09, N=802
  Estimated time remaining to complete simulation: 1 weeks, 3 days, 7 hours, 39 minutes, 34 seconds
  Estimated time remaining to next output: 20 minutes, 21 seconds
Output 248/977: t=2700000.0 yr, dE/E0=3.12e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 3 days, 6 hours, 37 minutes, 44 seconds
  Estimated time remaining to next output: 20 minutes, 17 seconds
Output 249/977: t=2710000.0 yr, dE/E0=5.80e-09, N=802
  Estimated time remaining to complete simulation: 1 weeks, 3 days, 5 hours, 34 minutes, 34 seconds
  Estimated time remaining to next output: 20 minutes, 14 seconds
Output 250/977: t=2720000.0 yr, dE/E0=1.51e-10, N=802
  Estimated time remaining to complete simulation: 1 weeks, 3 days, 4 hours, 32 minutes, 46 seconds
  Estimated time remaining to next output: 20 minutes, 10 seconds
Output 251/977: t=2730000.0 yr, dE/E0=1.54e-09, N=802
  Estimated time remaining to complete simulation: 1 weeks, 3 days, 3 hours, 30 minutes, 34 seconds
  Estimated time remaining to next output: 20 minutes, 7 seconds
Output 252/977: t=2740000.0 yr, dE/E0=1.46e-09, N=802
  Estimated time remaining to complete simulation: 1 weeks, 3 days, 2 hours, 29 minutes, 51 seconds
  Estimated time remaining to next output: 20 minutes, 4 seconds
Output 253/977: t=2750000.0 yr, dE/E0=1.88e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 3 days, 1 hours, 28 minutes, 50 seconds
  Estimated time remaining to next output: 20 minutes
Output 254/977: t=2760000.0 yr, dE/E0=7.31e-09, N=802
  Estimated time remaining to complete simulation: 1 weeks, 3 days, 28 minutes, 5 seconds
  Estimated time remaining to next output: 19 minutes, 57 seconds
Output 255/977: t=2770000.0 yr, dE/E0=3.26e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 2 days, 23 hours, 27 minutes, 44 seconds
  Estimated time remaining to next output: 19 minutes, 53 seconds
Output 256/977: t=2780000.0 yr, dE/E0=8.04e-09, N=802
  Estimated time remaining to complete simulation: 1 weeks, 2 days, 22 hours, 28 minutes, 6 seconds
  Estimated time remaining to next output: 19 minutes, 50 seconds
Output 257/977: t=2790000.0 yr, dE/E0=1.95e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 2 days, 21 hours, 29 minutes, 24 seconds
  Estimated time remaining to next output: 19 minutes, 47 seconds
Output 258/977: t=2800000.0 yr, dE/E0=1.82e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 2 days, 20 hours, 30 minutes, 58 seconds
  Estimated time remaining to next output: 19 minutes, 44 seconds
Output 259/977: t=2810000.0 yr, dE/E0=1.80e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 2 days, 19 hours, 32 minutes, 58 seconds
  Estimated time remaining to next output: 19 minutes, 41 seconds
Output 260/977: t=2820000.0 yr, dE/E0=2.90e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 2 days, 18 hours, 35 minutes, 54 seconds
  Estimated time remaining to next output: 19 minutes, 37 seconds
Output 261/977: t=2830000.0 yr, dE/E0=1.86e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 2 days, 17 hours, 38 minutes, 31 seconds
  Estimated time remaining to next output: 19 minutes, 34 seconds
Output 262/977: t=2840000.0 yr, dE/E0=3.64e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 2 days, 16 hours, 42 minutes, 47 seconds
  Estimated time remaining to next output: 19 minutes, 31 seconds
Output 263/977: t=2850000.0 yr, dE/E0=9.35e-09, N=802
  Estimated time remaining to complete simulation: 1 weeks, 2 days, 15 hours, 45 minutes, 59 seconds
  Estimated time remaining to next output: 19 minutes, 28 seconds
Output 264/977: t=2860000.0 yr, dE/E0=1.76e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 2 days, 14 hours, 49 minutes, 52 seconds
  Estimated time remaining to next output: 19 minutes, 25 seconds
Output 265/977: t=2870000.0 yr, dE/E0=2.07e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 2 days, 13 hours, 53 minutes, 21 seconds
  Estimated time remaining to next output: 19 minutes, 22 seconds
Output 266/977: t=2880000.0 yr, dE/E0=2.66e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 2 days, 12 hours, 59 minutes, 12 seconds
  Estimated time remaining to next output: 19 minutes, 19 seconds
Output 267/977: t=2890000.0 yr, dE/E0=2.99e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 2 days, 12 hours, 3 minutes, 20 seconds
  Estimated time remaining to next output: 19 minutes, 16 seconds
Output 268/977: t=2900000.0 yr, dE/E0=2.31e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 2 days, 11 hours, 8 minutes, 7 seconds
  Estimated time remaining to next output: 19 minutes, 13 seconds
Output 269/977: t=2910000.0 yr, dE/E0=1.61e-09, N=802
  Estimated time remaining to complete simulation: 1 weeks, 2 days, 10 hours, 13 minutes, 49 seconds
  Estimated time remaining to next output: 19 minutes, 10 seconds
Output 270/977: t=2920000.0 yr, dE/E0=1.00e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 2 days, 9 hours, 20 minutes, 3 seconds
  Estimated time remaining to next output: 19 minutes, 7 seconds
Output 271/977: t=2930000.0 yr, dE/E0=9.99e-09, N=802
  Estimated time remaining to complete simulation: 1 weeks, 2 days, 8 hours, 27 minutes, 5 seconds
  Estimated time remaining to next output: 19 minutes, 4 seconds
Output 272/977: t=2940000.0 yr, dE/E0=4.20e-09, N=802
  Estimated time remaining to complete simulation: 1 weeks, 2 days, 7 hours, 34 minutes, 3 seconds
  Estimated time remaining to next output: 19 minutes, 1 seconds
Output 273/977: t=2950000.0 yr, dE/E0=8.47e-09, N=802
  Estimated time remaining to complete simulation: 1 weeks, 2 days, 6 hours, 41 minutes
  Estimated time remaining to next output: 18 minutes, 58 seconds
Output 274/977: t=2960000.0 yr, dE/E0=1.97e-09, N=802
  Estimated time remaining to complete simulation: 1 weeks, 2 days, 5 hours, 47 minutes, 56 seconds
  Estimated time remaining to next output: 18 minutes, 55 seconds
Output 275/977: t=2970000.0 yr, dE/E0=4.28e-09, N=802
  Estimated time remaining to complete simulation: 1 weeks, 2 days, 4 hours, 54 minutes, 51 seconds
  Estimated time remaining to next output: 18 minutes, 52 seconds
Output 276/977: t=2980000.0 yr, dE/E0=9.49e-09, N=802
  Estimated time remaining to complete simulation: 1 weeks, 2 days, 4 hours, 3 minutes, 26 seconds
  Estimated time remaining to next output: 18 minutes, 50 seconds
Output 277/977: t=2990000.0 yr, dE/E0=2.05e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 2 days, 3 hours, 10 minutes, 43 seconds
  Estimated time remaining to next output: 18 minutes, 47 seconds
Output 278/977: t=3000000.0 yr, dE/E0=1.02e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 2 days, 2 hours, 19 minutes, 22 seconds
  Estimated time remaining to next output: 18 minutes, 44 seconds
Output 279/977: t=3010000.0 yr, dE/E0=3.09e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 2 days, 1 hours, 29 minutes, 6 seconds
  Estimated time remaining to next output: 18 minutes, 41 seconds
Output 280/977: t=3020000.0 yr, dE/E0=6.74e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 2 days, 39 minutes, 21 seconds
  Estimated time remaining to next output: 18 minutes, 39 seconds
Output 281/977: t=3030000.0 yr, dE/E0=4.52e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 1 days, 23 hours, 48 minutes, 44 seconds
  Estimated time remaining to next output: 18 minutes, 36 seconds
Output 282/977: t=3040000.0 yr, dE/E0=5.74e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 1 days, 22 hours, 58 minutes, 46 seconds
  Estimated time remaining to next output: 18 minutes, 33 seconds
Output 283/977: t=3050000.0 yr, dE/E0=6.10e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 1 days, 22 hours, 8 minutes, 33 seconds
  Estimated time remaining to next output: 18 minutes, 30 seconds
Output 284/977: t=3060000.0 yr, dE/E0=7.78e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 1 days, 21 hours, 18 minutes, 44 seconds
  Estimated time remaining to next output: 18 minutes, 28 seconds
Output 285/977: t=3070000.0 yr, dE/E0=6.66e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 1 days, 20 hours, 29 minutes, 23 seconds
  Estimated time remaining to next output: 18 minutes, 25 seconds
Output 286/977: t=3080000.0 yr, dE/E0=7.61e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 1 days, 19 hours, 40 minutes, 50 seconds
  Estimated time remaining to next output: 18 minutes, 22 seconds
Output 287/977: t=3090000.0 yr, dE/E0=6.87e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 1 days, 18 hours, 52 minutes, 8 seconds
  Estimated time remaining to next output: 18 minutes, 20 seconds
Output 288/977: t=3100000.0 yr, dE/E0=8.47e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 1 days, 18 hours, 4 minutes, 22 seconds
  Estimated time remaining to next output: 18 minutes, 17 seconds
Output 289/977: t=3110000.0 yr, dE/E0=7.70e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 1 days, 17 hours, 17 minutes, 39 seconds
  Estimated time remaining to next output: 18 minutes, 15 seconds
Output 290/977: t=3120000.0 yr, dE/E0=9.93e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 1 days, 16 hours, 29 minutes, 20 seconds
  Estimated time remaining to next output: 18 minutes, 12 seconds
Output 291/977: t=3130000.0 yr, dE/E0=1.00e-07, N=802
  Estimated time remaining to complete simulation: 1 weeks, 1 days, 15 hours, 41 minutes, 55 seconds
  Estimated time remaining to next output: 18 minutes, 9 seconds
Output 292/977: t=3140000.0 yr, dE/E0=1.00e-07, N=802
  Estimated time remaining to complete simulation: 1 weeks, 1 days, 14 hours, 54 minutes, 34 seconds
  Estimated time remaining to next output: 18 minutes, 7 seconds
Output 293/977: t=3150000.0 yr, dE/E0=7.49e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 1 days, 14 hours, 8 minutes, 28 seconds
  Estimated time remaining to next output: 18 minutes, 4 seconds
Output 294/977: t=3160000.0 yr, dE/E0=9.20e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 1 days, 13 hours, 21 minutes, 46 seconds
  Estimated time remaining to next output: 18 minutes, 2 seconds
Output 295/977: t=3170000.0 yr, dE/E0=8.59e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 1 days, 12 hours, 34 minutes, 42 seconds
  Estimated time remaining to next output: 17 minutes, 59 seconds
Output 296/977: t=3180000.0 yr, dE/E0=9.28e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 1 days, 11 hours, 48 minutes, 55 seconds
  Estimated time remaining to next output: 17 minutes, 57 seconds
Output 297/977: t=3190000.0 yr, dE/E0=9.28e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 1 days, 11 hours, 3 minutes, 12 seconds
  Estimated time remaining to next output: 17 minutes, 54 seconds
Output 298/977: t=3200000.0 yr, dE/E0=7.99e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 1 days, 10 hours, 17 minutes, 54 seconds
  Estimated time remaining to next output: 17 minutes, 52 seconds
Output 299/977: t=3210000.0 yr, dE/E0=1.09e-07, N=802
  Estimated time remaining to complete simulation: 1 weeks, 1 days, 9 hours, 31 minutes, 45 seconds
  Estimated time remaining to next output: 17 minutes, 50 seconds
Output 300/977: t=3220000.0 yr, dE/E0=1.02e-07, N=802
  Estimated time remaining to complete simulation: 1 weeks, 1 days, 8 hours, 46 minutes, 38 seconds
  Estimated time remaining to next output: 17 minutes, 47 seconds
Output 301/977: t=3230000.0 yr, dE/E0=8.77e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 1 days, 8 hours, 2 minutes, 4 seconds
  Estimated time remaining to next output: 17 minutes, 45 seconds
Output 302/977: t=3240000.0 yr, dE/E0=9.41e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 1 days, 7 hours, 17 minutes, 31 seconds
  Estimated time remaining to next output: 17 minutes, 42 seconds
Output 303/977: t=3250000.0 yr, dE/E0=1.08e-07, N=802
  Estimated time remaining to complete simulation: 1 weeks, 1 days, 6 hours, 34 minutes, 40 seconds
  Estimated time remaining to next output: 17 minutes, 40 seconds
Output 304/977: t=3260000.0 yr, dE/E0=1.16e-07, N=802
  Estimated time remaining to complete simulation: 1 weeks, 1 days, 5 hours, 50 minutes, 46 seconds
  Estimated time remaining to next output: 17 minutes, 38 seconds
Output 305/977: t=3270000.0 yr, dE/E0=1.15e-07, N=802
  Estimated time remaining to complete simulation: 1 weeks, 1 days, 5 hours, 6 minutes, 36 seconds
  Estimated time remaining to next output: 17 minutes, 35 seconds
Output 306/977: t=3280000.0 yr, dE/E0=1.16e-07, N=802
  Estimated time remaining to complete simulation: 1 weeks, 1 days, 4 hours, 22 minutes, 40 seconds
  Estimated time remaining to next output: 17 minutes, 33 seconds
Output 307/977: t=3290000.0 yr, dE/E0=1.13e-07, N=802
  Estimated time remaining to complete simulation: 1 weeks, 1 days, 3 hours, 39 minutes, 41 seconds
  Estimated time remaining to next output: 17 minutes, 31 seconds
Output 308/977: t=3300000.0 yr, dE/E0=1.19e-07, N=802
  Estimated time remaining to complete simulation: 1 weeks, 1 days, 2 hours, 57 minutes, 9 seconds
  Estimated time remaining to next output: 17 minutes, 29 seconds
Output 309/977: t=3310000.0 yr, dE/E0=1.16e-07, N=802
  Estimated time remaining to complete simulation: 1 weeks, 1 days, 2 hours, 15 minutes, 40 seconds
  Estimated time remaining to next output: 17 minutes, 26 seconds
Output 310/977: t=3320000.0 yr, dE/E0=1.22e-07, N=802
  Estimated time remaining to complete simulation: 1 weeks, 1 days, 1 hours, 32 minutes, 37 seconds
  Estimated time remaining to next output: 17 minutes, 24 seconds
Output 311/977: t=3330000.0 yr, dE/E0=1.00e-07, N=802
  Estimated time remaining to complete simulation: 1 weeks, 1 days, 49 minutes, 54 seconds
  Estimated time remaining to next output: 17 minutes, 22 seconds
Output 312/977: t=3340000.0 yr, dE/E0=1.13e-07, N=802
  Estimated time remaining to complete simulation: 1 weeks, 1 days, 8 minutes
  Estimated time remaining to next output: 17 minutes, 20 seconds
Output 313/977: t=3350000.0 yr, dE/E0=1.03e-07, N=802
  Estimated time remaining to complete simulation: 1 weeks, 23 hours, 26 minutes, 12 seconds
  Estimated time remaining to next output: 17 minutes, 17 seconds
Output 314/977: t=3360000.0 yr, dE/E0=1.03e-07, N=802
  Estimated time remaining to complete simulation: 1 weeks, 22 hours, 44 minutes, 56 seconds
  Estimated time remaining to next output: 17 minutes, 15 seconds
Output 315/977: t=3370000.0 yr, dE/E0=9.41e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 22 hours, 2 minutes, 54 seconds
  Estimated time remaining to next output: 17 minutes, 13 seconds
Output 316/977: t=3380000.0 yr, dE/E0=9.26e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 21 hours, 21 minutes, 38 seconds
  Estimated time remaining to next output: 17 minutes, 11 seconds
Output 317/977: t=3390000.0 yr, dE/E0=9.88e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 20 hours, 40 minutes, 6 seconds
  Estimated time remaining to next output: 17 minutes, 9 seconds
Output 318/977: t=3400000.0 yr, dE/E0=1.18e-07, N=802
  Estimated time remaining to complete simulation: 1 weeks, 19 hours, 59 minutes, 41 seconds
  Estimated time remaining to next output: 17 minutes, 6 seconds
Output 319/977: t=3410000.0 yr, dE/E0=1.03e-07, N=802
  Estimated time remaining to complete simulation: 1 weeks, 19 hours, 19 minutes, 28 seconds
  Estimated time remaining to next output: 17 minutes, 4 seconds
Output 320/977: t=3420000.0 yr, dE/E0=1.10e-07, N=802
  Estimated time remaining to complete simulation: 1 weeks, 18 hours, 38 minutes, 53 seconds
  Estimated time remaining to next output: 17 minutes, 2 seconds
Output 321/977: t=3430000.0 yr, dE/E0=1.23e-07, N=802
  Estimated time remaining to complete simulation: 1 weeks, 17 hours, 57 minutes, 53 seconds
  Estimated time remaining to next output: 17 minutes
Output 322/977: t=3440000.0 yr, dE/E0=1.17e-07, N=802
  Estimated time remaining to complete simulation: 1 weeks, 17 hours, 18 minutes, 10 seconds
  Estimated time remaining to next output: 16 minutes, 58 seconds
Output 323/977: t=3450000.0 yr, dE/E0=1.07e-07, N=802
  Estimated time remaining to complete simulation: 1 weeks, 16 hours, 38 minutes, 48 seconds
  Estimated time remaining to next output: 16 minutes, 56 seconds
Output 324/977: t=3460000.0 yr, dE/E0=1.03e-07, N=802
  Estimated time remaining to complete simulation: 1 weeks, 15 hours, 58 minutes, 59 seconds
  Estimated time remaining to next output: 16 minutes, 54 seconds
Output 325/977: t=3470000.0 yr, dE/E0=9.87e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 15 hours, 19 minutes, 45 seconds
  Estimated time remaining to next output: 16 minutes, 52 seconds
Output 326/977: t=3480000.0 yr, dE/E0=1.11e-07, N=802
  Estimated time remaining to complete simulation: 1 weeks, 14 hours, 41 minutes, 2 seconds
  Estimated time remaining to next output: 16 minutes, 50 seconds
Output 327/977: t=3490000.0 yr, dE/E0=9.26e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 14 hours, 2 minutes, 25 seconds
  Estimated time remaining to next output: 16 minutes, 48 seconds
Output 328/977: t=3500000.0 yr, dE/E0=1.02e-07, N=802
  Estimated time remaining to complete simulation: 1 weeks, 13 hours, 23 minutes, 18 seconds
  Estimated time remaining to next output: 16 minutes, 46 seconds
Output 329/977: t=3510000.0 yr, dE/E0=1.04e-07, N=802
  Estimated time remaining to complete simulation: 1 weeks, 12 hours, 45 minutes, 27 seconds
  Estimated time remaining to next output: 16 minutes, 44 seconds
Output 330/977: t=3520000.0 yr, dE/E0=1.03e-07, N=802
  Estimated time remaining to complete simulation: 1 weeks, 12 hours, 7 minutes, 20 seconds
  Estimated time remaining to next output: 16 minutes, 42 seconds
Output 331/977: t=3530000.0 yr, dE/E0=1.05e-07, N=802
  Estimated time remaining to complete simulation: 1 weeks, 11 hours, 29 minutes, 12 seconds
  Estimated time remaining to next output: 16 minutes, 40 seconds
Output 332/977: t=3540000.0 yr, dE/E0=1.14e-07, N=802
  Estimated time remaining to complete simulation: 1 weeks, 10 hours, 51 minutes, 33 seconds
  Estimated time remaining to next output: 16 minutes, 38 seconds
Output 333/977: t=3550000.0 yr, dE/E0=1.05e-07, N=802
  Estimated time remaining to complete simulation: 1 weeks, 10 hours, 14 minutes, 30 seconds
  Estimated time remaining to next output: 16 minutes, 36 seconds
Output 334/977: t=3560000.0 yr, dE/E0=9.59e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 9 hours, 36 minutes, 59 seconds
  Estimated time remaining to next output: 16 minutes, 34 seconds
Output 335/977: t=3570000.0 yr, dE/E0=8.38e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 8 hours, 59 minutes, 37 seconds
  Estimated time remaining to next output: 16 minutes, 32 seconds
Output 336/977: t=3580000.0 yr, dE/E0=8.20e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 8 hours, 22 minutes, 11 seconds
  Estimated time remaining to next output: 16 minutes, 30 seconds
Output 337/977: t=3590000.0 yr, dE/E0=7.86e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 7 hours, 45 minutes, 29 seconds
  Estimated time remaining to next output: 16 minutes, 28 seconds
Output 338/977: t=3600000.0 yr, dE/E0=7.86e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 7 hours, 8 minutes, 40 seconds
  Estimated time remaining to next output: 16 minutes, 26 seconds
Output 339/977: t=3610000.0 yr, dE/E0=7.20e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 6 hours, 31 minutes, 48 seconds
  Estimated time remaining to next output: 16 minutes, 24 seconds
Output 340/977: t=3620000.0 yr, dE/E0=6.75e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 5 hours, 55 minutes, 56 seconds
  Estimated time remaining to next output: 16 minutes, 22 seconds
Output 341/977: t=3630000.0 yr, dE/E0=8.50e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 5 hours, 19 minutes, 14 seconds
  Estimated time remaining to next output: 16 minutes, 21 seconds
Output 342/977: t=3640000.0 yr, dE/E0=8.27e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 4 hours, 43 minutes, 22 seconds
  Estimated time remaining to next output: 16 minutes, 19 seconds
Output 343/977: t=3650000.0 yr, dE/E0=9.51e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 4 hours, 8 minutes, 4 seconds
  Estimated time remaining to next output: 16 minutes, 17 seconds
Output 344/977: t=3660000.0 yr, dE/E0=8.52e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 3 hours, 33 minutes, 14 seconds
  Estimated time remaining to next output: 16 minutes, 15 seconds
Output 345/977: t=3670000.0 yr, dE/E0=1.00e-07, N=802
  Estimated time remaining to complete simulation: 1 weeks, 2 hours, 58 minutes, 49 seconds
  Estimated time remaining to next output: 16 minutes, 13 seconds
Output 346/977: t=3680000.0 yr, dE/E0=1.05e-07, N=802
  Estimated time remaining to complete simulation: 1 weeks, 2 hours, 23 minutes, 19 seconds
  Estimated time remaining to next output: 16 minutes, 12 seconds
Output 347/977: t=3690000.0 yr, dE/E0=1.13e-07, N=802
  Estimated time remaining to complete simulation: 1 weeks, 1 hours, 48 minutes, 39 seconds
  Estimated time remaining to next output: 16 minutes, 10 seconds
Output 348/977: t=3700000.0 yr, dE/E0=1.09e-07, N=802
  Estimated time remaining to complete simulation: 1 weeks, 1 hours, 13 minutes, 55 seconds
  Estimated time remaining to next output: 16 minutes, 8 seconds
Output 349/977: t=3710000.0 yr, dE/E0=9.26e-08, N=802
  Estimated time remaining to complete simulation: 1 weeks, 39 minutes, 4 seconds
  Estimated time remaining to next output: 16 minutes, 6 seconds
Output 350/977: t=3720000.0 yr, dE/E0=1.08e-07, N=802
  Estimated time remaining to complete simulation: 1 weeks, 4 minutes, 37 seconds
  Estimated time remaining to next output: 16 minutes, 5 seconds
Output 351/977: t=3730000.0 yr, dE/E0=1.00e-07, N=802
  Estimated time remaining to complete simulation: 6 days, 23 hours, 30 minutes, 12 seconds
  Estimated time remaining to next output: 16 minutes, 3 seconds
Output 352/977: t=3740000.0 yr, dE/E0=7.13e-08, N=802
  Estimated time remaining to complete simulation: 6 days, 22 hours, 56 minutes, 32 seconds
  Estimated time remaining to next output: 16 minutes, 1 seconds
Output 353/977: t=3750000.0 yr, dE/E0=8.19e-08, N=802
  Estimated time remaining to complete simulation: 6 days, 22 hours, 22 minutes, 27 seconds
  Estimated time remaining to next output: 15 minutes, 59 seconds
Output 354/977: t=3760000.0 yr, dE/E0=8.21e-08, N=802
  Estimated time remaining to complete simulation: 6 days, 21 hours, 48 minutes, 22 seconds
  Estimated time remaining to next output: 15 minutes, 58 seconds
Output 355/977: t=3770000.0 yr, dE/E0=7.58e-08, N=802
  Estimated time remaining to complete simulation: 6 days, 21 hours, 15 minutes, 2 seconds
  Estimated time remaining to next output: 15 minutes, 56 seconds
Output 356/977: t=3780000.0 yr, dE/E0=9.65e-08, N=802
  Estimated time remaining to complete simulation: 6 days, 20 hours, 41 minutes, 33 seconds
  Estimated time remaining to next output: 15 minutes, 54 seconds
Output 357/977: t=3790000.0 yr, dE/E0=6.33e-08, N=802
  Estimated time remaining to complete simulation: 6 days, 20 hours, 8 minutes, 6 seconds
  Estimated time remaining to next output: 15 minutes, 53 seconds
Output 358/977: t=3800000.0 yr, dE/E0=8.67e-08, N=802
  Estimated time remaining to complete simulation: 6 days, 19 hours, 35 minutes, 4 seconds
  Estimated time remaining to next output: 15 minutes, 51 seconds
Output 359/977: t=3810000.0 yr, dE/E0=6.39e-08, N=802
  Estimated time remaining to complete simulation: 6 days, 19 hours, 2 minutes, 35 seconds
  Estimated time remaining to next output: 15 minutes, 49 seconds
Output 360/977: t=3820000.0 yr, dE/E0=7.08e-08, N=802
  Estimated time remaining to complete simulation: 6 days, 18 hours, 30 minutes
  Estimated time remaining to next output: 15 minutes, 48 seconds
Output 361/977: t=3830000.0 yr, dE/E0=7.98e-08, N=802
  Estimated time remaining to complete simulation: 6 days, 17 hours, 57 minutes, 4 seconds
  Estimated time remaining to next output: 15 minutes, 46 seconds
Output 362/977: t=3840000.0 yr, dE/E0=7.80e-08, N=802
  Estimated time remaining to complete simulation: 6 days, 17 hours, 24 minutes, 54 seconds
  Estimated time remaining to next output: 15 minutes, 44 seconds
Output 363/977: t=3850000.0 yr, dE/E0=8.70e-08, N=802
  Estimated time remaining to complete simulation: 6 days, 16 hours, 52 minutes, 29 seconds
  Estimated time remaining to next output: 15 minutes, 43 seconds
Output 364/977: t=3860000.0 yr, dE/E0=8.10e-08, N=802
  Estimated time remaining to complete simulation: 6 days, 16 hours, 20 minutes, 3 seconds
  Estimated time remaining to next output: 15 minutes, 41 seconds
Output 365/977: t=3870000.0 yr, dE/E0=9.31e-08, N=802
  Estimated time remaining to complete simulation: 6 days, 15 hours, 48 minutes, 50 seconds
  Estimated time remaining to next output: 15 minutes, 40 seconds
Output 366/977: t=3880000.0 yr, dE/E0=7.76e-08, N=802
  Estimated time remaining to complete simulation: 6 days, 15 hours, 16 minutes, 4 seconds
  Estimated time remaining to next output: 15 minutes, 38 seconds
Output 367/977: t=3890000.0 yr, dE/E0=8.32e-08, N=802
  Estimated time remaining to complete simulation: 6 days, 14 hours, 43 minutes, 53 seconds
  Estimated time remaining to next output: 15 minutes, 36 seconds
Output 368/977: t=3900000.0 yr, dE/E0=7.31e-08, N=802
  Estimated time remaining to complete simulation: 6 days, 14 hours, 11 minutes, 46 seconds
  Estimated time remaining to next output: 15 minutes, 35 seconds
Output 369/977: t=3910000.0 yr, dE/E0=1.04e-07, N=802
  Estimated time remaining to complete simulation: 6 days, 13 hours, 39 minutes, 34 seconds
  Estimated time remaining to next output: 15 minutes, 33 seconds
Output 370/977: t=3920000.0 yr, dE/E0=9.35e-08, N=802
  Estimated time remaining to complete simulation: 6 days, 13 hours, 7 minutes, 54 seconds
  Estimated time remaining to next output: 15 minutes, 31 seconds
Output 371/977: t=3930000.0 yr, dE/E0=1.02e-07, N=802
  Estimated time remaining to complete simulation: 6 days, 12 hours, 35 minutes, 43 seconds
  Estimated time remaining to next output: 15 minutes, 30 seconds
Output 372/977: t=3940000.0 yr, dE/E0=9.88e-08, N=802
  Estimated time remaining to complete simulation: 6 days, 12 hours, 3 minutes, 31 seconds
  Estimated time remaining to next output: 15 minutes, 28 seconds
Output 373/977: t=3950000.0 yr, dE/E0=7.11e-08, N=802
  Estimated time remaining to complete simulation: 6 days, 11 hours, 31 minutes, 32 seconds
  Estimated time remaining to next output: 15 minutes, 26 seconds
Output 374/977: t=3960000.0 yr, dE/E0=6.89e-08, N=802
  Estimated time remaining to complete simulation: 6 days, 11 hours, 14 seconds
  Estimated time remaining to next output: 15 minutes, 25 seconds
Output 375/977: t=3970000.0 yr, dE/E0=5.83e-08, N=802
  Estimated time remaining to complete simulation: 6 days, 10 hours, 28 minutes, 54 seconds
  Estimated time remaining to next output: 15 minutes, 23 seconds
Output 376/977: t=3980000.0 yr, dE/E0=7.45e-08, N=802
  Estimated time remaining to complete simulation: 6 days, 9 hours, 57 minutes, 39 seconds
  Estimated time remaining to next output: 15 minutes, 22 seconds
Output 377/977: t=3990000.0 yr, dE/E0=5.79e-08, N=802
  Estimated time remaining to complete simulation: 6 days, 9 hours, 26 minutes, 19 seconds
  Estimated time remaining to next output: 15 minutes, 20 seconds
Output 378/977: t=4000000.0 yr, dE/E0=5.88e-08, N=802
  Estimated time remaining to complete simulation: 6 days, 8 hours, 54 minutes, 47 seconds
  Estimated time remaining to next output: 15 minutes, 19 seconds
Output 379/977: t=4010000.0 yr, dE/E0=6.09e-08, N=802
  Estimated time remaining to complete simulation: 6 days, 8 hours, 23 minutes, 32 seconds
  Estimated time remaining to next output: 15 minutes, 17 seconds
Output 380/977: t=4020000.0 yr, dE/E0=4.53e-08, N=802
  Estimated time remaining to complete simulation: 6 days, 7 hours, 52 minutes, 55 seconds
  Estimated time remaining to next output: 15 minutes, 15 seconds
Output 381/977: t=4030000.0 yr, dE/E0=7.51e-08, N=802
  Estimated time remaining to complete simulation: 6 days, 7 hours, 22 minutes, 14 seconds
  Estimated time remaining to next output: 15 minutes, 14 seconds
Output 382/977: t=4040000.0 yr, dE/E0=3.95e-08, N=802
  Estimated time remaining to complete simulation: 6 days, 6 hours, 52 minutes, 14 seconds
  Estimated time remaining to next output: 15 minutes, 12 seconds
Output 383/977: t=4050000.0 yr, dE/E0=6.34e-08, N=802
  Estimated time remaining to complete simulation: 6 days, 6 hours, 22 minutes, 12 seconds
  Estimated time remaining to next output: 15 minutes, 11 seconds
Output 384/977: t=4060000.0 yr, dE/E0=7.33e-08, N=802
  Estimated time remaining to complete simulation: 6 days, 5 hours, 51 minutes, 37 seconds
  Estimated time remaining to next output: 15 minutes, 9 seconds
Output 385/977: t=4070000.0 yr, dE/E0=5.05e-08, N=802
  Estimated time remaining to complete simulation: 6 days, 5 hours, 21 minutes, 56 seconds
  Estimated time remaining to next output: 15 minutes, 8 seconds
Output 386/977: t=4080000.0 yr, dE/E0=2.15e-08, N=802
  Estimated time remaining to complete simulation: 6 days, 4 hours, 52 minutes, 50 seconds
  Estimated time remaining to next output: 15 minutes, 6 seconds
Output 387/977: t=4090000.0 yr, dE/E0=4.57e-08, N=802
  Estimated time remaining to complete simulation: 6 days, 4 hours, 23 minutes, 24 seconds
  Estimated time remaining to next output: 15 minutes, 5 seconds
Output 388/977: t=4100000.0 yr, dE/E0=2.97e-08, N=802
  Estimated time remaining to complete simulation: 6 days, 3 hours, 54 minutes, 14 seconds
  Estimated time remaining to next output: 15 minutes, 3 seconds
Output 389/977: t=4110000.0 yr, dE/E0=1.67e-08, N=802
  Estimated time remaining to complete simulation: 6 days, 3 hours, 24 minutes, 39 seconds
  Estimated time remaining to next output: 15 minutes, 2 seconds
Output 390/977: t=4120000.0 yr, dE/E0=2.22e-08, N=802
  Estimated time remaining to complete simulation: 6 days, 2 hours, 55 minutes, 34 seconds
  Estimated time remaining to next output: 15 minutes, 1 seconds
Output 391/977: t=4130000.0 yr, dE/E0=4.29e-08, N=802
  Estimated time remaining to complete simulation: 6 days, 2 hours, 26 minutes, 22 seconds
  Estimated time remaining to next output: 14 minutes, 59 seconds
Output 392/977: t=4140000.0 yr, dE/E0=3.21e-08, N=802
  Estimated time remaining to complete simulation: 6 days, 1 hours, 56 minutes, 55 seconds
  Estimated time remaining to next output: 14 minutes, 58 seconds
Output 393/977: t=4150000.0 yr, dE/E0=4.95e-08, N=802
  Estimated time remaining to complete simulation: 6 days, 1 hours, 27 minutes, 54 seconds
  Estimated time remaining to next output: 14 minutes, 56 seconds
Output 394/977: t=4160000.0 yr, dE/E0=4.85e-08, N=802
  Estimated time remaining to complete simulation: 6 days, 59 minutes, 40 seconds
  Estimated time remaining to next output: 14 minutes, 55 seconds
Output 395/977: t=4170000.0 yr, dE/E0=5.97e-08, N=802
  Estimated time remaining to complete simulation: 6 days, 31 minutes, 27 seconds
  Estimated time remaining to next output: 14 minutes, 53 seconds
Output 396/977: t=4180000.0 yr, dE/E0=4.52e-08, N=802
  Estimated time remaining to complete simulation: 6 days, 3 minutes, 5 seconds
  Estimated time remaining to next output: 14 minutes, 52 seconds
Output 397/977: t=4190000.0 yr, dE/E0=4.84e-08, N=802
  Estimated time remaining to complete simulation: 5 days, 23 hours, 34 minutes, 54 seconds
  Estimated time remaining to next output: 14 minutes, 51 seconds
Output 398/977: t=4200000.0 yr, dE/E0=2.49e-08, N=802
  Estimated time remaining to complete simulation: 5 days, 23 hours, 6 minutes, 10 seconds
  Estimated time remaining to next output: 14 minutes, 49 seconds
Output 399/977: t=4210000.0 yr, dE/E0=2.23e-08, N=802
  Estimated time remaining to complete simulation: 5 days, 22 hours, 37 minutes, 59 seconds
  Estimated time remaining to next output: 14 minutes, 48 seconds
Output 400/977: t=4220000.0 yr, dE/E0=5.16e-08, N=802
  Estimated time remaining to complete simulation: 5 days, 22 hours, 10 minutes, 3 seconds
  Estimated time remaining to next output: 14 minutes, 47 seconds
Output 401/977: t=4230000.0 yr, dE/E0=5.83e-08, N=802
  Estimated time remaining to complete simulation: 5 days, 21 hours, 41 minutes, 47 seconds
  Estimated time remaining to next output: 14 minutes, 45 seconds
Output 402/977: t=4240000.0 yr, dE/E0=5.73e-08, N=802
  Estimated time remaining to complete simulation: 5 days, 21 hours, 13 minutes, 56 seconds
  Estimated time remaining to next output: 14 minutes, 44 seconds
Output 403/977: t=4250000.0 yr, dE/E0=3.41e-08, N=802
  Estimated time remaining to complete simulation: 5 days, 20 hours, 45 minutes, 56 seconds
  Estimated time remaining to next output: 14 minutes, 42 seconds
Output 404/977: t=4260000.0 yr, dE/E0=4.37e-08, N=802
  Estimated time remaining to complete simulation: 5 days, 20 hours, 18 minutes, 9 seconds
  Estimated time remaining to next output: 14 minutes, 41 seconds
Output 405/977: t=4270000.0 yr, dE/E0=4.50e-08, N=802
  Estimated time remaining to complete simulation: 5 days, 19 hours, 50 minutes, 6 seconds
  Estimated time remaining to next output: 14 minutes, 40 seconds
Output 406/977: t=4280000.0 yr, dE/E0=4.71e-08, N=802
  Estimated time remaining to complete simulation: 5 days, 19 hours, 22 minutes, 45 seconds
  Estimated time remaining to next output: 14 minutes, 38 seconds
Output 407/977: t=4290000.0 yr, dE/E0=6.74e-08, N=802
  Estimated time remaining to complete simulation: 5 days, 18 hours, 54 minutes, 52 seconds
  Estimated time remaining to next output: 14 minutes, 37 seconds
Output 408/977: t=4300000.0 yr, dE/E0=5.33e-08, N=802
  Estimated time remaining to complete simulation: 5 days, 18 hours, 27 minutes, 22 seconds
  Estimated time remaining to next output: 14 minutes, 35 seconds
Output 409/977: t=4310000.0 yr, dE/E0=5.68e-08, N=802
  Estimated time remaining to complete simulation: 5 days, 18 hours, 7 seconds
  Estimated time remaining to next output: 14 minutes, 34 seconds
Output 410/977: t=4320000.0 yr, dE/E0=7.41e-08, N=802
  Estimated time remaining to complete simulation: 5 days, 17 hours, 32 minutes, 29 seconds
  Estimated time remaining to next output: 14 minutes, 33 seconds
Output 411/977: t=4330000.0 yr, dE/E0=8.26e-08, N=802
  Estimated time remaining to complete simulation: 5 days, 17 hours, 4 minutes, 36 seconds
  Estimated time remaining to next output: 14 minutes, 31 seconds
Output 412/977: t=4340000.0 yr, dE/E0=9.01e-08, N=802
  Estimated time remaining to complete simulation: 5 days, 16 hours, 37 minutes, 28 seconds
  Estimated time remaining to next output: 14 minutes, 30 seconds
Output 413/977: t=4350000.0 yr, dE/E0=7.60e-08, N=802
  Estimated time remaining to complete simulation: 5 days, 16 hours, 10 minutes, 7 seconds
  Estimated time remaining to next output: 14 minutes, 29 seconds
Output 414/977: t=4360000.0 yr, dE/E0=7.65e-08, N=802
  Estimated time remaining to complete simulation: 5 days, 15 hours, 42 minutes, 54 seconds
  Estimated time remaining to next output: 14 minutes, 27 seconds
Output 415/977: t=4370000.0 yr, dE/E0=7.42e-08, N=802
  Estimated time remaining to complete simulation: 5 days, 15 hours, 15 minutes, 41 seconds
  Estimated time remaining to next output: 14 minutes, 26 seconds
Output 416/977: t=4380000.0 yr, dE/E0=4.66e-08, N=802
  Estimated time remaining to complete simulation: 5 days, 14 hours, 48 minutes, 59 seconds
  Estimated time remaining to next output: 14 minutes, 25 seconds
Output 417/977: t=4390000.0 yr, dE/E0=6.00e-08, N=802
  Estimated time remaining to complete simulation: 5 days, 14 hours, 22 minutes
  Estimated time remaining to next output: 14 minutes, 23 seconds
Output 418/977: t=4400000.0 yr, dE/E0=5.19e-08, N=802
  Estimated time remaining to complete simulation: 5 days, 13 hours, 55 minutes, 39 seconds
  Estimated time remaining to next output: 14 minutes, 22 seconds
Output 419/977: t=4410000.0 yr, dE/E0=4.61e-08, N=802
  Estimated time remaining to complete simulation: 5 days, 13 hours, 28 minutes, 52 seconds
  Estimated time remaining to next output: 14 minutes, 21 seconds
Output 420/977: t=4420000.0 yr, dE/E0=4.32e-08, N=802
  Estimated time remaining to complete simulation: 5 days, 13 hours, 2 minutes, 6 seconds
  Estimated time remaining to next output: 14 minutes, 19 seconds
Output 421/977: t=4430000.0 yr, dE/E0=5.60e-08, N=802
  Estimated time remaining to complete simulation: 5 days, 12 hours, 35 minutes, 38 seconds
  Estimated time remaining to next output: 14 minutes, 18 seconds
Output 422/977: t=4440000.0 yr, dE/E0=4.29e-08, N=802
  Estimated time remaining to complete simulation: 5 days, 12 hours, 9 minutes, 14 seconds
  Estimated time remaining to next output: 14 minutes, 17 seconds
Output 423/977: t=4450000.0 yr, dE/E0=3.82e-08, N=802
  Estimated time remaining to complete simulation: 5 days, 11 hours, 43 minutes, 7 seconds
  Estimated time remaining to next output: 14 minutes, 15 seconds
Output 424/977: t=4460000.0 yr, dE/E0=5.01e-08, N=802
  Estimated time remaining to complete simulation: 5 days, 11 hours, 16 minutes, 39 seconds
  Estimated time remaining to next output: 14 minutes, 14 seconds
Output 425/977: t=4470000.0 yr, dE/E0=3.42e-08, N=802
  Estimated time remaining to complete simulation: 5 days, 10 hours, 50 minutes, 39 seconds
  Estimated time remaining to next output: 14 minutes, 13 seconds
Output 426/977: t=4480000.0 yr, dE/E0=4.23e-08, N=802
  Estimated time remaining to complete simulation: 5 days, 10 hours, 24 minutes, 44 seconds
  Estimated time remaining to next output: 14 minutes, 12 seconds
Output 427/977: t=4490000.0 yr, dE/E0=2.59e-08, N=802
  Estimated time remaining to complete simulation: 5 days, 9 hours, 59 minutes, 24 seconds
  Estimated time remaining to next output: 14 minutes, 10 seconds
Output 428/977: t=4500000.0 yr, dE/E0=3.07e-08, N=802
  Estimated time remaining to complete simulation: 5 days, 9 hours, 33 minutes, 44 seconds
  Estimated time remaining to next output: 14 minutes, 9 seconds
Output 429/977: t=4510000.0 yr, dE/E0=2.25e-08, N=802
  Estimated time remaining to complete simulation: 5 days, 9 hours, 8 minutes, 6 seconds
  Estimated time remaining to next output: 14 minutes, 8 seconds
Output 430/977: t=4520000.0 yr, dE/E0=3.46e-08, N=802
  Estimated time remaining to complete simulation: 5 days, 8 hours, 42 minutes, 29 seconds
  Estimated time remaining to next output: 14 minutes, 7 seconds
Output 431/977: t=4530000.0 yr, dE/E0=3.77e-08, N=802
  Estimated time remaining to complete simulation: 5 days, 8 hours, 17 minutes, 16 seconds
  Estimated time remaining to next output: 14 minutes, 5 seconds
Output 432/977: t=4540000.0 yr, dE/E0=3.49e-08, N=802
  Estimated time remaining to complete simulation: 5 days, 7 hours, 51 minutes, 37 seconds
  Estimated time remaining to next output: 14 minutes, 4 seconds
Output 433/977: t=4550000.0 yr, dE/E0=6.33e-08, N=802
  Estimated time remaining to complete simulation: 5 days, 7 hours, 26 minutes, 19 seconds
  Estimated time remaining to next output: 14 minutes, 3 seconds
Output 434/977: t=4560000.0 yr, dE/E0=6.28e-08, N=802
  Estimated time remaining to complete simulation: 5 days, 7 hours, 31 seconds
  Estimated time remaining to next output: 14 minutes, 2 seconds
Output 435/977: t=4570000.0 yr, dE/E0=8.35e-08, N=802
  Estimated time remaining to complete simulation: 5 days, 6 hours, 35 minutes, 23 seconds
  Estimated time remaining to next output: 14 minutes
Output 436/977: t=4580000.0 yr, dE/E0=7.96e-08, N=802
  Estimated time remaining to complete simulation: 5 days, 6 hours, 10 minutes, 41 seconds
  Estimated time remaining to next output: 13 minutes, 59 seconds
Output 437/977: t=4590000.0 yr, dE/E0=6.13e-08, N=802
  Estimated time remaining to complete simulation: 5 days, 5 hours, 45 minutes, 48 seconds
  Estimated time remaining to next output: 13 minutes, 58 seconds
Output 438/977: t=4600000.0 yr, dE/E0=6.24e-08, N=802
  Estimated time remaining to complete simulation: 5 days, 5 hours, 20 minutes, 36 seconds
  Estimated time remaining to next output: 13 minutes, 57 seconds
Output 439/977: t=4610000.0 yr, dE/E0=5.87e-08, N=802
  Estimated time remaining to complete simulation: 5 days, 4 hours, 56 minutes, 14 seconds
  Estimated time remaining to next output: 13 minutes, 56 seconds
Output 440/977: t=4620000.0 yr, dE/E0=3.97e-08, N=802
  Estimated time remaining to complete simulation: 5 days, 4 hours, 31 minutes, 41 seconds
  Estimated time remaining to next output: 13 minutes, 54 seconds
Output 441/977: t=4630000.0 yr, dE/E0=3.21e-08, N=802
  Estimated time remaining to complete simulation: 5 days, 4 hours, 7 minutes, 5 seconds
  Estimated time remaining to next output: 13 minutes, 53 seconds
Output 442/977: t=4640000.0 yr, dE/E0=3.13e-08, N=802
  Estimated time remaining to complete simulation: 5 days, 3 hours, 42 minutes, 16 seconds
  Estimated time remaining to next output: 13 minutes, 52 seconds
Output 443/977: t=4650000.0 yr, dE/E0=2.73e-08, N=802
  Estimated time remaining to complete simulation: 5 days, 3 hours, 18 minutes, 24 seconds
  Estimated time remaining to next output: 13 minutes, 51 seconds
Output 444/977: t=4660000.0 yr, dE/E0=1.70e-08, N=802
  Estimated time remaining to complete simulation: 5 days, 2 hours, 54 minutes, 19 seconds
  Estimated time remaining to next output: 13 minutes, 50 seconds
Output 445/977: t=4670000.0 yr, dE/E0=4.55e-08, N=802
  Estimated time remaining to complete simulation: 5 days, 2 hours, 29 minutes, 59 seconds
  Estimated time remaining to next output: 13 minutes, 48 seconds
Output 446/977: t=4680000.0 yr, dE/E0=3.02e-08, N=802
  Estimated time remaining to complete simulation: 5 days, 2 hours, 6 minutes, 7 seconds
  Estimated time remaining to next output: 13 minutes, 47 seconds
Output 447/977: t=4690000.0 yr, dE/E0=2.73e-08, N=802
  Estimated time remaining to complete simulation: 5 days, 1 hours, 42 minutes, 15 seconds
  Estimated time remaining to next output: 13 minutes, 46 seconds
Output 448/977: t=4700000.0 yr, dE/E0=3.46e-09, N=802
  Estimated time remaining to complete simulation: 5 days, 1 hours, 18 minutes, 22 seconds
  Estimated time remaining to next output: 13 minutes, 45 seconds
Output 449/977: t=4710000.0 yr, dE/E0=1.67e-08, N=802
  Estimated time remaining to complete simulation: 5 days, 54 minutes, 38 seconds
  Estimated time remaining to next output: 13 minutes, 44 seconds
Output 450/977: t=4720000.0 yr, dE/E0=3.75e-08, N=802
  Estimated time remaining to complete simulation: 5 days, 31 minutes, 12 seconds
  Estimated time remaining to next output: 13 minutes, 43 seconds
Output 451/977: t=4730000.0 yr, dE/E0=2.15e-08, N=802
  Estimated time remaining to complete simulation: 5 days, 7 minutes, 53 seconds
  Estimated time remaining to next output: 13 minutes, 42 seconds
Output 452/977: t=4740000.0 yr, dE/E0=1.50e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 23 hours, 44 minutes, 24 seconds
  Estimated time remaining to next output: 13 minutes, 41 seconds
Output 453/977: t=4750000.0 yr, dE/E0=3.59e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 23 hours, 20 minutes, 43 seconds
  Estimated time remaining to next output: 13 minutes, 39 seconds
Output 454/977: t=4760000.0 yr, dE/E0=4.50e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 22 hours, 57 minutes, 7 seconds
  Estimated time remaining to next output: 13 minutes, 38 seconds
Output 455/977: t=4770000.0 yr, dE/E0=4.35e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 22 hours, 33 minutes, 50 seconds
  Estimated time remaining to next output: 13 minutes, 37 seconds
Output 456/977: t=4780000.0 yr, dE/E0=4.33e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 22 hours, 10 minutes, 22 seconds
  Estimated time remaining to next output: 13 minutes, 36 seconds
Output 457/977: t=4790000.0 yr, dE/E0=3.39e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 21 hours, 47 minutes, 5 seconds
  Estimated time remaining to next output: 13 minutes, 35 seconds
Output 458/977: t=4800000.0 yr, dE/E0=1.83e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 21 hours, 23 minutes, 40 seconds
  Estimated time remaining to next output: 13 minutes, 34 seconds
Output 459/977: t=4810000.0 yr, dE/E0=9.67e-09, N=802
  Estimated time remaining to complete simulation: 4 days, 21 hours, 44 seconds
  Estimated time remaining to next output: 13 minutes, 33 seconds
Output 460/977: t=4820000.0 yr, dE/E0=1.75e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 20 hours, 37 minutes, 38 seconds
  Estimated time remaining to next output: 13 minutes, 32 seconds
Output 461/977: t=4830000.0 yr, dE/E0=3.24e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 20 hours, 14 minutes, 58 seconds
  Estimated time remaining to next output: 13 minutes, 31 seconds
Output 462/977: t=4840000.0 yr, dE/E0=3.54e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 19 hours, 52 minutes, 18 seconds
  Estimated time remaining to next output: 13 minutes, 29 seconds
Output 463/977: t=4850000.0 yr, dE/E0=3.66e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 19 hours, 29 minutes, 31 seconds
  Estimated time remaining to next output: 13 minutes, 28 seconds
Output 464/977: t=4860000.0 yr, dE/E0=5.06e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 19 hours, 7 minutes, 15 seconds
  Estimated time remaining to next output: 13 minutes, 27 seconds
Output 465/977: t=4870000.0 yr, dE/E0=3.51e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 18 hours, 44 minutes, 29 seconds
  Estimated time remaining to next output: 13 minutes, 26 seconds
Output 466/977: t=4880000.0 yr, dE/E0=2.24e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 18 hours, 21 minutes, 49 seconds
  Estimated time remaining to next output: 13 minutes, 25 seconds
Output 467/977: t=4890000.0 yr, dE/E0=4.60e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 17 hours, 59 minutes, 13 seconds
  Estimated time remaining to next output: 13 minutes, 24 seconds
Output 468/977: t=4900000.0 yr, dE/E0=3.88e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 17 hours, 37 minutes, 4 seconds
  Estimated time remaining to next output: 13 minutes, 23 seconds
Output 469/977: t=4910000.0 yr, dE/E0=2.88e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 17 hours, 14 minutes, 54 seconds
  Estimated time remaining to next output: 13 minutes, 22 seconds
Output 470/977: t=4920000.0 yr, dE/E0=4.07e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 16 hours, 52 minutes, 35 seconds
  Estimated time remaining to next output: 13 minutes, 21 seconds
Output 471/977: t=4930000.0 yr, dE/E0=4.81e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 16 hours, 30 minutes, 31 seconds
  Estimated time remaining to next output: 13 minutes, 20 seconds
Output 472/977: t=4940000.0 yr, dE/E0=3.70e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 16 hours, 8 minutes, 5 seconds
  Estimated time remaining to next output: 13 minutes, 19 seconds
Output 473/977: t=4950000.0 yr, dE/E0=3.78e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 15 hours, 46 minutes, 2 seconds
  Estimated time remaining to next output: 13 minutes, 18 seconds
Output 474/977: t=4960000.0 yr, dE/E0=5.31e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 15 hours, 23 minutes, 53 seconds
  Estimated time remaining to next output: 13 minutes, 17 seconds
Output 475/977: t=4970000.0 yr, dE/E0=2.90e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 15 hours, 1 minutes, 53 seconds
  Estimated time remaining to next output: 13 minutes, 16 seconds
Output 476/977: t=4980000.0 yr, dE/E0=5.13e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 14 hours, 39 minutes, 57 seconds
  Estimated time remaining to next output: 13 minutes, 15 seconds
Output 477/977: t=4990000.0 yr, dE/E0=5.01e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 14 hours, 17 minutes, 56 seconds
  Estimated time remaining to next output: 13 minutes, 14 seconds
Output 478/977: t=5000000.0 yr, dE/E0=5.10e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 13 hours, 56 minutes, 40 seconds
  Estimated time remaining to next output: 13 minutes, 13 seconds
Output 479/977: t=5010000.0 yr, dE/E0=2.70e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 13 hours, 35 minutes, 3 seconds
  Estimated time remaining to next output: 13 minutes, 12 seconds
Output 480/977: t=5020000.0 yr, dE/E0=4.50e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 13 hours, 13 minutes, 41 seconds
  Estimated time remaining to next output: 13 minutes, 11 seconds
Output 481/977: t=5030000.0 yr, dE/E0=3.23e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 12 hours, 52 minutes, 14 seconds
  Estimated time remaining to next output: 13 minutes, 10 seconds
Output 482/977: t=5040000.0 yr, dE/E0=4.68e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 12 hours, 30 minutes, 43 seconds
  Estimated time remaining to next output: 13 minutes, 9 seconds
Output 483/977: t=5050000.0 yr, dE/E0=2.27e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 12 hours, 9 minutes, 15 seconds
  Estimated time remaining to next output: 13 minutes, 8 seconds
Output 484/977: t=5060000.0 yr, dE/E0=4.52e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 11 hours, 47 minutes, 47 seconds
  Estimated time remaining to next output: 13 minutes, 7 seconds
Output 485/977: t=5070000.0 yr, dE/E0=5.89e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 11 hours, 27 minutes, 10 seconds
  Estimated time remaining to next output: 13 minutes, 6 seconds
Output 486/977: t=5080000.0 yr, dE/E0=6.48e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 11 hours, 6 minutes, 19 seconds
  Estimated time remaining to next output: 13 minutes, 5 seconds
Output 487/977: t=5090000.0 yr, dE/E0=5.79e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 10 hours, 45 minutes, 29 seconds
  Estimated time remaining to next output: 13 minutes, 4 seconds
Output 488/977: t=5100000.0 yr, dE/E0=6.72e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 10 hours, 24 minutes, 24 seconds
  Estimated time remaining to next output: 13 minutes, 3 seconds
Output 489/977: t=5110000.0 yr, dE/E0=7.67e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 10 hours, 3 minutes, 56 seconds
  Estimated time remaining to next output: 13 minutes, 2 seconds
Output 490/977: t=5120000.0 yr, dE/E0=7.68e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 9 hours, 42 minutes, 52 seconds
  Estimated time remaining to next output: 13 minutes, 1 seconds
Output 491/977: t=5130000.0 yr, dE/E0=5.95e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 9 hours, 21 minutes, 53 seconds
  Estimated time remaining to next output: 13 minutes
Output 492/977: t=5140000.0 yr, dE/E0=6.31e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 9 hours, 1 minutes, 20 seconds
  Estimated time remaining to next output: 12 minutes, 59 seconds
Output 493/977: t=5150000.0 yr, dE/E0=7.55e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 8 hours, 40 minutes, 35 seconds
  Estimated time remaining to next output: 12 minutes, 58 seconds
Output 494/977: t=5160000.0 yr, dE/E0=4.85e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 8 hours, 20 minutes, 3 seconds
  Estimated time remaining to next output: 12 minutes, 57 seconds
Output 495/977: t=5170000.0 yr, dE/E0=6.10e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 7 hours, 59 minutes, 33 seconds
  Estimated time remaining to next output: 12 minutes, 56 seconds
Output 496/977: t=5180000.0 yr, dE/E0=7.07e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 7 hours, 39 minutes, 5 seconds
  Estimated time remaining to next output: 12 minutes, 55 seconds
Output 497/977: t=5190000.0 yr, dE/E0=7.57e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 7 hours, 18 minutes, 20 seconds
  Estimated time remaining to next output: 12 minutes, 54 seconds
Output 498/977: t=5200000.0 yr, dE/E0=7.03e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 6 hours, 58 minutes, 3 seconds
  Estimated time remaining to next output: 12 minutes, 53 seconds
Output 499/977: t=5210000.0 yr, dE/E0=8.51e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 6 hours, 37 minutes, 43 seconds
  Estimated time remaining to next output: 12 minutes, 52 seconds
Output 500/977: t=5220000.0 yr, dE/E0=1.05e-07, N=802
  Estimated time remaining to complete simulation: 4 days, 6 hours, 17 minutes, 54 seconds
  Estimated time remaining to next output: 12 minutes, 52 seconds
Output 501/977: t=5230000.0 yr, dE/E0=7.39e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 5 hours, 57 minutes, 32 seconds
  Estimated time remaining to next output: 12 minutes, 51 seconds
Output 502/977: t=5240000.0 yr, dE/E0=9.66e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 5 hours, 37 minutes, 12 seconds
  Estimated time remaining to next output: 12 minutes, 50 seconds
Output 503/977: t=5250000.0 yr, dE/E0=7.90e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 5 hours, 17 minutes, 15 seconds
  Estimated time remaining to next output: 12 minutes, 49 seconds
Output 504/977: t=5260000.0 yr, dE/E0=8.03e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 4 hours, 57 minutes, 9 seconds
  Estimated time remaining to next output: 12 minutes, 48 seconds
Output 505/977: t=5270000.0 yr, dE/E0=7.22e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 4 hours, 37 minutes, 15 seconds
  Estimated time remaining to next output: 12 minutes, 47 seconds
Output 506/977: t=5280000.0 yr, dE/E0=5.77e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 4 hours, 17 minutes, 41 seconds
  Estimated time remaining to next output: 12 minutes, 46 seconds
Output 507/977: t=5290000.0 yr, dE/E0=6.87e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 3 hours, 58 minutes, 10 seconds
  Estimated time remaining to next output: 12 minutes, 45 seconds
Output 508/977: t=5300000.0 yr, dE/E0=6.00e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 3 hours, 38 minutes, 30 seconds
  Estimated time remaining to next output: 12 minutes, 44 seconds
Output 509/977: t=5310000.0 yr, dE/E0=6.99e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 3 hours, 18 minutes, 35 seconds
  Estimated time remaining to next output: 12 minutes, 43 seconds
Output 510/977: t=5320000.0 yr, dE/E0=6.83e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 2 hours, 58 minutes, 51 seconds
  Estimated time remaining to next output: 12 minutes, 43 seconds
Output 511/977: t=5330000.0 yr, dE/E0=5.73e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 2 hours, 39 minutes, 13 seconds
  Estimated time remaining to next output: 12 minutes, 42 seconds
Output 512/977: t=5340000.0 yr, dE/E0=5.10e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 2 hours, 19 minutes, 33 seconds
  Estimated time remaining to next output: 12 minutes, 41 seconds
Output 513/977: t=5350000.0 yr, dE/E0=5.66e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 2 hours, 3 seconds
  Estimated time remaining to next output: 12 minutes, 40 seconds
Output 514/977: t=5360000.0 yr, dE/E0=3.80e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 1 hours, 40 minutes, 40 seconds
  Estimated time remaining to next output: 12 minutes, 39 seconds
Output 515/977: t=5370000.0 yr, dE/E0=6.54e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 1 hours, 21 minutes, 15 seconds
  Estimated time remaining to next output: 12 minutes, 38 seconds
Output 516/977: t=5380000.0 yr, dE/E0=6.51e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 1 hours, 1 minutes, 38 seconds
  Estimated time remaining to next output: 12 minutes, 37 seconds
Output 517/977: t=5390000.0 yr, dE/E0=7.67e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 42 minutes, 17 seconds
  Estimated time remaining to next output: 12 minutes, 36 seconds
Output 518/977: t=5400000.0 yr, dE/E0=7.97e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 22 minutes, 53 seconds
  Estimated time remaining to next output: 12 minutes, 35 seconds
Output 519/977: t=5410000.0 yr, dE/E0=7.27e-08, N=802
  Estimated time remaining to complete simulation: 4 days, 3 minutes, 36 seconds
  Estimated time remaining to next output: 12 minutes, 35 seconds
Output 520/977: t=5420000.0 yr, dE/E0=6.37e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 23 hours, 44 minutes, 34 seconds
  Estimated time remaining to next output: 12 minutes, 34 seconds
Output 521/977: t=5430000.0 yr, dE/E0=6.05e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 23 hours, 25 minutes, 20 seconds
  Estimated time remaining to next output: 12 minutes, 33 seconds
Output 522/977: t=5440000.0 yr, dE/E0=7.41e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 23 hours, 6 minutes, 4 seconds
  Estimated time remaining to next output: 12 minutes, 32 seconds
Output 523/977: t=5450000.0 yr, dE/E0=7.56e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 22 hours, 46 minutes, 55 seconds
  Estimated time remaining to next output: 12 minutes, 31 seconds
Output 524/977: t=5460000.0 yr, dE/E0=6.68e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 22 hours, 28 minutes, 3 seconds
  Estimated time remaining to next output: 12 minutes, 30 seconds
Output 525/977: t=5470000.0 yr, dE/E0=6.89e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 22 hours, 8 minutes, 55 seconds
  Estimated time remaining to next output: 12 minutes, 29 seconds
Output 526/977: t=5480000.0 yr, dE/E0=7.72e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 21 hours, 50 minutes, 28 seconds
  Estimated time remaining to next output: 12 minutes, 29 seconds
Output 527/977: t=5490000.0 yr, dE/E0=6.68e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 21 hours, 31 minutes, 46 seconds
  Estimated time remaining to next output: 12 minutes, 28 seconds
Output 528/977: t=5500000.0 yr, dE/E0=6.91e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 21 hours, 12 minutes, 53 seconds
  Estimated time remaining to next output: 12 minutes, 27 seconds
Output 529/977: t=5510000.0 yr, dE/E0=6.39e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 20 hours, 53 minutes, 52 seconds
  Estimated time remaining to next output: 12 minutes, 26 seconds
Output 530/977: t=5520000.0 yr, dE/E0=8.45e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 20 hours, 35 minutes, 9 seconds
  Estimated time remaining to next output: 12 minutes, 25 seconds
Output 531/977: t=5530000.0 yr, dE/E0=6.67e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 20 hours, 16 minutes, 25 seconds
  Estimated time remaining to next output: 12 minutes, 24 seconds
Output 532/977: t=5540000.0 yr, dE/E0=5.65e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 19 hours, 57 minutes, 51 seconds
  Estimated time remaining to next output: 12 minutes, 23 seconds
Output 533/977: t=5550000.0 yr, dE/E0=6.85e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 19 hours, 39 minutes, 29 seconds
  Estimated time remaining to next output: 12 minutes, 23 seconds
Output 534/977: t=5560000.0 yr, dE/E0=8.32e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 19 hours, 20 minutes, 51 seconds
  Estimated time remaining to next output: 12 minutes, 22 seconds
Output 535/977: t=5570000.0 yr, dE/E0=7.74e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 19 hours, 2 minutes, 27 seconds
  Estimated time remaining to next output: 12 minutes, 21 seconds
Output 536/977: t=5580000.0 yr, dE/E0=7.34e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 18 hours, 44 minutes, 13 seconds
  Estimated time remaining to next output: 12 minutes, 20 seconds
Output 537/977: t=5590000.0 yr, dE/E0=5.99e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 18 hours, 25 minutes, 48 seconds
  Estimated time remaining to next output: 12 minutes, 19 seconds
Output 538/977: t=5600000.0 yr, dE/E0=6.63e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 18 hours, 7 minutes, 18 seconds
  Estimated time remaining to next output: 12 minutes, 19 seconds
Output 539/977: t=5610000.0 yr, dE/E0=5.04e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 17 hours, 48 minutes, 58 seconds
  Estimated time remaining to next output: 12 minutes, 18 seconds
Output 540/977: t=5620000.0 yr, dE/E0=7.07e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 17 hours, 30 minutes, 40 seconds
  Estimated time remaining to next output: 12 minutes, 17 seconds
Output 541/977: t=5630000.0 yr, dE/E0=6.70e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 17 hours, 12 minutes, 37 seconds
  Estimated time remaining to next output: 12 minutes, 16 seconds
Output 542/977: t=5640000.0 yr, dE/E0=3.99e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 16 hours, 54 minutes, 52 seconds
  Estimated time remaining to next output: 12 minutes, 15 seconds
Output 543/977: t=5650000.0 yr, dE/E0=7.12e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 16 hours, 36 minutes, 44 seconds
  Estimated time remaining to next output: 12 minutes, 15 seconds
Output 544/977: t=5660000.0 yr, dE/E0=6.74e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 16 hours, 18 minutes, 44 seconds
  Estimated time remaining to next output: 12 minutes, 14 seconds
Output 545/977: t=5670000.0 yr, dE/E0=8.71e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 16 hours, 41 seconds
  Estimated time remaining to next output: 12 minutes, 13 seconds
Output 546/977: t=5680000.0 yr, dE/E0=8.48e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 15 hours, 42 minutes, 40 seconds
  Estimated time remaining to next output: 12 minutes, 12 seconds
Output 547/977: t=5690000.0 yr, dE/E0=7.66e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 15 hours, 24 minutes, 45 seconds
  Estimated time remaining to next output: 12 minutes, 11 seconds
Output 548/977: t=5700000.0 yr, dE/E0=6.49e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 15 hours, 6 minutes, 59 seconds
  Estimated time remaining to next output: 12 minutes, 11 seconds
Output 549/977: t=5710000.0 yr, dE/E0=4.88e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 14 hours, 49 minutes, 18 seconds
  Estimated time remaining to next output: 12 minutes, 10 seconds
Output 550/977: t=5720000.0 yr, dE/E0=6.57e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 14 hours, 31 minutes, 38 seconds
  Estimated time remaining to next output: 12 minutes, 9 seconds
Output 551/977: t=5730000.0 yr, dE/E0=5.69e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 14 hours, 13 minutes, 45 seconds
  Estimated time remaining to next output: 12 minutes, 8 seconds
Output 552/977: t=5740000.0 yr, dE/E0=7.31e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 13 hours, 56 minutes, 25 seconds
  Estimated time remaining to next output: 12 minutes, 7 seconds
Output 553/977: t=5750000.0 yr, dE/E0=5.43e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 13 hours, 38 minutes, 52 seconds
  Estimated time remaining to next output: 12 minutes, 7 seconds
Output 554/977: t=5760000.0 yr, dE/E0=5.51e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 13 hours, 21 minutes, 29 seconds
  Estimated time remaining to next output: 12 minutes, 6 seconds
Output 555/977: t=5770000.0 yr, dE/E0=8.05e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 13 hours, 4 minutes, 2 seconds
  Estimated time remaining to next output: 12 minutes, 5 seconds
Output 556/977: t=5780000.0 yr, dE/E0=5.41e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 12 hours, 46 minutes, 35 seconds
  Estimated time remaining to next output: 12 minutes, 4 seconds
Output 557/977: t=5790000.0 yr, dE/E0=7.88e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 12 hours, 29 minutes, 11 seconds
  Estimated time remaining to next output: 12 minutes, 4 seconds
Output 558/977: t=5800000.0 yr, dE/E0=9.62e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 12 hours, 11 minutes, 55 seconds
  Estimated time remaining to next output: 12 minutes, 3 seconds
Output 559/977: t=5810000.0 yr, dE/E0=9.14e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 11 hours, 54 minutes, 48 seconds
  Estimated time remaining to next output: 12 minutes, 2 seconds
Output 560/977: t=5820000.0 yr, dE/E0=8.83e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 11 hours, 37 minutes, 24 seconds
  Estimated time remaining to next output: 12 minutes, 1 seconds
Output 561/977: t=5830000.0 yr, dE/E0=5.30e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 11 hours, 20 minutes, 33 seconds
  Estimated time remaining to next output: 12 minutes, 1 seconds
Output 562/977: t=5840000.0 yr, dE/E0=7.26e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 11 hours, 3 minutes, 41 seconds
  Estimated time remaining to next output: 12 minutes
Output 563/977: t=5850000.0 yr, dE/E0=6.68e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 10 hours, 46 minutes, 35 seconds
  Estimated time remaining to next output: 11 minutes, 59 seconds
Output 564/977: t=5860000.0 yr, dE/E0=8.17e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 10 hours, 29 minutes, 30 seconds
  Estimated time remaining to next output: 11 minutes, 59 seconds
Output 565/977: t=5870000.0 yr, dE/E0=8.56e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 10 hours, 12 minutes, 40 seconds
  Estimated time remaining to next output: 11 minutes, 58 seconds
Output 566/977: t=5880000.0 yr, dE/E0=9.89e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 9 hours, 55 minutes, 35 seconds
  Estimated time remaining to next output: 11 minutes, 57 seconds
Output 567/977: t=5890000.0 yr, dE/E0=1.01e-07, N=802
  Estimated time remaining to complete simulation: 3 days, 9 hours, 38 minutes, 36 seconds
  Estimated time remaining to next output: 11 minutes, 56 seconds
Output 568/977: t=5900000.0 yr, dE/E0=1.14e-07, N=802
  Estimated time remaining to complete simulation: 3 days, 9 hours, 21 minutes, 58 seconds
  Estimated time remaining to next output: 11 minutes, 56 seconds
Output 569/977: t=5910000.0 yr, dE/E0=1.23e-07, N=802
  Estimated time remaining to complete simulation: 3 days, 9 hours, 4 minutes, 58 seconds
  Estimated time remaining to next output: 11 minutes, 55 seconds
Output 570/977: t=5920000.0 yr, dE/E0=1.08e-07, N=802
  Estimated time remaining to complete simulation: 3 days, 8 hours, 48 minutes, 21 seconds
  Estimated time remaining to next output: 11 minutes, 54 seconds
Output 571/977: t=5930000.0 yr, dE/E0=1.25e-07, N=802
  Estimated time remaining to complete simulation: 3 days, 8 hours, 31 minutes, 34 seconds
  Estimated time remaining to next output: 11 minutes, 54 seconds
Output 572/977: t=5940000.0 yr, dE/E0=1.20e-07, N=802
  Estimated time remaining to complete simulation: 3 days, 8 hours, 14 minutes, 46 seconds
  Estimated time remaining to next output: 11 minutes, 53 seconds
Output 573/977: t=5950000.0 yr, dE/E0=1.36e-07, N=802
  Estimated time remaining to complete simulation: 3 days, 7 hours, 58 minutes, 1 seconds
  Estimated time remaining to next output: 11 minutes, 52 seconds
Output 574/977: t=5960000.0 yr, dE/E0=1.30e-07, N=802
  Estimated time remaining to complete simulation: 3 days, 7 hours, 41 minutes, 35 seconds
  Estimated time remaining to next output: 11 minutes, 51 seconds
Output 575/977: t=5970000.0 yr, dE/E0=1.03e-07, N=802
  Estimated time remaining to complete simulation: 3 days, 7 hours, 25 minutes, 4 seconds
  Estimated time remaining to next output: 11 minutes, 51 seconds
Output 576/977: t=5980000.0 yr, dE/E0=1.16e-07, N=802
  Estimated time remaining to complete simulation: 3 days, 7 hours, 8 minutes, 37 seconds
  Estimated time remaining to next output: 11 minutes, 50 seconds
Output 577/977: t=5990000.0 yr, dE/E0=1.02e-07, N=802
  Estimated time remaining to complete simulation: 3 days, 6 hours, 52 minutes, 5 seconds
  Estimated time remaining to next output: 11 minutes, 49 seconds
Output 578/977: t=6000000.0 yr, dE/E0=1.02e-07, N=802
  Estimated time remaining to complete simulation: 3 days, 6 hours, 35 minutes, 50 seconds
  Estimated time remaining to next output: 11 minutes, 49 seconds
Output 579/977: t=6010000.0 yr, dE/E0=1.11e-07, N=802
  Estimated time remaining to complete simulation: 3 days, 6 hours, 19 minutes, 13 seconds
  Estimated time remaining to next output: 11 minutes, 48 seconds
Output 580/977: t=6020000.0 yr, dE/E0=9.92e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 6 hours, 2 minutes, 57 seconds
  Estimated time remaining to next output: 11 minutes, 47 seconds
Output 581/977: t=6030000.0 yr, dE/E0=9.70e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 5 hours, 46 minutes, 36 seconds
  Estimated time remaining to next output: 11 minutes, 47 seconds
Output 582/977: t=6040000.0 yr, dE/E0=7.96e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 5 hours, 30 minutes, 5 seconds
  Estimated time remaining to next output: 11 minutes, 46 seconds
Output 583/977: t=6050000.0 yr, dE/E0=1.03e-07, N=802
  Estimated time remaining to complete simulation: 3 days, 5 hours, 13 minutes, 37 seconds
  Estimated time remaining to next output: 11 minutes, 45 seconds
Output 584/977: t=6060000.0 yr, dE/E0=1.11e-07, N=802
  Estimated time remaining to complete simulation: 3 days, 4 hours, 57 minutes, 20 seconds
  Estimated time remaining to next output: 11 minutes, 44 seconds
Output 585/977: t=6070000.0 yr, dE/E0=1.10e-07, N=802
  Estimated time remaining to complete simulation: 3 days, 4 hours, 41 minutes, 12 seconds
  Estimated time remaining to next output: 11 minutes, 44 seconds
Output 586/977: t=6080000.0 yr, dE/E0=1.10e-07, N=802
  Estimated time remaining to complete simulation: 3 days, 4 hours, 24 minutes, 46 seconds
  Estimated time remaining to next output: 11 minutes, 43 seconds
Output 587/977: t=6090000.0 yr, dE/E0=1.23e-07, N=802
  Estimated time remaining to complete simulation: 3 days, 4 hours, 8 minutes, 33 seconds
  Estimated time remaining to next output: 11 minutes, 42 seconds
Output 588/977: t=6100000.0 yr, dE/E0=1.27e-07, N=802
  Estimated time remaining to complete simulation: 3 days, 3 hours, 52 minutes, 41 seconds
  Estimated time remaining to next output: 11 minutes, 42 seconds
Output 589/977: t=6110000.0 yr, dE/E0=1.02e-07, N=802
  Estimated time remaining to complete simulation: 3 days, 3 hours, 36 minutes, 21 seconds
  Estimated time remaining to next output: 11 minutes, 41 seconds
Output 590/977: t=6120000.0 yr, dE/E0=1.27e-07, N=802
  Estimated time remaining to complete simulation: 3 days, 3 hours, 20 minutes, 26 seconds
  Estimated time remaining to next output: 11 minutes, 40 seconds
Output 591/977: t=6130000.0 yr, dE/E0=1.07e-07, N=802
  Estimated time remaining to complete simulation: 3 days, 3 hours, 4 minutes, 18 seconds
  Estimated time remaining to next output: 11 minutes, 40 seconds
Output 592/977: t=6140000.0 yr, dE/E0=1.21e-07, N=802
  Estimated time remaining to complete simulation: 3 days, 2 hours, 48 minutes, 15 seconds
  Estimated time remaining to next output: 11 minutes, 39 seconds
Output 593/977: t=6150000.0 yr, dE/E0=1.16e-07, N=802
  Estimated time remaining to complete simulation: 3 days, 2 hours, 32 minutes, 21 seconds
  Estimated time remaining to next output: 11 minutes, 38 seconds
Output 594/977: t=6160000.0 yr, dE/E0=1.10e-07, N=802
  Estimated time remaining to complete simulation: 3 days, 2 hours, 16 minutes, 24 seconds
  Estimated time remaining to next output: 11 minutes, 38 seconds
Output 595/977: t=6170000.0 yr, dE/E0=1.14e-07, N=802
  Estimated time remaining to complete simulation: 3 days, 2 hours, 47 seconds
  Estimated time remaining to next output: 11 minutes, 37 seconds
Output 596/977: t=6180000.0 yr, dE/E0=1.04e-07, N=802
  Estimated time remaining to complete simulation: 3 days, 1 hours, 44 minutes, 55 seconds
  Estimated time remaining to next output: 11 minutes, 36 seconds
Output 597/977: t=6190000.0 yr, dE/E0=1.00e-07, N=802
  Estimated time remaining to complete simulation: 3 days, 1 hours, 29 minutes, 3 seconds
  Estimated time remaining to next output: 11 minutes, 36 seconds
Output 598/977: t=6200000.0 yr, dE/E0=8.24e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 1 hours, 13 minutes, 7 seconds
  Estimated time remaining to next output: 11 minutes, 35 seconds
Output 599/977: t=6210000.0 yr, dE/E0=1.02e-07, N=802
  Estimated time remaining to complete simulation: 3 days, 57 minutes, 19 seconds
  Estimated time remaining to next output: 11 minutes, 34 seconds
Output 600/977: t=6220000.0 yr, dE/E0=9.07e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 41 minutes, 36 seconds
  Estimated time remaining to next output: 11 minutes, 34 seconds
Output 601/977: t=6230000.0 yr, dE/E0=9.10e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 25 minutes, 59 seconds
  Estimated time remaining to next output: 11 minutes, 33 seconds
Output 602/977: t=6240000.0 yr, dE/E0=7.70e-08, N=802
  Estimated time remaining to complete simulation: 3 days, 10 minutes, 22 seconds
  Estimated time remaining to next output: 11 minutes, 32 seconds
Output 603/977: t=6250000.0 yr, dE/E0=7.71e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 23 hours, 54 minutes, 44 seconds
  Estimated time remaining to next output: 11 minutes, 32 seconds
Output 604/977: t=6260000.0 yr, dE/E0=7.93e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 23 hours, 39 minutes, 13 seconds
  Estimated time remaining to next output: 11 minutes, 31 seconds
Output 605/977: t=6270000.0 yr, dE/E0=8.03e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 23 hours, 23 minutes, 49 seconds
  Estimated time remaining to next output: 11 minutes, 30 seconds
Output 606/977: t=6280000.0 yr, dE/E0=7.33e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 23 hours, 8 minutes, 10 seconds
  Estimated time remaining to next output: 11 minutes, 30 seconds
Output 607/977: t=6290000.0 yr, dE/E0=8.47e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 22 hours, 52 minutes, 46 seconds
  Estimated time remaining to next output: 11 minutes, 29 seconds
Output 608/977: t=6300000.0 yr, dE/E0=7.60e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 22 hours, 37 minutes, 8 seconds
  Estimated time remaining to next output: 11 minutes, 28 seconds
Output 609/977: t=6310000.0 yr, dE/E0=8.84e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 22 hours, 21 minutes, 39 seconds
  Estimated time remaining to next output: 11 minutes, 28 seconds
Output 610/977: t=6320000.0 yr, dE/E0=1.03e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 22 hours, 6 minutes, 21 seconds
  Estimated time remaining to next output: 11 minutes, 27 seconds
Output 611/977: t=6330000.0 yr, dE/E0=1.03e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 21 hours, 51 minutes, 8 seconds
  Estimated time remaining to next output: 11 minutes, 27 seconds
Output 612/977: t=6340000.0 yr, dE/E0=1.13e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 21 hours, 35 minutes, 51 seconds
  Estimated time remaining to next output: 11 minutes, 26 seconds
Output 613/977: t=6350000.0 yr, dE/E0=1.06e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 21 hours, 20 minutes, 38 seconds
  Estimated time remaining to next output: 11 minutes, 25 seconds
Output 614/977: t=6360000.0 yr, dE/E0=1.19e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 21 hours, 5 minutes, 31 seconds
  Estimated time remaining to next output: 11 minutes, 25 seconds
Output 615/977: t=6370000.0 yr, dE/E0=1.08e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 20 hours, 50 minutes, 16 seconds
  Estimated time remaining to next output: 11 minutes, 24 seconds
Output 616/977: t=6380000.0 yr, dE/E0=8.95e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 20 hours, 35 minutes, 6 seconds
  Estimated time remaining to next output: 11 minutes, 23 seconds
Output 617/977: t=6390000.0 yr, dE/E0=1.13e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 20 hours, 20 minutes, 1 seconds
  Estimated time remaining to next output: 11 minutes, 23 seconds
Output 618/977: t=6400000.0 yr, dE/E0=1.15e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 20 hours, 4 minutes, 57 seconds
  Estimated time remaining to next output: 11 minutes, 22 seconds
Output 619/977: t=6410000.0 yr, dE/E0=1.03e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 19 hours, 49 minutes, 52 seconds
  Estimated time remaining to next output: 11 minutes, 22 seconds
Output 620/977: t=6420000.0 yr, dE/E0=1.36e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 19 hours, 34 minutes, 53 seconds
  Estimated time remaining to next output: 11 minutes, 21 seconds
Output 621/977: t=6430000.0 yr, dE/E0=1.12e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 19 hours, 19 minutes, 54 seconds
  Estimated time remaining to next output: 11 minutes, 20 seconds
Output 622/977: t=6440000.0 yr, dE/E0=1.16e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 19 hours, 5 minutes
  Estimated time remaining to next output: 11 minutes, 20 seconds
Output 623/977: t=6450000.0 yr, dE/E0=1.04e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 18 hours, 49 minutes, 59 seconds
  Estimated time remaining to next output: 11 minutes, 19 seconds
Output 624/977: t=6460000.0 yr, dE/E0=9.81e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 18 hours, 34 minutes, 57 seconds
  Estimated time remaining to next output: 11 minutes, 19 seconds
Output 625/977: t=6470000.0 yr, dE/E0=1.17e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 18 hours, 20 minutes, 1 seconds
  Estimated time remaining to next output: 11 minutes, 18 seconds
Output 626/977: t=6480000.0 yr, dE/E0=1.23e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 18 hours, 5 minutes, 12 seconds
  Estimated time remaining to next output: 11 minutes, 17 seconds
Output 627/977: t=6490000.0 yr, dE/E0=1.22e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 17 hours, 50 minutes, 21 seconds
  Estimated time remaining to next output: 11 minutes, 17 seconds
Output 628/977: t=6500000.0 yr, dE/E0=1.55e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 17 hours, 35 minutes, 27 seconds
  Estimated time remaining to next output: 11 minutes, 16 seconds
Output 629/977: t=6510000.0 yr, dE/E0=1.50e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 17 hours, 20 minutes, 39 seconds
  Estimated time remaining to next output: 11 minutes, 15 seconds
Output 630/977: t=6520000.0 yr, dE/E0=1.46e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 17 hours, 6 minutes, 5 seconds
  Estimated time remaining to next output: 11 minutes, 15 seconds
Output 631/977: t=6530000.0 yr, dE/E0=1.62e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 16 hours, 51 minutes, 29 seconds
  Estimated time remaining to next output: 11 minutes, 14 seconds
Output 632/977: t=6540000.0 yr, dE/E0=1.85e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 16 hours, 36 minutes, 48 seconds
  Estimated time remaining to next output: 11 minutes, 14 seconds
Output 633/977: t=6550000.0 yr, dE/E0=1.75e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 16 hours, 21 minutes, 59 seconds
  Estimated time remaining to next output: 11 minutes, 13 seconds
Output 634/977: t=6560000.0 yr, dE/E0=1.78e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 16 hours, 7 minutes, 28 seconds
  Estimated time remaining to next output: 11 minutes, 13 seconds
Output 635/977: t=6570000.0 yr, dE/E0=1.79e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 15 hours, 52 minutes, 59 seconds
  Estimated time remaining to next output: 11 minutes, 12 seconds
Output 636/977: t=6580000.0 yr, dE/E0=1.88e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 15 hours, 38 minutes, 27 seconds
  Estimated time remaining to next output: 11 minutes, 11 seconds
Output 637/977: t=6590000.0 yr, dE/E0=1.87e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 15 hours, 24 minutes
  Estimated time remaining to next output: 11 minutes, 11 seconds
Output 638/977: t=6600000.0 yr, dE/E0=1.81e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 15 hours, 9 minutes, 26 seconds
  Estimated time remaining to next output: 11 minutes, 10 seconds
Output 639/977: t=6610000.0 yr, dE/E0=1.88e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 14 hours, 54 minutes, 54 seconds
  Estimated time remaining to next output: 11 minutes, 10 seconds
Output 640/977: t=6620000.0 yr, dE/E0=1.79e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 14 hours, 40 minutes, 26 seconds
  Estimated time remaining to next output: 11 minutes, 9 seconds
Output 641/977: t=6630000.0 yr, dE/E0=1.61e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 14 hours, 25 minutes, 54 seconds
  Estimated time remaining to next output: 11 minutes, 8 seconds
Output 642/977: t=6640000.0 yr, dE/E0=1.47e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 14 hours, 11 minutes, 35 seconds
  Estimated time remaining to next output: 11 minutes, 8 seconds
Output 643/977: t=6650000.0 yr, dE/E0=1.51e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 13 hours, 57 minutes, 16 seconds
  Estimated time remaining to next output: 11 minutes, 7 seconds
Output 644/977: t=6660000.0 yr, dE/E0=1.72e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 13 hours, 42 minutes, 58 seconds
  Estimated time remaining to next output: 11 minutes, 7 seconds
Output 645/977: t=6670000.0 yr, dE/E0=1.58e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 13 hours, 28 minutes, 45 seconds
  Estimated time remaining to next output: 11 minutes, 6 seconds
Output 646/977: t=6680000.0 yr, dE/E0=1.69e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 13 hours, 14 minutes, 33 seconds
  Estimated time remaining to next output: 11 minutes, 6 seconds
Output 647/977: t=6690000.0 yr, dE/E0=1.81e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 13 hours, 16 seconds
  Estimated time remaining to next output: 11 minutes, 5 seconds
Output 648/977: t=6700000.0 yr, dE/E0=1.87e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 12 hours, 46 minutes, 7 seconds
  Estimated time remaining to next output: 11 minutes, 4 seconds
Output 649/977: t=6710000.0 yr, dE/E0=1.93e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 12 hours, 31 minutes, 58 seconds
  Estimated time remaining to next output: 11 minutes, 4 seconds
Output 650/977: t=6720000.0 yr, dE/E0=1.74e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 12 hours, 17 minutes, 46 seconds
  Estimated time remaining to next output: 11 minutes, 3 seconds
Output 651/977: t=6730000.0 yr, dE/E0=1.73e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 12 hours, 3 minutes, 32 seconds
  Estimated time remaining to next output: 11 minutes, 3 seconds
Output 652/977: t=6740000.0 yr, dE/E0=1.90e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 11 hours, 49 minutes, 19 seconds
  Estimated time remaining to next output: 11 minutes, 2 seconds
Output 653/977: t=6750000.0 yr, dE/E0=1.73e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 11 hours, 35 minutes, 15 seconds
  Estimated time remaining to next output: 11 minutes, 2 seconds
Output 654/977: t=6760000.0 yr, dE/E0=1.86e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 11 hours, 21 minutes, 19 seconds
  Estimated time remaining to next output: 11 minutes, 1 seconds
Output 655/977: t=6770000.0 yr, dE/E0=1.53e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 11 hours, 7 minutes, 14 seconds
  Estimated time remaining to next output: 11 minutes
Output 656/977: t=6780000.0 yr, dE/E0=1.50e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 10 hours, 53 minutes, 13 seconds
  Estimated time remaining to next output: 11 minutes
Output 657/977: t=6790000.0 yr, dE/E0=1.58e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 10 hours, 39 minutes, 20 seconds
  Estimated time remaining to next output: 10 minutes, 59 seconds
Output 658/977: t=6800000.0 yr, dE/E0=1.57e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 10 hours, 25 minutes, 25 seconds
  Estimated time remaining to next output: 10 minutes, 59 seconds
Output 659/977: t=6810000.0 yr, dE/E0=1.58e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 10 hours, 11 minutes, 35 seconds
  Estimated time remaining to next output: 10 minutes, 58 seconds
Output 660/977: t=6820000.0 yr, dE/E0=1.62e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 9 hours, 57 minutes, 52 seconds
  Estimated time remaining to next output: 10 minutes, 58 seconds
Output 661/977: t=6830000.0 yr, dE/E0=1.56e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 9 hours, 43 minutes, 58 seconds
  Estimated time remaining to next output: 10 minutes, 57 seconds
Output 662/977: t=6840000.0 yr, dE/E0=1.72e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 9 hours, 30 minutes, 7 seconds
  Estimated time remaining to next output: 10 minutes, 57 seconds
Output 663/977: t=6850000.0 yr, dE/E0=1.57e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 9 hours, 16 minutes, 24 seconds
  Estimated time remaining to next output: 10 minutes, 56 seconds
Output 664/977: t=6860000.0 yr, dE/E0=1.55e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 9 hours, 2 minutes, 43 seconds
  Estimated time remaining to next output: 10 minutes, 56 seconds
Output 665/977: t=6870000.0 yr, dE/E0=1.66e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 8 hours, 49 minutes
  Estimated time remaining to next output: 10 minutes, 55 seconds
Output 666/977: t=6880000.0 yr, dE/E0=1.54e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 8 hours, 35 minutes, 26 seconds
  Estimated time remaining to next output: 10 minutes, 55 seconds
Output 667/977: t=6890000.0 yr, dE/E0=1.52e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 8 hours, 21 minutes, 49 seconds
  Estimated time remaining to next output: 10 minutes, 54 seconds
Output 668/977: t=6900000.0 yr, dE/E0=1.58e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 8 hours, 8 minutes, 20 seconds
  Estimated time remaining to next output: 10 minutes, 54 seconds
Output 669/977: t=6910000.0 yr, dE/E0=1.83e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 7 hours, 54 minutes, 42 seconds
  Estimated time remaining to next output: 10 minutes, 53 seconds
Output 670/977: t=6920000.0 yr, dE/E0=1.56e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 7 hours, 41 minutes
  Estimated time remaining to next output: 10 minutes, 52 seconds
Output 671/977: t=6930000.0 yr, dE/E0=1.41e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 7 hours, 27 minutes, 29 seconds
  Estimated time remaining to next output: 10 minutes, 52 seconds
Output 672/977: t=6940000.0 yr, dE/E0=1.53e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 7 hours, 13 minutes, 57 seconds
  Estimated time remaining to next output: 10 minutes, 51 seconds
Output 673/977: t=6950000.0 yr, dE/E0=1.62e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 7 hours, 25 seconds
  Estimated time remaining to next output: 10 minutes, 51 seconds
Output 674/977: t=6960000.0 yr, dE/E0=1.84e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 6 hours, 47 minutes, 2 seconds
  Estimated time remaining to next output: 10 minutes, 50 seconds
Output 675/977: t=6970000.0 yr, dE/E0=1.88e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 6 hours, 33 minutes, 37 seconds
  Estimated time remaining to next output: 10 minutes, 50 seconds
Output 676/977: t=6980000.0 yr, dE/E0=1.84e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 6 hours, 20 minutes, 13 seconds
  Estimated time remaining to next output: 10 minutes, 49 seconds
Output 677/977: t=6990000.0 yr, dE/E0=1.82e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 6 hours, 6 minutes, 48 seconds
  Estimated time remaining to next output: 10 minutes, 49 seconds
Output 678/977: t=7000000.0 yr, dE/E0=1.99e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 5 hours, 53 minutes, 22 seconds
  Estimated time remaining to next output: 10 minutes, 48 seconds
Output 679/977: t=7010000.0 yr, dE/E0=1.84e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 5 hours, 40 minutes, 2 seconds
  Estimated time remaining to next output: 10 minutes, 48 seconds
Output 680/977: t=7020000.0 yr, dE/E0=1.80e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 5 hours, 26 minutes, 38 seconds
  Estimated time remaining to next output: 10 minutes, 47 seconds
Output 681/977: t=7030000.0 yr, dE/E0=1.83e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 5 hours, 13 minutes, 21 seconds
  Estimated time remaining to next output: 10 minutes, 47 seconds
Output 682/977: t=7040000.0 yr, dE/E0=1.95e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 5 hours, 8 seconds
  Estimated time remaining to next output: 10 minutes, 46 seconds
Output 683/977: t=7050000.0 yr, dE/E0=1.95e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 4 hours, 47 minutes, 2 seconds
  Estimated time remaining to next output: 10 minutes, 46 seconds
Output 684/977: t=7060000.0 yr, dE/E0=1.97e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 4 hours, 33 minutes, 47 seconds
  Estimated time remaining to next output: 10 minutes, 45 seconds
Output 685/977: t=7070000.0 yr, dE/E0=1.92e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 4 hours, 20 minutes, 33 seconds
  Estimated time remaining to next output: 10 minutes, 45 seconds
Output 686/977: t=7080000.0 yr, dE/E0=2.08e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 4 hours, 7 minutes, 13 seconds
  Estimated time remaining to next output: 10 minutes, 44 seconds
Output 687/977: t=7090000.0 yr, dE/E0=2.06e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 3 hours, 54 minutes, 8 seconds
  Estimated time remaining to next output: 10 minutes, 44 seconds
Output 688/977: t=7100000.0 yr, dE/E0=2.35e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 3 hours, 41 minutes, 5 seconds
  Estimated time remaining to next output: 10 minutes, 43 seconds
Output 689/977: t=7110000.0 yr, dE/E0=2.47e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 3 hours, 28 minutes, 6 seconds
  Estimated time remaining to next output: 10 minutes, 43 seconds
Output 690/977: t=7120000.0 yr, dE/E0=2.31e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 3 hours, 14 minutes, 59 seconds
  Estimated time remaining to next output: 10 minutes, 42 seconds
Output 691/977: t=7130000.0 yr, dE/E0=2.44e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 3 hours, 1 minutes, 51 seconds
  Estimated time remaining to next output: 10 minutes, 42 seconds
Output 692/977: t=7140000.0 yr, dE/E0=2.23e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 2 hours, 48 minutes, 47 seconds
  Estimated time remaining to next output: 10 minutes, 41 seconds
Output 693/977: t=7150000.0 yr, dE/E0=2.22e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 2 hours, 35 minutes, 43 seconds
  Estimated time remaining to next output: 10 minutes, 41 seconds
Output 694/977: t=7160000.0 yr, dE/E0=2.17e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 2 hours, 22 minutes, 47 seconds
  Estimated time remaining to next output: 10 minutes, 40 seconds
Output 695/977: t=7170000.0 yr, dE/E0=2.43e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 2 hours, 9 minutes, 53 seconds
  Estimated time remaining to next output: 10 minutes, 40 seconds
Output 696/977: t=7180000.0 yr, dE/E0=2.40e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 1 hours, 56 minutes, 46 seconds
  Estimated time remaining to next output: 10 minutes, 39 seconds
Output 697/977: t=7190000.0 yr, dE/E0=2.17e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 1 hours, 43 minutes, 47 seconds
  Estimated time remaining to next output: 10 minutes, 39 seconds
Output 698/977: t=7200000.0 yr, dE/E0=2.30e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 1 hours, 30 minutes, 56 seconds
  Estimated time remaining to next output: 10 minutes, 38 seconds
Output 699/977: t=7210000.0 yr, dE/E0=2.43e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 1 hours, 17 minutes, 58 seconds
  Estimated time remaining to next output: 10 minutes, 38 seconds
Output 700/977: t=7220000.0 yr, dE/E0=2.48e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 1 hours, 4 minutes, 59 seconds
  Estimated time remaining to next output: 10 minutes, 37 seconds
Output 701/977: t=7230000.0 yr, dE/E0=2.68e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 52 minutes, 10 seconds
  Estimated time remaining to next output: 10 minutes, 37 seconds
Output 702/977: t=7240000.0 yr, dE/E0=2.56e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 39 minutes, 21 seconds
  Estimated time remaining to next output: 10 minutes, 36 seconds
Output 703/977: t=7250000.0 yr, dE/E0=2.64e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 26 minutes, 34 seconds
  Estimated time remaining to next output: 10 minutes, 36 seconds
Output 704/977: t=7260000.0 yr, dE/E0=2.52e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 13 minutes, 45 seconds
  Estimated time remaining to next output: 10 minutes, 35 seconds
Output 705/977: t=7270000.0 yr, dE/E0=2.57e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 58 seconds
  Estimated time remaining to next output: 10 minutes, 35 seconds
Output 706/977: t=7280000.0 yr, dE/E0=2.68e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 23 hours, 48 minutes, 15 seconds
  Estimated time remaining to next output: 10 minutes, 35 seconds
Output 707/977: t=7290000.0 yr, dE/E0=2.66e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 23 hours, 35 minutes, 38 seconds
  Estimated time remaining to next output: 10 minutes, 34 seconds
Output 708/977: t=7300000.0 yr, dE/E0=2.83e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 23 hours, 23 minutes, 1 seconds
  Estimated time remaining to next output: 10 minutes, 34 seconds
Output 709/977: t=7310000.0 yr, dE/E0=2.69e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 23 hours, 10 minutes, 19 seconds
  Estimated time remaining to next output: 10 minutes, 33 seconds
Output 710/977: t=7320000.0 yr, dE/E0=2.65e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 22 hours, 57 minutes, 43 seconds
  Estimated time remaining to next output: 10 minutes, 33 seconds
Output 711/977: t=7330000.0 yr, dE/E0=2.68e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 22 hours, 45 minutes, 4 seconds
  Estimated time remaining to next output: 10 minutes, 32 seconds
Output 712/977: t=7340000.0 yr, dE/E0=2.64e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 22 hours, 32 minutes, 23 seconds
  Estimated time remaining to next output: 10 minutes, 32 seconds
Output 713/977: t=7350000.0 yr, dE/E0=2.51e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 22 hours, 19 minutes, 49 seconds
  Estimated time remaining to next output: 10 minutes, 31 seconds
Output 714/977: t=7360000.0 yr, dE/E0=2.62e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 22 hours, 7 minutes, 12 seconds
  Estimated time remaining to next output: 10 minutes, 31 seconds
Output 715/977: t=7370000.0 yr, dE/E0=2.70e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 21 hours, 54 minutes, 43 seconds
  Estimated time remaining to next output: 10 minutes, 30 seconds
Output 716/977: t=7380000.0 yr, dE/E0=2.83e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 21 hours, 42 minutes, 6 seconds
  Estimated time remaining to next output: 10 minutes, 30 seconds
Output 717/977: t=7390000.0 yr, dE/E0=2.89e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 21 hours, 29 minutes, 38 seconds
  Estimated time remaining to next output: 10 minutes, 29 seconds
Output 718/977: t=7400000.0 yr, dE/E0=2.83e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 21 hours, 17 minutes, 13 seconds
  Estimated time remaining to next output: 10 minutes, 29 seconds
Output 719/977: t=7410000.0 yr, dE/E0=2.79e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 21 hours, 4 minutes, 51 seconds
  Estimated time remaining to next output: 10 minutes, 29 seconds
Output 720/977: t=7420000.0 yr, dE/E0=2.87e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 20 hours, 52 minutes, 22 seconds
  Estimated time remaining to next output: 10 minutes, 28 seconds
Output 721/977: t=7430000.0 yr, dE/E0=3.03e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 20 hours, 40 minutes
  Estimated time remaining to next output: 10 minutes, 28 seconds
Output 722/977: t=7440000.0 yr, dE/E0=2.72e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 20 hours, 27 minutes, 36 seconds
  Estimated time remaining to next output: 10 minutes, 27 seconds
Output 723/977: t=7450000.0 yr, dE/E0=2.70e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 20 hours, 15 minutes, 14 seconds
  Estimated time remaining to next output: 10 minutes, 27 seconds
Output 724/977: t=7460000.0 yr, dE/E0=2.81e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 20 hours, 2 minutes, 50 seconds
  Estimated time remaining to next output: 10 minutes, 26 seconds
Output 725/977: t=7470000.0 yr, dE/E0=2.85e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 19 hours, 50 minutes, 33 seconds
  Estimated time remaining to next output: 10 minutes, 26 seconds
Output 726/977: t=7480000.0 yr, dE/E0=2.75e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 19 hours, 38 minutes, 13 seconds
  Estimated time remaining to next output: 10 minutes, 25 seconds
Output 727/977: t=7490000.0 yr, dE/E0=2.87e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 19 hours, 25 minutes, 54 seconds
  Estimated time remaining to next output: 10 minutes, 25 seconds
Output 728/977: t=7500000.0 yr, dE/E0=2.78e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 19 hours, 13 minutes, 34 seconds
  Estimated time remaining to next output: 10 minutes, 24 seconds
Output 729/977: t=7510000.0 yr, dE/E0=2.77e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 19 hours, 1 minutes, 18 seconds
  Estimated time remaining to next output: 10 minutes, 24 seconds
Output 730/977: t=7520000.0 yr, dE/E0=2.92e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 18 hours, 49 minutes, 3 seconds
  Estimated time remaining to next output: 10 minutes, 24 seconds
Output 731/977: t=7530000.0 yr, dE/E0=2.93e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 18 hours, 36 minutes, 52 seconds
  Estimated time remaining to next output: 10 minutes, 23 seconds
Output 732/977: t=7540000.0 yr, dE/E0=2.78e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 18 hours, 24 minutes, 43 seconds
  Estimated time remaining to next output: 10 minutes, 23 seconds
Output 733/977: t=7550000.0 yr, dE/E0=2.91e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 18 hours, 12 minutes, 37 seconds
  Estimated time remaining to next output: 10 minutes, 22 seconds
Output 734/977: t=7560000.0 yr, dE/E0=3.02e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 18 hours, 24 seconds
  Estimated time remaining to next output: 10 minutes, 22 seconds
Output 735/977: t=7570000.0 yr, dE/E0=3.04e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 17 hours, 48 minutes, 19 seconds
  Estimated time remaining to next output: 10 minutes, 21 seconds
Output 736/977: t=7580000.0 yr, dE/E0=2.97e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 17 hours, 36 minutes, 13 seconds
  Estimated time remaining to next output: 10 minutes, 21 seconds
Output 737/977: t=7590000.0 yr, dE/E0=2.76e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 17 hours, 24 minutes, 13 seconds
  Estimated time remaining to next output: 10 minutes, 21 seconds
Output 738/977: t=7600000.0 yr, dE/E0=3.03e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 17 hours, 12 minutes, 11 seconds
  Estimated time remaining to next output: 10 minutes, 20 seconds
Output 739/977: t=7610000.0 yr, dE/E0=3.07e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 17 hours
  Estimated time remaining to next output: 10 minutes, 20 seconds
Output 740/977: t=7620000.0 yr, dE/E0=3.09e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 16 hours, 47 minutes, 54 seconds
  Estimated time remaining to next output: 10 minutes, 19 seconds
Output 741/977: t=7630000.0 yr, dE/E0=3.17e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 16 hours, 35 minutes, 51 seconds
  Estimated time remaining to next output: 10 minutes, 19 seconds
Output 742/977: t=7640000.0 yr, dE/E0=3.24e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 16 hours, 23 minutes, 47 seconds
  Estimated time remaining to next output: 10 minutes, 18 seconds
Output 743/977: t=7650000.0 yr, dE/E0=3.14e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 16 hours, 11 minutes, 46 seconds
  Estimated time remaining to next output: 10 minutes, 18 seconds
Output 744/977: t=7660000.0 yr, dE/E0=3.06e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 15 hours, 59 minutes, 53 seconds
  Estimated time remaining to next output: 10 minutes, 17 seconds
Output 745/977: t=7670000.0 yr, dE/E0=3.09e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 15 hours, 47 minutes, 53 seconds
  Estimated time remaining to next output: 10 minutes, 17 seconds
Output 746/977: t=7680000.0 yr, dE/E0=3.29e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 15 hours, 35 minutes, 59 seconds
  Estimated time remaining to next output: 10 minutes, 17 seconds
Output 747/977: t=7690000.0 yr, dE/E0=3.10e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 15 hours, 24 minutes, 1 seconds
  Estimated time remaining to next output: 10 minutes, 16 seconds
Output 748/977: t=7700000.0 yr, dE/E0=2.87e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 15 hours, 12 minutes, 5 seconds
  Estimated time remaining to next output: 10 minutes, 16 seconds
Output 749/977: t=7710000.0 yr, dE/E0=3.10e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 15 hours, 13 seconds
  Estimated time remaining to next output: 10 minutes, 15 seconds
Output 750/977: t=7720000.0 yr, dE/E0=3.24e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 14 hours, 48 minutes, 20 seconds
  Estimated time remaining to next output: 10 minutes, 15 seconds
Output 751/977: t=7730000.0 yr, dE/E0=3.29e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 14 hours, 36 minutes, 31 seconds
  Estimated time remaining to next output: 10 minutes, 15 seconds
Output 752/977: t=7740000.0 yr, dE/E0=3.13e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 14 hours, 24 minutes, 46 seconds
  Estimated time remaining to next output: 10 minutes, 14 seconds
Output 753/977: t=7750000.0 yr, dE/E0=3.15e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 14 hours, 12 minutes, 50 seconds
  Estimated time remaining to next output: 10 minutes, 14 seconds
Output 754/977: t=7760000.0 yr, dE/E0=3.11e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 14 hours, 1 minutes, 2 seconds
  Estimated time remaining to next output: 10 minutes, 13 seconds
Output 755/977: t=7770000.0 yr, dE/E0=3.12e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 13 hours, 49 minutes, 11 seconds
  Estimated time remaining to next output: 10 minutes, 13 seconds
Output 756/977: t=7780000.0 yr, dE/E0=3.15e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 13 hours, 37 minutes, 23 seconds
  Estimated time remaining to next output: 10 minutes, 12 seconds
Output 757/977: t=7790000.0 yr, dE/E0=3.37e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 13 hours, 25 minutes, 34 seconds
  Estimated time remaining to next output: 10 minutes, 12 seconds
Output 758/977: t=7800000.0 yr, dE/E0=3.26e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 13 hours, 13 minutes, 54 seconds
  Estimated time remaining to next output: 10 minutes, 12 seconds
Output 759/977: t=7810000.0 yr, dE/E0=3.27e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 13 hours, 2 minutes, 8 seconds
  Estimated time remaining to next output: 10 minutes, 11 seconds
Output 760/977: t=7820000.0 yr, dE/E0=3.20e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 12 hours, 50 minutes, 26 seconds
  Estimated time remaining to next output: 10 minutes, 11 seconds
Output 761/977: t=7830000.0 yr, dE/E0=3.17e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 12 hours, 38 minutes, 41 seconds
  Estimated time remaining to next output: 10 minutes, 10 seconds
Output 762/977: t=7840000.0 yr, dE/E0=3.24e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 12 hours, 26 minutes, 59 seconds
  Estimated time remaining to next output: 10 minutes, 10 seconds
Output 763/977: t=7850000.0 yr, dE/E0=3.28e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 12 hours, 15 minutes, 21 seconds
  Estimated time remaining to next output: 10 minutes, 9 seconds
Output 764/977: t=7860000.0 yr, dE/E0=3.29e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 12 hours, 3 minutes, 48 seconds
  Estimated time remaining to next output: 10 minutes, 9 seconds
Output 765/977: t=7870000.0 yr, dE/E0=3.52e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 11 hours, 52 minutes, 9 seconds
  Estimated time remaining to next output: 10 minutes, 9 seconds
Output 766/977: t=7880000.0 yr, dE/E0=3.51e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 11 hours, 40 minutes, 35 seconds
  Estimated time remaining to next output: 10 minutes, 8 seconds
Output 767/977: t=7890000.0 yr, dE/E0=3.52e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 11 hours, 28 minutes, 58 seconds
  Estimated time remaining to next output: 10 minutes, 8 seconds
Output 768/977: t=7900000.0 yr, dE/E0=3.54e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 11 hours, 17 minutes, 23 seconds
  Estimated time remaining to next output: 10 minutes, 7 seconds
Output 769/977: t=7910000.0 yr, dE/E0=3.65e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 11 hours, 5 minutes, 53 seconds
  Estimated time remaining to next output: 10 minutes, 7 seconds
Output 770/977: t=7920000.0 yr, dE/E0=3.68e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 10 hours, 54 minutes, 25 seconds
  Estimated time remaining to next output: 10 minutes, 7 seconds
Output 771/977: t=7930000.0 yr, dE/E0=3.67e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 10 hours, 42 minutes, 50 seconds
  Estimated time remaining to next output: 10 minutes, 6 seconds
Output 772/977: t=7940000.0 yr, dE/E0=3.67e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 10 hours, 31 minutes, 24 seconds
  Estimated time remaining to next output: 10 minutes, 6 seconds
Output 773/977: t=7950000.0 yr, dE/E0=3.63e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 10 hours, 19 minutes, 53 seconds
  Estimated time remaining to next output: 10 minutes, 5 seconds
Output 774/977: t=7960000.0 yr, dE/E0=3.85e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 10 hours, 8 minutes, 26 seconds
  Estimated time remaining to next output: 10 minutes, 5 seconds
Output 775/977: t=7970000.0 yr, dE/E0=3.91e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 9 hours, 56 minutes, 54 seconds
  Estimated time remaining to next output: 10 minutes, 5 seconds
Output 776/977: t=7980000.0 yr, dE/E0=3.81e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 9 hours, 45 minutes, 24 seconds
  Estimated time remaining to next output: 10 minutes, 4 seconds
Output 777/977: t=7990000.0 yr, dE/E0=3.89e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 9 hours, 34 minutes
  Estimated time remaining to next output: 10 minutes, 4 seconds
Output 778/977: t=8000000.0 yr, dE/E0=3.98e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 9 hours, 22 minutes, 32 seconds
  Estimated time remaining to next output: 10 minutes, 3 seconds
Output 779/977: t=8010000.0 yr, dE/E0=3.97e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 9 hours, 11 minutes, 6 seconds
  Estimated time remaining to next output: 10 minutes, 3 seconds
Output 780/977: t=8020000.0 yr, dE/E0=4.10e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 8 hours, 59 minutes, 45 seconds
  Estimated time remaining to next output: 10 minutes, 2 seconds
Output 781/977: t=8030000.0 yr, dE/E0=4.09e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 8 hours, 48 minutes, 28 seconds
  Estimated time remaining to next output: 10 minutes, 2 seconds
Output 782/977: t=8040000.0 yr, dE/E0=4.19e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 8 hours, 37 minutes, 8 seconds
  Estimated time remaining to next output: 10 minutes, 2 seconds
Output 783/977: t=8050000.0 yr, dE/E0=4.01e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 8 hours, 25 minutes, 50 seconds
  Estimated time remaining to next output: 10 minutes, 1 seconds
Output 784/977: t=8060000.0 yr, dE/E0=3.99e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 8 hours, 14 minutes, 33 seconds
  Estimated time remaining to next output: 10 minutes, 1 seconds
Output 785/977: t=8070000.0 yr, dE/E0=4.08e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 8 hours, 3 minutes, 21 seconds
  Estimated time remaining to next output: 10 minutes, 1 seconds
Output 786/977: t=8080000.0 yr, dE/E0=4.06e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 7 hours, 52 minutes, 11 seconds
  Estimated time remaining to next output: 10 minutes
Output 787/977: t=8090000.0 yr, dE/E0=4.08e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 7 hours, 40 minutes, 59 seconds
  Estimated time remaining to next output: 10 minutes
Output 788/977: t=8100000.0 yr, dE/E0=3.75e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 7 hours, 29 minutes, 44 seconds
  Estimated time remaining to next output: 9 minutes, 59 seconds
Output 789/977: t=8110000.0 yr, dE/E0=3.84e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 7 hours, 18 minutes, 32 seconds
  Estimated time remaining to next output: 9 minutes, 59 seconds
Output 790/977: t=8120000.0 yr, dE/E0=3.96e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 7 hours, 7 minutes, 22 seconds
  Estimated time remaining to next output: 9 minutes, 59 seconds
Output 791/977: t=8130000.0 yr, dE/E0=3.89e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 6 hours, 56 minutes, 10 seconds
  Estimated time remaining to next output: 9 minutes, 58 seconds
Output 792/977: t=8140000.0 yr, dE/E0=3.98e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 6 hours, 44 minutes, 59 seconds
  Estimated time remaining to next output: 9 minutes, 58 seconds
Output 793/977: t=8150000.0 yr, dE/E0=3.98e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 6 hours, 33 minutes, 46 seconds
  Estimated time remaining to next output: 9 minutes, 57 seconds
Output 794/977: t=8160000.0 yr, dE/E0=3.74e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 6 hours, 22 minutes, 39 seconds
  Estimated time remaining to next output: 9 minutes, 57 seconds
Output 795/977: t=8170000.0 yr, dE/E0=3.72e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 6 hours, 11 minutes, 31 seconds
  Estimated time remaining to next output: 9 minutes, 57 seconds
Output 796/977: t=8180000.0 yr, dE/E0=3.71e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 6 hours, 30 seconds
  Estimated time remaining to next output: 9 minutes, 56 seconds
Output 797/977: t=8190000.0 yr, dE/E0=3.68e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 5 hours, 49 minutes, 26 seconds
  Estimated time remaining to next output: 9 minutes, 56 seconds
Output 798/977: t=8200000.0 yr, dE/E0=3.59e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 5 hours, 38 minutes, 18 seconds
  Estimated time remaining to next output: 9 minutes, 56 seconds
Output 799/977: t=8210000.0 yr, dE/E0=3.59e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 5 hours, 27 minutes, 15 seconds
  Estimated time remaining to next output: 9 minutes, 55 seconds
Output 800/977: t=8220000.0 yr, dE/E0=3.54e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 5 hours, 16 minutes, 12 seconds
  Estimated time remaining to next output: 9 minutes, 55 seconds
Output 801/977: t=8230000.0 yr, dE/E0=3.59e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 5 hours, 5 minutes, 13 seconds
  Estimated time remaining to next output: 9 minutes, 54 seconds
Output 802/977: t=8240000.0 yr, dE/E0=3.67e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 4 hours, 54 minutes, 14 seconds
  Estimated time remaining to next output: 9 minutes, 54 seconds
Output 803/977: t=8250000.0 yr, dE/E0=3.74e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 4 hours, 43 minutes, 14 seconds
  Estimated time remaining to next output: 9 minutes, 54 seconds
Output 804/977: t=8260000.0 yr, dE/E0=3.51e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 4 hours, 32 minutes, 17 seconds
  Estimated time remaining to next output: 9 minutes, 53 seconds
Output 805/977: t=8270000.0 yr, dE/E0=3.64e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 4 hours, 21 minutes, 22 seconds
  Estimated time remaining to next output: 9 minutes, 53 seconds
Output 806/977: t=8280000.0 yr, dE/E0=3.72e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 4 hours, 10 minutes, 20 seconds
  Estimated time remaining to next output: 9 minutes, 53 seconds
Output 807/977: t=8290000.0 yr, dE/E0=3.87e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 3 hours, 59 minutes, 24 seconds
  Estimated time remaining to next output: 9 minutes, 52 seconds
Output 808/977: t=8300000.0 yr, dE/E0=3.56e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 3 hours, 48 minutes, 28 seconds
  Estimated time remaining to next output: 9 minutes, 52 seconds
Output 809/977: t=8310000.0 yr, dE/E0=3.69e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 3 hours, 37 minutes, 33 seconds
  Estimated time remaining to next output: 9 minutes, 51 seconds
Output 810/977: t=8320000.0 yr, dE/E0=3.67e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 3 hours, 26 minutes, 38 seconds
  Estimated time remaining to next output: 9 minutes, 51 seconds
Output 811/977: t=8330000.0 yr, dE/E0=3.99e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 3 hours, 15 minutes, 41 seconds
  Estimated time remaining to next output: 9 minutes, 51 seconds
Output 812/977: t=8340000.0 yr, dE/E0=3.80e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 3 hours, 4 minutes, 47 seconds
  Estimated time remaining to next output: 9 minutes, 50 seconds
Output 813/977: t=8350000.0 yr, dE/E0=3.86e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 2 hours, 53 minutes, 57 seconds
  Estimated time remaining to next output: 9 minutes, 50 seconds
Output 814/977: t=8360000.0 yr, dE/E0=3.76e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 2 hours, 43 minutes, 9 seconds
  Estimated time remaining to next output: 9 minutes, 50 seconds
Output 815/977: t=8370000.0 yr, dE/E0=3.68e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 2 hours, 32 minutes, 22 seconds
  Estimated time remaining to next output: 9 minutes, 49 seconds
Output 816/977: t=8380000.0 yr, dE/E0=3.47e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 2 hours, 21 minutes, 32 seconds
  Estimated time remaining to next output: 9 minutes, 49 seconds
Output 817/977: t=8390000.0 yr, dE/E0=3.45e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 2 hours, 10 minutes, 44 seconds
  Estimated time remaining to next output: 9 minutes, 49 seconds
Output 818/977: t=8400000.0 yr, dE/E0=3.33e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 1 hours, 59 minutes, 57 seconds
  Estimated time remaining to next output: 9 minutes, 48 seconds
Output 819/977: t=8410000.0 yr, dE/E0=3.44e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 1 hours, 49 minutes, 14 seconds
  Estimated time remaining to next output: 9 minutes, 48 seconds
Output 820/977: t=8420000.0 yr, dE/E0=3.31e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 1 hours, 38 minutes, 31 seconds
  Estimated time remaining to next output: 9 minutes, 47 seconds
Output 821/977: t=8430000.0 yr, dE/E0=3.46e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 1 hours, 27 minutes, 44 seconds
  Estimated time remaining to next output: 9 minutes, 47 seconds
Output 822/977: t=8440000.0 yr, dE/E0=3.36e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 1 hours, 17 minutes
  Estimated time remaining to next output: 9 minutes, 47 seconds
Output 823/977: t=8450000.0 yr, dE/E0=3.01e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 1 hours, 6 minutes, 17 seconds
  Estimated time remaining to next output: 9 minutes, 46 seconds
Output 824/977: t=8460000.0 yr, dE/E0=3.21e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 55 minutes, 35 seconds
  Estimated time remaining to next output: 9 minutes, 46 seconds
Output 825/977: t=8470000.0 yr, dE/E0=3.17e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 44 minutes, 54 seconds
  Estimated time remaining to next output: 9 minutes, 46 seconds
Output 826/977: t=8480000.0 yr, dE/E0=3.04e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 34 minutes, 16 seconds
  Estimated time remaining to next output: 9 minutes, 45 seconds
Output 827/977: t=8490000.0 yr, dE/E0=2.98e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 23 minutes, 38 seconds
  Estimated time remaining to next output: 9 minutes, 45 seconds
Output 828/977: t=8500000.0 yr, dE/E0=3.20e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 13 minutes
  Estimated time remaining to next output: 9 minutes, 45 seconds
Output 829/977: t=8510000.0 yr, dE/E0=3.21e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 2 minutes, 25 seconds
  Estimated time remaining to next output: 9 minutes, 44 seconds
Output 830/977: t=8520000.0 yr, dE/E0=3.19e-07, N=802
  Estimated time remaining to complete simulation: 23 hours, 51 minutes, 45 seconds
  Estimated time remaining to next output: 9 minutes, 44 seconds
Output 831/977: t=8530000.0 yr, dE/E0=3.48e-07, N=802
  Estimated time remaining to complete simulation: 23 hours, 41 minutes, 10 seconds
  Estimated time remaining to next output: 9 minutes, 44 seconds
Output 832/977: t=8540000.0 yr, dE/E0=3.39e-07, N=802
  Estimated time remaining to complete simulation: 23 hours, 30 minutes, 34 seconds
  Estimated time remaining to next output: 9 minutes, 43 seconds
Output 833/977: t=8550000.0 yr, dE/E0=3.36e-07, N=802
  Estimated time remaining to complete simulation: 23 hours, 20 minutes
  Estimated time remaining to next output: 9 minutes, 43 seconds
Output 834/977: t=8560000.0 yr, dE/E0=3.57e-07, N=802
  Estimated time remaining to complete simulation: 23 hours, 9 minutes, 29 seconds
  Estimated time remaining to next output: 9 minutes, 43 seconds
Output 835/977: t=8570000.0 yr, dE/E0=3.64e-07, N=802
  Estimated time remaining to complete simulation: 22 hours, 58 minutes, 55 seconds
  Estimated time remaining to next output: 9 minutes, 42 seconds
Output 836/977: t=8580000.0 yr, dE/E0=3.74e-07, N=802
  Estimated time remaining to complete simulation: 22 hours, 48 minutes, 30 seconds
  Estimated time remaining to next output: 9 minutes, 42 seconds
Output 837/977: t=8590000.0 yr, dE/E0=3.78e-07, N=802
  Estimated time remaining to complete simulation: 22 hours, 37 minutes, 56 seconds
  Estimated time remaining to next output: 9 minutes, 41 seconds
Output 838/977: t=8600000.0 yr, dE/E0=3.66e-07, N=802
  Estimated time remaining to complete simulation: 22 hours, 27 minutes, 24 seconds
  Estimated time remaining to next output: 9 minutes, 41 seconds
Output 839/977: t=8610000.0 yr, dE/E0=3.89e-07, N=802
  Estimated time remaining to complete simulation: 22 hours, 16 minutes, 54 seconds
  Estimated time remaining to next output: 9 minutes, 41 seconds
Output 840/977: t=8620000.0 yr, dE/E0=3.68e-07, N=802
  Estimated time remaining to complete simulation: 22 hours, 6 minutes, 26 seconds
  Estimated time remaining to next output: 9 minutes, 40 seconds
Output 841/977: t=8630000.0 yr, dE/E0=4.06e-07, N=802
  Estimated time remaining to complete simulation: 21 hours, 55 minutes, 58 seconds
  Estimated time remaining to next output: 9 minutes, 40 seconds
Output 842/977: t=8640000.0 yr, dE/E0=3.91e-07, N=802
  Estimated time remaining to complete simulation: 21 hours, 45 minutes, 29 seconds
  Estimated time remaining to next output: 9 minutes, 40 seconds
Output 843/977: t=8650000.0 yr, dE/E0=3.94e-07, N=802
  Estimated time remaining to complete simulation: 21 hours, 35 minutes, 6 seconds
  Estimated time remaining to next output: 9 minutes, 39 seconds
Output 844/977: t=8660000.0 yr, dE/E0=3.79e-07, N=802
  Estimated time remaining to complete simulation: 21 hours, 24 minutes, 40 seconds
  Estimated time remaining to next output: 9 minutes, 39 seconds
Output 845/977: t=8670000.0 yr, dE/E0=3.85e-07, N=802
  Estimated time remaining to complete simulation: 21 hours, 14 minutes, 14 seconds
  Estimated time remaining to next output: 9 minutes, 39 seconds
Output 846/977: t=8680000.0 yr, dE/E0=3.80e-07, N=802
  Estimated time remaining to complete simulation: 21 hours, 3 minutes, 50 seconds
  Estimated time remaining to next output: 9 minutes, 38 seconds
Output 847/977: t=8690000.0 yr, dE/E0=3.82e-07, N=802
  Estimated time remaining to complete simulation: 20 hours, 53 minutes, 24 seconds
  Estimated time remaining to next output: 9 minutes, 38 seconds
Output 848/977: t=8700000.0 yr, dE/E0=3.84e-07, N=802
  Estimated time remaining to complete simulation: 20 hours, 43 minutes, 2 seconds
  Estimated time remaining to next output: 9 minutes, 38 seconds
Output 849/977: t=8710000.0 yr, dE/E0=3.74e-07, N=802
  Estimated time remaining to complete simulation: 20 hours, 32 minutes, 42 seconds
  Estimated time remaining to next output: 9 minutes, 37 seconds
Output 850/977: t=8720000.0 yr, dE/E0=3.51e-07, N=802
  Estimated time remaining to complete simulation: 20 hours, 22 minutes, 20 seconds
  Estimated time remaining to next output: 9 minutes, 37 seconds
Output 851/977: t=8730000.0 yr, dE/E0=3.60e-07, N=802
  Estimated time remaining to complete simulation: 20 hours, 12 minutes, 3 seconds
  Estimated time remaining to next output: 9 minutes, 37 seconds
Output 852/977: t=8740000.0 yr, dE/E0=3.59e-07, N=802
  Estimated time remaining to complete simulation: 20 hours, 1 minutes, 43 seconds
  Estimated time remaining to next output: 9 minutes, 36 seconds
Output 853/977: t=8750000.0 yr, dE/E0=3.70e-07, N=802
  Estimated time remaining to complete simulation: 19 hours, 51 minutes, 25 seconds
  Estimated time remaining to next output: 9 minutes, 36 seconds
Output 854/977: t=8760000.0 yr, dE/E0=3.71e-07, N=802
  Estimated time remaining to complete simulation: 19 hours, 41 minutes, 7 seconds
  Estimated time remaining to next output: 9 minutes, 36 seconds
Output 855/977: t=8770000.0 yr, dE/E0=3.58e-07, N=802
  Estimated time remaining to complete simulation: 19 hours, 30 minutes, 48 seconds
  Estimated time remaining to next output: 9 minutes, 35 seconds
Output 856/977: t=8780000.0 yr, dE/E0=3.82e-07, N=802
  Estimated time remaining to complete simulation: 19 hours, 20 minutes, 34 seconds
  Estimated time remaining to next output: 9 minutes, 35 seconds
Output 857/977: t=8790000.0 yr, dE/E0=3.83e-07, N=802
  Estimated time remaining to complete simulation: 19 hours, 10 minutes, 18 seconds
  Estimated time remaining to next output: 9 minutes, 35 seconds
Output 858/977: t=8800000.0 yr, dE/E0=3.79e-07, N=802
  Estimated time remaining to complete simulation: 19 hours, 2 seconds
  Estimated time remaining to next output: 9 minutes, 34 seconds
Output 859/977: t=8810000.0 yr, dE/E0=3.95e-07, N=802
  Estimated time remaining to complete simulation: 18 hours, 49 minutes, 49 seconds
  Estimated time remaining to next output: 9 minutes, 34 seconds
Output 860/977: t=8820000.0 yr, dE/E0=3.86e-07, N=802
  Estimated time remaining to complete simulation: 18 hours, 39 minutes, 33 seconds
  Estimated time remaining to next output: 9 minutes, 34 seconds
Output 861/977: t=8830000.0 yr, dE/E0=3.76e-07, N=802
  Estimated time remaining to complete simulation: 18 hours, 29 minutes, 22 seconds
  Estimated time remaining to next output: 9 minutes, 33 seconds
Output 862/977: t=8840000.0 yr, dE/E0=4.00e-07, N=802
  Estimated time remaining to complete simulation: 18 hours, 19 minutes, 12 seconds
  Estimated time remaining to next output: 9 minutes, 33 seconds
Output 863/977: t=8850000.0 yr, dE/E0=3.99e-07, N=802
  Estimated time remaining to complete simulation: 18 hours, 8 minutes, 59 seconds
  Estimated time remaining to next output: 9 minutes, 33 seconds
Output 864/977: t=8860000.0 yr, dE/E0=3.73e-07, N=802
  Estimated time remaining to complete simulation: 17 hours, 58 minutes, 49 seconds
  Estimated time remaining to next output: 9 minutes, 32 seconds
Output 865/977: t=8870000.0 yr, dE/E0=3.74e-07, N=802
  Estimated time remaining to complete simulation: 17 hours, 48 minutes, 42 seconds
  Estimated time remaining to next output: 9 minutes, 32 seconds
Output 866/977: t=8880000.0 yr, dE/E0=3.71e-07, N=802
  Estimated time remaining to complete simulation: 17 hours, 38 minutes, 34 seconds
  Estimated time remaining to next output: 9 minutes, 32 seconds
Output 867/977: t=8890000.0 yr, dE/E0=3.79e-07, N=802
  Estimated time remaining to complete simulation: 17 hours, 28 minutes, 28 seconds
  Estimated time remaining to next output: 9 minutes, 31 seconds
Output 868/977: t=8900000.0 yr, dE/E0=3.41e-07, N=802
  Estimated time remaining to complete simulation: 17 hours, 18 minutes, 20 seconds
  Estimated time remaining to next output: 9 minutes, 31 seconds
Output 869/977: t=8910000.0 yr, dE/E0=3.47e-07, N=802
  Estimated time remaining to complete simulation: 17 hours, 8 minutes, 12 seconds
  Estimated time remaining to next output: 9 minutes, 31 seconds
Output 870/977: t=8920000.0 yr, dE/E0=3.54e-07, N=802
  Estimated time remaining to complete simulation: 16 hours, 58 minutes, 3 seconds
  Estimated time remaining to next output: 9 minutes, 30 seconds
Output 871/977: t=8930000.0 yr, dE/E0=3.54e-07, N=802
  Estimated time remaining to complete simulation: 16 hours, 47 minutes, 59 seconds
  Estimated time remaining to next output: 9 minutes, 30 seconds
Output 872/977: t=8940000.0 yr, dE/E0=3.32e-07, N=802
  Estimated time remaining to complete simulation: 16 hours, 37 minutes, 56 seconds
  Estimated time remaining to next output: 9 minutes, 30 seconds
Output 873/977: t=8950000.0 yr, dE/E0=3.55e-07, N=802
  Estimated time remaining to complete simulation: 16 hours, 27 minutes, 52 seconds
  Estimated time remaining to next output: 9 minutes, 29 seconds
Output 874/977: t=8960000.0 yr, dE/E0=3.43e-07, N=802
  Estimated time remaining to complete simulation: 16 hours, 17 minutes, 50 seconds
  Estimated time remaining to next output: 9 minutes, 29 seconds
Output 875/977: t=8970000.0 yr, dE/E0=3.30e-07, N=802
  Estimated time remaining to complete simulation: 16 hours, 7 minutes, 50 seconds
  Estimated time remaining to next output: 9 minutes, 29 seconds
Output 876/977: t=8980000.0 yr, dE/E0=3.52e-07, N=802
  Estimated time remaining to complete simulation: 15 hours, 57 minutes, 49 seconds
  Estimated time remaining to next output: 9 minutes, 29 seconds
Output 877/977: t=8990000.0 yr, dE/E0=3.12e-07, N=802
  Estimated time remaining to complete simulation: 15 hours, 47 minutes, 47 seconds
  Estimated time remaining to next output: 9 minutes, 28 seconds
Output 878/977: t=9000000.0 yr, dE/E0=3.16e-07, N=802
  Estimated time remaining to complete simulation: 15 hours, 37 minutes, 45 seconds
  Estimated time remaining to next output: 9 minutes, 28 seconds
Output 879/977: t=9010000.0 yr, dE/E0=3.18e-07, N=802
  Estimated time remaining to complete simulation: 15 hours, 27 minutes, 46 seconds
  Estimated time remaining to next output: 9 minutes, 28 seconds
Output 880/977: t=9020000.0 yr, dE/E0=3.38e-07, N=802
  Estimated time remaining to complete simulation: 15 hours, 17 minutes, 47 seconds
  Estimated time remaining to next output: 9 minutes, 27 seconds
Output 881/977: t=9030000.0 yr, dE/E0=3.48e-07, N=802
  Estimated time remaining to complete simulation: 15 hours, 7 minutes, 50 seconds
  Estimated time remaining to next output: 9 minutes, 27 seconds
Output 882/977: t=9040000.0 yr, dE/E0=3.20e-07, N=802
  Estimated time remaining to complete simulation: 14 hours, 57 minutes, 54 seconds
  Estimated time remaining to next output: 9 minutes, 27 seconds
Output 883/977: t=9050000.0 yr, dE/E0=3.05e-07, N=802
  Estimated time remaining to complete simulation: 14 hours, 47 minutes, 59 seconds
  Estimated time remaining to next output: 9 minutes, 26 seconds
Output 884/977: t=9060000.0 yr, dE/E0=3.13e-07, N=802
  Estimated time remaining to complete simulation: 14 hours, 38 minutes, 4 seconds
  Estimated time remaining to next output: 9 minutes, 26 seconds
Output 885/977: t=9070000.0 yr, dE/E0=3.04e-07, N=802
  Estimated time remaining to complete simulation: 14 hours, 28 minutes, 9 seconds
  Estimated time remaining to next output: 9 minutes, 26 seconds
Output 886/977: t=9080000.0 yr, dE/E0=3.11e-07, N=802
  Estimated time remaining to complete simulation: 14 hours, 18 minutes, 15 seconds
  Estimated time remaining to next output: 9 minutes, 25 seconds
Output 887/977: t=9090000.0 yr, dE/E0=3.21e-07, N=802
  Estimated time remaining to complete simulation: 14 hours, 8 minutes, 21 seconds
  Estimated time remaining to next output: 9 minutes, 25 seconds
Output 888/977: t=9100000.0 yr, dE/E0=3.31e-07, N=802
  Estimated time remaining to complete simulation: 13 hours, 58 minutes, 28 seconds
  Estimated time remaining to next output: 9 minutes, 25 seconds
Output 889/977: t=9110000.0 yr, dE/E0=3.07e-07, N=802
  Estimated time remaining to complete simulation: 13 hours, 48 minutes, 35 seconds
  Estimated time remaining to next output: 9 minutes, 24 seconds
Output 890/977: t=9120000.0 yr, dE/E0=3.22e-07, N=802
  Estimated time remaining to complete simulation: 13 hours, 38 minutes, 44 seconds
  Estimated time remaining to next output: 9 minutes, 24 seconds
Output 891/977: t=9130000.0 yr, dE/E0=3.30e-07, N=802
  Estimated time remaining to complete simulation: 13 hours, 28 minutes, 53 seconds
  Estimated time remaining to next output: 9 minutes, 24 seconds
Output 892/977: t=9140000.0 yr, dE/E0=3.53e-07, N=802
  Estimated time remaining to complete simulation: 13 hours, 19 minutes, 1 seconds
  Estimated time remaining to next output: 9 minutes, 24 seconds
Output 893/977: t=9150000.0 yr, dE/E0=3.35e-07, N=802
  Estimated time remaining to complete simulation: 13 hours, 9 minutes, 11 seconds
  Estimated time remaining to next output: 9 minutes, 23 seconds
Output 894/977: t=9160000.0 yr, dE/E0=3.38e-07, N=802
  Estimated time remaining to complete simulation: 12 hours, 59 minutes, 23 seconds
  Estimated time remaining to next output: 9 minutes, 23 seconds
Output 895/977: t=9170000.0 yr, dE/E0=3.23e-07, N=802
  Estimated time remaining to complete simulation: 12 hours, 49 minutes, 34 seconds
  Estimated time remaining to next output: 9 minutes, 23 seconds
Output 896/977: t=9180000.0 yr, dE/E0=3.41e-07, N=802
  Estimated time remaining to complete simulation: 12 hours, 39 minutes, 45 seconds
  Estimated time remaining to next output: 9 minutes, 22 seconds
Output 897/977: t=9190000.0 yr, dE/E0=3.48e-07, N=802
  Estimated time remaining to complete simulation: 12 hours, 29 minutes, 57 seconds
  Estimated time remaining to next output: 9 minutes, 22 seconds
Output 898/977: t=9200000.0 yr, dE/E0=3.30e-07, N=802
  Estimated time remaining to complete simulation: 12 hours, 20 minutes, 11 seconds
  Estimated time remaining to next output: 9 minutes, 22 seconds
Output 899/977: t=9210000.0 yr, dE/E0=3.39e-07, N=802
  Estimated time remaining to complete simulation: 12 hours, 10 minutes, 25 seconds
  Estimated time remaining to next output: 9 minutes, 21 seconds
Output 900/977: t=9220000.0 yr, dE/E0=3.31e-07, N=802
  Estimated time remaining to complete simulation: 12 hours, 40 seconds
  Estimated time remaining to next output: 9 minutes, 21 seconds
Output 901/977: t=9230000.0 yr, dE/E0=3.21e-07, N=802
  Estimated time remaining to complete simulation: 11 hours, 50 minutes, 56 seconds
  Estimated time remaining to next output: 9 minutes, 21 seconds
Output 902/977: t=9240000.0 yr, dE/E0=3.20e-07, N=802
  Estimated time remaining to complete simulation: 11 hours, 41 minutes, 13 seconds
  Estimated time remaining to next output: 9 minutes, 20 seconds
Output 903/977: t=9250000.0 yr, dE/E0=3.23e-07, N=802
  Estimated time remaining to complete simulation: 11 hours, 31 minutes, 29 seconds
  Estimated time remaining to next output: 9 minutes, 20 seconds
Output 904/977: t=9260000.0 yr, dE/E0=3.28e-07, N=802
  Estimated time remaining to complete simulation: 11 hours, 21 minutes, 46 seconds
  Estimated time remaining to next output: 9 minutes, 20 seconds
Output 905/977: t=9270000.0 yr, dE/E0=3.22e-07, N=802
  Estimated time remaining to complete simulation: 11 hours, 12 minutes, 5 seconds
  Estimated time remaining to next output: 9 minutes, 20 seconds
Output 906/977: t=9280000.0 yr, dE/E0=3.30e-07, N=802
  Estimated time remaining to complete simulation: 11 hours, 2 minutes, 23 seconds
  Estimated time remaining to next output: 9 minutes, 19 seconds
Output 907/977: t=9290000.0 yr, dE/E0=3.32e-07, N=802
  Estimated time remaining to complete simulation: 10 hours, 52 minutes, 42 seconds
  Estimated time remaining to next output: 9 minutes, 19 seconds
Output 908/977: t=9300000.0 yr, dE/E0=3.52e-07, N=802
  Estimated time remaining to complete simulation: 10 hours, 43 minutes, 3 seconds
  Estimated time remaining to next output: 9 minutes, 19 seconds
Output 909/977: t=9310000.0 yr, dE/E0=3.48e-07, N=802
  Estimated time remaining to complete simulation: 10 hours, 33 minutes, 22 seconds
  Estimated time remaining to next output: 9 minutes, 18 seconds
Output 910/977: t=9320000.0 yr, dE/E0=3.53e-07, N=802
  Estimated time remaining to complete simulation: 10 hours, 23 minutes, 42 seconds
  Estimated time remaining to next output: 9 minutes, 18 seconds
Output 911/977: t=9330000.0 yr, dE/E0=3.27e-07, N=802
  Estimated time remaining to complete simulation: 10 hours, 14 minutes, 4 seconds
  Estimated time remaining to next output: 9 minutes, 18 seconds
Output 912/977: t=9340000.0 yr, dE/E0=3.34e-07, N=802
  Estimated time remaining to complete simulation: 10 hours, 4 minutes, 27 seconds
  Estimated time remaining to next output: 9 minutes, 17 seconds
Output 913/977: t=9350000.0 yr, dE/E0=3.25e-07, N=802
  Estimated time remaining to complete simulation: 9 hours, 54 minutes, 50 seconds
  Estimated time remaining to next output: 9 minutes, 17 seconds
Output 914/977: t=9360000.0 yr, dE/E0=3.38e-07, N=802
  Estimated time remaining to complete simulation: 9 hours, 45 minutes, 14 seconds
  Estimated time remaining to next output: 9 minutes, 17 seconds
Output 915/977: t=9370000.0 yr, dE/E0=3.50e-07, N=802
  Estimated time remaining to complete simulation: 9 hours, 35 minutes, 38 seconds
  Estimated time remaining to next output: 9 minutes, 17 seconds
Output 916/977: t=9380000.0 yr, dE/E0=3.21e-07, N=802
  Estimated time remaining to complete simulation: 9 hours, 26 minutes, 3 seconds
  Estimated time remaining to next output: 9 minutes, 16 seconds
Output 917/977: t=9390000.0 yr, dE/E0=3.42e-07, N=802
  Estimated time remaining to complete simulation: 9 hours, 16 minutes, 29 seconds
  Estimated time remaining to next output: 9 minutes, 16 seconds
Output 918/977: t=9400000.0 yr, dE/E0=3.40e-07, N=802
  Estimated time remaining to complete simulation: 9 hours, 6 minutes, 55 seconds
  Estimated time remaining to next output: 9 minutes, 16 seconds
Output 919/977: t=9410000.0 yr, dE/E0=3.47e-07, N=802
  Estimated time remaining to complete simulation: 8 hours, 57 minutes, 22 seconds
  Estimated time remaining to next output: 9 minutes, 15 seconds
Output 920/977: t=9420000.0 yr, dE/E0=3.41e-07, N=802
  Estimated time remaining to complete simulation: 8 hours, 47 minutes, 50 seconds
  Estimated time remaining to next output: 9 minutes, 15 seconds
Output 921/977: t=9430000.0 yr, dE/E0=3.43e-07, N=802
  Estimated time remaining to complete simulation: 8 hours, 38 minutes, 19 seconds
  Estimated time remaining to next output: 9 minutes, 15 seconds
Output 922/977: t=9440000.0 yr, dE/E0=3.41e-07, N=802
  Estimated time remaining to complete simulation: 8 hours, 28 minutes, 47 seconds
  Estimated time remaining to next output: 9 minutes, 15 seconds
Output 923/977: t=9450000.0 yr, dE/E0=3.38e-07, N=802
  Estimated time remaining to complete simulation: 8 hours, 19 minutes, 17 seconds
  Estimated time remaining to next output: 9 minutes, 14 seconds
Output 924/977: t=9460000.0 yr, dE/E0=3.37e-07, N=802
  Estimated time remaining to complete simulation: 8 hours, 9 minutes, 46 seconds
  Estimated time remaining to next output: 9 minutes, 14 seconds
Output 925/977: t=9470000.0 yr, dE/E0=3.38e-07, N=802
  Estimated time remaining to complete simulation: 8 hours, 18 seconds
  Estimated time remaining to next output: 9 minutes, 14 seconds
Output 926/977: t=9480000.0 yr, dE/E0=3.23e-07, N=802
  Estimated time remaining to complete simulation: 7 hours, 50 minutes, 48 seconds
  Estimated time remaining to next output: 9 minutes, 13 seconds
Output 927/977: t=9490000.0 yr, dE/E0=3.18e-07, N=802
  Estimated time remaining to complete simulation: 7 hours, 41 minutes, 19 seconds
  Estimated time remaining to next output: 9 minutes, 13 seconds
Output 928/977: t=9500000.0 yr, dE/E0=3.16e-07, N=802
  Estimated time remaining to complete simulation: 7 hours, 31 minutes, 52 seconds
  Estimated time remaining to next output: 9 minutes, 13 seconds
Output 929/977: t=9510000.0 yr, dE/E0=3.20e-07, N=802
  Estimated time remaining to complete simulation: 7 hours, 22 minutes, 24 seconds
  Estimated time remaining to next output: 9 minutes, 13 seconds
Output 930/977: t=9520000.0 yr, dE/E0=3.08e-07, N=802
  Estimated time remaining to complete simulation: 7 hours, 12 minutes, 58 seconds
  Estimated time remaining to next output: 9 minutes, 12 seconds
Output 931/977: t=9530000.0 yr, dE/E0=3.42e-07, N=802
  Estimated time remaining to complete simulation: 7 hours, 3 minutes, 32 seconds
  Estimated time remaining to next output: 9 minutes, 12 seconds
Output 932/977: t=9540000.0 yr, dE/E0=3.10e-07, N=802
  Estimated time remaining to complete simulation: 6 hours, 54 minutes, 6 seconds
  Estimated time remaining to next output: 9 minutes, 12 seconds
Output 933/977: t=9550000.0 yr, dE/E0=3.29e-07, N=802
  Estimated time remaining to complete simulation: 6 hours, 44 minutes, 41 seconds
  Estimated time remaining to next output: 9 minutes, 11 seconds
Output 934/977: t=9560000.0 yr, dE/E0=3.32e-07, N=802
  Estimated time remaining to complete simulation: 6 hours, 35 minutes, 17 seconds
  Estimated time remaining to next output: 9 minutes, 11 seconds
Output 935/977: t=9570000.0 yr, dE/E0=3.24e-07, N=802
  Estimated time remaining to complete simulation: 6 hours, 25 minutes, 54 seconds
  Estimated time remaining to next output: 9 minutes, 11 seconds
Output 936/977: t=9580000.0 yr, dE/E0=3.31e-07, N=802
  Estimated time remaining to complete simulation: 6 hours, 16 minutes, 31 seconds
  Estimated time remaining to next output: 9 minutes, 11 seconds
Output 937/977: t=9590000.0 yr, dE/E0=3.22e-07, N=802
  Estimated time remaining to complete simulation: 6 hours, 7 minutes, 9 seconds
  Estimated time remaining to next output: 9 minutes, 10 seconds
Output 938/977: t=9600000.0 yr, dE/E0=3.40e-07, N=802
  Estimated time remaining to complete simulation: 5 hours, 57 minutes, 48 seconds
  Estimated time remaining to next output: 9 minutes, 10 seconds
Output 939/977: t=9610000.0 yr, dE/E0=3.40e-07, N=802
  Estimated time remaining to complete simulation: 5 hours, 48 minutes, 26 seconds
  Estimated time remaining to next output: 9 minutes, 10 seconds
Output 940/977: t=9620000.0 yr, dE/E0=3.42e-07, N=802
  Estimated time remaining to complete simulation: 5 hours, 39 minutes, 5 seconds
  Estimated time remaining to next output: 9 minutes, 9 seconds
Output 941/977: t=9630000.0 yr, dE/E0=3.33e-07, N=802
  Estimated time remaining to complete simulation: 5 hours, 29 minutes, 45 seconds
  Estimated time remaining to next output: 9 minutes, 9 seconds
Output 942/977: t=9640000.0 yr, dE/E0=3.56e-07, N=802
  Estimated time remaining to complete simulation: 5 hours, 20 minutes, 26 seconds
  Estimated time remaining to next output: 9 minutes, 9 seconds
Output 943/977: t=9650000.0 yr, dE/E0=3.53e-07, N=802
  Estimated time remaining to complete simulation: 5 hours, 11 minutes, 8 seconds
  Estimated time remaining to next output: 9 minutes, 9 seconds
Output 944/977: t=9660000.0 yr, dE/E0=3.51e-07, N=802
  Estimated time remaining to complete simulation: 5 hours, 1 minutes, 50 seconds
  Estimated time remaining to next output: 9 minutes, 8 seconds
Output 945/977: t=9670000.0 yr, dE/E0=3.62e-07, N=802
  Estimated time remaining to complete simulation: 4 hours, 52 minutes, 32 seconds
  Estimated time remaining to next output: 9 minutes, 8 seconds
Output 946/977: t=9680000.0 yr, dE/E0=3.66e-07, N=802
  Estimated time remaining to complete simulation: 4 hours, 43 minutes, 15 seconds
  Estimated time remaining to next output: 9 minutes, 8 seconds
Output 947/977: t=9690000.0 yr, dE/E0=3.64e-07, N=802
  Estimated time remaining to complete simulation: 4 hours, 33 minutes, 58 seconds
  Estimated time remaining to next output: 9 minutes, 7 seconds
Output 948/977: t=9700000.0 yr, dE/E0=3.47e-07, N=802
  Estimated time remaining to complete simulation: 4 hours, 24 minutes, 43 seconds
  Estimated time remaining to next output: 9 minutes, 7 seconds
Output 949/977: t=9710000.0 yr, dE/E0=3.60e-07, N=802
  Estimated time remaining to complete simulation: 4 hours, 15 minutes, 28 seconds
  Estimated time remaining to next output: 9 minutes, 7 seconds
Output 950/977: t=9720000.0 yr, dE/E0=3.65e-07, N=802
  Estimated time remaining to complete simulation: 4 hours, 6 minutes, 13 seconds
  Estimated time remaining to next output: 9 minutes, 7 seconds
Output 951/977: t=9730000.0 yr, dE/E0=3.74e-07, N=802
  Estimated time remaining to complete simulation: 3 hours, 56 minutes, 59 seconds
  Estimated time remaining to next output: 9 minutes, 6 seconds
Output 952/977: t=9740000.0 yr, dE/E0=3.56e-07, N=802
  Estimated time remaining to complete simulation: 3 hours, 47 minutes, 45 seconds
  Estimated time remaining to next output: 9 minutes, 6 seconds
Output 953/977: t=9750000.0 yr, dE/E0=3.84e-07, N=802
  Estimated time remaining to complete simulation: 3 hours, 38 minutes, 33 seconds
  Estimated time remaining to next output: 9 minutes, 6 seconds
Output 954/977: t=9760000.0 yr, dE/E0=3.70e-07, N=802
  Estimated time remaining to complete simulation: 3 hours, 29 minutes, 20 seconds
  Estimated time remaining to next output: 9 minutes, 6 seconds
Output 955/977: t=9770000.0 yr, dE/E0=3.75e-07, N=802
  Estimated time remaining to complete simulation: 3 hours, 20 minutes, 8 seconds
  Estimated time remaining to next output: 9 minutes, 5 seconds
Output 956/977: t=9780000.0 yr, dE/E0=3.81e-07, N=802
  Estimated time remaining to complete simulation: 3 hours, 10 minutes, 57 seconds
  Estimated time remaining to next output: 9 minutes, 5 seconds
Output 957/977: t=9790000.0 yr, dE/E0=3.82e-07, N=802
  Estimated time remaining to complete simulation: 3 hours, 1 minutes, 46 seconds
  Estimated time remaining to next output: 9 minutes, 5 seconds
Output 958/977: t=9800000.0 yr, dE/E0=3.65e-07, N=802
  Estimated time remaining to complete simulation: 2 hours, 52 minutes, 35 seconds
  Estimated time remaining to next output: 9 minutes, 5 seconds
Output 959/977: t=9810000.0 yr, dE/E0=3.91e-07, N=802
  Estimated time remaining to complete simulation: 2 hours, 43 minutes, 25 seconds
  Estimated time remaining to next output: 9 minutes, 4 seconds
Output 960/977: t=9820000.0 yr, dE/E0=3.88e-07, N=802
  Estimated time remaining to complete simulation: 2 hours, 34 minutes, 16 seconds
  Estimated time remaining to next output: 9 minutes, 4 seconds
Output 961/977: t=9830000.0 yr, dE/E0=3.84e-07, N=802
  Estimated time remaining to complete simulation: 2 hours, 25 minutes, 7 seconds
  Estimated time remaining to next output: 9 minutes, 4 seconds
Output 962/977: t=9840000.0 yr, dE/E0=3.90e-07, N=802
  Estimated time remaining to complete simulation: 2 hours, 15 minutes, 59 seconds
  Estimated time remaining to next output: 9 minutes, 3 seconds
Output 963/977: t=9850000.0 yr, dE/E0=3.81e-07, N=802
  Estimated time remaining to complete simulation: 2 hours, 6 minutes, 51 seconds
  Estimated time remaining to next output: 9 minutes, 3 seconds
Output 964/977: t=9860000.0 yr, dE/E0=3.71e-07, N=802
  Estimated time remaining to complete simulation: 1 hours, 57 minutes, 44 seconds
  Estimated time remaining to next output: 9 minutes, 3 seconds
Output 965/977: t=9870000.0 yr, dE/E0=3.92e-07, N=802
  Estimated time remaining to complete simulation: 1 hours, 48 minutes, 37 seconds
  Estimated time remaining to next output: 9 minutes, 3 seconds
Output 966/977: t=9880000.0 yr, dE/E0=3.91e-07, N=802
  Estimated time remaining to complete simulation: 1 hours, 39 minutes, 31 seconds
  Estimated time remaining to next output: 9 minutes, 2 seconds
Output 967/977: t=9890000.0 yr, dE/E0=3.77e-07, N=802
  Estimated time remaining to complete simulation: 1 hours, 30 minutes, 25 seconds
  Estimated time remaining to next output: 9 minutes, 2 seconds
Output 968/977: t=9900000.0 yr, dE/E0=3.81e-07, N=802
  Estimated time remaining to complete simulation: 1 hours, 21 minutes, 20 seconds
  Estimated time remaining to next output: 9 minutes, 2 seconds
Output 969/977: t=9910000.0 yr, dE/E0=3.77e-07, N=802
  Estimated time remaining to complete simulation: 1 hours, 12 minutes, 16 seconds
  Estimated time remaining to next output: 9 minutes, 2 seconds
Output 970/977: t=9920000.0 yr, dE/E0=3.96e-07, N=802
  Estimated time remaining to complete simulation: 1 hours, 3 minutes, 12 seconds
  Estimated time remaining to next output: 9 minutes, 1 seconds
Output 971/977: t=9930000.0 yr, dE/E0=4.01e-07, N=802
  Estimated time remaining to complete simulation: 54 minutes, 9 seconds
  Estimated time remaining to next output: 9 minutes, 1 seconds
Output 972/977: t=9940000.0 yr, dE/E0=3.89e-07, N=802
  Estimated time remaining to complete simulation: 45 minutes, 6 seconds
  Estimated time remaining to next output: 9 minutes, 1 seconds
Output 973/977: t=9950000.0 yr, dE/E0=3.93e-07, N=802
  Estimated time remaining to complete simulation: 36 minutes, 3 seconds
  Estimated time remaining to next output: 9 minutes
Output 974/977: t=9960000.0 yr, dE/E0=3.86e-07, N=802
  Estimated time remaining to complete simulation: 27 minutes, 2 seconds
  Estimated time remaining to next output: 9 minutes
Output 975/977: t=9970000.0 yr, dE/E0=3.89e-07, N=802
  Estimated time remaining to complete simulation: 18 minutes
  Estimated time remaining to next output: 9 minutes
Output 976/977: t=9980000.0 yr, dE/E0=3.61e-07, N=802
  Estimated time remaining to complete simulation: 9 minutes
  Estimated time remaining to next output: 9 minutes
Output 977/977: t=9990000.0 yr, dE/E0=3.73e-07, N=802
  Estimated time remaining to complete simulation: 0 seconds
Output 978/977: t=10000000.0 yr, dE/E0=3.97e-07, N=802
  Estimated time remaining to complete simulation: -1 months, 4 weeks, 1 days, 23 hours, 51 minutes, 1 seconds

Simulation complete.
Total runtime: 6 days, 2 hours, 36 minutes, 37 seconds

Krivov & Booth (2018) self-stirring check (Eqs. 9-10):
  NOTE: a giant planet is present; the two-population self-stirring model assumes no external perturber, so C_e below is only indicative.
  Final time:                 t = 1.000000e+07 yr
  Rayleigh outlier cut:       e > 5 sigma = 2.5674e-01 (sigma = median(e)/sqrt(2 ln 2) = 5.1347e-02)
  Stirred-disk check:         median(e) = 6.0457e-02 vs 30 x disk.emax = 9.6000e-04 -> stirred, cut applied
  Excluded MPs:               14 -- MP_302 (e = 0.6846), MP_551 (e = 0.5754), MP_410 (e = 0.4699), MP_562 (e = 0.4500), MP_386 (e = 0.4413), MP_366 (e = 0.4251), MP_493 (e = 0.3825), MP_620 (e = 0.3584), MP_219 (e = 0.3539), MP_786 (e = 0.3483), MP_738 (e = 0.3420), MP_330 (e = 0.3417), MP_163 (e = 0.3252), MP_609 (e = 0.3249)
  KS test of kept e vs Rayleigh: D = 0.0349, p = 0.286
  RMS eccentricity (786 of 800 MPs): 7.044601e-02  (all MPs: 8.989870e-02)
  Belt geometry:              a = 100, da = 10, a/da = 10
  Masses:                     M_max = 2.152034e-08 Msun, M_disc = 3.003490e-06 Msun
  Implied stirring timescale: T = 8.120903e+11 yr
  Effective stirring factor:  C_e = 1905.1475  (all MPs, no cut: 5052.6186)
  WARNING: C_e = 1905.1475 >= 40 (Ida & Makino 1993 canonical value) -- this run stirs at or above the analytic self-stirring rate.
Saved archive: outputs/SS_800MP_10Myr_PSD2B_100Mearth_lorentzian/SS_800MP_10Myr_PSD2B_100Mearth_lorentzian.bin
Number of snapshots saved: 1002
Archive time range: 0.000e+00 yr to 1.000e+07 yr
Particle-name check: OK (1002 snapshots)
Loaded snapshot table from archive.
role
massive_planetesimal    800
star                      1
giant_planet              1
Name: count, dtype: int64
Saved: outputs/SS_800MP_10Myr_PSD2B_100Mearth_lorentzian/figures/survival_fraction_vs_time.png
Saved: outputs/SS_800MP_10Myr_PSD2B_100Mearth_lorentzian/figures/mean_semimajor_axis_vs_time.png
Saved: outputs/SS_800MP_10Myr_PSD2B_100Mearth_lorentzian/figures/mean_eccentricity_vs_time.png
Saved: outputs/SS_800MP_10Myr_PSD2B_100Mearth_lorentzian/figures/rms_eccentricity_vs_time.png
Saved: outputs/SS_800MP_10Myr_PSD2B_100Mearth_lorentzian/figures/rms_inclination_vs_time.png
Saved: outputs/SS_800MP_10Myr_PSD2B_100Mearth_lorentzian/figures/data/orbits_initial_final.csv
Saved: outputs/SS_800MP_10Myr_PSD2B_100Mearth_lorentzian/figures/a_vs_e_initial_final.png
Saved: outputs/SS_800MP_10Myr_PSD2B_100Mearth_lorentzian/figures/a_vs_i_initial_final.png
Inner plotted edge = 95.04 AU
Outer plotted edge = 104.92 AU
Saved: outputs/SS_800MP_10Myr_PSD2B_100Mearth_lorentzian/figures/xy_initial_final.png
All summary figures saved.
```
