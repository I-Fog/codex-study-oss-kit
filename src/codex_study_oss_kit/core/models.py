from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ScaffoldSpec:
    title: str
    language: str

    @property
    def normalized_language(self) -> str:
        return self.language.strip().lower() or "python"


@dataclass(frozen=True)
class ScaffoldFileSet:
    files: dict[str, str]
