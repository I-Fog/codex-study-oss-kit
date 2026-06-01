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


def audit_project(root: Path) -> AuditReport:
    checks = [
        _exists(root, "AGENTS.md", "agent instructions are present"),
        _exists(root, "README.md", "project context is documented"),
        _has_any(root, ["tests", "test"], "tests", "test folder exists"),
        _has_any(root, ["rubrica.md", "rubric.md", "review.md"], "rubric", "review criteria exist"),
        _has_any(root, ["src", "source", "app"], "source folder", "source folder exists"),
        _readme_mentions_validation(root),
    ]
    return AuditReport(root=root, checks=checks)


def _exists(root: Path, relative_name: str, detail: str) -> AuditCheck:
    path = root / relative_name
    return AuditCheck(relative_name, path.exists(), detail if path.exists() else "file not found")


def _has_any(root: Path, names: list[str], label: str, detail: str) -> AuditCheck:
    found = [name for name in names if (root / name).exists()]
    return AuditCheck(label, bool(found), detail if found else f"none of {', '.join(names)} found")


def _readme_mentions_validation(root: Path) -> AuditCheck:
    readme = root / "README.md"
    if not readme.exists():
        return AuditCheck("validation command", False, "README.md not found")

    text = readme.read_text(encoding="utf-8", errors="ignore").lower()
    keywords = ["test", "pytest", "unittest", "npm test", "cargo test", "validacion", "validation"]
    ok = any(keyword in text for keyword in keywords)
    detail = "README mentions how to validate changes" if ok else "README has no validation command"
    return AuditCheck("validation command", ok, detail)
