"""Link every bare evidence id (E07) in the Markdown files to its entry.

Usage: python tools/link_ids.py

Applies to proposal.md, ROADMAP.md, the evidence entries and evidence/README.md.
Code spans and the YAML header of an entry are left alone; running it twice
changes nothing. Run it after writing a new id in the text.
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
        linked = evidence.link_ids(text, prefix)
        if linked != text:
            path.write_text(linked, encoding="utf-8")


if __name__ == "__main__":
    main()
