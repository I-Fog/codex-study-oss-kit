from __future__ import annotations

from pathlib import Path


def write_text_files(root: Path, files: dict[str, str], force: bool = False) -> list[Path]:
    created: list[Path] = []
    root.mkdir(parents=True, exist_ok=True)

    for relative_name, content in files.items():
        path = root / relative_name
        if path.exists() and not force:
            continue
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        created.append(path)

    return created
