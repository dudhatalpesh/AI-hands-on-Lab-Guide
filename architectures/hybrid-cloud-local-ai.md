# Hybrid cloud and local AI

## Logical architecture

```mermaid
flowchart LR
  User --> Classification
  Classification --> SensitiveLocalRoute
  Classification --> ApprovedCloudRoute
  SensitiveLocalRoute --> LocalModel
  ApprovedCloudRoute --> CloudModel
  LocalModel --> Review
  CloudModel --> Review
```

## Data flow and trust boundary

Use explicit permitted-data routing and region/retention requirements. Redaction can fail and is not a substitute for authorization.

## Trade-offs and validation

Compare task quality, egress, latency, availability and operations. Test that outages do not bypass routing policy.

## Customer design decisions

Record data classification, scale, p95 latency target, acceptable failure behavior, operating owner and deployment boundary in the [solution one-pager](../templates/solution-design-one-pager.md). Trace a normal request and a rejected request across every component.

## Implementation scope

This is a reference design, not a claim that every box is implemented in the educational labs. Compare it with [the security playbook](../docs/05-ai-security-playbook.md) before proposing a production deployment.
