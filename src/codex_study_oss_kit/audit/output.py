from __future__ import annotations

from pathlib import Path

from .formatters import FORMATTERS
from .models import AuditReport


def render_audit_report(report: AuditReport, output_format: str) -> str:
    formatter = FORMATTERS[output_format]
    return formatter(report)


def write_audit_report(content: str, output: Path) -> Path:
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(content, encoding="utf-8")
    return output
