"""Link the evidence ids (E07) and the page references (p. 6) in the Markdown files.

Usage: python tools/link_refs.py

An id links to its entry, a page number from 1 to 8 to the full page of the
manuscript (Source 1, or Source 2 where the sentence is about Source 2).
Applies to proposal.md, ROADMAP.md, the evidence entries and evidence/README.md.
Code spans and the YAML header of an entry are left alone; running it twice
changes nothing. Run it after writing a new id or page reference in the text.
"""

from __future__ import annotations

from pathlib import Path

import evidence

ROOT = Path(__file__).resolve().parent.parent


def targets() -> list[tuple[Path, str]]:
    files = [(ROOT / "proposal.md", "evidence/"), (ROOT / "ROADMAP.md", "evidence/"),
             (evidence.EVIDENCE / "README.md", "")]
    files += [(p, "") for p in evidence.entry_files()]
    return files


def main() -> None:
    for path, prefix in targets():
        text = path.read_text(encoding="utf-8")
        linked = evidence.link_refs(text, prefix)
        if linked != text:
            path.write_text(linked, encoding="utf-8")


if __name__ == "__main__":
    main()
