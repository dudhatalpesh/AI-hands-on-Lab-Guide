# Contributing

Start with an issue describing the learner or customer problem. Keep changes focused and use imperative commit subjects such as `Add retrieval isolation regression test`; no prior Git history establishes a stricter convention.

## Local checks

Use Python 3.11+ and four-space indentation, snake_case functions/files, PascalCase classes and type hints on public functions. Folder names use kebab-case. Run:

```bash
python -m pip install -r requirements-dev.txt
python -m unittest discover -s tests -v
python scripts/check_repo.py
python -m ruff check .
```

Keep core tests offline and deterministic. Add regression tests for changed behavior, especially tenant isolation, tool validation, input bounds and output parsing. No percentage coverage target is claimed; security invariants must have explicit tests.

Each module needs objectives, prerequisites, time, concepts, lab, architecture, troubleshooting, security, customer prompts, knowledge check and next steps. Each lab needs exact commands, expected behavior and a measurable deliverable. Use synthetic data only.

PRs must describe the problem, resulting behavior, validation and limitations; link issues and include screenshots for UI changes. Identify new dependencies, licenses, network calls and data flows. Do not commit credentials, generated customer artifacts or model weights. Verify live model examples separately and report model/version and platform. Update sources when changing external API guidance.
