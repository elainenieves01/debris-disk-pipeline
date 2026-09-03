# debris-disk-pipeline

## Development setup

After cloning, enable the repo's git hooks once:

```bash
git config core.hooksPath .githooks
```

This installs `prepare-commit-msg`, which appends a `Claude-Session:` link to
any commit made from inside a Claude Code session. List them later with:

```bash
git log --format='%h %s%n  %(trailers:key=Claude-Session,valueonly)'
```

## Running a simulation

```bash
python src/simulation/run_simulation.py config/<your_config>.yaml
```

Console output is also embedded in the run report at
`outputs/<name>/<name>_report.md`, so the full log is recoverable after the run
even if you didn't capture the terminal.

## Run provenance

Every run writes a self-contained record into `outputs/<name>/` so that months
later you can tie any figure back to exactly what produced it:

| File | Contents |
|---|---|
| `config.yaml` | Verbatim frozen copy of the YAML used (comments preserved). Edit the original `config/…` file freely afterwards — this copy is the truth for the run. |
| `run_metadata.yaml` | Run UUID, timestamps, wall runtime, outcome, the exact command, git commit + branch + **dirty flag**, and key package versions. |
| `environment.txt` | Full `pip freeze` of the environment the run used. |

Every generated figure carries a one-line footer:

```
run <name> · uuid 8c5c4d2a · git a83f21c (DIRTY) · 2026-08-28
```

`(DIRTY)` means there were uncommitted changes to tracked files when the run
started — the committed code at that hash is **not** exactly what ran. Recover
the code state with `git checkout <commit>` (clean runs only).

Turn the figure footer off for a specific run (e.g. paper figures) with:

```yaml
plots:
  enabled: true
  provenance_stamp: false   # default: true
```

`run_metadata.yaml`, `config.yaml`, and `environment.txt` are always written
regardless of this toggle.

## Running long simulations

A process started from an interactive shell (including anything launched inside a
Claude Code session) is killed when that shell/session closes. Detach it so the
run survives:

```bash
tmux new -s ss_run
python src/simulation/run_simulation.py config/SS_1000MP_100Myr_.yaml
# detach with Ctrl-b d ; reattach later with: tmux attach -t ss_run
```

### Completion / failure notifications

`run_simulation.py` can POST a status line to an [ntfy.sh](https://ntfy.sh)
topic when the run finishes or raises. Add an optional top-level section to the
config:

```yaml
notify:
  enabled: true
  ntfy_topic: "https://ntfy.sh/elaine-hd216435-run"
```

It fires on success (with runtime, particle count, archive path) and on an
unhandled exception (with the exception type and message); the traceback still
prints to the terminal. Omit the section or set `enabled: false` to disable it.
A failed notification only prints a warning — it never breaks the run.

## Planetesimal masses

Under `massive_planetesimals`, set **exactly one** of:

| Key | Meaning |
|---|---|
| `total_disk_mass_earth` | Total disk mass in Earth masses; each of `N` planetesimals gets `value / N`. |
| `individual_MP_mass_plutos` | Mass of a single planetesimal in Pluto masses; total disk mass is `value * N`. |
| `mass_fraction_of_giant_planet` | (legacy) Each planetesimal has mass `value * M_giant_planet`; requires a giant planet. |

`total_mass_earth` still works as a deprecated alias of `total_disk_mass_earth`.
Setting more than one key (or none) is an error. The console output names which
mode was used.

### Power-law mass spectrum

By default the chosen mass key gives every planetesimal the identical mass. Add
an optional `distribution` block to draw the `N` masses from a truncated power
law (a Dohnanyi collisional cascade) instead. It has two named `mode`s:

| `mode` | Anchor | Needs a sibling mass key? | Disk mass |
|---|---|---|---|
| `total_mass` (default) | `total_disk_mass_earth` | yes — `total_disk_mass_earth` | fixed (sample rescaled to sum to it) |
| `size_range` | the literal `[min, max]` | no (must have none) | computed from the `N` bodies |

```yaml
# mode: total_mass  —  power-law split of a fixed disk mass
massive_planetesimals:
  N: 800
  total_disk_mass_earth: 0.28
  distribution:
    type: power_law
    mode: total_mass
    variable: radius        # radius | mass
    min: 1
    max: 100
    unit: km                # km for radius, earth_mass for mass
    slope: 3.5              # dN/dvariable ∝ variable^-slope  (Dohnanyi: 3.5 in size, 11/6 in mass)
    seed: 42               # optional

# mode: size_range  —  literal size limits, disk mass falls out
massive_planetesimals:
  N: 800
  distribution:
    type: power_law
    mode: size_range
    variable: radius
    min: 1
    max: 100
    unit: km
    slope: 3.5
    seed: 42
```

In `total_mass`, `slope` and the `[min, max]` *ratio* set the spectrum shape
while the absolute scale stays `total_disk_mass_earth / N`, so realized body
radii differ from `min`/`max`. In `size_range`, `min`/`max` are the actual radius
(or mass) limits and the total disk mass is whatever the bodies sum to (printed
in the run output and report).

Either way the run writes the sampled input spectrum to
`outputs/<name>/distribution.csv` and
`outputs/<name>/figures/dohnanyi_{per_particle,differential_histogram}.png`.
See `config/Sim_100MP_100thouyr_dohnanyi.yaml` and
`config/Sim_100MP_100thouyr_dohnanyi_sizes.yaml`.

### Standalone distribution tool

`src/mass_models/make_distribution.py` runs the same sampler outside a
simulation, for exploring a spectrum and its plots:

```bash
python src/mass_models/make_distribution.py \
    --n 800 --slope 1.8333 --mass-min 1e-6 --mass-max 1e-2 \
    --total-disk-mass-earth 2.8 --seed 42 --outdir outputs/dohnanyi_demo
```

Writes `<outdir>/distribution.csv` plus the same two figures.
`--total-disk-mass-earth 0` disables the rescale; `--variable radius` samples a
size spectrum (`--size-min` / `--size-max` in km).

### Slope sweep

`src/mass_models/plot_slope_sweep.py` draws 1000 planetesimals for each slope
`q` in `{0, 0.5, 1.0, ..., 5.0}` and plots number-per-mass-bin, showing how the
spectrum tilts from mass-dominated (`q < 1`) to number-dominated (`q > 1`):

```bash
python src/mass_models/plot_slope_sweep.py
```

Writes `src/mass_models/mass_distribution_slope_sweep{,_grid}.png` plus one
standalone figure per slope (`mass_distribution_slope_q<q>.png`).
