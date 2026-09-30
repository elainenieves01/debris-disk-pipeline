"""
rayleigh_cut.py

Outlier cut on a sample of massive-planetesimal eccentricities, shared by the
C_e diagnostic (src/simulation/run_simulation.py) and the cut RMS(e) figure
(src/plotting/summary_figures.py) so both always drop the same bodies.

A self-stirred swarm has Rayleigh-distributed eccentricities (Ida & Makino
1992). The Rayleigh width is estimated robustly from the median,
sigma = median(e) / sqrt(2 ln 2), and bodies with e > nsigma * sigma are
flagged. nsigma defaults to RAYLEIGH_CUT_NSIGMA = 5; a run can set it with
``rayleigh_cut: {nsigma: ...}`` in its config (``cut_nsigma_from_config``).
With N = 800 the expected largest value is ~3.7 sigma, so 5 sigma only catches bodies scattered by a single strong encounter (e.g. an
initially Hill-overlapping pair), not the stirred bulk.

The cut only makes sense once the disk has actually been stirred. Initial
eccentricities are drawn uniformly from [emin, emax] (a few 1e-5), so the cut
is applied only when median(e) >= STIRRED_MEDIAN_FACTOR * emax; otherwise (e.g.
a near-massless control run, or a short smoke test) no body is excluded.

A KS test of the kept eccentricities against a Rayleigh distribution is
reported as a diagnostic, with a warning below RAYLEIGH_KS_WARN_P, but it does
not switch the cut on or off: with a mass spectrum, dynamical friction makes
the bulk only approximately Rayleigh and p drifts around ~0.01-0.5 from one
snapshot to the next.
"""

import numpy as np
from scipy import stats

RAYLEIGH_CUT_NSIGMA = 5.0
STIRRED_MEDIAN_FACTOR = 30.0
RAYLEIGH_KS_WARN_P = 0.05


def cut_nsigma_from_config(config):
    """The cut factor for a run: ``rayleigh_cut.nsigma`` in its config, else the default."""
    section = (config or {}).get("rayleigh_cut") or {}
    return float(section.get("nsigma", RAYLEIGH_CUT_NSIGMA))


def rayleigh_outlier_cut(ecc, e_initial_max, nsigma=RAYLEIGH_CUT_NSIGMA):
    """Apply the Rayleigh outlier cut to an array of eccentricities.

    ``e_initial_max`` is the upper end of the initial eccentricity draw
    (``config["disk"]["emax"]``), used to decide whether the disk is stirred.
    Bodies with e > ``nsigma`` * sigma are cut.

    Returns a dict with ``keep`` (boolean mask, all True if the cut is not
    applied), ``applied`` (= disk stirred), ``median_e``, ``stirred_threshold``,
    ``sigma``, ``e_cut``, and ``ks_D`` / ``ks_p`` / ``ks_warning`` (KS test of
    the kept values against a Rayleigh of their own MLE width).
    """
    ecc = np.asarray(ecc, dtype=float)
    median_e = float(np.median(ecc))
    stirred_threshold = STIRRED_MEDIAN_FACTOR * float(e_initial_max)
    applied = bool(median_e >= stirred_threshold)

    sigma = median_e / np.sqrt(2.0 * np.log(2.0))
    e_cut = float(nsigma) * sigma
    keep = ecc <= e_cut if applied else np.ones(ecc.shape, dtype=bool)

    rms_kept = np.sqrt(np.mean(ecc[keep] ** 2))
    ks = stats.kstest(ecc[keep], "rayleigh", args=(0.0, rms_kept / np.sqrt(2.0)))

    return {
        "keep": keep,
        "applied": applied,
        "median_e": median_e,
        "stirred_threshold": stirred_threshold,
        "sigma": float(sigma),
        "e_cut": float(e_cut),
        "ks_D": float(ks.statistic),
        "ks_p": float(ks.pvalue),
        "ks_warning": bool(ks.pvalue < RAYLEIGH_KS_WARN_P),
    }
