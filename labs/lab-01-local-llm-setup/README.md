# Lab 01: Confirm local inference

## Scenario and prerequisites

You advise fictional Northstar Services using synthetic policy and procurement data. Complete [setup](../../docs/02-environment-setup.md). Allow 90–150 minutes. No model is needed for the offline smoke run.

## Run from the repository root

```bash
python scripts/run_lab.py --lab 1 --offline
python scripts/run_lab.py --lab 1
```

The live command needs Ollama and the downloaded models. The optional Chroma/LangGraph flags need packages in `requirements.txt`; they also work with `--offline`. Change the user question with `--question "your synthetic question"` where relevant. See [shared implementation](../../src/advisor/core.py) and [runner](../../scripts/run_lab.py).

## Exercise

1. Compare an offline fixture with a real model response. Record the model tag, machine RAM, first-call latency and a repeated-call latency.
2. Stop the model service; rerun and identify the connection error. Restart and recover.
3. Explain why a successful response does not establish task suitability.
4. Save your observations in an ignored `artifacts/lab-01-notes.md`, including versions, input, expected behavior, actual behavior and residual risk.

## Expected result and acceptance criteria

The live result contains a short explanation, while offline output is explicitly marked OFFLINE FIXTURE. The trace records mode and latency.

- [ ] The command exits successfully for the supported synthetic case.
- [ ] Inspect `artifacts/lab-01.json`; distinguish model output from deterministic policy decisions.
- [ ] Record one negative case and its expected outcome.
- [ ] Explain the customer decision supported by your evidence.
- [ ] Run the live version before claiming model-quality results.

## Architecture

```mermaid
flowchart LR
  S[Synthetic input] --> C[Bounded application code]
  C --> M[Local model or offline fixture]
  M --> V[Validation and evidence]
  V --> H[Human review]
```

## Security and limitations

No external account, credentials or production data are needed. Generated answers remain untrusted. Offline fixtures bypass model reasoning and are unsuitable for prompt quality or injection-resistance claims. The demo has no production identity provider, multi-user storage, persistent approval system or distributed rate limiter.

## Troubleshooting and cleanup

For connection or missing-model errors, follow [troubleshooting](../../docs/07-troubleshooting-guide.md). A schema or tool-validation error can be an intended rejection: inspect the proposal before changing controls. Outputs overwrite the lab JSON; traces append. Delete only your generated files under `artifacts/` when finished; source fixtures remain reusable.

## Next step

Continue to [lab 2](../lab-02-prompt-engineering/README.md) when directed by the [learning path](../../docs/00-learning-path.md).
