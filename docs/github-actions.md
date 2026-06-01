# GitHub Actions

Use `codex-study audit` in CI to catch missing maintainer instructions, validation commands, tests, rubrics and source layout before a PR is merged.

## Minimal workflow

```yaml
name: Codex Study Audit

on:
  pull_request:
  push:

jobs:
  audit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - name: Install codex-study-oss-kit
        run: python -m pip install "git+https://github.com/I-Fog/codex-study-oss-kit.git"
      - name: Audit repository
        run: codex-study audit . --format markdown --output codex-study-audit.md
      - name: Upload audit report
        uses: actions/upload-artifact@v4
        with:
          name: codex-study-audit
          path: codex-study-audit.md
```

## JSON output

Use JSON when another script needs to read the result:

```bash
codex-study audit . --format json --output codex-study-audit.json
```
