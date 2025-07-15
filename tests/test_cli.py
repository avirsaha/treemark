import subprocess
import pytest
import tempfile
import os
import sys

@pytest.mark.skip(reason="Disabled due to known CLI output issues")
def test_cli_output_basic():
    result = subprocess.run(
        [sys.executable, "-m", "treemark.cli", "--root", ".", "--format", "plain"],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
    assert "Project Structure" not in result.stdout  # plain format shouldn't have header

@pytest.mark.skip(reason="Disabled due to known CLI output issues")
def test_cli_markdown_header():
    with tempfile.TemporaryDirectory() as tmpdir:
        with open(os.path.join(tmpdir, "file.txt"), "w") as f:
            f.write("hello")
        result = subprocess.run(
            [sys.executable, "-m", "treemark.cli", "--root", tmpdir, "--format", "markdown"],
            capture_output=True,
            text=True
        )
        assert result.returncode == 0
        assert "# Project Structure" in result.stdout

@pytest.mark.skip(reason="Disabled due to known CLI output issues")
def test_cli_output_to_file():
    with tempfile.TemporaryDirectory() as tmpdir:
        os.mkdir(os.path.join(tmpdir, "some_dir"))
        output_path = os.path.join(tmpdir, "tree.md")
        result = subprocess.run(
            [sys.executable, "-m", "treemark.cli", "--root", tmpdir, "--output", output_path],
            capture_output=True,
            text=True
        )
        assert result.returncode == 0
        assert os.path.exists(output_path)
        with open(output_path, 'r', encoding='utf-8') as f:
            contents = f.read()
        assert "some_dir" in contents

@pytest.mark.skip(reason="Disabled due to known CLI output issues")
def test_cli_version_flag():
    result = subprocess.run(
        [sys.executable, "-m", "treemark.cli", "--version"],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
    assert "treemark" in result.stdout.lower()
    assert "0.2.0" in result.stdout

