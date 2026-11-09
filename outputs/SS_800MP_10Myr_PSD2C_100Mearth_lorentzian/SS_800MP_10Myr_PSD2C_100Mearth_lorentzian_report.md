# SS_800MP_10Myr_PSD2C_100Mearth_lorentzian — Simulation Report

Config file: `config/SS_800MP_10Myr_PSD2C_100Mearth_lorentzian.yaml`
Archive file: `outputs/SS_800MP_10Myr_PSD2C_100Mearth_lorentzian/SS_800MP_10Myr_PSD2C_100Mearth_lorentzian.bin`

## Provenance

- Run UUID: `de5ae135-05f3-4d83-b93b-81db8ab65734`
- Created: 2026-10-14T17:56:31-03:00
- Finished: 2026-10-22T19:31:01-03:00
- Wall runtime: 277575.0 s
- Outcome: completed
- Command: `src/simulation/run_simulation.py config/SS_800MP_10Myr_PSD2C_100Mearth_lorentzian.yaml`
- Git commit: `15327ac8beddbbea523b7b344d8dfb1a77d1f97c` (branch `main`) **(DIRTY — uncommitted tracked changes)**
    - modified: `notebooks/mass_model_playground.ipynb`
- Software: python 3.12.14, rebound 5.0.0, numpy 2.4.6, pandas 3.0.3, matplotlib 3.10.9, pyyaml 6.0.3
- Resumed 1 time(s) after the first run
- Frozen config: `config.yaml` (this directory)
- Full environment: `environment.txt` (this directory)

## Simulation
- Name: SS_800MP_10Myr_PSD2C_100Mearth_lorentzian
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
- Mass-assignment method (config): loaded from CSV (mode=csv): variable=radius, path=src/mass_models/Plantesimal_Size_Dist_2_1Mearth/model_C/selected.csv, slope=4.2 (radii/masses read verbatim from file; disk mass computed from file, not split by a power law)
- **Mass is NOT uniform** across the 800 massive planetesimals:
  - min / median / max: 9.658151e-10 / 1.715214e-09 / 4.504445e-08 Msun
  - min / median / max: 3.215643e-04 / 5.710737e-04 / 1.499737e-02 Earth masses
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
Saving SimulationArchive to: outputs/SS_800MP_10Myr_PSD2C_100Mearth_lorentzian/SS_800MP_10Myr_PSD2C_100Mearth_lorentzian.bin
Resuming from t=2.860000e+06 yr: times=array([ 2860000.,  2870000.,  2880000.,  2890000.,  2900000.,  2910000.,
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
  Timestep: 6.772343e+01 (0.1 x giant planet orbital period = 6.772343e+02)
Restored simulation from snapshot number at t=2.860000e+06 yr with N=802 particles.

Stirrer-coverage check (Krivov & Booth 2018: N x delta_af >= delta_a):
  Stirrers inside the belt [95, 105]: N = 770
  delta_af = 8 sqrt(3) h_M a_M:  mean = 1.339978e+00, sum over stirrers = 1.031783e+03
  Belt width delta_a = 1.000000e+01
  Coverage ratio (sum delta_af / delta_a) = 103.178
  OK: stirrer feeding zones span the belt.

Beginning the main integration
Output 1/714: t=2860000.0 yr, dE/E0=0.00e+00, N=802
  Estimated time remaining to complete simulation: 40 seconds
  Estimated time remaining to next output: 0 seconds
Output 2/714: t=2870000.0 yr, dE/E0=3.92e-09, N=802
  Estimated time remaining to complete simulation: 1 days, 11 hours, 12 minutes, 37 seconds
  Estimated time remaining to next output: 2 minutes, 58 seconds
Output 3/714: t=2880000.0 yr, dE/E0=1.67e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 22 minutes, 28 seconds
  Estimated time remaining to next output: 4 minutes, 4 seconds
Output 4/714: t=2890000.0 yr, dE/E0=8.24e-09, N=802
  Estimated time remaining to complete simulation: 2 days, 6 hours, 6 minutes, 48 seconds
  Estimated time remaining to next output: 4 minutes, 34 seconds
Output 5/714: t=2900000.0 yr, dE/E0=2.17e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 10 hours, 14 minutes, 51 seconds
  Estimated time remaining to next output: 4 minutes, 55 seconds
Output 6/714: t=2910000.0 yr, dE/E0=2.04e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 12 hours, 27 minutes, 48 seconds
  Estimated time remaining to next output: 5 minutes, 7 seconds
Output 7/714: t=2920000.0 yr, dE/E0=2.62e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 13 hours, 55 minutes, 8 seconds
  Estimated time remaining to next output: 5 minutes, 15 seconds
Output 8/714: t=2930000.0 yr, dE/E0=1.57e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 15 hours, 3 minutes, 33 seconds
  Estimated time remaining to next output: 5 minutes, 21 seconds
Output 9/714: t=2940000.0 yr, dE/E0=3.08e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 16 hours, 15 minutes, 39 seconds
  Estimated time remaining to next output: 5 minutes, 28 seconds
Output 10/714: t=2950000.0 yr, dE/E0=2.81e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 17 hours, 13 minutes, 29 seconds
  Estimated time remaining to next output: 5 minutes, 33 seconds
Output 11/714: t=2960000.0 yr, dE/E0=6.67e-09, N=802
  Estimated time remaining to complete simulation: 2 days, 17 hours, 57 minutes, 52 seconds
  Estimated time remaining to next output: 5 minutes, 37 seconds
Output 12/714: t=2970000.0 yr, dE/E0=1.65e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 18 hours, 27 minutes, 2 seconds
  Estimated time remaining to next output: 5 minutes, 40 seconds
Output 13/714: t=2980000.0 yr, dE/E0=2.77e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 18 hours, 42 minutes, 47 seconds
  Estimated time remaining to next output: 5 minutes, 42 seconds
Output 14/714: t=2990000.0 yr, dE/E0=4.30e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 19 hours, 8 minutes, 1 seconds
  Estimated time remaining to next output: 5 minutes, 45 seconds
Output 15/714: t=3000000.0 yr, dE/E0=3.26e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 19 hours, 23 minutes, 39 seconds
  Estimated time remaining to next output: 5 minutes, 47 seconds
Output 16/714: t=3010000.0 yr, dE/E0=3.63e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 19 hours, 50 minutes, 25 seconds
  Estimated time remaining to next output: 5 minutes, 49 seconds
Output 17/714: t=3020000.0 yr, dE/E0=6.81e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 19 hours, 58 minutes, 8 seconds
  Estimated time remaining to next output: 5 minutes, 51 seconds
Output 18/714: t=3030000.0 yr, dE/E0=5.11e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 20 hours, 9 minutes, 47 seconds
  Estimated time remaining to next output: 5 minutes, 52 seconds
Output 19/714: t=3040000.0 yr, dE/E0=5.09e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 20 hours, 34 minutes, 16 seconds
  Estimated time remaining to next output: 5 minutes, 55 seconds
Output 20/714: t=3050000.0 yr, dE/E0=5.44e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 20 hours, 54 minutes, 10 seconds
  Estimated time remaining to next output: 5 minutes, 57 seconds
Output 21/714: t=3060000.0 yr, dE/E0=4.03e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 20 hours, 58 minutes, 19 seconds
  Estimated time remaining to next output: 5 minutes, 58 seconds
Output 22/714: t=3070000.0 yr, dE/E0=6.42e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 21 hours, 22 minutes, 38 seconds
  Estimated time remaining to next output: 6 minutes
Output 23/714: t=3080000.0 yr, dE/E0=5.39e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 21 hours, 44 minutes, 57 seconds
  Estimated time remaining to next output: 6 minutes, 3 seconds
Output 24/714: t=3090000.0 yr, dE/E0=2.96e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 21 hours, 43 minutes, 8 seconds
  Estimated time remaining to next output: 6 minutes, 3 seconds
Output 25/714: t=3100000.0 yr, dE/E0=6.25e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 21 hours, 49 minutes, 53 seconds
  Estimated time remaining to next output: 6 minutes, 4 seconds
Output 26/714: t=3110000.0 yr, dE/E0=6.55e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 21 hours, 46 minutes, 29 seconds
  Estimated time remaining to next output: 6 minutes, 5 seconds
Output 27/714: t=3120000.0 yr, dE/E0=6.52e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 21 hours, 53 minutes, 57 seconds
  Estimated time remaining to next output: 6 minutes, 6 seconds
Output 28/714: t=3130000.0 yr, dE/E0=7.39e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 21 hours, 55 minutes, 49 seconds
  Estimated time remaining to next output: 6 minutes, 6 seconds
Output 29/714: t=3140000.0 yr, dE/E0=6.57e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 21 hours, 59 minutes, 25 seconds
  Estimated time remaining to next output: 6 minutes, 7 seconds
Output 30/714: t=3150000.0 yr, dE/E0=6.46e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 21 hours, 57 minutes, 21 seconds
  Estimated time remaining to next output: 6 minutes, 8 seconds
Output 31/714: t=3160000.0 yr, dE/E0=5.30e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 21 hours, 55 minutes, 10 seconds
  Estimated time remaining to next output: 6 minutes, 8 seconds
Output 32/714: t=3170000.0 yr, dE/E0=4.04e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 21 hours, 56 minutes, 24 seconds
  Estimated time remaining to next output: 6 minutes, 9 seconds
Output 33/714: t=3180000.0 yr, dE/E0=4.09e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 21 hours, 53 minutes, 24 seconds
  Estimated time remaining to next output: 6 minutes, 9 seconds
Output 34/714: t=3190000.0 yr, dE/E0=7.22e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 21 hours, 54 minutes, 21 seconds
  Estimated time remaining to next output: 6 minutes, 10 seconds
Output 35/714: t=3200000.0 yr, dE/E0=8.37e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 21 hours, 50 minutes
  Estimated time remaining to next output: 6 minutes, 10 seconds
Output 36/714: t=3210000.0 yr, dE/E0=9.85e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 21 hours, 46 minutes, 21 seconds
  Estimated time remaining to next output: 6 minutes, 10 seconds
Output 37/714: t=3220000.0 yr, dE/E0=9.70e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 21 hours, 44 minutes, 13 seconds
  Estimated time remaining to next output: 6 minutes, 10 seconds
Output 38/714: t=3230000.0 yr, dE/E0=9.95e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 21 hours, 43 minutes, 15 seconds
  Estimated time remaining to next output: 6 minutes, 11 seconds
Output 39/714: t=3240000.0 yr, dE/E0=1.10e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 21 hours, 40 minutes, 26 seconds
  Estimated time remaining to next output: 6 minutes, 11 seconds
Output 40/714: t=3250000.0 yr, dE/E0=7.09e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 21 hours, 40 minutes
  Estimated time remaining to next output: 6 minutes, 12 seconds
Output 41/714: t=3260000.0 yr, dE/E0=7.00e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 21 hours, 33 minutes, 26 seconds
  Estimated time remaining to next output: 6 minutes, 12 seconds
Output 42/714: t=3270000.0 yr, dE/E0=9.28e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 21 hours, 29 minutes, 51 seconds
  Estimated time remaining to next output: 6 minutes, 12 seconds
Output 43/714: t=3280000.0 yr, dE/E0=6.35e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 21 hours, 25 minutes, 44 seconds
  Estimated time remaining to next output: 6 minutes, 12 seconds
Output 44/714: t=3290000.0 yr, dE/E0=6.66e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 21 hours, 27 minutes, 52 seconds
  Estimated time remaining to next output: 6 minutes, 13 seconds
Output 45/714: t=3300000.0 yr, dE/E0=4.58e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 21 hours, 20 minutes, 26 seconds
  Estimated time remaining to next output: 6 minutes, 13 seconds
Output 46/714: t=3310000.0 yr, dE/E0=2.94e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 21 hours, 14 minutes, 26 seconds
  Estimated time remaining to next output: 6 minutes, 13 seconds
Output 47/714: t=3320000.0 yr, dE/E0=3.00e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 21 hours, 13 minutes, 33 seconds
  Estimated time remaining to next output: 6 minutes, 13 seconds
Output 48/714: t=3330000.0 yr, dE/E0=4.02e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 21 hours, 8 minutes, 20 seconds
  Estimated time remaining to next output: 6 minutes, 13 seconds
Output 49/714: t=3340000.0 yr, dE/E0=4.42e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 21 hours, 3 minutes, 12 seconds
  Estimated time remaining to next output: 6 minutes, 13 seconds
Output 50/714: t=3350000.0 yr, dE/E0=2.90e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 21 hours, 1 minutes, 42 seconds
  Estimated time remaining to next output: 6 minutes, 14 seconds
Output 51/714: t=3360000.0 yr, dE/E0=2.63e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 21 hours, 20 seconds
  Estimated time remaining to next output: 6 minutes, 14 seconds
Output 52/714: t=3370000.0 yr, dE/E0=4.90e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 20 hours, 58 minutes, 7 seconds
  Estimated time remaining to next output: 6 minutes, 15 seconds
Output 53/714: t=3380000.0 yr, dE/E0=5.19e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 20 hours, 57 minutes, 56 seconds
  Estimated time remaining to next output: 6 minutes, 15 seconds
Output 54/714: t=3390000.0 yr, dE/E0=1.33e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 20 hours, 54 minutes, 27 seconds
  Estimated time remaining to next output: 6 minutes, 15 seconds
Output 55/714: t=3400000.0 yr, dE/E0=7.85e-09, N=802
  Estimated time remaining to complete simulation: 2 days, 20 hours, 44 minutes, 54 seconds
  Estimated time remaining to next output: 6 minutes, 15 seconds
Output 56/714: t=3410000.0 yr, dE/E0=8.03e-09, N=802
  Estimated time remaining to complete simulation: 2 days, 20 hours, 36 minutes, 57 seconds
  Estimated time remaining to next output: 6 minutes, 15 seconds
Output 57/714: t=3420000.0 yr, dE/E0=3.46e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 20 hours, 34 minutes, 13 seconds
  Estimated time remaining to next output: 6 minutes, 15 seconds
Output 58/714: t=3430000.0 yr, dE/E0=3.60e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 20 hours, 30 minutes, 15 seconds
  Estimated time remaining to next output: 6 minutes, 15 seconds
Output 59/714: t=3440000.0 yr, dE/E0=3.57e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 20 hours, 25 minutes, 44 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 60/714: t=3450000.0 yr, dE/E0=4.38e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 20 hours, 19 minutes, 14 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 61/714: t=3460000.0 yr, dE/E0=7.00e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 20 hours, 12 minutes, 14 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 62/714: t=3470000.0 yr, dE/E0=4.07e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 20 hours, 8 minutes, 11 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 63/714: t=3480000.0 yr, dE/E0=4.25e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 19 hours, 58 minutes, 21 seconds
  Estimated time remaining to next output: 6 minutes, 15 seconds
Output 64/714: t=3490000.0 yr, dE/E0=4.38e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 19 hours, 53 minutes, 8 seconds
  Estimated time remaining to next output: 6 minutes, 15 seconds
Output 65/714: t=3500000.0 yr, dE/E0=5.28e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 19 hours, 50 minutes, 2 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 66/714: t=3510000.0 yr, dE/E0=4.55e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 19 hours, 44 minutes, 58 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 67/714: t=3520000.0 yr, dE/E0=3.66e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 19 hours, 39 minutes, 16 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 68/714: t=3530000.0 yr, dE/E0=5.43e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 19 hours, 37 minutes, 45 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 69/714: t=3540000.0 yr, dE/E0=6.00e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 19 hours, 27 minutes, 15 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 70/714: t=3550000.0 yr, dE/E0=7.54e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 19 hours, 24 minutes, 23 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 71/714: t=3560000.0 yr, dE/E0=6.54e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 19 hours, 17 minutes, 31 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 72/714: t=3570000.0 yr, dE/E0=5.65e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 19 hours, 11 minutes, 48 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 73/714: t=3580000.0 yr, dE/E0=8.14e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 19 hours, 2 minutes, 45 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 74/714: t=3590000.0 yr, dE/E0=7.52e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 18 hours, 58 minutes, 43 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 75/714: t=3600000.0 yr, dE/E0=7.50e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 18 hours, 55 minutes, 29 seconds
  Estimated time remaining to next output: 6 minutes, 17 seconds
Output 76/714: t=3610000.0 yr, dE/E0=6.38e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 18 hours, 46 minutes, 59 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 77/714: t=3620000.0 yr, dE/E0=7.33e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 18 hours, 41 minutes, 6 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 78/714: t=3630000.0 yr, dE/E0=7.91e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 18 hours, 38 minutes, 41 seconds
  Estimated time remaining to next output: 6 minutes, 17 seconds
Output 79/714: t=3640000.0 yr, dE/E0=6.27e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 18 hours, 29 minutes, 22 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 80/714: t=3650000.0 yr, dE/E0=6.96e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 18 hours, 22 minutes, 4 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 81/714: t=3660000.0 yr, dE/E0=7.68e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 18 hours, 17 minutes, 36 seconds
  Estimated time remaining to next output: 6 minutes, 17 seconds
Output 82/714: t=3670000.0 yr, dE/E0=6.48e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 18 hours, 14 minutes, 56 seconds
  Estimated time remaining to next output: 6 minutes, 17 seconds
Output 83/714: t=3680000.0 yr, dE/E0=4.51e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 18 hours, 8 minutes, 43 seconds
  Estimated time remaining to next output: 6 minutes, 17 seconds
Output 84/714: t=3690000.0 yr, dE/E0=3.23e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 18 hours, 1 minutes, 50 seconds
  Estimated time remaining to next output: 6 minutes, 17 seconds
Output 85/714: t=3700000.0 yr, dE/E0=5.88e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 17 hours, 56 minutes, 58 seconds
  Estimated time remaining to next output: 6 minutes, 17 seconds
Output 86/714: t=3710000.0 yr, dE/E0=3.99e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 17 hours, 47 minutes, 24 seconds
  Estimated time remaining to next output: 6 minutes, 17 seconds
Output 87/714: t=3720000.0 yr, dE/E0=6.47e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 17 hours, 38 minutes, 46 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 88/714: t=3730000.0 yr, dE/E0=3.40e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 17 hours, 34 minutes, 9 seconds
  Estimated time remaining to next output: 6 minutes, 17 seconds
Output 89/714: t=3740000.0 yr, dE/E0=3.08e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 17 hours, 26 minutes, 21 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 90/714: t=3750000.0 yr, dE/E0=3.12e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 17 hours, 20 minutes, 4 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 91/714: t=3760000.0 yr, dE/E0=4.15e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 17 hours, 14 minutes, 19 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 92/714: t=3770000.0 yr, dE/E0=4.15e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 17 hours, 9 minutes, 18 seconds
  Estimated time remaining to next output: 6 minutes, 17 seconds
Output 93/714: t=3780000.0 yr, dE/E0=4.67e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 17 hours, 2 minutes, 18 seconds
  Estimated time remaining to next output: 6 minutes, 17 seconds
Output 94/714: t=3790000.0 yr, dE/E0=6.61e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 16 hours, 54 minutes, 36 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 95/714: t=3800000.0 yr, dE/E0=4.35e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 16 hours, 48 minutes, 23 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 96/714: t=3810000.0 yr, dE/E0=3.86e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 16 hours, 42 minutes, 12 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 97/714: t=3820000.0 yr, dE/E0=6.72e-11, N=802
  Estimated time remaining to complete simulation: 2 days, 16 hours, 36 minutes, 27 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 98/714: t=3830000.0 yr, dE/E0=3.65e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 16 hours, 27 minutes, 39 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 99/714: t=3840000.0 yr, dE/E0=4.23e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 16 hours, 23 minutes, 39 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 100/714: t=3850000.0 yr, dE/E0=6.98e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 16 hours, 16 minutes, 51 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 101/714: t=3860000.0 yr, dE/E0=6.60e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 16 hours, 9 minutes, 37 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 102/714: t=3870000.0 yr, dE/E0=6.32e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 16 hours, 2 minutes, 29 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 103/714: t=3880000.0 yr, dE/E0=7.15e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 15 hours, 54 minutes, 18 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 104/714: t=3890000.0 yr, dE/E0=6.86e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 15 hours, 49 minutes, 40 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 105/714: t=3900000.0 yr, dE/E0=7.53e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 15 hours, 43 minutes, 13 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 106/714: t=3910000.0 yr, dE/E0=7.20e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 15 hours, 36 minutes, 35 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 107/714: t=3920000.0 yr, dE/E0=4.82e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 15 hours, 28 minutes, 29 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 108/714: t=3930000.0 yr, dE/E0=3.59e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 15 hours, 21 minutes, 30 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 109/714: t=3940000.0 yr, dE/E0=3.06e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 15 hours, 14 minutes, 50 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 110/714: t=3950000.0 yr, dE/E0=4.31e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 15 hours, 11 minutes, 33 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 111/714: t=3960000.0 yr, dE/E0=7.35e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 15 hours, 4 minutes, 23 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 112/714: t=3970000.0 yr, dE/E0=8.07e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 14 hours, 58 minutes, 7 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 113/714: t=3980000.0 yr, dE/E0=6.67e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 14 hours, 53 minutes, 24 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 114/714: t=3990000.0 yr, dE/E0=9.07e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 14 hours, 45 minutes, 11 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 115/714: t=4000000.0 yr, dE/E0=9.13e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 14 hours, 38 minutes, 51 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 116/714: t=4010000.0 yr, dE/E0=1.06e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 14 hours, 32 minutes, 26 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 117/714: t=4020000.0 yr, dE/E0=9.20e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 14 hours, 25 minutes
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 118/714: t=4030000.0 yr, dE/E0=8.82e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 14 hours, 18 minutes, 52 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 119/714: t=4040000.0 yr, dE/E0=8.87e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 14 hours, 13 minutes, 23 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 120/714: t=4050000.0 yr, dE/E0=9.46e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 14 hours, 6 minutes, 46 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 121/714: t=4060000.0 yr, dE/E0=8.38e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 13 hours, 58 minutes, 56 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 122/714: t=4070000.0 yr, dE/E0=8.55e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 13 hours, 52 minutes, 59 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 123/714: t=4080000.0 yr, dE/E0=8.19e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 13 hours, 45 minutes, 53 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 124/714: t=4090000.0 yr, dE/E0=8.18e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 13 hours, 40 minutes, 32 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 125/714: t=4100000.0 yr, dE/E0=1.00e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 13 hours, 34 minutes, 49 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 126/714: t=4110000.0 yr, dE/E0=8.25e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 13 hours, 29 minutes, 2 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 127/714: t=4120000.0 yr, dE/E0=6.99e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 13 hours, 22 minutes, 4 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 128/714: t=4130000.0 yr, dE/E0=7.33e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 13 hours, 16 minutes, 30 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 129/714: t=4140000.0 yr, dE/E0=6.04e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 13 hours, 10 minutes, 21 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 130/714: t=4150000.0 yr, dE/E0=4.03e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 13 hours, 4 minutes, 32 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 131/714: t=4160000.0 yr, dE/E0=5.05e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 12 hours, 58 minutes, 35 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 132/714: t=4170000.0 yr, dE/E0=2.56e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 12 hours, 52 minutes, 7 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 133/714: t=4180000.0 yr, dE/E0=3.07e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 12 hours, 45 minutes, 40 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 134/714: t=4190000.0 yr, dE/E0=3.08e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 12 hours, 39 minutes, 1 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 135/714: t=4200000.0 yr, dE/E0=2.88e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 12 hours, 34 minutes
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 136/714: t=4210000.0 yr, dE/E0=1.78e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 12 hours, 29 minutes, 56 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 137/714: t=4220000.0 yr, dE/E0=6.99e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 12 hours, 23 minutes, 13 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 138/714: t=4230000.0 yr, dE/E0=5.55e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 12 hours, 16 minutes, 6 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 139/714: t=4240000.0 yr, dE/E0=4.99e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 12 hours, 11 minutes, 41 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 140/714: t=4250000.0 yr, dE/E0=7.04e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 12 hours, 6 minutes, 49 seconds
  Estimated time remaining to next output: 6 minutes, 17 seconds
Output 141/714: t=4260000.0 yr, dE/E0=6.20e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 12 hours, 2 minutes, 5 seconds
  Estimated time remaining to next output: 6 minutes, 17 seconds
Output 142/714: t=4270000.0 yr, dE/E0=8.64e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 11 hours, 55 minutes, 30 seconds
  Estimated time remaining to next output: 6 minutes, 17 seconds
Output 143/714: t=4280000.0 yr, dE/E0=7.43e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 11 hours, 49 minutes, 30 seconds
  Estimated time remaining to next output: 6 minutes, 17 seconds
Output 144/714: t=4290000.0 yr, dE/E0=5.11e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 11 hours, 43 minutes, 17 seconds
  Estimated time remaining to next output: 6 minutes, 17 seconds
Output 145/714: t=4300000.0 yr, dE/E0=3.87e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 11 hours, 37 minutes, 24 seconds
  Estimated time remaining to next output: 6 minutes, 17 seconds
Output 146/714: t=4310000.0 yr, dE/E0=4.75e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 11 hours, 30 minutes, 24 seconds
  Estimated time remaining to next output: 6 minutes, 17 seconds
Output 147/714: t=4320000.0 yr, dE/E0=5.11e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 11 hours, 24 minutes, 46 seconds
  Estimated time remaining to next output: 6 minutes, 17 seconds
Output 148/714: t=4330000.0 yr, dE/E0=3.92e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 11 hours, 17 minutes, 38 seconds
  Estimated time remaining to next output: 6 minutes, 17 seconds
Output 149/714: t=4340000.0 yr, dE/E0=6.11e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 11 hours, 12 minutes, 9 seconds
  Estimated time remaining to next output: 6 minutes, 17 seconds
Output 150/714: t=4350000.0 yr, dE/E0=7.12e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 11 hours, 5 minutes, 37 seconds
  Estimated time remaining to next output: 6 minutes, 17 seconds
Output 151/714: t=4360000.0 yr, dE/E0=6.98e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 10 hours, 59 minutes, 44 seconds
  Estimated time remaining to next output: 6 minutes, 17 seconds
Output 152/714: t=4370000.0 yr, dE/E0=5.27e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 10 hours, 53 minutes, 27 seconds
  Estimated time remaining to next output: 6 minutes, 17 seconds
Output 153/714: t=4380000.0 yr, dE/E0=7.11e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 10 hours, 46 minutes, 26 seconds
  Estimated time remaining to next output: 6 minutes, 17 seconds
Output 154/714: t=4390000.0 yr, dE/E0=9.12e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 10 hours, 40 minutes, 41 seconds
  Estimated time remaining to next output: 6 minutes, 17 seconds
Output 155/714: t=4400000.0 yr, dE/E0=6.97e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 10 hours, 34 minutes, 16 seconds
  Estimated time remaining to next output: 6 minutes, 17 seconds
Output 156/714: t=4410000.0 yr, dE/E0=7.17e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 10 hours, 28 minutes, 35 seconds
  Estimated time remaining to next output: 6 minutes, 17 seconds
Output 157/714: t=4420000.0 yr, dE/E0=6.89e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 10 hours, 22 minutes, 12 seconds
  Estimated time remaining to next output: 6 minutes, 17 seconds
Output 158/714: t=4430000.0 yr, dE/E0=9.50e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 10 hours, 15 minutes, 16 seconds
  Estimated time remaining to next output: 6 minutes, 17 seconds
Output 159/714: t=4440000.0 yr, dE/E0=8.18e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 10 hours, 8 minutes, 51 seconds
  Estimated time remaining to next output: 6 minutes, 17 seconds
Output 160/714: t=4450000.0 yr, dE/E0=6.87e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 10 hours, 3 minutes, 7 seconds
  Estimated time remaining to next output: 6 minutes, 17 seconds
Output 161/714: t=4460000.0 yr, dE/E0=7.93e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 9 hours, 57 minutes, 50 seconds
  Estimated time remaining to next output: 6 minutes, 17 seconds
Output 162/714: t=4470000.0 yr, dE/E0=5.76e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 9 hours, 51 minutes, 35 seconds
  Estimated time remaining to next output: 6 minutes, 17 seconds
Output 163/714: t=4480000.0 yr, dE/E0=8.48e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 9 hours, 43 minutes, 52 seconds
  Estimated time remaining to next output: 6 minutes, 17 seconds
Output 164/714: t=4490000.0 yr, dE/E0=6.71e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 9 hours, 37 minutes, 54 seconds
  Estimated time remaining to next output: 6 minutes, 17 seconds
Output 165/714: t=4500000.0 yr, dE/E0=6.14e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 9 hours, 32 minutes, 13 seconds
  Estimated time remaining to next output: 6 minutes, 17 seconds
Output 166/714: t=4510000.0 yr, dE/E0=3.25e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 9 hours, 24 minutes, 54 seconds
  Estimated time remaining to next output: 6 minutes, 17 seconds
Output 167/714: t=4520000.0 yr, dE/E0=1.57e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 9 hours, 18 minutes, 21 seconds
  Estimated time remaining to next output: 6 minutes, 17 seconds
Output 168/714: t=4530000.0 yr, dE/E0=3.84e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 9 hours, 12 minutes, 56 seconds
  Estimated time remaining to next output: 6 minutes, 17 seconds
Output 169/714: t=4540000.0 yr, dE/E0=1.23e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 9 hours, 6 minutes, 38 seconds
  Estimated time remaining to next output: 6 minutes, 17 seconds
Output 170/714: t=4550000.0 yr, dE/E0=1.68e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 9 hours, 17 seconds
  Estimated time remaining to next output: 6 minutes, 17 seconds
Output 171/714: t=4560000.0 yr, dE/E0=3.77e-09, N=802
  Estimated time remaining to complete simulation: 2 days, 8 hours, 54 minutes, 24 seconds
  Estimated time remaining to next output: 6 minutes, 17 seconds
Output 172/714: t=4570000.0 yr, dE/E0=2.63e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 8 hours, 47 minutes, 9 seconds
  Estimated time remaining to next output: 6 minutes, 17 seconds
Output 173/714: t=4580000.0 yr, dE/E0=3.50e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 8 hours, 40 minutes, 56 seconds
  Estimated time remaining to next output: 6 minutes, 17 seconds
Output 174/714: t=4590000.0 yr, dE/E0=3.90e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 8 hours, 34 minutes, 22 seconds
  Estimated time remaining to next output: 6 minutes, 17 seconds
Output 175/714: t=4600000.0 yr, dE/E0=2.47e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 8 hours, 28 minutes, 43 seconds
  Estimated time remaining to next output: 6 minutes, 17 seconds
Output 176/714: t=4610000.0 yr, dE/E0=1.74e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 8 hours, 21 minutes, 36 seconds
  Estimated time remaining to next output: 6 minutes, 17 seconds
Output 177/714: t=4620000.0 yr, dE/E0=3.39e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 8 hours, 15 minutes, 44 seconds
  Estimated time remaining to next output: 6 minutes, 17 seconds
Output 178/714: t=4630000.0 yr, dE/E0=3.32e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 8 hours, 9 minutes, 7 seconds
  Estimated time remaining to next output: 6 minutes, 17 seconds
Output 179/714: t=4640000.0 yr, dE/E0=5.20e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 8 hours, 2 minutes, 34 seconds
  Estimated time remaining to next output: 6 minutes, 17 seconds
Output 180/714: t=4650000.0 yr, dE/E0=2.46e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 7 hours, 55 minutes, 28 seconds
  Estimated time remaining to next output: 6 minutes, 17 seconds
Output 181/714: t=4660000.0 yr, dE/E0=4.29e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 7 hours, 49 minutes, 7 seconds
  Estimated time remaining to next output: 6 minutes, 17 seconds
Output 182/714: t=4670000.0 yr, dE/E0=3.97e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 7 hours, 43 minutes, 2 seconds
  Estimated time remaining to next output: 6 minutes, 17 seconds
Output 183/714: t=4680000.0 yr, dE/E0=7.44e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 7 hours, 36 minutes, 28 seconds
  Estimated time remaining to next output: 6 minutes, 17 seconds
Output 184/714: t=4690000.0 yr, dE/E0=6.43e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 7 hours, 29 minutes, 45 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 185/714: t=4700000.0 yr, dE/E0=8.24e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 7 hours, 23 minutes, 36 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 186/714: t=4710000.0 yr, dE/E0=9.89e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 7 hours, 17 minutes, 19 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 187/714: t=4720000.0 yr, dE/E0=1.02e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 7 hours, 10 minutes, 44 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 188/714: t=4730000.0 yr, dE/E0=1.01e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 7 hours, 3 minutes, 37 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 189/714: t=4740000.0 yr, dE/E0=1.10e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 6 hours, 55 minutes, 45 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 190/714: t=4750000.0 yr, dE/E0=8.14e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 6 hours, 48 minutes, 31 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 191/714: t=4760000.0 yr, dE/E0=7.56e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 6 hours, 42 minutes, 39 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 192/714: t=4770000.0 yr, dE/E0=5.90e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 6 hours, 36 minutes
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 193/714: t=4780000.0 yr, dE/E0=6.18e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 6 hours, 29 minutes, 47 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 194/714: t=4790000.0 yr, dE/E0=1.04e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 6 hours, 23 minutes, 28 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 195/714: t=4800000.0 yr, dE/E0=9.00e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 6 hours, 16 minutes, 47 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 196/714: t=4810000.0 yr, dE/E0=8.79e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 6 hours, 10 minutes, 38 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 197/714: t=4820000.0 yr, dE/E0=1.06e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 6 hours, 4 minutes, 14 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 198/714: t=4830000.0 yr, dE/E0=1.13e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 5 hours, 58 minutes, 17 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 199/714: t=4840000.0 yr, dE/E0=1.16e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 5 hours, 52 minutes, 30 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 200/714: t=4850000.0 yr, dE/E0=1.18e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 5 hours, 45 minutes, 43 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 201/714: t=4860000.0 yr, dE/E0=1.38e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 5 hours, 38 minutes, 44 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 202/714: t=4870000.0 yr, dE/E0=1.41e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 5 hours, 32 minutes, 7 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 203/714: t=4880000.0 yr, dE/E0=1.33e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 5 hours, 25 minutes, 28 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 204/714: t=4890000.0 yr, dE/E0=1.05e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 5 hours, 19 minutes, 21 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 205/714: t=4900000.0 yr, dE/E0=9.81e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 5 hours, 13 minutes, 23 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 206/714: t=4910000.0 yr, dE/E0=1.05e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 5 hours, 7 minutes, 30 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 207/714: t=4920000.0 yr, dE/E0=1.22e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 5 hours, 1 minutes, 44 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 208/714: t=4930000.0 yr, dE/E0=1.51e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 4 hours, 55 minutes, 23 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 209/714: t=4940000.0 yr, dE/E0=1.60e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 4 hours, 48 minutes, 37 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 210/714: t=4950000.0 yr, dE/E0=1.57e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 4 hours, 42 minutes, 7 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 211/714: t=4960000.0 yr, dE/E0=1.62e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 4 hours, 35 minutes, 7 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 212/714: t=4970000.0 yr, dE/E0=1.70e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 4 hours, 28 minutes, 33 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 213/714: t=4980000.0 yr, dE/E0=1.53e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 4 hours, 21 minutes, 51 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 214/714: t=4990000.0 yr, dE/E0=1.22e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 4 hours, 15 minutes, 16 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 215/714: t=5000000.0 yr, dE/E0=1.42e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 4 hours, 9 minutes, 38 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 216/714: t=5010000.0 yr, dE/E0=1.05e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 4 hours, 2 minutes, 33 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 217/714: t=5020000.0 yr, dE/E0=1.01e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 3 hours, 55 minutes, 45 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 218/714: t=5030000.0 yr, dE/E0=7.20e-08, N=802
  Estimated time remaining to complete simulation: 2 days, 3 hours, 48 minutes, 27 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 219/714: t=5040000.0 yr, dE/E0=1.32e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 3 hours, 42 minutes, 28 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 220/714: t=5050000.0 yr, dE/E0=1.31e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 3 hours, 36 minutes, 34 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 221/714: t=5060000.0 yr, dE/E0=1.51e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 3 hours, 30 minutes, 9 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 222/714: t=5070000.0 yr, dE/E0=1.30e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 3 hours, 23 minutes, 31 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 223/714: t=5080000.0 yr, dE/E0=1.43e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 3 hours, 16 minutes, 29 seconds
  Estimated time remaining to next output: 6 minutes, 15 seconds
Output 224/714: t=5090000.0 yr, dE/E0=1.38e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 3 hours, 10 minutes, 10 seconds
  Estimated time remaining to next output: 6 minutes, 15 seconds
Output 225/714: t=5100000.0 yr, dE/E0=1.69e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 3 hours, 4 minutes, 9 seconds
  Estimated time remaining to next output: 6 minutes, 15 seconds
Output 226/714: t=5110000.0 yr, dE/E0=1.65e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 2 hours, 56 minutes, 56 seconds
  Estimated time remaining to next output: 6 minutes, 15 seconds
Output 227/714: t=5120000.0 yr, dE/E0=1.95e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 2 hours, 50 minutes, 37 seconds
  Estimated time remaining to next output: 6 minutes, 15 seconds
Output 228/714: t=5130000.0 yr, dE/E0=1.93e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 2 hours, 44 minutes, 2 seconds
  Estimated time remaining to next output: 6 minutes, 15 seconds
Output 229/714: t=5140000.0 yr, dE/E0=1.68e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 2 hours, 38 minutes, 7 seconds
  Estimated time remaining to next output: 6 minutes, 15 seconds
Output 230/714: t=5150000.0 yr, dE/E0=1.79e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 2 hours, 32 minutes, 27 seconds
  Estimated time remaining to next output: 6 minutes, 15 seconds
Output 231/714: t=5160000.0 yr, dE/E0=1.82e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 2 hours, 26 minutes, 41 seconds
  Estimated time remaining to next output: 6 minutes, 15 seconds
Output 232/714: t=5170000.0 yr, dE/E0=1.73e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 2 hours, 21 minutes, 24 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 233/714: t=5180000.0 yr, dE/E0=1.78e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 2 hours, 20 minutes, 11 seconds
  Estimated time remaining to next output: 6 minutes, 16 seconds
Output 234/714: t=5190000.0 yr, dE/E0=2.02e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 2 hours, 16 minutes, 2 seconds
  Estimated time remaining to next output: 6 minutes, 17 seconds
Output 235/714: t=5200000.0 yr, dE/E0=1.83e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 2 hours, 10 minutes, 1 seconds
  Estimated time remaining to next output: 6 minutes, 17 seconds
Output 236/714: t=5210000.0 yr, dE/E0=1.93e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 2 hours, 10 minutes, 16 seconds
  Estimated time remaining to next output: 6 minutes, 17 seconds
Output 237/714: t=5220000.0 yr, dE/E0=2.19e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 2 hours, 11 minutes, 18 seconds
  Estimated time remaining to next output: 6 minutes, 18 seconds
Output 238/714: t=5230000.0 yr, dE/E0=2.29e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 2 hours, 12 minutes, 32 seconds
  Estimated time remaining to next output: 6 minutes, 19 seconds
Output 239/714: t=5240000.0 yr, dE/E0=1.97e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 2 hours, 14 minutes, 36 seconds
  Estimated time remaining to next output: 6 minutes, 20 seconds
Output 240/714: t=5250000.0 yr, dE/E0=2.14e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 2 hours, 9 minutes, 5 seconds
  Estimated time remaining to next output: 6 minutes, 20 seconds
Output 241/714: t=5260000.0 yr, dE/E0=2.39e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 2 hours, 2 minutes, 51 seconds
  Estimated time remaining to next output: 6 minutes, 20 seconds
Output 242/714: t=5270000.0 yr, dE/E0=2.43e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 2 hours, 3 minutes, 37 seconds
  Estimated time remaining to next output: 6 minutes, 21 seconds
Output 243/714: t=5280000.0 yr, dE/E0=2.57e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 2 hours, 19 seconds
  Estimated time remaining to next output: 6 minutes, 22 seconds
Output 244/714: t=5290000.0 yr, dE/E0=2.56e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 1 hours, 55 minutes, 10 seconds
  Estimated time remaining to next output: 6 minutes, 22 seconds
Output 245/714: t=5300000.0 yr, dE/E0=2.29e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 1 hours, 48 minutes, 47 seconds
  Estimated time remaining to next output: 6 minutes, 22 seconds
Output 246/714: t=5310000.0 yr, dE/E0=2.19e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 1 hours, 42 minutes, 50 seconds
  Estimated time remaining to next output: 6 minutes, 22 seconds
Output 247/714: t=5320000.0 yr, dE/E0=2.40e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 1 hours, 36 minutes, 22 seconds
  Estimated time remaining to next output: 6 minutes, 22 seconds
Output 248/714: t=5330000.0 yr, dE/E0=2.30e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 1 hours, 32 minutes, 19 seconds
  Estimated time remaining to next output: 6 minutes, 22 seconds
Output 249/714: t=5340000.0 yr, dE/E0=2.17e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 1 hours, 30 minutes, 51 seconds
  Estimated time remaining to next output: 6 minutes, 23 seconds
Output 250/714: t=5350000.0 yr, dE/E0=2.11e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 1 hours, 24 minutes, 54 seconds
  Estimated time remaining to next output: 6 minutes, 23 seconds
Output 251/714: t=5360000.0 yr, dE/E0=2.05e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 1 hours, 19 minutes, 5 seconds
  Estimated time remaining to next output: 6 minutes, 23 seconds
Output 252/714: t=5370000.0 yr, dE/E0=2.04e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 1 hours, 14 minutes, 24 seconds
  Estimated time remaining to next output: 6 minutes, 23 seconds
Output 253/714: t=5380000.0 yr, dE/E0=1.78e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 1 hours, 13 minutes, 36 seconds
  Estimated time remaining to next output: 6 minutes, 24 seconds
Output 254/714: t=5390000.0 yr, dE/E0=1.78e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 1 hours, 13 minutes, 54 seconds
  Estimated time remaining to next output: 6 minutes, 25 seconds
Output 255/714: t=5400000.0 yr, dE/E0=1.71e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 1 hours, 12 minutes, 38 seconds
  Estimated time remaining to next output: 6 minutes, 25 seconds
Output 256/714: t=5410000.0 yr, dE/E0=1.84e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 1 hours, 12 minutes, 10 seconds
  Estimated time remaining to next output: 6 minutes, 26 seconds
Output 257/714: t=5420000.0 yr, dE/E0=1.76e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 1 hours, 12 minutes, 14 seconds
  Estimated time remaining to next output: 6 minutes, 27 seconds
Output 258/714: t=5430000.0 yr, dE/E0=1.76e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 1 hours, 11 minutes, 31 seconds
  Estimated time remaining to next output: 6 minutes, 28 seconds
Output 259/714: t=5440000.0 yr, dE/E0=1.87e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 1 hours, 10 minutes, 26 seconds
  Estimated time remaining to next output: 6 minutes, 29 seconds
Output 260/714: t=5450000.0 yr, dE/E0=1.97e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 1 hours, 6 minutes, 41 seconds
  Estimated time remaining to next output: 6 minutes, 29 seconds
Output 261/714: t=5460000.0 yr, dE/E0=2.16e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 59 minutes, 52 seconds
  Estimated time remaining to next output: 6 minutes, 29 seconds
Output 262/714: t=5470000.0 yr, dE/E0=2.11e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 52 minutes, 16 seconds
  Estimated time remaining to next output: 6 minutes, 29 seconds
Output 263/714: t=5480000.0 yr, dE/E0=1.87e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 46 minutes, 8 seconds
  Estimated time remaining to next output: 6 minutes, 29 seconds
Output 264/714: t=5490000.0 yr, dE/E0=1.78e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 39 minutes
  Estimated time remaining to next output: 6 minutes, 29 seconds
Output 265/714: t=5500000.0 yr, dE/E0=2.00e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 31 minutes, 51 seconds
  Estimated time remaining to next output: 6 minutes, 29 seconds
Output 266/714: t=5510000.0 yr, dE/E0=1.96e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 24 minutes, 40 seconds
  Estimated time remaining to next output: 6 minutes, 29 seconds
Output 267/714: t=5520000.0 yr, dE/E0=1.88e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 17 minutes, 52 seconds
  Estimated time remaining to next output: 6 minutes, 28 seconds
Output 268/714: t=5530000.0 yr, dE/E0=1.99e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 11 minutes, 27 seconds
  Estimated time remaining to next output: 6 minutes, 28 seconds
Output 269/714: t=5540000.0 yr, dE/E0=2.04e-07, N=802
  Estimated time remaining to complete simulation: 2 days, 4 minutes, 32 seconds
  Estimated time remaining to next output: 6 minutes, 28 seconds
Output 270/714: t=5550000.0 yr, dE/E0=1.99e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 23 hours, 57 minutes, 37 seconds
  Estimated time remaining to next output: 6 minutes, 28 seconds
Output 271/714: t=5560000.0 yr, dE/E0=1.66e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 23 hours, 50 minutes, 53 seconds
  Estimated time remaining to next output: 6 minutes, 28 seconds
Output 272/714: t=5570000.0 yr, dE/E0=1.69e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 23 hours, 44 minutes, 6 seconds
  Estimated time remaining to next output: 6 minutes, 28 seconds
Output 273/714: t=5580000.0 yr, dE/E0=1.93e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 23 hours, 37 minutes, 9 seconds
  Estimated time remaining to next output: 6 minutes, 28 seconds
Output 274/714: t=5590000.0 yr, dE/E0=2.03e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 23 hours, 30 minutes, 22 seconds
  Estimated time remaining to next output: 6 minutes, 28 seconds
Output 275/714: t=5600000.0 yr, dE/E0=1.71e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 23 hours, 23 minutes, 15 seconds
  Estimated time remaining to next output: 6 minutes, 28 seconds
Output 276/714: t=5610000.0 yr, dE/E0=2.21e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 23 hours, 16 minutes, 20 seconds
  Estimated time remaining to next output: 6 minutes, 28 seconds
Output 277/714: t=5620000.0 yr, dE/E0=1.72e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 23 hours, 9 minutes, 17 seconds
  Estimated time remaining to next output: 6 minutes, 28 seconds
Output 278/714: t=5630000.0 yr, dE/E0=1.91e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 23 hours, 2 minutes, 41 seconds
  Estimated time remaining to next output: 6 minutes, 28 seconds
Output 279/714: t=5640000.0 yr, dE/E0=1.95e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 22 hours, 55 minutes, 55 seconds
  Estimated time remaining to next output: 6 minutes, 28 seconds
Output 280/714: t=5650000.0 yr, dE/E0=1.90e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 22 hours, 50 minutes, 18 seconds
  Estimated time remaining to next output: 6 minutes, 28 seconds
Output 281/714: t=5660000.0 yr, dE/E0=1.88e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 22 hours, 49 minutes, 54 seconds
  Estimated time remaining to next output: 6 minutes, 29 seconds
Output 282/714: t=5670000.0 yr, dE/E0=1.81e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 22 hours, 48 minutes, 57 seconds
  Estimated time remaining to next output: 6 minutes, 30 seconds
Output 283/714: t=5680000.0 yr, dE/E0=1.81e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 22 hours, 47 minutes, 40 seconds
  Estimated time remaining to next output: 6 minutes, 30 seconds
Output 284/714: t=5690000.0 yr, dE/E0=1.76e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 22 hours, 46 minutes, 50 seconds
  Estimated time remaining to next output: 6 minutes, 31 seconds
Output 285/714: t=5700000.0 yr, dE/E0=1.63e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 22 hours, 45 minutes, 58 seconds
  Estimated time remaining to next output: 6 minutes, 32 seconds
Output 286/714: t=5710000.0 yr, dE/E0=1.62e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 22 hours, 45 minutes, 8 seconds
  Estimated time remaining to next output: 6 minutes, 33 seconds
Output 287/714: t=5720000.0 yr, dE/E0=1.50e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 22 hours, 43 minutes, 48 seconds
  Estimated time remaining to next output: 6 minutes, 33 seconds
Output 288/714: t=5730000.0 yr, dE/E0=1.35e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 22 hours, 42 minutes, 25 seconds
  Estimated time remaining to next output: 6 minutes, 34 seconds
Output 289/714: t=5740000.0 yr, dE/E0=1.54e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 22 hours, 41 minutes, 26 seconds
  Estimated time remaining to next output: 6 minutes, 35 seconds
Output 290/714: t=5750000.0 yr, dE/E0=1.62e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 22 hours, 39 minutes, 47 seconds
  Estimated time remaining to next output: 6 minutes, 36 seconds
Output 291/714: t=5760000.0 yr, dE/E0=1.52e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 22 hours, 38 minutes, 40 seconds
  Estimated time remaining to next output: 6 minutes, 36 seconds
Output 292/714: t=5770000.0 yr, dE/E0=1.76e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 22 hours, 37 minutes, 27 seconds
  Estimated time remaining to next output: 6 minutes, 37 seconds
Output 293/714: t=5780000.0 yr, dE/E0=1.75e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 22 hours, 34 minutes, 56 seconds
  Estimated time remaining to next output: 6 minutes, 38 seconds
Output 294/714: t=5790000.0 yr, dE/E0=1.58e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 22 hours, 33 minutes, 26 seconds
  Estimated time remaining to next output: 6 minutes, 39 seconds
Output 295/714: t=5800000.0 yr, dE/E0=1.52e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 22 hours, 31 minutes, 21 seconds
  Estimated time remaining to next output: 6 minutes, 39 seconds
Output 296/714: t=5810000.0 yr, dE/E0=1.54e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 22 hours, 29 minutes, 42 seconds
  Estimated time remaining to next output: 6 minutes, 40 seconds
Output 297/714: t=5820000.0 yr, dE/E0=1.72e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 22 hours, 28 minutes, 59 seconds
  Estimated time remaining to next output: 6 minutes, 41 seconds
Output 298/714: t=5830000.0 yr, dE/E0=1.70e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 22 hours, 27 minutes, 26 seconds
  Estimated time remaining to next output: 6 minutes, 42 seconds
Output 299/714: t=5840000.0 yr, dE/E0=1.58e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 22 hours, 26 minutes, 7 seconds
  Estimated time remaining to next output: 6 minutes, 42 seconds
Output 300/714: t=5850000.0 yr, dE/E0=1.97e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 22 hours, 22 minutes, 58 seconds
  Estimated time remaining to next output: 6 minutes, 43 seconds
Output 301/714: t=5860000.0 yr, dE/E0=1.93e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 22 hours, 21 minutes, 4 seconds
  Estimated time remaining to next output: 6 minutes, 44 seconds
Output 302/714: t=5870000.0 yr, dE/E0=2.06e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 22 hours, 19 minutes, 28 seconds
  Estimated time remaining to next output: 6 minutes, 44 seconds
Output 303/714: t=5880000.0 yr, dE/E0=1.90e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 22 hours, 17 minutes, 1 seconds
  Estimated time remaining to next output: 6 minutes, 45 seconds
Output 304/714: t=5890000.0 yr, dE/E0=2.15e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 22 hours, 14 minutes, 13 seconds
  Estimated time remaining to next output: 6 minutes, 45 seconds
Output 305/714: t=5900000.0 yr, dE/E0=2.25e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 22 hours, 12 minutes, 6 seconds
  Estimated time remaining to next output: 6 minutes, 46 seconds
Output 306/714: t=5910000.0 yr, dE/E0=2.22e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 22 hours, 9 minutes, 17 seconds
  Estimated time remaining to next output: 6 minutes, 47 seconds
Output 307/714: t=5920000.0 yr, dE/E0=2.36e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 22 hours, 7 minutes, 37 seconds
  Estimated time remaining to next output: 6 minutes, 48 seconds
Output 308/714: t=5930000.0 yr, dE/E0=2.21e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 22 hours, 4 minutes, 5 seconds
  Estimated time remaining to next output: 6 minutes, 48 seconds
Output 309/714: t=5940000.0 yr, dE/E0=2.28e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 22 hours, 2 minutes, 16 seconds
  Estimated time remaining to next output: 6 minutes, 49 seconds
Output 310/714: t=5950000.0 yr, dE/E0=2.20e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 22 hours, 13 seconds
  Estimated time remaining to next output: 6 minutes, 49 seconds
Output 311/714: t=5960000.0 yr, dE/E0=2.30e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 21 hours, 58 minutes, 25 seconds
  Estimated time remaining to next output: 6 minutes, 50 seconds
Output 312/714: t=5970000.0 yr, dE/E0=2.41e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 21 hours, 57 minutes, 15 seconds
  Estimated time remaining to next output: 6 minutes, 51 seconds
Output 313/714: t=5980000.0 yr, dE/E0=2.51e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 21 hours, 53 minutes, 53 seconds
  Estimated time remaining to next output: 6 minutes, 52 seconds
Output 314/714: t=5990000.0 yr, dE/E0=2.28e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 21 hours, 51 minutes, 17 seconds
  Estimated time remaining to next output: 6 minutes, 52 seconds
Output 315/714: t=6000000.0 yr, dE/E0=2.25e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 21 hours, 46 minutes, 41 seconds
  Estimated time remaining to next output: 6 minutes, 53 seconds
Output 316/714: t=6010000.0 yr, dE/E0=2.20e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 21 hours, 38 minutes, 29 seconds
  Estimated time remaining to next output: 6 minutes, 52 seconds
Output 317/714: t=6020000.0 yr, dE/E0=2.13e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 21 hours, 30 minutes, 54 seconds
  Estimated time remaining to next output: 6 minutes, 52 seconds
Output 318/714: t=6030000.0 yr, dE/E0=2.04e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 21 hours, 22 minutes, 59 seconds
  Estimated time remaining to next output: 6 minutes, 52 seconds
Output 319/714: t=6040000.0 yr, dE/E0=1.92e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 21 hours, 15 minutes, 25 seconds
  Estimated time remaining to next output: 6 minutes, 52 seconds
Output 320/714: t=6050000.0 yr, dE/E0=1.93e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 21 hours, 7 minutes, 38 seconds
  Estimated time remaining to next output: 6 minutes, 52 seconds
Output 321/714: t=6060000.0 yr, dE/E0=2.00e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 20 hours, 59 minutes, 46 seconds
  Estimated time remaining to next output: 6 minutes, 52 seconds
Output 322/714: t=6070000.0 yr, dE/E0=2.23e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 20 hours, 51 minutes, 36 seconds
  Estimated time remaining to next output: 6 minutes, 51 seconds
Output 323/714: t=6080000.0 yr, dE/E0=1.97e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 20 hours, 43 minutes, 52 seconds
  Estimated time remaining to next output: 6 minutes, 51 seconds
Output 324/714: t=6090000.0 yr, dE/E0=2.06e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 20 hours, 36 minutes, 39 seconds
  Estimated time remaining to next output: 6 minutes, 51 seconds
Output 325/714: t=6100000.0 yr, dE/E0=2.07e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 20 hours, 28 minutes, 36 seconds
  Estimated time remaining to next output: 6 minutes, 51 seconds
Output 326/714: t=6110000.0 yr, dE/E0=1.69e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 20 hours, 21 minutes, 13 seconds
  Estimated time remaining to next output: 6 minutes, 51 seconds
Output 327/714: t=6120000.0 yr, dE/E0=1.72e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 20 hours, 13 minutes, 31 seconds
  Estimated time remaining to next output: 6 minutes, 51 seconds
Output 328/714: t=6130000.0 yr, dE/E0=1.75e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 20 hours, 5 minutes, 44 seconds
  Estimated time remaining to next output: 6 minutes, 51 seconds
Output 329/714: t=6140000.0 yr, dE/E0=2.37e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 19 hours, 58 minutes, 6 seconds
  Estimated time remaining to next output: 6 minutes, 51 seconds
Output 330/714: t=6150000.0 yr, dE/E0=2.45e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 19 hours, 50 minutes, 27 seconds
  Estimated time remaining to next output: 6 minutes, 51 seconds
Output 331/714: t=6160000.0 yr, dE/E0=2.22e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 19 hours, 42 minutes, 58 seconds
  Estimated time remaining to next output: 6 minutes, 50 seconds
Output 332/714: t=6170000.0 yr, dE/E0=2.18e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 19 hours, 35 minutes, 37 seconds
  Estimated time remaining to next output: 6 minutes, 50 seconds
Output 333/714: t=6180000.0 yr, dE/E0=2.25e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 19 hours, 28 minutes, 6 seconds
  Estimated time remaining to next output: 6 minutes, 50 seconds
Output 334/714: t=6190000.0 yr, dE/E0=2.24e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 19 hours, 20 minutes, 22 seconds
  Estimated time remaining to next output: 6 minutes, 50 seconds
Output 335/714: t=6200000.0 yr, dE/E0=2.25e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 19 hours, 12 minutes, 30 seconds
  Estimated time remaining to next output: 6 minutes, 50 seconds
Output 336/714: t=6210000.0 yr, dE/E0=2.21e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 19 hours, 4 minutes, 45 seconds
  Estimated time remaining to next output: 6 minutes, 50 seconds
Output 337/714: t=6220000.0 yr, dE/E0=2.02e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 18 hours, 57 minutes
  Estimated time remaining to next output: 6 minutes, 50 seconds
Output 338/714: t=6230000.0 yr, dE/E0=1.90e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 18 hours, 49 minutes, 22 seconds
  Estimated time remaining to next output: 6 minutes, 50 seconds
Output 339/714: t=6240000.0 yr, dE/E0=2.07e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 18 hours, 41 minutes, 44 seconds
  Estimated time remaining to next output: 6 minutes, 49 seconds
Output 340/714: t=6250000.0 yr, dE/E0=1.95e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 18 hours, 34 minutes, 5 seconds
  Estimated time remaining to next output: 6 minutes, 49 seconds
Output 341/714: t=6260000.0 yr, dE/E0=1.91e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 18 hours, 26 minutes, 42 seconds
  Estimated time remaining to next output: 6 minutes, 49 seconds
Output 342/714: t=6270000.0 yr, dE/E0=1.77e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 18 hours, 18 minutes, 57 seconds
  Estimated time remaining to next output: 6 minutes, 49 seconds
Output 343/714: t=6280000.0 yr, dE/E0=1.76e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 18 hours, 11 minutes, 35 seconds
  Estimated time remaining to next output: 6 minutes, 49 seconds
Output 344/714: t=6290000.0 yr, dE/E0=1.65e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 18 hours, 4 minutes, 17 seconds
  Estimated time remaining to next output: 6 minutes, 49 seconds
Output 345/714: t=6300000.0 yr, dE/E0=1.97e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 17 hours, 56 minutes, 31 seconds
  Estimated time remaining to next output: 6 minutes, 49 seconds
Output 346/714: t=6310000.0 yr, dE/E0=1.89e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 17 hours, 48 minutes, 48 seconds
  Estimated time remaining to next output: 6 minutes, 49 seconds
Output 347/714: t=6320000.0 yr, dE/E0=1.83e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 17 hours, 41 minutes, 6 seconds
  Estimated time remaining to next output: 6 minutes, 48 seconds
Output 348/714: t=6330000.0 yr, dE/E0=1.79e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 17 hours, 32 minutes, 56 seconds
  Estimated time remaining to next output: 6 minutes, 48 seconds
Output 349/714: t=6340000.0 yr, dE/E0=1.87e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 17 hours, 25 minutes, 31 seconds
  Estimated time remaining to next output: 6 minutes, 48 seconds
Output 350/714: t=6350000.0 yr, dE/E0=1.80e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 17 hours, 18 minutes, 2 seconds
  Estimated time remaining to next output: 6 minutes, 48 seconds
Output 351/714: t=6360000.0 yr, dE/E0=1.82e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 17 hours, 11 minutes, 8 seconds
  Estimated time remaining to next output: 6 minutes, 48 seconds
Output 352/714: t=6370000.0 yr, dE/E0=1.49e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 17 hours, 3 minutes, 55 seconds
  Estimated time remaining to next output: 6 minutes, 48 seconds
Output 353/714: t=6380000.0 yr, dE/E0=1.29e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 16 hours, 56 minutes, 49 seconds
  Estimated time remaining to next output: 6 minutes, 48 seconds
Output 354/714: t=6390000.0 yr, dE/E0=1.44e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 16 hours, 49 minutes, 18 seconds
  Estimated time remaining to next output: 6 minutes, 48 seconds
Output 355/714: t=6400000.0 yr, dE/E0=1.17e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 16 hours, 41 minutes, 30 seconds
  Estimated time remaining to next output: 6 minutes, 48 seconds
Output 356/714: t=6410000.0 yr, dE/E0=1.36e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 16 hours, 34 minutes, 10 seconds
  Estimated time remaining to next output: 6 minutes, 47 seconds
Output 357/714: t=6420000.0 yr, dE/E0=1.33e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 16 hours, 26 minutes, 42 seconds
  Estimated time remaining to next output: 6 minutes, 47 seconds
Output 358/714: t=6430000.0 yr, dE/E0=1.24e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 16 hours, 19 minutes, 20 seconds
  Estimated time remaining to next output: 6 minutes, 47 seconds
Output 359/714: t=6440000.0 yr, dE/E0=1.42e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 16 hours, 11 minutes, 46 seconds
  Estimated time remaining to next output: 6 minutes, 47 seconds
Output 360/714: t=6450000.0 yr, dE/E0=1.37e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 16 hours, 4 minutes, 15 seconds
  Estimated time remaining to next output: 6 minutes, 47 seconds
Output 361/714: t=6460000.0 yr, dE/E0=1.34e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 15 hours, 57 minutes, 7 seconds
  Estimated time remaining to next output: 6 minutes, 47 seconds
Output 362/714: t=6470000.0 yr, dE/E0=1.56e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 15 hours, 49 minutes, 55 seconds
  Estimated time remaining to next output: 6 minutes, 47 seconds
Output 363/714: t=6480000.0 yr, dE/E0=1.74e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 15 hours, 42 minutes, 30 seconds
  Estimated time remaining to next output: 6 minutes, 47 seconds
Output 364/714: t=6490000.0 yr, dE/E0=1.77e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 15 hours, 35 minutes, 16 seconds
  Estimated time remaining to next output: 6 minutes, 47 seconds
Output 365/714: t=6500000.0 yr, dE/E0=1.61e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 15 hours, 27 minutes, 39 seconds
  Estimated time remaining to next output: 6 minutes, 47 seconds
Output 366/714: t=6510000.0 yr, dE/E0=1.72e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 15 hours, 20 minutes, 28 seconds
  Estimated time remaining to next output: 6 minutes, 46 seconds
Output 367/714: t=6520000.0 yr, dE/E0=1.88e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 15 hours, 13 minutes, 7 seconds
  Estimated time remaining to next output: 6 minutes, 46 seconds
Output 368/714: t=6530000.0 yr, dE/E0=2.04e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 15 hours, 5 minutes, 52 seconds
  Estimated time remaining to next output: 6 minutes, 46 seconds
Output 369/714: t=6540000.0 yr, dE/E0=1.86e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 14 hours, 58 minutes, 27 seconds
  Estimated time remaining to next output: 6 minutes, 46 seconds
Output 370/714: t=6550000.0 yr, dE/E0=1.65e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 14 hours, 51 minutes
  Estimated time remaining to next output: 6 minutes, 46 seconds
Output 371/714: t=6560000.0 yr, dE/E0=1.62e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 14 hours, 43 minutes, 32 seconds
  Estimated time remaining to next output: 6 minutes, 46 seconds
Output 372/714: t=6570000.0 yr, dE/E0=1.31e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 14 hours, 36 minutes, 1 seconds
  Estimated time remaining to next output: 6 minutes, 46 seconds
Output 373/714: t=6580000.0 yr, dE/E0=1.28e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 14 hours, 29 minutes, 16 seconds
  Estimated time remaining to next output: 6 minutes, 46 seconds
Output 374/714: t=6590000.0 yr, dE/E0=1.33e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 14 hours, 21 minutes, 52 seconds
  Estimated time remaining to next output: 6 minutes, 46 seconds
Output 375/714: t=6600000.0 yr, dE/E0=1.25e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 14 hours, 14 minutes, 11 seconds
  Estimated time remaining to next output: 6 minutes, 46 seconds
Output 376/714: t=6610000.0 yr, dE/E0=1.10e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 14 hours, 6 minutes, 44 seconds
  Estimated time remaining to next output: 6 minutes, 45 seconds
Output 377/714: t=6620000.0 yr, dE/E0=1.12e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 13 hours, 59 minutes, 13 seconds
  Estimated time remaining to next output: 6 minutes, 45 seconds
Output 378/714: t=6630000.0 yr, dE/E0=1.02e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 13 hours, 51 minutes, 59 seconds
  Estimated time remaining to next output: 6 minutes, 45 seconds
Output 379/714: t=6640000.0 yr, dE/E0=1.05e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 13 hours, 44 minutes, 23 seconds
  Estimated time remaining to next output: 6 minutes, 45 seconds
Output 380/714: t=6650000.0 yr, dE/E0=1.21e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 13 hours, 36 minutes, 44 seconds
  Estimated time remaining to next output: 6 minutes, 45 seconds
Output 381/714: t=6660000.0 yr, dE/E0=1.23e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 13 hours, 29 minutes, 19 seconds
  Estimated time remaining to next output: 6 minutes, 45 seconds
Output 382/714: t=6670000.0 yr, dE/E0=1.46e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 13 hours, 22 minutes, 8 seconds
  Estimated time remaining to next output: 6 minutes, 45 seconds
Output 383/714: t=6680000.0 yr, dE/E0=1.51e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 13 hours, 14 minutes, 58 seconds
  Estimated time remaining to next output: 6 minutes, 45 seconds
Output 384/714: t=6690000.0 yr, dE/E0=1.49e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 13 hours, 7 minutes, 13 seconds
  Estimated time remaining to next output: 6 minutes, 44 seconds
Output 385/714: t=6700000.0 yr, dE/E0=1.54e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 12 hours, 59 minutes, 42 seconds
  Estimated time remaining to next output: 6 minutes, 44 seconds
Output 386/714: t=6710000.0 yr, dE/E0=1.72e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 12 hours, 52 minutes, 28 seconds
  Estimated time remaining to next output: 6 minutes, 44 seconds
Output 387/714: t=6720000.0 yr, dE/E0=1.76e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 12 hours, 44 minutes, 56 seconds
  Estimated time remaining to next output: 6 minutes, 44 seconds
Output 388/714: t=6730000.0 yr, dE/E0=1.82e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 12 hours, 37 minutes, 16 seconds
  Estimated time remaining to next output: 6 minutes, 44 seconds
Output 389/714: t=6740000.0 yr, dE/E0=1.77e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 12 hours, 29 minutes, 59 seconds
  Estimated time remaining to next output: 6 minutes, 44 seconds
Output 390/714: t=6750000.0 yr, dE/E0=1.70e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 12 hours, 22 minutes, 41 seconds
  Estimated time remaining to next output: 6 minutes, 44 seconds
Output 391/714: t=6760000.0 yr, dE/E0=1.61e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 12 hours, 15 minutes, 38 seconds
  Estimated time remaining to next output: 6 minutes, 44 seconds
Output 392/714: t=6770000.0 yr, dE/E0=1.68e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 12 hours, 8 minutes, 54 seconds
  Estimated time remaining to next output: 6 minutes, 44 seconds
Output 393/714: t=6780000.0 yr, dE/E0=1.84e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 12 hours, 1 minutes, 21 seconds
  Estimated time remaining to next output: 6 minutes, 43 seconds
Output 394/714: t=6790000.0 yr, dE/E0=1.76e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 11 hours, 54 minutes, 13 seconds
  Estimated time remaining to next output: 6 minutes, 43 seconds
Output 395/714: t=6800000.0 yr, dE/E0=1.75e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 11 hours, 47 minutes, 3 seconds
  Estimated time remaining to next output: 6 minutes, 43 seconds
Output 396/714: t=6810000.0 yr, dE/E0=1.63e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 11 hours, 39 minutes, 45 seconds
  Estimated time remaining to next output: 6 minutes, 43 seconds
Output 397/714: t=6820000.0 yr, dE/E0=1.59e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 11 hours, 32 minutes, 23 seconds
  Estimated time remaining to next output: 6 minutes, 43 seconds
Output 398/714: t=6830000.0 yr, dE/E0=1.70e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 11 hours, 25 minutes, 15 seconds
  Estimated time remaining to next output: 6 minutes, 43 seconds
Output 399/714: t=6840000.0 yr, dE/E0=1.84e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 11 hours, 17 minutes, 51 seconds
  Estimated time remaining to next output: 6 minutes, 43 seconds
Output 400/714: t=6850000.0 yr, dE/E0=2.01e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 11 hours, 10 minutes, 41 seconds
  Estimated time remaining to next output: 6 minutes, 43 seconds
Output 401/714: t=6860000.0 yr, dE/E0=1.52e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 11 hours, 3 minutes, 8 seconds
  Estimated time remaining to next output: 6 minutes, 43 seconds
Output 402/714: t=6870000.0 yr, dE/E0=1.69e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 10 hours, 56 minutes, 21 seconds
  Estimated time remaining to next output: 6 minutes, 43 seconds
Output 403/714: t=6880000.0 yr, dE/E0=1.39e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 10 hours, 49 minutes
  Estimated time remaining to next output: 6 minutes, 43 seconds
Output 404/714: t=6890000.0 yr, dE/E0=1.57e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 10 hours, 41 minutes, 48 seconds
  Estimated time remaining to next output: 6 minutes, 42 seconds
Output 405/714: t=6900000.0 yr, dE/E0=1.47e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 10 hours, 34 minutes, 21 seconds
  Estimated time remaining to next output: 6 minutes, 42 seconds
Output 406/714: t=6910000.0 yr, dE/E0=1.76e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 10 hours, 26 minutes, 58 seconds
  Estimated time remaining to next output: 6 minutes, 42 seconds
Output 407/714: t=6920000.0 yr, dE/E0=1.61e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 10 hours, 19 minutes, 49 seconds
  Estimated time remaining to next output: 6 minutes, 42 seconds
Output 408/714: t=6930000.0 yr, dE/E0=1.53e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 10 hours, 12 minutes, 52 seconds
  Estimated time remaining to next output: 6 minutes, 42 seconds
Output 409/714: t=6940000.0 yr, dE/E0=1.47e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 10 hours, 5 minutes, 37 seconds
  Estimated time remaining to next output: 6 minutes, 42 seconds
Output 410/714: t=6950000.0 yr, dE/E0=1.53e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 9 hours, 58 minutes, 23 seconds
  Estimated time remaining to next output: 6 minutes, 42 seconds
Output 411/714: t=6960000.0 yr, dE/E0=1.42e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 9 hours, 51 minutes, 17 seconds
  Estimated time remaining to next output: 6 minutes, 42 seconds
Output 412/714: t=6970000.0 yr, dE/E0=1.76e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 9 hours, 43 minutes, 57 seconds
  Estimated time remaining to next output: 6 minutes, 42 seconds
Output 413/714: t=6980000.0 yr, dE/E0=1.60e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 9 hours, 36 minutes, 54 seconds
  Estimated time remaining to next output: 6 minutes, 42 seconds
Output 414/714: t=6990000.0 yr, dE/E0=1.65e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 9 hours, 29 minutes, 38 seconds
  Estimated time remaining to next output: 6 minutes, 41 seconds
Output 415/714: t=7000000.0 yr, dE/E0=1.55e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 9 hours, 22 minutes, 34 seconds
  Estimated time remaining to next output: 6 minutes, 41 seconds
Output 416/714: t=7010000.0 yr, dE/E0=1.49e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 9 hours, 15 minutes, 27 seconds
  Estimated time remaining to next output: 6 minutes, 41 seconds
Output 417/714: t=7020000.0 yr, dE/E0=1.76e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 9 hours, 8 minutes, 20 seconds
  Estimated time remaining to next output: 6 minutes, 41 seconds
Output 418/714: t=7030000.0 yr, dE/E0=1.71e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 9 hours, 1 minutes, 12 seconds
  Estimated time remaining to next output: 6 minutes, 41 seconds
Output 419/714: t=7040000.0 yr, dE/E0=1.69e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 8 hours, 53 minutes, 55 seconds
  Estimated time remaining to next output: 6 minutes, 41 seconds
Output 420/714: t=7050000.0 yr, dE/E0=1.95e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 8 hours, 46 minutes, 55 seconds
  Estimated time remaining to next output: 6 minutes, 41 seconds
Output 421/714: t=7060000.0 yr, dE/E0=1.72e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 8 hours, 39 minutes, 38 seconds
  Estimated time remaining to next output: 6 minutes, 41 seconds
Output 422/714: t=7070000.0 yr, dE/E0=1.47e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 8 hours, 32 minutes, 31 seconds
  Estimated time remaining to next output: 6 minutes, 41 seconds
Output 423/714: t=7080000.0 yr, dE/E0=1.48e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 8 hours, 25 minutes, 41 seconds
  Estimated time remaining to next output: 6 minutes, 41 seconds
Output 424/714: t=7090000.0 yr, dE/E0=1.21e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 8 hours, 18 minutes, 41 seconds
  Estimated time remaining to next output: 6 minutes, 41 seconds
Output 425/714: t=7100000.0 yr, dE/E0=1.44e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 8 hours, 11 minutes, 38 seconds
  Estimated time remaining to next output: 6 minutes, 41 seconds
Output 426/714: t=7110000.0 yr, dE/E0=1.21e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 8 hours, 4 minutes, 35 seconds
  Estimated time remaining to next output: 6 minutes, 40 seconds
Output 427/714: t=7120000.0 yr, dE/E0=1.42e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 7 hours, 57 minutes, 40 seconds
  Estimated time remaining to next output: 6 minutes, 40 seconds
Output 428/714: t=7130000.0 yr, dE/E0=1.41e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 7 hours, 50 minutes, 32 seconds
  Estimated time remaining to next output: 6 minutes, 40 seconds
Output 429/714: t=7140000.0 yr, dE/E0=1.72e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 7 hours, 43 minutes, 21 seconds
  Estimated time remaining to next output: 6 minutes, 40 seconds
Output 430/714: t=7150000.0 yr, dE/E0=1.79e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 7 hours, 36 minutes
  Estimated time remaining to next output: 6 minutes, 40 seconds
Output 431/714: t=7160000.0 yr, dE/E0=1.66e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 7 hours, 29 minutes, 13 seconds
  Estimated time remaining to next output: 6 minutes, 40 seconds
Output 432/714: t=7170000.0 yr, dE/E0=1.41e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 7 hours, 22 minutes, 17 seconds
  Estimated time remaining to next output: 6 minutes, 40 seconds
Output 433/714: t=7180000.0 yr, dE/E0=1.27e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 7 hours, 15 minutes, 23 seconds
  Estimated time remaining to next output: 6 minutes, 40 seconds
Output 434/714: t=7190000.0 yr, dE/E0=1.43e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 7 hours, 8 minutes, 19 seconds
  Estimated time remaining to next output: 6 minutes, 40 seconds
Output 435/714: t=7200000.0 yr, dE/E0=1.17e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 7 hours, 1 minutes, 29 seconds
  Estimated time remaining to next output: 6 minutes, 40 seconds
Output 436/714: t=7210000.0 yr, dE/E0=1.08e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 6 hours, 54 minutes, 12 seconds
  Estimated time remaining to next output: 6 minutes, 40 seconds
Output 437/714: t=7220000.0 yr, dE/E0=1.07e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 6 hours, 46 minutes, 44 seconds
  Estimated time remaining to next output: 6 minutes, 40 seconds
Output 438/714: t=7230000.0 yr, dE/E0=1.17e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 6 hours, 39 minutes, 36 seconds
  Estimated time remaining to next output: 6 minutes, 39 seconds
Output 439/714: t=7240000.0 yr, dE/E0=9.23e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 6 hours, 32 minutes, 19 seconds
  Estimated time remaining to next output: 6 minutes, 39 seconds
Output 440/714: t=7250000.0 yr, dE/E0=7.75e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 6 hours, 25 minutes, 13 seconds
  Estimated time remaining to next output: 6 minutes, 39 seconds
Output 441/714: t=7260000.0 yr, dE/E0=9.14e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 6 hours, 18 minutes, 1 seconds
  Estimated time remaining to next output: 6 minutes, 39 seconds
Output 442/714: t=7270000.0 yr, dE/E0=8.22e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 6 hours, 11 minutes, 17 seconds
  Estimated time remaining to next output: 6 minutes, 39 seconds
Output 443/714: t=7280000.0 yr, dE/E0=1.14e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 6 hours, 4 minutes, 16 seconds
  Estimated time remaining to next output: 6 minutes, 39 seconds
Output 444/714: t=7290000.0 yr, dE/E0=9.94e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 5 hours, 57 minutes, 23 seconds
  Estimated time remaining to next output: 6 minutes, 39 seconds
Output 445/714: t=7300000.0 yr, dE/E0=1.03e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 5 hours, 50 minutes, 12 seconds
  Estimated time remaining to next output: 6 minutes, 39 seconds
Output 446/714: t=7310000.0 yr, dE/E0=1.06e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 5 hours, 43 minutes, 6 seconds
  Estimated time remaining to next output: 6 minutes, 39 seconds
Output 447/714: t=7320000.0 yr, dE/E0=8.56e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 5 hours, 36 minutes, 7 seconds
  Estimated time remaining to next output: 6 minutes, 39 seconds
Output 448/714: t=7330000.0 yr, dE/E0=9.70e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 5 hours, 29 minutes, 49 seconds
  Estimated time remaining to next output: 6 minutes, 39 seconds
Output 449/714: t=7340000.0 yr, dE/E0=9.96e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 5 hours, 24 minutes, 35 seconds
  Estimated time remaining to next output: 6 minutes, 39 seconds
Output 450/714: t=7350000.0 yr, dE/E0=9.25e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 5 hours, 19 minutes, 47 seconds
  Estimated time remaining to next output: 6 minutes, 39 seconds
Output 451/714: t=7360000.0 yr, dE/E0=8.66e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 5 hours, 15 minutes, 3 seconds
  Estimated time remaining to next output: 6 minutes, 40 seconds
Output 452/714: t=7370000.0 yr, dE/E0=8.70e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 5 hours, 10 minutes, 11 seconds
  Estimated time remaining to next output: 6 minutes, 40 seconds
Output 453/714: t=7380000.0 yr, dE/E0=8.81e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 5 hours, 5 minutes, 57 seconds
  Estimated time remaining to next output: 6 minutes, 41 seconds
Output 454/714: t=7390000.0 yr, dE/E0=9.51e-08, N=802
  Estimated time remaining to complete simulation: 1 days, 4 hours, 58 minutes, 56 seconds
  Estimated time remaining to next output: 6 minutes, 41 seconds
Output 455/714: t=7400000.0 yr, dE/E0=1.03e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 4 hours, 51 minutes, 51 seconds
  Estimated time remaining to next output: 6 minutes, 41 seconds
Output 456/714: t=7410000.0 yr, dE/E0=1.26e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 4 hours, 44 minutes, 40 seconds
  Estimated time remaining to next output: 6 minutes, 41 seconds
Output 457/714: t=7420000.0 yr, dE/E0=1.30e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 4 hours, 37 minutes, 42 seconds
  Estimated time remaining to next output: 6 minutes, 41 seconds
Output 458/714: t=7430000.0 yr, dE/E0=1.51e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 4 hours, 30 minutes, 41 seconds
  Estimated time remaining to next output: 6 minutes, 40 seconds
Output 459/714: t=7440000.0 yr, dE/E0=1.49e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 4 hours, 23 minutes, 33 seconds
  Estimated time remaining to next output: 6 minutes, 40 seconds
Output 460/714: t=7450000.0 yr, dE/E0=1.51e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 4 hours, 16 minutes, 20 seconds
  Estimated time remaining to next output: 6 minutes, 40 seconds
Output 461/714: t=7460000.0 yr, dE/E0=1.32e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 4 hours, 9 minutes, 27 seconds
  Estimated time remaining to next output: 6 minutes, 40 seconds
Output 462/714: t=7470000.0 yr, dE/E0=1.36e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 4 hours, 2 minutes, 27 seconds
  Estimated time remaining to next output: 6 minutes, 40 seconds
Output 463/714: t=7480000.0 yr, dE/E0=1.37e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 3 hours, 55 minutes, 14 seconds
  Estimated time remaining to next output: 6 minutes, 40 seconds
Output 464/714: t=7490000.0 yr, dE/E0=1.46e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 3 hours, 48 minutes, 13 seconds
  Estimated time remaining to next output: 6 minutes, 40 seconds
Output 465/714: t=7500000.0 yr, dE/E0=1.25e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 3 hours, 41 minutes, 6 seconds
  Estimated time remaining to next output: 6 minutes, 40 seconds
Output 466/714: t=7510000.0 yr, dE/E0=1.39e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 3 hours, 34 minutes, 20 seconds
  Estimated time remaining to next output: 6 minutes, 40 seconds
Output 467/714: t=7520000.0 yr, dE/E0=1.01e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 3 hours, 29 minutes, 7 seconds
  Estimated time remaining to next output: 6 minutes, 40 seconds
Output 468/714: t=7530000.0 yr, dE/E0=1.25e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 3 hours, 24 minutes, 31 seconds
  Estimated time remaining to next output: 6 minutes, 41 seconds
Output 469/714: t=7540000.0 yr, dE/E0=1.25e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 3 hours, 19 minutes, 36 seconds
  Estimated time remaining to next output: 6 minutes, 41 seconds
Output 470/714: t=7550000.0 yr, dE/E0=1.52e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 3 hours, 14 minutes, 27 seconds
  Estimated time remaining to next output: 6 minutes, 41 seconds
Output 471/714: t=7560000.0 yr, dE/E0=1.43e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 3 hours, 9 minutes, 34 seconds
  Estimated time remaining to next output: 6 minutes, 42 seconds
Output 472/714: t=7570000.0 yr, dE/E0=1.48e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 3 hours, 4 minutes, 9 seconds
  Estimated time remaining to next output: 6 minutes, 42 seconds
Output 473/714: t=7580000.0 yr, dE/E0=1.42e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 2 hours, 58 minutes, 52 seconds
  Estimated time remaining to next output: 6 minutes, 43 seconds
Output 474/714: t=7590000.0 yr, dE/E0=1.57e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 2 hours, 53 minutes, 54 seconds
  Estimated time remaining to next output: 6 minutes, 43 seconds
Output 475/714: t=7600000.0 yr, dE/E0=1.38e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 2 hours, 48 minutes, 40 seconds
  Estimated time remaining to next output: 6 minutes, 43 seconds
Output 476/714: t=7610000.0 yr, dE/E0=1.40e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 2 hours, 43 minutes, 32 seconds
  Estimated time remaining to next output: 6 minutes, 44 seconds
Output 477/714: t=7620000.0 yr, dE/E0=1.48e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 2 hours, 38 minutes, 3 seconds
  Estimated time remaining to next output: 6 minutes, 44 seconds
Output 478/714: t=7630000.0 yr, dE/E0=1.20e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 2 hours, 33 minutes, 4 seconds
  Estimated time remaining to next output: 6 minutes, 45 seconds
Output 479/714: t=7640000.0 yr, dE/E0=1.08e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 2 hours, 27 minutes, 39 seconds
  Estimated time remaining to next output: 6 minutes, 45 seconds
Output 480/714: t=7650000.0 yr, dE/E0=1.35e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 2 hours, 22 minutes, 17 seconds
  Estimated time remaining to next output: 6 minutes, 45 seconds
Output 481/714: t=7660000.0 yr, dE/E0=1.21e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 2 hours, 16 minutes, 55 seconds
  Estimated time remaining to next output: 6 minutes, 46 seconds
Output 482/714: t=7670000.0 yr, dE/E0=1.31e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 2 hours, 11 minutes, 26 seconds
  Estimated time remaining to next output: 6 minutes, 46 seconds
Output 483/714: t=7680000.0 yr, dE/E0=1.52e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 2 hours, 6 minutes, 9 seconds
  Estimated time remaining to next output: 6 minutes, 46 seconds
Output 484/714: t=7690000.0 yr, dE/E0=1.47e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 2 hours, 53 seconds
  Estimated time remaining to next output: 6 minutes, 47 seconds
Output 485/714: t=7700000.0 yr, dE/E0=1.35e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 1 hours, 55 minutes, 41 seconds
  Estimated time remaining to next output: 6 minutes, 47 seconds
Output 486/714: t=7710000.0 yr, dE/E0=1.45e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 1 hours, 48 minutes, 33 seconds
  Estimated time remaining to next output: 6 minutes, 47 seconds
Output 487/714: t=7720000.0 yr, dE/E0=1.03e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 1 hours, 41 minutes, 15 seconds
  Estimated time remaining to next output: 6 minutes, 47 seconds
Output 488/714: t=7730000.0 yr, dE/E0=1.14e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 1 hours, 34 minutes, 7 seconds
  Estimated time remaining to next output: 6 minutes, 47 seconds
Output 489/714: t=7740000.0 yr, dE/E0=1.10e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 1 hours, 26 minutes, 49 seconds
  Estimated time remaining to next output: 6 minutes, 47 seconds
Output 490/714: t=7750000.0 yr, dE/E0=1.19e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 1 hours, 19 minutes, 52 seconds
  Estimated time remaining to next output: 6 minutes, 47 seconds
Output 491/714: t=7760000.0 yr, dE/E0=1.24e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 1 hours, 12 minutes, 37 seconds
  Estimated time remaining to next output: 6 minutes, 46 seconds
Output 492/714: t=7770000.0 yr, dE/E0=1.25e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 1 hours, 5 minutes, 35 seconds
  Estimated time remaining to next output: 6 minutes, 46 seconds
Output 493/714: t=7780000.0 yr, dE/E0=1.39e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 58 minutes, 27 seconds
  Estimated time remaining to next output: 6 minutes, 46 seconds
Output 494/714: t=7790000.0 yr, dE/E0=1.30e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 51 minutes, 18 seconds
  Estimated time remaining to next output: 6 minutes, 46 seconds
Output 495/714: t=7800000.0 yr, dE/E0=1.16e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 44 minutes, 8 seconds
  Estimated time remaining to next output: 6 minutes, 46 seconds
Output 496/714: t=7810000.0 yr, dE/E0=1.35e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 36 minutes, 57 seconds
  Estimated time remaining to next output: 6 minutes, 46 seconds
Output 497/714: t=7820000.0 yr, dE/E0=1.31e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 29 minutes, 43 seconds
  Estimated time remaining to next output: 6 minutes, 46 seconds
Output 498/714: t=7830000.0 yr, dE/E0=1.42e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 22 minutes, 37 seconds
  Estimated time remaining to next output: 6 minutes, 46 seconds
Output 499/714: t=7840000.0 yr, dE/E0=1.34e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 15 minutes, 32 seconds
  Estimated time remaining to next output: 6 minutes, 46 seconds
Output 500/714: t=7850000.0 yr, dE/E0=1.45e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 8 minutes, 26 seconds
  Estimated time remaining to next output: 6 minutes, 46 seconds
Output 501/714: t=7860000.0 yr, dE/E0=1.25e-07, N=802
  Estimated time remaining to complete simulation: 1 days, 1 minutes, 25 seconds
  Estimated time remaining to next output: 6 minutes, 46 seconds
Output 502/714: t=7870000.0 yr, dE/E0=1.20e-07, N=802
  Estimated time remaining to complete simulation: 23 hours, 54 minutes, 26 seconds
  Estimated time remaining to next output: 6 minutes, 45 seconds
Output 503/714: t=7880000.0 yr, dE/E0=9.83e-08, N=802
  Estimated time remaining to complete simulation: 23 hours, 47 minutes, 15 seconds
  Estimated time remaining to next output: 6 minutes, 45 seconds
Output 504/714: t=7890000.0 yr, dE/E0=1.12e-07, N=802
  Estimated time remaining to complete simulation: 23 hours, 40 minutes, 1 seconds
  Estimated time remaining to next output: 6 minutes, 45 seconds
Output 505/714: t=7900000.0 yr, dE/E0=1.21e-07, N=802
  Estimated time remaining to complete simulation: 23 hours, 32 minutes, 52 seconds
  Estimated time remaining to next output: 6 minutes, 45 seconds
Output 506/714: t=7910000.0 yr, dE/E0=1.07e-07, N=802
  Estimated time remaining to complete simulation: 23 hours, 25 minutes, 55 seconds
  Estimated time remaining to next output: 6 minutes, 45 seconds
Output 507/714: t=7920000.0 yr, dE/E0=1.18e-07, N=802
  Estimated time remaining to complete simulation: 23 hours, 18 minutes, 55 seconds
  Estimated time remaining to next output: 6 minutes, 45 seconds
Output 508/714: t=7930000.0 yr, dE/E0=1.19e-07, N=802
  Estimated time remaining to complete simulation: 23 hours, 11 minutes, 41 seconds
  Estimated time remaining to next output: 6 minutes, 45 seconds
Output 509/714: t=7940000.0 yr, dE/E0=1.12e-07, N=802
  Estimated time remaining to complete simulation: 23 hours, 4 minutes, 28 seconds
  Estimated time remaining to next output: 6 minutes, 45 seconds
Output 510/714: t=7950000.0 yr, dE/E0=1.14e-07, N=802
  Estimated time remaining to complete simulation: 22 hours, 57 minutes, 20 seconds
  Estimated time remaining to next output: 6 minutes, 45 seconds
Output 511/714: t=7960000.0 yr, dE/E0=1.20e-07, N=802
  Estimated time remaining to complete simulation: 22 hours, 50 minutes, 7 seconds
  Estimated time remaining to next output: 6 minutes, 44 seconds
Output 512/714: t=7970000.0 yr, dE/E0=1.01e-07, N=802
  Estimated time remaining to complete simulation: 22 hours, 43 minutes, 2 seconds
  Estimated time remaining to next output: 6 minutes, 44 seconds
Output 513/714: t=7980000.0 yr, dE/E0=1.07e-07, N=802
  Estimated time remaining to complete simulation: 22 hours, 35 minutes, 55 seconds
  Estimated time remaining to next output: 6 minutes, 44 seconds
Output 514/714: t=7990000.0 yr, dE/E0=1.10e-07, N=802
  Estimated time remaining to complete simulation: 22 hours, 28 minutes, 52 seconds
  Estimated time remaining to next output: 6 minutes, 44 seconds
Output 515/714: t=8000000.0 yr, dE/E0=1.11e-07, N=802
  Estimated time remaining to complete simulation: 22 hours, 21 minutes, 53 seconds
  Estimated time remaining to next output: 6 minutes, 44 seconds
Output 516/714: t=8010000.0 yr, dE/E0=1.09e-07, N=802
  Estimated time remaining to complete simulation: 22 hours, 14 minutes, 42 seconds
  Estimated time remaining to next output: 6 minutes, 44 seconds
Output 517/714: t=8020000.0 yr, dE/E0=1.14e-07, N=802
  Estimated time remaining to complete simulation: 22 hours, 7 minutes, 35 seconds
  Estimated time remaining to next output: 6 minutes, 44 seconds
Output 518/714: t=8030000.0 yr, dE/E0=1.16e-07, N=802
  Estimated time remaining to complete simulation: 22 hours, 37 seconds
  Estimated time remaining to next output: 6 minutes, 44 seconds
Output 519/714: t=8040000.0 yr, dE/E0=1.11e-07, N=802
  Estimated time remaining to complete simulation: 21 hours, 53 minutes, 36 seconds
  Estimated time remaining to next output: 6 minutes, 44 seconds
Output 520/714: t=8050000.0 yr, dE/E0=9.62e-08, N=802
  Estimated time remaining to complete simulation: 21 hours, 46 minutes, 41 seconds
  Estimated time remaining to next output: 6 minutes, 44 seconds
Output 521/714: t=8060000.0 yr, dE/E0=1.05e-07, N=802
  Estimated time remaining to complete simulation: 21 hours, 39 minutes, 39 seconds
  Estimated time remaining to next output: 6 minutes, 44 seconds
Output 522/714: t=8070000.0 yr, dE/E0=9.90e-08, N=802
  Estimated time remaining to complete simulation: 21 hours, 32 minutes, 34 seconds
  Estimated time remaining to next output: 6 minutes, 43 seconds
Output 523/714: t=8080000.0 yr, dE/E0=9.17e-08, N=802
  Estimated time remaining to complete simulation: 21 hours, 25 minutes, 33 seconds
  Estimated time remaining to next output: 6 minutes, 43 seconds
Output 524/714: t=8090000.0 yr, dE/E0=9.70e-08, N=802
  Estimated time remaining to complete simulation: 21 hours, 18 minutes, 40 seconds
  Estimated time remaining to next output: 6 minutes, 43 seconds
Output 525/714: t=8100000.0 yr, dE/E0=8.83e-08, N=802
  Estimated time remaining to complete simulation: 21 hours, 11 minutes, 34 seconds
  Estimated time remaining to next output: 6 minutes, 43 seconds
Output 526/714: t=8110000.0 yr, dE/E0=9.96e-08, N=802
  Estimated time remaining to complete simulation: 21 hours, 4 minutes, 31 seconds
  Estimated time remaining to next output: 6 minutes, 43 seconds
Output 527/714: t=8120000.0 yr, dE/E0=1.22e-07, N=802
  Estimated time remaining to complete simulation: 20 hours, 57 minutes, 23 seconds
  Estimated time remaining to next output: 6 minutes, 43 seconds
Output 528/714: t=8130000.0 yr, dE/E0=1.10e-07, N=802
  Estimated time remaining to complete simulation: 20 hours, 50 minutes, 28 seconds
  Estimated time remaining to next output: 6 minutes, 43 seconds
Output 529/714: t=8140000.0 yr, dE/E0=1.12e-07, N=802
  Estimated time remaining to complete simulation: 20 hours, 43 minutes, 25 seconds
  Estimated time remaining to next output: 6 minutes, 43 seconds
Output 530/714: t=8150000.0 yr, dE/E0=1.40e-07, N=802
  Estimated time remaining to complete simulation: 20 hours, 36 minutes, 25 seconds
  Estimated time remaining to next output: 6 minutes, 43 seconds
Output 531/714: t=8160000.0 yr, dE/E0=1.32e-07, N=802
  Estimated time remaining to complete simulation: 20 hours, 29 minutes, 26 seconds
  Estimated time remaining to next output: 6 minutes, 43 seconds
Output 532/714: t=8170000.0 yr, dE/E0=1.08e-07, N=802
  Estimated time remaining to complete simulation: 20 hours, 22 minutes, 32 seconds
  Estimated time remaining to next output: 6 minutes, 43 seconds
Output 533/714: t=8180000.0 yr, dE/E0=1.10e-07, N=802
  Estimated time remaining to complete simulation: 20 hours, 15 minutes, 33 seconds
  Estimated time remaining to next output: 6 minutes, 42 seconds
Output 534/714: t=8190000.0 yr, dE/E0=1.05e-07, N=802
  Estimated time remaining to complete simulation: 20 hours, 8 minutes, 33 seconds
  Estimated time remaining to next output: 6 minutes, 42 seconds
Output 535/714: t=8200000.0 yr, dE/E0=1.08e-07, N=802
  Estimated time remaining to complete simulation: 20 hours, 1 minutes, 32 seconds
  Estimated time remaining to next output: 6 minutes, 42 seconds
Output 536/714: t=8210000.0 yr, dE/E0=9.95e-08, N=802
  Estimated time remaining to complete simulation: 19 hours, 54 minutes, 33 seconds
  Estimated time remaining to next output: 6 minutes, 42 seconds
Output 537/714: t=8220000.0 yr, dE/E0=9.42e-08, N=802
  Estimated time remaining to complete simulation: 19 hours, 47 minutes, 33 seconds
  Estimated time remaining to next output: 6 minutes, 42 seconds
Output 538/714: t=8230000.0 yr, dE/E0=1.16e-07, N=802
  Estimated time remaining to complete simulation: 19 hours, 40 minutes, 46 seconds
  Estimated time remaining to next output: 6 minutes, 42 seconds
Output 539/714: t=8240000.0 yr, dE/E0=9.06e-08, N=802
  Estimated time remaining to complete simulation: 19 hours, 33 minutes, 50 seconds
  Estimated time remaining to next output: 6 minutes, 42 seconds
Output 540/714: t=8250000.0 yr, dE/E0=8.03e-08, N=802
  Estimated time remaining to complete simulation: 19 hours, 26 minutes, 50 seconds
  Estimated time remaining to next output: 6 minutes, 42 seconds
Output 541/714: t=8260000.0 yr, dE/E0=8.51e-08, N=802
  Estimated time remaining to complete simulation: 19 hours, 19 minutes, 52 seconds
  Estimated time remaining to next output: 6 minutes, 42 seconds
Output 542/714: t=8270000.0 yr, dE/E0=7.02e-08, N=802
  Estimated time remaining to complete simulation: 19 hours, 12 minutes, 50 seconds
  Estimated time remaining to next output: 6 minutes, 42 seconds
Output 543/714: t=8280000.0 yr, dE/E0=1.11e-07, N=802
  Estimated time remaining to complete simulation: 19 hours, 6 minutes
  Estimated time remaining to next output: 6 minutes, 42 seconds
Output 544/714: t=8290000.0 yr, dE/E0=9.08e-08, N=802
  Estimated time remaining to complete simulation: 18 hours, 59 minutes, 10 seconds
  Estimated time remaining to next output: 6 minutes, 42 seconds
Output 545/714: t=8300000.0 yr, dE/E0=9.85e-08, N=802
  Estimated time remaining to complete simulation: 18 hours, 52 minutes, 11 seconds
  Estimated time remaining to next output: 6 minutes, 41 seconds
Output 546/714: t=8310000.0 yr, dE/E0=6.74e-08, N=802
  Estimated time remaining to complete simulation: 18 hours, 45 minutes, 20 seconds
  Estimated time remaining to next output: 6 minutes, 41 seconds
Output 547/714: t=8320000.0 yr, dE/E0=6.39e-08, N=802
  Estimated time remaining to complete simulation: 18 hours, 38 minutes, 24 seconds
  Estimated time remaining to next output: 6 minutes, 41 seconds
Output 548/714: t=8330000.0 yr, dE/E0=7.40e-08, N=802
  Estimated time remaining to complete simulation: 18 hours, 31 minutes, 28 seconds
  Estimated time remaining to next output: 6 minutes, 41 seconds
Output 549/714: t=8340000.0 yr, dE/E0=9.74e-08, N=802
  Estimated time remaining to complete simulation: 18 hours, 24 minutes, 29 seconds
  Estimated time remaining to next output: 6 minutes, 41 seconds
Output 550/714: t=8350000.0 yr, dE/E0=8.44e-08, N=802
  Estimated time remaining to complete simulation: 18 hours, 17 minutes, 25 seconds
  Estimated time remaining to next output: 6 minutes, 41 seconds
Output 551/714: t=8360000.0 yr, dE/E0=8.57e-08, N=802
  Estimated time remaining to complete simulation: 18 hours, 10 minutes, 27 seconds
  Estimated time remaining to next output: 6 minutes, 41 seconds
Output 552/714: t=8370000.0 yr, dE/E0=9.76e-08, N=802
  Estimated time remaining to complete simulation: 18 hours, 3 minutes, 28 seconds
  Estimated time remaining to next output: 6 minutes, 41 seconds
Output 553/714: t=8380000.0 yr, dE/E0=8.08e-08, N=802
  Estimated time remaining to complete simulation: 17 hours, 56 minutes, 41 seconds
  Estimated time remaining to next output: 6 minutes, 41 seconds
Output 554/714: t=8390000.0 yr, dE/E0=9.65e-08, N=802
  Estimated time remaining to complete simulation: 17 hours, 49 minutes, 48 seconds
  Estimated time remaining to next output: 6 minutes, 41 seconds
Output 555/714: t=8400000.0 yr, dE/E0=9.58e-08, N=802
  Estimated time remaining to complete simulation: 17 hours, 42 minutes, 50 seconds
  Estimated time remaining to next output: 6 minutes, 41 seconds
Output 556/714: t=8410000.0 yr, dE/E0=8.82e-08, N=802
  Estimated time remaining to complete simulation: 17 hours, 35 minutes, 54 seconds
  Estimated time remaining to next output: 6 minutes, 40 seconds
Output 557/714: t=8420000.0 yr, dE/E0=9.53e-08, N=802
  Estimated time remaining to complete simulation: 17 hours, 29 minutes, 2 seconds
  Estimated time remaining to next output: 6 minutes, 40 seconds
Output 558/714: t=8430000.0 yr, dE/E0=1.25e-07, N=802
  Estimated time remaining to complete simulation: 17 hours, 22 minutes, 16 seconds
  Estimated time remaining to next output: 6 minutes, 40 seconds
Output 559/714: t=8440000.0 yr, dE/E0=1.32e-07, N=802
  Estimated time remaining to complete simulation: 17 hours, 15 minutes, 24 seconds
  Estimated time remaining to next output: 6 minutes, 40 seconds
Output 560/714: t=8450000.0 yr, dE/E0=1.31e-07, N=802
  Estimated time remaining to complete simulation: 17 hours, 8 minutes, 35 seconds
  Estimated time remaining to next output: 6 minutes, 40 seconds
Output 561/714: t=8460000.0 yr, dE/E0=1.13e-07, N=802
  Estimated time remaining to complete simulation: 17 hours, 1 minutes, 42 seconds
  Estimated time remaining to next output: 6 minutes, 40 seconds
Output 562/714: t=8470000.0 yr, dE/E0=1.14e-07, N=802
  Estimated time remaining to complete simulation: 16 hours, 54 minutes, 51 seconds
  Estimated time remaining to next output: 6 minutes, 40 seconds
Output 563/714: t=8480000.0 yr, dE/E0=1.20e-07, N=802
  Estimated time remaining to complete simulation: 16 hours, 48 minutes, 3 seconds
  Estimated time remaining to next output: 6 minutes, 40 seconds
Output 564/714: t=8490000.0 yr, dE/E0=9.32e-08, N=802
  Estimated time remaining to complete simulation: 16 hours, 41 minutes, 9 seconds
  Estimated time remaining to next output: 6 minutes, 40 seconds
Output 565/714: t=8500000.0 yr, dE/E0=9.49e-08, N=802
  Estimated time remaining to complete simulation: 16 hours, 34 minutes, 20 seconds
  Estimated time remaining to next output: 6 minutes, 40 seconds
Output 566/714: t=8510000.0 yr, dE/E0=7.62e-08, N=802
  Estimated time remaining to complete simulation: 16 hours, 27 minutes, 29 seconds
  Estimated time remaining to next output: 6 minutes, 40 seconds
Output 567/714: t=8520000.0 yr, dE/E0=7.77e-08, N=802
  Estimated time remaining to complete simulation: 16 hours, 20 minutes, 33 seconds
  Estimated time remaining to next output: 6 minutes, 40 seconds
Output 568/714: t=8530000.0 yr, dE/E0=9.62e-08, N=802
  Estimated time remaining to complete simulation: 16 hours, 13 minutes, 48 seconds
  Estimated time remaining to next output: 6 minutes, 40 seconds
Output 569/714: t=8540000.0 yr, dE/E0=9.78e-08, N=802
  Estimated time remaining to complete simulation: 16 hours, 6 minutes, 53 seconds
  Estimated time remaining to next output: 6 minutes, 40 seconds
Output 570/714: t=8550000.0 yr, dE/E0=8.96e-08, N=802
  Estimated time remaining to complete simulation: 16 hours, 1 seconds
  Estimated time remaining to next output: 6 minutes, 40 seconds
Output 571/714: t=8560000.0 yr, dE/E0=1.02e-07, N=802
  Estimated time remaining to complete simulation: 15 hours, 53 minutes, 1 seconds
  Estimated time remaining to next output: 6 minutes, 39 seconds
Output 572/714: t=8570000.0 yr, dE/E0=1.24e-07, N=802
  Estimated time remaining to complete simulation: 15 hours, 46 minutes, 9 seconds
  Estimated time remaining to next output: 6 minutes, 39 seconds
Output 573/714: t=8580000.0 yr, dE/E0=1.30e-07, N=802
  Estimated time remaining to complete simulation: 15 hours, 39 minutes, 14 seconds
  Estimated time remaining to next output: 6 minutes, 39 seconds
Output 574/714: t=8590000.0 yr, dE/E0=1.15e-07, N=802
  Estimated time remaining to complete simulation: 15 hours, 32 minutes, 22 seconds
  Estimated time remaining to next output: 6 minutes, 39 seconds
Output 575/714: t=8600000.0 yr, dE/E0=1.15e-07, N=802
  Estimated time remaining to complete simulation: 15 hours, 25 minutes, 28 seconds
  Estimated time remaining to next output: 6 minutes, 39 seconds
Output 576/714: t=8610000.0 yr, dE/E0=1.04e-07, N=802
  Estimated time remaining to complete simulation: 15 hours, 18 minutes, 38 seconds
  Estimated time remaining to next output: 6 minutes, 39 seconds
Output 577/714: t=8620000.0 yr, dE/E0=1.14e-07, N=802
  Estimated time remaining to complete simulation: 15 hours, 11 minutes, 47 seconds
  Estimated time remaining to next output: 6 minutes, 39 seconds
Output 578/714: t=8630000.0 yr, dE/E0=1.28e-07, N=802
  Estimated time remaining to complete simulation: 15 hours, 5 minutes, 1 seconds
  Estimated time remaining to next output: 6 minutes, 39 seconds
Output 579/714: t=8640000.0 yr, dE/E0=1.10e-07, N=802
  Estimated time remaining to complete simulation: 14 hours, 58 minutes, 14 seconds
  Estimated time remaining to next output: 6 minutes, 39 seconds
Output 580/714: t=8650000.0 yr, dE/E0=1.03e-07, N=802
  Estimated time remaining to complete simulation: 14 hours, 51 minutes, 29 seconds
  Estimated time remaining to next output: 6 minutes, 39 seconds
Output 581/714: t=8660000.0 yr, dE/E0=1.21e-07, N=802
  Estimated time remaining to complete simulation: 14 hours, 44 minutes, 37 seconds
  Estimated time remaining to next output: 6 minutes, 39 seconds
Output 582/714: t=8670000.0 yr, dE/E0=1.17e-07, N=802
  Estimated time remaining to complete simulation: 14 hours, 37 minutes, 52 seconds
  Estimated time remaining to next output: 6 minutes, 39 seconds
Output 583/714: t=8680000.0 yr, dE/E0=1.27e-07, N=802
  Estimated time remaining to complete simulation: 14 hours, 31 minutes, 4 seconds
  Estimated time remaining to next output: 6 minutes, 38 seconds
Output 584/714: t=8690000.0 yr, dE/E0=1.08e-07, N=802
  Estimated time remaining to complete simulation: 14 hours, 24 minutes, 15 seconds
  Estimated time remaining to next output: 6 minutes, 38 seconds
Output 585/714: t=8700000.0 yr, dE/E0=1.29e-07, N=802
  Estimated time remaining to complete simulation: 14 hours, 17 minutes, 29 seconds
  Estimated time remaining to next output: 6 minutes, 38 seconds
Output 586/714: t=8710000.0 yr, dE/E0=1.32e-07, N=802
  Estimated time remaining to complete simulation: 14 hours, 10 minutes, 38 seconds
  Estimated time remaining to next output: 6 minutes, 38 seconds
Output 587/714: t=8720000.0 yr, dE/E0=1.17e-07, N=802
  Estimated time remaining to complete simulation: 14 hours, 3 minutes, 53 seconds
  Estimated time remaining to next output: 6 minutes, 38 seconds
Output 588/714: t=8730000.0 yr, dE/E0=1.17e-07, N=802
  Estimated time remaining to complete simulation: 13 hours, 57 minutes, 7 seconds
  Estimated time remaining to next output: 6 minutes, 38 seconds
Output 589/714: t=8740000.0 yr, dE/E0=1.27e-07, N=802
  Estimated time remaining to complete simulation: 13 hours, 50 minutes, 18 seconds
  Estimated time remaining to next output: 6 minutes, 38 seconds
Output 590/714: t=8750000.0 yr, dE/E0=1.22e-07, N=802
  Estimated time remaining to complete simulation: 13 hours, 43 minutes, 28 seconds
  Estimated time remaining to next output: 6 minutes, 38 seconds
Output 591/714: t=8760000.0 yr, dE/E0=1.22e-07, N=802
  Estimated time remaining to complete simulation: 13 hours, 36 minutes, 36 seconds
  Estimated time remaining to next output: 6 minutes, 38 seconds
Output 592/714: t=8770000.0 yr, dE/E0=1.17e-07, N=802
  Estimated time remaining to complete simulation: 13 hours, 29 minutes, 47 seconds
  Estimated time remaining to next output: 6 minutes, 38 seconds
Output 593/714: t=8780000.0 yr, dE/E0=9.36e-08, N=802
  Estimated time remaining to complete simulation: 13 hours, 22 minutes, 57 seconds
  Estimated time remaining to next output: 6 minutes, 38 seconds
Output 594/714: t=8790000.0 yr, dE/E0=8.93e-08, N=802
  Estimated time remaining to complete simulation: 13 hours, 16 minutes, 10 seconds
  Estimated time remaining to next output: 6 minutes, 38 seconds
Output 595/714: t=8800000.0 yr, dE/E0=1.03e-07, N=802
  Estimated time remaining to complete simulation: 13 hours, 9 minutes, 22 seconds
  Estimated time remaining to next output: 6 minutes, 38 seconds
Output 596/714: t=8810000.0 yr, dE/E0=1.03e-07, N=802
  Estimated time remaining to complete simulation: 13 hours, 2 minutes, 36 seconds
  Estimated time remaining to next output: 6 minutes, 37 seconds
Output 597/714: t=8820000.0 yr, dE/E0=8.55e-08, N=802
  Estimated time remaining to complete simulation: 12 hours, 55 minutes, 50 seconds
  Estimated time remaining to next output: 6 minutes, 37 seconds
Output 598/714: t=8830000.0 yr, dE/E0=7.76e-08, N=802
  Estimated time remaining to complete simulation: 12 hours, 49 minutes, 6 seconds
  Estimated time remaining to next output: 6 minutes, 37 seconds
Output 599/714: t=8840000.0 yr, dE/E0=5.64e-08, N=802
  Estimated time remaining to complete simulation: 12 hours, 42 minutes, 18 seconds
  Estimated time remaining to next output: 6 minutes, 37 seconds
Output 600/714: t=8850000.0 yr, dE/E0=5.35e-08, N=802
  Estimated time remaining to complete simulation: 12 hours, 35 minutes, 33 seconds
  Estimated time remaining to next output: 6 minutes, 37 seconds
Output 601/714: t=8860000.0 yr, dE/E0=3.71e-08, N=802
  Estimated time remaining to complete simulation: 12 hours, 28 minutes, 47 seconds
  Estimated time remaining to next output: 6 minutes, 37 seconds
Output 602/714: t=8870000.0 yr, dE/E0=5.35e-08, N=802
  Estimated time remaining to complete simulation: 12 hours, 22 minutes, 1 seconds
  Estimated time remaining to next output: 6 minutes, 37 seconds
Output 603/714: t=8880000.0 yr, dE/E0=5.74e-08, N=802
  Estimated time remaining to complete simulation: 12 hours, 15 minutes, 18 seconds
  Estimated time remaining to next output: 6 minutes, 37 seconds
Output 604/714: t=8890000.0 yr, dE/E0=5.31e-08, N=802
  Estimated time remaining to complete simulation: 12 hours, 8 minutes, 31 seconds
  Estimated time remaining to next output: 6 minutes, 37 seconds
Output 605/714: t=8900000.0 yr, dE/E0=5.52e-08, N=802
  Estimated time remaining to complete simulation: 12 hours, 1 minutes, 43 seconds
  Estimated time remaining to next output: 6 minutes, 37 seconds
Output 606/714: t=8910000.0 yr, dE/E0=4.50e-08, N=802
  Estimated time remaining to complete simulation: 11 hours, 54 minutes, 56 seconds
  Estimated time remaining to next output: 6 minutes, 37 seconds
Output 607/714: t=8920000.0 yr, dE/E0=5.68e-08, N=802
  Estimated time remaining to complete simulation: 11 hours, 48 minutes, 12 seconds
  Estimated time remaining to next output: 6 minutes, 37 seconds
Output 608/714: t=8930000.0 yr, dE/E0=6.84e-08, N=802
  Estimated time remaining to complete simulation: 11 hours, 41 minutes, 26 seconds
  Estimated time remaining to next output: 6 minutes, 37 seconds
Output 609/714: t=8940000.0 yr, dE/E0=4.39e-08, N=802
  Estimated time remaining to complete simulation: 11 hours, 34 minutes, 45 seconds
  Estimated time remaining to next output: 6 minutes, 37 seconds
Output 610/714: t=8950000.0 yr, dE/E0=7.45e-08, N=802
  Estimated time remaining to complete simulation: 11 hours, 28 minutes, 1 seconds
  Estimated time remaining to next output: 6 minutes, 36 seconds
Output 611/714: t=8960000.0 yr, dE/E0=6.06e-08, N=802
  Estimated time remaining to complete simulation: 11 hours, 21 minutes, 16 seconds
  Estimated time remaining to next output: 6 minutes, 36 seconds
Output 612/714: t=8970000.0 yr, dE/E0=7.11e-08, N=802
  Estimated time remaining to complete simulation: 11 hours, 14 minutes, 28 seconds
  Estimated time remaining to next output: 6 minutes, 36 seconds
Output 613/714: t=8980000.0 yr, dE/E0=8.18e-08, N=802
  Estimated time remaining to complete simulation: 11 hours, 7 minutes, 43 seconds
  Estimated time remaining to next output: 6 minutes, 36 seconds
Output 614/714: t=8990000.0 yr, dE/E0=3.28e-08, N=802
  Estimated time remaining to complete simulation: 11 hours, 57 seconds
  Estimated time remaining to next output: 6 minutes, 36 seconds
Output 615/714: t=9000000.0 yr, dE/E0=3.39e-08, N=802
  Estimated time remaining to complete simulation: 10 hours, 54 minutes, 14 seconds
  Estimated time remaining to next output: 6 minutes, 36 seconds
Output 616/714: t=9010000.0 yr, dE/E0=4.93e-08, N=802
  Estimated time remaining to complete simulation: 10 hours, 47 minutes, 33 seconds
  Estimated time remaining to next output: 6 minutes, 36 seconds
Output 617/714: t=9020000.0 yr, dE/E0=5.98e-08, N=802
  Estimated time remaining to complete simulation: 10 hours, 40 minutes, 49 seconds
  Estimated time remaining to next output: 6 minutes, 36 seconds
Output 618/714: t=9030000.0 yr, dE/E0=5.38e-08, N=802
  Estimated time remaining to complete simulation: 10 hours, 34 minutes, 3 seconds
  Estimated time remaining to next output: 6 minutes, 36 seconds
Output 619/714: t=9040000.0 yr, dE/E0=6.30e-08, N=802
  Estimated time remaining to complete simulation: 10 hours, 27 minutes, 23 seconds
  Estimated time remaining to next output: 6 minutes, 36 seconds
Output 620/714: t=9050000.0 yr, dE/E0=4.18e-08, N=802
  Estimated time remaining to complete simulation: 10 hours, 20 minutes, 42 seconds
  Estimated time remaining to next output: 6 minutes, 36 seconds
Output 621/714: t=9060000.0 yr, dE/E0=6.99e-08, N=802
  Estimated time remaining to complete simulation: 10 hours, 13 minutes, 57 seconds
  Estimated time remaining to next output: 6 minutes, 36 seconds
Output 622/714: t=9070000.0 yr, dE/E0=5.73e-08, N=802
  Estimated time remaining to complete simulation: 10 hours, 7 minutes, 14 seconds
  Estimated time remaining to next output: 6 minutes, 36 seconds
Output 623/714: t=9080000.0 yr, dE/E0=7.53e-08, N=802
  Estimated time remaining to complete simulation: 10 hours, 30 seconds
  Estimated time remaining to next output: 6 minutes, 35 seconds
Output 624/714: t=9090000.0 yr, dE/E0=5.69e-08, N=802
  Estimated time remaining to complete simulation: 9 hours, 53 minutes, 48 seconds
  Estimated time remaining to next output: 6 minutes, 35 seconds
Output 625/714: t=9100000.0 yr, dE/E0=6.76e-08, N=802
  Estimated time remaining to complete simulation: 9 hours, 47 minutes, 6 seconds
  Estimated time remaining to next output: 6 minutes, 35 seconds
Output 626/714: t=9110000.0 yr, dE/E0=7.21e-08, N=802
  Estimated time remaining to complete simulation: 9 hours, 40 minutes, 25 seconds
  Estimated time remaining to next output: 6 minutes, 35 seconds
Output 627/714: t=9120000.0 yr, dE/E0=7.92e-08, N=802
  Estimated time remaining to complete simulation: 9 hours, 33 minutes, 46 seconds
  Estimated time remaining to next output: 6 minutes, 35 seconds
Output 628/714: t=9130000.0 yr, dE/E0=6.80e-08, N=802
  Estimated time remaining to complete simulation: 9 hours, 27 minutes, 4 seconds
  Estimated time remaining to next output: 6 minutes, 35 seconds
Output 629/714: t=9140000.0 yr, dE/E0=4.54e-08, N=802
  Estimated time remaining to complete simulation: 9 hours, 20 minutes, 24 seconds
  Estimated time remaining to next output: 6 minutes, 35 seconds
Output 630/714: t=9150000.0 yr, dE/E0=4.96e-08, N=802
  Estimated time remaining to complete simulation: 9 hours, 13 minutes, 43 seconds
  Estimated time remaining to next output: 6 minutes, 35 seconds
Output 631/714: t=9160000.0 yr, dE/E0=4.24e-08, N=802
  Estimated time remaining to complete simulation: 9 hours, 7 minutes, 2 seconds
  Estimated time remaining to next output: 6 minutes, 35 seconds
Output 632/714: t=9170000.0 yr, dE/E0=6.46e-08, N=802
  Estimated time remaining to complete simulation: 9 hours, 24 seconds
  Estimated time remaining to next output: 6 minutes, 35 seconds
Output 633/714: t=9180000.0 yr, dE/E0=3.41e-08, N=802
  Estimated time remaining to complete simulation: 8 hours, 53 minutes, 42 seconds
  Estimated time remaining to next output: 6 minutes, 35 seconds
Output 634/714: t=9190000.0 yr, dE/E0=2.27e-08, N=802
  Estimated time remaining to complete simulation: 8 hours, 46 minutes, 57 seconds
  Estimated time remaining to next output: 6 minutes, 35 seconds
Output 635/714: t=9200000.0 yr, dE/E0=3.30e-08, N=802
  Estimated time remaining to complete simulation: 8 hours, 40 minutes, 17 seconds
  Estimated time remaining to next output: 6 minutes, 35 seconds
Output 636/714: t=9210000.0 yr, dE/E0=3.34e-08, N=802
  Estimated time remaining to complete simulation: 8 hours, 33 minutes, 36 seconds
  Estimated time remaining to next output: 6 minutes, 35 seconds
Output 637/714: t=9220000.0 yr, dE/E0=2.98e-08, N=802
  Estimated time remaining to complete simulation: 8 hours, 26 minutes, 54 seconds
  Estimated time remaining to next output: 6 minutes, 34 seconds
Output 638/714: t=9230000.0 yr, dE/E0=1.36e-08, N=802
  Estimated time remaining to complete simulation: 8 hours, 20 minutes, 15 seconds
  Estimated time remaining to next output: 6 minutes, 34 seconds
Output 639/714: t=9240000.0 yr, dE/E0=1.45e-08, N=802
  Estimated time remaining to complete simulation: 8 hours, 13 minutes, 35 seconds
  Estimated time remaining to next output: 6 minutes, 34 seconds
Output 640/714: t=9250000.0 yr, dE/E0=2.78e-08, N=802
  Estimated time remaining to complete simulation: 8 hours, 6 minutes, 55 seconds
  Estimated time remaining to next output: 6 minutes, 34 seconds
Output 641/714: t=9260000.0 yr, dE/E0=2.60e-08, N=802
  Estimated time remaining to complete simulation: 8 hours, 17 seconds
  Estimated time remaining to next output: 6 minutes, 34 seconds
Output 642/714: t=9270000.0 yr, dE/E0=4.19e-08, N=802
  Estimated time remaining to complete simulation: 7 hours, 53 minutes, 38 seconds
  Estimated time remaining to next output: 6 minutes, 34 seconds
Output 643/714: t=9280000.0 yr, dE/E0=2.63e-08, N=802
  Estimated time remaining to complete simulation: 7 hours, 46 minutes, 57 seconds
  Estimated time remaining to next output: 6 minutes, 34 seconds
Output 644/714: t=9290000.0 yr, dE/E0=3.05e-08, N=802
  Estimated time remaining to complete simulation: 7 hours, 40 minutes, 16 seconds
  Estimated time remaining to next output: 6 minutes, 34 seconds
Output 645/714: t=9300000.0 yr, dE/E0=1.35e-08, N=802
  Estimated time remaining to complete simulation: 7 hours, 33 minutes, 37 seconds
  Estimated time remaining to next output: 6 minutes, 34 seconds
Output 646/714: t=9310000.0 yr, dE/E0=2.82e-09, N=802
  Estimated time remaining to complete simulation: 7 hours, 26 minutes, 59 seconds
  Estimated time remaining to next output: 6 minutes, 34 seconds
Output 647/714: t=9320000.0 yr, dE/E0=1.71e-08, N=802
  Estimated time remaining to complete simulation: 7 hours, 20 minutes, 20 seconds
  Estimated time remaining to next output: 6 minutes, 34 seconds
Output 648/714: t=9330000.0 yr, dE/E0=1.63e-08, N=802
  Estimated time remaining to complete simulation: 7 hours, 13 minutes, 39 seconds
  Estimated time remaining to next output: 6 minutes, 34 seconds
Output 649/714: t=9340000.0 yr, dE/E0=5.78e-09, N=802
  Estimated time remaining to complete simulation: 7 hours, 7 minutes, 2 seconds
  Estimated time remaining to next output: 6 minutes, 34 seconds
Output 650/714: t=9350000.0 yr, dE/E0=1.82e-08, N=802
  Estimated time remaining to complete simulation: 7 hours, 21 seconds
  Estimated time remaining to next output: 6 minutes, 34 seconds
Output 651/714: t=9360000.0 yr, dE/E0=3.89e-08, N=802
  Estimated time remaining to complete simulation: 6 hours, 53 minutes, 42 seconds
  Estimated time remaining to next output: 6 minutes, 34 seconds
Output 652/714: t=9370000.0 yr, dE/E0=2.88e-08, N=802
  Estimated time remaining to complete simulation: 6 hours, 47 minutes, 4 seconds
  Estimated time remaining to next output: 6 minutes, 33 seconds
Output 653/714: t=9380000.0 yr, dE/E0=1.46e-08, N=802
  Estimated time remaining to complete simulation: 6 hours, 40 minutes, 27 seconds
  Estimated time remaining to next output: 6 minutes, 33 seconds
Output 654/714: t=9390000.0 yr, dE/E0=4.43e-08, N=802
  Estimated time remaining to complete simulation: 6 hours, 33 minutes, 48 seconds
  Estimated time remaining to next output: 6 minutes, 33 seconds
Output 655/714: t=9400000.0 yr, dE/E0=3.08e-08, N=802
  Estimated time remaining to complete simulation: 6 hours, 27 minutes, 10 seconds
  Estimated time remaining to next output: 6 minutes, 33 seconds
Output 656/714: t=9410000.0 yr, dE/E0=1.47e-08, N=802
  Estimated time remaining to complete simulation: 6 hours, 20 minutes, 33 seconds
  Estimated time remaining to next output: 6 minutes, 33 seconds
Output 657/714: t=9420000.0 yr, dE/E0=1.65e-08, N=802
  Estimated time remaining to complete simulation: 6 hours, 13 minutes, 54 seconds
  Estimated time remaining to next output: 6 minutes, 33 seconds
Output 658/714: t=9430000.0 yr, dE/E0=1.53e-08, N=802
  Estimated time remaining to complete simulation: 6 hours, 7 minutes, 15 seconds
  Estimated time remaining to next output: 6 minutes, 33 seconds
Output 659/714: t=9440000.0 yr, dE/E0=1.47e-08, N=802
  Estimated time remaining to complete simulation: 6 hours, 38 seconds
  Estimated time remaining to next output: 6 minutes, 33 seconds
Output 660/714: t=9450000.0 yr, dE/E0=2.82e-08, N=802
  Estimated time remaining to complete simulation: 5 hours, 54 minutes, 3 seconds
  Estimated time remaining to next output: 6 minutes, 33 seconds
Output 661/714: t=9460000.0 yr, dE/E0=9.34e-09, N=802
  Estimated time remaining to complete simulation: 5 hours, 47 minutes, 25 seconds
  Estimated time remaining to next output: 6 minutes, 33 seconds
Output 662/714: t=9470000.0 yr, dE/E0=2.76e-08, N=802
  Estimated time remaining to complete simulation: 5 hours, 40 minutes, 48 seconds
  Estimated time remaining to next output: 6 minutes, 33 seconds
Output 663/714: t=9480000.0 yr, dE/E0=3.40e-08, N=802
  Estimated time remaining to complete simulation: 5 hours, 34 minutes, 12 seconds
  Estimated time remaining to next output: 6 minutes, 33 seconds
Output 664/714: t=9490000.0 yr, dE/E0=7.53e-09, N=802
  Estimated time remaining to complete simulation: 5 hours, 27 minutes, 34 seconds
  Estimated time remaining to next output: 6 minutes, 33 seconds
Output 665/714: t=9500000.0 yr, dE/E0=3.87e-08, N=802
  Estimated time remaining to complete simulation: 5 hours, 20 minutes, 56 seconds
  Estimated time remaining to next output: 6 minutes, 32 seconds
Output 666/714: t=9510000.0 yr, dE/E0=9.26e-09, N=802
  Estimated time remaining to complete simulation: 5 hours, 14 minutes, 18 seconds
  Estimated time remaining to next output: 6 minutes, 32 seconds
Output 667/714: t=9520000.0 yr, dE/E0=8.99e-09, N=802
  Estimated time remaining to complete simulation: 5 hours, 7 minutes, 40 seconds
  Estimated time remaining to next output: 6 minutes, 32 seconds
Output 668/714: t=9530000.0 yr, dE/E0=2.28e-08, N=802
  Estimated time remaining to complete simulation: 5 hours, 1 minutes, 4 seconds
  Estimated time remaining to next output: 6 minutes, 32 seconds
Output 669/714: t=9540000.0 yr, dE/E0=2.20e-08, N=802
  Estimated time remaining to complete simulation: 4 hours, 54 minutes, 26 seconds
  Estimated time remaining to next output: 6 minutes, 32 seconds
Output 670/714: t=9550000.0 yr, dE/E0=1.18e-08, N=802
  Estimated time remaining to complete simulation: 4 hours, 47 minutes, 49 seconds
  Estimated time remaining to next output: 6 minutes, 32 seconds
Output 671/714: t=9560000.0 yr, dE/E0=1.21e-08, N=802
  Estimated time remaining to complete simulation: 4 hours, 41 minutes, 12 seconds
  Estimated time remaining to next output: 6 minutes, 32 seconds
Output 672/714: t=9570000.0 yr, dE/E0=5.98e-09, N=802
  Estimated time remaining to complete simulation: 4 hours, 34 minutes, 36 seconds
  Estimated time remaining to next output: 6 minutes, 32 seconds
Output 673/714: t=9580000.0 yr, dE/E0=3.68e-08, N=802
  Estimated time remaining to complete simulation: 4 hours, 28 minutes
  Estimated time remaining to next output: 6 minutes, 32 seconds
Output 674/714: t=9590000.0 yr, dE/E0=3.19e-08, N=802
  Estimated time remaining to complete simulation: 4 hours, 21 minutes, 24 seconds
  Estimated time remaining to next output: 6 minutes, 32 seconds
Output 675/714: t=9600000.0 yr, dE/E0=1.71e-08, N=802
  Estimated time remaining to complete simulation: 4 hours, 14 minutes, 48 seconds
  Estimated time remaining to next output: 6 minutes, 32 seconds
Output 676/714: t=9610000.0 yr, dE/E0=2.07e-08, N=802
  Estimated time remaining to complete simulation: 4 hours, 8 minutes, 11 seconds
  Estimated time remaining to next output: 6 minutes, 31 seconds
Output 677/714: t=9620000.0 yr, dE/E0=1.96e-08, N=802
  Estimated time remaining to complete simulation: 4 hours, 1 minutes, 36 seconds
  Estimated time remaining to next output: 6 minutes, 31 seconds
Output 678/714: t=9630000.0 yr, dE/E0=3.68e-08, N=802
  Estimated time remaining to complete simulation: 3 hours, 55 minutes, 1 seconds
  Estimated time remaining to next output: 6 minutes, 31 seconds
Output 679/714: t=9640000.0 yr, dE/E0=2.62e-08, N=802
  Estimated time remaining to complete simulation: 3 hours, 48 minutes, 26 seconds
  Estimated time remaining to next output: 6 minutes, 31 seconds
Output 680/714: t=9650000.0 yr, dE/E0=4.14e-08, N=802
  Estimated time remaining to complete simulation: 3 hours, 41 minutes, 52 seconds
  Estimated time remaining to next output: 6 minutes, 31 seconds
Output 681/714: t=9660000.0 yr, dE/E0=4.96e-08, N=802
  Estimated time remaining to complete simulation: 3 hours, 35 minutes, 18 seconds
  Estimated time remaining to next output: 6 minutes, 31 seconds
Output 682/714: t=9670000.0 yr, dE/E0=1.88e-08, N=802
  Estimated time remaining to complete simulation: 3 hours, 28 minutes, 43 seconds
  Estimated time remaining to next output: 6 minutes, 31 seconds
Output 683/714: t=9680000.0 yr, dE/E0=2.75e-08, N=802
  Estimated time remaining to complete simulation: 3 hours, 22 minutes, 9 seconds
  Estimated time remaining to next output: 6 minutes, 31 seconds
Output 684/714: t=9690000.0 yr, dE/E0=2.11e-08, N=802
  Estimated time remaining to complete simulation: 3 hours, 15 minutes, 35 seconds
  Estimated time remaining to next output: 6 minutes, 31 seconds
Output 685/714: t=9700000.0 yr, dE/E0=2.85e-08, N=802
  Estimated time remaining to complete simulation: 3 hours, 9 minutes, 1 seconds
  Estimated time remaining to next output: 6 minutes, 31 seconds
Output 686/714: t=9710000.0 yr, dE/E0=3.06e-08, N=802
  Estimated time remaining to complete simulation: 3 hours, 2 minutes, 27 seconds
  Estimated time remaining to next output: 6 minutes, 30 seconds
Output 687/714: t=9720000.0 yr, dE/E0=1.12e-08, N=802
  Estimated time remaining to complete simulation: 2 hours, 55 minutes, 53 seconds
  Estimated time remaining to next output: 6 minutes, 30 seconds
Output 688/714: t=9730000.0 yr, dE/E0=2.88e-08, N=802
  Estimated time remaining to complete simulation: 2 hours, 49 minutes, 20 seconds
  Estimated time remaining to next output: 6 minutes, 30 seconds
Output 689/714: t=9740000.0 yr, dE/E0=3.32e-08, N=802
  Estimated time remaining to complete simulation: 2 hours, 42 minutes, 47 seconds
  Estimated time remaining to next output: 6 minutes, 30 seconds
Output 690/714: t=9750000.0 yr, dE/E0=2.26e-08, N=802
  Estimated time remaining to complete simulation: 2 hours, 36 minutes, 13 seconds
  Estimated time remaining to next output: 6 minutes, 30 seconds
Output 691/714: t=9760000.0 yr, dE/E0=1.03e-08, N=802
  Estimated time remaining to complete simulation: 2 hours, 29 minutes, 41 seconds
  Estimated time remaining to next output: 6 minutes, 30 seconds
Output 692/714: t=9770000.0 yr, dE/E0=2.14e-08, N=802
  Estimated time remaining to complete simulation: 2 hours, 23 minutes, 7 seconds
  Estimated time remaining to next output: 6 minutes, 30 seconds
Output 693/714: t=9780000.0 yr, dE/E0=1.43e-08, N=802
  Estimated time remaining to complete simulation: 2 hours, 16 minutes, 36 seconds
  Estimated time remaining to next output: 6 minutes, 30 seconds
Output 694/714: t=9790000.0 yr, dE/E0=1.16e-08, N=802
  Estimated time remaining to complete simulation: 2 hours, 10 minutes, 3 seconds
  Estimated time remaining to next output: 6 minutes, 30 seconds
Output 695/714: t=9800000.0 yr, dE/E0=2.07e-08, N=802
  Estimated time remaining to complete simulation: 2 hours, 3 minutes, 31 seconds
  Estimated time remaining to next output: 6 minutes, 30 seconds
Output 696/714: t=9810000.0 yr, dE/E0=4.37e-08, N=802
  Estimated time remaining to complete simulation: 1 hours, 57 minutes
  Estimated time remaining to next output: 6 minutes, 30 seconds
Output 697/714: t=9820000.0 yr, dE/E0=3.38e-08, N=802
  Estimated time remaining to complete simulation: 1 hours, 50 minutes, 28 seconds
  Estimated time remaining to next output: 6 minutes, 29 seconds
Output 698/714: t=9830000.0 yr, dE/E0=4.37e-08, N=802
  Estimated time remaining to complete simulation: 1 hours, 43 minutes, 57 seconds
  Estimated time remaining to next output: 6 minutes, 29 seconds
Output 699/714: t=9840000.0 yr, dE/E0=3.42e-08, N=802
  Estimated time remaining to complete simulation: 1 hours, 37 minutes, 25 seconds
  Estimated time remaining to next output: 6 minutes, 29 seconds
Output 700/714: t=9850000.0 yr, dE/E0=3.35e-08, N=802
  Estimated time remaining to complete simulation: 1 hours, 30 minutes, 54 seconds
  Estimated time remaining to next output: 6 minutes, 29 seconds
Output 701/714: t=9860000.0 yr, dE/E0=1.39e-08, N=802
  Estimated time remaining to complete simulation: 1 hours, 24 minutes, 24 seconds
  Estimated time remaining to next output: 6 minutes, 29 seconds
Output 702/714: t=9870000.0 yr, dE/E0=3.00e-08, N=802
  Estimated time remaining to complete simulation: 1 hours, 17 minutes, 53 seconds
  Estimated time remaining to next output: 6 minutes, 29 seconds
Output 703/714: t=9880000.0 yr, dE/E0=3.77e-08, N=802
  Estimated time remaining to complete simulation: 1 hours, 11 minutes, 22 seconds
  Estimated time remaining to next output: 6 minutes, 29 seconds
Output 704/714: t=9890000.0 yr, dE/E0=3.62e-08, N=802
  Estimated time remaining to complete simulation: 1 hours, 4 minutes, 52 seconds
  Estimated time remaining to next output: 6 minutes, 29 seconds
Output 705/714: t=9900000.0 yr, dE/E0=2.31e-08, N=802
  Estimated time remaining to complete simulation: 58 minutes, 22 seconds
  Estimated time remaining to next output: 6 minutes, 29 seconds
Output 706/714: t=9910000.0 yr, dE/E0=3.41e-08, N=802
  Estimated time remaining to complete simulation: 51 minutes, 52 seconds
  Estimated time remaining to next output: 6 minutes, 29 seconds
Output 707/714: t=9920000.0 yr, dE/E0=1.45e-08, N=802
  Estimated time remaining to complete simulation: 45 minutes, 22 seconds
  Estimated time remaining to next output: 6 minutes, 28 seconds
Output 708/714: t=9930000.0 yr, dE/E0=1.55e-08, N=802
  Estimated time remaining to complete simulation: 38 minutes, 53 seconds
  Estimated time remaining to next output: 6 minutes, 28 seconds
Output 709/714: t=9940000.0 yr, dE/E0=5.38e-09, N=802
  Estimated time remaining to complete simulation: 32 minutes, 24 seconds
  Estimated time remaining to next output: 6 minutes, 28 seconds
Output 710/714: t=9950000.0 yr, dE/E0=1.30e-08, N=802
  Estimated time remaining to complete simulation: 25 minutes, 54 seconds
  Estimated time remaining to next output: 6 minutes, 28 seconds
Output 711/714: t=9960000.0 yr, dE/E0=9.36e-09, N=802
  Estimated time remaining to complete simulation: 19 minutes, 25 seconds
  Estimated time remaining to next output: 6 minutes, 28 seconds
Output 712/714: t=9970000.0 yr, dE/E0=1.18e-08, N=802
  Estimated time remaining to complete simulation: 12 minutes, 56 seconds
  Estimated time remaining to next output: 6 minutes, 28 seconds
Output 713/714: t=9980000.0 yr, dE/E0=1.51e-08, N=802
  Estimated time remaining to complete simulation: 6 minutes, 28 seconds
  Estimated time remaining to next output: 6 minutes, 28 seconds
Output 714/714: t=9990000.0 yr, dE/E0=5.49e-09, N=802
  Estimated time remaining to complete simulation: 0 seconds
Output 715/714: t=10000000.0 yr, dE/E0=3.31e-09, N=802
  Estimated time remaining to complete simulation: -1 months, 4 weeks, 1 days, 23 hours, 53 minutes, 32 seconds

Simulation complete.
Total runtime: 3 days, 5 hours, 6 minutes, 14 seconds

Krivov & Booth (2018) self-stirring check (Eqs. 9-10):
  NOTE: a giant planet is present; the two-population self-stirring model assumes no external perturber, so C_e below is only indicative.
  Final time:                 t = 1.000000e+07 yr
  Rayleigh outlier cut:       e > 5 sigma = 2.7120e-01 (sigma = median(e)/sqrt(2 ln 2) = 5.4239e-02)
  Stirred-disk check:         median(e) = 6.3862e-02 vs 30 x disk.emax = 9.6000e-04 -> stirred, cut applied
  Excluded MPs:               21 -- MP_26 (e = 0.7019), MP_365 (e = 0.6233), MP_579 (e = 0.5737), MP_353 (e = 0.5692), MP_683 (e = 0.5457), MP_130 (e = 0.5443), MP_634 (e = 0.4871), MP_598 (e = 0.4856), MP_603 (e = 0.4834), MP_417 (e = 0.4404), MP_261 (e = 0.3930), MP_186 (e = 0.3795), MP_734 (e = 0.3722), MP_258 (e = 0.3713), MP_587 (e = 0.3599), MP_140 (e = 0.3566), MP_467 (e = 0.3398), MP_420 (e = 0.3281), MP_93 (e = 0.3233), MP_696 (e = 0.3200), MP_240 (e = 0.3161)
  KS test of kept e vs Rayleigh: D = 0.0552, p = 0.0167  (WARNING: p < 0.05, kept e deviates from a Rayleigh distribution)
  RMS eccentricity (779 of 800 MPs): 7.859057e-02  (all MPs: 1.072499e-01)
  Belt geometry:              a = 100, da = 10, a/da = 10
  Masses:                     M_max = 4.504445e-08 Msun, M_disc = 3.003490e-06 Msun
  Implied stirring timescale: T = 5.242618e+11 yr
  Effective stirring factor:  C_e = 1409.9139  (all MPs, no cut: 4889.8861)
  WARNING: C_e = 1409.9139 >= 40 (Ida & Makino 1993 canonical value) -- this run stirs at or above the analytic self-stirring rate.
Saved archive: outputs/SS_800MP_10Myr_PSD2C_100Mearth_lorentzian/SS_800MP_10Myr_PSD2C_100Mearth_lorentzian.bin
Number of snapshots saved: 1002
Archive time range: 0.000e+00 yr to 1.000e+07 yr
Particle-name check: OK (1002 snapshots)
Loaded snapshot table from archive.
role
massive_planetesimal    800
star                      1
giant_planet              1
Name: count, dtype: int64
Saved: outputs/SS_800MP_10Myr_PSD2C_100Mearth_lorentzian/figures/survival_fraction_vs_time.png
Saved: outputs/SS_800MP_10Myr_PSD2C_100Mearth_lorentzian/figures/mean_semimajor_axis_vs_time.png
Saved: outputs/SS_800MP_10Myr_PSD2C_100Mearth_lorentzian/figures/mean_eccentricity_vs_time.png
Saved: outputs/SS_800MP_10Myr_PSD2C_100Mearth_lorentzian/figures/rms_eccentricity_vs_time.png
Saved: outputs/SS_800MP_10Myr_PSD2C_100Mearth_lorentzian/figures/rms_inclination_vs_time.png
Saved: outputs/SS_800MP_10Myr_PSD2C_100Mearth_lorentzian/figures/data/orbits_initial_final.csv
Saved: outputs/SS_800MP_10Myr_PSD2C_100Mearth_lorentzian/figures/a_vs_e_initial_final.png
Saved: outputs/SS_800MP_10Myr_PSD2C_100Mearth_lorentzian/figures/a_vs_i_initial_final.png
Inner plotted edge = 95.04 AU
Outer plotted edge = 104.92 AU
Saved: outputs/SS_800MP_10Myr_PSD2C_100Mearth_lorentzian/figures/xy_initial_final.png
All summary figures saved.
```
