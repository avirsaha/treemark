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
  treemark --max-depth 2 --sizes --format plain --output tree.md
""",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument('--root', type=str, default='.', help='Root directory to start from')
    parser.add_argument('--ignore', nargs='*', help='Files/folders to ignore')
    parser.add_argument('--select-only', nargs='*', help='Only include specific top-level entries')
    parser.add_argument('--max-depth', type=int, help='Limit recursion depth')
    parser.add_argument('--sizes', action='store_true', help='Show file sizes')
    parser.add_argument('--format', choices=['markdown', 'plain'], default='markdown', help='Output format')
    parser.add_argument('--output', type=str, help='Write output to file')
    parser.add_argument('--version', action='version', version=f"%(prog)s {__version__}")

    args = parser.parse_args()

    ignore = set(args.ignore) if args.ignore else set()
    select_only = set(args.select_only) if args.select_only else None
    use_markdown = args.format == 'markdown'

    lines = []
    if use_markdown:
        lines.append("# Project Structure\n")

    lines.extend(generate_markdown_tree(
        root_dir=args.root,
        ignore=ignore,
        select_only=select_only,
        max_depth=args.max_depth,
        show_sizes=args.sizes,
        markdown=use_markdown
    ))

    output = "\n".join(lines)

    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(output + '\n')
    else:
        print(output)
