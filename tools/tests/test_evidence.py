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
            assert (evidence.EVIDENCE / evidence.image_path(image)).is_file(), (e["id"], image)
        if e["status"] == "cited":
            assert e["page"] and e["image"] and e["transcription"], e["id"]


def test_files_are_in_canonical_form():
    for f in evidence.entry_files():
        text = f.read_text(encoding="utf-8")
        assert evidence.render(evidence.parse(text)) == text, f.name


def test_headers_are_valid_yaml():
    # GitHub renders the header as YAML; an unquoted ": " inside a value breaks it.
    yaml = __import__("pytest").importorskip("yaml")
    for f in evidence.entry_files():
        header = f.read_text(encoding="utf-8").split("---\n")[1]
        data = yaml.safe_load(header)
        assert data["id"] == f.stem


def test_all_pages_present():
    names = {p.name for p in (evidence.EVIDENCE / "pages").glob("*.jpg")}
    assert names == {f"S{s}-p{p}.jpg" for s in (1, 2) for p in range(1, 9)}


def test_crops_refer_to_pages_and_images():
    import csv
    with (evidence.EVIDENCE / "crops.csv").open(encoding="utf-8") as f:
        for row in csv.DictReader(f):
            assert (evidence.EVIDENCE / "pages" / f"{row['page']}.jpg").is_file(), row
            assert (evidence.EVIDENCE / "images" / row["image"]).is_file(), row
            assert int(row["left"]) < int(row["right"]) and int(row["top"]) < int(row["bottom"]), row


def test_references_are_linked():
    import link_refs
    for path, prefix in link_refs.targets():
        text = path.read_text(encoding="utf-8")
        assert evidence.link_refs(text, prefix) == text, f"{path.name}: run python tools/link_refs.py"
