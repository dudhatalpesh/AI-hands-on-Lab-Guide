# Lab 06: Constrain an agent

## Scenario and prerequisites

You advise fictional Northstar Services using synthetic policy and procurement data. Complete [setup](../../docs/02-environment-setup.md). Allow 90–150 minutes. Complete [lab 5](../lab-05-document-intelligence-workflow/README.md) first.

## Run from the repository root

```bash
python scripts/run_lab.py --lab 6 --offline
python scripts/run_lab.py --lab 6
```

The live command needs Ollama and the downloaded models. The optional Chroma/LangGraph flags need packages in `requirements.txt`; they also work with `--offline`. Change the user question with `--question "your synthetic question"` where relevant. See [shared implementation](../../src/advisor/core.py) and [runner](../../scripts/run_lab.py).

## Exercise

1. Inspect the model-selected proposal, validated tool result and final answer. Run an access question and a support question. Trace the two-call limit.
2. Try requesting a shell command. A proposal outside the allowlist must fail even if the model suggests it.
3. List tools that may be read-only and actions that need explicit approval.
4. Save your observations in an ignored `artifacts/lab-06-notes.md`, including versions, input, expected behavior, actual behavior and residual risk.

## Expected result and acceptance criteria

Only policy_lookup with an allowed topic can execute; malformed live proposals fail closed.

- [ ] The command exits successfully for the supported synthetic case.
- [ ] Inspect `artifacts/lab-06.json`; distinguish model output from deterministic policy decisions.
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

Continue to [lab 7](../lab-07-multi-agent-research-assistant/README.md) when directed by the [learning path](../../docs/00-learning-path.md).
