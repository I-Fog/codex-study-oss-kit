from __future__ import annotations

import json
import tempfile
import unittest
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path

from codex_study_oss_kit.audit import audit_project
from codex_study_oss_kit.cli import main
from codex_study_oss_kit.handoff import build_handoff_markdown
from codex_study_oss_kit.scaffold import build_scaffold, scaffold_project


class ScaffoldTest(unittest.TestCase):
    def test_scaffold_creates_agent_ready_layout(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "practica"

            created = scaffold_project(root, "Practica 1", "python")

            self.assertTrue((root / "AGENTS.md").exists())
            self.assertTrue((root / "README.md").exists())
            self.assertTrue((root / "rubrica.md").exists())
            self.assertTrue((root / "src" / "ejercicio.py").exists())
            self.assertTrue((root / "tests" / "test_ejercicio.py").exists())
            self.assertGreaterEqual(len(created), 6)

    def test_scaffold_does_not_overwrite_without_force(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "practica"
            scaffold_project(root, "Practica 1", "python")
            readme = root / "README.md"
            readme.write_text("custom", encoding="utf-8")

            scaffold_project(root, "Practica 2", "python")

            self.assertEqual(readme.read_text(encoding="utf-8"), "custom")

    def test_python_scaffold_uses_language_template(self) -> None:
        files = build_scaffold("Practica Python", "python").files

        self.assertIn("src/ejercicio.py", files)
        self.assertIn("tests/test_ejercicio.py", files)
        self.assertIn("python -m unittest discover -s tests", files["README.md"])

    def test_unknown_language_keeps_base_layout(self) -> None:
        files = build_scaffold("Practica C", "c").files

        self.assertIn("AGENTS.md", files)
        self.assertIn("README.md", files)
        self.assertNotIn("src/ejercicio.py", files)

    def test_cpp_scaffold_uses_language_template(self) -> None:
        files = build_scaffold("Practica C++", "cpp").files

        self.assertIn("src/sumar_pares.hpp", files)
        self.assertIn("tests/test_sumar_pares.cpp", files)
        self.assertIn("g++ -std=c++17", files["README.md"])


class AuditTest(unittest.TestCase):
    def test_audit_passes_on_scaffold(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "practica"
            scaffold_project(root, "Practica 1", "python")

            report = audit_project(root)

            self.assertTrue(report.ok)
            self.assertEqual(report.score, report.total)
            self.assertTrue(report.to_dict()["ok"])

    def test_audit_fails_on_empty_folder(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            report = audit_project(Path(directory))

            self.assertFalse(report.ok)
            self.assertLess(report.score, report.total)


class HandoffTest(unittest.TestCase):
    def test_handoff_contains_core_sections(self) -> None:
        content = build_handoff_markdown(
            root=Path("repo"),
            objective="Terminar tests",
            current="Falta caso borde",
            done="Scaffold creado",
            pending="Anadir CI",
            command="python -m unittest discover -s tests",
            restriction="No usar servicios externos",
        )

        self.assertIn("## Objective", content)
        self.assertIn("Terminar tests", content)
        self.assertIn("## Current", content)
        self.assertIn("No usar servicios externos", content)


class CliTest(unittest.TestCase):
    def test_cli_scaffold_and_audit(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "practica"

            self.assertEqual(main(["scaffold", str(root), "--title", "Practica CLI"]), 0)
            self.assertEqual(main(["audit", str(root)]), 0)

    def test_cli_audit_writes_json_report(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "practica"
            output = Path(directory) / "audit.json"
            scaffold_project(root, "Practica CLI", "python")

            self.assertEqual(main(["audit", str(root), "--format", "json", "--output", str(output)]), 0)

            data = json.loads(output.read_text(encoding="utf-8"))
            self.assertTrue(data["ok"])
            self.assertEqual(data["score"], data["total"])

    def test_cli_audit_prints_json_report(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "practica"
            scaffold_project(root, "Practica CLI", "python")
            stdout = StringIO()

            with redirect_stdout(stdout):
                exit_code = main(["audit", str(root), "--format", "json"])

            self.assertEqual(exit_code, 0)
            self.assertTrue(json.loads(stdout.getvalue())["ok"])


if __name__ == "__main__":
    unittest.main()
