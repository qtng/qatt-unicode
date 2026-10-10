"""Cut the evidence images out of the full pages.

Usage: python tools/make_crops.py

evidence/crops.csv lists, for each image in evidence/images, the page in
evidence/pages it comes from and the box (left, top, right, bottom) in pixels.
"""

from __future__ import annotations

import csv

from PIL import Image

import evidence


def main() -> None:
    with (evidence.EVIDENCE / "crops.csv").open(encoding="utf-8") as f:
        for row in csv.DictReader(f):
            page = Image.open(evidence.EVIDENCE / "pages" / f"{row['page']}.jpg")
            box = tuple(int(row[k]) for k in ("left", "top", "right", "bottom"))
            page.crop(box).save(evidence.EVIDENCE / "images" / row["image"])


if __name__ == "__main__":
    main()
