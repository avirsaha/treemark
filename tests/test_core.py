import os
import tempfile
import shutil
from treemark.core import generate_markdown_tree

def test_basic_tree_structure():
    with tempfile.TemporaryDirectory() as tmpdir:
        os.mkdir(os.path.join(tmpdir, "folder"))
        with open(os.path.join(tmpdir, "file.txt"), 'w') as f:
            f.write("test")

        tree = generate_markdown_tree(tmpdir)
        tree_str = "\n".join(tree)
        assert "**folder/**" in tree_str
        assert "file.txt" in tree_str

def test_ignore_option():
    with tempfile.TemporaryDirectory() as tmpdir:
        os.mkdir(os.path.join(tmpdir, "ignore_me"))
        with open(os.path.join(tmpdir, "keep_me.txt"), 'w') as f:
            f.write("ok")

        tree = generate_markdown_tree(tmpdir, ignore={"ignore_me"})
        tree_str = "\n".join(tree)
        assert "ignore_me" not in tree_str
        assert "keep_me.txt" in tree_str

def test_select_only_option():
    with tempfile.TemporaryDirectory() as tmpdir:
        os.mkdir(os.path.join(tmpdir, "src"))
        os.mkdir(os.path.join(tmpdir, "docs"))
        with open(os.path.join(tmpdir, "README.md"), 'w') as f:
            f.write("readme")

        tree = generate_markdown_tree(tmpdir, select_only={"src"})
        tree_str = "\n".join(tree)
        assert "**src/**" in tree_str
        assert "**docs/**" not in tree_str
        assert "README.md" not in tree_str

def test_permission_error_handling(monkeypatch):
    def fake_listdir(path):
        raise PermissionError("Simulated permission denied")

    monkeypatch.setattr(os, "listdir", fake_listdir)
    result = generate_markdown_tree(".")
    assert result == []

