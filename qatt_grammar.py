"""Validation and cluster segmentation for Quốc Âm Tân Tự (QATT) sequences.

Reference implementation of the encoding model in proposal.md (sections 5 and 6).
Components are stored in reading order; a Hợp Thư is Chi Tự + Hợp Thư joiner +
Cán Lược, and nothing is reordered.

Segmentation and validation are separate steps:

* ``segment`` splits text into clusters with local rules only, in the style of
  UAX #29. Whether to break between two adjacent code points depends on those two
  code points and, for one rule, the code point before them:

      CanLuoc  x  (any)        Cán Lược behaves like Prepend ...
      HJ CanLuoc ÷ (any)       ... except directly after the Hợp Thư joiner
      (any)    x  ToneMark     tone marks behave like Extend
      (any)    x  Joiner       never break before a joiner (HJ or COMB)
      Joiner   x  (any)        never break after a joiner
      otherwise ÷

  Ill-formed text therefore still segments predictably: a chain such as
  ``CT COMB CT COMB CT`` is one cluster, never re-paired.

* ``validate_cluster`` checks one cluster against the sequence grammar of the
  proposal, which describes the attested forms:

      Character := Cluster [ToneMark]
      Cluster   := CanTu | ChiTu | PhanThiet | HopThu | ThamThu
      PhanThiet := CanLuoc(X) ChiTu(Y)                X ≠ Y
      HopThu    := ChiTu(X) HopThuJoiner CanLuoc(X)   same Cán Tự X
      ThamThu   := HopThu Combiner ChiTu

  With ``extended=True`` it accepts the sequences the proposal leaves
  unprohibited but unattested: any bases in a pair, and a phản thiết pair or a
  single Chi Tự as the base of a Tham Thư.

The block position is not assigned yet ([TBD] in the proposal). ``BLOCK_BASE``
is a provisional stand-in in Supplementary Private Use Area-A so that the module
can run; only the offsets come from the proposal. The order of the eight tone
marks inside +9C..+A3 is not fixed by the proposal either and is provisional.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
import re

BLOCK_BASE = 0xF0000  # provisional, see module docstring

NUM_BASES = 22
NUM_POSITIONS = 5

CAN_TU_OFFSET = 0x00          # +00..+15, 22 code points
CAN_LUOC_OFFSET = 0x16        # +16..+2B, 22 code points
CHI_TU_OFFSET = 0x2C          # +2C..+99, 110 code points, five per base
COMBINER_OFFSET = 0x9A        # +9A, Tham Thư combiner
HOP_THU_JOINER_OFFSET = 0x9B  # +9B
TONE_OFFSET = 0x9C            # +9C..+A3, 8 code points
RESERVED_OFFSET = 0xA4        # +A4..+AF
BLOCK_SIZE = 0xB0             # 176

TONE_SHAPES = ("CIRCLE", "SEMICIRCLE")
TONE_CORNERS = ("UPPER LEFT", "UPPER RIGHT", "LOWER LEFT", "LOWER RIGHT")


class Kind(Enum):
    CAN_TU = "A"
    CAN_LUOC = "L"
    CHI_TU = "C"
    COMBINER = "J"
    HOP_THU_JOINER = "H"
    TONE = "T"
    OTHER = "O"  # outside the block, or a reserved code point


# Letter codes of Kind, used to match the grammar as a regular expression.
_ATTESTED_RE = re.compile(r"(?:A|C|LC|CHL|CHLJC)T?")
_EXTENDED_RE = re.compile(r"(?:A|C|LC|CHL|(?:CHL|LC|C)JC)T?")
_JOINERS = (Kind.COMBINER, Kind.HOP_THU_JOINER)


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
HOP_THU_JOINER = chr(BLOCK_BASE + HOP_THU_JOINER_OFFSET)


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
    if offset == HOP_THU_JOINER_OFFSET:
        return Kind.HOP_THU_JOINER
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


def is_break(prev: str | None, before: str, after: str) -> bool:
    """Whether a cluster boundary lies between `before` and `after`.
    `prev` is the code point before `before`, or None at the start of the text."""
    k_before, k_after = kind(before), kind(after)
    if k_after is Kind.TONE or k_after in _JOINERS or k_before in _JOINERS:
        return False
    if k_before is Kind.CAN_LUOC:
        return prev is not None and kind(prev) is Kind.HOP_THU_JOINER
    return True


def segment(text: str) -> list[str]:
    """Split text into clusters. Code points outside the block form their own clusters
    unless a QATT rule joins them; other scripts' segmentation rules are not modelled."""
    clusters: list[str] = []
    start = 0
    for i in range(1, len(text)):
        prev = text[i - 2] if i >= 2 else None
        if is_break(prev, text[i - 1], text[i]):
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


NOT_HOP_THU_BASE = "base of a Tham Thư must be a Hợp Thư"
SAME_BASE_PHAN_THIET = "same-base phản thiết pair is written as the Chi Tự alone"
MIXED_HOP_THU = "Hợp Thư joins a Chi Tự and a Cán Lược of different Cán Tự"


def validate_cluster(cluster: str, extended: bool = False) -> str | None:
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
    pattern = _EXTENDED_RE if extended else _ATTESTED_RE
    if not pattern.fullmatch(kinds):
        return _describe(kinds, extended)
    if extended:
        return None
    core = kinds.rstrip("T")
    if core == "LC" and base_of(cluster[0]) == base_of(cluster[1]):
        return SAME_BASE_PHAN_THIET
    if core.startswith("CHL") and base_of(cluster[0]) != base_of(cluster[2]):
        return MIXED_HOP_THU
    return None


def _describe(kinds: str, extended: bool) -> str:
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
    if "J" in core and core.split("J", 1)[1] != "C":
        return "top component of a Tham Thư must be a single Chi Tự"
    if core.count("H") > 1:
        return "more than one Hợp Thư joiner"
    for i, k in enumerate(core):
        if k == "H" and not (0 < i < len(core) - 1 and core[i - 1] == "C" and core[i + 1] == "L"):
            return "Hợp Thư joiner must stand between a Chi Tự and a Cán Lược"
    if "A" in core:
        return "Cán Tự combined with other components"
    for i, k in enumerate(core):
        after_joiner = i > 0 and core[i - 1] == "H"
        before_chi_tu = i + 1 < len(core) and core[i + 1] == "C"
        if k == "L" and not (after_joiner or before_chi_tu):
            return "Cán Lược neither followed by a Chi Tự nor joined to a preceding one"
    if "J" in core and not extended and core.split("J", 1)[0] != "CHL":
        return NOT_HOP_THU_BASE
    return "sequence does not match the grammar"


def analyse(text: str, extended: bool = False) -> list[Cluster]:
    """Segment text and validate each cluster."""
    return [Cluster(c, validate_cluster(c, extended)) for c in segment(text)]


def is_well_formed(text: str, extended: bool = False) -> bool:
    return all(c.valid for c in analyse(text, extended))


def is_hop_thu(cluster: str) -> bool:
    """Whether the cluster begins with a Hợp Thư: Chi Tự, Hợp Thư joiner, Cán Lược."""
    return (len(cluster) >= 3
            and kind(cluster[0]) is Kind.CHI_TU
            and kind(cluster[1]) is Kind.HOP_THU_JOINER
            and kind(cluster[2]) is Kind.CAN_LUOC)
