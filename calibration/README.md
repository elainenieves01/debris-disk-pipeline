# calibration

Cross-run checks comparing N-body output against analytic expectations.

## `plot_kirvov_calibration.py`

RMS eccentricity vs time (log-log) for the near-massless control
`SS_100MP_100Myr_6e-5Mearth` and the self-stirring sweep
`SS_100MP_100Myr_{10,30,50}xStir`, overlaid with the Krivov & Booth (2018)
analytic self-stirring prediction (their Eqs. 9-10, viscous stirring after
Ida & Makino 1993):

```
T^-1   = (1 / 2 pi) * C_e * Omega * (a / da) * (M / Mstar) * (Mdisc / Mstar)
RMS(e) = (2 t / T)^(1/4)
```

with `C_e = 40`, `Omega = sqrt(G Mstar / a^3)` at the belt centre
(`a = 100 AU`, `da = 10 AU`), `M` the individual planetesimal mass and
`Mdisc` the total disk mass. Every planetesimal is a stirrer, so
`M = Mdisc / 100`; each run gets its own analytic curve because
`RMS(e) ~ (M Mdisc)^(1/4)`.

Only the control and the 10x / 30x / 50x runs exist so far (no 20x / 40x).

Run:

```
python calibration/plot_kirvov_calibration.py
```

Outputs:

- `calibration/rmse_kirvov_calibration.png` — control + 10x / 30x / 50x
- `calibration/rmse_kirvov_calibration_stir_only.png` — 10x / 30x / 50x only

Edit the `FIGURES` dict in the script to change which runs land on which figure.
