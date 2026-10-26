"""Offline resume selection/refresh planner; all scenario writes use temp dirs.

This models the written startup rules, not a live intake or package updater.
select_saved_profile(home, opened) only reads its inputs and returns a plan.
"""

from dataclasses import dataclass
import json
import os
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Optional, Tuple


PACKAGE_FILES = (
    "AGENTS.md", "README.md", "CLAUDE.md", "CLAUDE_PROMPT.md",
    "CURSOR_PROMPT.md", "CHATGPT_PROMPT.md", "START_PROMPT.md",
    "profile.template.json",
)
PACKAGE_DIRS = ("prompts", "reference", "test", ".cursor")


@dataclass(frozen=True)
class Selection:
    profile: Optional[Path]
    package: Optional[Path]
    # Relative file paths only. Back up old versions under
    # reports/package-backup-<timestamp>/ before applying; never apply here.
    refresh_plan: Tuple[Path, ...]


def children(folder):
    return sorted((p for p in folder.iterdir() if p.is_dir()),
                  key=lambda p: p.name) if folder.is_dir() else []


def is_package(folder):
    return all((folder / name).is_file()
               for name in ("AGENTS.md", "profile.template.json"))


def package_candidates(opened):
    if is_package(opened):
        return [opened]
    first = children(opened)
    return [p for p in first + [c for p in first for c in children(p)]
            if is_package(p)]


def has_answers(value, path=()):
    """Ignore metadata/approvals/dry_run; explicit false and zero are answers."""
    if isinstance(value, dict):
        return any(has_answers(v, path + (k,)) for k, v in value.items()
                   if not (not path and k in {"metadata", "approvals"})
                   and path + (k,) != ("intake", "dry_run"))
    if isinstance(value, list):
        return any(has_answers(v, path) for v in value)
    return value is not None and value != ""


def refresh_plan(package, saved):
    """Plan changed source files only; no deletion or directory replacement."""
    if package is None or saved is None:
        return ()
    paths = [Path(name) for name in PACKAGE_FILES]
    for name in PACKAGE_DIRS:
        paths.extend(p.relative_to(package) for p in (package / name).rglob("*")
                     if p.is_file())
    changes = []
    for relative in sorted(paths):
        if any(part in {"profile.json", "reports", "approvals.log"}
               for part in relative.parts):
            continue
        # Do not follow links in either package or saved-folder paths.
        if any((root / parent).is_symlink()
               for root in (package, saved)
               for parent in (relative, *relative.parents)):
            continue
        source, destination = package / relative, saved / relative
        if source.is_file() and (not destination.exists() or
                                 source.read_bytes() != destination.read_bytes()):
            changes.append(relative)
    return tuple(changes)


def select_saved_profile(home, opened):
    """Read-only selection: real before test, newest answers, search-order ties.

    Package choice is independent of saved-profile choice. No directories are
    created, no profile is overwritten, and no refresh is executed.
    """
    home, opened = Path(home), Path(opened)
    packages = package_candidates(opened)
    package = max(packages, key=lambda p: (
        "Resume check" in (p / "AGENTS.md").read_text(encoding="utf-8"),
        (p / "AGENTS.md").stat().st_mtime_ns,
    ), default=None)
    helpers = sorted(p for p in home.glob("RecruitingHelper*") if p.is_dir())
    candidates = [opened] + helpers + children(opened.parent)
    for root in (home / "Desktop", home / "Documents", home / "Documents/projects"):
        candidates.extend(p for p in children(root)
                          if "recruit" in p.name.lower() or
                          (p / "profile.template.json").is_file())
    # Descendant packages supplement, rather than replace, the earlier search.
    candidates.extend(packages)
    answered, seen = [], set()
    for folder in candidates:
        if folder in seen:
            continue
        seen.add(folder)
        profile = folder / "profile.json"
        marker = any((folder / name).is_file()
                     for name in ("AGENTS.md", "profile.template.json"))
        if not profile.is_file() or not (marker or folder in helpers):
            continue
        data = json.loads(profile.read_text(encoding="utf-8"))
        if has_answers(data):
            answered.append((profile, data))
    chosen = max(answered, key=lambda item: (
        item[1].get("intake", {}).get("dry_run") is False,
        item[0].stat().st_mtime_ns,
    ), default=None)
    profile = chosen[0] if chosen else None
    return Selection(profile, package,
                     refresh_plan(package, profile.parent if profile else None))


def write(folder, name, value, stamp=100):
    path = folder / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value) if isinstance(value, dict) else value,
                    encoding="utf-8")
    os.utime(path, (stamp, stamp))
    return path


def make_package(folder, *, current=False, stamp=100):
    write(folder, "AGENTS.md", "Resume check" if current else "Old intake rules", stamp)
    write(folder, "profile.template.json", {"athlete": {"first_name": ""}})
    write(folder, "README.md", "Current instructions" if current else "Old instructions")
    write(folder, "prompts/start.md", "Current prompt" if current else "Old prompt")


def snapshot(home):
    # Include all files and directories, bytes and mtimes: catches a new numbered
    # folder, refresh writes, deleted profiles, and even an unchanged rewrite.
    return {p.relative_to(home): (p.is_dir(), p.stat().st_mtime_ns,
                                 None if p.is_dir() else p.read_bytes())
            for p in home.rglob("*")}


def run_scenarios():
    with TemporaryDirectory(prefix="rq-resume-") as temporary:
        home = Path(temporary)
        opened = home / "Documents/projects"
        stale = opened / "recruiting-questionnaire-codex"
        blank = home / "RecruitingHelper"
        saved = home / "RecruitingHelper2"
        make_package(stale, stamp=900)
        make_package(saved, stamp=100)
        old_profile = write(stale, "profile.json", {
            "intake": {"dry_run": True}, "athlete": {"first_name": "Older Test"},
        }, 200)
        write(blank, "profile.json", {
            "metadata": {"updated_at": "synthetic"}, "approvals": {"approved": True},
            "intake": {"dry_run": True}, "athlete": {"first_name": ""},
        }, 999)
        saved_profile = write(saved, "profile.json", {
            "intake": {"dry_run": True}, "athlete": {"first_name": "Test Athlete"},
        }, 300)
        write(saved, "reports/approvals.log", "Keep original approval history")
        before = snapshot(home)
        result = select_saved_profile(home, opened)
        assert result.profile == saved_profile, "The newer dry-run profile must win"
        assert result.package == stale, "All-stale fallback must still resume"
        assert snapshot(home) == before, "Selection must never modify saved work"
        assert not (home / "RecruitingHelper3").exists()

        # A current package two levels down beats a newer stale AGENTS.md.
        current = opened / "worktrees/current-package"
        make_package(current, current=True, stamp=400)
        other = opened / "current-older"
        make_package(other, current=True, stamp=350)
        # Even if source packages contain private files, refresh excludes them.
        write(current, "profile.json", {"athlete": {"first_name": ""}}, 1000)
        write(current, "reports/approvals.log", "Do not copy")
        write(current, "test/profile.json", {"athlete": {"first_name": "Private"}})
        write(current, "test/reports/private.txt", "Do not copy")
        before = snapshot(home)
        result = select_saved_profile(home, opened)
        assert result.profile == saved_profile
        assert result.package == current, "Prefer Resume check, then newest AGENTS.md"
        assert {Path("AGENTS.md"), Path("README.md"), Path("prompts/start.md")} <= set(
            result.refresh_plan), "Changed package files need a refresh plan"
        assert all("profile.json" not in p.parts and "reports" not in p.parts
                   and "approvals.log" not in p.parts for p in result.refresh_plan)
        assert snapshot(home) == before, "A refresh plan must not execute writes"

        # Missing/stale markers never disqualify a saved RecruitingHelper folder.
        (saved / "AGENTS.md").unlink()
        (saved / "profile.template.json").unlink()
        assert select_saved_profile(home, opened).profile == saved_profile
        # Existing real-family precedence is retained, even over a newer test.
        write(stale, "profile.json", {"intake": {"dry_run": False},
                                       "athlete": {"first_name": "Test Real"}}, 200)
        assert select_saved_profile(home, opened).profile == old_profile
        # Equal profile mtimes use the documented search order (helpers first).
        write(stale, "profile.json", {"intake": {"dry_run": True},
                                       "athlete": {"first_name": "Older Test"}}, 300)
        assert select_saved_profile(home, opened).profile == saved_profile
        assert has_answers({"intake": {"dry_run": True}, "answer": False})
        assert has_answers({"answer": 0})
        assert not has_answers({"metadata": {"stamp": 1},
                                "approvals": {"approved": True},
                                "intake": {"dry_run": False}})
        for path in home.rglob("profile.json"):
            write(path.parent, path.name, {})
        before = snapshot(home)
        assert select_saved_profile(home, opened).profile is None
        assert snapshot(home) == before, "No answers must not create a new folder"
    print("PASS: offline stale-package resume scenarios; profiles preserved, safe refresh plan")


if __name__ == "__main__":
    run_scenarios()
