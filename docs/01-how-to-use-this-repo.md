# How to use this repository

Read the [learning path](00-learning-path.md), prepare the [environment](02-environment-setup.md), then follow modules in numeric order. Work from the repository root so commands can find the shared package.

Each module follows concept → customer scenario → lab → evidence → recommendation. The shared runner prevents drift between eleven labs; each lab README adds a distinct experiment and acceptance criteria. Read the relevant function in `src/advisor/core.py` before modifying it.

Start offline to validate application plumbing. Switch to live Ollama to examine actual generation and embedding behavior. A deterministic fixture is never evidence of hallucination resistance, extraction quality or semantic search quality.

Retain outputs in ignored `artifacts/`. Copy [templates](../templates/discovery-questionnaire.md) for customer exercises and use only synthetic names and records. Record hardware, model tag, prompt version, corpus changes and run date. Never commit real customer data.

Use Mermaid-enabled Markdown preview or GitHub to view diagrams. At each gate, explain the design to a peer acting as a skeptical customer. A credible answer identifies evidence, uncertainty and the next test. Use the learning-progress issue template for accountability.
