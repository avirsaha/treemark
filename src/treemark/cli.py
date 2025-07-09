import argparse
from treemark.core import generate_markdown_tree
from treemark import __version__

def main():
    parser = argparse.ArgumentParser(
        prog="treemark",
        description="📁 Generate a markdown-formatted tree of your project folder structure.",
        epilog="""
Examples:
  treemark --root . --ignore .git __pycache__
  treemark --select-only src tests
  treemark --root /path/to/project
""",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument(
        '--root',
        type=str,
        default='.',
        help='Root directory to start from (default: current directory)'
    )
    parser.add_argument(
        '--ignore',
        nargs='*',
        help='List of folders/files to ignore (e.g., --ignore .git __pycache__)'
    )
    parser.add_argument(
        '--select-only',
        nargs='*',
        help='Only include these files/folders (top-level filtering)'
    )
    parser.add_argument(
        '--version',
        action='version',
        version=f"%(prog)s {__version__}"
    )

    args = parser.parse_args()

    ignore = set(args.ignore) if args.ignore else set()
    select_only = set(args.select_only) if args.select_only else None

    markdown_output = ["# Project Structure\n"]
    markdown_output.extend(generate_markdown_tree(args.root, ignore=ignore, select_only=select_only))
    print("\n".join(markdown_output))

