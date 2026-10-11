"""Read and write the evidence entries in ../evidence (one Markdown file per entry).

Each file starts with a YAML header between --- lines, one `key: value` per line;
text values are double-quoted, list values are written as [a, b]. The body has optional sections
## Transcription, ## Translation and ## Notes, after the images.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

EVIDENCE = Path(__file__).resolve().parent.parent / "evidence"
LIST_FIELDS = ("sections", "source", "image")
QUOTED_FIELDS = ("claim", "location")
HEADER_FIELDS = ("id", "claim", "sections", "source", "page", "location", "image", "status")
BODY_FIELDS = ("transcription", "translation", "notes")
STATUSES = ("missing", "located", "cited")
_ENTRY_NAME = re.compile(r"E\d+[a-z]?\.md")


def entry_files() -> list[Path]:
    return sorted((p for p in EVIDENCE.glob("E*.md") if _ENTRY_NAME.fullmatch(p.name)),
                  key=lambda p: (int(re.sub(r"\D", "", p.stem)), p.stem))


def image_path(image: str) -> str:
    """Path of an image relative to the evidence folder: a cut-out in images/ or a
    full page given as pages/S1-p3.jpg."""
    return image if "/" in image else f"images/{image}"


def parse(text: str) -> dict:
    _, header, body = text.split("---\n", 2)
    entry: dict = {}
    for line in header.splitlines():
        key, _, value = line.partition(":")
        value = value.strip()
        if key in LIST_FIELDS:
            inner = value.strip("[]").strip()
            entry[key] = [v.strip() for v in inner.split(",")] if inner else []
        elif value.startswith('"'):
            entry[key] = json.loads(value)
        else:
            entry[key] = value
    sections = re.split(r"^## (\w+)\n", body, flags=re.M)
    for name, content in zip(sections[1::2], sections[2::2]):
        entry[name.lower()] = content.strip()
    for field in BODY_FIELDS:
        entry.setdefault(field, "")
    return entry


def render(entry: dict) -> str:
    lines = ["---"]
    for key in HEADER_FIELDS:
        value = entry.get(key, [] if key in LIST_FIELDS else "")
        if key in LIST_FIELDS:
            value = "[" + ", ".join(value) + "]"
        elif key in QUOTED_FIELDS and value:
            value = json.dumps(value, ensure_ascii=False)
        lines.append(f"{key}: {value}".rstrip())
    lines += ["---", ""]
    for image, source in zip(entry.get("image", []), entry.get("source", [])):
        lines.append(f"![{source}]({image_path(image)})")
    if entry.get("image"):
        lines.append("")
    for field in BODY_FIELDS:
        if entry.get(field):
            lines += [f"## {field.capitalize()}", "", entry[field], ""]
    return "\n".join(lines)


_CODE = re.compile(r"(```.*?```|`[^`\n]*`)", re.S)
_ID = re.compile(r"(?<![\w\[/.-])(E\d{2}[a-z]?)(?![\w]|-\d|\.md|\.png|\]\()")
_PAGES = re.compile(r"(?<![\w])([Pp]p?\.) ?([1-8])(?:([–-])([1-8]))?(?!\d)")


def _page_link(text: str, start: int, number: str, prefix: str) -> str:
    """Link to the full page of Source 1, or of Source 2 where the sentence is about Source 2."""
    window = text[max(0, start - 160):start]
    for stop in (". ", "; ", "\n"):
        window = window.rpartition(stop)[2]
    source = "S2" if "Source 2" in window and "Source 1" not in window else "S1"
    return f"[{number}]({prefix}pages/{source}-p{number}.jpg)"


def link_refs(text: str, prefix: str = "") -> str:
    """Link entry ids (E07 -> [E07](<prefix>E07.md)) and page references
    (p. 6 -> p. [6](<prefix>pages/S1-p6.jpg), pp. 3-4 likewise) to their targets.

    Page numbers 1 to 8 are pages of the manuscripts; other numbers, for example
    pages of a dictionary, are not linked. Code spans and code blocks are left
    alone, and so is the YAML header of an entry. Linking twice changes nothing."""
    head = ""
    if text.startswith("---\n"):
        _, header, body = text.split("---\n", 2)
        head, text = "---\n" + header + "---\n", body

    def pages(m: re.Match, whole: str) -> str:
        first = _page_link(whole, m.start(), m.group(2), prefix)
        out = f"{m.group(1)} {first}"
        if m.group(4):
            out += m.group(3) + _page_link(whole, m.start(), m.group(4), prefix)
        return out

    parts = _CODE.split(text)
    offset = 0
    for i in range(len(parts)):
        if i % 2 == 0:
            segment = parts[i]
            segment = _ID.sub(lambda m: f"[{m.group(1)}]({prefix}{m.group(1)}.md)", segment)
            segment = _PAGES.sub(lambda m, s=segment: pages(m, s), segment)
            parts[i] = segment
    return head + "".join(parts)


link_ids = link_refs  # earlier name


def load() -> list[dict]:
    return [parse(p.read_text(encoding="utf-8")) for p in entry_files()]


def save(entry: dict) -> None:
    (EVIDENCE / f"{entry['id']}.md").write_text(render(entry), encoding="utf-8")
