![codecov](https://codecov.io/gh/avirsaha/treemark/branch/main/graph/badge.svg)
![Test Status](https://github.com/avirsaha/treemark/actions/workflows/test.yml/badge.svg)

#  TreeMark

**TreeMark** is a lightweight Python CLI tool that generates a clean, readable **Markdown** representation of your project’s directory structure. Perfect for documentation, code walkthroughs, and feeding structured project info to LLMs.


##  Features

* 📁 Recursively walks through your folder structure
* 📝 Outputs a Markdown tree that works in GitHub, Notion, etc.
* 🎯 Supports ignoring files/folders
* 🎯 Supports selecting only certain top-level items
* ✅ No external dependencies, pure Python!


## 📦 Installation

### 📌 From PyPI (Recommended)

> Requires Python 3.6+

```bash
pip install treemark
```

Once installed, run it using:

```bash
treemark
```


### 🛠️ From Source

Clone the repository:

```bash
git clone https://github.com/<your-username>/treemark.git
cd treemark
pip install .
```

Or install in editable mode (for development):

```bash
pip install -e .
```


##  Usage

### Basic Usage

```bash
treemark
```

This generates a Markdown representation of the current directory.


### Options


| Option          | Description                                                    |
| --------------- | -------------------------------------------------------------- |
| `--root PATH`   | Root directory to start from (default: current directory)      |
| `--ignore`      | Space-separated list of files/folders to ignore                |
| `--select-only` | Space-separated list of top-level items to include exclusively |
| `--version`     | Display version info and exit                                  |
| `-h, --help`    | Show help message and exit                                     |


### Example

```bash
treemark --root myproject --ignore __pycache__ venv .git
```

Output:

```
# Project Structure

├── README.md
├── requirements.txt
└── src/
    ├── main.py
    └── utils.py
```


##  Ideal For

* Project READMEs
* Codebase onboarding docs
* Prompting LLMs with structural context
* Static documentation sites


##  Testing

```bash
pytest
```

Tests are located in the `tests/` directory.


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


## 🐛 Troubleshooting

* **PermissionError**: If you get access errors (e.g., `System Volume Information` on Windows), TreeMark now safely skips such directories.
* **Output looks weird?** Make sure you’re viewing the output in a Markdown-capable viewer like GitHub or VSCode preview.


##  Contributing

We welcome PRs and suggestions!

1. Fork the repo
2. Create a feature branch
3. Make your changes
4. Write or update tests
5. Submit a pull request 🚀

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for more.


## 📜 License

[MIT License](LICENSE) © 2025 Aviraj Saha


## 🔗 Related Projects

* [`tree`](https://man7.org/linux/man-pages/man1/tree.1.html) (Linux command)
* [`py-tree`](https://pypi.org/project/tree/) — CLI tree views, not markdown-focused


## ✅ TODOs

* [ ] Add output to file support
* [ ] Add folder depth limit
* [ ] Add theme options (ASCII vs Markdown)
* [ ] Add badge support


## 📣 Stay in Touch

* GitHub: [@avirsaha](https://github.com/avirsaha)
* Issues or feature requests? [Submit here](https://github.com/avirsaha/treemark/issues)
* Email: aviraj.saha@outlook.com
