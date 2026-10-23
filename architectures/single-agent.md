# Single agent

## Logical architecture

```mermaid
flowchart LR
  Request --> Planner
  Planner --> ToolPolicy
  ToolPolicy --> ReadOnlyTool
  ReadOnlyTool --> Observation
  Observation --> Answer
```

## Data flow and trust boundary

Treat the model's tool request as an untrusted proposal. Enforce allowlists, arguments, identity and iteration budgets outside the model.

## Trade-offs and validation

Compare against direct lookup. Test unauthorized tools, invalid arguments and service failures.

## Customer design decisions

Record data classification, scale, p95 latency target, acceptable failure behavior, operating owner and deployment boundary in the [solution one-pager](../templates/solution-design-one-pager.md). Trace a normal request and a rejected request across every component.

## Implementation scope

This is a reference design, not a claim that every box is implemented in the educational labs. Compare it with [the security playbook](../docs/05-ai-security-playbook.md) before proposing a production deployment.
