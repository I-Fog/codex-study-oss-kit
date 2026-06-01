from __future__ import annotations

from pathlib import Path

from .common import exists
from ..models import AuditCheck


def check_readme(root: Path) -> AuditCheck:
    return exists(root, "README.md", "project context is documented")
