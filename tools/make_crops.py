"""Cut the evidence images out of the full pages.

Usage: python tools/make_crops.py

evidence/crops.csv lists, for each image in evidence/images, the page in
evidence/pages it comes from and the box (left, top, right, bottom) in pixels.
The optional column `strike` lists boxes (left top right bottom, separated by
semicolons) that are not relevant to the evidence: each is framed with a
rectangle and crossed out with a diagonal cross, so a full page can be shown
with the relevant columns only.
"""

from __future__ import annotations

import csv

from PIL import Image, ImageDraw

import evidence

MARK = (200, 0, 0)
WIDTH = 6


def strike(page: Image.Image, boxes: str) -> None:
    draw = ImageDraw.Draw(page)
    for part in boxes.split(";"):
        left, top, right, bottom = (int(v) for v in part.split())
        draw.rectangle((left, top, right, bottom), outline=MARK, width=WIDTH)
        draw.line((left, top, right, bottom), fill=MARK, width=WIDTH)
        draw.line((left, bottom, right, top), fill=MARK, width=WIDTH)


def main() -> None:
    with (evidence.EVIDENCE / "crops.csv").open(encoding="utf-8") as f:
        for row in csv.DictReader(f):
            page = Image.open(evidence.EVIDENCE / "pages" / f"{row['page']}.jpg").convert("RGB")
            if row.get("strike"):
                strike(page, row["strike"])
            box = tuple(int(row[k]) for k in ("left", "top", "right", "bottom"))
            page.crop(box).save(evidence.EVIDENCE / "images" / row["image"])


if __name__ == "__main__":
    main()
