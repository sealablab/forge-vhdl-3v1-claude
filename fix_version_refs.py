#!/usr/bin/env python3
"""
Comprehensive script to find and replace all '3v1' references with '3v1'
Searches through all text files in the repository.
"""

import os
import re
from pathlib import Path
from typing import List, Tuple

# Directories to exclude from search
EXCLUDE_DIRS = {
    '.git',
    '__pycache__',
    '.pytest_cache',
    'node_modules',
    '.venv',
    'venv',
    'build',
    'dist',
    '.uv',
}

# File extensions to include (add more as needed)
TEXT_EXTENSIONS = {
    '.md', '.txt', '.py', '.vhd', '.vhdl', '.sh', '.bash',
    '.json', '.yaml', '.yml', '.toml', '.cfg', '.ini',
    '.rst', '.tex', '.html', '.xml', '.csv',
    # No extension (for files like README, LICENSE, etc.)
    ''
}

def should_process_file(filepath: Path) -> bool:
    """Determine if a file should be processed."""
    # Skip if in excluded directory
    for parent in filepath.parents:
        if parent.name in EXCLUDE_DIRS:
            return False

    # Check extension
    return filepath.suffix in TEXT_EXTENSIONS

def find_3v1_references(root_dir: Path) -> List[Tuple[Path, List[int]]]:
    """Find all files containing '3v1' and the line numbers."""
    matches = []

    for filepath in root_dir.rglob('*'):
        if not filepath.is_file():
            continue

        if not should_process_file(filepath):
            continue

        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                matching_lines = [i + 1 for i, line in enumerate(lines) if '3v1' in line.lower()]

                if matching_lines:
                    matches.append((filepath, matching_lines))
        except (UnicodeDecodeError, PermissionError):
            # Skip binary files or files we can't read
            continue

    return matches

def replace_3v1_with_3v1(filepath: Path) -> int:
    """Replace all instances of 3v1 with 3v1 in a file. Returns number of replacements."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Count replacements
        count = len(re.findall(r'3v1', content, re.IGNORECASE))

        if count == 0:
            return 0

        # Replace (case-insensitive, preserving case pattern)
        new_content = content.replace('3v1', '3v1')
        new_content = new_content.replace('3V1', '3V1')
        new_content = new_content.replace('3v1', '3v1')  # lowercase

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

        return count
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return 0

def main():
    root_dir = Path.cwd()

    print("=" * 80)
    print("PHASE 1: Finding all '3v1' references...")
    print("=" * 80)

    matches = find_3v1_references(root_dir)

    if not matches:
        print("\n✅ No '3v1' references found!")
        return

    print(f"\n📍 Found '3v1' in {len(matches)} file(s):\n")

    total_lines = 0
    for filepath, line_numbers in matches:
        rel_path = filepath.relative_to(root_dir)
        print(f"  {rel_path}")
        print(f"    Lines: {', '.join(map(str, line_numbers))}")
        total_lines += len(line_numbers)

    print(f"\n  Total: {total_lines} line(s) across {len(matches)} file(s)")

    print("\n" + "=" * 80)
    print("PHASE 2: Replacing '3v1' → '3v1'...")
    print("=" * 80)

    total_replacements = 0
    for filepath, _ in matches:
        count = replace_3v1_with_3v1(filepath)
        if count > 0:
            rel_path = filepath.relative_to(root_dir)
            print(f"  ✅ {rel_path}: {count} replacement(s)")
            total_replacements += count

    print(f"\n🎉 Total replacements: {total_replacements}")
    print("\n" + "=" * 80)
    print("PHASE 3: Verification...")
    print("=" * 80)

    # Verify no '3v1' remains
    remaining = find_3v1_references(root_dir)
    if remaining:
        print(f"\n⚠️  WARNING: Still found '3v1' in {len(remaining)} file(s):")
        for filepath, line_numbers in remaining:
            rel_path = filepath.relative_to(root_dir)
            print(f"  {rel_path}: lines {', '.join(map(str, line_numbers))}")
    else:
        print("\n✅ Verification passed: No '3v1' references remain!")

    print("\n" + "=" * 80)
    print("Done! Ready to commit changes.")
    print("=" * 80)

if __name__ == '__main__':
    main()
