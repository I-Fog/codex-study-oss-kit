from __future__ import annotations

from importlib.resources import files


def render_template(relative_path: str, values: dict[str, str]) -> str:
    template = read_template(relative_path)
    return template.format_map(values)


def read_template(relative_path: str) -> str:
    parts = relative_path.replace("\\", "/").split("/")
    resource = files("codex_study_oss_kit").joinpath("templates", *parts)
    return resource.read_text(encoding="utf-8")
