# Solution design one-pager

Customer/project:  
Prepared by:  
Date/version:  
Data classification: synthetic training / approved internal

## Outcome and scope
- User, task and measurable business outcome:
- In scope / out of scope:
- Baseline and success gate:

## Architecture
```mermaid
flowchart LR
  User --> Gateway
  Gateway --> Orchestration
  Orchestration --> Retrieval
  Retrieval --> Model
  Model --> Review
```

- Deployment: local / cloud / hybrid, with rationale:
- Data sources, classification and identity/ACL enforcement:
- Model, retrieval and tool boundaries:
- Latency, concurrency and failure behavior:

## Trade-offs and operation
- Alternatives considered and evidence:
- Cost assumptions and review workload:
- Monitoring, deletion, rollback and owning team:
- Residual risks and approval decision:
