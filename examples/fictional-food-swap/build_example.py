"""Rebuild the fictional example's CSV and dashboard with Python's standard library."""

import csv
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
data_path = HERE / "example-data.json"
template_path = HERE / "../../templates/dashboard.template.html"
if not data_path.is_file():
    raise SystemExit("Missing example-data.json beside build_example.py")
if not template_path.is_file():
    raise SystemExit("Missing ../../templates/dashboard.template.html; keep the skill folder intact")

DATA = json.loads(data_path.read_text(encoding="utf-8"))
COLUMNS = DATA["matrixColumns"]

with (HERE / "research-matrix.csv").open("w", newline="", encoding="utf-8") as output:
    writer = csv.DictWriter(output, fieldnames=COLUMNS, extrasaction="ignore", lineterminator="\n")
    writer.writeheader()
    writer.writerows(DATA["competitors"])

template = template_path.read_text(encoding="utf-8")
assert template.count("__DASHBOARD_DATA__") == 1
payload = json.dumps(DATA, ensure_ascii=False, separators=(",", ":")).replace("<", "\\u003c")
(HERE / "dashboard.html").write_text(
    template.replace("__DASHBOARD_DATA__", payload), encoding="utf-8"
)
