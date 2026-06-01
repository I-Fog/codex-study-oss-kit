from __future__ import annotations

from pathlib import Path

from .templates import build_scaffold


def scaffold_project(target: Path, title: str, language: str, force: bool = False) -> list[Path]:
    scaffold = build_scaffold(title=title, language=language)
    created: list[Path] = []

    target.mkdir(parents=True, exist_ok=True)
    for relative_name, content in scaffold.files.items():
        path = target / relative_name
        if path.exists() and not force:
            continue
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        created.append(path)

    return created
