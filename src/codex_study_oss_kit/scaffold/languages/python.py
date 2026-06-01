from __future__ import annotations

from ...core.models import ScaffoldSpec
from ...core.rendering import render_template
from .base import LanguageScaffold


def build_files(spec: ScaffoldSpec) -> dict[str, str]:
    context = {
        "title": spec.title,
        "language": spec.normalized_language,
        "validation_command": PYTHON_LANGUAGE.validation_command,
    }
    return {
        "src/ejercicio.py": render_template("scaffold/python/ejercicio.py.tmpl", context),
        "tests/test_ejercicio.py": render_template("scaffold/python/test_ejercicio.py.tmpl", context),
    }


PYTHON_LANGUAGE = LanguageScaffold(
    name="python",
    validation_command="python -m unittest discover -s tests",
    build_files=build_files,
)
