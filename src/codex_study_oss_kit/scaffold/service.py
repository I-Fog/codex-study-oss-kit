from __future__ import annotations

from pathlib import Path

from ..core.models import ScaffoldFileSet, ScaffoldSpec
from ..core.paths import write_text_files
from ..core.rendering import render_template
from .languages import LANGUAGES


def scaffold_project(target: Path, title: str, language: str, force: bool = False) -> list[Path]:
    scaffold = build_scaffold(title=title, language=language)
    return write_text_files(target, scaffold.files, force)


def build_scaffold(title: str, language: str) -> ScaffoldFileSet:
    spec = ScaffoldSpec(title=title, language=language)
    language_scaffold = LANGUAGES.get(spec.normalized_language)
    validation_command = (
        language_scaffold.validation_command if language_scaffold else "Add the repository validation command here."
    )
    context = {
        "title": spec.title,
        "language": spec.normalized_language,
        "validation_command": validation_command,
    }
    files = {
        "AGENTS.md": render_template("scaffold/base/AGENTS.md.tmpl", context),
        "README.md": render_template("scaffold/base/README.md.tmpl", context),
        "rubrica.md": render_template("scaffold/base/rubrica.md.tmpl", context),
        "src/.gitkeep": "",
        "tests/.gitkeep": "",
        "soluciones/.gitkeep": "",
    }

    if language_scaffold:
        files.update(language_scaffold.build_files(spec))

    return ScaffoldFileSet(files=files)
