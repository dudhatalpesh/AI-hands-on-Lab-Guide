# AI security playbook

Treat the application as a system of identities, data stores, models and tools. A model is not a trusted policy enforcement point.

## Threat-model the boundaries

Draw user → gateway → orchestrator → retriever → model → downstream tool. Mark each data source, trust boundary, identity, credential and action. Review confidentiality, integrity, availability and harms to affected users.

| Risk | Preventive control | Verification |
| --- | --- | --- |
| Direct/indirect prompt injection | Least-privilege tools; isolate untrusted evidence; constrain actions | Adversarial prompts plus tool-boundary tests |
| Sensitive disclosure | Pre-retrieval ACLs, minimization, scoped sessions | Cross-tenant and revoked-document cases |
| Excessive agency | Narrow tool schemas, budgets, explicit approvals | Reject unknown tools and replayed approvals |
| Improper output handling | Typed validation, escaping, parameterized operations | Treat output as text; never eval or execute it |
| Supply-chain compromise | Review model provenance, dependencies and licenses | Pin reviewed releases; verify artifacts and scan |
| Model abuse/resource exhaustion | Input bounds, concurrency limits, quotas, timeouts | Oversized input and bounded retry tests |
| Poisoned knowledge | Trusted ingestion, provenance and version rollback | Injected-document and stale-source tests |
| Privacy failures | Retention, deletion, consent/purpose review | Trace data lifecycle and deletion propagation |

Map these to the [OWASP LLM risk guidance](https://owasp.org/www-project-top-10-for-large-language-model-applications/). This checklist is an implementation aid, not a certification.

## What the code enforces

The example filters tenant documents before retrieval, bounds input size, validates one allowlisted read-only tool and emits metadata-only generation traces. Unknown tenants receive no model call. Extraction always awaits human review.

The fixed API identity is for a single-user demo. In production, validate identity at the gateway and derive tenant and permissions from trusted claims. Enforce document ACL changes and deletions across caches, indexes and backups. Add per-user quotas, rate limits, request IDs, secure transport, persistent approvals, audited tool credentials and incident recovery.

## What prompting cannot guarantee

A prompt cannot reliably neutralize malicious documents, prove factuality or prevent leakage from already exposed context. Neither keyword filters nor citations provide an authorization boundary. The red-team suite is intentionally small; expanding it and testing real models is required before making security claims.

## Response and governance

Assign incident owners and escalation channels. Define how to disable tools, revoke credentials, quarantine documents, preserve privacy-safe evidence and notify affected parties. Review risk at every model, prompt, tool or corpus change. Record residual risk and accountable acceptance in the [risk register](../templates/risk-register.md).
