from __future__ import annotations

import json

from ..models import AuditReport


def format_json(report: AuditReport) -> str:
    return json.dumps(report.to_dict(), ensure_ascii=False, indent=2) + "\n"
