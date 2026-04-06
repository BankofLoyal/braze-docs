#!/usr/bin/env python3
"""
Group cspell lint output by unknown word so you can see every file:line per token.

Usage:
  ./node_modules/.bin/cspell lint --no-progress "_docs/**/*.md" "_includes/**/*.md" 2>&1 \\
    | python3 scripts/cspell_group_report.py

  python3 scripts/cspell_group_report.py /tmp/cspell-full.log

Output is Markdown (stdout). Redirect to a file if you want a local report:
  ... | python3 scripts/cspell_group_report.py > config/cspell/cspell-issues-by-word.md

Lines must match cspell's default issue format:
  path/to/file.md:42:10 - Unknown word (someword)
Optional suffix:  fix: (suggestion)
"""

from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path

# path:line:col - Unknown word (token) [optional fix: (...)]
LINE_RE = re.compile(
    r"^(.+?):(\d+):\d+\s+-\s+Unknown word\s+\(([^)]+)\)"
)


def parse_lines(lines: list[str]) -> dict[str, list[tuple[str, int]]]:
    """word -> [(filepath, line_no), ...]"""
    by_word: dict[str, list[tuple[str, int]]] = defaultdict(list)
    for raw in lines:
        line = raw.strip()
        if not line or line.startswith("CSpell:"):
            continue
        m = LINE_RE.match(line)
        if not m:
            continue
        path, lineno, word = m.group(1), int(m.group(2)), m.group(3)
        by_word[word].append((path, lineno))
    return by_word


def render_markdown(by_word: dict[str, list[tuple[str, int]]]) -> str:
    lines_out: list[str] = []
    lines_out.append("# cspell issues grouped by unknown word\n\n")
    lines_out.append(
        "Local-only backlog (gitignored). Regenerated with full-repo `cspell lint` "
        "on `_docs/**/*.md` and `_includes/**/*.md`, piped through "
        "`scripts/cspell_group_report.py`. Each section lists every `file:line` "
        "for that token.\n\n"
    )
    lines_out.append(
        f"**Unique words:** {len(by_word)}  \n"
        f"**Total occurrences:** {sum(len(v) for v in by_word.values())}\n"
    )
    lines_out.append("\n---\n")

    if not by_word:
        lines_out.append(
            "\n_No unknown words — `cspell lint` found no issues for this scope "
            "(or no issue lines were piped to this script)._\n"
        )
        return "".join(lines_out)

    for word in sorted(by_word.keys(), key=lambda w: (w.lower(), w)):
        locs = by_word[word]
        lines_out.append(f"\n## `{word}`\n")
        lines_out.append(f"*Occurrences: {len(locs)}*\n")
        # Stable sort: path then line
        for path, lineno in sorted(locs, key=lambda t: (t[0].lower(), t[1])):
            lines_out.append(f"- `{path}:{lineno}`\n")

    return "".join(lines_out)


def main() -> int:
    if len(sys.argv) > 1:
        text = Path(sys.argv[1]).read_text(encoding="utf-8", errors="replace")
        input_lines = text.splitlines()
    else:
        input_lines = sys.stdin.read().splitlines()

    by_word = parse_lines(input_lines)
    sys.stdout.write(render_markdown(by_word))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
