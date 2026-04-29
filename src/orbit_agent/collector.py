"""Workspace inspection helpers."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


IGNORED_DIRS = {
    ".git",
    ".hg",
    ".svn",
    "__pycache__",
    ".venv",
    "node_modules",
    "dist",
    "build",
    "out",
    "target",
}

TEXT_EXTENSIONS = {
    ".py",
    ".md",
    ".txt",
    ".toml",
    ".json",
    ".yaml",
    ".yml",
    ".js",
    ".ts",
    ".tsx",
    ".jsx",
    ".sh",
    ".bat",
    ".ps1",
}


@dataclass(frozen=True)
class FileSignal:
    path: Path
    score: int
    size: int


@dataclass(frozen=True)
class WorkspaceContext:
    root: Path
    files: list[FileSignal]
    sample_contents: dict[Path, str]
    todo_count: int


def _score_path(path: Path) -> int:
    name = path.name.lower()
    score = 0
    if name in {"readme.md", "readme.txt"}:
        score += 100
    if name in {"pyproject.toml", "package.json", "requirements.txt"}:
        score += 80
    if name.startswith(("main", "app", "index", "cli")):
        score += 60
    if path.suffix.lower() in TEXT_EXTENSIONS:
        score += 20
    if "demo" in name or "sample" in name:
        score += 15
    return score


def _is_ignored(path: Path) -> bool:
    return any(part in IGNORED_DIRS for part in path.parts)


def collect_workspace_context(root: Path, max_files: int = 8, max_chars: int = 1800) -> WorkspaceContext:
    """Inspect a workspace and capture the most useful evidence."""

    root = root.resolve()
    signals: list[FileSignal] = []
    samples: dict[Path, str] = {}
    todo_count = 0

    for path in root.rglob("*"):
        if not path.is_file() or _is_ignored(path):
            continue
        try:
            size = path.stat().st_size
        except OSError:
            continue
        signal = FileSignal(path=path, score=_score_path(path), size=size)
        signals.append(signal)

    signals.sort(key=lambda item: (-item.score, item.size, str(item.path).lower()))
    selected = signals[:max_files]

    for signal in selected:
        try:
            if signal.path.suffix.lower() not in TEXT_EXTENSIONS:
                samples[signal.path] = f"[binary or unsupported file type: {signal.path.suffix or 'no extension'}]"
                continue
            content = signal.path.read_text(encoding="utf-8", errors="replace")
            samples[signal.path] = content[:max_chars].strip()
            todo_count += content.lower().count("todo")
            todo_count += content.lower().count("fixme")
        except OSError:
            samples[signal.path] = "[unreadable file]"

    return WorkspaceContext(root=root, files=selected, sample_contents=samples, todo_count=todo_count)

