# SS_800MP_10Myr_PSD2B_500Mearth_lorentzian — Simulation Report

Config file: `config/SS_800MP_10Myr_PSD2B_500Mearth_lorentzian.yaml`
Archive file: `outputs/SS_800MP_10Myr_PSD2B_500Mearth_lorentzian/SS_800MP_10Myr_PSD2B_500Mearth_lorentzian.bin`

## Provenance

- Run UUID: `dbb0ac71-e837-48f2-be31-55395e381d5b`
- Created: 2026-10-14T17:56:22-03:00
- Finished: 2026-10-22T14:57:13-03:00
- Wall runtime: 261148.4 s
- Outcome: completed
- Command: `src/simulation/run_simulation.py config/SS_800MP_10Myr_PSD2B_500Mearth_lorentzian.yaml`
- Git commit: `c46a9348dbd0b6e8d878420e8bb4e1428d899c23` (branch `main`) **(DIRTY — uncommitted tracked changes)**
    - modified: `notebooks/mass_model_playground.ipynb`
- Software: python 3.12.14, rebound 5.0.0, numpy 2.4.6, pandas 3.0.3, matplotlib 3.10.9, pyyaml 6.0.3
- Resumed 1 time(s) after the first run
- Frozen config: `config.yaml` (this directory)
- Full environment: `environment.txt` (this directory)

## Simulation
- Name: SS_800MP_10Myr_PSD2B_500Mearth_lorentzian
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
- Final particle count: 785
- Particles lost (escaped / unbound / other removal): 17
- Archive time range: 0.000000e+00 to 1.000000e+07
- Number of snapshots: 1002

## Terminal Output

```
Saving SimulationArchive to: outputs/SS_800MP_10Myr_PSD2B_500Mearth_lorentzian/SS_800MP_10Myr_PSD2B_500Mearth_lorentzian.bin
Resuming from t=2.620000e+06 yr: times=array([ 2620000.,  2630000.,  2640000.,  2650000.,  2660000.,  2670000.,
        2680000.,  2690000.,  2700000.,  2710000.,  2720000.,  2730000.,
        2740000.,  2750000.,  2760000.,  2770000.,  2780000.,  2790000.,
        2800000.,  2810000.,  2820000.,  2830000.,  2840000.,  2850000.,
        2860000.,  2870000.,  2880000.,  2890000.,  2900000.,  2910000.,
        2920000.,  2930000.,  2940000.,  2950000.,  2960000.,  2970000.,
        2980000.,  2990000.,  3000000.,  3010000.,  3020000.,  3030000.,
        3040000.,  3050000.,  3060000.,  3070000.,  3080000.,  3090000.,
        3100000.,  3110000.,  3120000.,  3130000.,  3140000.,  3150000.,
        3160000.,  3170000.,  3180000.,  3190000.,  3200000.,  3210000.,
        3220000.,  3230000.,  3240000.,  3250000.,  3260000.,  3270000.,
        3280000.,  3290000.,  3300000.,  3310000.,  3320000.,  3330000.,
        3340000.,  3350000.,  3360000.,  3370000.,  3380000.,  3390000.,
        3400000.,  3410000.,  3420000.,  3430000.,  3440000.,  3450000.,
        3460000.,  3470000.,  3480000.,  3490000.,  3500000.,  3510000.,
        3520000.,  3530000.,  3540000.,  3550000.,  3560000.,  3570000.,
        3580000.,  3590000.,  3600000.,  3610000.,  3620000.,  3630000.,
        3640000.,  3650000.,  3660000.,  3670000.,  3680000.,  3690000.,
        3700000.,  3710000.,  3720000.,  3730000.,  3740000.,  3750000.,
        3760000.,  3770000.,  3780000.,  3790000.,  3800000.,  3810000.,
        3820000.,  3830000.,  3840000.,  3850000.,  3860000.,  3870000.,
        3880000.,  3890000.,  3900000.,  3910000.,  3920000.,  3930000.,
        3940000.,  3950000.,  3960000.,  3970000.,  3980000.,  3990000.,
        4000000.,  4010000.,  4020000.,  4030000.,  4040000.,  4050000.,
        4060000.,  4070000.,  4080000.,  4090000.,  4100000.,  4110000.,
        4120000.,  4130000.,  4140000.,  4150000.,  4160000.,  4170000.,
        4180000.,  4190000.,  4200000.,  4210000.,  4220000.,  4230000.,
        4240000.,  4250000.,  4260000.,  4270000.,  4280000.,  4290000.,
        4300000.,  4310000.,  4320000.,  4330000.,  4340000.,  4350000.,
        4360000.,  4370000.,  4380000.,  4390000.,  4400000.,  4410000.,
        4420000.,  4430000.,  4440000.,  4450000.,  4460000.,  4470000.,
        4480000.,  4490000.,  4500000.,  4510000.,  4520000.,  4530000.,
        4540000.,  4550000.,  4560000.,  4570000.,  4580000.,  4590000.,
        4600000.,  4610000.,  4620000.,  4630000.,  4640000.,  4650000.,
        4660000.,  4670000.,  4680000.,  4690000.,  4700000.,  4710000.,
        4720000.,  4730000.,  4740000.,  4750000.,  4760000.,  4770000.,
        4780000.,  4790000.,  4800000.,  4810000.,  4820000.,  4830000.,
        4840000.,  4850000.,  4860000.,  4870000.,  4880000.,  4890000.,
        4900000.,  4910000.,  4920000.,  4930000.,  4940000.,  4950000.,
        4960000.,  4970000.,  4980000.,  4990000.,  5000000.,  5010000.,
        5020000.,  5030000.,  5040000.,  5050000.,  5060000.,  5070000.,
        5080000.,  5090000.,  5100000.,  5110000.,  5120000.,  5130000.,
        5140000.,  5150000.,  5160000.,  5170000.,  5180000.,  5190000.,
        5200000.,  5210000.,  5220000.,  5230000.,  5240000.,  5250000.,
        5260000.,  5270000.,  5280000.,  5290000.,  5300000.,  5310000.,
        5320000.,  5330000.,  5340000.,  5350000.,  5360000.,  5370000.,
        5380000.,  5390000.,  5400000.,  5410000.,  5420000.,  5430000.,
        5440000.,  5450000.,  5460000.,  5470000.,  5480000.,  5490000.,
        5500000.,  5510000.,  5520000.,  5530000.,  5540000.,  5550000.,
        5560000.,  5570000.,  5580000.,  5590000.,  5600000.,  5610000.,
        5620000.,  5630000.,  5640000.,  5650000.,  5660000.,  5670000.,
        5680000.,  5690000.,  5700000.,  5710000.,  5720000.,  5730000.,
        5740000.,  5750000.,  5760000.,  5770000.,  5780000.,  5790000.,
        5800000.,  5810000.,  5820000.,  5830000.,  5840000.,  5850000.,
        5860000.,  5870000.,  5880000.,  5890000.,  5900000.,  5910000.,
        5920000.,  5930000.,  5940000.,  5950000.,  5960000.,  5970000.,
        5980000.,  5990000.,  6000000.,  6010000.,  6020000.,  6030000.,
        6040000.,  6050000.,  6060000.,  6070000.,  6080000.,  6090000.,
        6100000.,  6110000.,  6120000.,  6130000.,  6140000.,  6150000.,
        6160000.,  6170000.,  6180000.,  6190000.,  6200000.,  6210000.,
        6220000.,  6230000.,  6240000.,  6250000.,  6260000.,  6270000.,
        6280000.,  6290000.,  6300000.,  6310000.,  6320000.,  6330000.,
        6340000.,  6350000.,  6360000.,  6370000.,  6380000.,  6390000.,
        6400000.,  6410000.,  6420000.,  6430000.,  6440000.,  6450000.,
        6460000.,  6470000.,  6480000.,  6490000.,  6500000.,  6510000.,
        6520000.,  6530000.,  6540000.,  6550000.,  6560000.,  6570000.,
        6580000.,  6590000.,  6600000.,  6610000.,  6620000.,  6630000.,
        6640000.,  6650000.,  6660000.,  6670000.,  6680000.,  6690000.,
        6700000.,  6710000.,  6720000.,  6730000.,  6740000.,  6750000.,
        6760000.,  6770000.,  6780000.,  6790000.,  6800000.,  6810000.,
        6820000.,  6830000.,  6840000.,  6850000.,  6860000.,  6870000.,
        6880000.,  6890000.,  6900000.,  6910000.,  6920000.,  6930000.,
        6940000.,  6950000.,  6960000.,  6970000.,  6980000.,  6990000.,
        7000000.,  7010000.,  7020000.,  7030000.,  7040000.,  7050000.,
        7060000.,  7070000.,  7080000.,  7090000.,  7100000.,  7110000.,
        7120000.,  7130000.,  7140000.,  7150000.,  7160000.,  7170000.,
        7180000.,  7190000.,  7200000.,  7210000.,  7220000.,  7230000.,
        7240000.,  7250000.,  7260000.,  7270000.,  7280000.,  7290000.,
        7300000.,  7310000.,  7320000.,  7330000.,  7340000.,  7350000.,
        7360000.,  7370000.,  7380000.,  7390000.,  7400000.,  7410000.,
        7420000.,  7430000.,  7440000.,  7450000.,  7460000.,  7470000.,
        7480000.,  7490000.,  7500000.,  7510000.,  7520000.,  7530000.,
        7540000.,  7550000.,  7560000.,  7570000.,  7580000.,  7590000.,
        7600000.,  7610000.,  7620000.,  7630000.,  7640000.,  7650000.,
        7660000.,  7670000.,  7680000.,  7690000.,  7700000.,  7710000.,
        7720000.,  7730000.,  7740000.,  7750000.,  7760000.,  7770000.,
        7780000.,  7790000.,  7800000.,  7810000.,  7820000.,  7830000.,
        7840000.,  7850000.,  7860000.,  7870000.,  7880000.,  7890000.,
        7900000.,  7910000.,  7920000.,  7930000.,  7940000.,  7950000.,
        7960000.,  7970000.,  7980000.,  7990000.,  8000000.,  8010000.,
        8020000.,  8030000.,  8040000.,  8050000.,  8060000.,  8070000.,
        8080000.,  8090000.,  8100000.,  8110000.,  8120000.,  8130000.,
        8140000.,  8150000.,  8160000.,  8170000.,  8180000.,  8190000.,
        8200000.,  8210000.,  8220000.,  8230000.,  8240000.,  8250000.,
        8260000.,  8270000.,  8280000.,  8290000.,  8300000.,  8310000.,
        8320000.,  8330000.,  8340000.,  8350000.,  8360000.,  8370000.,
        8380000.,  8390000.,  8400000.,  8410000.,  8420000.,  8430000.,
        8440000.,  8450000.,  8460000.,  8470000.,  8480000.,  8490000.,
        8500000.,  8510000.,  8520000.,  8530000.,  8540000.,  8550000.,
        8560000.,  8570000.,  8580000.,  8590000.,  8600000.,  8610000.,
        8620000.,  8630000.,  8640000.,  8650000.,  8660000.,  8670000.,
        8680000.,  8690000.,  8700000.,  8710000.,  8720000.,  8730000.,
        8740000.,  8750000.,  8760000.,  8770000.,  8780000.,  8790000.,
        8800000.,  8810000.,  8820000.,  8830000.,  8840000.,  8850000.,
        8860000.,  8870000.,  8880000.,  8890000.,  8900000.,  8910000.,
        8920000.,  8930000.,  8940000.,  8950000.,  8960000.,  8970000.,
        8980000.,  8990000.,  9000000.,  9010000.,  9020000.,  9030000.,
        9040000.,  9050000.,  9060000.,  9070000.,  9080000.,  9090000.,
        9100000.,  9110000.,  9120000.,  9130000.,  9140000.,  9150000.,
        9160000.,  9170000.,  9180000.,  9190000.,  9200000.,  9210000.,
        9220000.,  9230000.,  9240000.,  9250000.,  9260000.,  9270000.,
        9280000.,  9290000.,  9300000.,  9310000.,  9320000.,  9330000.,
        9340000.,  9350000.,  9360000.,  9370000.,  9380000.,  9390000.,
        9400000.,  9410000.,  9420000.,  9430000.,  9440000.,  9450000.,
        9460000.,  9470000.,  9480000.,  9490000.,  9500000.,  9510000.,
        9520000.,  9530000.,  9540000.,  9550000.,  9560000.,  9570000.,
        9580000.,  9590000.,  9600000.,  9610000.,  9620000.,  9630000.,
        9640000.,  9650000.,  9660000.,  9670000.,  9680000.,  9690000.,
        9700000.,  9710000.,  9720000.,  9730000.,  9740000.,  9750000.,
        9760000.,  9770000.,  9780000.,  9790000.,  9800000.,  9810000.,
        9820000.,  9830000.,  9840000.,  9850000.,  9860000.,  9870000.,
        9880000.,  9890000.,  9900000.,  9910000.,  9920000.,  9930000.,
        9940000.,  9950000.,  9960000.,  9970000.,  9980000.,  9990000.,
       10000000.])
Found dump file. Restoring simulation from snapshot...
  Timestep: 5.607178e+01 (0.1 x giant planet orbital period = 5.607178e+02)
Restored simulation from snapshot number at t=2.620000e+06 yr with N=801 particles.

Stirrer-coverage check (Krivov & Booth 2018: N x delta_af >= delta_a):
  Stirrers inside the belt [95, 105]: N = 778
  delta_af = 8 sqrt(3) h_M a_M:  mean = 1.374968e+00, sum over stirrers = 1.069725e+03
  Belt width delta_a = 1.000000e+01
  Coverage ratio (sum delta_af / delta_a) = 106.972
  OK: stirrer feeding zones span the belt.

Beginning the main integration
Output 1/738: t=2620000.0 yr, dE/E0=0.00e+00, N=801
  Estimated time remaining to complete simulation: 1 minutes, 29 seconds
  Estimated time remaining to next output: 0 seconds
Output 2/738: t=2630000.0 yr, dE/E0=1.19e-08, N=801
  Estimated time remaining to complete simulation: 1 days, 7 hours, 8 minutes, 48 seconds
  Estimated time remaining to next output: 2 minutes, 32 seconds
Output 3/738: t=2640000.0 yr, dE/E0=1.92e-08, N=801
  Estimated time remaining to complete simulation: 1 days, 18 hours, 23 minutes, 13 seconds
  Estimated time remaining to next output: 3 minutes, 27 seconds
Output 4/738: t=2650000.0 yr, dE/E0=2.13e-08, N=801
  Estimated time remaining to complete simulation: 1 days, 23 hours, 44 minutes, 49 seconds
  Estimated time remaining to next output: 3 minutes, 54 seconds
Output 5/738: t=2660000.0 yr, dE/E0=2.23e-08, N=801
  Estimated time remaining to complete simulation: 2 days, 3 hours, 16 minutes, 26 seconds
  Estimated time remaining to next output: 4 minutes, 11 seconds
Output 6/738: t=2670000.0 yr, dE/E0=1.14e-08, N=801
  Estimated time remaining to complete simulation: 2 days, 5 hours, 23 minutes, 44 seconds
  Estimated time remaining to next output: 4 minutes, 22 seconds
Output 7/738: t=2680000.0 yr, dE/E0=2.02e-08, N=801
  Estimated time remaining to complete simulation: 2 days, 6 hours, 36 minutes, 32 seconds
  Estimated time remaining to next output: 4 minutes, 28 seconds
Output 8/738: t=2690000.0 yr, dE/E0=1.80e-09, N=801
  Estimated time remaining to complete simulation: 2 days, 8 hours, 31 seconds
  Estimated time remaining to next output: 4 minutes, 36 seconds
Output 9/738: t=2700000.0 yr, dE/E0=5.22e-10, N=801
  Estimated time remaining to complete simulation: 2 days, 8 hours, 50 minutes, 8 seconds
  Estimated time remaining to next output: 4 minutes, 40 seconds
Output 10/738: t=2710000.0 yr, dE/E0=1.17e-09, N=801
  Estimated time remaining to complete simulation: 2 days, 9 hours, 28 minutes, 28 seconds
  Estimated time remaining to next output: 4 minutes, 44 seconds
Output 11/738: t=2720000.0 yr, dE/E0=2.67e-09, N=801
  Estimated time remaining to complete simulation: 2 days, 9 hours, 45 minutes, 57 seconds
  Estimated time remaining to next output: 4 minutes, 46 seconds
Output 12/738: t=2730000.0 yr, dE/E0=5.79e-09, N=801
  Estimated time remaining to complete simulation: 2 days, 10 hours, 35 minutes, 59 seconds
  Estimated time remaining to next output: 4 minutes, 50 seconds
Output 13/738: t=2740000.0 yr, dE/E0=6.41e-09, N=801
  Estimated time remaining to complete simulation: 2 days, 10 hours, 44 minutes, 35 seconds
  Estimated time remaining to next output: 4 minutes, 51 seconds
Output 14/738: t=2750000.0 yr, dE/E0=9.93e-09, N=801
  Estimated time remaining to complete simulation: 2 days, 11 hours, 40 seconds
  Estimated time remaining to next output: 4 minutes, 53 seconds
Output 15/738: t=2760000.0 yr, dE/E0=1.69e-08, N=801
  Estimated time remaining to complete simulation: 2 days, 10 hours, 59 minutes, 5 seconds
  Estimated time remaining to next output: 4 minutes, 53 seconds
Output 16/738: t=2770000.0 yr, dE/E0=6.03e-09, N=801
  Estimated time remaining to complete simulation: 2 days, 11 hours, 11 minutes, 38 seconds
  Estimated time remaining to next output: 4 minutes, 55 seconds
Output 17/738: t=2780000.0 yr, dE/E0=9.61e-09, N=801
  Estimated time remaining to complete simulation: 2 days, 11 hours, 19 minutes, 52 seconds
  Estimated time remaining to next output: 4 minutes, 56 seconds
Output 18/738: t=2790000.0 yr, dE/E0=9.67e-09, N=801
  Estimated time remaining to complete simulation: 2 days, 11 hours, 24 minutes, 27 seconds
  Estimated time remaining to next output: 4 minutes, 57 seconds
Output 19/738: t=2800000.0 yr, dE/E0=1.81e-08, N=801
  Estimated time remaining to complete simulation: 2 days, 11 hours, 35 minutes, 59 seconds
  Estimated time remaining to next output: 4 minutes, 58 seconds
Output 20/738: t=2810000.0 yr, dE/E0=1.99e-08, N=801
  Estimated time remaining to complete simulation: 2 days, 11 hours, 44 minutes, 36 seconds
  Estimated time remaining to next output: 4 minutes, 59 seconds
Output 21/738: t=2820000.0 yr, dE/E0=1.17e-08, N=801
  Estimated time remaining to complete simulation: 2 days, 11 hours, 48 minutes, 58 seconds
  Estimated time remaining to next output: 5 minutes
Output 22/738: t=2830000.0 yr, dE/E0=1.20e-08, N=801
  Estimated time remaining to complete simulation: 2 days, 11 hours, 41 minutes, 20 seconds
  Estimated time remaining to next output: 5 minutes
Output 23/738: t=2840000.0 yr, dE/E0=1.58e-09, N=801
  Estimated time remaining to complete simulation: 2 days, 11 hours, 32 minutes, 10 seconds
  Estimated time remaining to next output: 4 minutes, 59 seconds
Output 24/738: t=2850000.0 yr, dE/E0=9.65e-10, N=801
  Estimated time remaining to complete simulation: 2 days, 11 hours, 44 minutes, 7 seconds
  Estimated time remaining to next output: 5 minutes, 1 seconds
Output 25/738: t=2860000.0 yr, dE/E0=6.84e-09, N=801
  Estimated time remaining to complete simulation: 2 days, 11 hours, 38 minutes, 20 seconds
  Estimated time remaining to next output: 5 minutes, 1 seconds
Output 26/738: t=2870000.0 yr, dE/E0=1.49e-08, N=801
  Estimated time remaining to complete simulation: 2 days, 11 hours, 43 minutes, 17 seconds
  Estimated time remaining to next output: 5 minutes, 1 seconds
Output 27/738: t=2880000.0 yr, dE/E0=1.57e-09, N=801
  Estimated time remaining to complete simulation: 2 days, 11 hours, 47 minutes, 11 seconds
  Estimated time remaining to next output: 5 minutes, 2 seconds
Output 28/738: t=2890000.0 yr, dE/E0=5.95e-09, N=801
  Estimated time remaining to complete simulation: 2 days, 11 hours, 49 minutes, 21 seconds
  Estimated time remaining to next output: 5 minutes, 3 seconds
Output 29/738: t=2900000.0 yr, dE/E0=5.54e-09, N=801
  Estimated time remaining to complete simulation: 2 days, 11 hours, 49 minutes, 40 seconds
  Estimated time remaining to next output: 5 minutes, 3 seconds
Output 30/738: t=2910000.0 yr, dE/E0=1.35e-08, N=801
  Estimated time remaining to complete simulation: 2 days, 11 hours, 53 minutes, 37 seconds
  Estimated time remaining to next output: 5 minutes, 4 seconds
Output 31/738: t=2920000.0 yr, dE/E0=3.96e-09, N=801
  Estimated time remaining to complete simulation: 2 days, 11 hours, 50 minutes, 46 seconds
  Estimated time remaining to next output: 5 minutes, 4 seconds
Output 32/738: t=2930000.0 yr, dE/E0=1.17e-09, N=801
  Estimated time remaining to complete simulation: 2 days, 11 hours, 49 minutes, 12 seconds
  Estimated time remaining to next output: 5 minutes, 5 seconds
Output 33/738: t=2940000.0 yr, dE/E0=1.70e-08, N=801
  Estimated time remaining to complete simulation: 2 days, 11 hours, 48 minutes, 11 seconds
  Estimated time remaining to next output: 5 minutes, 5 seconds
Output 34/738: t=2950000.0 yr, dE/E0=2.26e-08, N=801
  Estimated time remaining to complete simulation: 2 days, 11 hours, 42 minutes, 12 seconds
  Estimated time remaining to next output: 5 minutes, 5 seconds
Output 35/738: t=2960000.0 yr, dE/E0=1.73e-08, N=801
  Estimated time remaining to complete simulation: 2 days, 11 hours, 41 minutes, 27 seconds
  Estimated time remaining to next output: 5 minutes, 5 seconds
Output 36/738: t=2970000.0 yr, dE/E0=6.70e-09, N=801
  Estimated time remaining to complete simulation: 2 days, 11 hours, 42 minutes, 52 seconds
  Estimated time remaining to next output: 5 minutes, 6 seconds
Output 37/738: t=2980000.0 yr, dE/E0=1.22e-08, N=801
  Estimated time remaining to complete simulation: 2 days, 11 hours, 34 minutes, 55 seconds
  Estimated time remaining to next output: 5 minutes, 5 seconds
Output 38/738: t=2990000.0 yr, dE/E0=3.85e-09, N=801
  Estimated time remaining to complete simulation: 2 days, 11 hours, 26 minutes, 36 seconds
  Estimated time remaining to next output: 5 minutes, 5 seconds
Output 39/738: t=3000000.0 yr, dE/E0=3.38e-09, N=801
  Estimated time remaining to complete simulation: 2 days, 11 hours, 23 minutes, 55 seconds
  Estimated time remaining to next output: 5 minutes, 5 seconds
Output 40/738: t=3010000.0 yr, dE/E0=3.14e-09, N=801
  Estimated time remaining to complete simulation: 2 days, 11 hours, 19 minutes
  Estimated time remaining to next output: 5 minutes, 5 seconds
Output 41/738: t=3020000.0 yr, dE/E0=1.81e-09, N=801
  Estimated time remaining to complete simulation: 2 days, 11 hours, 18 minutes, 14 seconds
  Estimated time remaining to next output: 5 minutes, 6 seconds
Output 42/738: t=3030000.0 yr, dE/E0=1.33e-08, N=801
  Estimated time remaining to complete simulation: 2 days, 11 hours, 12 minutes, 25 seconds
  Estimated time remaining to next output: 5 minutes, 6 seconds
Output 43/738: t=3040000.0 yr, dE/E0=1.51e-08, N=801
  Estimated time remaining to complete simulation: 2 days, 11 hours, 9 minutes, 43 seconds
  Estimated time remaining to next output: 5 minutes, 6 seconds
Output 44/738: t=3050000.0 yr, dE/E0=5.01e-09, N=801
  Estimated time remaining to complete simulation: 2 days, 11 hours, 6 minutes, 15 seconds
  Estimated time remaining to next output: 5 minutes, 6 seconds
Output 45/738: t=3060000.0 yr, dE/E0=8.01e-09, N=801
  Estimated time remaining to complete simulation: 2 days, 11 hours, 1 minutes, 34 seconds
  Estimated time remaining to next output: 5 minutes, 6 seconds
Output 46/738: t=3070000.0 yr, dE/E0=4.30e-09, N=801
  Estimated time remaining to complete simulation: 2 days, 10 hours, 57 minutes, 26 seconds
  Estimated time remaining to next output: 5 minutes, 6 seconds
Output 47/738: t=3080000.0 yr, dE/E0=1.15e-08, N=801
  Estimated time remaining to complete simulation: 2 days, 10 hours, 59 minutes, 59 seconds
  Estimated time remaining to next output: 5 minutes, 7 seconds
Output 48/738: t=3090000.0 yr, dE/E0=6.13e-10, N=801
  Estimated time remaining to complete simulation: 2 days, 11 hours, 27 seconds
  Estimated time remaining to next output: 5 minutes, 7 seconds
Output 49/738: t=3100000.0 yr, dE/E0=4.16e-09, N=801
  Estimated time remaining to complete simulation: 2 days, 10 hours, 52 minutes, 38 seconds
  Estimated time remaining to next output: 5 minutes, 7 seconds
Output 50/738: t=3110000.0 yr, dE/E0=6.24e-09, N=801
  Estimated time remaining to complete simulation: 2 days, 10 hours, 46 minutes, 32 seconds
  Estimated time remaining to next output: 5 minutes, 7 seconds
Output 51/738: t=3120000.0 yr, dE/E0=1.17e-08, N=801
  Estimated time remaining to complete simulation: 2 days, 10 hours, 44 minutes, 39 seconds
  Estimated time remaining to next output: 5 minutes, 7 seconds
Output 52/738: t=3130000.0 yr, dE/E0=1.36e-08, N=801
  Estimated time remaining to complete simulation: 2 days, 10 hours, 40 minutes, 55 seconds
  Estimated time remaining to next output: 5 minutes, 7 seconds
Output 53/738: t=3140000.0 yr, dE/E0=2.70e-08, N=801
  Estimated time remaining to complete simulation: 2 days, 10 hours, 40 minutes, 28 seconds
  Estimated time remaining to next output: 5 minutes, 8 seconds
Output 54/738: t=3150000.0 yr, dE/E0=1.73e-08, N=801
  Estimated time remaining to complete simulation: 2 days, 10 hours, 36 minutes, 31 seconds
  Estimated time remaining to next output: 5 minutes, 8 seconds
Output 55/738: t=3160000.0 yr, dE/E0=1.54e-08, N=801
  Estimated time remaining to complete simulation: 2 days, 10 hours, 30 minutes, 36 seconds
  Estimated time remaining to next output: 5 minutes, 8 seconds
Output 56/738: t=3170000.0 yr, dE/E0=7.71e-09, N=801
  Estimated time remaining to complete simulation: 2 days, 10 hours, 25 minutes, 42 seconds
  Estimated time remaining to next output: 5 minutes, 8 seconds
Output 57/738: t=3180000.0 yr, dE/E0=4.83e-09, N=801
  Estimated time remaining to complete simulation: 2 days, 10 hours, 19 minutes, 39 seconds
  Estimated time remaining to next output: 5 minutes, 8 seconds
Output 58/738: t=3190000.0 yr, dE/E0=8.97e-09, N=801
  Estimated time remaining to complete simulation: 2 days, 10 hours, 16 minutes, 6 seconds
  Estimated time remaining to next output: 5 minutes, 8 seconds
Output 59/738: t=3200000.0 yr, dE/E0=2.41e-08, N=801
  Estimated time remaining to complete simulation: 2 days, 10 hours, 11 minutes, 16 seconds
  Estimated time remaining to next output: 5 minutes, 8 seconds
Output 60/738: t=3210000.0 yr, dE/E0=6.01e-09, N=801
  Estimated time remaining to complete simulation: 2 days, 10 hours, 4 minutes, 50 seconds
  Estimated time remaining to next output: 5 minutes, 8 seconds
Output 61/738: t=3220000.0 yr, dE/E0=2.88e-09, N=801
  Estimated time remaining to complete simulation: 2 days, 10 hours, 56 seconds
  Estimated time remaining to next output: 5 minutes, 8 seconds
Output 62/738: t=3230000.0 yr, dE/E0=9.07e-09, N=801
  Estimated time remaining to complete simulation: 2 days, 10 hours, 50 seconds
  Estimated time remaining to next output: 5 minutes, 8 seconds
Output 63/738: t=3240000.0 yr, dE/E0=1.23e-08, N=801
  Estimated time remaining to complete simulation: 2 days, 9 hours, 57 minutes, 32 seconds
  Estimated time remaining to next output: 5 minutes, 9 seconds
Output 64/738: t=3250000.0 yr, dE/E0=2.24e-08, N=801
  Estimated time remaining to complete simulation: 2 days, 9 hours, 52 minutes, 51 seconds
  Estimated time remaining to next output: 5 minutes, 9 seconds
Output 65/738: t=3260000.0 yr, dE/E0=8.68e-09, N=801
  Estimated time remaining to complete simulation: 2 days, 9 hours, 52 minutes, 38 seconds
  Estimated time remaining to next output: 5 minutes, 9 seconds
Output 66/738: t=3270000.0 yr, dE/E0=1.91e-08, N=801
  Estimated time remaining to complete simulation: 2 days, 9 hours, 46 minutes, 43 seconds
  Estimated time remaining to next output: 5 minutes, 9 seconds
Output 67/738: t=3280000.0 yr, dE/E0=5.53e-09, N=801
  Estimated time remaining to complete simulation: 2 days, 9 hours, 41 minutes, 58 seconds
  Estimated time remaining to next output: 5 minutes, 9 seconds
Output 68/738: t=3290000.0 yr, dE/E0=1.80e-08, N=801
  Estimated time remaining to complete simulation: 2 days, 9 hours, 36 minutes, 30 seconds
  Estimated time remaining to next output: 5 minutes, 9 seconds
Output 69/738: t=3300000.0 yr, dE/E0=1.76e-08, N=801
  Estimated time remaining to complete simulation: 2 days, 9 hours, 28 minutes, 55 seconds
  Estimated time remaining to next output: 5 minutes, 9 seconds
Output 70/738: t=3310000.0 yr, dE/E0=2.38e-08, N=801
  Estimated time remaining to complete simulation: 2 days, 9 hours, 28 minutes, 53 seconds
  Estimated time remaining to next output: 5 minutes, 9 seconds
Output 71/738: t=3320000.0 yr, dE/E0=3.05e-08, N=801
  Estimated time remaining to complete simulation: 2 days, 9 hours, 23 minutes, 17 seconds
  Estimated time remaining to next output: 5 minutes, 9 seconds
Output 72/738: t=3330000.0 yr, dE/E0=1.36e-08, N=801
  Estimated time remaining to complete simulation: 2 days, 9 hours, 23 minutes, 51 seconds
  Estimated time remaining to next output: 5 minutes, 10 seconds
Output 73/738: t=3340000.0 yr, dE/E0=6.06e-09, N=801
  Estimated time remaining to complete simulation: 2 days, 9 hours, 22 minutes, 25 seconds
  Estimated time remaining to next output: 5 minutes, 10 seconds
Output 74/738: t=3350000.0 yr, dE/E0=1.35e-10, N=801
  Estimated time remaining to complete simulation: 2 days, 9 hours, 21 minutes, 9 seconds
  Estimated time remaining to next output: 5 minutes, 10 seconds
Output 75/738: t=3360000.0 yr, dE/E0=8.30e-09, N=801
  Estimated time remaining to complete simulation: 2 days, 9 hours, 15 minutes, 58 seconds
  Estimated time remaining to next output: 5 minutes, 10 seconds
Output 76/738: t=3370000.0 yr, dE/E0=1.30e-08, N=801
  Estimated time remaining to complete simulation: 2 days, 9 hours, 9 minutes, 47 seconds
  Estimated time remaining to next output: 5 minutes, 10 seconds
Output 77/738: t=3380000.0 yr, dE/E0=1.56e-08, N=801
  Estimated time remaining to complete simulation: 2 days, 9 hours, 4 minutes, 25 seconds
  Estimated time remaining to next output: 5 minutes, 10 seconds
Output 78/738: t=3390000.0 yr, dE/E0=1.62e-08, N=801
  Estimated time remaining to complete simulation: 2 days, 8 hours, 59 minutes, 2 seconds
  Estimated time remaining to next output: 5 minutes, 10 seconds
Output 79/738: t=3400000.0 yr, dE/E0=1.09e-08, N=801
  Estimated time remaining to complete simulation: 2 days, 8 hours, 56 minutes, 33 seconds
  Estimated time remaining to next output: 5 minutes, 11 seconds
Output 80/738: t=3410000.0 yr, dE/E0=1.09e-08, N=801
  Estimated time remaining to complete simulation: 2 days, 8 hours, 48 minutes, 51 seconds
  Estimated time remaining to next output: 5 minutes, 10 seconds
Output 81/738: t=3420000.0 yr, dE/E0=1.47e-08, N=801
  Estimated time remaining to complete simulation: 2 days, 8 hours, 45 minutes, 7 seconds
  Estimated time remaining to next output: 5 minutes, 10 seconds
Output 82/738: t=3430000.0 yr, dE/E0=1.45e-08, N=801
  Estimated time remaining to complete simulation: 2 days, 8 hours, 42 minutes, 35 seconds
  Estimated time remaining to next output: 5 minutes, 11 seconds
Output 83/738: t=3440000.0 yr, dE/E0=2.26e-08, N=801
  Estimated time remaining to complete simulation: 2 days, 8 hours, 35 minutes, 56 seconds
  Estimated time remaining to next output: 5 minutes, 11 seconds
Output 84/738: t=3450000.0 yr, dE/E0=1.78e-09, N=801
  Estimated time remaining to complete simulation: 2 days, 8 hours, 30 minutes, 42 seconds
  Estimated time remaining to next output: 5 minutes, 11 seconds
Output 85/738: t=3460000.0 yr, dE/E0=4.67e-09, N=801
  Estimated time remaining to complete simulation: 2 days, 8 hours, 28 minutes, 35 seconds
  Estimated time remaining to next output: 5 minutes, 11 seconds
Output 86/738: t=3470000.0 yr, dE/E0=7.72e-09, N=801
  Estimated time remaining to complete simulation: 2 days, 8 hours, 23 minutes, 16 seconds
  Estimated time remaining to next output: 5 minutes, 11 seconds
Output 87/738: t=3480000.0 yr, dE/E0=9.74e-09, N=801
  Estimated time remaining to complete simulation: 2 days, 8 hours, 19 minutes, 55 seconds
  Estimated time remaining to next output: 5 minutes, 11 seconds
Output 88/738: t=3490000.0 yr, dE/E0=2.64e-09, N=801
  Estimated time remaining to complete simulation: 2 days, 8 hours, 16 minutes, 32 seconds
  Estimated time remaining to next output: 5 minutes, 11 seconds
Output 89/738: t=3500000.0 yr, dE/E0=1.23e-08, N=801
  Estimated time remaining to complete simulation: 2 days, 8 hours, 11 minutes, 38 seconds
  Estimated time remaining to next output: 5 minutes, 11 seconds
Output 90/738: t=3510000.0 yr, dE/E0=1.40e-10, N=801
  Estimated time remaining to complete simulation: 2 days, 8 hours, 4 minutes, 55 seconds
  Estimated time remaining to next output: 5 minutes, 11 seconds
Output 91/738: t=3520000.0 yr, dE/E0=1.74e-08, N=801
  Estimated time remaining to complete simulation: 2 days, 7 hours, 59 minutes, 36 seconds
  Estimated time remaining to next output: 5 minutes, 11 seconds
Output 92/738: t=3530000.0 yr, dE/E0=1.76e-10, N=801
  Estimated time remaining to complete simulation: 2 days, 7 hours, 53 minutes, 48 seconds
  Estimated time remaining to next output: 5 minutes, 11 seconds
Output 93/738: t=3540000.0 yr, dE/E0=1.21e-08, N=801
  Estimated time remaining to complete simulation: 2 days, 7 hours, 51 minutes, 10 seconds
  Estimated time remaining to next output: 5 minutes, 11 seconds
Output 94/738: t=3550000.0 yr, dE/E0=1.32e-08, N=801
  Estimated time remaining to complete simulation: 2 days, 7 hours, 45 minutes, 43 seconds
  Estimated time remaining to next output: 5 minutes, 11 seconds
Output 95/738: t=3560000.0 yr, dE/E0=2.66e-08, N=801
  Estimated time remaining to complete simulation: 2 days, 7 hours, 40 minutes, 27 seconds
  Estimated time remaining to next output: 5 minutes, 11 seconds
Output 96/738: t=3570000.0 yr, dE/E0=2.46e-08, N=801
  Estimated time remaining to complete simulation: 2 days, 7 hours, 34 minutes, 19 seconds
  Estimated time remaining to next output: 5 minutes, 11 seconds
Output 97/738: t=3580000.0 yr, dE/E0=2.17e-08, N=801
  Estimated time remaining to complete simulation: 2 days, 7 hours, 30 minutes, 34 seconds
  Estimated time remaining to next output: 5 minutes, 11 seconds
Output 98/738: t=3590000.0 yr, dE/E0=1.85e-08, N=801
  Estimated time remaining to complete simulation: 2 days, 7 hours, 26 minutes, 56 seconds
  Estimated time remaining to next output: 5 minutes, 11 seconds
Output 99/738: t=3600000.0 yr, dE/E0=2.54e-08, N=801
  Estimated time remaining to complete simulation: 2 days, 7 hours, 22 minutes, 14 seconds
  Estimated time remaining to next output: 5 minutes, 11 seconds
Output 100/738: t=3610000.0 yr, dE/E0=3.69e-08, N=801
  Estimated time remaining to complete simulation: 2 days, 7 hours, 19 minutes, 13 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 101/738: t=3620000.0 yr, dE/E0=4.14e-08, N=801
  Estimated time remaining to complete simulation: 2 days, 7 hours, 14 minutes, 34 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 102/738: t=3630000.0 yr, dE/E0=4.31e-08, N=801
  Estimated time remaining to complete simulation: 2 days, 7 hours, 10 minutes, 38 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 103/738: t=3640000.0 yr, dE/E0=3.34e-08, N=801
  Estimated time remaining to complete simulation: 2 days, 7 hours, 6 minutes, 34 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 104/738: t=3650000.0 yr, dE/E0=2.38e-08, N=801
  Estimated time remaining to complete simulation: 2 days, 7 hours, 49 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 105/738: t=3660000.0 yr, dE/E0=3.04e-08, N=801
  Estimated time remaining to complete simulation: 2 days, 6 hours, 56 minutes, 32 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 106/738: t=3670000.0 yr, dE/E0=4.53e-08, N=801
  Estimated time remaining to complete simulation: 2 days, 6 hours, 53 minutes, 36 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 107/738: t=3680000.0 yr, dE/E0=4.55e-08, N=801
  Estimated time remaining to complete simulation: 2 days, 6 hours, 51 minutes, 11 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 108/738: t=3690000.0 yr, dE/E0=3.15e-08, N=801
  Estimated time remaining to complete simulation: 2 days, 6 hours, 45 minutes, 31 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 109/738: t=3700000.0 yr, dE/E0=3.13e-08, N=801
  Estimated time remaining to complete simulation: 2 days, 6 hours, 40 minutes, 27 seconds
  Estimated time remaining to next output: 5 minutes, 12 seconds
Output 110/738: t=3710000.0 yr, dE/E0=2.77e-08, N=801
  Estimated time remaining to complete simulation: 2 days, 6 hours, 36 minutes, 50 seconds
  Estimated time remaining to next output: 5 minutes, 13 seconds
Output 111/738: t=3720000.0 yr, dE/E0=4.52e-08, N=801
  Estimated time remaining to complete simulation: 2 days, 6 hours, 32 minutes, 11 seconds
  Estimated time remaining to next output: 5 minutes, 13 seconds
Output 112/738: t=3730000.0 yr, dE/E0=4.90e-08, N=801
  Estimated time remaining to complete simulation: 2 days, 6 hours, 28 minutes, 26 seconds
  Estimated time remaining to next output: 5 minutes, 13 seconds
Output 113/738: t=3740000.0 yr, dE/E0=5.17e-08, N=801
  Estimated time remaining to complete simulation: 2 days, 6 hours, 22 minutes, 5 seconds
  Estimated time remaining to next output: 5 minutes, 13 seconds
Output 114/738: t=3750000.0 yr, dE/E0=4.08e-08, N=801
  Estimated time remaining to complete simulation: 2 days, 6 hours, 17 minutes, 23 seconds
  Estimated time remaining to next output: 5 minutes, 13 seconds
Output 115/738: t=3760000.0 yr, dE/E0=4.05e-08, N=801
  Estimated time remaining to complete simulation: 2 days, 6 hours, 12 minutes, 24 seconds
  Estimated time remaining to next output: 5 minutes, 13 seconds
Output 116/738: t=3770000.0 yr, dE/E0=4.00e-08, N=801
  Estimated time remaining to complete simulation: 2 days, 6 hours, 7 minutes, 49 seconds
  Estimated time remaining to next output: 5 minutes, 13 seconds
Output 117/738: t=3780000.0 yr, dE/E0=2.47e-08, N=801
  Estimated time remaining to complete simulation: 2 days, 6 hours, 2 minutes, 54 seconds
  Estimated time remaining to next output: 5 minutes, 13 seconds
Output 118/738: t=3790000.0 yr, dE/E0=4.81e-08, N=801
  Estimated time remaining to complete simulation: 2 days, 5 hours, 58 minutes, 8 seconds
  Estimated time remaining to next output: 5 minutes, 13 seconds
Output 119/738: t=3800000.0 yr, dE/E0=3.34e-08, N=801
  Estimated time remaining to complete simulation: 2 days, 5 hours, 53 minutes, 9 seconds
  Estimated time remaining to next output: 5 minutes, 13 seconds
Output 120/738: t=3810000.0 yr, dE/E0=2.02e-08, N=801
  Estimated time remaining to complete simulation: 2 days, 5 hours, 49 minutes, 13 seconds
  Estimated time remaining to next output: 5 minutes, 13 seconds
Output 121/738: t=3820000.0 yr, dE/E0=1.66e-08, N=801
  Estimated time remaining to complete simulation: 2 days, 5 hours, 44 minutes, 9 seconds
  Estimated time remaining to next output: 5 minutes, 13 seconds
Output 122/738: t=3830000.0 yr, dE/E0=2.05e-08, N=801
  Estimated time remaining to complete simulation: 2 days, 5 hours, 38 minutes, 17 seconds
  Estimated time remaining to next output: 5 minutes, 13 seconds
Output 123/738: t=3840000.0 yr, dE/E0=3.72e-08, N=801
  Estimated time remaining to complete simulation: 2 days, 5 hours, 32 minutes, 25 seconds
  Estimated time remaining to next output: 5 minutes, 13 seconds
Output 124/738: t=3850000.0 yr, dE/E0=2.73e-08, N=801
  Estimated time remaining to complete simulation: 2 days, 5 hours, 26 minutes, 26 seconds
  Estimated time remaining to next output: 5 minutes, 13 seconds
Output 125/738: t=3860000.0 yr, dE/E0=3.84e-08, N=801
  Estimated time remaining to complete simulation: 2 days, 5 hours, 22 minutes, 18 seconds
  Estimated time remaining to next output: 5 minutes, 13 seconds
Output 126/738: t=3870000.0 yr, dE/E0=3.62e-08, N=801
  Estimated time remaining to complete simulation: 2 days, 5 hours, 17 minutes, 24 seconds
  Estimated time remaining to next output: 5 minutes, 13 seconds
Output 127/738: t=3880000.0 yr, dE/E0=2.01e-08, N=801
  Estimated time remaining to complete simulation: 2 days, 5 hours, 12 minutes, 34 seconds
  Estimated time remaining to next output: 5 minutes, 13 seconds
Output 128/738: t=3890000.0 yr, dE/E0=1.24e-08, N=801
  Estimated time remaining to complete simulation: 2 days, 5 hours, 8 minutes, 35 seconds
  Estimated time remaining to next output: 5 minutes, 13 seconds
Output 129/738: t=3900000.0 yr, dE/E0=2.34e-08, N=801
  Estimated time remaining to complete simulation: 2 days, 5 hours, 3 minutes, 51 seconds
  Estimated time remaining to next output: 5 minutes, 13 seconds
Output 130/738: t=3910000.0 yr, dE/E0=3.30e-08, N=801
  Estimated time remaining to complete simulation: 2 days, 4 hours, 58 minutes, 18 seconds
  Estimated time remaining to next output: 5 minutes, 13 seconds
Output 131/738: t=3920000.0 yr, dE/E0=3.93e-08, N=801
  Estimated time remaining to complete simulation: 2 days, 4 hours, 53 minutes, 58 seconds
  Estimated time remaining to next output: 5 minutes, 13 seconds
Output 132/738: t=3930000.0 yr, dE/E0=3.32e-08, N=801
  Estimated time remaining to complete simulation: 2 days, 4 hours, 50 minutes, 36 seconds
  Estimated time remaining to next output: 5 minutes, 13 seconds
Output 133/738: t=3940000.0 yr, dE/E0=3.09e-08, N=801
  Estimated time remaining to complete simulation: 2 days, 4 hours, 45 minutes, 37 seconds
  Estimated time remaining to next output: 5 minutes, 13 seconds
Output 134/738: t=3950000.0 yr, dE/E0=2.94e-08, N=801
  Estimated time remaining to complete simulation: 2 days, 4 hours, 39 minutes, 52 seconds
  Estimated time remaining to next output: 5 minutes, 13 seconds
A particle escaped (r>exit_max_distance).
Removing escaped particle at index 692
Remaining particles: 800
Output 135/738: t=3957345.4 yr, dE/E0=5.90e-08, N=800
  Estimated time remaining to complete simulation: 2 days, 4 hours, 29 minutes, 18 seconds
  Estimated time remaining to next output: 5 minutes, 13 seconds
Output 136/738: t=3970000.0 yr, dE/E0=4.71e-08, N=800
  Estimated time remaining to complete simulation: 2 days, 4 hours, 29 minutes, 31 seconds
  Estimated time remaining to next output: 5 minutes, 13 seconds
Output 137/738: t=3980000.0 yr, dE/E0=5.06e-08, N=800
  Estimated time remaining to complete simulation: 2 days, 4 hours, 25 minutes, 46 seconds
  Estimated time remaining to next output: 5 minutes, 14 seconds
Output 138/738: t=3990000.0 yr, dE/E0=4.27e-08, N=800
  Estimated time remaining to complete simulation: 2 days, 4 hours, 21 minutes, 40 seconds
  Estimated time remaining to next output: 5 minutes, 14 seconds
Output 139/738: t=4000000.0 yr, dE/E0=5.40e-08, N=800
  Estimated time remaining to complete simulation: 2 days, 4 hours, 17 minutes, 3 seconds
  Estimated time remaining to next output: 5 minutes, 14 seconds
Output 140/738: t=4010000.0 yr, dE/E0=6.55e-08, N=800
  Estimated time remaining to complete simulation: 2 days, 4 hours, 13 minutes, 14 seconds
  Estimated time remaining to next output: 5 minutes, 14 seconds
Output 141/738: t=4020000.0 yr, dE/E0=5.26e-08, N=800
  Estimated time remaining to complete simulation: 2 days, 4 hours, 8 minutes, 52 seconds
  Estimated time remaining to next output: 5 minutes, 14 seconds
Output 142/738: t=4030000.0 yr, dE/E0=4.05e-08, N=800
  Estimated time remaining to complete simulation: 2 days, 4 hours, 12 minutes, 39 seconds
  Estimated time remaining to next output: 5 minutes, 15 seconds
Output 143/738: t=4040000.0 yr, dE/E0=4.30e-08, N=800
  Estimated time remaining to complete simulation: 2 days, 4 hours, 22 minutes, 1 seconds
  Estimated time remaining to next output: 5 minutes, 16 seconds
Output 144/738: t=4050000.0 yr, dE/E0=5.11e-08, N=800
  Estimated time remaining to complete simulation: 2 days, 4 hours, 30 minutes, 43 seconds
  Estimated time remaining to next output: 5 minutes, 18 seconds
Output 145/738: t=4060000.0 yr, dE/E0=7.16e-08, N=800
  Estimated time remaining to complete simulation: 2 days, 4 hours, 39 minutes, 1 seconds
  Estimated time remaining to next output: 5 minutes, 19 seconds
Output 146/738: t=4070000.0 yr, dE/E0=6.88e-08, N=800
  Estimated time remaining to complete simulation: 2 days, 4 hours, 46 minutes, 28 seconds
  Estimated time remaining to next output: 5 minutes, 20 seconds
Output 147/738: t=4080000.0 yr, dE/E0=6.78e-08, N=800
  Estimated time remaining to complete simulation: 2 days, 4 hours, 54 minutes, 17 seconds
  Estimated time remaining to next output: 5 minutes, 22 seconds
Output 148/738: t=4090000.0 yr, dE/E0=6.45e-08, N=800
  Estimated time remaining to complete simulation: 2 days, 5 hours, 1 minutes, 38 seconds
  Estimated time remaining to next output: 5 minutes, 23 seconds
Output 149/738: t=4100000.0 yr, dE/E0=6.86e-08, N=800
  Estimated time remaining to complete simulation: 2 days, 5 hours, 8 minutes, 12 seconds
  Estimated time remaining to next output: 5 minutes, 24 seconds
Output 150/738: t=4110000.0 yr, dE/E0=6.44e-08, N=800
  Estimated time remaining to complete simulation: 2 days, 5 hours, 16 minutes, 43 seconds
  Estimated time remaining to next output: 5 minutes, 26 seconds
Output 151/738: t=4120000.0 yr, dE/E0=7.31e-08, N=800
  Estimated time remaining to complete simulation: 2 days, 5 hours, 23 minutes, 38 seconds
  Estimated time remaining to next output: 5 minutes, 27 seconds
Output 152/738: t=4130000.0 yr, dE/E0=8.08e-08, N=800
  Estimated time remaining to complete simulation: 2 days, 5 hours, 29 minutes, 46 seconds
  Estimated time remaining to next output: 5 minutes, 28 seconds
Output 153/738: t=4140000.0 yr, dE/E0=9.38e-08, N=800
  Estimated time remaining to complete simulation: 2 days, 5 hours, 36 minutes, 28 seconds
  Estimated time remaining to next output: 5 minutes, 29 seconds
Output 154/738: t=4150000.0 yr, dE/E0=7.06e-08, N=800
  Estimated time remaining to complete simulation: 2 days, 5 hours, 43 minutes, 31 seconds
  Estimated time remaining to next output: 5 minutes, 31 seconds
Output 155/738: t=4160000.0 yr, dE/E0=7.61e-08, N=800
  Estimated time remaining to complete simulation: 2 days, 5 hours, 50 minutes, 27 seconds
  Estimated time remaining to next output: 5 minutes, 32 seconds
Output 156/738: t=4170000.0 yr, dE/E0=8.58e-08, N=800
  Estimated time remaining to complete simulation: 2 days, 5 hours, 58 minutes, 28 seconds
  Estimated time remaining to next output: 5 minutes, 33 seconds
Output 157/738: t=4180000.0 yr, dE/E0=8.07e-08, N=800
  Estimated time remaining to complete simulation: 2 days, 6 hours, 3 minutes, 24 seconds
  Estimated time remaining to next output: 5 minutes, 34 seconds
Output 158/738: t=4190000.0 yr, dE/E0=9.54e-08, N=800
  Estimated time remaining to complete simulation: 2 days, 6 hours, 9 minutes, 45 seconds
  Estimated time remaining to next output: 5 minutes, 36 seconds
Output 159/738: t=4200000.0 yr, dE/E0=1.02e-07, N=800
  Estimated time remaining to complete simulation: 2 days, 6 hours, 15 minutes, 58 seconds
  Estimated time remaining to next output: 5 minutes, 37 seconds
Output 160/738: t=4210000.0 yr, dE/E0=1.02e-07, N=800
  Estimated time remaining to complete simulation: 2 days, 6 hours, 20 minutes, 56 seconds
  Estimated time remaining to next output: 5 minutes, 38 seconds
A particle escaped (r>exit_max_distance).
Removing escaped particle at index 458
Remaining particles: 799
Output 161/738: t=4217009.0 yr, dE/E0=2.52e-07, N=799
  Estimated time remaining to complete simulation: 2 days, 6 hours, 16 minutes, 28 seconds
  Estimated time remaining to next output: 5 minutes, 38 seconds
Output 162/738: t=4230000.0 yr, dE/E0=2.37e-07, N=799
  Estimated time remaining to complete simulation: 2 days, 6 hours, 30 minutes, 17 seconds
  Estimated time remaining to next output: 5 minutes, 40 seconds
Output 163/738: t=4240000.0 yr, dE/E0=2.37e-07, N=799
  Estimated time remaining to complete simulation: 2 days, 6 hours, 35 minutes, 40 seconds
  Estimated time remaining to next output: 5 minutes, 41 seconds
Output 164/738: t=4250000.0 yr, dE/E0=2.51e-07, N=799
  Estimated time remaining to complete simulation: 2 days, 6 hours, 39 minutes, 36 seconds
  Estimated time remaining to next output: 5 minutes, 42 seconds
Output 165/738: t=4260000.0 yr, dE/E0=2.49e-07, N=799
  Estimated time remaining to complete simulation: 2 days, 6 hours, 45 minutes, 2 seconds
  Estimated time remaining to next output: 5 minutes, 43 seconds
Output 166/738: t=4270000.0 yr, dE/E0=2.37e-07, N=799
  Estimated time remaining to complete simulation: 2 days, 6 hours, 49 minutes, 19 seconds
  Estimated time remaining to next output: 5 minutes, 45 seconds
Output 167/738: t=4280000.0 yr, dE/E0=2.60e-07, N=799
  Estimated time remaining to complete simulation: 2 days, 6 hours, 54 minutes, 3 seconds
  Estimated time remaining to next output: 5 minutes, 46 seconds
Output 168/738: t=4290000.0 yr, dE/E0=2.56e-07, N=799
  Estimated time remaining to complete simulation: 2 days, 6 hours, 57 minutes, 33 seconds
  Estimated time remaining to next output: 5 minutes, 47 seconds
Output 169/738: t=4300000.0 yr, dE/E0=2.55e-07, N=799
  Estimated time remaining to complete simulation: 2 days, 7 hours, 2 minutes, 9 seconds
  Estimated time remaining to next output: 5 minutes, 48 seconds
Output 170/738: t=4310000.0 yr, dE/E0=2.63e-07, N=799
  Estimated time remaining to complete simulation: 2 days, 7 hours, 5 minutes, 24 seconds
  Estimated time remaining to next output: 5 minutes, 49 seconds
Output 171/738: t=4320000.0 yr, dE/E0=2.64e-07, N=799
  Estimated time remaining to complete simulation: 2 days, 7 hours, 9 minutes, 49 seconds
  Estimated time remaining to next output: 5 minutes, 50 seconds
Output 172/738: t=4330000.0 yr, dE/E0=2.35e-07, N=799
  Estimated time remaining to complete simulation: 2 days, 7 hours, 12 minutes, 18 seconds
  Estimated time remaining to next output: 5 minutes, 51 seconds
Output 173/738: t=4340000.0 yr, dE/E0=2.29e-07, N=799
  Estimated time remaining to complete simulation: 2 days, 7 hours, 15 minutes, 35 seconds
  Estimated time remaining to next output: 5 minutes, 52 seconds
Output 174/738: t=4350000.0 yr, dE/E0=2.39e-07, N=799
  Estimated time remaining to complete simulation: 2 days, 7 hours, 17 minutes, 3 seconds
  Estimated time remaining to next output: 5 minutes, 52 seconds
Output 175/738: t=4360000.0 yr, dE/E0=2.60e-07, N=799
  Estimated time remaining to complete simulation: 2 days, 7 hours, 19 minutes, 11 seconds
  Estimated time remaining to next output: 5 minutes, 53 seconds
Output 176/738: t=4370000.0 yr, dE/E0=2.61e-07, N=799
  Estimated time remaining to complete simulation: 2 days, 7 hours, 23 minutes, 1 seconds
  Estimated time remaining to next output: 5 minutes, 54 seconds
Output 177/738: t=4380000.0 yr, dE/E0=2.63e-07, N=799
  Estimated time remaining to complete simulation: 2 days, 7 hours, 25 minutes, 54 seconds
  Estimated time remaining to next output: 5 minutes, 55 seconds
Output 178/738: t=4390000.0 yr, dE/E0=2.44e-07, N=799
  Estimated time remaining to complete simulation: 2 days, 7 hours, 28 minutes, 35 seconds
  Estimated time remaining to next output: 5 minutes, 56 seconds
Output 179/738: t=4400000.0 yr, dE/E0=2.40e-07, N=799
  Estimated time remaining to complete simulation: 2 days, 7 hours, 24 minutes, 12 seconds
  Estimated time remaining to next output: 5 minutes, 56 seconds
Output 180/738: t=4410000.0 yr, dE/E0=2.33e-07, N=799
  Estimated time remaining to complete simulation: 2 days, 7 hours, 18 minutes, 14 seconds
  Estimated time remaining to next output: 5 minutes, 56 seconds
Output 181/738: t=4420000.0 yr, dE/E0=2.54e-07, N=799
  Estimated time remaining to complete simulation: 2 days, 7 hours, 9 minutes, 58 seconds
  Estimated time remaining to next output: 5 minutes, 56 seconds
Output 182/738: t=4430000.0 yr, dE/E0=2.67e-07, N=799
  Estimated time remaining to complete simulation: 2 days, 7 hours, 3 minutes, 5 seconds
  Estimated time remaining to next output: 5 minutes, 56 seconds
Output 183/738: t=4440000.0 yr, dE/E0=2.63e-07, N=799
  Estimated time remaining to complete simulation: 2 days, 6 hours, 56 minutes, 7 seconds
  Estimated time remaining to next output: 5 minutes, 56 seconds
Output 184/738: t=4450000.0 yr, dE/E0=2.50e-07, N=799
  Estimated time remaining to complete simulation: 2 days, 6 hours, 48 minutes, 16 seconds
  Estimated time remaining to next output: 5 minutes, 56 seconds
Output 185/738: t=4460000.0 yr, dE/E0=2.40e-07, N=799
  Estimated time remaining to complete simulation: 2 days, 6 hours, 40 minutes, 18 seconds
  Estimated time remaining to next output: 5 minutes, 55 seconds
Output 186/738: t=4470000.0 yr, dE/E0=2.36e-07, N=799
  Estimated time remaining to complete simulation: 2 days, 6 hours, 32 minutes, 39 seconds
  Estimated time remaining to next output: 5 minutes, 55 seconds
Output 187/738: t=4480000.0 yr, dE/E0=2.51e-07, N=799
  Estimated time remaining to complete simulation: 2 days, 6 hours, 25 minutes, 33 seconds
  Estimated time remaining to next output: 5 minutes, 55 seconds
Output 188/738: t=4490000.0 yr, dE/E0=2.48e-07, N=799
  Estimated time remaining to complete simulation: 2 days, 6 hours, 18 minutes, 10 seconds
  Estimated time remaining to next output: 5 minutes, 55 seconds
Output 189/738: t=4500000.0 yr, dE/E0=2.64e-07, N=799
  Estimated time remaining to complete simulation: 2 days, 6 hours, 10 minutes, 20 seconds
  Estimated time remaining to next output: 5 minutes, 55 seconds
Output 190/738: t=4510000.0 yr, dE/E0=2.58e-07, N=799
  Estimated time remaining to complete simulation: 2 days, 6 hours, 2 minutes, 47 seconds
  Estimated time remaining to next output: 5 minutes, 55 seconds
Output 191/738: t=4520000.0 yr, dE/E0=2.52e-07, N=799
  Estimated time remaining to complete simulation: 2 days, 5 hours, 54 minutes, 29 seconds
  Estimated time remaining to next output: 5 minutes, 54 seconds
Output 192/738: t=4530000.0 yr, dE/E0=2.58e-07, N=799
  Estimated time remaining to complete simulation: 2 days, 5 hours, 46 minutes, 46 seconds
  Estimated time remaining to next output: 5 minutes, 54 seconds
Output 193/738: t=4540000.0 yr, dE/E0=2.70e-07, N=799
  Estimated time remaining to complete simulation: 2 days, 5 hours, 39 minutes, 29 seconds
  Estimated time remaining to next output: 5 minutes, 54 seconds
Output 194/738: t=4550000.0 yr, dE/E0=2.74e-07, N=799
  Estimated time remaining to complete simulation: 2 days, 5 hours, 32 minutes, 12 seconds
  Estimated time remaining to next output: 5 minutes, 54 seconds
Output 195/738: t=4560000.0 yr, dE/E0=2.69e-07, N=799
  Estimated time remaining to complete simulation: 2 days, 5 hours, 25 minutes, 21 seconds
  Estimated time remaining to next output: 5 minutes, 54 seconds
Output 196/738: t=4570000.0 yr, dE/E0=2.57e-07, N=799
  Estimated time remaining to complete simulation: 2 days, 5 hours, 17 minutes, 16 seconds
  Estimated time remaining to next output: 5 minutes, 53 seconds
Output 197/738: t=4580000.0 yr, dE/E0=2.46e-07, N=799
  Estimated time remaining to complete simulation: 2 days, 5 hours, 9 minutes, 9 seconds
  Estimated time remaining to next output: 5 minutes, 53 seconds
Output 198/738: t=4590000.0 yr, dE/E0=2.58e-07, N=799
  Estimated time remaining to complete simulation: 2 days, 5 hours, 1 minutes, 23 seconds
  Estimated time remaining to next output: 5 minutes, 53 seconds
Output 199/738: t=4600000.0 yr, dE/E0=2.59e-07, N=799
  Estimated time remaining to complete simulation: 2 days, 4 hours, 53 minutes, 42 seconds
  Estimated time remaining to next output: 5 minutes, 53 seconds
Output 200/738: t=4610000.0 yr, dE/E0=2.59e-07, N=799
  Estimated time remaining to complete simulation: 2 days, 4 hours, 45 minutes, 47 seconds
  Estimated time remaining to next output: 5 minutes, 53 seconds
Output 201/738: t=4620000.0 yr, dE/E0=2.61e-07, N=799
  Estimated time remaining to complete simulation: 2 days, 4 hours, 38 minutes, 24 seconds
  Estimated time remaining to next output: 5 minutes, 52 seconds
Output 202/738: t=4630000.0 yr, dE/E0=2.47e-07, N=799
  Estimated time remaining to complete simulation: 2 days, 4 hours, 30 minutes, 42 seconds
  Estimated time remaining to next output: 5 minutes, 52 seconds
Output 203/738: t=4640000.0 yr, dE/E0=2.42e-07, N=799
  Estimated time remaining to complete simulation: 2 days, 4 hours, 23 minutes, 13 seconds
  Estimated time remaining to next output: 5 minutes, 52 seconds
Output 204/738: t=4650000.0 yr, dE/E0=2.37e-07, N=799
  Estimated time remaining to complete simulation: 2 days, 4 hours, 15 minutes, 56 seconds
  Estimated time remaining to next output: 5 minutes, 52 seconds
Output 205/738: t=4660000.0 yr, dE/E0=2.47e-07, N=799
  Estimated time remaining to complete simulation: 2 days, 4 hours, 8 minutes, 47 seconds
  Estimated time remaining to next output: 5 minutes, 52 seconds
Output 206/738: t=4670000.0 yr, dE/E0=2.53e-07, N=799
  Estimated time remaining to complete simulation: 2 days, 4 hours, 45 seconds
  Estimated time remaining to next output: 5 minutes, 51 seconds
Output 207/738: t=4680000.0 yr, dE/E0=2.45e-07, N=799
  Estimated time remaining to complete simulation: 2 days, 3 hours, 53 minutes
  Estimated time remaining to next output: 5 minutes, 51 seconds
Output 208/738: t=4690000.0 yr, dE/E0=2.43e-07, N=799
  Estimated time remaining to complete simulation: 2 days, 3 hours, 44 minutes, 57 seconds
  Estimated time remaining to next output: 5 minutes, 51 seconds
Output 209/738: t=4700000.0 yr, dE/E0=2.36e-07, N=799
  Estimated time remaining to complete simulation: 2 days, 3 hours, 37 minutes, 26 seconds
  Estimated time remaining to next output: 5 minutes, 51 seconds
Output 210/738: t=4710000.0 yr, dE/E0=2.38e-07, N=799
  Estimated time remaining to complete simulation: 2 days, 3 hours, 29 minutes, 52 seconds
  Estimated time remaining to next output: 5 minutes, 51 seconds
Output 211/738: t=4720000.0 yr, dE/E0=2.48e-07, N=799
  Estimated time remaining to complete simulation: 2 days, 3 hours, 22 minutes, 49 seconds
  Estimated time remaining to next output: 5 minutes, 50 seconds
Output 212/738: t=4730000.0 yr, dE/E0=2.45e-07, N=799
  Estimated time remaining to complete simulation: 2 days, 3 hours, 15 minutes, 27 seconds
  Estimated time remaining to next output: 5 minutes, 50 seconds
Output 213/738: t=4740000.0 yr, dE/E0=2.63e-07, N=799
  Estimated time remaining to complete simulation: 2 days, 3 hours, 8 minutes, 19 seconds
  Estimated time remaining to next output: 5 minutes, 50 seconds
Output 214/738: t=4750000.0 yr, dE/E0=2.55e-07, N=799
  Estimated time remaining to complete simulation: 2 days, 3 hours, 1 minutes, 11 seconds
  Estimated time remaining to next output: 5 minutes, 50 seconds
Output 215/738: t=4760000.0 yr, dE/E0=2.32e-07, N=799
  Estimated time remaining to complete simulation: 2 days, 2 hours, 53 minutes, 51 seconds
  Estimated time remaining to next output: 5 minutes, 50 seconds
Output 216/738: t=4770000.0 yr, dE/E0=2.39e-07, N=799
  Estimated time remaining to complete simulation: 2 days, 2 hours, 46 minutes, 21 seconds
  Estimated time remaining to next output: 5 minutes, 50 seconds
Output 217/738: t=4780000.0 yr, dE/E0=2.36e-07, N=799
  Estimated time remaining to complete simulation: 2 days, 2 hours, 39 minutes, 6 seconds
  Estimated time remaining to next output: 5 minutes, 49 seconds
Output 218/738: t=4790000.0 yr, dE/E0=2.42e-07, N=799
  Estimated time remaining to complete simulation: 2 days, 2 hours, 31 minutes, 36 seconds
  Estimated time remaining to next output: 5 minutes, 49 seconds
Output 219/738: t=4800000.0 yr, dE/E0=2.50e-07, N=799
  Estimated time remaining to complete simulation: 2 days, 2 hours, 25 minutes, 8 seconds
  Estimated time remaining to next output: 5 minutes, 49 seconds
Output 220/738: t=4810000.0 yr, dE/E0=2.39e-07, N=799
  Estimated time remaining to complete simulation: 2 days, 2 hours, 17 minutes, 50 seconds
  Estimated time remaining to next output: 5 minutes, 49 seconds
Output 221/738: t=4820000.0 yr, dE/E0=2.30e-07, N=799
  Estimated time remaining to complete simulation: 2 days, 2 hours, 11 minutes, 32 seconds
  Estimated time remaining to next output: 5 minutes, 49 seconds
Output 222/738: t=4830000.0 yr, dE/E0=2.38e-07, N=799
  Estimated time remaining to complete simulation: 2 days, 2 hours, 4 minutes, 18 seconds
  Estimated time remaining to next output: 5 minutes, 49 seconds
Output 223/738: t=4840000.0 yr, dE/E0=2.40e-07, N=799
  Estimated time remaining to complete simulation: 2 days, 1 hours, 56 minutes, 41 seconds
  Estimated time remaining to next output: 5 minutes, 49 seconds
Output 224/738: t=4850000.0 yr, dE/E0=2.60e-07, N=799
  Estimated time remaining to complete simulation: 2 days, 1 hours, 49 minutes, 8 seconds
  Estimated time remaining to next output: 5 minutes, 48 seconds
Output 225/738: t=4860000.0 yr, dE/E0=2.44e-07, N=799
  Estimated time remaining to complete simulation: 2 days, 1 hours, 41 minutes, 30 seconds
  Estimated time remaining to next output: 5 minutes, 48 seconds
Output 226/738: t=4870000.0 yr, dE/E0=2.45e-07, N=799
  Estimated time remaining to complete simulation: 2 days, 1 hours, 33 minutes, 41 seconds
  Estimated time remaining to next output: 5 minutes, 48 seconds
Output 227/738: t=4880000.0 yr, dE/E0=2.40e-07, N=799
  Estimated time remaining to complete simulation: 2 days, 1 hours, 26 minutes, 23 seconds
  Estimated time remaining to next output: 5 minutes, 48 seconds
Output 228/738: t=4890000.0 yr, dE/E0=2.43e-07, N=799
  Estimated time remaining to complete simulation: 2 days, 1 hours, 19 minutes, 20 seconds
  Estimated time remaining to next output: 5 minutes, 48 seconds
Output 229/738: t=4900000.0 yr, dE/E0=2.56e-07, N=799
  Estimated time remaining to complete simulation: 2 days, 1 hours, 12 minutes, 7 seconds
  Estimated time remaining to next output: 5 minutes, 47 seconds
Output 230/738: t=4910000.0 yr, dE/E0=2.62e-07, N=799
  Estimated time remaining to complete simulation: 2 days, 1 hours, 5 minutes, 11 seconds
  Estimated time remaining to next output: 5 minutes, 47 seconds
Output 231/738: t=4920000.0 yr, dE/E0=2.42e-07, N=799
  Estimated time remaining to complete simulation: 2 days, 58 minutes, 29 seconds
  Estimated time remaining to next output: 5 minutes, 47 seconds
Output 232/738: t=4930000.0 yr, dE/E0=2.51e-07, N=799
  Estimated time remaining to complete simulation: 2 days, 51 minutes, 19 seconds
  Estimated time remaining to next output: 5 minutes, 47 seconds
Output 233/738: t=4940000.0 yr, dE/E0=2.36e-07, N=799
  Estimated time remaining to complete simulation: 2 days, 44 minutes, 58 seconds
  Estimated time remaining to next output: 5 minutes, 47 seconds
Output 234/738: t=4950000.0 yr, dE/E0=2.20e-07, N=799
  Estimated time remaining to complete simulation: 2 days, 37 minutes, 24 seconds
  Estimated time remaining to next output: 5 minutes, 47 seconds
Output 235/738: t=4960000.0 yr, dE/E0=2.03e-07, N=799
  Estimated time remaining to complete simulation: 2 days, 29 minutes, 55 seconds
  Estimated time remaining to next output: 5 minutes, 47 seconds
Output 236/738: t=4970000.0 yr, dE/E0=2.27e-07, N=799
  Estimated time remaining to complete simulation: 2 days, 23 minutes, 2 seconds
  Estimated time remaining to next output: 5 minutes, 46 seconds
Output 237/738: t=4980000.0 yr, dE/E0=2.26e-07, N=799
  Estimated time remaining to complete simulation: 2 days, 16 minutes, 22 seconds
  Estimated time remaining to next output: 5 minutes, 46 seconds
Output 238/738: t=4990000.0 yr, dE/E0=2.27e-07, N=799
  Estimated time remaining to complete simulation: 2 days, 8 minutes, 57 seconds
  Estimated time remaining to next output: 5 minutes, 46 seconds
Output 239/738: t=5000000.0 yr, dE/E0=2.23e-07, N=799
  Estimated time remaining to complete simulation: 2 days, 2 minutes, 25 seconds
  Estimated time remaining to next output: 5 minutes, 46 seconds
Output 240/738: t=5010000.0 yr, dE/E0=2.41e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 23 hours, 54 minutes, 47 seconds
  Estimated time remaining to next output: 5 minutes, 46 seconds
Output 241/738: t=5020000.0 yr, dE/E0=2.33e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 23 hours, 47 minutes, 28 seconds
  Estimated time remaining to next output: 5 minutes, 46 seconds
Output 242/738: t=5030000.0 yr, dE/E0=2.32e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 23 hours, 41 minutes, 7 seconds
  Estimated time remaining to next output: 5 minutes, 46 seconds
Output 243/738: t=5040000.0 yr, dE/E0=2.46e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 23 hours, 34 minutes, 21 seconds
  Estimated time remaining to next output: 5 minutes, 45 seconds
Output 244/738: t=5050000.0 yr, dE/E0=2.30e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 23 hours, 28 minutes, 11 seconds
  Estimated time remaining to next output: 5 minutes, 45 seconds
Output 245/738: t=5060000.0 yr, dE/E0=2.22e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 23 hours, 21 minutes, 53 seconds
  Estimated time remaining to next output: 5 minutes, 45 seconds
Output 246/738: t=5070000.0 yr, dE/E0=2.11e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 23 hours, 15 minutes, 52 seconds
  Estimated time remaining to next output: 5 minutes, 45 seconds
Output 247/738: t=5080000.0 yr, dE/E0=2.22e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 23 hours, 11 minutes, 55 seconds
  Estimated time remaining to next output: 5 minutes, 46 seconds
Output 248/738: t=5090000.0 yr, dE/E0=2.25e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 23 hours, 11 minutes, 1 seconds
  Estimated time remaining to next output: 5 minutes, 46 seconds
Output 249/738: t=5100000.0 yr, dE/E0=2.33e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 23 hours, 10 minutes, 33 seconds
  Estimated time remaining to next output: 5 minutes, 47 seconds
Output 250/738: t=5110000.0 yr, dE/E0=2.25e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 23 hours, 10 minutes, 17 seconds
  Estimated time remaining to next output: 5 minutes, 47 seconds
Output 251/738: t=5120000.0 yr, dE/E0=2.20e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 23 hours, 9 minutes, 18 seconds
  Estimated time remaining to next output: 5 minutes, 48 seconds
Output 252/738: t=5130000.0 yr, dE/E0=2.03e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 23 hours, 4 minutes, 18 seconds
  Estimated time remaining to next output: 5 minutes, 48 seconds
Output 253/738: t=5140000.0 yr, dE/E0=2.15e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 23 hours, 4 minutes, 11 seconds
  Estimated time remaining to next output: 5 minutes, 49 seconds
Output 254/738: t=5150000.0 yr, dE/E0=2.32e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 23 hours, 3 minutes, 59 seconds
  Estimated time remaining to next output: 5 minutes, 50 seconds
Output 255/738: t=5160000.0 yr, dE/E0=2.27e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 23 hours, 2 minutes, 43 seconds
  Estimated time remaining to next output: 5 minutes, 50 seconds
Output 256/738: t=5170000.0 yr, dE/E0=2.21e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 23 hours, 2 minutes, 6 seconds
  Estimated time remaining to next output: 5 minutes, 51 seconds
Output 257/738: t=5180000.0 yr, dE/E0=2.03e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 23 hours, 1 minutes, 20 seconds
  Estimated time remaining to next output: 5 minutes, 51 seconds
Output 258/738: t=5190000.0 yr, dE/E0=1.99e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 23 hours, 1 minutes, 45 seconds
  Estimated time remaining to next output: 5 minutes, 52 seconds
Output 259/738: t=5200000.0 yr, dE/E0=1.99e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 22 hours, 56 minutes, 25 seconds
  Estimated time remaining to next output: 5 minutes, 52 seconds
Output 260/738: t=5210000.0 yr, dE/E0=2.19e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 22 hours, 52 minutes, 43 seconds
  Estimated time remaining to next output: 5 minutes, 53 seconds
Output 261/738: t=5220000.0 yr, dE/E0=2.29e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 22 hours, 51 minutes, 19 seconds
  Estimated time remaining to next output: 5 minutes, 53 seconds
Output 262/738: t=5230000.0 yr, dE/E0=2.21e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 22 hours, 47 minutes, 52 seconds
  Estimated time remaining to next output: 5 minutes, 53 seconds
Output 263/738: t=5240000.0 yr, dE/E0=2.04e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 22 hours, 41 minutes, 15 seconds
  Estimated time remaining to next output: 5 minutes, 53 seconds
Output 264/738: t=5250000.0 yr, dE/E0=2.01e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 22 hours, 34 minutes, 29 seconds
  Estimated time remaining to next output: 5 minutes, 53 seconds
Output 265/738: t=5260000.0 yr, dE/E0=1.92e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 22 hours, 27 minutes, 46 seconds
  Estimated time remaining to next output: 5 minutes, 53 seconds
Output 266/738: t=5270000.0 yr, dE/E0=2.07e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 22 hours, 20 minutes, 54 seconds
  Estimated time remaining to next output: 5 minutes, 53 seconds
Output 267/738: t=5280000.0 yr, dE/E0=2.17e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 22 hours, 13 minutes, 45 seconds
  Estimated time remaining to next output: 5 minutes, 53 seconds
Output 268/738: t=5290000.0 yr, dE/E0=2.08e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 22 hours, 7 minutes, 19 seconds
  Estimated time remaining to next output: 5 minutes, 53 seconds
Output 269/738: t=5300000.0 yr, dE/E0=1.98e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 22 hours, 2 minutes, 16 seconds
  Estimated time remaining to next output: 5 minutes, 53 seconds
Output 270/738: t=5310000.0 yr, dE/E0=2.05e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 21 hours, 55 minutes, 29 seconds
  Estimated time remaining to next output: 5 minutes, 53 seconds
Output 271/738: t=5320000.0 yr, dE/E0=2.01e-07, N=799
  Estimated time remaining to complete simulation: 1 days, 21 hours, 48 minutes, 28 seconds
  Estimated time remaining to next output: 5 minutes, 53 seconds
A particle escaped (r>exit_max_distance).
Removing escaped particle at index 646
Remaining particles: 798
Output 272/738: t=5323252.2 yr, dE/E0=2.96e-07, N=798
  Estimated time remaining to complete simulation: 1 days, 21 hours, 35 minutes, 27 seconds
  Estimated time remaining to next output: 5 minutes, 52 seconds
Output 273/738: t=5340000.0 yr, dE/E0=2.97e-07, N=798
  Estimated time remaining to complete simulation: 1 days, 21 hours, 35 minutes, 24 seconds
  Estimated time remaining to next output: 5 minutes, 52 seconds
Output 274/738: t=5350000.0 yr, dE/E0=2.84e-07, N=798
  Estimated time remaining to complete simulation: 1 days, 21 hours, 31 minutes, 18 seconds
  Estimated time remaining to next output: 5 minutes, 53 seconds
Output 275/738: t=5360000.0 yr, dE/E0=2.86e-07, N=798
  Estimated time remaining to complete simulation: 1 days, 21 hours, 30 minutes, 31 seconds
  Estimated time remaining to next output: 5 minutes, 53 seconds
Output 276/738: t=5370000.0 yr, dE/E0=2.79e-07, N=798
  Estimated time remaining to complete simulation: 1 days, 21 hours, 28 minutes, 12 seconds
  Estimated time remaining to next output: 5 minutes, 54 seconds
Output 277/738: t=5380000.0 yr, dE/E0=2.81e-07, N=798
  Estimated time remaining to complete simulation: 1 days, 21 hours, 27 minutes, 14 seconds
  Estimated time remaining to next output: 5 minutes, 54 seconds
Output 278/738: t=5390000.0 yr, dE/E0=2.85e-07, N=798
  Estimated time remaining to complete simulation: 1 days, 21 hours, 26 minutes, 25 seconds
  Estimated time remaining to next output: 5 minutes, 55 seconds
Output 279/738: t=5400000.0 yr, dE/E0=2.98e-07, N=798
  Estimated time remaining to complete simulation: 1 days, 21 hours, 24 minutes, 11 seconds
  Estimated time remaining to next output: 5 minutes, 56 seconds
Output 280/738: t=5410000.0 yr, dE/E0=2.85e-07, N=798
  Estimated time remaining to complete simulation: 1 days, 21 hours, 18 minutes, 46 seconds
  Estimated time remaining to next output: 5 minutes, 56 seconds
Output 281/738: t=5420000.0 yr, dE/E0=2.82e-07, N=798
  Estimated time remaining to complete simulation: 1 days, 21 hours, 11 minutes, 59 seconds
  Estimated time remaining to next output: 5 minutes, 56 seconds
Output 282/738: t=5430000.0 yr, dE/E0=2.78e-07, N=798
  Estimated time remaining to complete simulation: 1 days, 21 hours, 4 minutes, 56 seconds
  Estimated time remaining to next output: 5 minutes, 55 seconds
Output 283/738: t=5440000.0 yr, dE/E0=2.88e-07, N=798
  Estimated time remaining to complete simulation: 1 days, 20 hours, 58 minutes
  Estimated time remaining to next output: 5 minutes, 55 seconds
Output 284/738: t=5450000.0 yr, dE/E0=3.02e-07, N=798
  Estimated time remaining to complete simulation: 1 days, 20 hours, 51 minutes, 30 seconds
  Estimated time remaining to next output: 5 minutes, 55 seconds
Output 285/738: t=5460000.0 yr, dE/E0=3.01e-07, N=798
  Estimated time remaining to complete simulation: 1 days, 20 hours, 44 minutes, 1 seconds
  Estimated time remaining to next output: 5 minutes, 55 seconds
Output 286/738: t=5470000.0 yr, dE/E0=2.94e-07, N=798
  Estimated time remaining to complete simulation: 1 days, 20 hours, 36 minutes, 56 seconds
  Estimated time remaining to next output: 5 minutes, 55 seconds
Output 287/738: t=5480000.0 yr, dE/E0=3.06e-07, N=798
  Estimated time remaining to complete simulation: 1 days, 20 hours, 30 minutes, 23 seconds
  Estimated time remaining to next output: 5 minutes, 55 seconds
Output 288/738: t=5490000.0 yr, dE/E0=3.12e-07, N=798
  Estimated time remaining to complete simulation: 1 days, 20 hours, 23 minutes, 23 seconds
  Estimated time remaining to next output: 5 minutes, 55 seconds
A particle escaped (r>exit_max_distance).
Removing escaped particle at index 381
Remaining particles: 797
Output 289/738: t=5490672.9 yr, dE/E0=4.73e-07, N=797
  Estimated time remaining to complete simulation: 1 days, 20 hours, 8 minutes, 56 seconds
  Estimated time remaining to next output: 5 minutes, 53 seconds
Output 290/738: t=5510000.0 yr, dE/E0=4.58e-07, N=797
  Estimated time remaining to complete simulation: 1 days, 20 hours, 8 minutes, 43 seconds
  Estimated time remaining to next output: 5 minutes, 54 seconds
Output 291/738: t=5520000.0 yr, dE/E0=4.70e-07, N=797
  Estimated time remaining to complete simulation: 1 days, 20 hours, 2 minutes, 39 seconds
  Estimated time remaining to next output: 5 minutes, 54 seconds
Output 292/738: t=5530000.0 yr, dE/E0=4.57e-07, N=797
  Estimated time remaining to complete simulation: 1 days, 19 hours, 55 minutes, 45 seconds
  Estimated time remaining to next output: 5 minutes, 54 seconds
Output 293/738: t=5540000.0 yr, dE/E0=4.51e-07, N=797
  Estimated time remaining to complete simulation: 1 days, 19 hours, 49 minutes, 5 seconds
  Estimated time remaining to next output: 5 minutes, 54 seconds
Output 294/738: t=5550000.0 yr, dE/E0=4.36e-07, N=797
  Estimated time remaining to complete simulation: 1 days, 19 hours, 42 minutes, 12 seconds
  Estimated time remaining to next output: 5 minutes, 54 seconds
Output 295/738: t=5560000.0 yr, dE/E0=4.43e-07, N=797
  Estimated time remaining to complete simulation: 1 days, 19 hours, 35 minutes, 34 seconds
  Estimated time remaining to next output: 5 minutes, 54 seconds
Output 296/738: t=5570000.0 yr, dE/E0=4.41e-07, N=797
  Estimated time remaining to complete simulation: 1 days, 19 hours, 28 minutes, 22 seconds
  Estimated time remaining to next output: 5 minutes, 54 seconds
Output 297/738: t=5580000.0 yr, dE/E0=4.42e-07, N=797
  Estimated time remaining to complete simulation: 1 days, 19 hours, 21 minutes, 38 seconds
  Estimated time remaining to next output: 5 minutes, 53 seconds
Output 298/738: t=5590000.0 yr, dE/E0=4.52e-07, N=797
  Estimated time remaining to complete simulation: 1 days, 19 hours, 14 minutes, 37 seconds
  Estimated time remaining to next output: 5 minutes, 53 seconds
Output 299/738: t=5600000.0 yr, dE/E0=4.40e-07, N=797
  Estimated time remaining to complete simulation: 1 days, 19 hours, 7 minutes, 53 seconds
  Estimated time remaining to next output: 5 minutes, 53 seconds
Output 300/738: t=5610000.0 yr, dE/E0=4.37e-07, N=797
  Estimated time remaining to complete simulation: 1 days, 19 hours, 51 seconds
  Estimated time remaining to next output: 5 minutes, 53 seconds
Output 301/738: t=5620000.0 yr, dE/E0=4.38e-07, N=797
  Estimated time remaining to complete simulation: 1 days, 18 hours, 53 minutes, 50 seconds
  Estimated time remaining to next output: 5 minutes, 53 seconds
Output 302/738: t=5630000.0 yr, dE/E0=4.54e-07, N=797
  Estimated time remaining to complete simulation: 1 days, 18 hours, 46 minutes, 44 seconds
  Estimated time remaining to next output: 5 minutes, 53 seconds
Output 303/738: t=5640000.0 yr, dE/E0=4.52e-07, N=797
  Estimated time remaining to complete simulation: 1 days, 18 hours, 39 minutes, 40 seconds
  Estimated time remaining to next output: 5 minutes, 53 seconds
Output 304/738: t=5650000.0 yr, dE/E0=4.51e-07, N=797
  Estimated time remaining to complete simulation: 1 days, 18 hours, 32 minutes, 27 seconds
  Estimated time remaining to next output: 5 minutes, 52 seconds
A particle escaped (r>exit_max_distance).
Removing escaped particle at index 393
Remaining particles: 796
Output 305/738: t=5650897.1 yr, dE/E0=5.89e-07, N=796
  Estimated time remaining to complete simulation: 1 days, 18 hours, 18 minutes, 53 seconds
  Estimated time remaining to next output: 5 minutes, 51 seconds
Output 306/738: t=5670000.0 yr, dE/E0=5.87e-07, N=796
  Estimated time remaining to complete simulation: 1 days, 18 hours, 19 minutes, 20 seconds
  Estimated time remaining to next output: 5 minutes, 52 seconds
Output 307/738: t=5680000.0 yr, dE/E0=5.85e-07, N=796
  Estimated time remaining to complete simulation: 1 days, 18 hours, 12 minutes, 42 seconds
  Estimated time remaining to next output: 5 minutes, 52 seconds
Output 308/738: t=5690000.0 yr, dE/E0=5.93e-07, N=796
  Estimated time remaining to complete simulation: 1 days, 18 hours, 5 minutes, 31 seconds
  Estimated time remaining to next output: 5 minutes, 52 seconds
Output 309/738: t=5700000.0 yr, dE/E0=5.95e-07, N=796
  Estimated time remaining to complete simulation: 1 days, 17 hours, 58 minutes, 49 seconds
  Estimated time remaining to next output: 5 minutes, 52 seconds
Output 310/738: t=5710000.0 yr, dE/E0=5.88e-07, N=796
  Estimated time remaining to complete simulation: 1 days, 17 hours, 52 minutes, 23 seconds
  Estimated time remaining to next output: 5 minutes, 52 seconds
Output 311/738: t=5720000.0 yr, dE/E0=5.76e-07, N=796
  Estimated time remaining to complete simulation: 1 days, 17 hours, 45 minutes, 44 seconds
  Estimated time remaining to next output: 5 minutes, 52 seconds
Output 312/738: t=5730000.0 yr, dE/E0=5.66e-07, N=796
  Estimated time remaining to complete simulation: 1 days, 17 hours, 38 minutes, 40 seconds
  Estimated time remaining to next output: 5 minutes, 51 seconds
Output 313/738: t=5740000.0 yr, dE/E0=5.79e-07, N=796
  Estimated time remaining to complete simulation: 1 days, 17 hours, 31 minutes, 50 seconds
  Estimated time remaining to next output: 5 minutes, 51 seconds
Output 314/738: t=5750000.0 yr, dE/E0=5.98e-07, N=796
  Estimated time remaining to complete simulation: 1 days, 17 hours, 25 minutes, 11 seconds
  Estimated time remaining to next output: 5 minutes, 51 seconds
Output 315/738: t=5760000.0 yr, dE/E0=5.93e-07, N=796
  Estimated time remaining to complete simulation: 1 days, 17 hours, 18 minutes, 18 seconds
  Estimated time remaining to next output: 5 minutes, 51 seconds
Output 316/738: t=5770000.0 yr, dE/E0=5.86e-07, N=796
  Estimated time remaining to complete simulation: 1 days, 17 hours, 11 minutes, 44 seconds
  Estimated time remaining to next output: 5 minutes, 51 seconds
Output 317/738: t=5780000.0 yr, dE/E0=5.84e-07, N=796
  Estimated time remaining to complete simulation: 1 days, 17 hours, 4 minutes, 59 seconds
  Estimated time remaining to next output: 5 minutes, 51 seconds
Output 318/738: t=5790000.0 yr, dE/E0=5.86e-07, N=796
  Estimated time remaining to complete simulation: 1 days, 16 hours, 58 minutes, 16 seconds
  Estimated time remaining to next output: 5 minutes, 51 seconds
Output 319/738: t=5800000.0 yr, dE/E0=5.85e-07, N=796
  Estimated time remaining to complete simulation: 1 days, 16 hours, 52 minutes, 2 seconds
  Estimated time remaining to next output: 5 minutes, 51 seconds
Output 320/738: t=5810000.0 yr, dE/E0=5.94e-07, N=796
  Estimated time remaining to complete simulation: 1 days, 16 hours, 45 minutes, 21 seconds
  Estimated time remaining to next output: 5 minutes, 51 seconds
Output 321/738: t=5820000.0 yr, dE/E0=6.01e-07, N=796
  Estimated time remaining to complete simulation: 1 days, 16 hours, 38 minutes, 49 seconds
  Estimated time remaining to next output: 5 minutes, 50 seconds
Output 322/738: t=5830000.0 yr, dE/E0=5.90e-07, N=796
  Estimated time remaining to complete simulation: 1 days, 16 hours, 31 minutes, 58 seconds
  Estimated time remaining to next output: 5 minutes, 50 seconds
Output 323/738: t=5840000.0 yr, dE/E0=5.89e-07, N=796
  Estimated time remaining to complete simulation: 1 days, 16 hours, 25 minutes, 17 seconds
  Estimated time remaining to next output: 5 minutes, 50 seconds
Output 324/738: t=5850000.0 yr, dE/E0=5.80e-07, N=796
  Estimated time remaining to complete simulation: 1 days, 16 hours, 18 minutes, 46 seconds
  Estimated time remaining to next output: 5 minutes, 50 seconds
Output 325/738: t=5860000.0 yr, dE/E0=5.85e-07, N=796
  Estimated time remaining to complete simulation: 1 days, 16 hours, 12 minutes, 13 seconds
  Estimated time remaining to next output: 5 minutes, 50 seconds
Output 326/738: t=5870000.0 yr, dE/E0=6.00e-07, N=796
  Estimated time remaining to complete simulation: 1 days, 16 hours, 5 minutes, 29 seconds
  Estimated time remaining to next output: 5 minutes, 50 seconds
Output 327/738: t=5880000.0 yr, dE/E0=5.96e-07, N=796
  Estimated time remaining to complete simulation: 1 days, 15 hours, 58 minutes, 37 seconds
  Estimated time remaining to next output: 5 minutes, 50 seconds
Output 328/738: t=5890000.0 yr, dE/E0=5.91e-07, N=796
  Estimated time remaining to complete simulation: 1 days, 15 hours, 52 minutes, 3 seconds
  Estimated time remaining to next output: 5 minutes, 50 seconds
Output 329/738: t=5900000.0 yr, dE/E0=5.86e-07, N=796
  Estimated time remaining to complete simulation: 1 days, 15 hours, 45 minutes, 22 seconds
  Estimated time remaining to next output: 5 minutes, 49 seconds
Output 330/738: t=5910000.0 yr, dE/E0=5.94e-07, N=796
  Estimated time remaining to complete simulation: 1 days, 15 hours, 38 minutes, 46 seconds
  Estimated time remaining to next output: 5 minutes, 49 seconds
Output 331/738: t=5920000.0 yr, dE/E0=5.81e-07, N=796
  Estimated time remaining to complete simulation: 1 days, 15 hours, 32 minutes, 17 seconds
  Estimated time remaining to next output: 5 minutes, 49 seconds
Output 332/738: t=5930000.0 yr, dE/E0=5.96e-07, N=796
  Estimated time remaining to complete simulation: 1 days, 15 hours, 25 minutes, 34 seconds
  Estimated time remaining to next output: 5 minutes, 49 seconds
Output 333/738: t=5940000.0 yr, dE/E0=6.05e-07, N=796
  Estimated time remaining to complete simulation: 1 days, 15 hours, 18 minutes, 55 seconds
  Estimated time remaining to next output: 5 minutes, 49 seconds
Output 334/738: t=5950000.0 yr, dE/E0=6.04e-07, N=796
  Estimated time remaining to complete simulation: 1 days, 15 hours, 12 minutes, 10 seconds
  Estimated time remaining to next output: 5 minutes, 49 seconds
Output 335/738: t=5960000.0 yr, dE/E0=6.06e-07, N=796
  Estimated time remaining to complete simulation: 1 days, 15 hours, 5 minutes, 29 seconds
  Estimated time remaining to next output: 5 minutes, 49 seconds
Output 336/738: t=5970000.0 yr, dE/E0=5.85e-07, N=796
  Estimated time remaining to complete simulation: 1 days, 14 hours, 58 minutes, 56 seconds
  Estimated time remaining to next output: 5 minutes, 49 seconds
Output 337/738: t=5980000.0 yr, dE/E0=6.05e-07, N=796
  Estimated time remaining to complete simulation: 1 days, 14 hours, 52 minutes, 26 seconds
  Estimated time remaining to next output: 5 minutes, 48 seconds
Output 338/738: t=5990000.0 yr, dE/E0=6.08e-07, N=796
  Estimated time remaining to complete simulation: 1 days, 14 hours, 45 minutes, 58 seconds
  Estimated time remaining to next output: 5 minutes, 48 seconds
Output 339/738: t=6000000.0 yr, dE/E0=6.14e-07, N=796
  Estimated time remaining to complete simulation: 1 days, 14 hours, 39 minutes, 26 seconds
  Estimated time remaining to next output: 5 minutes, 48 seconds
Output 340/738: t=6010000.0 yr, dE/E0=5.96e-07, N=796
  Estimated time remaining to complete simulation: 1 days, 14 hours, 33 minutes, 22 seconds
  Estimated time remaining to next output: 5 minutes, 48 seconds
Output 341/738: t=6020000.0 yr, dE/E0=6.08e-07, N=796
  Estimated time remaining to complete simulation: 1 days, 14 hours, 26 minutes, 50 seconds
  Estimated time remaining to next output: 5 minutes, 48 seconds
Output 342/738: t=6030000.0 yr, dE/E0=6.02e-07, N=796
  Estimated time remaining to complete simulation: 1 days, 14 hours, 20 minutes, 29 seconds
  Estimated time remaining to next output: 5 minutes, 48 seconds
Output 343/738: t=6040000.0 yr, dE/E0=6.08e-07, N=796
  Estimated time remaining to complete simulation: 1 days, 14 hours, 13 minutes, 42 seconds
  Estimated time remaining to next output: 5 minutes, 48 seconds
Output 344/738: t=6050000.0 yr, dE/E0=6.02e-07, N=796
  Estimated time remaining to complete simulation: 1 days, 14 hours, 7 minutes, 12 seconds
  Estimated time remaining to next output: 5 minutes, 48 seconds
Output 345/738: t=6060000.0 yr, dE/E0=6.10e-07, N=796
  Estimated time remaining to complete simulation: 1 days, 14 hours, 54 seconds
  Estimated time remaining to next output: 5 minutes, 48 seconds
Output 346/738: t=6070000.0 yr, dE/E0=6.01e-07, N=796
  Estimated time remaining to complete simulation: 1 days, 13 hours, 54 minutes, 24 seconds
  Estimated time remaining to next output: 5 minutes, 48 seconds
Output 347/738: t=6080000.0 yr, dE/E0=5.94e-07, N=796
  Estimated time remaining to complete simulation: 1 days, 13 hours, 47 minutes, 59 seconds
  Estimated time remaining to next output: 5 minutes, 48 seconds
Output 348/738: t=6090000.0 yr, dE/E0=5.88e-07, N=796
  Estimated time remaining to complete simulation: 1 days, 13 hours, 41 minutes, 23 seconds
  Estimated time remaining to next output: 5 minutes, 47 seconds
Output 349/738: t=6100000.0 yr, dE/E0=5.87e-07, N=796
  Estimated time remaining to complete simulation: 1 days, 13 hours, 34 minutes, 47 seconds
  Estimated time remaining to next output: 5 minutes, 47 seconds
Output 350/738: t=6110000.0 yr, dE/E0=5.97e-07, N=796
  Estimated time remaining to complete simulation: 1 days, 13 hours, 28 minutes, 29 seconds
  Estimated time remaining to next output: 5 minutes, 47 seconds
Output 351/738: t=6120000.0 yr, dE/E0=5.85e-07, N=796
  Estimated time remaining to complete simulation: 1 days, 13 hours, 23 minutes, 14 seconds
  Estimated time remaining to next output: 5 minutes, 47 seconds
Output 352/738: t=6130000.0 yr, dE/E0=6.04e-07, N=796
  Estimated time remaining to complete simulation: 1 days, 13 hours, 16 minutes, 49 seconds
  Estimated time remaining to next output: 5 minutes, 47 seconds
Output 353/738: t=6140000.0 yr, dE/E0=5.93e-07, N=796
  Estimated time remaining to complete simulation: 1 days, 13 hours, 10 minutes, 23 seconds
  Estimated time remaining to next output: 5 minutes, 47 seconds
Output 354/738: t=6150000.0 yr, dE/E0=6.04e-07, N=796
  Estimated time remaining to complete simulation: 1 days, 13 hours, 3 minutes, 50 seconds
  Estimated time remaining to next output: 5 minutes, 47 seconds
Output 355/738: t=6160000.0 yr, dE/E0=6.08e-07, N=796
  Estimated time remaining to complete simulation: 1 days, 12 hours, 57 minutes, 33 seconds
  Estimated time remaining to next output: 5 minutes, 47 seconds
Output 356/738: t=6170000.0 yr, dE/E0=6.01e-07, N=796
  Estimated time remaining to complete simulation: 1 days, 12 hours, 51 minutes, 23 seconds
  Estimated time remaining to next output: 5 minutes, 47 seconds
Output 357/738: t=6180000.0 yr, dE/E0=6.03e-07, N=796
  Estimated time remaining to complete simulation: 1 days, 12 hours, 45 minutes, 30 seconds
  Estimated time remaining to next output: 5 minutes, 47 seconds
Output 358/738: t=6190000.0 yr, dE/E0=6.13e-07, N=796
  Estimated time remaining to complete simulation: 1 days, 12 hours, 39 minutes, 3 seconds
  Estimated time remaining to next output: 5 minutes, 47 seconds
Output 359/738: t=6200000.0 yr, dE/E0=5.99e-07, N=796
  Estimated time remaining to complete simulation: 1 days, 12 hours, 32 minutes, 44 seconds
  Estimated time remaining to next output: 5 minutes, 47 seconds
Output 360/738: t=6210000.0 yr, dE/E0=5.79e-07, N=796
  Estimated time remaining to complete simulation: 1 days, 12 hours, 26 minutes, 28 seconds
  Estimated time remaining to next output: 5 minutes, 47 seconds
Output 361/738: t=6220000.0 yr, dE/E0=5.62e-07, N=796
  Estimated time remaining to complete simulation: 1 days, 12 hours, 20 minutes, 8 seconds
  Estimated time remaining to next output: 5 minutes, 46 seconds
Output 362/738: t=6230000.0 yr, dE/E0=5.77e-07, N=796
  Estimated time remaining to complete simulation: 1 days, 12 hours, 13 minutes, 48 seconds
  Estimated time remaining to next output: 5 minutes, 46 seconds
Output 363/738: t=6240000.0 yr, dE/E0=5.91e-07, N=796
  Estimated time remaining to complete simulation: 1 days, 12 hours, 7 minutes, 25 seconds
  Estimated time remaining to next output: 5 minutes, 46 seconds
Output 364/738: t=6250000.0 yr, dE/E0=5.91e-07, N=796
  Estimated time remaining to complete simulation: 1 days, 12 hours, 43 seconds
  Estimated time remaining to next output: 5 minutes, 46 seconds
Output 365/738: t=6260000.0 yr, dE/E0=5.83e-07, N=796
  Estimated time remaining to complete simulation: 1 days, 11 hours, 54 minutes, 34 seconds
  Estimated time remaining to next output: 5 minutes, 46 seconds
A particle escaped (r>exit_max_distance).
Removing escaped particle at index 569
Remaining particles: 795
Output 366/738: t=6265158.6 yr, dE/E0=7.01e-07, N=795
  Estimated time remaining to complete simulation: 1 days, 11 hours, 45 minutes, 41 seconds
  Estimated time remaining to next output: 5 minutes, 46 seconds
Output 367/738: t=6280000.0 yr, dE/E0=6.74e-07, N=795
  Estimated time remaining to complete simulation: 1 days, 11 hours, 42 minutes, 20 seconds
  Estimated time remaining to next output: 5 minutes, 46 seconds
A particle escaped (r>exit_max_distance).
Removing escaped particle at index 570
Remaining particles: 794
Output 368/738: t=6287233.3 yr, dE/E0=8.00e-07, N=794
  Estimated time remaining to complete simulation: 1 days, 11 hours, 34 minutes, 40 seconds
  Estimated time remaining to next output: 5 minutes, 46 seconds
Output 369/738: t=6300000.0 yr, dE/E0=8.12e-07, N=794
  Estimated time remaining to complete simulation: 1 days, 11 hours, 29 minutes, 52 seconds
  Estimated time remaining to next output: 5 minutes, 46 seconds
Output 370/738: t=6310000.0 yr, dE/E0=8.13e-07, N=794
  Estimated time remaining to complete simulation: 1 days, 11 hours, 23 minutes, 48 seconds
  Estimated time remaining to next output: 5 minutes, 46 seconds
Output 371/738: t=6320000.0 yr, dE/E0=8.04e-07, N=794
  Estimated time remaining to complete simulation: 1 days, 11 hours, 17 minutes, 28 seconds
  Estimated time remaining to next output: 5 minutes, 46 seconds
Output 372/738: t=6330000.0 yr, dE/E0=8.08e-07, N=794
  Estimated time remaining to complete simulation: 1 days, 11 hours, 11 minutes
  Estimated time remaining to next output: 5 minutes, 46 seconds
Output 373/738: t=6340000.0 yr, dE/E0=8.04e-07, N=794
  Estimated time remaining to complete simulation: 1 days, 11 hours, 4 minutes, 52 seconds
  Estimated time remaining to next output: 5 minutes, 46 seconds
Output 374/738: t=6350000.0 yr, dE/E0=8.04e-07, N=794
  Estimated time remaining to complete simulation: 1 days, 10 hours, 58 minutes, 20 seconds
  Estimated time remaining to next output: 5 minutes, 45 seconds
Output 375/738: t=6360000.0 yr, dE/E0=8.04e-07, N=794
  Estimated time remaining to complete simulation: 1 days, 10 hours, 52 minutes, 10 seconds
  Estimated time remaining to next output: 5 minutes, 45 seconds
Output 376/738: t=6370000.0 yr, dE/E0=8.20e-07, N=794
  Estimated time remaining to complete simulation: 1 days, 10 hours, 45 minutes, 54 seconds
  Estimated time remaining to next output: 5 minutes, 45 seconds
Output 377/738: t=6380000.0 yr, dE/E0=8.04e-07, N=794
  Estimated time remaining to complete simulation: 1 days, 10 hours, 39 minutes, 28 seconds
  Estimated time remaining to next output: 5 minutes, 45 seconds
Output 378/738: t=6390000.0 yr, dE/E0=8.27e-07, N=794
  Estimated time remaining to complete simulation: 1 days, 10 hours, 33 minutes, 13 seconds
  Estimated time remaining to next output: 5 minutes, 45 seconds
Output 379/738: t=6400000.0 yr, dE/E0=8.19e-07, N=794
  Estimated time remaining to complete simulation: 1 days, 10 hours, 27 minutes, 9 seconds
  Estimated time remaining to next output: 5 minutes, 45 seconds
Output 380/738: t=6410000.0 yr, dE/E0=8.27e-07, N=794
  Estimated time remaining to complete simulation: 1 days, 10 hours, 20 minutes, 44 seconds
  Estimated time remaining to next output: 5 minutes, 45 seconds
A particle escaped (r>exit_max_distance).
Removing escaped particle at index 748
Remaining particles: 793
Output 381/738: t=6413308.2 yr, dE/E0=9.21e-07, N=793
  Estimated time remaining to complete simulation: 1 days, 10 hours, 11 minutes, 7 seconds
  Estimated time remaining to next output: 5 minutes, 44 seconds
Output 382/738: t=6430000.0 yr, dE/E0=9.14e-07, N=793
  Estimated time remaining to complete simulation: 1 days, 10 hours, 8 minutes, 5 seconds
  Estimated time remaining to next output: 5 minutes, 45 seconds
Output 383/738: t=6440000.0 yr, dE/E0=9.17e-07, N=793
  Estimated time remaining to complete simulation: 1 days, 10 hours, 1 minutes, 35 seconds
  Estimated time remaining to next output: 5 minutes, 45 seconds
Output 384/738: t=6450000.0 yr, dE/E0=9.23e-07, N=793
  Estimated time remaining to complete simulation: 1 days, 9 hours, 55 minutes, 16 seconds
  Estimated time remaining to next output: 5 minutes, 44 seconds
Output 385/738: t=6460000.0 yr, dE/E0=9.15e-07, N=793
  Estimated time remaining to complete simulation: 1 days, 9 hours, 48 minutes, 59 seconds
  Estimated time remaining to next output: 5 minutes, 44 seconds
Output 386/738: t=6470000.0 yr, dE/E0=9.23e-07, N=793
  Estimated time remaining to complete simulation: 1 days, 9 hours, 42 minutes, 48 seconds
  Estimated time remaining to next output: 5 minutes, 44 seconds
Output 387/738: t=6480000.0 yr, dE/E0=9.31e-07, N=793
  Estimated time remaining to complete simulation: 1 days, 9 hours, 36 minutes, 22 seconds
  Estimated time remaining to next output: 5 minutes, 44 seconds
Output 388/738: t=6490000.0 yr, dE/E0=9.40e-07, N=793
  Estimated time remaining to complete simulation: 1 days, 9 hours, 30 minutes, 18 seconds
  Estimated time remaining to next output: 5 minutes, 44 seconds
Output 389/738: t=6500000.0 yr, dE/E0=9.37e-07, N=793
  Estimated time remaining to complete simulation: 1 days, 9 hours, 24 minutes, 2 seconds
  Estimated time remaining to next output: 5 minutes, 44 seconds
Output 390/738: t=6510000.0 yr, dE/E0=9.38e-07, N=793
  Estimated time remaining to complete simulation: 1 days, 9 hours, 17 minutes, 43 seconds
  Estimated time remaining to next output: 5 minutes, 44 seconds
Output 391/738: t=6520000.0 yr, dE/E0=9.39e-07, N=793
  Estimated time remaining to complete simulation: 1 days, 9 hours, 11 minutes, 26 seconds
  Estimated time remaining to next output: 5 minutes, 44 seconds
Output 392/738: t=6530000.0 yr, dE/E0=9.29e-07, N=793
  Estimated time remaining to complete simulation: 1 days, 9 hours, 5 minutes, 1 seconds
  Estimated time remaining to next output: 5 minutes, 44 seconds
Output 393/738: t=6540000.0 yr, dE/E0=9.20e-07, N=793
  Estimated time remaining to complete simulation: 1 days, 8 hours, 58 minutes, 53 seconds
  Estimated time remaining to next output: 5 minutes, 44 seconds
Output 394/738: t=6550000.0 yr, dE/E0=9.27e-07, N=793
  Estimated time remaining to complete simulation: 1 days, 8 hours, 52 minutes, 52 seconds
  Estimated time remaining to next output: 5 minutes, 44 seconds
Output 395/738: t=6560000.0 yr, dE/E0=9.32e-07, N=793
  Estimated time remaining to complete simulation: 1 days, 8 hours, 46 minutes, 19 seconds
  Estimated time remaining to next output: 5 minutes, 43 seconds
Output 396/738: t=6570000.0 yr, dE/E0=8.98e-07, N=793
  Estimated time remaining to complete simulation: 1 days, 8 hours, 40 minutes, 3 seconds
  Estimated time remaining to next output: 5 minutes, 43 seconds
Output 397/738: t=6580000.0 yr, dE/E0=9.14e-07, N=793
  Estimated time remaining to complete simulation: 1 days, 8 hours, 33 minutes, 59 seconds
  Estimated time remaining to next output: 5 minutes, 43 seconds
Output 398/738: t=6590000.0 yr, dE/E0=9.18e-07, N=793
  Estimated time remaining to complete simulation: 1 days, 8 hours, 27 minutes, 47 seconds
  Estimated time remaining to next output: 5 minutes, 43 seconds
Output 399/738: t=6600000.0 yr, dE/E0=9.10e-07, N=793
  Estimated time remaining to complete simulation: 1 days, 8 hours, 21 minutes, 31 seconds
  Estimated time remaining to next output: 5 minutes, 43 seconds
Output 400/738: t=6610000.0 yr, dE/E0=9.30e-07, N=793
  Estimated time remaining to complete simulation: 1 days, 8 hours, 15 minutes, 27 seconds
  Estimated time remaining to next output: 5 minutes, 43 seconds
Output 401/738: t=6620000.0 yr, dE/E0=9.28e-07, N=793
  Estimated time remaining to complete simulation: 1 days, 8 hours, 9 minutes, 27 seconds
  Estimated time remaining to next output: 5 minutes, 43 seconds
Output 402/738: t=6630000.0 yr, dE/E0=9.11e-07, N=793
  Estimated time remaining to complete simulation: 1 days, 8 hours, 3 minutes, 19 seconds
  Estimated time remaining to next output: 5 minutes, 43 seconds
Output 403/738: t=6640000.0 yr, dE/E0=9.02e-07, N=793
  Estimated time remaining to complete simulation: 1 days, 7 hours, 57 minutes, 19 seconds
  Estimated time remaining to next output: 5 minutes, 43 seconds
Output 404/738: t=6650000.0 yr, dE/E0=9.15e-07, N=793
  Estimated time remaining to complete simulation: 1 days, 7 hours, 51 minutes, 3 seconds
  Estimated time remaining to next output: 5 minutes, 43 seconds
Output 405/738: t=6660000.0 yr, dE/E0=9.18e-07, N=793
  Estimated time remaining to complete simulation: 1 days, 7 hours, 45 minutes, 1 seconds
  Estimated time remaining to next output: 5 minutes, 43 seconds
Output 406/738: t=6670000.0 yr, dE/E0=9.20e-07, N=793
  Estimated time remaining to complete simulation: 1 days, 7 hours, 38 minutes, 55 seconds
  Estimated time remaining to next output: 5 minutes, 43 seconds
Output 407/738: t=6680000.0 yr, dE/E0=9.10e-07, N=793
  Estimated time remaining to complete simulation: 1 days, 7 hours, 32 minutes, 44 seconds
  Estimated time remaining to next output: 5 minutes, 43 seconds
Output 408/738: t=6690000.0 yr, dE/E0=9.16e-07, N=793
  Estimated time remaining to complete simulation: 1 days, 7 hours, 26 minutes, 38 seconds
  Estimated time remaining to next output: 5 minutes, 43 seconds
Output 409/738: t=6700000.0 yr, dE/E0=9.21e-07, N=793
  Estimated time remaining to complete simulation: 1 days, 7 hours, 20 minutes, 43 seconds
  Estimated time remaining to next output: 5 minutes, 42 seconds
Output 410/738: t=6710000.0 yr, dE/E0=9.09e-07, N=793
  Estimated time remaining to complete simulation: 1 days, 7 hours, 14 minutes, 25 seconds
  Estimated time remaining to next output: 5 minutes, 42 seconds
Output 411/738: t=6720000.0 yr, dE/E0=9.33e-07, N=793
  Estimated time remaining to complete simulation: 1 days, 7 hours, 8 minutes, 19 seconds
  Estimated time remaining to next output: 5 minutes, 42 seconds
Output 412/738: t=6730000.0 yr, dE/E0=9.22e-07, N=793
  Estimated time remaining to complete simulation: 1 days, 7 hours, 2 minutes, 10 seconds
  Estimated time remaining to next output: 5 minutes, 42 seconds
Output 413/738: t=6740000.0 yr, dE/E0=9.24e-07, N=793
  Estimated time remaining to complete simulation: 1 days, 6 hours, 55 minutes, 58 seconds
  Estimated time remaining to next output: 5 minutes, 42 seconds
A particle escaped (r>exit_max_distance).
Removing escaped particle at index 761
Remaining particles: 792
Output 414/738: t=6743925.0 yr, dE/E0=1.02e-06, N=792
  Estimated time remaining to complete simulation: 1 days, 6 hours, 47 minutes, 24 seconds
  Estimated time remaining to next output: 5 minutes, 42 seconds
Output 415/738: t=6760000.0 yr, dE/E0=1.00e-06, N=792
  Estimated time remaining to complete simulation: 1 days, 6 hours, 43 minutes, 36 seconds
  Estimated time remaining to next output: 5 minutes, 42 seconds
Output 416/738: t=6770000.0 yr, dE/E0=1.01e-06, N=792
  Estimated time remaining to complete simulation: 1 days, 6 hours, 37 minutes, 36 seconds
  Estimated time remaining to next output: 5 minutes, 42 seconds
Output 417/738: t=6780000.0 yr, dE/E0=1.03e-06, N=792
  Estimated time remaining to complete simulation: 1 days, 6 hours, 31 minutes, 33 seconds
  Estimated time remaining to next output: 5 minutes, 42 seconds
Output 418/738: t=6790000.0 yr, dE/E0=1.03e-06, N=792
  Estimated time remaining to complete simulation: 1 days, 6 hours, 25 minutes, 36 seconds
  Estimated time remaining to next output: 5 minutes, 42 seconds
Output 419/738: t=6800000.0 yr, dE/E0=1.03e-06, N=792
  Estimated time remaining to complete simulation: 1 days, 6 hours, 19 minutes, 38 seconds
  Estimated time remaining to next output: 5 minutes, 42 seconds
Output 420/738: t=6810000.0 yr, dE/E0=1.03e-06, N=792
  Estimated time remaining to complete simulation: 1 days, 6 hours, 13 minutes, 45 seconds
  Estimated time remaining to next output: 5 minutes, 42 seconds
Output 421/738: t=6820000.0 yr, dE/E0=1.02e-06, N=792
  Estimated time remaining to complete simulation: 1 days, 6 hours, 7 minutes, 32 seconds
  Estimated time remaining to next output: 5 minutes, 42 seconds
Output 422/738: t=6830000.0 yr, dE/E0=1.03e-06, N=792
  Estimated time remaining to complete simulation: 1 days, 6 hours, 1 minutes, 30 seconds
  Estimated time remaining to next output: 5 minutes, 42 seconds
Output 423/738: t=6840000.0 yr, dE/E0=1.04e-06, N=792
  Estimated time remaining to complete simulation: 1 days, 5 hours, 55 minutes, 26 seconds
  Estimated time remaining to next output: 5 minutes, 41 seconds
Output 424/738: t=6850000.0 yr, dE/E0=1.04e-06, N=792
  Estimated time remaining to complete simulation: 1 days, 5 hours, 49 minutes, 18 seconds
  Estimated time remaining to next output: 5 minutes, 41 seconds
Output 425/738: t=6860000.0 yr, dE/E0=1.02e-06, N=792
  Estimated time remaining to complete simulation: 1 days, 5 hours, 43 minutes, 8 seconds
  Estimated time remaining to next output: 5 minutes, 41 seconds
Output 426/738: t=6870000.0 yr, dE/E0=1.01e-06, N=792
  Estimated time remaining to complete simulation: 1 days, 5 hours, 37 minutes, 9 seconds
  Estimated time remaining to next output: 5 minutes, 41 seconds
Output 427/738: t=6880000.0 yr, dE/E0=1.03e-06, N=792
  Estimated time remaining to complete simulation: 1 days, 5 hours, 31 minutes, 1 seconds
  Estimated time remaining to next output: 5 minutes, 41 seconds
Output 428/738: t=6890000.0 yr, dE/E0=1.03e-06, N=792
  Estimated time remaining to complete simulation: 1 days, 5 hours, 25 minutes, 14 seconds
  Estimated time remaining to next output: 5 minutes, 41 seconds
Output 429/738: t=6900000.0 yr, dE/E0=1.03e-06, N=792
  Estimated time remaining to complete simulation: 1 days, 5 hours, 19 minutes, 10 seconds
  Estimated time remaining to next output: 5 minutes, 41 seconds
Output 430/738: t=6910000.0 yr, dE/E0=1.03e-06, N=792
  Estimated time remaining to complete simulation: 1 days, 5 hours, 13 minutes, 5 seconds
  Estimated time remaining to next output: 5 minutes, 41 seconds
Output 431/738: t=6920000.0 yr, dE/E0=1.03e-06, N=792
  Estimated time remaining to complete simulation: 1 days, 5 hours, 6 minutes, 51 seconds
  Estimated time remaining to next output: 5 minutes, 41 seconds
Output 432/738: t=6930000.0 yr, dE/E0=1.04e-06, N=792
  Estimated time remaining to complete simulation: 1 days, 5 hours, 36 seconds
  Estimated time remaining to next output: 5 minutes, 41 seconds
A particle escaped (r>exit_max_distance).
Removing escaped particle at index 455
Remaining particles: 791
Output 433/738: t=6933756.8 yr, dE/E0=1.18e-06, N=791
  Estimated time remaining to complete simulation: 1 days, 4 hours, 52 minutes, 17 seconds
  Estimated time remaining to next output: 5 minutes, 40 seconds
Output 434/738: t=6950000.0 yr, dE/E0=1.19e-06, N=791
  Estimated time remaining to complete simulation: 1 days, 4 hours, 48 minutes, 45 seconds
  Estimated time remaining to next output: 5 minutes, 41 seconds
Output 435/738: t=6960000.0 yr, dE/E0=1.18e-06, N=791
  Estimated time remaining to complete simulation: 1 days, 4 hours, 42 minutes, 45 seconds
  Estimated time remaining to next output: 5 minutes, 41 seconds
Output 436/738: t=6970000.0 yr, dE/E0=1.18e-06, N=791
  Estimated time remaining to complete simulation: 1 days, 4 hours, 36 minutes, 49 seconds
  Estimated time remaining to next output: 5 minutes, 41 seconds
Output 437/738: t=6980000.0 yr, dE/E0=1.19e-06, N=791
  Estimated time remaining to complete simulation: 1 days, 4 hours, 30 minutes, 50 seconds
  Estimated time remaining to next output: 5 minutes, 41 seconds
Output 438/738: t=6990000.0 yr, dE/E0=1.17e-06, N=791
  Estimated time remaining to complete simulation: 1 days, 4 hours, 24 minutes, 44 seconds
  Estimated time remaining to next output: 5 minutes, 40 seconds
Output 439/738: t=7000000.0 yr, dE/E0=1.17e-06, N=791
  Estimated time remaining to complete simulation: 1 days, 4 hours, 18 minutes, 43 seconds
  Estimated time remaining to next output: 5 minutes, 40 seconds
Output 440/738: t=7010000.0 yr, dE/E0=1.17e-06, N=791
  Estimated time remaining to complete simulation: 1 days, 4 hours, 12 minutes, 49 seconds
  Estimated time remaining to next output: 5 minutes, 40 seconds
Output 441/738: t=7020000.0 yr, dE/E0=1.19e-06, N=791
  Estimated time remaining to complete simulation: 1 days, 4 hours, 6 minutes, 49 seconds
  Estimated time remaining to next output: 5 minutes, 40 seconds
Output 442/738: t=7030000.0 yr, dE/E0=1.20e-06, N=791
  Estimated time remaining to complete simulation: 1 days, 4 hours, 46 seconds
  Estimated time remaining to next output: 5 minutes, 40 seconds
Output 443/738: t=7040000.0 yr, dE/E0=1.19e-06, N=791
  Estimated time remaining to complete simulation: 1 days, 3 hours, 54 minutes, 53 seconds
  Estimated time remaining to next output: 5 minutes, 40 seconds
Output 444/738: t=7050000.0 yr, dE/E0=1.20e-06, N=791
  Estimated time remaining to complete simulation: 1 days, 3 hours, 49 minutes
  Estimated time remaining to next output: 5 minutes, 40 seconds
Output 445/738: t=7060000.0 yr, dE/E0=1.19e-06, N=791
  Estimated time remaining to complete simulation: 1 days, 3 hours, 42 minutes, 50 seconds
  Estimated time remaining to next output: 5 minutes, 40 seconds
Output 446/738: t=7070000.0 yr, dE/E0=1.18e-06, N=791
  Estimated time remaining to complete simulation: 1 days, 3 hours, 36 minutes, 38 seconds
  Estimated time remaining to next output: 5 minutes, 40 seconds
Output 447/738: t=7080000.0 yr, dE/E0=1.18e-06, N=791
  Estimated time remaining to complete simulation: 1 days, 3 hours, 30 minutes, 32 seconds
  Estimated time remaining to next output: 5 minutes, 40 seconds
Output 448/738: t=7090000.0 yr, dE/E0=1.19e-06, N=791
  Estimated time remaining to complete simulation: 1 days, 3 hours, 24 minutes, 41 seconds
  Estimated time remaining to next output: 5 minutes, 40 seconds
Output 449/738: t=7100000.0 yr, dE/E0=1.19e-06, N=791
  Estimated time remaining to complete simulation: 1 days, 3 hours, 18 minutes, 43 seconds
  Estimated time remaining to next output: 5 minutes, 40 seconds
Output 450/738: t=7110000.0 yr, dE/E0=1.17e-06, N=791
  Estimated time remaining to complete simulation: 1 days, 3 hours, 12 minutes, 42 seconds
  Estimated time remaining to next output: 5 minutes, 40 seconds
Output 451/738: t=7120000.0 yr, dE/E0=1.18e-06, N=791
  Estimated time remaining to complete simulation: 1 days, 3 hours, 6 minutes, 42 seconds
  Estimated time remaining to next output: 5 minutes, 40 seconds
Output 452/738: t=7130000.0 yr, dE/E0=1.18e-06, N=791
  Estimated time remaining to complete simulation: 1 days, 3 hours, 50 seconds
  Estimated time remaining to next output: 5 minutes, 40 seconds
Output 453/738: t=7140000.0 yr, dE/E0=1.19e-06, N=791
  Estimated time remaining to complete simulation: 1 days, 2 hours, 54 minutes, 50 seconds
  Estimated time remaining to next output: 5 minutes, 39 seconds
Output 454/738: t=7150000.0 yr, dE/E0=1.19e-06, N=791
  Estimated time remaining to complete simulation: 1 days, 2 hours, 48 minutes, 47 seconds
  Estimated time remaining to next output: 5 minutes, 39 seconds
Output 455/738: t=7160000.0 yr, dE/E0=1.20e-06, N=791
  Estimated time remaining to complete simulation: 1 days, 2 hours, 42 minutes, 46 seconds
  Estimated time remaining to next output: 5 minutes, 39 seconds
Output 456/738: t=7170000.0 yr, dE/E0=1.18e-06, N=791
  Estimated time remaining to complete simulation: 1 days, 2 hours, 36 minutes, 39 seconds
  Estimated time remaining to next output: 5 minutes, 39 seconds
Output 457/738: t=7180000.0 yr, dE/E0=1.18e-06, N=791
  Estimated time remaining to complete simulation: 1 days, 2 hours, 30 minutes, 39 seconds
  Estimated time remaining to next output: 5 minutes, 39 seconds
Output 458/738: t=7190000.0 yr, dE/E0=1.19e-06, N=791
  Estimated time remaining to complete simulation: 1 days, 2 hours, 24 minutes, 43 seconds
  Estimated time remaining to next output: 5 minutes, 39 seconds
Output 459/738: t=7200000.0 yr, dE/E0=1.19e-06, N=791
  Estimated time remaining to complete simulation: 1 days, 2 hours, 18 minutes, 55 seconds
  Estimated time remaining to next output: 5 minutes, 39 seconds
Output 460/738: t=7210000.0 yr, dE/E0=1.19e-06, N=791
  Estimated time remaining to complete simulation: 1 days, 2 hours, 13 minutes, 4 seconds
  Estimated time remaining to next output: 5 minutes, 39 seconds
Output 461/738: t=7220000.0 yr, dE/E0=1.20e-06, N=791
  Estimated time remaining to complete simulation: 1 days, 2 hours, 7 minutes, 6 seconds
  Estimated time remaining to next output: 5 minutes, 39 seconds
Output 462/738: t=7230000.0 yr, dE/E0=1.18e-06, N=791
  Estimated time remaining to complete simulation: 1 days, 2 hours, 1 minutes, 18 seconds
  Estimated time remaining to next output: 5 minutes, 39 seconds
Output 463/738: t=7240000.0 yr, dE/E0=1.18e-06, N=791
  Estimated time remaining to complete simulation: 1 days, 1 hours, 55 minutes, 42 seconds
  Estimated time remaining to next output: 5 minutes, 39 seconds
Output 464/738: t=7250000.0 yr, dE/E0=1.18e-06, N=791
  Estimated time remaining to complete simulation: 1 days, 1 hours, 49 minutes, 43 seconds
  Estimated time remaining to next output: 5 minutes, 39 seconds
Output 465/738: t=7260000.0 yr, dE/E0=1.18e-06, N=791
  Estimated time remaining to complete simulation: 1 days, 1 hours, 43 minutes, 50 seconds
  Estimated time remaining to next output: 5 minutes, 39 seconds
Output 466/738: t=7270000.0 yr, dE/E0=1.19e-06, N=791
  Estimated time remaining to complete simulation: 1 days, 1 hours, 37 minutes, 57 seconds
  Estimated time remaining to next output: 5 minutes, 39 seconds
Output 467/738: t=7280000.0 yr, dE/E0=1.19e-06, N=791
  Estimated time remaining to complete simulation: 1 days, 1 hours, 31 minutes, 54 seconds
  Estimated time remaining to next output: 5 minutes, 39 seconds
Output 468/738: t=7290000.0 yr, dE/E0=1.19e-06, N=791
  Estimated time remaining to complete simulation: 1 days, 1 hours, 26 minutes, 2 seconds
  Estimated time remaining to next output: 5 minutes, 39 seconds
Output 469/738: t=7300000.0 yr, dE/E0=1.18e-06, N=791
  Estimated time remaining to complete simulation: 1 days, 1 hours, 20 minutes, 10 seconds
  Estimated time remaining to next output: 5 minutes, 39 seconds
Output 470/738: t=7310000.0 yr, dE/E0=1.19e-06, N=791
  Estimated time remaining to complete simulation: 1 days, 1 hours, 14 minutes, 11 seconds
  Estimated time remaining to next output: 5 minutes, 38 seconds
Output 471/738: t=7320000.0 yr, dE/E0=1.20e-06, N=791
  Estimated time remaining to complete simulation: 1 days, 1 hours, 8 minutes, 19 seconds
  Estimated time remaining to next output: 5 minutes, 38 seconds
Output 472/738: t=7330000.0 yr, dE/E0=1.18e-06, N=791
  Estimated time remaining to complete simulation: 1 days, 1 hours, 2 minutes, 13 seconds
  Estimated time remaining to next output: 5 minutes, 38 seconds
Output 473/738: t=7340000.0 yr, dE/E0=1.19e-06, N=791
  Estimated time remaining to complete simulation: 1 days, 56 minutes, 18 seconds
  Estimated time remaining to next output: 5 minutes, 38 seconds
Output 474/738: t=7350000.0 yr, dE/E0=1.18e-06, N=791
  Estimated time remaining to complete simulation: 1 days, 50 minutes, 34 seconds
  Estimated time remaining to next output: 5 minutes, 38 seconds
A particle escaped (r>exit_max_distance).
Removing escaped particle at index 743
Remaining particles: 790
Output 475/738: t=7351906.4 yr, dE/E0=1.26e-06, N=790
  Estimated time remaining to complete simulation: 1 days, 42 minutes, 18 seconds
  Estimated time remaining to next output: 5 minutes, 38 seconds
Output 476/738: t=7370000.0 yr, dE/E0=1.26e-06, N=790
  Estimated time remaining to complete simulation: 1 days, 38 minutes, 42 seconds
  Estimated time remaining to next output: 5 minutes, 38 seconds
Output 477/738: t=7380000.0 yr, dE/E0=1.28e-06, N=790
  Estimated time remaining to complete simulation: 1 days, 32 minutes, 47 seconds
  Estimated time remaining to next output: 5 minutes, 38 seconds
Output 478/738: t=7390000.0 yr, dE/E0=1.29e-06, N=790
  Estimated time remaining to complete simulation: 1 days, 26 minutes, 50 seconds
  Estimated time remaining to next output: 5 minutes, 38 seconds
Output 479/738: t=7400000.0 yr, dE/E0=1.30e-06, N=790
  Estimated time remaining to complete simulation: 1 days, 21 minutes, 2 seconds
  Estimated time remaining to next output: 5 minutes, 38 seconds
Output 480/738: t=7410000.0 yr, dE/E0=1.27e-06, N=790
  Estimated time remaining to complete simulation: 1 days, 15 minutes, 16 seconds
  Estimated time remaining to next output: 5 minutes, 38 seconds
Output 481/738: t=7420000.0 yr, dE/E0=1.27e-06, N=790
  Estimated time remaining to complete simulation: 1 days, 9 minutes, 25 seconds
  Estimated time remaining to next output: 5 minutes, 38 seconds
Output 482/738: t=7430000.0 yr, dE/E0=1.27e-06, N=790
  Estimated time remaining to complete simulation: 1 days, 3 minutes, 40 seconds
  Estimated time remaining to next output: 5 minutes, 38 seconds
Output 483/738: t=7440000.0 yr, dE/E0=1.27e-06, N=790
  Estimated time remaining to complete simulation: 23 hours, 57 minutes, 45 seconds
  Estimated time remaining to next output: 5 minutes, 38 seconds
Output 484/738: t=7450000.0 yr, dE/E0=1.27e-06, N=790
  Estimated time remaining to complete simulation: 23 hours, 51 minutes, 52 seconds
  Estimated time remaining to next output: 5 minutes, 38 seconds
Output 485/738: t=7460000.0 yr, dE/E0=1.27e-06, N=790
  Estimated time remaining to complete simulation: 23 hours, 45 minutes, 58 seconds
  Estimated time remaining to next output: 5 minutes, 38 seconds
Output 486/738: t=7470000.0 yr, dE/E0=1.27e-06, N=790
  Estimated time remaining to complete simulation: 23 hours, 40 minutes, 5 seconds
  Estimated time remaining to next output: 5 minutes, 38 seconds
Output 487/738: t=7480000.0 yr, dE/E0=1.27e-06, N=790
  Estimated time remaining to complete simulation: 23 hours, 35 minutes, 31 seconds
  Estimated time remaining to next output: 5 minutes, 38 seconds
Output 488/738: t=7490000.0 yr, dE/E0=1.27e-06, N=790
  Estimated time remaining to complete simulation: 23 hours, 31 minutes, 13 seconds
  Estimated time remaining to next output: 5 minutes, 38 seconds
Output 489/738: t=7500000.0 yr, dE/E0=1.26e-06, N=790
  Estimated time remaining to complete simulation: 23 hours, 27 minutes, 31 seconds
  Estimated time remaining to next output: 5 minutes, 39 seconds
Output 490/738: t=7510000.0 yr, dE/E0=1.28e-06, N=790
  Estimated time remaining to complete simulation: 23 hours, 23 minutes, 4 seconds
  Estimated time remaining to next output: 5 minutes, 39 seconds
Output 491/738: t=7520000.0 yr, dE/E0=1.26e-06, N=790
  Estimated time remaining to complete simulation: 23 hours, 18 minutes, 46 seconds
  Estimated time remaining to next output: 5 minutes, 39 seconds
Output 492/738: t=7530000.0 yr, dE/E0=1.27e-06, N=790
  Estimated time remaining to complete simulation: 23 hours, 14 minutes, 20 seconds
  Estimated time remaining to next output: 5 minutes, 40 seconds
Output 493/738: t=7540000.0 yr, dE/E0=1.25e-06, N=790
  Estimated time remaining to complete simulation: 23 hours, 10 minutes
  Estimated time remaining to next output: 5 minutes, 40 seconds
Output 494/738: t=7550000.0 yr, dE/E0=1.27e-06, N=790
  Estimated time remaining to complete simulation: 23 hours, 5 minutes, 53 seconds
  Estimated time remaining to next output: 5 minutes, 40 seconds
Output 495/738: t=7560000.0 yr, dE/E0=1.26e-06, N=790
  Estimated time remaining to complete simulation: 23 hours, 1 minutes, 53 seconds
  Estimated time remaining to next output: 5 minutes, 41 seconds
Output 496/738: t=7570000.0 yr, dE/E0=1.27e-06, N=790
  Estimated time remaining to complete simulation: 22 hours, 57 minutes, 30 seconds
  Estimated time remaining to next output: 5 minutes, 41 seconds
Output 497/738: t=7580000.0 yr, dE/E0=1.25e-06, N=790
  Estimated time remaining to complete simulation: 22 hours, 53 minutes, 5 seconds
  Estimated time remaining to next output: 5 minutes, 41 seconds
Output 498/738: t=7590000.0 yr, dE/E0=1.26e-06, N=790
  Estimated time remaining to complete simulation: 22 hours, 48 minutes, 31 seconds
  Estimated time remaining to next output: 5 minutes, 42 seconds
Output 499/738: t=7600000.0 yr, dE/E0=1.26e-06, N=790
  Estimated time remaining to complete simulation: 22 hours, 44 minutes, 15 seconds
  Estimated time remaining to next output: 5 minutes, 42 seconds
Output 500/738: t=7610000.0 yr, dE/E0=1.24e-06, N=790
  Estimated time remaining to complete simulation: 22 hours, 38 minutes, 12 seconds
  Estimated time remaining to next output: 5 minutes, 42 seconds
Output 501/738: t=7620000.0 yr, dE/E0=1.26e-06, N=790
  Estimated time remaining to complete simulation: 22 hours, 32 minutes, 21 seconds
  Estimated time remaining to next output: 5 minutes, 42 seconds
Output 502/738: t=7630000.0 yr, dE/E0=1.26e-06, N=790
  Estimated time remaining to complete simulation: 22 hours, 26 minutes, 21 seconds
  Estimated time remaining to next output: 5 minutes, 42 seconds
Output 503/738: t=7640000.0 yr, dE/E0=1.27e-06, N=790
  Estimated time remaining to complete simulation: 22 hours, 20 minutes, 28 seconds
  Estimated time remaining to next output: 5 minutes, 42 seconds
Output 504/738: t=7650000.0 yr, dE/E0=1.26e-06, N=790
  Estimated time remaining to complete simulation: 22 hours, 14 minutes, 27 seconds
  Estimated time remaining to next output: 5 minutes, 42 seconds
Output 505/738: t=7660000.0 yr, dE/E0=1.26e-06, N=790
  Estimated time remaining to complete simulation: 22 hours, 8 minutes, 32 seconds
  Estimated time remaining to next output: 5 minutes, 42 seconds
Output 506/738: t=7670000.0 yr, dE/E0=1.25e-06, N=790
  Estimated time remaining to complete simulation: 22 hours, 2 minutes, 40 seconds
  Estimated time remaining to next output: 5 minutes, 42 seconds
Output 507/738: t=7680000.0 yr, dE/E0=1.26e-06, N=790
  Estimated time remaining to complete simulation: 21 hours, 56 minutes, 41 seconds
  Estimated time remaining to next output: 5 minutes, 41 seconds
Output 508/738: t=7690000.0 yr, dE/E0=1.27e-06, N=790
  Estimated time remaining to complete simulation: 21 hours, 50 minutes, 41 seconds
  Estimated time remaining to next output: 5 minutes, 41 seconds
Output 509/738: t=7700000.0 yr, dE/E0=1.27e-06, N=790
  Estimated time remaining to complete simulation: 21 hours, 44 minutes, 44 seconds
  Estimated time remaining to next output: 5 minutes, 41 seconds
Output 510/738: t=7710000.0 yr, dE/E0=1.27e-06, N=790
  Estimated time remaining to complete simulation: 21 hours, 38 minutes, 48 seconds
  Estimated time remaining to next output: 5 minutes, 41 seconds
Output 511/738: t=7720000.0 yr, dE/E0=1.25e-06, N=790
  Estimated time remaining to complete simulation: 21 hours, 32 minutes, 49 seconds
  Estimated time remaining to next output: 5 minutes, 41 seconds
Output 512/738: t=7730000.0 yr, dE/E0=1.26e-06, N=790
  Estimated time remaining to complete simulation: 21 hours, 26 minutes, 46 seconds
  Estimated time remaining to next output: 5 minutes, 41 seconds
Output 513/738: t=7740000.0 yr, dE/E0=1.26e-06, N=790
  Estimated time remaining to complete simulation: 21 hours, 20 minutes, 53 seconds
  Estimated time remaining to next output: 5 minutes, 41 seconds
Output 514/738: t=7750000.0 yr, dE/E0=1.27e-06, N=790
  Estimated time remaining to complete simulation: 21 hours, 15 minutes, 3 seconds
  Estimated time remaining to next output: 5 minutes, 41 seconds
Output 515/738: t=7760000.0 yr, dE/E0=1.27e-06, N=790
  Estimated time remaining to complete simulation: 21 hours, 9 minutes, 1 seconds
  Estimated time remaining to next output: 5 minutes, 41 seconds
Output 516/738: t=7770000.0 yr, dE/E0=1.26e-06, N=790
  Estimated time remaining to complete simulation: 21 hours, 3 minutes, 3 seconds
  Estimated time remaining to next output: 5 minutes, 41 seconds
Output 517/738: t=7780000.0 yr, dE/E0=1.27e-06, N=790
  Estimated time remaining to complete simulation: 20 hours, 57 minutes, 7 seconds
  Estimated time remaining to next output: 5 minutes, 41 seconds
Output 518/738: t=7790000.0 yr, dE/E0=1.26e-06, N=790
  Estimated time remaining to complete simulation: 20 hours, 51 minutes, 5 seconds
  Estimated time remaining to next output: 5 minutes, 41 seconds
Output 519/738: t=7800000.0 yr, dE/E0=1.27e-06, N=790
  Estimated time remaining to complete simulation: 20 hours, 45 minutes, 10 seconds
  Estimated time remaining to next output: 5 minutes, 41 seconds
Output 520/738: t=7810000.0 yr, dE/E0=1.29e-06, N=790
  Estimated time remaining to complete simulation: 20 hours, 39 minutes, 18 seconds
  Estimated time remaining to next output: 5 minutes, 41 seconds
Output 521/738: t=7820000.0 yr, dE/E0=1.30e-06, N=790
  Estimated time remaining to complete simulation: 20 hours, 33 minutes, 23 seconds
  Estimated time remaining to next output: 5 minutes, 41 seconds
Output 522/738: t=7830000.0 yr, dE/E0=1.30e-06, N=790
  Estimated time remaining to complete simulation: 20 hours, 27 minutes, 31 seconds
  Estimated time remaining to next output: 5 minutes, 40 seconds
Output 523/738: t=7840000.0 yr, dE/E0=1.29e-06, N=790
  Estimated time remaining to complete simulation: 20 hours, 21 minutes, 39 seconds
  Estimated time remaining to next output: 5 minutes, 40 seconds
Output 524/738: t=7850000.0 yr, dE/E0=1.29e-06, N=790
  Estimated time remaining to complete simulation: 20 hours, 15 minutes, 47 seconds
  Estimated time remaining to next output: 5 minutes, 40 seconds
Output 525/738: t=7860000.0 yr, dE/E0=1.30e-06, N=790
  Estimated time remaining to complete simulation: 20 hours, 9 minutes, 58 seconds
  Estimated time remaining to next output: 5 minutes, 40 seconds
Output 526/738: t=7870000.0 yr, dE/E0=1.30e-06, N=790
  Estimated time remaining to complete simulation: 20 hours, 4 minutes, 5 seconds
  Estimated time remaining to next output: 5 minutes, 40 seconds
Output 527/738: t=7880000.0 yr, dE/E0=1.31e-06, N=790
  Estimated time remaining to complete simulation: 19 hours, 58 minutes, 12 seconds
  Estimated time remaining to next output: 5 minutes, 40 seconds
Output 528/738: t=7890000.0 yr, dE/E0=1.29e-06, N=790
  Estimated time remaining to complete simulation: 19 hours, 52 minutes, 23 seconds
  Estimated time remaining to next output: 5 minutes, 40 seconds
Output 529/738: t=7900000.0 yr, dE/E0=1.30e-06, N=790
  Estimated time remaining to complete simulation: 19 hours, 46 minutes, 28 seconds
  Estimated time remaining to next output: 5 minutes, 40 seconds
Output 530/738: t=7910000.0 yr, dE/E0=1.28e-06, N=790
  Estimated time remaining to complete simulation: 19 hours, 40 minutes, 27 seconds
  Estimated time remaining to next output: 5 minutes, 40 seconds
Output 531/738: t=7920000.0 yr, dE/E0=1.29e-06, N=790
  Estimated time remaining to complete simulation: 19 hours, 34 minutes, 40 seconds
  Estimated time remaining to next output: 5 minutes, 40 seconds
Output 532/738: t=7930000.0 yr, dE/E0=1.30e-06, N=790
  Estimated time remaining to complete simulation: 19 hours, 28 minutes, 47 seconds
  Estimated time remaining to next output: 5 minutes, 40 seconds
Output 533/738: t=7940000.0 yr, dE/E0=1.29e-06, N=790
  Estimated time remaining to complete simulation: 19 hours, 22 minutes, 58 seconds
  Estimated time remaining to next output: 5 minutes, 40 seconds
Output 534/738: t=7950000.0 yr, dE/E0=1.29e-06, N=790
  Estimated time remaining to complete simulation: 19 hours, 17 minutes, 8 seconds
  Estimated time remaining to next output: 5 minutes, 40 seconds
Output 535/738: t=7960000.0 yr, dE/E0=1.27e-06, N=790
  Estimated time remaining to complete simulation: 19 hours, 11 minutes, 24 seconds
  Estimated time remaining to next output: 5 minutes, 40 seconds
Output 536/738: t=7970000.0 yr, dE/E0=1.29e-06, N=790
  Estimated time remaining to complete simulation: 19 hours, 5 minutes, 33 seconds
  Estimated time remaining to next output: 5 minutes, 40 seconds
Output 537/738: t=7980000.0 yr, dE/E0=1.28e-06, N=790
  Estimated time remaining to complete simulation: 18 hours, 59 minutes, 46 seconds
  Estimated time remaining to next output: 5 minutes, 40 seconds
Output 538/738: t=7990000.0 yr, dE/E0=1.29e-06, N=790
  Estimated time remaining to complete simulation: 18 hours, 53 minutes, 54 seconds
  Estimated time remaining to next output: 5 minutes, 40 seconds
Output 539/738: t=8000000.0 yr, dE/E0=1.30e-06, N=790
  Estimated time remaining to complete simulation: 18 hours, 47 minutes, 57 seconds
  Estimated time remaining to next output: 5 minutes, 40 seconds
Output 540/738: t=8010000.0 yr, dE/E0=1.29e-06, N=790
  Estimated time remaining to complete simulation: 18 hours, 42 minutes, 2 seconds
  Estimated time remaining to next output: 5 minutes, 40 seconds
Output 541/738: t=8020000.0 yr, dE/E0=1.28e-06, N=790
  Estimated time remaining to complete simulation: 18 hours, 36 minutes, 12 seconds
  Estimated time remaining to next output: 5 minutes, 39 seconds
Output 542/738: t=8030000.0 yr, dE/E0=1.28e-06, N=790
  Estimated time remaining to complete simulation: 18 hours, 30 minutes, 17 seconds
  Estimated time remaining to next output: 5 minutes, 39 seconds
Output 543/738: t=8040000.0 yr, dE/E0=1.29e-06, N=790
  Estimated time remaining to complete simulation: 18 hours, 24 minutes, 23 seconds
  Estimated time remaining to next output: 5 minutes, 39 seconds
Output 544/738: t=8050000.0 yr, dE/E0=1.28e-06, N=790
  Estimated time remaining to complete simulation: 18 hours, 18 minutes, 30 seconds
  Estimated time remaining to next output: 5 minutes, 39 seconds
Output 545/738: t=8060000.0 yr, dE/E0=1.30e-06, N=790
  Estimated time remaining to complete simulation: 18 hours, 12 minutes, 38 seconds
  Estimated time remaining to next output: 5 minutes, 39 seconds
Output 546/738: t=8070000.0 yr, dE/E0=1.29e-06, N=790
  Estimated time remaining to complete simulation: 18 hours, 6 minutes, 42 seconds
  Estimated time remaining to next output: 5 minutes, 39 seconds
Output 547/738: t=8080000.0 yr, dE/E0=1.28e-06, N=790
  Estimated time remaining to complete simulation: 18 hours, 52 seconds
  Estimated time remaining to next output: 5 minutes, 39 seconds
Output 548/738: t=8090000.0 yr, dE/E0=1.29e-06, N=790
  Estimated time remaining to complete simulation: 17 hours, 55 minutes, 5 seconds
  Estimated time remaining to next output: 5 minutes, 39 seconds
Output 549/738: t=8100000.0 yr, dE/E0=1.29e-06, N=790
  Estimated time remaining to complete simulation: 17 hours, 49 minutes, 14 seconds
  Estimated time remaining to next output: 5 minutes, 39 seconds
Output 550/738: t=8110000.0 yr, dE/E0=1.32e-06, N=790
  Estimated time remaining to complete simulation: 17 hours, 43 minutes, 43 seconds
  Estimated time remaining to next output: 5 minutes, 39 seconds
Output 551/738: t=8120000.0 yr, dE/E0=1.30e-06, N=790
  Estimated time remaining to complete simulation: 17 hours, 39 minutes, 1 seconds
  Estimated time remaining to next output: 5 minutes, 39 seconds
Output 552/738: t=8130000.0 yr, dE/E0=1.31e-06, N=790
  Estimated time remaining to complete simulation: 17 hours, 34 minutes, 20 seconds
  Estimated time remaining to next output: 5 minutes, 40 seconds
Output 553/738: t=8140000.0 yr, dE/E0=1.30e-06, N=790
  Estimated time remaining to complete simulation: 17 hours, 29 minutes, 32 seconds
  Estimated time remaining to next output: 5 minutes, 40 seconds
Output 554/738: t=8150000.0 yr, dE/E0=1.30e-06, N=790
  Estimated time remaining to complete simulation: 17 hours, 24 minutes, 45 seconds
  Estimated time remaining to next output: 5 minutes, 40 seconds
Output 555/738: t=8160000.0 yr, dE/E0=1.30e-06, N=790
  Estimated time remaining to complete simulation: 17 hours, 20 minutes, 4 seconds
  Estimated time remaining to next output: 5 minutes, 41 seconds
Output 556/738: t=8170000.0 yr, dE/E0=1.30e-06, N=790
  Estimated time remaining to complete simulation: 17 hours, 15 minutes, 16 seconds
  Estimated time remaining to next output: 5 minutes, 41 seconds
Output 557/738: t=8180000.0 yr, dE/E0=1.32e-06, N=790
  Estimated time remaining to complete simulation: 17 hours, 10 minutes, 32 seconds
  Estimated time remaining to next output: 5 minutes, 41 seconds
Output 558/738: t=8190000.0 yr, dE/E0=1.31e-06, N=790
  Estimated time remaining to complete simulation: 17 hours, 5 minutes, 40 seconds
  Estimated time remaining to next output: 5 minutes, 41 seconds
Output 559/738: t=8200000.0 yr, dE/E0=1.31e-06, N=790
  Estimated time remaining to complete simulation: 17 hours, 48 seconds
  Estimated time remaining to next output: 5 minutes, 42 seconds
Output 560/738: t=8210000.0 yr, dE/E0=1.30e-06, N=790
  Estimated time remaining to complete simulation: 16 hours, 55 minutes, 55 seconds
  Estimated time remaining to next output: 5 minutes, 42 seconds
Output 561/738: t=8220000.0 yr, dE/E0=1.28e-06, N=790
  Estimated time remaining to complete simulation: 16 hours, 51 minutes, 5 seconds
  Estimated time remaining to next output: 5 minutes, 42 seconds
Output 562/738: t=8230000.0 yr, dE/E0=1.30e-06, N=790
  Estimated time remaining to complete simulation: 16 hours, 46 minutes, 4 seconds
  Estimated time remaining to next output: 5 minutes, 42 seconds
Output 563/738: t=8240000.0 yr, dE/E0=1.31e-06, N=790
  Estimated time remaining to complete simulation: 16 hours, 41 minutes, 14 seconds
  Estimated time remaining to next output: 5 minutes, 43 seconds
Output 564/738: t=8250000.0 yr, dE/E0=1.29e-06, N=790
  Estimated time remaining to complete simulation: 16 hours, 36 minutes, 32 seconds
  Estimated time remaining to next output: 5 minutes, 43 seconds
Output 565/738: t=8260000.0 yr, dE/E0=1.30e-06, N=790
  Estimated time remaining to complete simulation: 16 hours, 31 minutes, 37 seconds
  Estimated time remaining to next output: 5 minutes, 43 seconds
Output 566/738: t=8270000.0 yr, dE/E0=1.29e-06, N=790
  Estimated time remaining to complete simulation: 16 hours, 26 minutes, 45 seconds
  Estimated time remaining to next output: 5 minutes, 44 seconds
Output 567/738: t=8280000.0 yr, dE/E0=1.29e-06, N=790
  Estimated time remaining to complete simulation: 16 hours, 21 minutes, 56 seconds
  Estimated time remaining to next output: 5 minutes, 44 seconds
Output 568/738: t=8290000.0 yr, dE/E0=1.31e-06, N=790
  Estimated time remaining to complete simulation: 16 hours, 17 minutes, 1 seconds
  Estimated time remaining to next output: 5 minutes, 44 seconds
Output 569/738: t=8300000.0 yr, dE/E0=1.31e-06, N=790
  Estimated time remaining to complete simulation: 16 hours, 12 minutes, 8 seconds
  Estimated time remaining to next output: 5 minutes, 45 seconds
Output 570/738: t=8310000.0 yr, dE/E0=1.31e-06, N=790
  Estimated time remaining to complete simulation: 16 hours, 7 minutes, 10 seconds
  Estimated time remaining to next output: 5 minutes, 45 seconds
Output 571/738: t=8320000.0 yr, dE/E0=1.29e-06, N=790
  Estimated time remaining to complete simulation: 16 hours, 2 minutes, 16 seconds
  Estimated time remaining to next output: 5 minutes, 45 seconds
Output 572/738: t=8330000.0 yr, dE/E0=1.30e-06, N=790
  Estimated time remaining to complete simulation: 15 hours, 56 minutes, 58 seconds
  Estimated time remaining to next output: 5 minutes, 45 seconds
Output 573/738: t=8340000.0 yr, dE/E0=1.29e-06, N=790
  Estimated time remaining to complete simulation: 15 hours, 51 minutes
  Estimated time remaining to next output: 5 minutes, 45 seconds
Output 574/738: t=8350000.0 yr, dE/E0=1.32e-06, N=790
  Estimated time remaining to complete simulation: 15 hours, 44 minutes, 59 seconds
  Estimated time remaining to next output: 5 minutes, 45 seconds
Output 575/738: t=8360000.0 yr, dE/E0=1.32e-06, N=790
  Estimated time remaining to complete simulation: 15 hours, 39 minutes
  Estimated time remaining to next output: 5 minutes, 45 seconds
Output 576/738: t=8370000.0 yr, dE/E0=1.32e-06, N=790
  Estimated time remaining to complete simulation: 15 hours, 33 minutes, 8 seconds
  Estimated time remaining to next output: 5 minutes, 45 seconds
A particle escaped (r>exit_max_distance).
Removing escaped particle at index 391
Remaining particles: 789
Output 577/738: t=8371626.1 yr, dE/E0=1.49e-06, N=789
  Estimated time remaining to complete simulation: 15 hours, 26 minutes, 2 seconds
  Estimated time remaining to next output: 5 minutes, 45 seconds
Output 578/738: t=8390000.0 yr, dE/E0=1.48e-06, N=789
  Estimated time remaining to complete simulation: 15 hours, 21 minutes, 10 seconds
  Estimated time remaining to next output: 5 minutes, 45 seconds
Output 579/738: t=8400000.0 yr, dE/E0=1.48e-06, N=789
  Estimated time remaining to complete simulation: 15 hours, 15 minutes, 15 seconds
  Estimated time remaining to next output: 5 minutes, 45 seconds
Output 580/738: t=8410000.0 yr, dE/E0=1.50e-06, N=789
  Estimated time remaining to complete simulation: 15 hours, 9 minutes, 15 seconds
  Estimated time remaining to next output: 5 minutes, 45 seconds
Output 581/738: t=8420000.0 yr, dE/E0=1.51e-06, N=789
  Estimated time remaining to complete simulation: 15 hours, 3 minutes, 15 seconds
  Estimated time remaining to next output: 5 minutes, 45 seconds
Output 582/738: t=8430000.0 yr, dE/E0=1.51e-06, N=789
  Estimated time remaining to complete simulation: 14 hours, 57 minutes, 16 seconds
  Estimated time remaining to next output: 5 minutes, 45 seconds
Output 583/738: t=8440000.0 yr, dE/E0=1.52e-06, N=789
  Estimated time remaining to complete simulation: 14 hours, 51 minutes, 24 seconds
  Estimated time remaining to next output: 5 minutes, 45 seconds
Output 584/738: t=8450000.0 yr, dE/E0=1.50e-06, N=789
  Estimated time remaining to complete simulation: 14 hours, 45 minutes, 26 seconds
  Estimated time remaining to next output: 5 minutes, 44 seconds
Output 585/738: t=8460000.0 yr, dE/E0=1.51e-06, N=789
  Estimated time remaining to complete simulation: 14 hours, 39 minutes, 36 seconds
  Estimated time remaining to next output: 5 minutes, 44 seconds
Output 586/738: t=8470000.0 yr, dE/E0=1.53e-06, N=789
  Estimated time remaining to complete simulation: 14 hours, 33 minutes, 39 seconds
  Estimated time remaining to next output: 5 minutes, 44 seconds
Output 587/738: t=8480000.0 yr, dE/E0=1.53e-06, N=789
  Estimated time remaining to complete simulation: 14 hours, 27 minutes, 44 seconds
  Estimated time remaining to next output: 5 minutes, 44 seconds
Output 588/738: t=8490000.0 yr, dE/E0=1.53e-06, N=789
  Estimated time remaining to complete simulation: 14 hours, 21 minutes, 52 seconds
  Estimated time remaining to next output: 5 minutes, 44 seconds
Output 589/738: t=8500000.0 yr, dE/E0=1.52e-06, N=789
  Estimated time remaining to complete simulation: 14 hours, 15 minutes, 59 seconds
  Estimated time remaining to next output: 5 minutes, 44 seconds
Output 590/738: t=8510000.0 yr, dE/E0=1.51e-06, N=789
  Estimated time remaining to complete simulation: 14 hours, 10 minutes, 3 seconds
  Estimated time remaining to next output: 5 minutes, 44 seconds
Output 591/738: t=8520000.0 yr, dE/E0=1.50e-06, N=789
  Estimated time remaining to complete simulation: 14 hours, 4 minutes, 6 seconds
  Estimated time remaining to next output: 5 minutes, 44 seconds
Output 592/738: t=8530000.0 yr, dE/E0=1.52e-06, N=789
  Estimated time remaining to complete simulation: 13 hours, 58 minutes, 8 seconds
  Estimated time remaining to next output: 5 minutes, 44 seconds
Output 593/738: t=8540000.0 yr, dE/E0=1.52e-06, N=789
  Estimated time remaining to complete simulation: 13 hours, 52 minutes, 12 seconds
  Estimated time remaining to next output: 5 minutes, 44 seconds
Output 594/738: t=8550000.0 yr, dE/E0=1.52e-06, N=789
  Estimated time remaining to complete simulation: 13 hours, 46 minutes, 17 seconds
  Estimated time remaining to next output: 5 minutes, 44 seconds
Output 595/738: t=8560000.0 yr, dE/E0=1.51e-06, N=789
  Estimated time remaining to complete simulation: 13 hours, 40 minutes, 23 seconds
  Estimated time remaining to next output: 5 minutes, 44 seconds
Output 596/738: t=8570000.0 yr, dE/E0=1.51e-06, N=789
  Estimated time remaining to complete simulation: 13 hours, 34 minutes, 30 seconds
  Estimated time remaining to next output: 5 minutes, 44 seconds
Output 597/738: t=8580000.0 yr, dE/E0=1.51e-06, N=789
  Estimated time remaining to complete simulation: 13 hours, 28 minutes, 36 seconds
  Estimated time remaining to next output: 5 minutes, 44 seconds
Output 598/738: t=8590000.0 yr, dE/E0=1.53e-06, N=789
  Estimated time remaining to complete simulation: 13 hours, 22 minutes, 41 seconds
  Estimated time remaining to next output: 5 minutes, 44 seconds
Output 599/738: t=8600000.0 yr, dE/E0=1.53e-06, N=789
  Estimated time remaining to complete simulation: 13 hours, 16 minutes, 47 seconds
  Estimated time remaining to next output: 5 minutes, 43 seconds
Output 600/738: t=8610000.0 yr, dE/E0=1.53e-06, N=789
  Estimated time remaining to complete simulation: 13 hours, 10 minutes, 52 seconds
  Estimated time remaining to next output: 5 minutes, 43 seconds
Output 601/738: t=8620000.0 yr, dE/E0=1.51e-06, N=789
  Estimated time remaining to complete simulation: 13 hours, 5 minutes
  Estimated time remaining to next output: 5 minutes, 43 seconds
Output 602/738: t=8630000.0 yr, dE/E0=1.51e-06, N=789
  Estimated time remaining to complete simulation: 12 hours, 59 minutes, 10 seconds
  Estimated time remaining to next output: 5 minutes, 43 seconds
Output 603/738: t=8640000.0 yr, dE/E0=1.52e-06, N=789
  Estimated time remaining to complete simulation: 12 hours, 53 minutes, 19 seconds
  Estimated time remaining to next output: 5 minutes, 43 seconds
Output 604/738: t=8650000.0 yr, dE/E0=1.53e-06, N=789
  Estimated time remaining to complete simulation: 12 hours, 47 minutes, 30 seconds
  Estimated time remaining to next output: 5 minutes, 43 seconds
Output 605/738: t=8660000.0 yr, dE/E0=1.54e-06, N=789
  Estimated time remaining to complete simulation: 12 hours, 41 minutes, 40 seconds
  Estimated time remaining to next output: 5 minutes, 43 seconds
A particle escaped (r>exit_max_distance).
Removing escaped particle at index 763
Remaining particles: 788
Output 606/738: t=8662355.0 yr, dE/E0=1.62e-06, N=788
  Estimated time remaining to complete simulation: 12 hours, 34 minutes, 57 seconds
  Estimated time remaining to next output: 5 minutes, 43 seconds
Output 607/738: t=8680000.0 yr, dE/E0=1.61e-06, N=788
  Estimated time remaining to complete simulation: 12 hours, 30 minutes, 2 seconds
  Estimated time remaining to next output: 5 minutes, 43 seconds
Output 608/738: t=8690000.0 yr, dE/E0=1.61e-06, N=788
  Estimated time remaining to complete simulation: 12 hours, 24 minutes, 9 seconds
  Estimated time remaining to next output: 5 minutes, 43 seconds
Output 609/738: t=8700000.0 yr, dE/E0=1.60e-06, N=788
  Estimated time remaining to complete simulation: 12 hours, 18 minutes, 19 seconds
  Estimated time remaining to next output: 5 minutes, 43 seconds
Output 610/738: t=8710000.0 yr, dE/E0=1.61e-06, N=788
  Estimated time remaining to complete simulation: 12 hours, 12 minutes, 28 seconds
  Estimated time remaining to next output: 5 minutes, 43 seconds
Output 611/738: t=8720000.0 yr, dE/E0=1.64e-06, N=788
  Estimated time remaining to complete simulation: 12 hours, 6 minutes, 40 seconds
  Estimated time remaining to next output: 5 minutes, 43 seconds
Output 612/738: t=8730000.0 yr, dE/E0=1.63e-06, N=788
  Estimated time remaining to complete simulation: 12 hours, 53 seconds
  Estimated time remaining to next output: 5 minutes, 43 seconds
Output 613/738: t=8740000.0 yr, dE/E0=1.60e-06, N=788
  Estimated time remaining to complete simulation: 11 hours, 55 minutes, 1 seconds
  Estimated time remaining to next output: 5 minutes, 43 seconds
Output 614/738: t=8750000.0 yr, dE/E0=1.61e-06, N=788
  Estimated time remaining to complete simulation: 11 hours, 49 minutes, 6 seconds
  Estimated time remaining to next output: 5 minutes, 43 seconds
Output 615/738: t=8760000.0 yr, dE/E0=1.61e-06, N=788
  Estimated time remaining to complete simulation: 11 hours, 43 minutes, 13 seconds
  Estimated time remaining to next output: 5 minutes, 43 seconds
Output 616/738: t=8770000.0 yr, dE/E0=1.63e-06, N=788
  Estimated time remaining to complete simulation: 11 hours, 37 minutes, 22 seconds
  Estimated time remaining to next output: 5 minutes, 42 seconds
Output 617/738: t=8780000.0 yr, dE/E0=1.64e-06, N=788
  Estimated time remaining to complete simulation: 11 hours, 31 minutes, 32 seconds
  Estimated time remaining to next output: 5 minutes, 42 seconds
Output 618/738: t=8790000.0 yr, dE/E0=1.63e-06, N=788
  Estimated time remaining to complete simulation: 11 hours, 25 minutes, 41 seconds
  Estimated time remaining to next output: 5 minutes, 42 seconds
Output 619/738: t=8800000.0 yr, dE/E0=1.62e-06, N=788
  Estimated time remaining to complete simulation: 11 hours, 19 minutes, 53 seconds
  Estimated time remaining to next output: 5 minutes, 42 seconds
Output 620/738: t=8810000.0 yr, dE/E0=1.61e-06, N=788
  Estimated time remaining to complete simulation: 11 hours, 14 minutes, 2 seconds
  Estimated time remaining to next output: 5 minutes, 42 seconds
Output 621/738: t=8820000.0 yr, dE/E0=1.61e-06, N=788
  Estimated time remaining to complete simulation: 11 hours, 8 minutes, 12 seconds
  Estimated time remaining to next output: 5 minutes, 42 seconds
Output 622/738: t=8830000.0 yr, dE/E0=1.62e-06, N=788
  Estimated time remaining to complete simulation: 11 hours, 2 minutes, 23 seconds
  Estimated time remaining to next output: 5 minutes, 42 seconds
Output 623/738: t=8840000.0 yr, dE/E0=1.63e-06, N=788
  Estimated time remaining to complete simulation: 10 hours, 56 minutes, 34 seconds
  Estimated time remaining to next output: 5 minutes, 42 seconds
Output 624/738: t=8850000.0 yr, dE/E0=1.63e-06, N=788
  Estimated time remaining to complete simulation: 10 hours, 50 minutes, 43 seconds
  Estimated time remaining to next output: 5 minutes, 42 seconds
Output 625/738: t=8860000.0 yr, dE/E0=1.63e-06, N=788
  Estimated time remaining to complete simulation: 10 hours, 44 minutes, 56 seconds
  Estimated time remaining to next output: 5 minutes, 42 seconds
Output 626/738: t=8870000.0 yr, dE/E0=1.62e-06, N=788
  Estimated time remaining to complete simulation: 10 hours, 39 minutes, 9 seconds
  Estimated time remaining to next output: 5 minutes, 42 seconds
Output 627/738: t=8880000.0 yr, dE/E0=1.61e-06, N=788
  Estimated time remaining to complete simulation: 10 hours, 33 minutes, 21 seconds
  Estimated time remaining to next output: 5 minutes, 42 seconds
Output 628/738: t=8890000.0 yr, dE/E0=1.62e-06, N=788
  Estimated time remaining to complete simulation: 10 hours, 27 minutes, 33 seconds
  Estimated time remaining to next output: 5 minutes, 42 seconds
Output 629/738: t=8900000.0 yr, dE/E0=1.62e-06, N=788
  Estimated time remaining to complete simulation: 10 hours, 21 minutes, 43 seconds
  Estimated time remaining to next output: 5 minutes, 42 seconds
Output 630/738: t=8910000.0 yr, dE/E0=1.62e-06, N=788
  Estimated time remaining to complete simulation: 10 hours, 15 minutes, 56 seconds
  Estimated time remaining to next output: 5 minutes, 42 seconds
Output 631/738: t=8920000.0 yr, dE/E0=1.62e-06, N=788
  Estimated time remaining to complete simulation: 10 hours, 10 minutes, 10 seconds
  Estimated time remaining to next output: 5 minutes, 42 seconds
Output 632/738: t=8930000.0 yr, dE/E0=1.61e-06, N=788
  Estimated time remaining to complete simulation: 10 hours, 4 minutes, 19 seconds
  Estimated time remaining to next output: 5 minutes, 42 seconds
Output 633/738: t=8940000.0 yr, dE/E0=1.60e-06, N=788
  Estimated time remaining to complete simulation: 9 hours, 58 minutes, 32 seconds
  Estimated time remaining to next output: 5 minutes, 42 seconds
Output 634/738: t=8950000.0 yr, dE/E0=1.61e-06, N=788
  Estimated time remaining to complete simulation: 9 hours, 52 minutes, 46 seconds
  Estimated time remaining to next output: 5 minutes, 41 seconds
Output 635/738: t=8960000.0 yr, dE/E0=1.61e-06, N=788
  Estimated time remaining to complete simulation: 9 hours, 46 minutes, 56 seconds
  Estimated time remaining to next output: 5 minutes, 41 seconds
Output 636/738: t=8970000.0 yr, dE/E0=1.61e-06, N=788
  Estimated time remaining to complete simulation: 9 hours, 41 minutes, 9 seconds
  Estimated time remaining to next output: 5 minutes, 41 seconds
Output 637/738: t=8980000.0 yr, dE/E0=1.61e-06, N=788
  Estimated time remaining to complete simulation: 9 hours, 35 minutes, 25 seconds
  Estimated time remaining to next output: 5 minutes, 41 seconds
Output 638/738: t=8990000.0 yr, dE/E0=1.60e-06, N=788
  Estimated time remaining to complete simulation: 9 hours, 29 minutes, 36 seconds
  Estimated time remaining to next output: 5 minutes, 41 seconds
Output 639/738: t=9000000.0 yr, dE/E0=1.60e-06, N=788
  Estimated time remaining to complete simulation: 9 hours, 23 minutes, 51 seconds
  Estimated time remaining to next output: 5 minutes, 41 seconds
Output 640/738: t=9010000.0 yr, dE/E0=1.59e-06, N=788
  Estimated time remaining to complete simulation: 9 hours, 18 minutes, 7 seconds
  Estimated time remaining to next output: 5 minutes, 41 seconds
Output 641/738: t=9020000.0 yr, dE/E0=1.61e-06, N=788
  Estimated time remaining to complete simulation: 9 hours, 12 minutes, 18 seconds
  Estimated time remaining to next output: 5 minutes, 41 seconds
Output 642/738: t=9030000.0 yr, dE/E0=1.61e-06, N=788
  Estimated time remaining to complete simulation: 9 hours, 6 minutes, 33 seconds
  Estimated time remaining to next output: 5 minutes, 41 seconds
Output 643/738: t=9040000.0 yr, dE/E0=1.61e-06, N=788
  Estimated time remaining to complete simulation: 9 hours, 50 seconds
  Estimated time remaining to next output: 5 minutes, 41 seconds
Output 644/738: t=9050000.0 yr, dE/E0=1.59e-06, N=788
  Estimated time remaining to complete simulation: 8 hours, 55 minutes, 1 seconds
  Estimated time remaining to next output: 5 minutes, 41 seconds
Output 645/738: t=9060000.0 yr, dE/E0=1.58e-06, N=788
  Estimated time remaining to complete simulation: 8 hours, 49 minutes, 15 seconds
  Estimated time remaining to next output: 5 minutes, 41 seconds
Output 646/738: t=9070000.0 yr, dE/E0=1.59e-06, N=788
  Estimated time remaining to complete simulation: 8 hours, 43 minutes, 30 seconds
  Estimated time remaining to next output: 5 minutes, 41 seconds
Output 647/738: t=9080000.0 yr, dE/E0=1.60e-06, N=788
  Estimated time remaining to complete simulation: 8 hours, 37 minutes, 40 seconds
  Estimated time remaining to next output: 5 minutes, 41 seconds
Output 648/738: t=9090000.0 yr, dE/E0=1.59e-06, N=788
  Estimated time remaining to complete simulation: 8 hours, 31 minutes, 56 seconds
  Estimated time remaining to next output: 5 minutes, 41 seconds
Output 649/738: t=9100000.0 yr, dE/E0=1.58e-06, N=788
  Estimated time remaining to complete simulation: 8 hours, 26 minutes, 11 seconds
  Estimated time remaining to next output: 5 minutes, 41 seconds
Output 650/738: t=9110000.0 yr, dE/E0=1.57e-06, N=788
  Estimated time remaining to complete simulation: 8 hours, 20 minutes, 21 seconds
  Estimated time remaining to next output: 5 minutes, 41 seconds
Output 651/738: t=9120000.0 yr, dE/E0=1.57e-06, N=788
  Estimated time remaining to complete simulation: 8 hours, 14 minutes, 35 seconds
  Estimated time remaining to next output: 5 minutes, 41 seconds
Output 652/738: t=9130000.0 yr, dE/E0=1.58e-06, N=788
  Estimated time remaining to complete simulation: 8 hours, 8 minutes, 50 seconds
  Estimated time remaining to next output: 5 minutes, 41 seconds
Output 653/738: t=9140000.0 yr, dE/E0=1.59e-06, N=788
  Estimated time remaining to complete simulation: 8 hours, 3 minutes, 4 seconds
  Estimated time remaining to next output: 5 minutes, 40 seconds
Output 654/738: t=9150000.0 yr, dE/E0=1.60e-06, N=788
  Estimated time remaining to complete simulation: 7 hours, 57 minutes, 19 seconds
  Estimated time remaining to next output: 5 minutes, 40 seconds
A particle escaped (r>exit_max_distance).
Removing escaped particle at index 737
Remaining particles: 787
Output 655/738: t=9157009.0 yr, dE/E0=1.66e-06, N=787
  Estimated time remaining to complete simulation: 7 hours, 51 minutes, 22 seconds
  Estimated time remaining to next output: 5 minutes, 40 seconds
Output 656/738: t=9170000.0 yr, dE/E0=1.66e-06, N=787
  Estimated time remaining to complete simulation: 7 hours, 45 minutes, 47 seconds
  Estimated time remaining to next output: 5 minutes, 40 seconds
Output 657/738: t=9180000.0 yr, dE/E0=1.64e-06, N=787
  Estimated time remaining to complete simulation: 7 hours, 40 minutes, 5 seconds
  Estimated time remaining to next output: 5 minutes, 40 seconds
Output 658/738: t=9190000.0 yr, dE/E0=1.66e-06, N=787
  Estimated time remaining to complete simulation: 7 hours, 34 minutes, 20 seconds
  Estimated time remaining to next output: 5 minutes, 40 seconds
Output 659/738: t=9200000.0 yr, dE/E0=1.67e-06, N=787
  Estimated time remaining to complete simulation: 7 hours, 28 minutes, 34 seconds
  Estimated time remaining to next output: 5 minutes, 40 seconds
Output 660/738: t=9210000.0 yr, dE/E0=1.68e-06, N=787
  Estimated time remaining to complete simulation: 7 hours, 22 minutes, 49 seconds
  Estimated time remaining to next output: 5 minutes, 40 seconds
Output 661/738: t=9220000.0 yr, dE/E0=1.67e-06, N=787
  Estimated time remaining to complete simulation: 7 hours, 17 minutes, 4 seconds
  Estimated time remaining to next output: 5 minutes, 40 seconds
Output 662/738: t=9230000.0 yr, dE/E0=1.66e-06, N=787
  Estimated time remaining to complete simulation: 7 hours, 11 minutes, 20 seconds
  Estimated time remaining to next output: 5 minutes, 40 seconds
Output 663/738: t=9240000.0 yr, dE/E0=1.66e-06, N=787
  Estimated time remaining to complete simulation: 7 hours, 5 minutes, 38 seconds
  Estimated time remaining to next output: 5 minutes, 40 seconds
Output 664/738: t=9250000.0 yr, dE/E0=1.67e-06, N=787
  Estimated time remaining to complete simulation: 6 hours, 59 minutes, 52 seconds
  Estimated time remaining to next output: 5 minutes, 40 seconds
Output 665/738: t=9260000.0 yr, dE/E0=1.67e-06, N=787
  Estimated time remaining to complete simulation: 6 hours, 54 minutes, 8 seconds
  Estimated time remaining to next output: 5 minutes, 40 seconds
Output 666/738: t=9270000.0 yr, dE/E0=1.67e-06, N=787
  Estimated time remaining to complete simulation: 6 hours, 48 minutes, 22 seconds
  Estimated time remaining to next output: 5 minutes, 40 seconds
Output 667/738: t=9280000.0 yr, dE/E0=1.67e-06, N=787
  Estimated time remaining to complete simulation: 6 hours, 42 minutes, 39 seconds
  Estimated time remaining to next output: 5 minutes, 40 seconds
Output 668/738: t=9290000.0 yr, dE/E0=1.66e-06, N=787
  Estimated time remaining to complete simulation: 6 hours, 36 minutes, 56 seconds
  Estimated time remaining to next output: 5 minutes, 40 seconds
Output 669/738: t=9300000.0 yr, dE/E0=1.65e-06, N=787
  Estimated time remaining to complete simulation: 6 hours, 31 minutes, 11 seconds
  Estimated time remaining to next output: 5 minutes, 40 seconds
Output 670/738: t=9310000.0 yr, dE/E0=1.65e-06, N=787
  Estimated time remaining to complete simulation: 6 hours, 25 minutes, 28 seconds
  Estimated time remaining to next output: 5 minutes, 40 seconds
Output 671/738: t=9320000.0 yr, dE/E0=1.66e-06, N=787
  Estimated time remaining to complete simulation: 6 hours, 19 minutes, 47 seconds
  Estimated time remaining to next output: 5 minutes, 40 seconds
Output 672/738: t=9330000.0 yr, dE/E0=1.67e-06, N=787
  Estimated time remaining to complete simulation: 6 hours, 14 minutes, 25 seconds
  Estimated time remaining to next output: 5 minutes, 40 seconds
Output 673/738: t=9340000.0 yr, dE/E0=1.66e-06, N=787
  Estimated time remaining to complete simulation: 6 hours, 9 minutes
  Estimated time remaining to next output: 5 minutes, 40 seconds
Output 674/738: t=9350000.0 yr, dE/E0=1.64e-06, N=787
  Estimated time remaining to complete simulation: 6 hours, 3 minutes, 33 seconds
  Estimated time remaining to next output: 5 minutes, 40 seconds
Output 675/738: t=9360000.0 yr, dE/E0=1.64e-06, N=787
  Estimated time remaining to complete simulation: 5 hours, 58 minutes, 9 seconds
  Estimated time remaining to next output: 5 minutes, 41 seconds
Output 676/738: t=9370000.0 yr, dE/E0=1.66e-06, N=787
  Estimated time remaining to complete simulation: 5 hours, 52 minutes, 41 seconds
  Estimated time remaining to next output: 5 minutes, 41 seconds
Output 677/738: t=9380000.0 yr, dE/E0=1.67e-06, N=787
  Estimated time remaining to complete simulation: 5 hours, 47 minutes, 13 seconds
  Estimated time remaining to next output: 5 minutes, 41 seconds
Output 678/738: t=9390000.0 yr, dE/E0=1.65e-06, N=787
  Estimated time remaining to complete simulation: 5 hours, 41 minutes, 45 seconds
  Estimated time remaining to next output: 5 minutes, 41 seconds
Output 679/738: t=9400000.0 yr, dE/E0=1.66e-06, N=787
  Estimated time remaining to complete simulation: 5 hours, 36 minutes, 16 seconds
  Estimated time remaining to next output: 5 minutes, 41 seconds
Output 680/738: t=9410000.0 yr, dE/E0=1.65e-06, N=787
  Estimated time remaining to complete simulation: 5 hours, 30 minutes, 48 seconds
  Estimated time remaining to next output: 5 minutes, 42 seconds
A particle escaped (r>exit_max_distance).
Removing escaped particle at index 645
Remaining particles: 786
Output 681/738: t=9416616.5 yr, dE/E0=1.75e-06, N=786
  Estimated time remaining to complete simulation: 5 hours, 25 minutes, 5 seconds
  Estimated time remaining to next output: 5 minutes, 42 seconds
Output 682/738: t=9430000.0 yr, dE/E0=1.74e-06, N=786
  Estimated time remaining to complete simulation: 5 hours, 19 minutes, 50 seconds
  Estimated time remaining to next output: 5 minutes, 42 seconds
Output 683/738: t=9440000.0 yr, dE/E0=1.74e-06, N=786
  Estimated time remaining to complete simulation: 5 hours, 14 minutes, 21 seconds
  Estimated time remaining to next output: 5 minutes, 42 seconds
Output 684/738: t=9450000.0 yr, dE/E0=1.76e-06, N=786
  Estimated time remaining to complete simulation: 5 hours, 8 minutes, 50 seconds
  Estimated time remaining to next output: 5 minutes, 43 seconds
Output 685/738: t=9460000.0 yr, dE/E0=1.76e-06, N=786
  Estimated time remaining to complete simulation: 5 hours, 3 minutes, 19 seconds
  Estimated time remaining to next output: 5 minutes, 43 seconds
Output 686/738: t=9470000.0 yr, dE/E0=1.73e-06, N=786
  Estimated time remaining to complete simulation: 4 hours, 57 minutes, 48 seconds
  Estimated time remaining to next output: 5 minutes, 43 seconds
Output 687/738: t=9480000.0 yr, dE/E0=1.73e-06, N=786
  Estimated time remaining to complete simulation: 4 hours, 52 minutes, 16 seconds
  Estimated time remaining to next output: 5 minutes, 43 seconds
Output 688/738: t=9490000.0 yr, dE/E0=1.74e-06, N=786
  Estimated time remaining to complete simulation: 4 hours, 46 minutes, 44 seconds
  Estimated time remaining to next output: 5 minutes, 44 seconds
Output 689/738: t=9500000.0 yr, dE/E0=1.75e-06, N=786
  Estimated time remaining to complete simulation: 4 hours, 41 minutes, 10 seconds
  Estimated time remaining to next output: 5 minutes, 44 seconds
Output 690/738: t=9510000.0 yr, dE/E0=1.75e-06, N=786
  Estimated time remaining to complete simulation: 4 hours, 35 minutes, 37 seconds
  Estimated time remaining to next output: 5 minutes, 44 seconds
Output 691/738: t=9520000.0 yr, dE/E0=1.74e-06, N=786
  Estimated time remaining to complete simulation: 4 hours, 30 minutes, 4 seconds
  Estimated time remaining to next output: 5 minutes, 44 seconds
Output 692/738: t=9530000.0 yr, dE/E0=1.73e-06, N=786
  Estimated time remaining to complete simulation: 4 hours, 24 minutes, 31 seconds
  Estimated time remaining to next output: 5 minutes, 45 seconds
Output 693/738: t=9540000.0 yr, dE/E0=1.73e-06, N=786
  Estimated time remaining to complete simulation: 4 hours, 18 minutes, 54 seconds
  Estimated time remaining to next output: 5 minutes, 45 seconds
Output 694/738: t=9550000.0 yr, dE/E0=1.73e-06, N=786
  Estimated time remaining to complete simulation: 4 hours, 13 minutes, 17 seconds
  Estimated time remaining to next output: 5 minutes, 45 seconds
Output 695/738: t=9560000.0 yr, dE/E0=1.74e-06, N=786
  Estimated time remaining to complete simulation: 4 hours, 7 minutes, 41 seconds
  Estimated time remaining to next output: 5 minutes, 45 seconds
Output 696/738: t=9570000.0 yr, dE/E0=1.75e-06, N=786
  Estimated time remaining to complete simulation: 4 hours, 2 minutes, 5 seconds
  Estimated time remaining to next output: 5 minutes, 45 seconds
Output 697/738: t=9580000.0 yr, dE/E0=1.76e-06, N=786
  Estimated time remaining to complete simulation: 3 hours, 56 minutes, 28 seconds
  Estimated time remaining to next output: 5 minutes, 46 seconds
Output 698/738: t=9590000.0 yr, dE/E0=1.74e-06, N=786
  Estimated time remaining to complete simulation: 3 hours, 50 minutes, 51 seconds
  Estimated time remaining to next output: 5 minutes, 46 seconds
Output 699/738: t=9600000.0 yr, dE/E0=1.75e-06, N=786
  Estimated time remaining to complete simulation: 3 hours, 45 minutes, 13 seconds
  Estimated time remaining to next output: 5 minutes, 46 seconds
Output 700/738: t=9610000.0 yr, dE/E0=1.76e-06, N=786
  Estimated time remaining to complete simulation: 3 hours, 39 minutes, 36 seconds
  Estimated time remaining to next output: 5 minutes, 46 seconds
Output 701/738: t=9620000.0 yr, dE/E0=1.78e-06, N=786
  Estimated time remaining to complete simulation: 3 hours, 33 minutes, 56 seconds
  Estimated time remaining to next output: 5 minutes, 46 seconds
Output 702/738: t=9630000.0 yr, dE/E0=1.77e-06, N=786
  Estimated time remaining to complete simulation: 3 hours, 28 minutes, 17 seconds
  Estimated time remaining to next output: 5 minutes, 47 seconds
Output 703/738: t=9640000.0 yr, dE/E0=1.76e-06, N=786
  Estimated time remaining to complete simulation: 3 hours, 22 minutes, 36 seconds
  Estimated time remaining to next output: 5 minutes, 47 seconds
Output 704/738: t=9650000.0 yr, dE/E0=1.75e-06, N=786
  Estimated time remaining to complete simulation: 3 hours, 16 minutes, 56 seconds
  Estimated time remaining to next output: 5 minutes, 47 seconds
Output 705/738: t=9660000.0 yr, dE/E0=1.75e-06, N=786
  Estimated time remaining to complete simulation: 3 hours, 11 minutes, 16 seconds
  Estimated time remaining to next output: 5 minutes, 47 seconds
Output 706/738: t=9670000.0 yr, dE/E0=1.75e-06, N=786
  Estimated time remaining to complete simulation: 3 hours, 5 minutes, 35 seconds
  Estimated time remaining to next output: 5 minutes, 47 seconds
Output 707/738: t=9680000.0 yr, dE/E0=1.76e-06, N=786
  Estimated time remaining to complete simulation: 2 hours, 59 minutes, 53 seconds
  Estimated time remaining to next output: 5 minutes, 48 seconds
Output 708/738: t=9690000.0 yr, dE/E0=1.74e-06, N=786
  Estimated time remaining to complete simulation: 2 hours, 54 minutes, 10 seconds
  Estimated time remaining to next output: 5 minutes, 48 seconds
Output 709/738: t=9700000.0 yr, dE/E0=1.74e-06, N=786
  Estimated time remaining to complete simulation: 2 hours, 48 minutes, 28 seconds
  Estimated time remaining to next output: 5 minutes, 48 seconds
Output 710/738: t=9710000.0 yr, dE/E0=1.74e-06, N=786
  Estimated time remaining to complete simulation: 2 hours, 42 minutes, 44 seconds
  Estimated time remaining to next output: 5 minutes, 48 seconds
Output 711/738: t=9720000.0 yr, dE/E0=1.75e-06, N=786
  Estimated time remaining to complete simulation: 2 hours, 37 minutes, 1 seconds
  Estimated time remaining to next output: 5 minutes, 48 seconds
Output 712/738: t=9730000.0 yr, dE/E0=1.75e-06, N=786
  Estimated time remaining to complete simulation: 2 hours, 31 minutes, 16 seconds
  Estimated time remaining to next output: 5 minutes, 49 seconds
Output 713/738: t=9740000.0 yr, dE/E0=1.77e-06, N=786
  Estimated time remaining to complete simulation: 2 hours, 25 minutes, 33 seconds
  Estimated time remaining to next output: 5 minutes, 49 seconds
Output 714/738: t=9750000.0 yr, dE/E0=1.78e-06, N=786
  Estimated time remaining to complete simulation: 2 hours, 19 minutes, 49 seconds
  Estimated time remaining to next output: 5 minutes, 49 seconds
Output 715/738: t=9760000.0 yr, dE/E0=1.78e-06, N=786
  Estimated time remaining to complete simulation: 2 hours, 14 minutes, 5 seconds
  Estimated time remaining to next output: 5 minutes, 49 seconds
Output 716/738: t=9770000.0 yr, dE/E0=1.77e-06, N=786
  Estimated time remaining to complete simulation: 2 hours, 8 minutes, 20 seconds
  Estimated time remaining to next output: 5 minutes, 50 seconds
Output 717/738: t=9780000.0 yr, dE/E0=1.76e-06, N=786
  Estimated time remaining to complete simulation: 2 hours, 2 minutes, 34 seconds
  Estimated time remaining to next output: 5 minutes, 50 seconds
Output 718/738: t=9790000.0 yr, dE/E0=1.77e-06, N=786
  Estimated time remaining to complete simulation: 1 hours, 56 minutes, 49 seconds
  Estimated time remaining to next output: 5 minutes, 50 seconds
Output 719/738: t=9800000.0 yr, dE/E0=1.76e-06, N=786
  Estimated time remaining to complete simulation: 1 hours, 51 minutes, 2 seconds
  Estimated time remaining to next output: 5 minutes, 50 seconds
Output 720/738: t=9810000.0 yr, dE/E0=1.79e-06, N=786
  Estimated time remaining to complete simulation: 1 hours, 45 minutes, 16 seconds
  Estimated time remaining to next output: 5 minutes, 50 seconds
Output 721/738: t=9820000.0 yr, dE/E0=1.77e-06, N=786
  Estimated time remaining to complete simulation: 1 hours, 39 minutes, 29 seconds
  Estimated time remaining to next output: 5 minutes, 51 seconds
Output 722/738: t=9830000.0 yr, dE/E0=1.77e-06, N=786
  Estimated time remaining to complete simulation: 1 hours, 33 minutes, 41 seconds
  Estimated time remaining to next output: 5 minutes, 51 seconds
Output 723/738: t=9840000.0 yr, dE/E0=1.76e-06, N=786
  Estimated time remaining to complete simulation: 1 hours, 27 minutes, 52 seconds
  Estimated time remaining to next output: 5 minutes, 51 seconds
Output 724/738: t=9850000.0 yr, dE/E0=1.76e-06, N=786
  Estimated time remaining to complete simulation: 1 hours, 22 minutes, 3 seconds
  Estimated time remaining to next output: 5 minutes, 51 seconds
Output 725/738: t=9860000.0 yr, dE/E0=1.76e-06, N=786
  Estimated time remaining to complete simulation: 1 hours, 16 minutes, 14 seconds
  Estimated time remaining to next output: 5 minutes, 51 seconds
Output 726/738: t=9870000.0 yr, dE/E0=1.77e-06, N=786
  Estimated time remaining to complete simulation: 1 hours, 10 minutes, 24 seconds
  Estimated time remaining to next output: 5 minutes, 52 seconds
Output 727/738: t=9880000.0 yr, dE/E0=1.77e-06, N=786
  Estimated time remaining to complete simulation: 1 hours, 4 minutes, 34 seconds
  Estimated time remaining to next output: 5 minutes, 52 seconds
Output 728/738: t=9890000.0 yr, dE/E0=1.76e-06, N=786
  Estimated time remaining to complete simulation: 58 minutes, 44 seconds
  Estimated time remaining to next output: 5 minutes, 52 seconds
Output 729/738: t=9900000.0 yr, dE/E0=1.76e-06, N=786
  Estimated time remaining to complete simulation: 52 minutes, 54 seconds
  Estimated time remaining to next output: 5 minutes, 52 seconds
Output 730/738: t=9910000.0 yr, dE/E0=1.75e-06, N=786
  Estimated time remaining to complete simulation: 47 minutes, 2 seconds
  Estimated time remaining to next output: 5 minutes, 52 seconds
Output 731/738: t=9920000.0 yr, dE/E0=1.77e-06, N=786
  Estimated time remaining to complete simulation: 41 minutes, 11 seconds
  Estimated time remaining to next output: 5 minutes, 53 seconds
Output 732/738: t=9930000.0 yr, dE/E0=1.77e-06, N=786
  Estimated time remaining to complete simulation: 35 minutes, 19 seconds
  Estimated time remaining to next output: 5 minutes, 53 seconds
Output 733/738: t=9940000.0 yr, dE/E0=1.77e-06, N=786
  Estimated time remaining to complete simulation: 29 minutes, 27 seconds
  Estimated time remaining to next output: 5 minutes, 53 seconds
A particle escaped (r>exit_max_distance).
Removing escaped particle at index 524
Remaining particles: 785
Output 734/738: t=9942018.6 yr, dE/E0=1.89e-06, N=785
  Estimated time remaining to complete simulation: 23 minutes, 32 seconds
  Estimated time remaining to next output: 5 minutes, 53 seconds
Output 735/738: t=9960000.0 yr, dE/E0=1.88e-06, N=785
  Estimated time remaining to complete simulation: 17 minutes, 41 seconds
  Estimated time remaining to next output: 5 minutes, 53 seconds
Output 736/738: t=9970000.0 yr, dE/E0=1.89e-06, N=785
  Estimated time remaining to complete simulation: 11 minutes, 47 seconds
  Estimated time remaining to next output: 5 minutes, 53 seconds
Output 737/738: t=9980000.0 yr, dE/E0=1.90e-06, N=785
  Estimated time remaining to complete simulation: 5 minutes, 53 seconds
  Estimated time remaining to next output: 5 minutes, 53 seconds
Output 738/738: t=9990000.0 yr, dE/E0=1.91e-06, N=785
  Estimated time remaining to complete simulation: 0 seconds
Output 739/738: t=10000000.0 yr, dE/E0=1.90e-06, N=785
  Estimated time remaining to complete simulation: -1 months, 4 weeks, 1 days, 23 hours, 54 minutes, 7 seconds

Simulation complete.
Total runtime: 3 days, 32 minutes, 28 seconds

Krivov & Booth (2018) self-stirring check (Eqs. 9-10):
  NOTE: a giant planet is present; the two-population self-stirring model assumes no external perturber, so C_e below is only indicative.
  Final time:                 t = 1.000000e+07 yr
  Rayleigh outlier cut:       e > 5 sigma = 1.4029e-01 (sigma = median(e)/sqrt(2 ln 2) = 2.8058e-02)
  Stirred-disk check:         median(e) = 3.3036e-02 vs 30 x disk.emax = 9.6000e-04 -> stirred, cut applied
  Excluded MPs:               16 -- MP_197 (e = 0.7951), MP_602 (e = 0.6996), MP_129 (e = 0.5535), MP_337 (e = 0.5070), MP_65 (e = 0.4429), MP_709 (e = 0.3241), MP_135 (e = 0.3103), MP_389 (e = 0.2829), MP_99 (e = 0.1729), MP_295 (e = 0.1479), MP_792 (e = 0.1474), MP_234 (e = 0.1459), MP_667 (e = 0.1453), MP_226 (e = 0.1436), MP_695 (e = 0.1423), MP_587 (e = 0.1409)
  KS test of kept e vs Rayleigh: D = 0.1103, p = 1.39e-08  (WARNING: p < 0.05, kept e deviates from a Rayleigh distribution)
  RMS eccentricity (767 of 783 MPs): 4.525636e-02  (all MPs: 7.066542e-02)
  Belt geometry:              a = 100, da = 10, a/da = 10
  Masses:                     M_max = 2.152034e-08 Msun, M_disc = 2.977588e-06 Msun
  Implied stirring timescale: T = 4.767730e+12 yr
  Effective stirring factor:  C_e = 327.3277  (all MPs, no cut: 1945.7734)
  WARNING: C_e = 327.3277 >= 40 (Ida & Makino 1993 canonical value) -- this run stirs at or above the analytic self-stirring rate.
Saved archive: outputs/SS_800MP_10Myr_PSD2B_500Mearth_lorentzian/SS_800MP_10Myr_PSD2B_500Mearth_lorentzian.bin
Number of snapshots saved: 1002
Archive time range: 0.000e+00 yr to 1.000e+07 yr
Particle-name check: OK (1002 snapshots)
Loaded snapshot table from archive.
role
massive_planetesimal    800
star                      1
giant_planet              1
Name: count, dtype: int64
Saved: outputs/SS_800MP_10Myr_PSD2B_500Mearth_lorentzian/figures/survival_fraction_vs_time.png
Saved: outputs/SS_800MP_10Myr_PSD2B_500Mearth_lorentzian/figures/mean_semimajor_axis_vs_time.png
Saved: outputs/SS_800MP_10Myr_PSD2B_500Mearth_lorentzian/figures/mean_eccentricity_vs_time.png
Saved: outputs/SS_800MP_10Myr_PSD2B_500Mearth_lorentzian/figures/rms_eccentricity_vs_time.png
Saved: outputs/SS_800MP_10Myr_PSD2B_500Mearth_lorentzian/figures/rms_inclination_vs_time.png
Saved: outputs/SS_800MP_10Myr_PSD2B_500Mearth_lorentzian/figures/data/orbits_initial_final.csv
Saved: outputs/SS_800MP_10Myr_PSD2B_500Mearth_lorentzian/figures/a_vs_e_initial_final.png
Saved: outputs/SS_800MP_10Myr_PSD2B_500Mearth_lorentzian/figures/a_vs_i_initial_final.png
Inner plotted edge = 95.04 AU
Outer plotted edge = 104.92 AU
Saved: outputs/SS_800MP_10Myr_PSD2B_500Mearth_lorentzian/figures/xy_initial_final.png
All summary figures saved.
```
