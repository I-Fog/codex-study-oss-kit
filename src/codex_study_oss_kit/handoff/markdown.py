from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

from .models import Handoff


def build_handoff_markdown(
    root: Path,
    objective: str,
    current: str,
    done: str = "",
    pending: str = "",
    command: str = "",
    restriction: str = "",
) -> str:
    return render_handoff_markdown(
        Handoff(
            root=root,
            objective=objective,
            current=current,
            done=done,
            pending=pending,
            command=command,
            restriction=restriction,
        )
    )


def render_handoff_markdown(handoff: Handoff) -> str:
    timestamp = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    sections = [
        ("Objective", handoff.objective),
        ("Repository", str(handoff.root)),
        ("Current", handoff.current),
        ("Done", handoff.done or "Not recorded."),
        ("Pending", handoff.pending or "Not recorded."),
        ("Command", handoff.command or "Not recorded."),
        ("Restriction", handoff.restriction or "Not recorded."),
    ]
    lines = ["# Codex Study Handoff", "", f"Generated: {timestamp}", ""]
    for title, value in sections:
        lines.extend([f"## {title}", "", value.strip(), ""])
    return "\n".join(lines)
