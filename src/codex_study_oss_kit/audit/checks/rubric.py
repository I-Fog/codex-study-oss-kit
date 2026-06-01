from __future__ import annotations

from pathlib import Path

from .common import has_any
from ..models import AuditCheck


def check_rubric(root: Path) -> AuditCheck:
    return has_any(root, ["rubrica.md", "rubric.md", "review.md"], "rubric", "review criteria exist")
