# AI gateway

## Logical architecture

```mermaid
flowchart LR
  Client --> IdentityGateway
  IdentityGateway --> Quotas
  Quotas --> Routing
  Routing --> LocalModel
  Routing --> CloudModel
  Routing --> AuditMetadata
```

## Data flow and trust boundary

Validate identity, policy and budgets before model routing. Apply data-classification rules before cloud egress. Keep secrets out of prompts and logs.

## Trade-offs and validation

Test authentication failure, quotas, provider timeout and fallback policy. Do not silently send sensitive traffic to a cloud fallback.

## Customer design decisions

Record data classification, scale, p95 latency target, acceptable failure behavior, operating owner and deployment boundary in the [solution one-pager](../templates/solution-design-one-pager.md). Trace a normal request and a rejected request across every component.

## Implementation scope

This is a reference design, not a claim that every box is implemented in the educational labs. Compare it with [the security playbook](../docs/05-ai-security-playbook.md) before proposing a production deployment.
