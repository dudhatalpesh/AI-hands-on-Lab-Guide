# Learning path

Plan for 5–7 hours per week: concepts, implementation, testing and customer communication. Prior Python programming experience helps; enterprise fundamentals are assumed. Labs 8–11 are deliberately reused for architecture, security and governance with different deliverables.

| Week | Phase and module | Lab | Evidence to retain |
| --- | --- | --- | --- |
| 1 | Foundations: 01 AI foundations | 01 | Local inference baseline and limitations |
| 2 | Foundations: 02 LLMs and prompting | 02 | Prompt comparison scorecard |
| 3 | Conversation/RAG: 03 conversational AI | 03 | Escalation and session design |
| 4 | Conversation/RAG: 04 enterprise knowledge | 04 | Retrieval and citation review |
| 5 | Workflows: 05 AI workflows | 05 | Schema and human review map |
| 6 | Agents: 06 single-agent systems | 06 | Tool permissions and action budget |
| 7 | Agents: 07 multi-agent systems | 07 | Single versus multi-role comparison |
| 8 | Architecture: 08 deployment | 08 | Local/cloud decision and trust boundaries |
| 9 | Evaluation: 09 observability | 10 | Holdout cases and quality/latency baseline |
| 10 | Security: 10 fundamentals + 11 red teaming | 08 + 09 | Threat model and scoped findings |
| 11 | Adoption: 12 governance | 11 | Accountable risk and privacy review |
| 12 | Adoption: 13 capstone | 11 | Customer briefing and go/revise/stop decision |

## Accelerated four-week path

Allocate 15–20 hours per week. Preserve all security and evaluation gates.

1. Modules 01–04; labs 01–04. Deliver a grounded assistant and explain its limitations.
2. Modules 05–07; labs 05–07. Demonstrate validated extraction and bounded tools.
3. Modules 08–11; labs 08–10. Establish a deployment design, holdout evaluation and red-team evidence.
4. Modules 12–13; lab 11. Complete governance and present the customer recommendation.

## Progress gates

- [ ] Gate 1: Explain model limitations and demonstrate repeatable local inference.
- [ ] Gate 2: Show evidence-backed answers and an unsupported-question test.
- [ ] Gate 3: Reject an unauthorized tool and describe human approval boundaries.
- [ ] Gate 4: Demonstrate tenant retrieval isolation and measure quality and latency.
- [ ] Gate 5: Present a documented recommendation with accountable residual risk.

Use [PROGRESS.md](../PROGRESS.md) for module-level checklists.

## Capstone assessment

Score each area 0–4: discovery, architecture, working demo, evaluation, security, economics and communication. Zero means absent; one is asserted; two is documented; three is demonstrated with reproducible evidence; four includes negative tests and defended alternatives. Pass at 21/28 with security and evaluation each at least 3. A demonstrated unauthorized disclosure or executable unapproved tool blocks a pass regardless of score.

Submit a one-page design, ten-case holdout set, scored results, risk register, cost model and ten-minute demo. Include at least two unsupported questions, two tenant/permission cases and one outage case. A peer records the decision and remaining actions.
