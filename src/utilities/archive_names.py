"""
archive_names.py

Guard against wrong or missing particle names in a REBOUND SimulationArchive.

The pipeline identifies every body by name only -- roles (star / GP / MP_* /
TP_*) in summary_figures.build_snapshot_table, the massive planetesimals in
the C_e diagnostic, and the bodies the Rayleigh cut excludes. REBOUND 5.0.0
stores names as C string pointers, and names read back from small hand-built
archives have been seen to come back wrong, duplicated or missing (without a
warning). The pipeline's own archives have all checked out, but nothing else
would notice if one did not, so every archive reader runs these checks:

  1. particle 0 is "star"; every other particle has a name, no name repeats
     within a snapshot, and each matches GP / MP_<n> / TP_<n>;
  2. in the first snapshot MP_ and TP_ are numbered 0, 1, 2, ... in order;
  3. every later snapshot's names are the first snapshot's names in the same
     order, with some possibly removed (escapes) -- never reordered or new;
  4. each name keeps its first-snapshot mass (skipped if collisions are on,
     since merging changes masses) -- a name moved onto another body shows up
     here whenever the masses differ.

Check archives by hand (exit status 1 if any fail):

    python src/utilities/archive_names.py outputs/*/*.bin
"""

import re
import sys

NAME_PATTERN = re.compile(r"^(GP|MP_\d+|TP_\d+)$")


class ArchiveNameError(ValueError):
    """A snapshot's particle names are missing, duplicated, malformed or inconsistent."""


class ArchiveNameChecker:
    """Check snapshots one at a time against the first snapshot passed in.

    Call ``check(sim, index)`` for each snapshot in order (the first call sets
    the reference). Raises ArchiveNameError on the first problem.
    """

    def __init__(self, source=""):
        self.source = f"{source}: " if source else ""
        self._ref_names = None
        self._ref_mass = None
        self._check_mass = True

    def _fail(self, sim, index, problem):
        raise ArchiveNameError(
            f"{self.source}snapshot {index} (t = {sim.t:.6g}): {problem}. "
            "Particle names in this archive cannot be trusted, so bodies would be "
            "misidentified; see src/utilities/archive_names.py."
        )

    def check(self, sim, index):
        names = [sim.particles[j].name for j in range(sim.N)]
        if not names or names[0] != "star":
            self._fail(sim, index, f"particle 0 is named {names[0] if names else None!r}, "
                                   "not 'star'")

        body = names[1:]
        missing = [j + 1 for j, n in enumerate(body) if not n]
        if missing:
            self._fail(sim, index, f"{len(missing)} particle(s) have no name "
                                   f"(first at index {missing[0]})")
        if len(set(body)) != len(body):
            seen, dups = set(), []
            for n in body:
                if n in seen:
                    dups.append(n)
                seen.add(n)
            self._fail(sim, index, f"duplicate name(s): {', '.join(sorted(set(dups))[:5])}")
        bad = [n for n in body if not NAME_PATTERN.match(n)]
        if bad:
            self._fail(sim, index, f"unexpected name(s): {', '.join(map(repr, bad[:5]))}")

        masses = [sim.particles[j].m for j in range(sim.N)]

        if self._ref_names is None:
            for prefix in ("MP_", "TP_"):
                numbers = [int(n[3:]) for n in body if n.startswith(prefix)]
                if numbers != list(range(len(numbers))):
                    self._fail(sim, index, f"{prefix}* are not numbered 0, 1, 2, ... in order")
            self._ref_names = names
            self._ref_mass = dict(zip(names, masses))
            self._check_mass = str(getattr(sim, "collision", "none")).lower() == "none"
            return

        remaining = iter(self._ref_names)
        if not all(any(n == ref for ref in remaining) for n in names):
            self._fail(sim, index, "names are not the first snapshot's names in the same "
                                   "order (reordered or new names)")
        if self._check_mass:
            changed = [n for n, m in zip(names, masses) if m != self._ref_mass[n]]
            if changed:
                self._fail(sim, index, f"{len(changed)} name(s) changed mass since the first "
                                       f"snapshot (e.g. {changed[0]}), i.e. moved to another body")


def check_archive_names(archive_path):
    """Check every snapshot of an archive; return the number checked or raise."""
    import rebound

    sa = rebound.Simulationarchive(str(archive_path))
    checker = ArchiveNameChecker(str(archive_path))
    for index in range(len(sa)):
        checker.check(sa[index], index)
    return len(sa)


def main(argv=None):
    paths = sys.argv[1:] if argv is None else argv
    if not paths:
        print("Usage: python src/utilities/archive_names.py <archive.bin> [...]")
        return 2
    failed = 0
    for path in paths:
        try:
            n = check_archive_names(path)
            print(f"OK   {path} ({n} snapshots)")
        except ArchiveNameError as error:
            failed += 1
            print(f"FAIL {error}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
