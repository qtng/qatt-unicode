# Roadmap

Plan for resolving the open points in section 9 of the proposal. The source work comes first, because almost every other decision depends on it.

## Phase A – Sources (evidence catalogue)

Record each passage as an entry in [evidence/](evidence/), one Markdown file per claim.

1. Function of the components: initial and rhyme in phản thiết pairs and Hợp Thư ([E06](evidence/E06.md), [E08](evidence/E08.md)). Main argument for the encoding model.
2. Standalone and adjacent components ([E04](evidence/E04.md)). Main argument for the explicit joiner.
3. Scope of the term Hợp Thư and the omission convention ([E07](evidence/E07.md), [E09](evidence/E09.md)).
4. Both Tham Thư, phản thiết examples, tone marks in all four corners ([E05](evidence/E05.md), [E10](evidence/E10.md)–[E16](evidence/E16.md)).
5. Layout of the components within a cell (proposal 4.5), from the same examples.
6. Date, provenance and location of both sources; scholarly literature ([E17](evidence/E17.md)–[E21](evidence/E21.md)).

## Phase B – Names and order

1. Names of the 22 Cán from the source listing; ASCII names with DD and DZ (done, proposal 7.1).
2. Forms named by the position of the marking stroke, UNMARKED and MARKED-1 to MARKED-6, and code point order (done, proposal 6.4 and 7).
3. Final name of the component joiner (open).

## Phase C – Justification

1. Reasons for encoding and modern use (proposal 2.2, 3.3), including documented written forms from online discussion ([E22](evidence/E22.md)).

## Phase D – Technical

1. Draft Unicode Character Database entries and a list of questions for the Unicode experts. Drafted in [ucd/](ucd/); next: review of [ucd/questions.md](ucd/questions.md).
2. Reference font and code chart glyphs: check existing QATT glyphs; designer and licence to be decided.
3. Horizontal use: record as an assumption rather than an open point.

## Phase E – Submission

1. UTC Proposal Summary Form (proposer: Nguyễn Quốc Trung, independent researcher).
2. Check the Unicode roadmap for the Supplementary Multilingual Plane; the block position is assigned by the UTC.
3. Pre-submission review by the Script Encoding Initiative (UC Berkeley).
4. Images of the sources (not part of the proposal text): the proposer found a scan on Wikimedia Commons, [File:Quốc âm tân tự.png](https://commons.wikimedia.org/wiki/File:Qu%E1%BB%91c_%C3%A2m_t%C3%A2n_t%E1%BB%B1.png), licence tags Public domain (United States, published before 1931) and Public domain (Vietnam), author given as Nguyễn Tử; it shows a few pages and is said to be the same scan as the working copies. Not yet downloaded (HTTP 429 from the container); to do: cut the pages out and replace the files in `evidence/pages/`. The proposer states that the Institute of Hán Nôm Studies took the manuscripts over from holdings of the French colonial administration (no source yet). Rights of the images are not discussed in the proposal.

## Deferred – Tham Thư

Tham Thư is the least certain part of the script: two examples, no stated reading. Its reading and the function of its components ([E11](evidence/E11.md)) stay open. The decision in proposal 5.8, Tham Thư combiner now or later, is taken last.
