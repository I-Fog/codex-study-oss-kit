from __future__ import annotations

from pathlib import Path

from .checks import DEFAULT_CHECKS
from .models import AuditReport


def audit_project(root: Path) -> AuditReport:
    checks = [check(root) for check in DEFAULT_CHECKS]
    return AuditReport(root=root, checks=checks)
