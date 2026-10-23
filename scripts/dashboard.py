"""Read metadata traces; no model calls from this dashboard."""
import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import streamlit as st  # noqa: E402
from src.advisor.core import ARTIFACTS  # noqa: E402

st.title("AI advisor lab observability")
st.caption("Generation latency only. Offline and live measurements are kept separate.")
path = ARTIFACTS / "events.jsonl"
if not path.exists():
    st.info("Run lab 10 first to create traces.")
    st.stop()
events = [json.loads(line) for line in path.read_text().splitlines() if line.strip()]
mode = st.selectbox("Mode", ["live", "offline"])
selected = [event for event in events if event["mode"] == mode]
st.metric("Recorded calls", len(selected))
if selected:
    st.line_chart([event["latency_ms"] for event in selected])
    st.dataframe(selected)
st.warning("No dollar estimate is inferred from token counts. Add an explicit dated rate card.")
