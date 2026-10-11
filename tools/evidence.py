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


def link_ids(text: str, prefix: str = "") -> str:
    """Turn every bare entry id (E07) into a link ([E07](<prefix>E07.md)).

    Code spans and code blocks are left alone, and so is the YAML header of an
    entry. Linking twice changes nothing."""
    head = ""
    if text.startswith("---\n"):
        _, header, body = text.split("---\n", 2)
        head, text = "---\n" + header + "---\n", body
    parts = _CODE.split(text)
    for i in range(0, len(parts), 2):
        parts[i] = _ID.sub(lambda m: f"[{m.group(1)}]({prefix}{m.group(1)}.md)", parts[i])
    return head + "".join(parts)


def load() -> list[dict]:
    return [parse(p.read_text(encoding="utf-8")) for p in entry_files()]


def save(entry: dict) -> None:
    (EVIDENCE / f"{entry['id']}.md").write_text(render(entry), encoding="utf-8")
