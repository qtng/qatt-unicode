"""Fill Appendix B of proposal.md from evidence/catalog.csv.

Usage: python tools/make_appendix.py

Writes a table of every catalogue entry with a located page between the
markers <!-- appendix-b:start --> and <!-- appendix-b:end -->.
"""

from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROPOSAL = ROOT / "proposal.md"
CATALOG = ROOT / "evidence" / "catalog.csv"
START, END = "<!-- appendix-b:start -->", "<!-- appendix-b:end -->"


def page_key(row):
    first = row["page"].split(";")[0].strip()
    return (int(first) if first.isdigit() else 999, row["id"])


def table() -> str:
    rows = [r for r in csv.DictReader(CATALOG.open(encoding="utf-8")) if r["status"] != "missing" and r["page"]]
    lines = ["Passages located in the source, by page. Page references are to Source 2 (section 3); images are in the evidence catalogue.",
             "",
             "| Page | Passage | Shows | Status |",
             "| --- | --- | --- | --- |"]
    for r in sorted(rows, key=page_key):
        passage = r["transcription"].replace("|", "\\|") or "–"
        lines.append(f"| {r['page'].split(';')[0].strip()} | {passage} | {r['claim']} ({r['id']}) | {r['status']} |")
    return "\n".join(lines)


def main() -> None:
    text = PROPOSAL.read_text(encoding="utf-8")
    head, rest = text.split(START, 1)
    _, tail = rest.split(END, 1)
    PROPOSAL.write_text(f"{head}{START}\n{table()}\n{END}{tail}", encoding="utf-8")


if __name__ == "__main__":
    main()
