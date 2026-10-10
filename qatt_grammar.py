"""Validation and cluster segmentation for Quốc Âm Tân Tự (QATT) sequences.

Reference implementation of the encoding model in proposal.md (sections 5 and 6).

Segmentation and validation are separate steps:

* ``segment`` splits text into clusters with local rules only. Whether to break
  between two adjacent code points depends on those two code points and nothing
  else, in the style of UAX #29:

      CanLuoc  x  (any)        Cán Lược behaves like Prepend
      (any)    x  ToneMark     tone marks behave like Extend
      (any)    x  Combiner     never break before the combiner
      Combiner x  (any)        never break after the combiner
      otherwise ÷

  Ill-formed text therefore still segments predictably: a chain such as
  ``CT COMB CT COMB CT`` is one cluster, never re-paired.

* ``validate_cluster`` checks one cluster against the sequence grammar:

      Character := Cluster [ToneMark]
      Cluster   := CanTu | ChiTu | Pair | ThamThu
      Pair      := CanLuoc ChiTu              phản thiết or Hợp Thư
      ThamThu   := HopThu Combiner ChiTu
      HopThu    := CanLuoc(X) ChiTu(X)        same Cán Tự X

  The same-base condition is checked here, not in segmentation.

The block position is not assigned yet ([TBD] in the proposal). ``BLOCK_BASE``
is a provisional stand-in in Supplementary Private Use Area-A so that the module
can run; only the offsets come from the proposal. The order of the eight tone
marks inside +9B..+A2 is not fixed by the proposal either and is provisional.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
import re

BLOCK_BASE = 0xF0000  # provisional, see module docstring

NUM_BASES = 22
NUM_POSITIONS = 5

CAN_TU_OFFSET = 0x00     # +00..+15, 22 code points
CAN_LUOC_OFFSET = 0x16   # +16..+2B, 22 code points
CHI_TU_OFFSET = 0x2C     # +2C..+99, 110 code points, five per base
COMBINER_OFFSET = 0x9A   # +9A
TONE_OFFSET = 0x9B       # +9B..+A2, 8 code points
RESERVED_OFFSET = 0xA3   # +A3..+AF
BLOCK_SIZE = 0xB0        # 176

TONE_SHAPES = ("CIRCLE", "SEMICIRCLE")
TONE_CORNERS = ("UPPER LEFT", "UPPER RIGHT", "LOWER LEFT", "LOWER RIGHT")


class Kind(Enum):
    CAN_TU = "A"
    CAN_LUOC = "L"
    CHI_TU = "C"
    COMBINER = "J"
    TONE = "T"
    OTHER = "O"  # outside the block, or a reserved code point


# Letter codes of Kind, used to match the grammar as a regular expression.
_CLUSTER_RE = re.compile(r"(?:A|C|LC|LCJC)T?")


def can_tu(base: int) -> str:
    _check_base(base)
    return chr(BLOCK_BASE + CAN_TU_OFFSET + base)


def can_luoc(base: int) -> str:
    _check_base(base)
    return chr(BLOCK_BASE + CAN_LUOC_OFFSET + base)


def chi_tu(base: int, position: int) -> str:
    _check_base(base)
    if not 0 <= position < NUM_POSITIONS:
        raise ValueError(f"position must be 0..{NUM_POSITIONS - 1}, got {position}")
    return chr(BLOCK_BASE + CHI_TU_OFFSET + base * NUM_POSITIONS + position)


COMBINER = chr(BLOCK_BASE + COMBINER_OFFSET)


def tone(shape: str, corner: str) -> str:
    return chr(BLOCK_BASE + TONE_OFFSET
               + TONE_SHAPES.index(shape) * len(TONE_CORNERS)
               + TONE_CORNERS.index(corner))


def _check_base(base: int) -> None:
    if not 0 <= base < NUM_BASES:
        raise ValueError(f"base must be 0..{NUM_BASES - 1}, got {base}")


def kind(ch: str) -> Kind:
    offset = ord(ch) - BLOCK_BASE
    if offset < 0 or offset >= RESERVED_OFFSET:
        return Kind.OTHER
    if offset < CAN_LUOC_OFFSET:
        return Kind.CAN_TU
    if offset < CHI_TU_OFFSET:
        return Kind.CAN_LUOC
    if offset < COMBINER_OFFSET:
        return Kind.CHI_TU
    if offset == COMBINER_OFFSET:
        return Kind.COMBINER
    return Kind.TONE


def base_of(ch: str) -> int | None:
    """Index of the Cán Tự a component derives from, or None for other code points."""
    offset = ord(ch) - BLOCK_BASE
    k = kind(ch)
    if k is Kind.CAN_TU:
        return offset - CAN_TU_OFFSET
    if k is Kind.CAN_LUOC:
        return offset - CAN_LUOC_OFFSET
    if k is Kind.CHI_TU:
        return (offset - CHI_TU_OFFSET) // NUM_POSITIONS
    return None


def is_break(before: str, after: str) -> bool:
    """Whether a cluster boundary lies between two adjacent code points."""
    if kind(before) in (Kind.CAN_LUOC, Kind.COMBINER):
        return False
    if kind(after) in (Kind.TONE, Kind.COMBINER):
        return False
    return True


def segment(text: str) -> list[str]:
    """Split text into clusters. Code points outside the block form their own clusters
    unless a QATT rule joins them; other scripts' segmentation rules are not modelled."""
    clusters: list[str] = []
    start = 0
    for i in range(1, len(text)):
        if is_break(text[i - 1], text[i]):
            clusters.append(text[start:i])
            start = i
    if text:
        clusters.append(text[start:])
    return clusters


@dataclass(frozen=True)
class Cluster:
    text: str
    error: str | None  # None when the cluster is well-formed

    @property
    def valid(self) -> bool:
        return self.error is None


def validate_cluster(cluster: str) -> str | None:
    """Return None for a well-formed cluster, otherwise a short description of the problem.

    A cluster made only of code points outside the block is accepted unchanged;
    the grammar applies to QATT clusters.
    """
    kinds = "".join(kind(ch).value for ch in cluster)
    if not kinds:
        return "empty cluster"
    if set(kinds) == {Kind.OTHER.value}:
        return None
    if Kind.OTHER.value in kinds:
        return "QATT code point combined with a code point outside the block"
    if not _CLUSTER_RE.fullmatch(kinds):
        return _describe(kinds)
    if "J" in kinds and base_of(cluster[0]) != base_of(cluster[1]):
        return _NOT_HOP_THU
    return None


_NOT_HOP_THU = "base of a Tham Thư must be a Hợp Thư (Cán Lược and Chi Tự of the same Cán Tự)"


def _describe(kinds: str) -> str:
    if kinds.count("T") > 1:
        return "more than one tone mark"
    if "T" in kinds[:-1]:
        return "tone mark inside a cluster"
    core = kinds.rstrip("T")
    if not core:
        return "tone mark without a base"
    if core.count("J") > 1:
        return "more than one combiner"
    if core.startswith("J") or core.endswith("J"):
        return "combiner without a component on both sides"
    if "A" in core:
        return "Cán Tự combined with other components"
    if core.endswith("L") or "LL" in core or "LJ" in core:
        return "Cán Lược not followed by a Chi Tự"
    if "J" in core and "L" in core.split("J", 1)[1]:
        return "top component of a Tham Thư must be a single Chi Tự"
    if "J" in core and not core.startswith("LCJ"):
        return _NOT_HOP_THU
    return "sequence does not match the grammar"


def analyse(text: str) -> list[Cluster]:
    """Segment text and validate each cluster."""
    return [Cluster(c, validate_cluster(c)) for c in segment(text)]


def is_well_formed(text: str) -> bool:
    return all(c.valid for c in analyse(text))


def is_exchanged(cluster: str) -> bool:
    """Whether the rendering rule of proposal 5.4 applies: the cluster begins with a
    Hợp Thư, a Cán Lược and a Chi Tự of the same Cán Tự."""
    return (len(cluster) >= 2
            and kind(cluster[0]) is Kind.CAN_LUOC
            and kind(cluster[1]) is Kind.CHI_TU
            and base_of(cluster[0]) == base_of(cluster[1]))
