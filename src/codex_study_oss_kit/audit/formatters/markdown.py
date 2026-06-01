from __future__ import annotations

from ..models import AuditReport


def format_markdown(report: AuditReport) -> str:
    return report.to_markdown()
