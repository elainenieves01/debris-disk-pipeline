"""Initial semimajor-axis distributions (disk.a_distribution)."""

import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src", "utilities"))

from semimajor_axis import SemimajorAxisSampler, lorentzian_log_params  # noqa: E402

DISK = {"amin": 95.0, "amax": 105.0}
LOR = {**DISK, "a_distribution": "lorentzian", "a_center": 100.0, "a_sigma": 2.0}


def test_uniform_default_matches_previous_draws():
    s = SemimajorAxisSampler(DISK)
    r1, r2 = np.random.default_rng(42), np.random.default_rng(42)
    for _ in range(50):
        assert s.draw(r1) == r2.uniform(95.0, 105.0)


def test_lorentzian_peak_formula():
    ln_mu, gamma = lorentzian_log_params(100.0, 2.0)
    assert ln_mu == pytest.approx(np.log(100.0**2 / np.sqrt(100.0**2 + 2.0**2)))
    assert gamma == pytest.approx(np.sqrt(np.log(1 + (2.0 / 100.0) ** 2)))


def test_lorentzian_one_draw_per_body_and_within_bounds():
    s = SemimajorAxisSampler(LOR)
    r1, r2 = np.random.default_rng(0), np.random.default_rng(0)
    a = np.array([s.draw(r1) for _ in range(20000)])
    for _ in range(20000):
        r2.uniform()
    assert r1.uniform() == r2.uniform()  # streams stay in lockstep
    assert a.min() >= 95.0 and a.max() <= 105.0


def test_lorentzian_median_and_quartiles():
    s = SemimajorAxisSampler({**LOR, "amin": 1.0, "amax": 1e4})
    rng = np.random.default_rng(1)
    ln_a = np.log([s.draw(rng) for _ in range(200000)])
    q25, q50, q75 = np.percentile(ln_a, [25, 50, 75])
    assert q50 == pytest.approx(s.ln_mu, abs=2e-3 * s.gamma + 1e-4)
    # Cauchy quartiles sit at +/- gamma.
    assert (q75 - q25) / 2 == pytest.approx(s.gamma, rel=0.02)


@pytest.mark.parametrize("disk", [
    {**DISK, "a_distribution": "gaussian"},
    {**DISK, "a_distribution": "lorentzian", "a_sigma": 2.0},
    {**DISK, "a_distribution": "lorentzian", "a_center": 100.0, "a_sigma": 0.0},
])
def test_bad_config_raises(disk):
    with pytest.raises(ValueError):
        SemimajorAxisSampler(disk)
