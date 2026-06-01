from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class AuditCheck:
    name: str
    ok: bool
    detail: str


@dataclass(frozen=True)
class AuditReport:
    root: Path
    checks: list[AuditCheck]

    @property
    def score(self) -> int:
        return sum(1 for check in self.checks if check.ok)

    @property
    def total(self) -> int:
        return len(self.checks)

    @property
    def ok(self) -> bool:
        return self.score == self.total

    def to_markdown(self) -> str:
        lines = [
            f"# Agent-readiness audit: {self.root}",
            "",
            f"Score: {self.score}/{self.total}",
            "",
        ]
        for check in self.checks:
            marker = "OK" if check.ok else "MISSING"
            lines.append(f"- [{marker}] {check.name}: {check.detail}")
        lines.append("")
        return "\n".join(lines)
