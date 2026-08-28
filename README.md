# debris-disk-pipeline

## Running a simulation

```bash
python src/simulation/run_simulation.py config/<your_config>.yaml
```

Console output is also embedded in the run report at
`outputs/<name>/<name>_report.md`, so the full log is recoverable after the run
even if you didn't capture the terminal.

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
