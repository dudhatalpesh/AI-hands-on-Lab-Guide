# Environment setup

## Requirements

Use Python 3.11 or newer; CI covers 3.11 and 3.12. Install Python from [python.org](https://www.python.org/downloads/) and Git from [git-scm.com](https://git-scm.com/downloads). Install [Ollama](https://ollama.com/download) for your OS. Start with 8 GB RAM and several GB of free disk as a practical planning estimate, not a guaranteed minimum. CPU inference works but speed varies. Offline smoke tests need neither Ollama nor third-party packages.

Clone your own published fork URL, or open this downloaded directory. No GitHub repository URL is assumed.

## Windows PowerShell

```powershell
cd AI-for-Solutions-Consultants
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
Copy-Item .env.example .env
```

If activation is blocked by organizational policy, use `.\.venv\Scripts\python.exe` in place of `python`; do not weaken machine policy. Ensure `py -3 --version` reports at least 3.11.

## macOS and Linux

```bash
cd AI-for-Solutions-Consultants
python3 --version
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
cp .env.example .env
```

Use a Python 3.11+ interpreter. Some Linux distributions require their Python venv package. Follow distribution documentation; do not install packages globally with sudo pip.

## Ollama models

Start the desktop app or run `ollama serve` in a separate terminal if no server is running.

```bash
ollama pull qwen2.5:1.5b
ollama pull nomic-embed-text
ollama list
python scripts/run_lab.py --lab 1
python scripts/run_lab.py --lab 4
```

The [generation model](https://ollama.com/library/qwen2.5:1.5b) is intentionally small for learning. Review each model's license separately from the runtime license. Configure model tags, URL and timeout in `.env`. Model downloads require internet; inference can run locally afterward. Re-embed the corpus after changing embedding models.

## Verify and launch demos

```bash
python -m unittest discover -s tests -v
python scripts/check_repo.py
python scripts/run_lab.py --lab 11 --offline
python -m uvicorn src.advisor.api:app --host 127.0.0.1 --port 8000
```

Visit `http://127.0.0.1:8000/docs` and use POST /ask with `{"question":"What requires MFA?"}`. In another terminal:

```bash
python scripts/run_lab.py --lab 10
python -m streamlit run scripts/dashboard.py --server.address 127.0.0.1
```

The dashboard is for trace inspection; the API is the interactive question demo. Keep both on loopback.

## Docker alternative

Install Docker Engine or Docker Desktop under applicable licensing terms. Start the daemon and run:

```bash
docker compose up -d ollama
docker compose exec ollama ollama pull qwen2.5:1.5b
docker compose exec ollama ollama pull nomic-embed-text
docker compose --profile lab run --rm lab
docker compose --profile lab run --rm lab python -m unittest discover -s tests -v
docker compose down
```

Do not run the host Ollama and container on port 11434 simultaneously. Container outputs are ephemeral; copy evidence out before removing a container if needed. The named volume retains models; `docker compose down` does not remove it. This CPU-first image uses a rolling Ollama tag for onboarding: record image digests and freeze reviewed dependency versions before reproducible workshops. No cross-platform lockfile or production image attestation is claimed.

## Optional cloud services

No cloud API is implemented or required. Free quotas and eligibility change. Evaluate provider privacy terms and quotas before adding an adapter, keep keys in environment variables, and retain Ollama as the fallback. Never promise a permanently free quota.
