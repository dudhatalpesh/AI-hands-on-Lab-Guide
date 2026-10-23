# Multi-agent systems

[Learning path](../../docs/00-learning-path.md) · Module 7 of 13

## Learning objectives

Orchestrate researcher and reviewer roles; compare with one agent.

## Prerequisites and estimated time

Complete [module 6](../06-single-agent-systems/README.md). Allow 60–90 minutes for concepts and 90–150 minutes for the lab and consulting artifact.

## Customer scenario

A consultant needs a reviewed architecture recommendation.

## Concepts

Multiple roles can separate research and critique, but increase cost, latency and correlated error. Use explicit state, typed handoffs and stop conditions. A reviewer using the same model is not independent assurance. Prefer fixed workflows when dynamic delegation adds no measured value.

## Hands-on lab

Complete [lab-07-multi-agent-research-assistant](../../labs/lab-07-multi-agent-research-assistant/README.md). Record the command, configuration, observed result and one limitation. 

## Architecture diagram

```mermaid
flowchart LR
  U[Customer requirement] --> P[Application policy]
  P --> C[Multi-agent systems]
  C --> E[Evidence and evaluation]
  E --> H[Human decision]
```

Identify the untrusted input and the authority that approves an action. Expand the relevant [reference architecture](../../architectures/secure-ai-reference-architecture.md) with customer-specific boundaries.

## Troubleshooting

If the lab cannot reach Ollama, check its URL and service before changing prompts. If output is inconsistent, preserve the input and model tag, rerun the same case, and compare against the rubric. Offline fixtures validate plumbing only. See [troubleshooting](../../docs/07-troubleshooting-guide.md).

## Security considerations

Treat all model output and retrieved text as untrusted. Use synthetic data, minimize retained content and enforce permissions outside the model. For this scenario, document one disclosure risk, one integrity risk and one operational failure with an owner.

## Customer conversation prompts

Does a second agent improve measured quality? Who resolves conflicting findings?

## Knowledge check

1. Does agreement between agents establish truth?
2. Name one failure mode in this scenario and a measurable test for it.
3. Explain the design trade-off to a non-specialist in two sentences.

<details>
<summary>Answer guidance</summary>

No; they can share the same faulty premise. A strong scenario answer names an observable failure, the control enforcing the boundary and a pass/fail test; trade-offs should connect quality, cost or latency to the customer's requirement.
</details>

## Deliverable and next step

- [ ] Complete the lab acceptance criteria.
- [ ] Write a five-sentence customer recommendation with evidence and residual risk.
- [ ] Explain the knowledge-check answers without reading the lesson.

Continue to [AI architecture and deployment](../08-ai-architecture-and-deployment/README.md).
