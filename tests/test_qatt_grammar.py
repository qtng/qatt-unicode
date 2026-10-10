import itertools
import re

import pytest
from hypothesis import given, settings, strategies as st

import qatt_grammar as q
from qatt_grammar import COMBINER, Kind, can_luoc, can_tu, chi_tu, tone

CT = chi_tu
CL = can_luoc
COMB = COMBINER
TONE = tone("CIRCLE", "UPPER LEFT")
HAN = "字"


# --- Block layout (proposal section 7) ---------------------------------------

def test_block_layout_counts():
    counts = {}
    for offset in range(q.BLOCK_SIZE):
        k = q.kind(chr(q.BLOCK_BASE + offset))
        counts[k] = counts.get(k, 0) + 1
    assert counts == {Kind.CAN_TU: 22, Kind.CAN_LUOC: 22, Kind.CHI_TU: 110,
                      Kind.COMBINER: 1, Kind.TONE: 8, Kind.OTHER: 13}
    assert sum(v for k, v in counts.items() if k is not Kind.OTHER) == 163


def test_offsets():
    assert ord(can_tu(0)) - q.BLOCK_BASE == 0x00
    assert ord(can_tu(21)) - q.BLOCK_BASE == 0x15
    assert ord(can_luoc(0)) - q.BLOCK_BASE == 0x16
    assert ord(can_luoc(21)) - q.BLOCK_BASE == 0x2B
    assert ord(chi_tu(0, 0)) - q.BLOCK_BASE == 0x2C
    assert ord(chi_tu(21, 4)) - q.BLOCK_BASE == 0x99
    assert ord(COMB) - q.BLOCK_BASE == 0x9A
    tones = {tone(s, c) for s in q.TONE_SHAPES for c in q.TONE_CORNERS}
    assert {ord(t) - q.BLOCK_BASE for t in tones} == set(range(0x9B, 0xA3))


def test_base_of():
    assert q.base_of(can_tu(7)) == 7
    assert q.base_of(can_luoc(7)) == 7
    assert all(q.base_of(chi_tu(7, p)) == 7 for p in range(5))
    assert q.base_of(COMB) is None
    assert q.base_of(HAN) is None


def test_constructors_reject_out_of_range():
    with pytest.raises(ValueError):
        can_tu(22)
    with pytest.raises(ValueError):
        chi_tu(0, 5)


# --- Counts from proposal 5.2 ------------------------------------------------

MULTIPLICITY = {"A": 22, "L": 22, "C": 110, "J": 1, "T": 8}


def count_well_formed(with_tone):
    pattern = re.compile(q._CLUSTER_RE.pattern)
    total = 0
    for n in range(1, 6):
        for kinds in itertools.product("ALCJT", repeat=n):
            s = "".join(kinds)
            if ("T" in s) != with_tone or not pattern.fullmatch(s):
                continue
            m = 1
            for k in s:
                m *= MULTIPLICITY[k]
            total += m
    return total


def test_cluster_counts_match_proposal():
    hop_thu = 22 * 110
    tham_thu = (hop_thu + 110) * 110
    assert hop_thu == 2_420
    assert tham_thu == 278_300
    untoned = count_well_formed(with_tone=False)
    assert untoned == 22 + 110 + hop_thu + tham_thu
    assert count_well_formed(with_tone=True) == untoned * 8


# --- Sequences from proposal 5.3 ---------------------------------------------

WELL_FORMED = {
    "standalone Cán Tự": can_tu(3),
    "standalone Chi Tự": CT(3, 1),
    "Hợp Thư, different bases": CL(3) + CT(5, 2),
    "Hợp Thư, same base": CL(3) + CT(3, 2),
    "Tham Thư on a Hợp Thư": CL(3) + CT(5, 2) + COMB + CT(9, 0),
    "Tham Thư on a single Chi Tự": CT(3, 1) + COMB + CT(9, 0),
    "Cán Tự with tone": can_tu(3) + TONE,
    "Tham Thư with tone": CL(3) + CT(3, 2) + COMB + CT(9, 0) + TONE,
}


@pytest.mark.parametrize("name", WELL_FORMED)
def test_well_formed_cluster(name):
    seq = WELL_FORMED[name]
    assert q.segment(seq) == [seq]
    assert q.validate_cluster(seq) is None


ILL_FORMED = [
    (CL(3), "Cán Lược not followed by a Chi Tự"),
    (CL(3) + can_tu(4), "Cán Tự combined with other components"),
    (CL(3) + CL(4) + CT(4, 0), "Cán Lược not followed by a Chi Tự"),
    (CT(1, 0) + COMB, "combiner without a component on both sides"),
    (COMB + CT(1, 0), "combiner without a component on both sides"),
    (CT(1, 0) + COMB + CL(2) + CT(2, 0), "top component of a Tham Thư must be a single Chi Tự"),
    (CT(1, 0) + COMB + CT(2, 0) + COMB + CT(3, 0), "more than one combiner"),
    (can_tu(1) + COMB + CT(2, 0), "Cán Tự combined with other components"),
    (CT(1, 0) + TONE + COMB + CT(2, 0), "tone mark inside a cluster"),
    (CT(1, 0) + TONE + TONE, "more than one tone mark"),
    (TONE, "tone mark without a base"),
    (HAN + TONE, "QATT code point combined with a code point outside the block"),
]


@pytest.mark.parametrize("seq,reason", ILL_FORMED)
def test_ill_formed_cluster(seq, reason):
    assert q.segment(seq) == [seq], "each case must segment as a single cluster"
    assert q.validate_cluster(seq) == reason


def test_ill_formed_chain_is_one_cluster():
    chain = CT(1, 0) + COMB + CT(2, 0) + COMB + CT(3, 0) + COMB + CT(4, 0)
    [cluster] = q.analyse(chain)
    assert not cluster.valid


def test_mixed_text():
    text = HAN + CL(0) + CT(1, 1) + TONE + CT(2, 2) + HAN
    assert q.segment(text) == [HAN, CL(0) + CT(1, 1) + TONE, CT(2, 2), HAN]
    assert q.is_well_formed(text)


def test_adjacent_chi_tu_are_separate_clusters():
    assert q.segment(CT(1, 0) + CT(1, 0)) == [CT(1, 0), CT(1, 0)]


def test_exchange_rule_detection():
    assert q.is_exchanged(CL(3) + CT(3, 4))
    assert q.is_exchanged(CL(3) + CT(3, 4) + COMB + CT(8, 0))
    assert not q.is_exchanged(CL(3) + CT(4, 4))
    assert not q.is_exchanged(CT(3, 4))


def test_examples_from_section_5_5():
    # Deleting the top component of a Tham Thư merges the next Chi Tự into it.
    x, z, w = CT(1, 0), CT(2, 0), CT(3, 0)
    assert q.segment(x + COMB + z + w) == [x + COMB + z, w]
    assert q.segment(x + COMB + w) == [x + COMB + w]
    # Deleting the combiner splits the cluster.
    assert q.segment(x + z) == [x, z]


# --- Properties --------------------------------------------------------------

ALPHABET = ([can_tu(b) for b in range(22)] + [can_luoc(b) for b in range(22)]
            + [chi_tu(b, p) for b in range(22) for p in range(5)]
            + [COMB] + [tone(s, c) for s in q.TONE_SHAPES for c in q.TONE_CORNERS]
            + [chr(q.BLOCK_BASE + 0xA3), HAN, " "])

# Skewed towards the code points that join, so long clusters and chains are common.
code_points = st.one_of(
    st.sampled_from(ALPHABET),
    st.sampled_from([COMB, CL(0), CL(5), TONE, CT(0, 0), CT(5, 3)]),
)
texts = st.lists(code_points, max_size=30).map("".join)


def spans(text):
    out, start = [], 0
    for cluster in q.segment(text):
        out.append((start, start + len(cluster)))
        start += len(cluster)
    return out


def assert_only_neighbours_change(old, new, edit_at, touched, shift):
    """Every old cluster that contains none of the `touched` positions must appear,
    shifted by `shift` if it lies after the edit, as a cluster of the new text."""
    new_spans = set(spans(new))
    for s, e in spans(old):
        if any(s <= t < e for t in touched):
            continue
        moved = (s, e) if e <= edit_at else (s + shift, e + shift)
        assert moved in new_spans, (old, new, (s, e))


@settings(max_examples=2000)
@given(texts, st.data())
def test_insertion_changes_only_adjacent_clusters(text, data):
    p = data.draw(st.integers(0, len(text)))
    ch = data.draw(code_points)
    new = text[:p] + ch + text[p:]
    assert_only_neighbours_change(text, new, p, touched=(p - 1, p), shift=1)


@settings(max_examples=2000)
@given(texts.filter(bool), st.data())
def test_deletion_changes_only_adjacent_clusters(text, data):
    p = data.draw(st.integers(0, len(text) - 1))
    new = text[:p] + text[p + 1:]
    assert_only_neighbours_change(text, new, p, touched=(p - 1, p, p + 1), shift=-1)


@given(texts)
def test_segment_concatenates_to_input(text):
    assert "".join(q.segment(text)) == text


def well_formed_cluster():
    ct = st.builds(chi_tu, st.integers(0, 21), st.integers(0, 4))
    cl = st.builds(can_luoc, st.integers(0, 21))
    ca = st.builds(can_tu, st.integers(0, 21))
    hop = st.tuples(cl, ct).map("".join)
    tham = st.tuples(st.one_of(hop, ct), ct).map(lambda t: t[0] + COMB + t[1])
    core = st.one_of(ca, ct, hop, tham)
    tones = st.sampled_from([""] + [tone(s, c) for s in q.TONE_SHAPES for c in q.TONE_CORNERS])
    return st.tuples(core, tones).map("".join)


@given(st.lists(well_formed_cluster(), max_size=15))
def test_well_formed_text_segments_into_its_clusters(clusters):
    text = "".join(clusters)
    assert q.segment(text) == clusters
    assert q.is_well_formed(text)
