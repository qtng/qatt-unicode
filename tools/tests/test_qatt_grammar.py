import itertools

import pytest
from hypothesis import given, settings, strategies as st

import qatt_grammar as q
from qatt_grammar import COMBINER, JOINER, Kind, unmarked, marked_can, chi, tone

CH = chi
CU = unmarked
COMB = COMBINER
JOIN = JOINER
TONE = tone("SEMICIRCLE", "LOWER LEFT")
HAN = "字"


def hop(base, position=0):
    return CH(base, position) + JOIN + CU(base)


def pt(cl_base, ct_base, position=0):
    return CU(cl_base) + JOIN + CH(ct_base, position)


# --- Block layout (proposal section 7) ---------------------------------------

def test_block_layout_counts():
    counts = {}
    for offset in range(q.BLOCK_SIZE):
        k = q.kind(chr(q.BLOCK_BASE + offset))
        counts[k] = counts.get(k, 0) + 1
    assert counts == {Kind.MARKED_CAN: 22, Kind.UNMARKED: 22, Kind.CHI: 110,
                      Kind.COMBINER: 1, Kind.JOINER: 1, Kind.TONE: 8,
                      Kind.OTHER: 12}
    assert sum(v for k, v in counts.items() if k is not Kind.OTHER) == 164


def test_offsets():
    assert ord(unmarked(0)) - q.BLOCK_BASE == 0x00
    assert ord(marked_can(0)) - q.BLOCK_BASE == 0x01
    assert ord(chi(0, 0)) - q.BLOCK_BASE == 0x02
    assert ord(chi(0, 4)) - q.BLOCK_BASE == 0x06
    assert ord(unmarked(1)) - q.BLOCK_BASE == 0x07      # seven forms per base
    assert ord(unmarked(21)) - q.BLOCK_BASE == 0x93
    assert ord(marked_can(21)) - q.BLOCK_BASE == 0x94
    assert ord(chi(21, 4)) - q.BLOCK_BASE == 0x99
    assert ord(COMB) - q.BLOCK_BASE == 0x9A
    assert ord(JOIN) - q.BLOCK_BASE == 0x9B
    tones = {tone(s, c) for s in q.TONE_SHAPES for c in q.TONE_CORNERS}
    assert {ord(t) - q.BLOCK_BASE for t in tones} == set(range(0x9C, 0xA4))


def test_tone_order_is_traditional():
    # âm bình, dương bình, âm thượng, dương thượng, âm khứ, dương khứ, âm nhập, dương nhập
    order = [tone(s, c) for c in q.TONE_CORNERS for s in q.TONE_SHAPES]
    assert [ord(t) - q.BLOCK_BASE for t in order] == list(range(0x9C, 0xA4))
    assert ord(tone("SEMICIRCLE", "LOWER LEFT")) - q.BLOCK_BASE == 0x9C  # âm bình (ngang)
    assert ord(tone("CIRCLE", "LOWER LEFT")) - q.BLOCK_BASE == 0x9D  # dương bình (huyền)
    assert [q.TONE_NAMES[(s, c)] for c in q.TONE_CORNERS for s in q.TONE_SHAPES][:6] == [
        "âm bình (ngang)", "dương bình (huyền)", "âm thượng (hỏi)",
        "dương thượng (ngã)", "âm khứ (sắc)", "dương khứ (nặng)"]
    assert len(q.TONE_NAMES) == 8


def test_base_of():
    assert q.base_of(marked_can(7)) == 7
    assert q.base_of(unmarked(7)) == 7
    assert all(q.base_of(chi(7, p)) == 7 for p in range(5))
    assert q.base_of(COMB) is None
    assert q.base_of(JOIN) is None
    assert q.base_of(HAN) is None


def test_marked_can_names_are_unique_ascii():
    assert len(q.CAN_NAMES) == q.NUM_BASES == len(set(q.CAN_NAMES))
    assert all(n.isascii() and n.isupper() for n in q.CAN_NAMES)


def test_forms_are_grouped_by_base():
    # Seven consecutive forms per base: unmarked, then MARKED-1 to MARKED-6.
    used = [ord(c) - q.BLOCK_BASE for c in ALL_UNMARKED + ALL_MARKED_CAN + ALL_CHI]
    assert sorted(used) == list(range(0x9A))
    for base in range(22):
        forms = [unmarked(base)] + [q.marked(base, n) for n in range(1, 7)]
        assert [ord(c) - q.BLOCK_BASE for c in forms] == list(range(base * 7, base * 7 + 7))
        assert forms[1] == marked_can(base)
        assert forms[2:] == [chi(base, p) for p in range(5)]
        assert [q.marked_position(c) for c in forms[1:]] == [1, 2, 3, 4, 5, 6]
        assert q.marked_position(forms[0]) is None
        assert all(q.base_of(c) == base for c in forms)
        assert [q.kind(c) for c in forms] == [Kind.UNMARKED, Kind.MARKED_CAN] + [Kind.CHI] * 5


def test_binary_order_groups_clusters_by_first_base():
    # Without collation, clusters sort by the base of their first component, so a
    # base's Phân Thiết and Hợp Thư lie in one contiguous range.
    clusters = [unmarked(x) + JOIN + chi(y, 0) for x in range(22) for y in range(22) if x != y]
    clusters += [chi(x, p) + JOIN + unmarked(x) for x in range(22) for p in range(5)]
    clusters.sort()
    firsts = [q.base_of(c[0]) for c in clusters]
    assert firsts == sorted(firsts)
    with pytest.raises(ValueError):
        q.marked(0, 0)
    with pytest.raises(ValueError):
        q.marked(0, 7)


def test_character_names():
    names = [q.character_name(chr(q.BLOCK_BASE + o)) for o in range(q.BLOCK_SIZE)]
    assigned = [n for n in names if n]
    assert len(assigned) == len(set(assigned)) == 164
    assert all(n.replace("-", "").replace(" ", "").isalnum() and n.isupper() for n in assigned)
    assert q.character_name(marked_can(0)) == "QUOC AM TAN TU ONG MARKED-1"
    assert q.character_name(marked_can(13)) == "QUOC AM TAN TU DZONG MARKED-1"
    assert q.character_name(unmarked(13)) == "QUOC AM TAN TU DZONG UNMARKED"
    assert q.character_name(chi(0, 0)) == "QUOC AM TAN TU ONG MARKED-2"
    assert q.character_name(chi(21, 4)) == "QUOC AM TAN TU PHONG MARKED-6"
    assert q.character_name(tone("SEMICIRCLE", "LOWER LEFT")) == "QUOC AM TAN TU TONE SEMICIRCLE LOWER LEFT"
    assert q.character_name(HAN) is None


def test_constructors_reject_out_of_range():
    with pytest.raises(ValueError):
        marked_can(22)
    with pytest.raises(ValueError):
        chi(0, 5)


# --- Counts from proposal 5.2 ------------------------------------------------

ALL_MARKED_CAN = [marked_can(b) for b in range(22)]
ALL_UNMARKED = [unmarked(b) for b in range(22)]
ALL_CHI = [chi(b, p) for b in range(22) for p in range(5)]


def count_valid(sequences, extended=False):
    return sum(q.validate_cluster("".join(seq), extended) is None for seq in sequences)


def test_two_component_counts_match_proposal():
    phan_thiet = list(itertools.product(ALL_UNMARKED, [JOIN], ALL_CHI))
    hop_thu = list(itertools.product(ALL_CHI, [JOIN], ALL_UNMARKED))
    assert count_valid(phan_thiet) == 2_310
    assert count_valid(hop_thu) == 110
    assert count_valid(phan_thiet) + count_valid(hop_thu) == 2_420


def test_tham_thu_count_matches_proposal():
    on_hop_thu = itertools.product(ALL_CHI, [JOIN], ALL_UNMARKED, [COMB], ALL_CHI)
    assert count_valid(on_hop_thu) == 110 * 110 == 12_100


def test_every_cluster_takes_any_of_eight_tones():
    tones = [tone(s, c) for s in q.TONE_SHAPES for c in q.TONE_CORNERS]
    samples = [ALL_MARKED_CAN[0], ALL_CHI[0], ALL_UNMARKED[0], pt(1, 2), hop(1), hop(1) + COMB + CH(3, 0)]
    assert count_valid((s, t) for s in samples for t in tones) == len(samples) * 8


# --- Sequences from proposal 5.3 ---------------------------------------------

WELL_FORMED = {
    "standalone marked Cán": marked_can(3),
    "standalone Chi": CH(3, 1),
    "standalone unmarked Cán": CU(3),
    "phản thiết pair": pt(3, 5, 2),
    "Hợp Thư": hop(3, 2),
    "Tham Thư": hop(3, 2) + COMB + CH(9, 0),
    "marked Cán with tone": marked_can(3) + TONE,
    "Tham Thư with tone": hop(3, 2) + COMB + CH(9, 0) + TONE,
}


@pytest.mark.parametrize("name", WELL_FORMED)
def test_well_formed_cluster(name):
    seq = WELL_FORMED[name]
    assert q.segment(seq) == [seq]
    assert q.validate_cluster(seq) is None
    assert q.validate_cluster(seq, extended=True) is None


ILL_FORMED = [
    (CU(3) + JOIN + marked_can(4), "component joiner must stand between a Chi and an unmarked Cán"),
    (CU(3) + JOIN + CU(4), "component joiner must stand between a Chi and an unmarked Cán"),
    (CH(3, 0) + JOIN + CH(4, 0), "component joiner must stand between a Chi and an unmarked Cán"),
    (JOIN + CH(4, 0), "component joiner must stand between a Chi and an unmarked Cán"),
    (CU(3) + COMB + CH(4, 0), q.NOT_JOINED),
    (CH(1, 0) + COMB, "combiner without a component on both sides"),
    (COMB + CH(1, 0), "combiner without a component on both sides"),
    (CH(1, 0) + JOIN, "component joiner must stand between a Chi and an unmarked Cán"),
    (hop(1) + JOIN + CH(2, 0), "more than one component joiner"),
    (hop(1) + COMB + hop(2), "top component of a Tham Thư must be a single Chi"),
    (hop(1) + COMB + CH(2, 0) + COMB + CH(3, 0), "more than one combiner"),
    (marked_can(1) + COMB + CH(2, 0), "marked Cán combined with other components"),
    (CH(1, 0) + TONE + COMB + CH(2, 0), "tone mark inside a cluster"),
    (CH(1, 0) + TONE + TONE, "more than one tone mark"),
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
    (pt(3, 3, 1), q.SAME_BASE_PHAN_THIET),
    (CH(3, 1) + JOIN + CU(4), q.MIXED_HOP_THU),
    (pt(3, 5, 2) + COMB + CH(9, 0), q.NOT_HOP_THU_BASE),
    (CH(3, 1) + COMB + CH(9, 0), q.NOT_HOP_THU_BASE),
    (CH(3, 1) + JOIN + CU(4) + COMB + CH(9, 0), q.MIXED_HOP_THU),
]


@pytest.mark.parametrize("seq,reason", UNATTESTED)
def test_unattested_but_not_prohibited(seq, reason):
    assert q.segment(seq) == [seq]
    assert q.validate_cluster(seq) == reason
    assert q.validate_cluster(seq, extended=True) is None


def test_ill_formed_chain_is_one_cluster():
    chain = CH(1, 0) + COMB + CH(2, 0) + COMB + CH(3, 0) + COMB + CH(4, 0)
    [cluster] = q.analyse(chain)
    assert not cluster.valid


def test_mixed_text():
    text = HAN + pt(0, 1, 1) + TONE + hop(2) + CH(2, 2) + HAN
    assert q.segment(text) == [HAN, pt(0, 1, 1) + TONE, hop(2), CH(2, 2), HAN]
    assert q.is_well_formed(text)


def test_adjacent_chi_are_separate_clusters():
    assert q.segment(CH(1, 0) + CH(1, 0)) == [CH(1, 0), CH(1, 0)]


def test_components_without_joiner_stay_separate():
    # Passage of the form 如{CU}{CH}反切云{CU}{CU}... (proposal 3.2).
    text = "如" + CU(1) + CH(2, 0) + "反切云" + CU(3) + CU(4) + "鳥衣"
    assert q.segment(text) == ["如", CU(1), CH(2, 0), "反", "切", "云", CU(3), CU(4), "鳥", "衣"]
    assert q.is_well_formed(text)
    assert q.segment(hop(1) + CH(1, 0)) == [hop(1), CH(1, 0)]
    assert q.segment(CU(1) + HAN) == [CU(1), HAN]


def test_is_hop_thu_and_is_phan_thiet():
    assert q.is_hop_thu(hop(3))
    assert q.is_hop_thu(hop(3) + COMB + CH(8, 0))
    assert not q.is_hop_thu(pt(3, 3, 4))
    assert not q.is_hop_thu(CH(3, 4))
    assert q.is_phan_thiet(pt(3, 4))
    assert not q.is_phan_thiet(hop(3))


def test_examples_from_section_5_5():
    b, a = CH(1, 0), CU(1)
    # With the joiner each reading has one spelling.
    assert q.segment(b + JOIN + a + b) == [b + JOIN + a, b]
    assert q.segment(b + a + JOIN + b) == [b, a + JOIN + b]
    assert q.segment(b + a + b) == [b, a, b]
    # Deleting the top component of a Tham Thư merges the next Chi into it.
    x, z, w = hop(1), CH(2, 0), CH(3, 0)
    assert q.analyse(x + COMB + z + w) == [q.Cluster(x + COMB + z, None), q.Cluster(w, None)]
    assert q.analyse(x + COMB + w) == [q.Cluster(x + COMB + w, None)]
    # Deleting the combiner splits the cluster.
    assert q.segment(x + z) == [x, z]


# --- Properties --------------------------------------------------------------

ALPHABET = (ALL_UNMARKED + ALL_MARKED_CAN + ALL_CHI + [COMB, JOIN]
            + [tone(s, c) for s in q.TONE_SHAPES for c in q.TONE_CORNERS]
            + [chr(q.BLOCK_BASE + 0xA4), HAN, " "])

# Skewed towards the code points that join, so long clusters and chains are common.
code_points = st.one_of(
    st.sampled_from(ALPHABET),
    st.sampled_from([COMB, JOIN, JOIN, CU(0), CU(5), TONE, CH(0, 0), CH(5, 3)]),
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


@settings(max_examples=3000)
@given(texts, st.data())
def test_insertion_changes_only_adjacent_clusters(text, data):
    p = data.draw(st.integers(0, len(text)))
    ch = data.draw(code_points)
    new = text[:p] + ch + text[p:]
    assert_only_neighbours_change(text, new, p, touched=(p - 1, p), shift=1)


@settings(max_examples=3000)
@given(texts.filter(bool), st.data())
def test_deletion_changes_only_adjacent_clusters(text, data):
    p = data.draw(st.integers(0, len(text) - 1))
    new = text[:p] + text[p + 1:]
    assert_only_neighbours_change(text, new, p, touched=(p - 1, p, p + 1), shift=-1)


@given(texts)
def test_segment_concatenates_to_input(text):
    assert "".join(q.segment(text)) == text


def well_formed_cluster():
    ct = st.builds(chi, st.integers(0, 21), st.integers(0, 4))
    ca = st.builds(marked_can, st.integers(0, 21))
    phan_thiet = (st.tuples(st.integers(0, 21), st.integers(0, 21), st.integers(0, 4))
                  .filter(lambda t: t[0] != t[1])
                  .map(lambda t: pt(*t)))
    hop_thu = st.builds(hop, st.integers(0, 21), st.integers(0, 4))
    tham = st.tuples(hop_thu, ct).map(lambda t: t[0] + COMB + t[1])
    cl = st.builds(unmarked, st.integers(0, 21))
    core = st.one_of(ca, ct, cl, phan_thiet, hop_thu, tham)
    tones = st.sampled_from([""] + [tone(s, c) for s in q.TONE_SHAPES for c in q.TONE_CORNERS])
    return st.tuples(core, tones).map("".join)


@given(st.lists(well_formed_cluster(), max_size=15))
def test_well_formed_text_segments_into_its_clusters(clusters):
    text = "".join(clusters)
    assert q.segment(text) == clusters
    assert q.is_well_formed(text)
