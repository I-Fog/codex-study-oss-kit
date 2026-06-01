from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Handoff:
    root: Path
    objective: str
    current: str
    done: str = ""
    pending: str = ""
    command: str = ""
    restriction: str = ""
