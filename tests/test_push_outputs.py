"""Tests for src/launch/push_outputs.py (no SSH: subprocess.run is faked)."""

import yaml

import push_outputs

REMOTE = {"username": "u", "host": "h", "remote_dir": "/r/pipeline", "ssh_opts": []}


def _local(outputs, name, **meta):
    (outputs / name).mkdir(parents=True)
    if meta:
        (outputs / name / "run_metadata.yaml").write_text(yaml.safe_dump(meta))


def test_local_runs_reads_metadata(tmp_path):
    _local(tmp_path, "done", run_uuid="a", outcome="completed")
    _local(tmp_path, "live", run_uuid="b")
    _local(tmp_path, "legacy")
    runs = push_outputs.local_runs(tmp_path)
    assert runs["done"] == {"run_uuid": "a", "outcome": "completed", "has_metadata": True}
    assert runs["live"]["outcome"] is None and runs["live"]["has_metadata"]
    assert runs["legacy"]["has_metadata"] is False


def test_plan_decides_per_run():
    def info(uuid=None, outcome="completed", meta=True):
        return {"run_uuid": uuid, "outcome": outcome, "has_metadata": meta}

    local = {
        "new": info("n"),
        "same": info("s"),
        "other": info("o"),
        "live": info("l", outcome=None),
        "legacy_new": info(meta=False, outcome=None),
        "legacy_there": info(meta=False, outcome=None),
        "bad name": info("b"),
    }
    remote = {"same": "s", "other": "different", "legacy_there": None}
    actions = {n: a for n, (a, _) in push_outputs.plan(local, remote).items()}
    assert actions == {
        "new": "copy",
        "same": "update",
        "other": "conflict",        # a different run of that name: never touched
        "live": "running",
        "legacy_new": "copy",       # old run without metadata, not on the cluster
        "legacy_there": "exists",   # can't tell if it's the same run: not touched
        "bad name": "skip",
    }


def test_copy_never_deletes_and_never_prompts(tmp_path):
    cmd = push_outputs.build_copy_cmd(REMOTE, "run1", tmp_path)
    assert "--delete" not in cmd and not any(a.startswith("--remove") for a in cmd)
    assert "BatchMode=yes" in cmd[cmd.index("-e") + 1]
    assert cmd[-2:] == [f"{tmp_path}/run1/", "u@h:/r/pipeline/outputs/run1/"]


def test_verify_is_a_size_only_dry_run(tmp_path):
    cmd = push_outputs.build_verify_cmd(REMOTE, "run1", tmp_path)
    assert cmd[1] == "-rn" and "--size-only" in cmd and "--itemize-changes" in cmd


class _R:
    def __init__(self, rc=0, out="", err=""):
        self.returncode, self.stdout, self.stderr = rc, out, err


def _fake(monkeypatch, listing="", copy_rc=0, verify_out=""):
    monkeypatch.setattr(push_outputs.run_log, "known_remotes", lambda: {"barbieri": REMOTE})
    calls = []

    def run(cmd, **kw):
        calls.append(cmd)
        if cmd[0] == "ssh":
            return _R(out=listing)
        if "--itemize-changes" in cmd:
            return _R(out=verify_out)
        return _R(rc=copy_rc)

    monkeypatch.setattr(push_outputs.subprocess, "run", run)
    return calls


def test_push_copies_then_verifies(tmp_path, monkeypatch):
    _local(tmp_path, "done", run_uuid="a", outcome="completed")
    _local(tmp_path, "live", run_uuid="b")
    calls = _fake(monkeypatch)
    assert push_outputs.push(outputs_dir=tmp_path) == {"done": "verified", "live": "running"}
    assert [c[0] for c in calls] == ["ssh", "rsync", "rsync"]  # list, copy, verify


def test_push_flags_a_mismatch(tmp_path, monkeypatch):
    _local(tmp_path, "done", run_uuid="a", outcome="completed")
    _fake(monkeypatch, verify_out=">f.st...... done.bin\n")
    assert push_outputs.push(outputs_dir=tmp_path) == {"done": "MISMATCH"}


def test_failed_copy_is_not_verified(tmp_path, monkeypatch):
    _local(tmp_path, "done", run_uuid="a", outcome="completed")
    calls = _fake(monkeypatch, copy_rc=23)
    assert push_outputs.push(outputs_dir=tmp_path) == {"done": "copy failed"}
    assert len([c for c in calls if c[0] == "rsync"]) == 1


def test_dry_run_copies_nothing(tmp_path, monkeypatch):
    _local(tmp_path, "done", run_uuid="a", outcome="completed")
    calls = _fake(monkeypatch)
    assert push_outputs.push(outputs_dir=tmp_path, dry_run=True) == {"done": "would copy"}
    assert not [c for c in calls if c[0] == "rsync"]
