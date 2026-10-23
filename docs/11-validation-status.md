# Validation status

This file separates completed verification from pending environment-dependent checks.

## Initial environment

The authoring host has no Python interpreter on PATH and its Docker daemon is stopped. Live Ollama generation, embeddings, Chroma, LangGraph, API and dashboard execution therefore have not yet been verified on this host.

On 2026-10-23, PowerShell static validation passed for local Markdown link targets, all required module sections, the 13-module/11-lab layout, and JSON fixture parsing. The repository contains 88 files. An attempt to obtain a workspace-local Python runtime could not connect to the download server. No Python test execution is claimed.

## Release checks

- [ ] Run offline unittest suite on Python 3.11 and 3.12.
- [ ] Run scripts/check_repo.py and Python compile checks.
- [ ] Install optional dependencies and run Chroma and LangGraph fixture integrations.
- [ ] Run live labs 01–11 with the recorded model versions.
- [ ] Validate API and dashboard on loopback.
- [ ] Test Docker Compose with a running daemon.
- [ ] Capture reviewed dependency versions and image digests.
- [ ] Publish a monitored private security/moderation contact before public launch.

GitHub Actions is configured for cross-platform offline checks and Linux framework integration checks. Configuration is not evidence that a workflow has executed. Update this record with commands, platform, date and actual results.
