# QATT Unicode Proposal – Draft (Sections 4 and 5)

Oct 9, 2026 · @Trung

## 1. Summary

This proposal encodes Quốc Âm Tân Tự (QATT), a Vietnamese script used inside Han Nôm texts, as 163 characters in the Supplementary Multilingual Plane.

| Item | Entry |
| --- | --- |
| Script | Quốc Âm Tân Tự (QATT) |
| Proposer | \[TBD: name and affiliation\] |
| Draft date | 2026-10-09 |
| Characters | 163: 154 components, 1 combiner, 8 tone marks |
| Model | Atomic components; Hợp Thư and Tham Thư as sequences |
| Plane | Supplementary Multilingual Plane \[TBD: block position assigned by the UTC\] |
| Direction | Follows Han Nôm; the sources are vertical |
| Attested sources | Two, both vertical Han Nôm texts |
| Official form | \[TBD: complete the UTC Proposal Summary Form\] |

## 2. Introduction

Quốc Âm Tân Tự is a Vietnamese script built from 22 base components, each of three strokes and one short marking stroke. Components stand alone or combine in groups of two or three, and any character may carry a tone mark in one of its corners.

### 2.1 Background

In the attested sources the script appears in running Han Nôm text and is treated exactly like Han Nôm characters. Three-component characters (Tham Thư) record dialectal vowel clusters. Eight tones are marked with circles and semicircles in the corners, following the Chinese yin-yang method. \[TBD: date and provenance of the sources; scholarly literature\]

### 2.2 Reasons for encoding

&#91;TBD: need for digital text, scholarship, user community and interest in the script\]

## 3. Sources and Evidence

Two sources attest the script. Both are vertical Han Nôm texts, and the text of the sources describes the methods of combination.

### 3.1 Attested sources

| Source | Date | Location | Text type | Direction |
| --- | --- | --- | --- | --- |
| Source 1 | \[TBD\] | \[TBD\] | Han Nôm | Vertical |
| Source 2 | \[TBD\] | \[TBD\] | Han Nôm | Vertical |

### 3.2 Evidence by feature

| Feature | Evidence | Status |
| --- | --- | --- |
| Cán Tự, Chi Tự, Cán Lược | Described in the sources | \[TBD: cite passages and examples\] |
| Hợp Thư | Described in the text; every example with a same-base pair shows the exchanged form | \[TBD: list the examples\] |
| Tham Thư | Rule described in the text; two examples attested, both on an exchanged Hợp Thư | \[TBD: cite both examples\] |
| Tone marks | Eight tones in four corners; semicircle orientation visible only in the examples | \[TBD: examples for all four corners\] |
| Writing direction | The text is silent; both sources are vertical Han Nôm | Assumption: Han Nôm habits |

### 3.3 Modern use

&#91;TBD: current use of the script, for example on chunom.org, and any user community\]

### 3.4 Scans and images

&#91;TBD: scans of the source pages with the relevant passages marked\]

## 4. Structure of the Script

Quốc Âm Tân Tự is built from 22 base components that stand alone or combine in groups of two or three, and any character may carry one tone mark in one of its four corners.

### 4.1 Components

Each of the 22 base components (*Cán Tự*) consists of three strokes and one short marking stroke. Repositioning the marking stroke yields five variants per base (*Chi Tự*). Omitting it yields one reduced form per base (*Cán Lược*).

| Component | Count | Derivation | Standalone | In combination |
| --- | --- | --- | --- | --- |
| Cán Tự | 22 | 3 strokes + 1 marking stroke | yes | never |
| Chi Tự | 110 (22 × 5) | marking stroke repositioned | yes | yes |
| Cán Lược | 22 | marking stroke omitted | no | only with a Chi Tự |

### 4.2 Hợp Thư (two components)

A Cán Lược and a Chi Tự combine into one character. If both derive from the same Cán Tự, their positions are exchanged. In the sources the non-exchanged form never occurs for such pairs, although the text does not forbid it. When the non-exchanged reading is intended, the Cán Lược is omitted and the Chi Tự stands alone. \[TBD: cite the source passage and the attested examples\]

### 4.3 Tham Thư (three components)

A Hợp Thư, or a single Chi Tự, may carry a third component above it. The third component must be a single Chi Tự and is otherwise unrestricted. The first two components always form a unit, and the third stands alone above them. The method records dialectal vowel clusters. Two examples are attested, both with an exchanged Hợp Thư as the base. \[TBD: cite the source passage and both examples\]

### 4.4 Tone marks

A tone mark is a circle or a semicircle placed in one of the four corners of the character, giving eight tones. The sources do not specify the orientation of the semicircle; every example shows its open side facing the centre of the character. Round versus angular forms of the semicircle are handwriting variation. A character carries at most one tone mark, and many carry none. \[TBD: cite the source passage and examples for all four corners\]

### 4.5 Layout

&#91;TBD: position of the two components within a Hợp Thư, and of the top component within a Tham Thư\]

## 5. Encoding Model

The script is encoded as 163 atomic characters. Hợp Thư and Tham Thư are sequences, so every character stays editable and its boundaries are determined locally.

### 5.1 Repertoire

| Group | Characters |
| --- | --- |
| Cán Tự | 22 |
| Chi Tự | 110 |
| Cán Lược (component only, never standalone) | 22 |
| Tham Thư combiner | 1 |
| Tone marks (combining) | 8 |
| **Total** | **163** |

### 5.2 Why not precomposed

Hợp Thư allows 2,420 combinations (22 Cán Lược × 110 Chi Tự). Tham Thư allows up to 2,530 × 110 = 278,300, because the base may be a Hợp Thư or a single Chi Tự. Only two Tham Thư are attested. Precomposing is neither feasible nor justified.

### 5.3 Sequence grammar

```
Character := Cluster [ToneMark]
Cluster   := CanTu | ChiTu | HopThu | ThamThu
HopThu    := CanLuoc ChiTu
ThamThu   := (HopThu | ChiTu) Combiner ChiTu
```

A Cán Lược never stands alone and always begins a Hợp Thư, so cluster boundaries need no lookahead beyond the next character.

| Intended character | Sequence |
| --- | --- |
| Standalone Chi Tự | CT |
| Hợp Thư, different bases | CL(X) CT(Y) |
| Hợp Thư, same base (rendered exchanged) | CL(X) CT(X) |
| Tham Thư on a Hợp Thư | CL(X) CT(Y) COMB CT(Z) |
| Tham Thư on a single Chi Tự | CT(X) COMB CT(Z) |
| Any of the above with a tone | sequence + TONE |

### 5.4 Positional exchange

For a Cán Lược and a Chi Tự of the same Cán Tự, the exchanged position is the only attested form. It is therefore a rendering rule, implemented with OpenType substitution, and not encoded. The non-exchanged form can be described with Ideographic Description Sequences in scholarly notation. \[TBD: IDS operator depends on the layout in 4.5\]

### 5.5 Edit stability

Deleting or inserting one character alters at most the clusters directly adjacent to the edit point. An edit can split a cluster, merge two neighbours (for example when the top component of a Tham Thư is deleted and the next Chi Tự takes its place) or attach a tone mark to the preceding cluster. Nothing beyond the neighbours changes.

**Hypothetical model, not part of this proposal.** To show why the proposed order matters, consider encoding the exchange by sequence order, with the Chi Tự written before the Cán Lược. This model is rejected, because it fails the test above and is also ambiguous. With B a Chi Tự and A a Cán Lược of the same base, the sequence `BAB` would read as `[BA][B]` or as `[B][AB]`, and both are valid texts. A left-to-right parser takes the first reading, so deleting the first A in `ABABAB` would regroup all following characters from `[AB][AB][AB]` into `[BA][BA][B]`. A parser that binds the Cán Lược forward first avoids that regrouping, but it could no longer express `[BA][B]` at all.

In the proposed model the Cán Lược always comes first, and the exchange is a rendering rule (5.4).

### 5.6 Tone marks

The eight tone marks are combining characters that follow the complete cluster. Each corner and each mark type is contrastive, so a tone is a character and not a glyph variant. The orientation of the semicircle follows from its corner and is a glyph property. A cluster takes at most one tone mark.

### 5.7 Alternatives considered

- Variation selector for the exchange: rejected, because the non-exchanged form is unattested.
- Exchange by sequence order (hypothetical model with the Chi Tự before the Cán Lược): rejected for ambiguity and edit instability (5.5).
- Two tone marks plus a position selector: rejected, because the corner is contrastive.
- Precomposed Hợp Thư and Tham Thư: rejected for size (5.2).

### 5.8 Open decision

Propose the Tham Thư combiner now, or describe Tham Thư with IDS first and add the combiner once more attestations exist. With two attested examples, the second option lowers the risk of rejection.

## 6. Character Properties

The proposed properties follow from the encoding model: components are letters, the combiner is a format character, and tone marks are nonspacing marks. Cells marked \[TBD\] depend on evidence from the sources or on review by the Unicode text-segmentation experts.

| Characters | General\_Category | Combining class | Grapheme\_Cluster\_Break | Line\_Break | Bidi\_Class |
| --- | --- | --- | --- | --- | --- |
| Cán Tự, Chi Tự | Lo | 0 | Other | ID | L |
| Cán Lược | Lo | 0 | Prepend | ID | L |
| Tham Thư combiner | Cf | 0 | \[TBD\] | CM | L |
| Tone marks (8) | Mn | 0 | Extend | CM | NSM |

### 6.1 Combining class of the tone marks

The corner is part of each tone mark's identity, so no positional combining classes are needed. A cluster takes at most one tone mark, so canonical reordering between marks never occurs. All eight marks therefore take class 0. \[TBD: confirm with current Unicode conventions\]

### 6.2 Grapheme clusters

A Cán Lược always joins the character that follows it. This matches the behaviour of Prepend characters. Tone marks match Extend. The combiner must keep the preceding cluster, itself and the following Chi Tự together, which resembles the conjunct rule for Indic scripts in UAX #29. \[TBD: decide between an existing property value and a new one\]

### 6.3 Line breaking and direction

The sources do not state a writing direction. Both attested sources contain vertical Han Nôm text, and in every case the script is treated exactly like Han Nôm and flows with it: vertical lines, columns running right to left, no spaces between words. No horizontal use is attested. The proposal therefore assumes the writing habits of Han Nôm. The characters behave like ideographs, each occupying one square cell. Proposed for the components: Bidi\_Class L, Line\_Break ID, East\_Asian\_Width W, Vertical\_Orientation U. Tone marks and the combiner never start a line, because they belong to the preceding cluster.

### 6.4 Code point order

The sources list the 22 Cán Tự roughly by place of articulation. This order has no encoding significance, so code points follow the order of that listing and no collation claim is made. Within each Cán Tự, the five Chi Tự follow one fixed order of the marking-stroke position. \[TBD: define that order of the five positions\]

## 7. Character Table and Code Chart

The 163 characters fit in a block of 176 code points (11 rows of 16), proposed for the Supplementary Multilingual Plane. \[TBD: block position assigned by the UTC\] Code points follow the source order of the 22 Cán Tự, and the five Chi Tự of each base are consecutive.

| Group | Offset in block | Count |
| --- | --- | --- |
| Cán Tự | +00 to +15 | 22 |
| Cán Lược | +16 to +2B | 22 |
| Chi Tự | +2C to +99 | 110 |
| Tham Thư combiner | +9A | 1 |
| Tone marks | +9B to +A2 | 8 |
| Reserved | +A3 to +AF | 13 |

### 7.1 Character names

Names use ASCII capitals without diacritics, as Unicode requires. Patterns:

```
QUOC AM TAN TU CAN TU <NAME>
QUOC AM TAN TU CAN LUOC <NAME>
QUOC AM TAN TU CHI TU <NAME> <POSITION>
QUOC AM TAN TU THAM THU COMBINER
QUOC AM TAN TU TONE CIRCLE UPPER LEFT
QUOC AM TAN TU TONE SEMICIRCLE LOWER RIGHT
```

The tone marks use the corners UPPER LEFT, UPPER RIGHT, LOWER LEFT and LOWER RIGHT, each for circle and semicircle. \[TBD: names of the 22 Cán Tự and of the five marking-stroke positions\]

### 7.2 Code chart

&#91;TBD: reference glyphs from the font, showing every Cán Tự, Chi Tự, Cán Lược, the combiner and the tone marks in their corners\]

## 8. Font Design Notes

A conforming font draws every cluster in one square cell and composes it with substitution and positioning rules, not with precomposed glyphs.

- **Cell:** Each cluster fills one square cell with the metrics of Han Nôm ideographs, so it sits in vertical or horizontal lines without adjustment.
- **Hợp Thư:** The two component glyphs share the cell. \[TBD: positions, see 4.5\]
- **Exchange rule:** For a Cán Lược and a Chi Tự of the same Cán Tự (110 pairs), the font swaps the positions of the two components. The non-exchanged form needs no rendering support, because it is notated with IDS.
- **Tham Thư:** After the combiner, the Chi Tự is drawn above the base cluster. The font composes the cluster by contextual substitution and positioning, because 278,300 precomposed glyphs are impractical. The two attested examples serve as test cases for the reference font.
- **Tone marks:** Eight combining glyphs sit in the four corners of the whole cluster cell. The open side of the semicircle faces the centre. Round or angular outlines are a design choice, since the sources treat the difference as handwriting variation.
- **Reference font:** \[TBD: designer and licence\]

## 9. Open Points

Seven points remain before the proposal can be submitted. The alternatives already weighed are in 5.7.

| Point | Section | What is needed |
| --- | --- | --- |
| Tham Thư combiner now, or IDS first | 5.8 | Decision |
| Layout of the components in Hợp Thư and Tham Thư | 4.5 | Positions from the source examples |
| Source passages and scans for Hợp Thư, Tham Thư and the tone corners | 4.2 to 4.4 | Citations and images |
| Names of the 22 Cán Tự, the five marking-stroke positions and their order | 6.4, 7.1 | Names and order |
| Block position in the Supplementary Multilingual Plane | 7 | Assignment by the UTC |
| Reference font | 8 | Designer and licence |
| Horizontal use | 6.3 | Not attested, so the proposal assumes Han Nôm habits |

## 10. Appendices

### A. Glossary

| Term | Meaning |
| --- | --- |
| Cán Tự | One of 22 base components; three strokes and one marking stroke; standalone only, never combined |
| Chi Tự | One of five variants per Cán Tự, made by repositioning the marking stroke (110 in total); standalone or combined |
| Cán Lược | The variant without a marking stroke (22 in total); only in combination with a Chi Tự |
| Hợp Thư | Combination of a Cán Lược and a Chi Tự; positions are exchanged when both share the same Cán Tự |
| Tham Thư | Hợp Thư or single Chi Tự with a third component, a Chi Tự, above it; records dialectal vowel clusters |

### B. Attested examples

&#91;TBD: table of every attested Hợp Thư and both Tham Thư with source, page and image\]

### C. Scans of the sources

&#91;TBD: images of the relevant pages\]

### D. References

&#91;TBD: scholarly literature and prior work on the script\]
