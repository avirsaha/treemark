
![codecov](https://codecov.io/gh/avirsaha/treemark/branch/main/graph/badge.svg)
![Test Status](https://github.com/avirsaha/treemark/actions/workflows/test.yml/badge.svg)

# TreeMark

**TreeMark** is a lightweight Python CLI tool that generates a clean, readable **Markdown** (or plain text) representation of your project’s directory structure. Perfect for documentation, code walkthroughs, and feeding structured project info to LLMs.

---

## 🚀 Features

* 📁 Recursively walks through your folder structure
* 📝 Outputs a Markdown tree that works in GitHub, Notion, etc.
* 🧾 Option to output in plain text instead of Markdown
* 📏 Limit directory depth with `--max-depth`
* 📦 Show file sizes with `--sizes`
* 💾 Save output to a file with `--output`
* 🎯 Supports ignoring files/folders
* 🎯 Supports selecting only certain top-level items
* ✅ No external dependencies, pure Python!

---

## 📦 Installation
<!--
### 📌 From PyPI (Recommended)

> Requires Python 3.6+

```bash
pip install treemark
````

Once installed, run it using:

```bash
treemark
```
-->
### 🛠️ From Source (Recommended)

Clone the repository:

```bash
git clone https://github.com/avirsaha/treemark.git
cd treemark
pip install .
```

Or install in editable mode (for development):

```bash
pip install -e .
```

---

## 📂 Usage

### Basic Usage

```bash
treemark
```

This generates a Markdown tree of the current directory.

### Options

| Option            | Description                                                    |
| ----------------- | -------------------------------------------------------------- |
| `--root PATH`     | Root directory to start from (default: current directory)      |
| `--ignore`        | Space-separated list of files/folders to ignore                |
| `--select-only`   | Space-separated list of top-level items to include exclusively |
| `--max-depth N`   | Limit how deep the recursion goes (e.g., `--max-depth 2`)      |
| `--sizes`         | Show file sizes in bytes next to each file                     |
| `--format FORMAT` | Choose output format: `markdown` (default) or `plain`          |
| `--output FILE`   | Save the tree output to a specified file                       |
| `--version`       | Display version info and exit                                  |
| `-h, --help`      | Show help message and exit                                     |

---

### Example

```bash
treemark --root myproject --ignore __pycache__ venv .git --max-depth 2 --sizes --output structure.md
```

Output (Markdown):

```
# Project Structure

├── README.md (1.2 KB)
├── requirements.txt (57 B)
└── src/
    ├── main.py (2.1 KB)
    └── utils.py (800 B)
```

---

## ✅ Ideal For

* Project READMEs
* Codebase onboarding docs
* Prompting LLMs with structural context
* Static documentation sites

---

## 🧪 Testing

```bash
pytest
```

Tests are located in the `tests/` directory.

---

## 🧹 Cleanup (Dev Only)

To remove build artifacts before packaging or publishing:

**Windows:**

```powershell
Remove-Item -Recurse -Force build, dist, *.egg-info
```

**macOS/Linux:**

```bash
rm -rf build dist *.egg-info
```

---

## 🐛 Troubleshooting

* **PermissionError**: TreeMark now skips inaccessible directories (e.g., `System Volume Information` on Windows).
* **Output formatting issues?** Make sure you’re viewing the result in a Markdown-capable viewer like GitHub or VSCode.

---

## 🤝 Contributing

We welcome PRs and suggestions!

1. Fork the repo
2. Create a feature branch
3. Make your changes
4. Write or update tests
5. Submit a pull request 🚀

<!--See [`CONTRIBUTING.md`](CONTRIBUTING.md) for more.-->

---

## 📜 License

[MIT License](LICENSE) © 2025 Aviraj Saha

---

## 🔗 Related Projects

* [`tree`](https://man7.org/linux/man-pages/man1/tree.1.html) — Classic CLI directory viewer
* [`py-tree`](https://pypi.org/project/tree/) — CLI tree views, not markdown-focused

---

## ✅ TODOs

* [x] Add output to file support
* [x] Add folder depth limit
* [x] Add format options (Markdown vs plain text)
* [x] Show file sizes
* [ ] Add color themes (for terminal output)
* [ ] Add Git integration (e.g., show tracked/untracked)

---

## 📣 Stay in Touch

* GitHub: [@avirsaha](https://github.com/avirsaha)
* Issues or feature requests? [Submit here](https://github.com/avirsaha/treemark/issues)
* Email: [aviraj.saha@outlook.com](mailto:aviraj.saha@outlook.com)


