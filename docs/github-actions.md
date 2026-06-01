# GitHub Actions

Use `codex-study audit` in CI to catch missing maintainer instructions, validation commands, tests, rubrics and source layout before a PR is merged.

## Minimal workflow

```yaml
name: Codex Study Audit

on:
  pull_request:
  push:

permissions:
  contents: read
  pull-requests: write

env:
  FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: "true"

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
      - name: Comment audit summary on pull request
        if: github.event_name == 'pull_request' && github.event.pull_request.head.repo.full_name == github.repository
        uses: actions/github-script@v7
        with:
          script: |
            const fs = require("fs");

            const marker = "<!-- codex-study-audit -->";
            const report = fs.readFileSync("codex-study-audit.md", "utf8").trim();
            const body = `${marker}\n## Codex Study Audit\n\n${report}\n\n_Updated by Codex Study Audit workflow._`;
            const { owner, repo } = context.repo;
            const issue_number = context.payload.pull_request.number;
            const comments = await github.rest.issues.listComments({ owner, repo, issue_number, per_page: 100 });
            const existing = comments.data.find(
              (comment) => comment.user.type === "Bot" && comment.body.includes(marker),
            );

            if (existing) {
              await github.rest.issues.updateComment({ owner, repo, comment_id: existing.id, body });
            } else {
              await github.rest.issues.createComment({ owner, repo, issue_number, body });
            }
      - name: Upload audit report
        uses: actions/upload-artifact@v4
        with:
          name: codex-study-audit
          path: codex-study-audit.md
```

The comment step is intentionally limited to pull requests whose source branch is in the same repository. Forked pull requests still get the uploaded artifact, but the workflow does not request elevated permissions to run untrusted contributor code.

`FORCE_JAVASCRIPT_ACTIONS_TO_NODE24` opts GitHub JavaScript actions into the newer Node runtime before GitHub's Node 20 runner deprecation deadline.

## JSON output

Use JSON when another script needs to read the result:

```bash
codex-study audit . --format json --output codex-study-audit.json
```
