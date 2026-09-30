"""Auto axis limits and the saved-table replot for the a-e / a-i figures."""

import os
import sys

import numpy as np
import pandas as pd

_SRC = os.path.join(os.path.dirname(__file__), "..", "src")
for _sub in ("plotting", "utilities"):
    sys.path.insert(0, os.path.join(_SRC, _sub))

import summary_figures as sf  # noqa: E402
from replot_orbits import main as replot_main  # noqa: E402


def _snapshot_table(n=200, seed=0):
    """Disk at 95-105 AU, giant planet at 3 AU, one scattered and one unbound body."""
    rng = np.random.default_rng(seed)
    rows = []
    for snap, t in ((0, 0.0), (1, 1e6)):
        rows.append(dict(snapshot=snap, time_yr=t, role="star", particle_index=0,
                         name="star", a_AU=np.nan, e=np.nan, inc_deg=np.nan))
        rows.append(dict(snapshot=snap, time_yr=t, role="giant_planet", particle_index=1,
                         name="GP", a_AU=3.0, e=0.07, inc_deg=1.0))
        for k in range(n):
            a, e, inc = rng.uniform(95, 105), rng.uniform(0, 0.05), rng.uniform(0, 2)
            if snap == 1 and k == 0:
                a, e, inc = 900.0, 0.9, 30.0
            if snap == 1 and k == 1:
                a, e, inc = -50.0, 1.3, 40.0
            rows.append(dict(snapshot=snap, time_yr=t, role="massive_planetesimal",
                             particle_index=2 + k, name=f"MP_{k}", a_AU=a, e=e, inc_deg=inc))
    return pd.DataFrame(rows)


def test_auto_limits_frame_the_disk_not_the_planet_or_outliers():
    first, last = sf.get_first_last_snapshots(_snapshot_table())
    (a_lo, a_hi), (e_lo, e_hi) = sf.auto_orbit_limits(first, last, "e")

    assert 90 < a_lo < 95 and 105 < a_hi < 110
    assert e_lo < 0 < 0.05 < e_hi < 0.07


def test_auto_limits_follow_tiny_inclinations():
    df = _snapshot_table()
    df.loc[df["role"] == "massive_planetesimal", "inc_deg"] *= 1e-5
    first, last = sf.get_first_last_snapshots(df)
    _, (_, i_hi) = sf.auto_orbit_limits(first, last, "inc_deg")

    assert i_hi < 1e-4


def test_user_limits_override_one_end_at_a_time():
    assert sf._merge_limits((90, None), (80.0, 120.0)) == (90.0, 120.0)
    assert sf._merge_limits(None, (80.0, 120.0)) == (80.0, 120.0)


def test_config_limits_are_read():
    config = {"plots": {"limits": {"ae": {"xlim": [90, 110], "ylim": None}}}}
    assert sf._config_limits(config, "ae") == ([90, 110], None)
    assert sf._config_limits(config, "ai") == (None, None)
    assert sf._config_limits({}, "ae") == (None, None)


def test_replot_from_saved_table(tmp_path):
    first, last = sf.get_first_last_snapshots(_snapshot_table())
    sf.save_orbit_table(first, last, tmp_path)

    replot_main(["--run", str(tmp_path), "--a", "98", "102", "--e", "0", "auto",
                 "--suffix", "_zoom", "--no-stamp"])

    figures = tmp_path / "figures"
    assert (figures / "a_vs_e_initial_final_zoom.png").stat().st_size > 0
    assert (figures / "a_vs_i_initial_final_zoom.png").stat().st_size > 0


def test_rms_eccentricity_rayleigh_cut_drops_scattered_body(tmp_path):
    # Two snapshots of a Rayleigh-stirred disk with one body flung out.
    rng = np.random.default_rng(3)
    rows = []
    for snap, t in ((0, 0.0), (1, 1.0e4)):
        e = rng.rayleigh(0.01, 400)
        e[5] = 0.4
        for k, ek in enumerate(e):
            rows.append({"snapshot": snap, "time_yr": t, "role": "massive_planetesimal",
                         "name": f"MP_{k}", "e": ek})
    df = pd.DataFrame(rows)

    times, rms_all, rms_cut, excluded = sf.rms_eccentricity_rayleigh_cut(df, 3.2e-5, 5.0)
    assert excluded == ["MP_5"]
    assert np.all(rms_cut < rms_all)

    sf.plot_rms_eccentricity_rayleigh_cut(df, tmp_path, 3.2e-5, 5.0, dpi=50)
    assert (tmp_path / "figures" / "rms_eccentricity_vs_time_all_vs_cut.png").exists()
    assert not (tmp_path / "figures" / "rms_eccentricity_vs_time.png").exists()
