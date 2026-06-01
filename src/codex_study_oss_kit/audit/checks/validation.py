from __future__ import annotations

from pathlib import Path

from ..models import AuditCheck


VALIDATION_KEYWORDS = ["test", "pytest", "unittest", "npm test", "cargo test", "validacion", "validation"]


def check_validation_command(root: Path) -> AuditCheck:
    readme = root / "README.md"
    if not readme.exists():
        return AuditCheck("validation command", False, "README.md not found")

    text = readme.read_text(encoding="utf-8", errors="ignore").lower()
    ok = any(keyword in text for keyword in VALIDATION_KEYWORDS)
    detail = "README mentions how to validate changes" if ok else "README has no validation command"
    return AuditCheck("validation command", ok, detail)
