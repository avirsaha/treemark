import os
import sys

def format_size(bytes):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes < 1024:
            return f"{bytes:.0f} {unit}"
        bytes /= 1024
    return f"{bytes:.0f} PB"

def generate_markdown_tree(root_dir='.', prefix='', ignore=None, select_only=None,
                           max_depth=None, current_depth=0, show_sizes=False, markdown=True):
    if max_depth is not None and current_depth >= max_depth:
        return []

    try:
        entries = sorted(os.listdir(root_dir))
    except PermissionError:
        print(f"⚠️ Skipping inaccessible directory: {root_dir}", file=sys.stderr)
        return []
    except FileNotFoundError:
        return []

    markdown_lines = []

    for index, entry in enumerate(entries):
        if ignore and entry in ignore:
            continue
        if select_only and entry not in select_only and current_depth == 0:
            continue

        path = os.path.join(root_dir, entry)
        connector = "├── " if index < len(entries) - 1 else "└── "

        if os.path.isdir(path):
            name = f"**{entry}/**" if markdown else f"{entry}/"
            markdown_lines.append(f"{prefix}{connector}{name}")
            extension_prefix = prefix + ("│   " if index < len(entries) - 1 else "    ")
            markdown_lines.extend(generate_markdown_tree(
                path,
                extension_prefix,
                ignore,
                None,
                max_depth,
                current_depth + 1,
                show_sizes,
                markdown
            ))
        else:
            size_str = ''
            if show_sizes:
                try:
                    size = os.path.getsize(path)
                    size_str = f" ({format_size(size)})"
                except:
                    pass
            markdown_lines.append(f"{prefix}{connector}{entry}{size_str}")

    return markdown_lines
