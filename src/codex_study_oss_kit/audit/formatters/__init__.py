from .json import format_json
from .markdown import format_markdown

FORMATTERS = {
    "json": format_json,
    "markdown": format_markdown,
}

__all__ = ["FORMATTERS", "format_json", "format_markdown"]
