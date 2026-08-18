from click.testing import CliRunner

from main import gen


def test_help_lists_generation_options():
    result = CliRunner().invoke(gen, ["--help"])

    assert result.exit_code == 0
    assert "--output-dir" in result.output
    assert "--seed" in result.output


def test_cli_rejects_too_many_sections():
    result = CliRunner().invoke(gen, ["10", "--sections", "3"])

    assert result.exit_code == 2
    assert "length must allow at least 5 characters per section" in result.output


def test_cli_writes_to_custom_output_directory(tmp_path):
    result = CliRunner().invoke(
        gen,
        ["10", "--output-dir", str(tmp_path), "--seed", "7"],
    )

    assert result.exit_code == 0
    assert len(list(tmp_path.glob("*.pdf"))) == 1
