# codex-study-oss-kit

Toolkit open source para preparar repos educativos en espanol para trabajo con Codex y agentes de codigo.

El objetivo es reducir trabajo repetitivo en repos de practicas, apuntes y ejercicios: crear estructura inicial, revisar si el repo tiene instrucciones mantenibles y generar handoffs claros cuando una sesion larga se queda a medias.

## Why this exists

Many educational OSS repositories are useful but hard to maintain: missing test commands, unclear exercise layout, no agent instructions, no rubric, and no clean handoff between review sessions. This project turns those conventions into a small CLI that teachers, students and maintainers can reuse.

## MVP commands

```powershell
python -m codex_study_oss_kit scaffold .\demo-practica --title "Practica 1: Python basico" --language python
python -m codex_study_oss_kit audit .\demo-practica
python -m codex_study_oss_kit audit .\demo-practica --format json --output audit.json
python -m codex_study_oss_kit handoff .\demo-practica --objective "Cerrar tests de la practica 1" --current "Falta revisar casos borde"
```

## Install for local development

```powershell
python -m pip install -e .
python -m codex_study_oss_kit --help
python -m unittest discover -s tests
```

The package currently has no runtime dependencies.

## What the toolkit creates

`scaffold` creates a small educational repository:

- `AGENTS.md` with agent-maintenance rules.
- `README.md` with exercise context and validation commands.
- `rubrica.md` for review criteria.
- `src/` and `tests/` folders.
- `soluciones/` for maintained reference material.

`audit` checks whether a repository has the core maintenance pieces:

- agent instructions
- README
- tests
- rubric or review notes
- source folder
- validation command references

It can print Markdown for maintainers or JSON for automation:

```powershell
codex-study audit . --format markdown --output codex-study-audit.md
codex-study audit . --format json --output codex-study-audit.json
```

`handoff` writes a compact Markdown summary that another Codex thread or maintainer can continue from.

## Architecture

The codebase is split so new languages, checks and output formats can be added without changing the CLI surface:

```text
src/codex_study_oss_kit/
  cli/        argparse entrypoint and thin command handlers
  core/       shared models, path helpers and template rendering
  scaffold/   scaffold service plus language-specific builders
  audit/      audit service plus small registered checks
  handoff/    handoff model, Markdown renderer and writer
  templates/  bundled scaffold templates
```

To add a scaffold language, create a module in `scaffold/languages/`, add its templates under `templates/scaffold/<language>/`, and register the language in `scaffold/languages/__init__.py`.

To add an audit rule, create a focused check in `audit/checks/` and append it to `DEFAULT_CHECKS`.

## GitHub Actions

Use the sample workflow in [`examples/github-actions/codex-study-audit.yml`](examples/github-actions/codex-study-audit.yml) to run the audit in an educational repository. More detail is in [`docs/github-actions.md`](docs/github-actions.md).

## Roadmap

The public roadmap is tracked in GitHub issues:

- [Add SageMath notebook scaffold](https://github.com/I-Fog/codex-study-oss-kit/issues/1)
- [Add pull request summary workflow for audit reports](https://github.com/I-Fog/codex-study-oss-kit/issues/2)
- [Add rubric review mode for educational submissions](https://github.com/I-Fog/codex-study-oss-kit/issues/3)
- [Add real-world educational repository audit fixtures](https://github.com/I-Fog/codex-study-oss-kit/issues/4)
- [Improve Spanish educational templates](https://github.com/I-Fog/codex-study-oss-kit/issues/5)

## Example

See [`examples/python-basics`](examples/python-basics) and [`examples/cpp-basics`](examples/cpp-basics) for checked-in sample educational repo layouts.

## OpenAI Codex for OSS angle

This project is intentionally aligned with maintainer workflows: issue triage, PR review preparation, reproducible validation commands, release notes and handoffs. API credits would be used to add assisted review and rubric generation while keeping the base toolkit usable offline.
