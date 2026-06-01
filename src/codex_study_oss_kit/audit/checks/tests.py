from __future__ import annotations

from pathlib import Path

from .common import has_any
from ..models import AuditCheck


def check_tests_folder(root: Path) -> AuditCheck:
    return has_any(root, ["tests", "test"], "tests", "test folder exists")
