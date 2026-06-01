from .cpp import CPP_LANGUAGE
from .python import PYTHON_LANGUAGE

_LANGUAGE_LIST = [PYTHON_LANGUAGE, CPP_LANGUAGE]

LANGUAGES = {
    name: language
    for language in _LANGUAGE_LIST
    for name in (language.name, *language.aliases)
}

__all__ = ["CPP_LANGUAGE", "LANGUAGES", "PYTHON_LANGUAGE"]
