import json
from pathlib import Path

out_dir = Path(__file__).parent
data = json.loads((out_dir / "gpt-5.4-mini_fewshot.json").read_text())

counts: dict[str, dict[str, int]] = {}
for entry in data:
    t = entry["type"]
    if t not in counts:
        counts[t] = {"correct": 0, "total": 0}
    counts[t]["total"] += 1
    if entry["correct"]:
        counts[t]["correct"] += 1

result = {
    t: {
        "correct": v["correct"],
        "total": v["total"],
        "pct_correct": round(v["correct"] / v["total"] * 100, 2) if v["total"] else 0,
    }
    for t, v in counts.items()
}

(out_dir / "result.json").write_text(json.dumps(result, indent=2))
print(json.dumps(result, indent=2))