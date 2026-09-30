"""End-to-end test for src/plotting/apply_rayleigh_cut.py.

The snapshot table is synthetic (build_snapshot_table is patched out): particle
names read back from small hand-built REBOUND 5.0.0 archives are not reliable
within one test process, while the CLI's job -- config, cut factor, output
folders, CSV and figures -- does not depend on the archive reader.
"""

import os
import sys

import numpy as np
import pandas as pd
import pytest
import yaml

_SRC = os.path.join(os.path.dirname(__file__), "..", "src")
for _sub in ("plotting", "utilities"):
    sys.path.insert(0, os.path.join(_SRC, _sub))

import apply_rayleigh_cut  # noqa: E402
from apply_rayleigh_cut import main as apply_cut_main  # noqa: E402

FIGURES = (
    "survival_fraction_vs_time.png",
    "mean_semimajor_axis_vs_time.png",
    "mean_eccentricity_vs_time.png",
    "rms_eccentricity_vs_time.png",
    "rms_eccentricity_vs_time_all_vs_cut.png",
    "rms_inclination_vs_time.png",
    "a_vs_e_initial_final.png",
    "a_vs_i_initial_final.png",
    "xy_initial_final.png",
)


def _snapshot_table(final_e):
    """Initial snapshot at the cold [0, emax] draw, final snapshot at final_e."""
    rng = np.random.default_rng(2)
    n = len(final_e)
    a = rng.uniform(95, 105, n)
    phase = rng.uniform(0, 2 * np.pi, n)
    rows = []
    for snap, t, ecc in ((0, 0.0, rng.uniform(0, 3.2e-5, n)), (1, 1.0e5, final_e)):
        rows.append(dict(snapshot=snap, time_yr=t, role="star", particle_index=0,
                         name="star", a_AU=np.nan, e=np.nan, inc_deg=np.nan,
                         x_AU=0.0, y_AU=0.0, z_AU=0.0))
        for k in range(n):
            rows.append(dict(snapshot=snap, time_yr=t, role="massive_planetesimal",
                             particle_index=k + 1, name=f"MP_{k}", a_AU=a[k], e=ecc[k],
                             inc_deg=0.1, x_AU=a[k] * np.cos(phase[k]),
                             y_AU=a[k] * np.sin(phase[k]), z_AU=0.0))
    return pd.DataFrame(rows)


@pytest.fixture
def make_run(tmp_path, monkeypatch):
    def _make(final_e, extra_config=None):
        run = tmp_path / "run"
        run.mkdir()
        config = {
            "simulation": {"name": "run"},
            "disk": {"amin": 95.0, "amax": 105.0, "emin": 0.0, "emax": 3.2e-5},
            "plots": {"dpi": 40},
            **(extra_config or {}),
        }
        (run / "config.yaml").write_text(yaml.safe_dump(config))
        (run / "run.bin").write_bytes(b"")  # the CLI only checks it exists
        table = _snapshot_table(np.asarray(final_e, dtype=float))
        monkeypatch.setattr(apply_rayleigh_cut, "build_snapshot_table",
                            lambda path: table)
        return run
    return _make


def test_cut_figures_written_to_subfolder_only(make_run):
    e = np.random.default_rng(0).rayleigh(0.01, 300)
    e[4] = 0.4  # scattered body
    run = make_run(e)

    assert apply_cut_main(["--run", str(run), "--no-stamp"]) == ["MP_4"]

    cut_dir = run / "figures" / "rayleigh_cut_5sigma"
    for name in FIGURES:
        assert (cut_dir / name).stat().st_size > 0
        assert not (run / "figures" / name).exists()  # originals untouched

    excluded = pd.read_csv(cut_dir / "excluded_bodies.csv")
    assert list(excluded["name"]) == ["MP_4"]
    assert excluded["nsigma"].iloc[0] == 5
    assert excluded["final_e"].iloc[0] > excluded["e_cut"].iloc[0]


def test_nsigma_flag_and_config_set_the_factor(make_run):
    e = np.random.default_rng(0).rayleigh(0.01, 300)
    e[4] = 0.4    # far outlier: cut at 5 and 3 sigma
    e[9] = 0.042  # ~4 sigma: kept at 5, cut at 3
    run = make_run(e, extra_config={"rayleigh_cut": {"nsigma": 3}})
    figures = run / "figures"

    # the config factor (3) is the default ...
    assert {"MP_4", "MP_9"} <= set(apply_cut_main(["--run", str(run), "--no-stamp"]))
    assert (figures / "rayleigh_cut_3sigma" / "excluded_bodies.csv").exists()
    # ... and --nsigma overrides it, into its own folder, leaving the 3 sigma one
    assert apply_cut_main(["--run", str(run), "--no-stamp", "--nsigma", "5"]) == ["MP_4"]
    assert (figures / "rayleigh_cut_5sigma" / "excluded_bodies.csv").exists()
    assert (figures / "rayleigh_cut_3sigma" / "excluded_bodies.csv").exists()


def test_nothing_written_when_disk_not_stirred(make_run):
    e = np.linspace(1e-6, 3e-5, 300)  # still at the initial [0, emax] draw
    e[4] = 1e-3
    run = make_run(e)

    assert apply_cut_main(["--run", str(run), "--no-stamp"]) == []
    assert not any((run / "figures").glob("rayleigh_cut*"))
