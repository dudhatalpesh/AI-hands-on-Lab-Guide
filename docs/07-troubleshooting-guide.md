# Troubleshooting guide

| Symptom | Check | Action |
| --- | --- | --- |
| Python not found | Interpreter installation and PATH | Install Python 3.11+; use py on Windows or python3 on Unix |
| Activation blocked | Organization PowerShell policy | Use the virtual environment interpreter directly |
| Module import fails | Active interpreter and requirements | Run python -m pip install -r requirements.txt |
| Connection refused | Ollama service and URL | Start Ollama; inspect OLLAMA_BASE_URL |
| Model not found | ollama list | Pull the configured generation and embedding models |
| Port 11434 already bound | Host app versus container | Run only the intended Ollama service |
| Slow generation/OOM | Model size, available RAM and concurrent calls | Use the default small model, reduce concurrency and measure |
| Bad retrieval | Query wording, embedding model and corpus | Inspect source IDs; re-embed after model changes |
| Invalid JSON/tool proposal | Raw synthetic test and schema | Fail closed and route to review; do not loosen authorization |
| Empty dashboard | Trace file and selected mode | Run lab 10; select offline or live correctly |
| Docker connection fails | Daemon status and permissions | Start Docker or use the native Python route |
| Unhelpful offline answer | Fixture mode | Run live inference for quality evaluation |

No code auto-retries a tool action. If you add retries, bound attempts and use idempotency for side effects. Do not increase timeouts indefinitely or expose Ollama publicly to solve local connectivity.

When reporting a bug, include OS, Python version, dependency versions, model tag, exact command and a synthetic reproduction. Remove secrets and customer data.
