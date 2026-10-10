import itertools

import pytest
from hypothesis import given, settings, strategies as st

import qatt_grammar as q
from qatt_grammar import COMBINER, HOP_THU_JOINER, Kind, can_luoc, can_tu, chi_tu, tone

CT = chi_tu
CL = can_luoc
COMB = COMBINER
HJ = HOP_THU_JOINER
TONE = tone("CIRCLE", "UPPER LEFT")
HAN = "字"


def hop(base, position=0):
    return CT(base, position) + HJ + CL(base)


# --- Block layout (proposal section 7) ---------------------------------------

def test_block_layout_counts():
    counts = {}
    for offset in range(q.BLOCK_SIZE):
        k = q.kind(chr(q.BLOCK_BASE + offset))
        counts[k] = counts.get(k, 0) + 1
    assert counts == {Kind.CAN_TU: 22, Kind.CAN_LUOC: 22, Kind.CHI_TU: 110,
                      Kind.COMBINER: 1, Kind.HOP_THU_JOINER: 1, Kind.TONE: 8,
                      Kind.OTHER: 12}
    assert sum(v for k, v in counts.items() if k is not Kind.OTHER) == 164


def test_offsets():
    assert ord(can_tu(0)) - q.BLOCK_BASE == 0x00
    assert ord(can_tu(21)) - q.BLOCK_BASE == 0x15
    assert ord(can_luoc(0)) - q.BLOCK_BASE == 0x16
    assert ord(can_luoc(21)) - q.BLOCK_BASE == 0x2B
    assert ord(chi_tu(0, 0)) - q.BLOCK_BASE == 0x2C
    assert ord(chi_tu(21, 4)) - q.BLOCK_BASE == 0x99
    assert ord(COMB) - q.BLOCK_BASE == 0x9A
    assert ord(HJ) - q.BLOCK_BASE == 0x9B
    tones = {tone(s, c) for s in q.TONE_SHAPES for c in q.TONE_CORNERS}
    assert {ord(t) - q.BLOCK_BASE for t in tones} == set(range(0x9C, 0xA4))


def test_base_of():
    assert q.base_of(can_tu(7)) == 7
    assert q.base_of(can_luoc(7)) == 7
    assert all(q.base_of(chi_tu(7, p)) == 7 for p in range(5))
    assert q.base_of(COMB) is None
    assert q.base_of(HJ) is None
    assert q.base_of(HAN) is None


def test_constructors_reject_out_of_range():
    with pytest.raises(ValueError):
        can_tu(22)
    with pytest.raises(ValueError):
        chi_tu(0, 5)


# --- Counts from proposal 5.2 ------------------------------------------------

ALL_CAN_TU = [can_tu(b) for b in range(22)]
ALL_CAN_LUOC = [can_luoc(b) for b in range(22)]
ALL_CHI_TU = [chi_tu(b, p) for b in range(22) for p in range(5)]


def count_valid(sequences, extended=False):
    return sum(q.validate_cluster("".join(seq), extended) is None for seq in sequences)


def test_two_component_counts_match_proposal():
    phan_thiet = list(itertools.product(ALL_CAN_LUOC, ALL_CHI_TU))
    hop_thu = list(itertools.product(ALL_CHI_TU, [HJ], ALL_CAN_LUOC))
    assert count_valid(phan_thiet) == 2_310
    assert count_valid(hop_thu) == 110
    assert count_valid(phan_thiet) + count_valid(hop_thu) == 2_420


def test_tham_thu_count_matches_proposal():
    on_hop_thu = itertools.product(ALL_CHI_TU, [HJ], ALL_CAN_LUOC, [COMB], ALL_CHI_TU)
    assert count_valid(on_hop_thu) == 110 * 110 == 12_100


def test_every_cluster_takes_any_of_eight_tones():
    tones = [tone(s, c) for s in q.TONE_SHAPES for c in q.TONE_CORNERS]
    samples = [ALL_CAN_TU[0], ALL_CHI_TU[0], CL(1) + CT(2, 0), hop(1), hop(1) + COMB + CT(3, 0)]
    assert count_valid((s, t) for s in samples for t in tones) == len(samples) * 8


# --- Sequences from proposal 5.3 ---------------------------------------------

WELL_FORMED = {
    "standalone Cán Tự": can_tu(3),
    "standalone Chi Tự": CT(3, 1),
    "phản thiết pair": CL(3) + CT(5, 2),
    "Hợp Thư": hop(3, 2),
    "Tham Thư": hop(3, 2) + COMB + CT(9, 0),
    "Cán Tự with tone": can_tu(3) + TONE,
    "Tham Thư with tone": hop(3, 2) + COMB + CT(9, 0) + TONE,
}


@pytest.mark.parametrize("name", WELL_FORMED)
def test_well_formed_cluster(name):
    seq = WELL_FORMED[name]
    assert q.segment(seq) == [seq]
    assert q.validate_cluster(seq) is None
    assert q.validate_cluster(seq, extended=True) is None


ILL_FORMED = [
    (CL(3), "Cán Lược neither followed by a Chi Tự nor joined to a preceding one"),
    (CL(3) + can_tu(4), "Cán Tự combined with other components"),
    (CL(3) + CL(4) + CT(4, 0), "Cán Lược neither followed by a Chi Tự nor joined to a preceding one"),
    (CT(1, 0) + COMB, "combiner without a component on both sides"),
    (COMB + CT(1, 0), "combiner without a component on both sides"),
    (CT(1, 0) + HJ, "Hợp Thư joiner must stand between a Chi Tự and a Cán Lược"),
    (CL(1) + HJ + CT(1, 0), "Hợp Thư joiner must stand between a Chi Tự and a Cán Lược"),
    (hop(1) + HJ + CL(2), "more than one Hợp Thư joiner"),
    (hop(1) + COMB + hop(2), "top component of a Tham Thư must be a single Chi Tự"),
    (hop(1) + COMB + CT(2, 0) + COMB + CT(3, 0), "more than one combiner"),
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
    assert q.validate_cluster(seq, extended=True) == reason


# Not attested, not prohibited (proposal 5.3): rejected by default, accepted with extended=True.
UNATTESTED = [
    (CL(3) + CT(3, 1), q.SAME_BASE_PHAN_THIET),
    (CT(3, 1) + HJ + CL(4), q.MIXED_HOP_THU),
    (CL(3) + CT(5, 2) + COMB + CT(9, 0), q.NOT_HOP_THU_BASE),
    (CT(3, 1) + COMB + CT(9, 0), q.NOT_HOP_THU_BASE),
    (CT(3, 1) + HJ + CL(4) + COMB + CT(9, 0), q.MIXED_HOP_THU),
]


@pytest.mark.parametrize("seq,reason", UNATTESTED)
def test_unattested_but_not_prohibited(seq, reason):
    assert q.segment(seq) == [seq]
    assert q.validate_cluster(seq) == reason
    assert q.validate_cluster(seq, extended=True) is None


def test_ill_formed_chain_is_one_cluster():
    chain = CT(1, 0) + COMB + CT(2, 0) + COMB + CT(3, 0) + COMB + CT(4, 0)
    [cluster] = q.analyse(chain)
    assert not cluster.valid


def test_mixed_text():
    text = HAN + CL(0) + CT(1, 1) + TONE + hop(2) + CT(2, 2) + HAN
    assert q.segment(text) == [HAN, CL(0) + CT(1, 1) + TONE, hop(2), CT(2, 2), HAN]
    assert q.is_well_formed(text)


def test_adjacent_chi_tu_are_separate_clusters():
    assert q.segment(CT(1, 0) + CT(1, 0)) == [CT(1, 0), CT(1, 0)]


def test_cluster_after_hop_thu_starts_fresh():
    # The Cán Lược of a Hợp Thư must not bind the following Chi Tự.
    assert q.segment(hop(1) + CT(1, 0)) == [hop(1), CT(1, 0)]
    assert q.segment(hop(1) + CL(2) + CT(3, 0)) == [hop(1), CL(2) + CT(3, 0)]


def test_is_hop_thu():
    assert q.is_hop_thu(hop(3))
    assert q.is_hop_thu(hop(3) + COMB + CT(8, 0))
    assert not q.is_hop_thu(CL(3) + CT(3, 4))
    assert not q.is_hop_thu(CT(3, 4))


def test_examples_from_section_5_5():
    b, a = CT(1, 0), CL(1)
    # With the joiner each reading has one spelling.
    assert q.segment(b + HJ + a + b) == [b + HJ + a, b]
    assert q.segment(b + a + b) == [b, a + b]
    # Deleting the top component of a Tham Thư merges the next Chi Tự into it.
    x, z, w = hop(1), CT(2, 0), CT(3, 0)
    assert q.analyse(x + COMB + z + w) == [q.Cluster(x + COMB + z, None), q.Cluster(w, None)]
    assert q.analyse(x + COMB + w) == [q.Cluster(x + COMB + w, None)]
    # Deleting the combiner splits the cluster.
    assert q.segment(x + z) == [x, z]


# --- Properties --------------------------------------------------------------

ALPHABET = (ALL_CAN_TU + ALL_CAN_LUOC + ALL_CHI_TU + [COMB, HJ]
            + [tone(s, c) for s in q.TONE_SHAPES for c in q.TONE_CORNERS]
            + [chr(q.BLOCK_BASE + 0xA4), HAN, " "])

# Skewed towards the code points that join, so long clusters and chains are common.
code_points = st.one_of(
    st.sampled_from(ALPHABET),
    st.sampled_from([COMB, HJ, HJ, CL(0), CL(5), TONE, CT(0, 0), CT(5, 3)]),
)
texts = st.lists(code_points, max_size=30).map("".join)


def spans(text):
    out, start = [], 0
    for cluster in q.segment(text):
        out.append((start, start + len(cluster)))
        start += len(cluster)
    return out


def assert_only_neighbours_change(old, new, edit_at, shift):
    """Every old cluster other than the one at the edit point and its immediate
    neighbours must appear, shifted by `shift` if it lies after the edit, as a
    cluster of the new text. For an insertion the edit point is the boundary
    between old[edit_at - 1] and old[edit_at]; both clusters count as at the edit."""
    old_spans = spans(old)
    new_spans = set(spans(new))
    at_edit = [i for i, (s, e) in enumerate(old_spans)
               if s <= edit_at < e or (shift > 0 and s <= edit_at - 1 < e)]
    if not at_edit:  # insertion at the end of the text
        at_edit = [len(old_spans) - 1] if old_spans else []
    if not at_edit:
        return
    lo, hi = min(at_edit) - 1, max(at_edit) + 1
    for i, (s, e) in enumerate(old_spans):
        if lo <= i <= hi:
            continue
        moved = (s, e) if e <= edit_at else (s + shift, e + shift)
        assert moved in new_spans, (old, new, (s, e))


@settings(max_examples=3000)
@given(texts, st.data())
def test_insertion_changes_only_adjacent_clusters(text, data):
    p = data.draw(st.integers(0, len(text)))
    ch = data.draw(code_points)
    new = text[:p] + ch + text[p:]
    assert_only_neighbours_change(text, new, p, shift=1)


@settings(max_examples=3000)
@given(texts.filter(bool), st.data())
def test_deletion_changes_only_adjacent_clusters(text, data):
    p = data.draw(st.integers(0, len(text) - 1))
    new = text[:p] + text[p + 1:]
    assert_only_neighbours_change(text, new, p, shift=-1)


@given(texts)
def test_segment_concatenates_to_input(text):
    assert "".join(q.segment(text)) == text


def well_formed_cluster():
    ct = st.builds(chi_tu, st.integers(0, 21), st.integers(0, 4))
    ca = st.builds(can_tu, st.integers(0, 21))
    phan_thiet = (st.tuples(st.integers(0, 21), st.integers(0, 21), st.integers(0, 4))
                  .filter(lambda t: t[0] != t[1])
                  .map(lambda t: can_luoc(t[0]) + chi_tu(t[1], t[2])))
    hop_thu = st.builds(hop, st.integers(0, 21), st.integers(0, 4))
    tham = st.tuples(hop_thu, ct).map(lambda t: t[0] + COMB + t[1])
    core = st.one_of(ca, ct, phan_thiet, hop_thu, tham)
    tones = st.sampled_from([""] + [tone(s, c) for s in q.TONE_SHAPES for c in q.TONE_CORNERS])
    return st.tuples(core, tones).map("".join)


@given(st.lists(well_formed_cluster(), max_size=15))
def test_well_formed_text_segments_into_its_clusters(clusters):
    text = "".join(clusters)
    assert q.segment(text) == clusters
    assert q.is_well_formed(text)
