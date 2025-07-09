import os
import sys

def generate_markdown_tree(root_dir='.', prefix='', ignore=None, select_only=None):
    try:
        entries = sorted(os.listdir(root_dir))
    except PermissionError:
        # Skip folders/files without permission silently
        print(f"⚠️ Skipping inaccessible directory: {root_dir}", file=sys.stderr)
        return []
    except FileNotFoundError:
        # In case the folder disappears during traversal
        return []

    markdown_lines = []

    for index, entry in enumerate(entries):
        if ignore and entry in ignore:
            continue
        if select_only and entry not in select_only:
            continue

        path = os.path.join(root_dir, entry)
        connector = "├── " if index < len(entries) - 1 else "└── "

        if os.path.isdir(path):
            markdown_lines.append(f"{prefix}{connector}**{entry}/**")
            extension_prefix = prefix + ("│   " if index < len(entries) - 1 else "    ")
            markdown_lines.extend(generate_markdown_tree(path, extension_prefix, ignore, None))
        else:
            markdown_lines.append(f"{prefix}{connector}{entry}")
    
    return markdown_lines

