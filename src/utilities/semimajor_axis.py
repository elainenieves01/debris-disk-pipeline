"""Initial semimajor-axis distributions for disk bodies.

``disk.a_distribution`` selects the shape (default ``uniform``):

- ``uniform``: a ~ U(amin, amax).
- ``lorentzian``: ln a follows a Lorentzian (Cauchy) profile, truncated to
  [amin, amax]. With mu_0 = ``disk.a_center`` (disk center, AU) and
  sigma = ``disk.a_sigma`` (disk standard deviation, AU), the peak sits at

      ln mu = ln( mu_0**2 / sqrt(mu_0**2 + sigma**2) )

  and the half-width at half-maximum in ln a is

      gamma = sqrt( ln(1 + sigma**2 / mu_0**2) ),

  i.e. the log-space location and width a lognormal with mean mu_0 and
  standard deviation sigma would have.

Every draw consumes exactly one ``rng.uniform`` call (the Lorentzian uses
the truncated inverse CDF), so the per-body draw order a, e, inc, omega,
Omega, M is the same for every distribution.
"""

import numpy as np

A_DISTRIBUTIONS = ("uniform", "lorentzian")


def lorentzian_log_params(mu_0, sigma):
    """(ln mu, gamma) of the log-space Lorentzian for disk center/std mu_0, sigma."""
    mu_0, sigma = float(mu_0), float(sigma)
    if mu_0 <= 0 or sigma <= 0:
        raise ValueError(f"a_center and a_sigma must be > 0, got {mu_0}, {sigma}")
    ln_mu = np.log(mu_0**2 / np.sqrt(mu_0**2 + sigma**2))
    gamma = np.sqrt(np.log1p(sigma**2 / mu_0**2))
    return ln_mu, gamma


class SemimajorAxisSampler:
    """Draws initial semimajor axes (AU) according to a config ``disk`` block."""

    def __init__(self, disk):
        self.amin = float(disk["amin"])
        self.amax = float(disk["amax"])
        self.kind = disk.get("a_distribution", "uniform")
        if self.kind not in A_DISTRIBUTIONS:
            raise ValueError(
                f"disk.a_distribution must be one of {A_DISTRIBUTIONS}, got {self.kind!r}"
            )
        if self.kind == "lorentzian":
            for key in ("a_center", "a_sigma"):
                if disk.get(key) is None:
                    raise ValueError(f"disk.a_distribution 'lorentzian' requires disk.{key}")
            self.mu_0 = float(disk["a_center"])
            self.sigma = float(disk["a_sigma"])
            self.ln_mu, self.gamma = lorentzian_log_params(self.mu_0, self.sigma)
            # Inverse-CDF angles of the truncation bounds in ln a.
            self._theta_lo = np.arctan((np.log(self.amin) - self.ln_mu) / self.gamma)
            self._theta_hi = np.arctan((np.log(self.amax) - self.ln_mu) / self.gamma)

    @property
    def peak(self):
        """Peak semimajor axis mu (AU); None for uniform."""
        return float(np.exp(self.ln_mu)) if self.kind == "lorentzian" else None

    def draw(self, rng):
        if self.kind == "uniform":
            return rng.uniform(self.amin, self.amax)
        theta = rng.uniform(self._theta_lo, self._theta_hi)
        return float(np.exp(self.ln_mu + self.gamma * np.tan(theta)))

    def describe(self):
        if self.kind == "uniform":
            return f"uniform in [{self.amin:g}, {self.amax:g}] AU"
        return (
            f"Lorentzian in ln a, mu_0 = {self.mu_0:g} AU, sigma = {self.sigma:g} AU "
            f"-> peak mu = {self.peak:.6g} AU, HWHM(ln a) = {self.gamma:.4g}, "
            f"truncated to [{self.amin:g}, {self.amax:g}] AU"
        )
