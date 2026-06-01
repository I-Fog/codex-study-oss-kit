from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ScaffoldFiles:
    files: dict[str, str]


def build_scaffold(title: str, language: str) -> ScaffoldFiles:
    normalized_language = language.strip().lower() or "python"
    files = {
        "AGENTS.md": _agents_md(title, normalized_language),
        "README.md": _readme_md(title, normalized_language),
        "rubrica.md": _rubric_md(title),
        "src/.gitkeep": "",
        "tests/.gitkeep": "",
        "soluciones/.gitkeep": "",
    }

    if normalized_language == "python":
        files.update(
            {
                "src/ejercicio.py": PYTHON_EXERCISE,
                "tests/test_ejercicio.py": PYTHON_TEST,
            }
        )

    return ScaffoldFiles(files=files)


def _agents_md(title: str, language: str) -> str:
    return f"""# AGENTS.md

## Contexto

Repositorio educativo: {title}

Lenguaje principal: {language}

## Flujo esperado

- Antes de cambiar codigo, mira el enunciado, los tests y la rubrica.
- Mantener las soluciones de referencia separadas del codigo que completa el estudiante.
- Cuando una explicacion este en espanol, usa un tono claro y cercano.
- No inventes requisitos: si falta un caso, anotalo como pendiente.

## Validacion

- Ejecuta los tests del repositorio antes de cerrar un cambio.
- Si no puedes ejecutar un comando, deja escrito el motivo exacto.
"""


def _readme_md(title: str, language: str) -> str:
    return f"""# {title}

Practica educativa preparada para trabajo con agentes de codigo.

## Objetivo

Completar los ejercicios manteniendo tests, explicaciones y rubrica alineados.

## Estructura

- `src/`: codigo del ejercicio.
- `tests/`: pruebas automatizadas.
- `soluciones/`: soluciones de referencia mantenidas por el equipo docente.
- `rubrica.md`: criterios de revision.

## Lenguaje

{language}

## Validacion

```powershell
python -m unittest discover -s tests
```
"""


def _rubric_md(title: str) -> str:
    return f"""# Rubrica

Practica: {title}

## Criterios

- Correctitud: el codigo cumple los casos pedidos.
- Claridad: nombres, estructura y comentarios ayudan a revisar.
- Tests: cubren casos normales y al menos un caso borde.
- Reproducibilidad: cualquier persona puede ejecutar la validacion documentada.

## Notas para revision con agentes

- Primero revisamos fallos reproducibles.
- Luego miramos legibilidad y explicacion.
- Al final dejamos pendientes concretos, no observaciones vagas.
"""


PYTHON_EXERCISE = '''"""Ejercicio de ejemplo para el scaffold."""


def sumar_pares(numeros: list[int]) -> int:
    """Sumamos solo los valores pares de la lista."""
    return sum(numero for numero in numeros if numero % 2 == 0)
'''


PYTHON_TEST = '''import unittest

from src.ejercicio import sumar_pares


class SumarParesTest(unittest.TestCase):
    def test_suma_solo_pares(self) -> None:
        self.assertEqual(sumar_pares([1, 2, 3, 4]), 6)

    def test_lista_sin_pares(self) -> None:
        self.assertEqual(sumar_pares([1, 3, 5]), 0)


if __name__ == "__main__":
    unittest.main()
'''
