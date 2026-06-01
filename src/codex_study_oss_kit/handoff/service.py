from __future__ import annotations

from pathlib import Path

from .markdown import build_handoff_markdown


def write_handoff(
    root: Path,
    objective: str,
    current: str,
    done: str = "",
    pending: str = "",
    command: str = "",
    restriction: str = "",
    output: Path | None = None,
) -> Path:
    target = output or root / "thread-handoffs" / "latest.md"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(
        build_handoff_markdown(
            root=root,
            objective=objective,
            current=current,
            done=done,
            pending=pending,
            command=command,
            restriction=restriction,
        ),
        encoding="utf-8",
    )
    return target
