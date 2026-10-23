# Enterprise RAG

## Logical architecture

```mermaid
flowchart LR
  Sources --> Ingestion
  Ingestion --> Chunks
  Chunks --> Embeddings
  Embeddings --> Index
  User --> Identity
  Identity --> ACLFilter
  ACLFilter --> Index
  Index --> Context
  Context --> Model
  Model --> Citations
```

## Data flow and trust boundary

Attach source ID, version and ACL metadata during ingestion. Apply permissions before sending evidence to the model. Re-index updates and propagate deletions.

## Trade-offs and validation

Measure retrieval recall, evidence support and stale-source behavior. Compare chunk sizes on held-out questions.

## Customer design decisions

Record data classification, scale, p95 latency target, acceptable failure behavior, operating owner and deployment boundary in the [solution one-pager](../templates/solution-design-one-pager.md). Trace a normal request and a rejected request across every component.

## Implementation scope

This is a reference design, not a claim that every box is implemented in the educational labs. Compare it with [the security playbook](../docs/05-ai-security-playbook.md) before proposing a production deployment.
