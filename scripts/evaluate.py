"""A seed evaluation set, not a production benchmark or untouched holdout."""
import argparse
import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src.advisor.core import ARTIFACTS, ROOT, Model, rag  # noqa: E402

parser = argparse.ArgumentParser()
parser.add_argument("--offline", action="store_true")
args = parser.parse_args()
model = Model(args.offline)
cases = json.loads((ROOT / "data/evaluation.json").read_text())
rows = []
for case in cases:
    started = time.perf_counter()
    result = rag(case["question"], case["tenant"], model)
    expected = case.get("expected_source")
    rows.append({
        "id": case["id"],
        "mode": "offline" if args.offline else "live",
        "end_to_end_ms": round((time.perf_counter() - started) * 1000, 2),
        "source_hit": expected in result["sources"] if expected else None,
        "forbidden_source_absent": case.get("forbidden_source") not in result["sources"],
        "empty_sources_as_expected": not result["sources"]
        if case.get("expect_no_sources") else None,
        "expect_abstention": case.get("expect_abstention", False),
        "answer": result["answer"],
        "sources": result["sources"],
        "human_correctness": None,
        "human_groundedness": None,
        "human_abstention_correct": None,
    })
ARTIFACTS.mkdir(exist_ok=True)
target = ARTIFACTS / "evaluation.json"
target.write_text(json.dumps(rows, indent=2), encoding="utf-8")
hits = [row["source_hit"] for row in rows if row["source_hit"] is not None]
print(json.dumps({
    "mode": "offline" if args.offline else "live",
    "expected_source_hit_rate_at_2": sum(hits) / len(hits),
    "case_count": len(rows),
    "report": str(target),
    "human_review": "Score correctness, groundedness and abstention before claiming quality.",
}, indent=2))
