import os
import tempfile
from treemark.core import generate_markdown_tree, format_size

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

def test_max_depth_limit():
    with tempfile.TemporaryDirectory() as tmpdir:
        os.mkdir(os.path.join(tmpdir, "level1"))
        os.mkdir(os.path.join(tmpdir, "level1", "level2"))
        tree = generate_markdown_tree(tmpdir, max_depth=1)
        tree_str = "\n".join(tree)
        assert "**level1/**" in tree_str
        assert "level2" not in tree_str

def test_show_sizes():
    with tempfile.TemporaryDirectory() as tmpdir:
        file_path = os.path.join(tmpdir, "file.txt")
        with open(file_path, 'w') as f:
            f.write("123456")
        tree = generate_markdown_tree(tmpdir, show_sizes=True, markdown=False)
        tree_str = "\n".join(tree)
        assert "file.txt (6 B)" in tree_str

def test_plain_formatting():
    with tempfile.TemporaryDirectory() as tmpdir:
        os.mkdir(os.path.join(tmpdir, "mydir"))
        tree = generate_markdown_tree(tmpdir, markdown=False)
        tree_str = "\n".join(tree)
        assert "**" not in tree_str  # no markdown
        assert "mydir/" in tree_str

def test_permission_error_handling(monkeypatch):
    def fake_listdir(path):
        raise PermissionError("Simulated permission denied")
    monkeypatch.setattr(os, "listdir", fake_listdir)
    result = generate_markdown_tree(".")
    assert result == []

def test_format_size():
    assert format_size(1023) == "1023 B"
    assert format_size(1024) == "1 KB"
    assert format_size(1024**2) == "1 MB"

