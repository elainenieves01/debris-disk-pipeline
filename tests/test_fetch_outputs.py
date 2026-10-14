"""Tests for src/launch/fetch_outputs.py (no SSH: subprocess.run is faked)."""

import yaml

import fetch_outputs

REMOTE = {"username": "u", "host": "h", "remote_dir": "/r/pipeline", "ssh_opts": []}


def _write_local(outputs, name, bin_bytes=None, **meta):
    (outputs / name).mkdir(parents=True)
    (outputs / name / "run_metadata.yaml").write_text(yaml.safe_dump(meta))
    if bin_bytes is not None:
        (outputs / name / f"{name}.bin").write_bytes(b"x" * bin_bytes)


def _remote(bin_size=100, **meta):
    return {"metadata": meta, "bin_size": bin_size}


def test_plan_decides_per_run(tmp_path):
    _write_local(tmp_path, "have_it", bin_bytes=100, run_uuid="a", outcome="completed")
    _write_local(tmp_path, "other_run", bin_bytes=100, run_uuid="old", outcome="completed")
    _write_local(tmp_path, "copied_early", run_uuid="c")
    _write_local(tmp_path, "metadata_only", run_uuid="m", outcome="completed")
    _write_local(tmp_path, "half_copied", bin_bytes=40, run_uuid="h", outcome="completed")
    _write_local(tmp_path, "no_archive", run_uuid="z", outcome="failed")
    runs = {
        "new_run": _remote(run_uuid="n", outcome="completed"),
        "have_it": _remote(run_uuid="a", outcome="completed"),
        "other_run": _remote(run_uuid="new", outcome="completed"),
        "copied_early": _remote(run_uuid="c", outcome="failed"),
        "metadata_only": _remote(run_uuid="m", outcome="completed"),
        "half_copied": _remote(run_uuid="h", outcome="completed"),
        "no_archive": _remote(bin_size=None, run_uuid="z", outcome="failed"),
        "still_going": _remote(run_uuid="s"),
        "bad name": _remote(run_uuid="b", outcome="completed"),
    }
    actions = {name: action for name, (action, _) in fetch_outputs.plan(runs, tmp_path).items()}
    assert actions == {
        "new_run": "fetch",
        "have_it": "have",
        "other_run": "conflict",       # never clobber a different run of the same name
        "copied_early": "fetch",
        "metadata_only": "fetch",      # git-tracked metadata, but no .bin here
        "half_copied": "fetch",        # .bin smaller than the remote one
        "no_archive": "have",          # nothing more to copy
        "still_going": "running",
        "bad name": "skip",
    }


def test_listing_parses_metadata_and_archive_size():
    text = ("=== run_a\nrun_uuid: a\noutcome: completed\n--- binsize\n8212594\n"
            "=== run_b\nrun_uuid: b\n--- binsize\nnone\n"
            "=== broken\n--- binsize\n12\n")
    runs = fetch_outputs._parse_listing(text)
    assert runs == {
        "run_a": {"metadata": {"run_uuid": "a", "outcome": "completed"}, "bin_size": 8212594},
        "run_b": {"metadata": {"run_uuid": "b"}, "bin_size": None},
    }


def test_copy_order_and_local_files_are_never_replaced(tmp_path):
    rest, archive, metadata = fetch_outputs.build_rsync_cmds(REMOTE, "run1", tmp_path)
    src = "u@h:/r/pipeline/outputs/run1/"
    dest = f"{tmp_path}/run1/"
    # 1. reports/figures: never replace a local file (they get revised locally)
    assert "--ignore-existing" in rest
    assert rest[-6:] == ["--exclude", "run_metadata.yaml", "--exclude", "run1.bin", src, dest]
    # 2. the archive is always brought up to date; 3. metadata last
    assert "--ignore-existing" not in archive and archive[-2:] == [src + "run1.bin", dest]
    assert "--ignore-existing" not in metadata
    assert metadata[-2:] == [src + "run_metadata.yaml", dest]
    for cmd in (rest, archive, metadata):
        assert "BatchMode=yes" in cmd[cmd.index("-e") + 1]  # never prompts


def test_run_without_an_archive_skips_that_copy(tmp_path):
    cmds = fetch_outputs.build_rsync_cmds(REMOTE, "run1", tmp_path, has_archive=False)
    assert len(cmds) == 2 and not any(c[-2].endswith(".bin") for c in cmds)


class _Result:
    def __init__(self, returncode=0, stdout="", stderr=""):
        self.returncode, self.stdout, self.stderr = returncode, stdout, stderr


def _fake_remote(monkeypatch, listing, rsync_rc=0):
    monkeypatch.setattr(fetch_outputs.run_log, "known_remotes", lambda: {"barbieri": REMOTE})
    calls = []

    def run(cmd, **kw):
        calls.append(cmd)
        if cmd[0] == "ssh":
            return _Result(stdout=listing)
        return _Result(returncode=rsync_rc)

    monkeypatch.setattr(fetch_outputs.subprocess, "run", run)
    return calls


LISTING = (
    "=== done_run\nrun_uuid: d\noutcome: completed\n--- binsize\n100\n"
    "=== live_run\nrun_uuid: l\ncreated: '2026-10-07T00:00:00+00:00'\n--- binsize\n50\n"
)


def test_fetch_copies_only_finished_runs(tmp_path, monkeypatch):
    calls = _fake_remote(monkeypatch, LISTING)
    assert fetch_outputs.fetch(outputs_dir=tmp_path) == ["done_run"]
    rsyncs = [c for c in calls if c[0] == "rsync"]
    assert len(rsyncs) == 3 and all("done_run" in c[-2] for c in rsyncs)


def test_dry_run_copies_nothing(tmp_path, monkeypatch):
    calls = _fake_remote(monkeypatch, LISTING)
    assert fetch_outputs.fetch(outputs_dir=tmp_path, dry_run=True) == []
    assert not [c for c in calls if c[0] == "rsync"]


def test_failed_copy_skips_metadata_so_it_retries(tmp_path, monkeypatch):
    calls = _fake_remote(monkeypatch, LISTING, rsync_rc=23)
    assert fetch_outputs.fetch(outputs_dir=tmp_path) == []
    assert len([c for c in calls if c[0] == "rsync"]) == 1  # metadata copy never ran
