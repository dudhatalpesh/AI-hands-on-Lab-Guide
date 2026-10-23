# Frequently asked questions

**Do I need a paid API?** No. The required path uses local inference. Offline tests require only Python.

**Do I need a GPU?** No for these exercises; CPU latency may be high. Start with the small configured model and measure on your hardware.

**Is the offline mode an AI demo?** It is a deterministic application test fixture. It cannot establish model quality or security against model-level attacks.

**Can I use real customer documents?** Keep this training repository synthetic. Any real-data pilot requires explicit customer authorization, appropriate infrastructure and a data-handling review.

**Why plain Python and frameworks?** Plain Python makes trust boundaries visible. Chroma and LangGraph extensions demonstrate common patterns without making a framework necessary for every lesson.

**Are agents always better than workflows?** No. Use an agent only if adaptive action selection yields measured benefit that justifies the added uncertainty and cost.

**Is n8n open source?** Its community distribution uses a source-available fair-code license. Review permitted uses; do not label it OSI open source.

**Does passing the labs certify compliance?** No. Compliance depends on jurisdiction, use, contracts and evidence. Obtain appropriate legal/privacy review.

**Is this ready to expose on the internet?** No. The local API intentionally omits production identity and operational controls. Use the reference architecture to plan those additions.

**Why are dependency ranges used?** They provide a maintainable starting point. Capture and review resolved versions before a workshop or release; the initial scaffold does not claim a validated lockfile.
