# Project Instructions

## Scope

This repository is an OSS toolkit for Spanish-speaking educational and study repositories that want to be easier to maintain with Codex or similar coding agents.

## Commands

- Run tests with `python -m unittest discover -s tests`.
- Smoke-test the CLI with `python -m codex_study_oss_kit --help`.
- Keep the package dependency-free unless a dependency removes clear complexity.

## Style

- Prefer small, explicit Python modules over broad abstractions.
- Keep generated templates practical and student-friendly.
- Spanish template comments should sound natural and close: prefer "dejamos", "miramos", "usamos" or direct explanations over formal manual phrasing.
- Keep public docs bilingual enough for discoverability, but prioritize Spanish examples.

## Architecture

- Keep CLI parsing in `src/codex_study_oss_kit/cli/`; command modules should call services instead of holding business logic.
- Keep reusable primitives in `src/codex_study_oss_kit/core/`.
- Add scaffold language support under `src/codex_study_oss_kit/scaffold/languages/` and register it in `languages/__init__.py`.
- Add audit checks as small functions under `src/codex_study_oss_kit/audit/checks/` and register them in `DEFAULT_CHECKS`.
- Add audit output formats under `src/codex_study_oss_kit/audit/formatters/` and register them in `FORMATTERS`.
- Keep text templates under `src/codex_study_oss_kit/templates/`; do not put large generated files back into Python strings.

## Generated Files

- Files under `examples/` are checked-in examples, not build artifacts.
- Scaffolds created by the CLI during tests must live in temporary directories.
- Do not commit local `.env` files, tokens, logs, screenshots, or generated handoffs from private work.
