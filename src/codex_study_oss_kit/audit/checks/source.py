from __future__ import annotations

from pathlib import Path

from .common import has_any
from ..models import AuditCheck


def check_source_folder(root: Path) -> AuditCheck:
    return has_any(root, ["src", "source", "app"], "source folder", "source folder exists")
