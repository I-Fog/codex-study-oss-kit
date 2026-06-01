from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

from ...core.models import ScaffoldSpec


LanguageFileBuilder = Callable[[ScaffoldSpec], dict[str, str]]


@dataclass(frozen=True)
class LanguageScaffold:
    name: str
    validation_command: str
    build_files: LanguageFileBuilder
