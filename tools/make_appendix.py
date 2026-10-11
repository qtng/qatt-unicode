"""Fill Appendix B of proposal.md and the overview in evidence/README.md from the
evidence entries (evidence/E*.md).

Usage: python tools/make_appendix.py

Both tables are written between <!-- …:start --> and <!-- …:end --> markers.
"""

from __future__ import annotations

from pathlib import Path

import evidence

ROOT = Path(__file__).resolve().parent.parent


def page_key(entry):
    return (int(entry["page"]) if entry["page"].isdigit() else 999, entry["id"])


def cell(text: str) -> str:
    return text.replace("|", "\\|").replace("\n", " ")


def page_link(page: str) -> str:
    return f"[{page}](pages/S1-p{page}.jpg)" if page else "–"


def appendix_b(entries) -> str:
    located = [e for e in entries if e["status"] != "missing" and e["page"]]
    lines = ["Passages located in the source, by page. Page references are to Source 1 (section 3); images are in the evidence catalogue.",
             "",
             "| Page | Passage | Shows | Status |",
             "| --- | --- | --- | --- |"]
    for e in sorted(located, key=page_key):
        lines.append(f"| [{e['page']}](evidence/pages/S1-p{e['page']}.jpg) | {cell(e['transcription']) or '–'} | {cell(e['claim'])} ({e['id']}) | {e['status']} |")
    return evidence.link_refs("\n".join(lines), "evidence/")


def overview(entries) -> str:
    lines = ["| Entry | Claim | Sections | Page | Status |", "| --- | --- | --- | --- | --- |"]
    for e in entries:
        lines.append(f"| [{e['id']}]({e['id']}.md) | {cell(e['claim'])} | {', '.join(e['sections'])} | {page_link(e['page'])} | {e['status']} |")
    return evidence.link_refs("\n".join(lines))


def fill(path: Path, marker: str, content: str) -> None:
    start, end = f"<!-- {marker}:start -->", f"<!-- {marker}:end -->"
    text = path.read_text(encoding="utf-8")
    head, rest = text.split(start, 1)
    _, tail = rest.split(end, 1)
    path.write_text(f"{head}{start}\n{content}\n{end}{tail}", encoding="utf-8")


def main() -> None:
    entries = evidence.load()
    fill(ROOT / "proposal.md", "appendix-b", appendix_b(entries))
    fill(evidence.EVIDENCE / "README.md", "overview", overview(entries))


if __name__ == "__main__":
    main()
