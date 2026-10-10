import evidence


def test_entries_are_consistent():
    files = evidence.entry_files()
    entries = evidence.load()
    assert files and len(entries) == len(files)
    assert [e["id"] for e in entries] == [f.stem for f in files]
    for e in entries:
        assert e["status"] in evidence.STATUSES, e["id"]
        assert len(e["image"]) in (0, len(e["source"])), e["id"]
        for image in e["image"]:
            assert (evidence.EVIDENCE / "images" / image).is_file(), (e["id"], image)
        if e["status"] == "cited":
            assert e["page"] and e["image"] and e["transcription"], e["id"]


def test_files_are_in_canonical_form():
    for f in evidence.entry_files():
        text = f.read_text(encoding="utf-8")
        assert evidence.render(evidence.parse(text)) == text, f.name
