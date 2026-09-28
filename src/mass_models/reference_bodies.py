"""
Solar System reference bodies for annotating mass / radius axes.

``add_mass_references(ax, axis="y")`` and ``add_radius_references(ax, axis="x")``
draw a faint dashed line + label for every reference body that falls on (or
just past) the current axis range, so a planetesimal's mass or size can be read
against familiar objects. Call them after the data is plotted and the axis scale
is set, so the autoscaled limits are known.

Masses are in Earth masses, radii are volumetric mean radii in km (NASA planetary
fact sheets; Arrokoth mass from its New Horizons density estimate, ~7.5e14 kg).
"""

import matplotlib.transforms as mtransforms

# name: (mass [M_earth], mean radius [km])
REFERENCE_BODIES = {
    "Jupiter": (317.83, 69911.0),
    "Neptune": (17.147, 24622.0),
    "Earth": (1.0, 6371.0),
    "Mars": (0.10745, 3389.5),
    "Mercury": (0.05527, 2439.7),
    "Moon": (0.012300, 1737.4),
    "Pluto": (0.002187, 1188.3),
    "Ceres": (1.574e-4, 469.7),
    "Vesta": (4.34e-5, 262.7),
    "Phoebe": (1.388e-6, 106.5),
    "Ida": (7.03e-9, 15.7),
    "Phobos": (1.785e-9, 11.1),
    "Arrokoth": (1.26e-10, 9.0),
}

# A body up to this factor beyond the data range is still drawn (and the axis
# stretched to include it), so there is always a nearby reference in view.
DEFAULT_PAD_FACTOR = 2.0

_LINE_KW = dict(color="0.35", lw=0.8, ls="--", alpha=0.6, zorder=2.5)
_TEXT_KW = dict(color="0.25", zorder=6,
                bbox=dict(boxstyle="round,pad=0.15", fc="white", ec="none", alpha=0.75))


def _add_references(ax, values, axis, pad_factor, label_pos, fontsize):
    lo, hi = ax.get_ylim() if axis == "y" else ax.get_xlim()
    lo, hi = min(lo, hi), max(lo, hi)
    shown = {name: v for name, v in values.items()
             if lo / pad_factor <= v <= hi * pad_factor}
    if not shown:
        return []

    new_lo = min(lo, min(shown.values()) / 1.15)
    new_hi = max(hi, max(shown.values()) * 1.15)

    text_kw = dict(_TEXT_KW, fontsize=fontsize)
    artists = []
    for name, v in shown.items():
        if axis == "y":
            artists.append(ax.axhline(v, **_LINE_KW))
            trans = mtransforms.blended_transform_factory(ax.transAxes, ax.transData)
            artists.append(ax.text(label_pos, v, name, transform=trans,
                                   ha="right", va="center", **text_kw))
        else:
            artists.append(ax.axvline(v, **_LINE_KW))
            trans = mtransforms.blended_transform_factory(ax.transData, ax.transAxes)
            artists.append(ax.text(v, label_pos, name, transform=trans,
                                   ha="center", va="top", rotation=90, **text_kw))

    if axis == "y":
        ax.set_ylim(new_lo, new_hi)
    else:
        ax.set_xlim(new_lo, new_hi)
    return artists


def add_mass_references(ax, axis="y", pad_factor=DEFAULT_PAD_FACTOR, label_pos=0.99,
                        bodies=None, fontsize=7):
    """Mark reference-body masses (Earth masses) on a log mass axis."""
    names = bodies or REFERENCE_BODIES
    values = {n: REFERENCE_BODIES[n][0] for n in names}
    return _add_references(ax, values, axis, pad_factor, label_pos, fontsize)


def add_radius_references(ax, axis="x", pad_factor=DEFAULT_PAD_FACTOR, label_pos=0.99,
                          bodies=None, fontsize=7):
    """Mark reference-body radii (km) on a log radius axis."""
    names = bodies or REFERENCE_BODIES
    values = {n: REFERENCE_BODIES[n][1] for n in names}
    return _add_references(ax, values, axis, pad_factor, label_pos, fontsize)

