from __future__ import annotations

from ...core.models import ScaffoldSpec
from ...core.rendering import render_template
from .base import LanguageScaffold


def build_files(spec: ScaffoldSpec) -> dict[str, str]:
    context = {
        "title": spec.title,
        "language": spec.normalized_language,
        "validation_command": CPP_LANGUAGE.validation_command,
    }
    return {
        "src/sumar_pares.hpp": render_template("scaffold/cpp/sumar_pares.hpp.tmpl", context),
        "tests/test_sumar_pares.cpp": render_template("scaffold/cpp/test_sumar_pares.cpp.tmpl", context),
    }


CPP_LANGUAGE = LanguageScaffold(
    name="cpp",
    aliases=("c++", "cxx"),
    validation_command="mkdir -p build && g++ -std=c++17 -I src tests/test_sumar_pares.cpp -o build/test_sumar_pares && ./build/test_sumar_pares",
    build_files=build_files,
)
