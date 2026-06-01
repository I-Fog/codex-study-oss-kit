from __future__ import annotations

from pathlib import Path

from ..models import AuditCheck


def exists(root: Path, relative_name: str, detail: str) -> AuditCheck:
    path = root / relative_name
    return AuditCheck(relative_name, path.exists(), detail if path.exists() else "file not found")


def has_any(root: Path, names: list[str], label: str, detail: str) -> AuditCheck:
    found = [name for name in names if (root / name).exists()]
    return AuditCheck(label, bool(found), detail if found else f"none of {', '.join(names)} found")
