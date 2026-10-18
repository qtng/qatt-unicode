"""Validation and cluster segmentation for Quốc Âm Tân Tự (QATT) sequences.

Reference implementation of the encoding model in proposal.md (sections 5 and 6).
Components are stored in reading order and nothing is reordered. Every
combination is written with an explicit joiner; components without a joiner are
separate characters.

Segmentation and validation are separate steps:

* ``segment`` splits text into clusters with pairwise rules only, in the style
  of UAX #29. Whether to break between two adjacent code points depends on those
  two code points and nothing else:

      (any)    x  ToneMark     tone marks behave like Extend
      (any)    x  Joiner       never break before a joiner (JOIN or COMB)
      Joiner   x  (any)        never break after a joiner
      otherwise ÷

  Ill-formed text therefore still segments predictably: a chain such as
  ``CH COMB CH COMB CH`` is one cluster, never re-paired.

* ``validate_cluster`` checks one cluster against the sequence grammar of the
  proposal, which describes the attested forms:

      Character := Cluster [ToneMark]
      Cluster   := MarkedCan | Chi | UnmarkedCan | PhanThiet | HopThu | ThamThu
      PhanThiet := UnmarkedCan(X) Joiner Chi(Y)     X ≠ Y
      HopThu    := Chi(X) Joiner UnmarkedCan(X)     same Cán X
      ThamThu   := HopThu Combiner Chi

  With ``extended=True`` it accepts the sequences the proposal leaves
  unprohibited but unattested: any bases in a pair, and a phản thiết pair or a
  single Chi as the base of a Tham Thư.

The block position is not assigned yet ([TBD] in the proposal). ``BLOCK_BASE``
is a provisional stand-in in Supplementary Private Use Area-A so that the module
can run; only the offsets come from the proposal.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
import re

BLOCK_BASE = 0xF0000  # provisional, see module docstring

NUM_BASES = 22
NUM_POSITIONS = 5   # Chi per base

NUM_MARKED = 6                # marking-stroke positions, counted counter-clockwise from the start position
FORMS_PER_BASE = NUM_MARKED + 1   # form 0: unmarked (no marking stroke); forms 1..6: MARKED-1 .. MARKED-6
# +00..+99: 154 code points, seven consecutive forms per base in source order
JOINER_OFFSET = 0x9A          # +9A, component joiner
COMBINER_OFFSET = 0x9B        # +9B, Tham Thư combiner
TONE_OFFSET = 0x9C            # +9C..+A3, 8 code points
RESERVED_OFFSET = 0xA4        # +A4..+AF
BLOCK_SIZE = 0xB0             # 176

# Names of the 22 Cán in source order (Source 1, p. 2, section 幹音二十二字),
# as used in character names; each form of a base takes the name of its Cán.
CAN_NAMES = ("ONG", "NGONG", "HONG", "GONG", "CONG", "LONG", "TRONG", "DDONG",
                "NONG", "TONG", "THONG", "NHONG", "CHONG", "DZONG", "XONG", "KHONG",
                "SONG", "RONG", "MONG", "BONG", "VONG", "PHONG")

# Tone marks in code point order (proposal 4.4 and 7), the traditional order of
# the eight tones: by tone class (bình, thượng, khứ, nhập; corners lower left,
# upper left, upper right, lower right), âm (semicircle) before dương (circle).
TONE_CORNERS = ("LOWER LEFT", "UPPER LEFT", "UPPER RIGHT", "LOWER RIGHT")
TONE_SHAPES = ("SEMICIRCLE", "CIRCLE")
TONE_NAMES = {
    ("SEMICIRCLE", "LOWER LEFT"): "âm bình (ngang)",
    ("CIRCLE", "LOWER LEFT"): "dương bình (huyền)",
    ("SEMICIRCLE", "UPPER LEFT"): "âm thượng (hỏi)",
    ("CIRCLE", "UPPER LEFT"): "dương thượng (ngã)",
    ("SEMICIRCLE", "UPPER RIGHT"): "âm khứ (sắc)",
    ("CIRCLE", "UPPER RIGHT"): "dương khứ (nặng)",
    ("SEMICIRCLE", "LOWER RIGHT"): "âm nhập",
    ("CIRCLE", "LOWER RIGHT"): "dương nhập",
}


class Kind(Enum):
    MARKED_CAN = "M"
    UNMARKED = "U"
    CHI = "C"
    COMBINER = "J"
    JOINER = "H"
    TONE = "T"
    OTHER = "O"  # outside the block, or a reserved code point


# Letter codes of Kind, used to match the grammar as a regular expression.
_ATTESTED_RE = re.compile(r"(?:M|C|U|UHC|CHU|CHUJC)T?")
_EXTENDED_RE = re.compile(r"(?:M|C|U|UHC|CHU|(?:CHU|UHC|C)JC)T?")
_JOINERS = (Kind.COMBINER, Kind.JOINER)


def unmarked(base: int) -> str:
    _check_base(base)
    return chr(BLOCK_BASE + base * FORMS_PER_BASE)


def marked(base: int, n: int) -> str:
    """The form of a base with the marking stroke at position n, 1 to 6."""
    _check_base(base)
    if not 1 <= n <= NUM_MARKED:
        raise ValueError(f"marking-stroke position must be 1..{NUM_MARKED}, got {n}")
    return chr(BLOCK_BASE + base * FORMS_PER_BASE + n)


def marked_can(base: int) -> str:
    """The marked Cán of a base: the marked form at position 1."""
    return marked(base, 1)


def chi(base: int, position: int) -> str:
    """A Chi of a base, position 0..4: the marked forms at positions 2 to 6."""
    if not 0 <= position < NUM_POSITIONS:
        raise ValueError(f"position must be 0..{NUM_POSITIONS - 1}, got {position}")
    return marked(base, position + 2)


COMBINER = chr(BLOCK_BASE + COMBINER_OFFSET)
JOINER = chr(BLOCK_BASE + JOINER_OFFSET)


def tone(shape: str, corner: str) -> str:
    return chr(BLOCK_BASE + TONE_OFFSET
               + TONE_CORNERS.index(corner) * len(TONE_SHAPES)
               + TONE_SHAPES.index(shape))


def _check_base(base: int) -> None:
    if not 0 <= base < NUM_BASES:
        raise ValueError(f"base must be 0..{NUM_BASES - 1}, got {base}")


def kind(ch: str) -> Kind:
    offset = ord(ch) - BLOCK_BASE
    if offset < 0 or offset >= RESERVED_OFFSET:
        return Kind.OTHER
    if offset < JOINER_OFFSET:
        form = offset % FORMS_PER_BASE
        return Kind.UNMARKED if form == 0 else Kind.MARKED_CAN if form == 1 else Kind.CHI
    if offset == JOINER_OFFSET:
        return Kind.JOINER
    if offset == COMBINER_OFFSET:
        return Kind.COMBINER
    return Kind.TONE


def base_of(ch: str) -> int | None:
    """Index of the Cán a component derives from, or None for other code points."""
    if kind(ch) in (Kind.UNMARKED, Kind.MARKED_CAN, Kind.CHI):
        return (ord(ch) - BLOCK_BASE) // FORMS_PER_BASE
    return None


def marked_position(ch: str) -> int | None:
    """Position of the marking stroke, 1 to 6, or None for other code points."""
    if kind(ch) in (Kind.MARKED_CAN, Kind.CHI):
        return (ord(ch) - BLOCK_BASE) % FORMS_PER_BASE
    return None


def is_break(before: str, after: str) -> bool:
    """Whether a cluster boundary lies between two adjacent code points."""
    k_before, k_after = kind(before), kind(after)
    return not (k_after is Kind.TONE or k_after in _JOINERS or k_before in _JOINERS)


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


NOT_HOP_THU_BASE = "base of a Tham Thư must be a Hợp Thư"
SAME_BASE_PHAN_THIET = "same-base phản thiết pair is written as the Chi alone"
MIXED_HOP_THU = "Hợp Thư joins a Chi and an unmarked Cán of different Cán"
NOT_JOINED = "components must be combined with the component joiner"


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
    if core == "UHC" and base_of(cluster[0]) == base_of(cluster[2]):
        return SAME_BASE_PHAN_THIET
    if core.startswith("CHU") and base_of(cluster[0]) != base_of(cluster[2]):
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
        return "top component of a Tham Thư must be a single Chi"
    if core.count("H") > 1:
        return "more than one component joiner"
    for i, k in enumerate(core):
        if k == "H" and (i == 0 or core[i - 1:i + 2] not in ("CHU", "UHC")):
            return "component joiner must stand between a Chi and an unmarked Cán"
    if "M" in core:
        return "marked Cán combined with other components"
    if "U" in core and "H" not in core:
        return NOT_JOINED
    if "J" in core and not extended and core.split("J", 1)[0] != "CHU":
        return NOT_HOP_THU_BASE
    return "sequence does not match the grammar"


def analyse(text: str, extended: bool = False) -> list[Cluster]:
    """Segment text and validate each cluster."""
    return [Cluster(c, validate_cluster(c, extended)) for c in segment(text)]


def is_well_formed(text: str, extended: bool = False) -> bool:
    return all(c.valid for c in analyse(text, extended))


def character_name(ch: str) -> str | None:
    """Proposed Unicode character name (proposal 7.1), or None outside the encoded repertoire."""
    offset = ord(ch) - BLOCK_BASE
    k = kind(ch)
    prefix = "QUOC AM TAN TU "
    if k is Kind.UNMARKED:
        return prefix + CAN_NAMES[base_of(ch)] + " UNMARKED"
    if k in (Kind.MARKED_CAN, Kind.CHI):
        return prefix + f"{CAN_NAMES[base_of(ch)]} MARKED-{marked_position(ch)}"
    if k is Kind.COMBINER:
        return prefix + "THAM THU COMBINER"
    if k is Kind.JOINER:
        return prefix + "COMPONENT JOINER"
    if k is Kind.TONE:
        index = offset - TONE_OFFSET
        corner = TONE_CORNERS[index // len(TONE_SHAPES)]
        shape = TONE_SHAPES[index % len(TONE_SHAPES)]
        return prefix + f"TONE {shape} {corner}"
    return None


def is_hop_thu(cluster: str) -> bool:
    """Whether the cluster begins with a Hợp Thư: Chi, joiner, unmarked Cán."""
    return _starts_with(cluster, Kind.CHI, Kind.JOINER, Kind.UNMARKED)


def is_phan_thiet(cluster: str) -> bool:
    """Whether the cluster begins with a phản thiết pair: unmarked Cán, joiner, Chi."""
    return _starts_with(cluster, Kind.UNMARKED, Kind.JOINER, Kind.CHI)


def _starts_with(cluster: str, *kinds: Kind) -> bool:
    return len(cluster) >= len(kinds) and all(kind(c) is k for c, k in zip(cluster, kinds))
