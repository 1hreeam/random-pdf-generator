from generate import _safe_filename, generate_pdf


def test_safe_filename_removes_path_characters():
    filename = _safe_filename('report/name:2026')

    assert "/" not in filename
    assert "\\" not in filename
    assert ":" not in filename


def test_safe_filename_handles_windows_reserved_names():
    assert _safe_filename("CON") == "_CON"


def test_generate_pdf_uses_unique_filenames(tmp_path):
    first_path = generate_pdf(10, output_dir=tmp_path, seed=7)
    second_path = generate_pdf(10, output_dir=tmp_path, seed=7)

    assert first_path.exists()
    assert second_path.exists()
    assert first_path != second_path
