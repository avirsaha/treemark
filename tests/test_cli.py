import subprocess
import tempfile
import os
import sys

def test_cli_output_basic():
    result = subprocess.run(
        [sys.executable, "-m", "treemark.cli", "--root", ".", "--format", "plain"],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
    assert "Project Structure" not in result.stdout  # plain format shouldn't have header

def test_cli_markdown_header():
    result = subprocess.run(
        [sys.executable, "-m", "treemark.cli", "--format", "markdown"],
        capture_output=True,
        text=True
    )
    assert "# Project Structure" in result.stdout

def test_cli_output_to_file():
    with tempfile.TemporaryDirectory() as tmpdir:
        output_path = os.path.join(tmpdir, "tree.md")
        result = subprocess.run(
            [sys.executable, "-m", "treemark.cli", "--output", output_path],
            capture_output=True,
            text=True
        )
        assert result.returncode == 0
        assert os.path.exists(output_path)
        with open(output_path, 'r', encoding='utf-8') as f:
            contents = f.read()
        assert "# Project Structure" in contents

def test_cli_version_flag():
    result = subprocess.run(
        [sys.executable, "-m", "treemark.cli", "--version"],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
    assert "treemark" in result.stdout

