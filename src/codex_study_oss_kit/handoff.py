from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path


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


def build_handoff_markdown(
    root: Path,
    objective: str,
    current: str,
    done: str = "",
    pending: str = "",
    command: str = "",
    restriction: str = "",
) -> str:
    timestamp = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    sections = [
        ("Objective", objective),
        ("Repository", str(root)),
        ("Current", current),
        ("Done", done or "Not recorded."),
        ("Pending", pending or "Not recorded."),
        ("Command", command or "Not recorded."),
        ("Restriction", restriction or "Not recorded."),
    ]
    lines = ["# Codex Study Handoff", "", f"Generated: {timestamp}", ""]
    for title, value in sections:
        lines.extend([f"## {title}", "", value.strip(), ""])
    return "\n".join(lines)
