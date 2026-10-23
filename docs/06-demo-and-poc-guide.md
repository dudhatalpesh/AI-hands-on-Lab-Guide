# Demo and POC guide

## Design a decision, not just a demonstration

Choose one bounded task, one audience and one measurable outcome. Agree the baseline, holdout cases, ownership, timebox and stop criteria before tuning. Use [POC plan](../templates/poc-plan.md) and [demo script](../templates/demo-script.md).

A ten-minute demo can allocate two minutes to the problem, three to a normal case, three to failures and controls, and two to trade-offs and next steps. Show source IDs, an unsupported question, tenant denial and an invalid tool. Keep offline fixtures clearly labeled if the model is unavailable.

## Evaluation worksheet

Create ten synthetic cases with fields: ID, question, expected source, expected action/abstention, risk severity and reviewer. Split development cases from holdout cases. Record prompt, model and corpus versions.

Score factual correctness and evidence support separately. Measure retrieval recall@k against expected documents, task success, refusal/abstention correctness, error rate and p50/p95 end-to-end latency. Generation traces in this starter do not include embedding/retrieval time: instrument the full request before reporting customer latency.

Example pilot gates to negotiate: zero unauthorized retrievals, all unapproved tools denied, at least 8/10 correctly reviewed holdout tasks and a p95 latency target measured on agreed hardware. Ten cases are a learning exercise, not a statistically sufficient production benchmark.

## Readout

Run the supplied ten-case seed set with `python scripts/evaluate.py --offline`, then `python scripts/evaluate.py` for live results. Inspect `artifacts/evaluation.json`, including end-to-end latency and source hit rate. Fill the human correctness, groundedness and abstention fields; the script intentionally does not invent these scores. Treat this published seed set as development data and create a separate untouched holdout set for your capstone. Evaluation artifacts contain synthetic answer text; operational traces remain metadata-only.

Report sample size and failure examples alongside averages. Separate measured results from estimates. Include review effort, infrastructure, integration and maintenance in TCO. Recommend go, revise or stop with an owner and date; do not translate a successful demo directly into an enterprise rollout.
