# Consultant playbook

## Discover before demonstrating

Identify the process owner, users, current baseline, decision frequency and consequences of error. Ask for representative examples, including failures and exceptions. Classify data and confirm who can authorize its use. Use the [discovery questionnaire](../templates/discovery-questionnaire.md).

Translate “we need a copilot” into a measurable task: “reduce policy lookup time while preserving access control and source accuracy.” Separate user satisfaction from business outcomes and technical metrics.

## Qualify the architecture

| Requirement | Candidate pattern | Trade-off to explain |
| --- | --- | --- |
| Current enterprise knowledge | RAG | Retrieval quality and document lifecycle |
| Repetitive structured intake | Validated workflow | Exceptions and review workload |
| Read-only adaptive lookup | Bounded agent | Tool selection errors and extra latency |
| Exact policy decision | Rules engine | Rule maintenance, but predictable behavior |
| Sensitive offline processing | Local inference | Capacity, patching and operational burden |

Ask who will run the solution after the POC. A demo without an operational owner is not an adoption plan.

## Business case

Estimate annual net value as eligible tasks × adoption × measured time saved × loaded labor rate × realizable benefit fraction, minus annual operating cost. Distinguish time capacity from actual cash savings. Include review, exception handling, integration, evaluation, security, infrastructure and model-change costs.

For a synthetic example: 10,000 tasks × 50% adoption × 4 minutes saved ÷ 60 × USD 60/hour = USD 20,000 gross capacity value before realization and costs. This is arithmetic, not a product price or promised ROI. Compare optimistic, base and pessimistic assumptions; include a non-AI baseline.

## Handle objections with evidence

“Can it hallucinate?” Yes. Explain bounded use, grounded evidence, abstention, review and observed failure rates.

“Can all data stay local?” The default inference does, but check model downloads, telemetry, integrations, backups and support tooling.

“Will agents replace approvals?” Approval belongs in trusted workflow controls. Model confidence cannot authorize a consequential action.

“Why not use a larger model?” Benchmark representative tasks, concurrency and total cost before assuming size improves the business outcome.

Close with agreed success criteria, owners, constraints, a stop condition and a dated next decision.
