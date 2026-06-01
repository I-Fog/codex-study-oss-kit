from __future__ import annotations

from pathlib import Path

from .common import exists
from ..models import AuditCheck


def check_agents(root: Path) -> AuditCheck:
    return exists(root, "AGENTS.md", "agent instructions are present")
