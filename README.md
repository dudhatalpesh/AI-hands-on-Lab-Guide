# AI-for-Solutions-Consultants

A practical journey from **AI-aware technologist** to **trusted AI solutions advisor** for Solutions Consultants, Sales Engineers, Solution Architects and cybersecurity consultants.

Learn to discover requirements, design architectures, demonstrate solutions, evaluate outcomes and guide secure adoption. All required labs run locally; no paid subscription or API key is required.

## Start here

1. Follow [environment setup](docs/02-environment-setup.md).
2. Choose the [12-week or accelerated 4-week path](docs/00-learning-path.md).
3. Complete each module, run its lab, and retain the customer deliverable.
4. Track evidence in [PROGRESS.md](PROGRESS.md) or a learning-progress issue.

```bash
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
python scripts/run_lab.py --lab 1 --offline
# With Ollama running and models downloaded:
python scripts/run_lab.py --lab 1
```

Offline mode supplies deterministic fixtures for exercising application behavior. It does **not** demonstrate model quality, real embeddings or resistance to prompt injection.

## Repository map

| Directory | Purpose |
| --- | --- |
| [docs](docs/01-how-to-use-this-repo.md) | Learning path, setup, tool guide and consultant playbooks |
| [modules](modules/01-ai-foundations/README.md) | Thirteen progressive lessons with knowledge checks |
| [labs](labs/lab-01-local-llm-setup/README.md) | Eleven local exercises with acceptance criteria |
| [architectures](architectures/secure-ai-reference-architecture.md) | Mermaid diagrams, trust boundaries and deployment trade-offs |
| [templates](templates/discovery-questionnaire.md) | Reusable customer workshop and POC artifacts |
| `src/advisor/`, `tests/` | Shared lab implementation and regression tests |
| `data/`, `assets/` | Synthetic fixtures and versionable visual sources |

## Scope and readiness

This is a maintainable educational starter, not a certified or production-hardened service. The API is a loopback-only demo with a fixed server-side identity. Production identity, distributed quotas, approval persistence, tenancy lifecycle and operational recovery are design exercises described in the security playbook.

The default stack is Python, Ollama, Chroma, LangGraph, FastAPI and Streamlit. Advanced tools are optional; see the [tool selection guide](docs/03-tool-selection-guide.md), including license distinctions for n8n and Docker Desktop.

See [CONTRIBUTING.md](CONTRIBUTING.md), [SECURITY.md](SECURITY.md) and [LICENSE](LICENSE). External interface sources and review dates are recorded in [sources](docs/10-sources-and-maintenance.md).
