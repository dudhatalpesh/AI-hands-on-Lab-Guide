# Tool selection guide

Choose the smallest stack that proves the use case. Labels describe the listed component, not every hosted offering under its brand.

| Tool | License/service label | Location | Curriculum role | Beginner recommendation |
| --- | --- | --- | --- | --- |
| Python | Open source | Local | Required runtime | Yes |
| Ollama | Open source runtime; model licenses vary | Local | Default live inference | Yes |
| Hugging Face Transformers | Open source library; model licenses vary | Local | Optional direct model loading | After foundations |
| LangChain | Open source library | Local | Optional application abstractions | After plain Python |
| LlamaIndex | Open source core | Local | Optional retrieval framework alternative | After RAG basics |
| LangGraph | Open source library | Local | Optional implemented orchestration extension | After single agent |
| CrewAI | Open source framework | Local | Optional multi-agent alternative | Advanced |
| Chroma | Open source core | Local | Implemented vector-search extension | Yes after baseline |
| Qdrant | Open source server; cloud service has separate terms | Local / Cloud | Optional vector database alternative | For service deployment |
| FAISS | Open source library | Local | Optional similarity-search alternative | For library-based search |
| FastAPI | Open source | Local | Included API demo | Yes |
| Streamlit | Open source library | Local | Included trace dashboard | Yes |
| Gradio | Open source library | Local | Optional UI alternative | Yes |
| Jupyter | Open source | Local | Optional notebook exploration | Yes |
| Docker Engine / Compose | Open source components | Local | Optional reproducibility | Yes |
| Docker Desktop | Freemium/proprietary distribution; eligibility-dependent | Local | Optional desktop container runtime | Check terms |
| n8n Community | Source-available, fair-code; not OSI open source | Local | Optional low-code exercise | Yes, with license review |
| n8n Cloud | Paid hosted service/trial terms vary | Cloud | Optional, never required | Not required |
| Hugging Face Hub | Freemium hosted service | Cloud | Optional model discovery/downloads | Review model cards |

No listed cloud service is necessary to finish a lab. Hosted quotas are deliberately not hard-coded.

## Selection questions

- Start with rules or search if the output is deterministic.
- Use RAG for changing authoritative knowledge; fine-tuning is not a replacement for current evidence or access control.
- Use a fixed workflow when transitions are known; introduce agents only for measured value from tool selection.
- Compare local and cloud inference on data policy, task quality, p95 latency, concurrency, operations and total cost.
- Use direct Python first. Add a framework when its state, persistence or integration features justify the dependency.

## Optional extensions

Transformers: follow the [official pipeline tutorial](https://huggingface.co/docs/transformers/pipeline_tutorial), select a compatible text-generation model and compare its license and measured memory use with Ollama.

n8n: follow [self-hosted setup](https://docs.n8n.io/hosting/), then build Manual Trigger → Edit Fields with synthetic request text → HTTP Request to local Ollama POST /api/generate → validation/review branch. Send model, prompt and stream=false as JSON. A container cannot reach host services through its own localhost; use an explicitly configured private network route. Never expose an unauthenticated model endpoint publicly. Keep all ordering actions disabled. Verify [license terms](https://github.com/n8n-io/n8n/blob/master/LICENSE.md) before embedding or reselling workflows.
