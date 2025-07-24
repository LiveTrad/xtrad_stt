import pytest
from click.testing import CliRunner
from xtrad_stt.cli.main import transcribe

def test_cli_transcribe(tmp_path):
    runner = CliRunner()
    output_file = tmp_path / "output.txt"
    result = runner.invoke(transcribe, ["--input", "dummy.wav", "--output", str(output_file)])
    assert result.exit_code != 0  # Fails until backends are implemented