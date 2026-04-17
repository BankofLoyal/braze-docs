#!/usr/bin/env python3
"""
Generate deploy PR + merged-contributor-PR lists for release notes.

Requires: gh CLI, authenticated for braze-inc/braze-docs.
Optional: git (for --auto-from-last-release-tag) to resolve the latest `v.*` tag.

Examples:
  # From day after latest v.* tag through today (UTC) — default output path
  python3 scripts/generate_releases_deploy.py --git-repo-root . --auto-from-last-release-tag

  # Explicit window (optional overrides)
  python3 scripts/generate_releases_deploy.py \\
    --merged-search "2026-03-06..2026-04-02" \\
    --window-start "2026-03-06T00:00:00Z" \\
    --window-end "2026-04-02T23:59:59Z" \\
    --month-title "April 2026" \\
    --output scripts/temp/releases_deploy_april_2026_20260306-20260402.md
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from collections import defaultdict
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

DEFAULT_REPO = "braze-inc/braze-docs"

SQUASH_END = re.compile(r"\(#(\d+)\)\s*$")
MERGE_PR = re.compile(r"^Merge pull request #(\d+)\b", re.IGNORECASE)
REVERT_START = re.compile(r'^Revert\s+"')

EXCLUDE_PATTERNS = [
    re.compile(p, re.IGNORECASE)
    for p in [
        r"Apply suggestion",
        r"Applied feedback",
        r"Address review",
        r"@Copilot",
        r"\bCopilot\b",
        r"code review",
        r"Merge branch ['\"]develop['\"] into",
        r"Merge develop into",
        r"^Merge branch ['\"]develop['\"]\s*$",
        r"^Merge branch ['\"]main['\"] into",
        r"^Merge remote-tracking branch",
    ]
]


def extract_pr_num(headline: str) -> int | tuple[str, str] | None:
    if not headline:
        return None
    h = headline.strip()
    m = SQUASH_END.search(h)
    if m:
        return int(m.group(1))
    m = MERGE_PR.match(h)
    if m:
        return int(m.group(1))
    return None


def passes_exclusion(headline: str) -> bool:
    """True if headline should be excluded (suggestion/sync churn)."""
    h = headline.strip()
    return any(pat.search(h) for pat in EXCLUDE_PATTERNS)


def is_revert_only_commit(headline: str) -> bool:
    return bool(REVERT_START.match((headline or "").strip()))


def is_merged_pr_commit(headline: str, *, allow_single_revert: bool) -> bool:
    if not headline:
        return False
    h = headline.strip()
    if allow_single_revert and is_revert_only_commit(h):
        return not passes_exclusion(h)
    if SQUASH_END.search(h) or MERGE_PR.match(h):
        return not passes_exclusion(h)
    return False


def format_contributor_line(headline: str, max_len: int = 200) -> str:
    """Drop trailing (#NNNN); normalize merge subject; no commit SHA in output."""
    h = headline.strip()
    h = re.sub(r"\s*\(#\d+\)\s*$", "", h)
    h = re.sub(r"(?i)^Merge pull request #\d+\s+", "Merge pull request ", h)
    h = h.strip()
    if len(h) > max_len:
        h = h[: max_len - 1] + "…"
    return h


def format_contributor_bullet(github_repo: str, prn: int | tuple[str, str] | None, display: str) -> str:
    """Markdown sub-bullet: linked PR number + subject (legacy-style `#NNNN - title`)."""
    if isinstance(prn, int):
        url = f"https://github.com/{github_repo}/pull/{prn}"
        return f"[#{prn}]({url}) - {display}"
    return display


def gh_json(args: list[str]) -> object:
    out = subprocess.check_output(args, text=True)
    return json.loads(out)


def parse_window(s: str) -> datetime:
    return datetime.fromisoformat(s.replace("Z", "+00:00"))


def _run_git(cwd: str, *git_args: str) -> str:
    r = subprocess.run(
        ["git", *git_args],
        cwd=cwd,
        capture_output=True,
        text=True,
        check=False,
    )
    if r.returncode != 0:
        raise RuntimeError((r.stderr or r.stdout or "git failed").strip())
    return r.stdout.strip()


def auto_window_from_last_v_tag(git_repo_root: str) -> tuple[str, str, str, str, date, date]:
    """
    Last v.* tag in the repo, then window starts the next calendar day (UTC) after that tag's
    commit, through end of today (UTC).

    Returns:
        merged_search, window_start_iso, window_end_iso, month_title, start_day, end_day
    """
    root = str(Path(git_repo_root).resolve())
    try:
        rev = _run_git(root, "rev-list", "--tags", "--max-count=1", "--tags=v.*")
    except RuntimeError as e:
        sys.exit(
            f"error: could not resolve latest v.* tag in {root!r}.\n"
            f"  {e}\n"
            "  Try: git fetch origin main --tags\n"
        )
    if not rev:
        sys.exit(
            f"error: no v.* tag found in {root!r}. "
            "Create a release tag or use explicit --merged-search / --window-* flags."
        )
    try:
        tag_ref = _run_git(root, "describe", "--tags", rev)
        iso = _run_git(root, "log", "-1", "--pretty=format:%cI", tag_ref)
    except RuntimeError as e:
        sys.exit(f"error: could not read tag commit date: {e}")

    dt = datetime.fromisoformat(iso.replace("Z", "+00:00"))
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    else:
        dt = dt.astimezone(timezone.utc)
    tag_day = dt.date()
    start_day = tag_day + timedelta(days=1)
    end_day = datetime.now(timezone.utc).date()
    if start_day > end_day:
        sys.exit(
            f"error: no eligible window (day after last v.* tag is {start_day}, today UTC is {end_day}). "
            "The tag may be too new, or use explicit --merged-search."
        )
    merged_search = f"{start_day.isoformat()}..{end_day.isoformat()}"
    window_start = f"{start_day.isoformat()}T00:00:00Z"
    window_end = f"{end_day.isoformat()}T23:59:59Z"
    month_title = end_day.strftime("%B %Y")
    return merged_search, window_start, window_end, month_title, start_day, end_day


def main() -> None:
    p = argparse.ArgumentParser(description="Generate deploy + merged-PR markdown via gh.")
    p.add_argument("--repo", default=DEFAULT_REPO)
    p.add_argument(
        "--git-repo-root",
        default=".",
        help="Git repo used with --auto-from-last-release-tag (default: cwd)",
    )
    p.add_argument(
        "--auto-from-last-release-tag",
        action="store_true",
        help="Set merged/window from latest v.* tag: day after tag commit → today (UTC)",
    )
    p.add_argument(
        "--merged-search",
        help='e.g. "2026-03-06..2026-04-02" for gh --search (omit with --auto-from-last-release-tag)',
    )
    p.add_argument("--window-start", help="ISO UTC, inclusive")
    p.add_argument("--window-end", help="ISO UTC, inclusive")
    p.add_argument("--month-title", help='e.g. "April 2026" (default in auto mode: month/year of end date)')
    p.add_argument(
        "--output",
        "-o",
        help="Output .md path (default: scripts/temp/releases_deploy_<start>_to_<end>.md)",
    )
    args = p.parse_args()

    start_day: date | None = None
    end_day: date | None = None

    if args.auto_from_last_release_tag:
        ms, ws, we, mt, start_day, end_day = auto_window_from_last_v_tag(args.git_repo_root)
        args.merged_search = ms
        args.window_start = ws
        args.window_end = we
        if not args.month_title:
            args.month_title = mt
    else:
        if not args.merged_search or not args.window_start or not args.window_end:
            p.error(
                "Either pass --auto-from-last-release-tag or all of "
                "--merged-search, --window-start, and --window-end"
            )
        if not args.month_title:
            p.error("--month-title is required when not using --auto-from-last-release-tag")

    window_start = parse_window(args.window_start)
    window_end = parse_window(args.window_end)

    if not args.output:
        root = Path(args.git_repo_root).resolve()
        if start_day is None:
            start_day = window_start.date()
        if end_day is None:
            end_day = window_end.date()
        args.output = str(
            root / "scripts" / "temp" / f"releases_deploy_{start_day.isoformat()}_to_{end_day.isoformat()}.md"
        )

    print(
        f"Merged deploy PRs: {args.merged_search} ({args.window_start} → {args.window_end})",
        file=sys.stderr,
    )

    raw = gh_json(
        [
            "gh",
            "pr",
            "list",
            "--repo",
            args.repo,
            "--state",
            "merged",
            "--label",
            "deploy",
            "--search",
            f"merged:{args.merged_search}",
            "--limit",
            "500",
            "--json",
            "number,title,mergedAt,url",
        ]
    )

    seen: set[int] = set()
    filtered_prs: list[dict] = []
    for row in raw:
        n = row["number"]
        if n in seen:
            continue
        seen.add(n)
        mt = datetime.fromisoformat(row["mergedAt"].replace("Z", "+00:00"))
        if mt < window_start or mt > window_end:
            continue
        filtered_prs.append(row)

    filtered_prs.sort(key=lambda x: x["mergedAt"], reverse=True)

    def gh_pr_view(num: int) -> dict:
        return gh_json(
            [
                "gh",
                "pr",
                "view",
                str(num),
                "--repo",
                args.repo,
                "--json",
                "commits,title,mergedAt,number",
            ]
        )

    def filter_commits(commits: list | None) -> list[dict]:
        clist = commits or []
        single = len(clist) == 1
        picked: list[dict] = []
        for c in clist:
            hl = c.get("messageHeadline") or ""
            allow_revert = single and is_revert_only_commit(hl)
            if not is_merged_pr_commit(hl, allow_single_revert=allow_revert):
                continue
            oid = c.get("oid") or ""
            date = c.get("committedDate") or c.get("authoredDate") or ""
            prn = extract_pr_num(hl)
            if allow_revert and prn is None:
                prn = ("revert", oid)
            picked.append(
                {
                    "oid": oid,
                    "headline": hl,
                    "prn": prn,
                    "date": date,
                    "display": format_contributor_line(hl),
                }
            )

        picked.sort(key=lambda x: x["date"] or "")
        out: list[dict] = []
        seen_pr: set = set()
        for row in picked:
            key = row["prn"]
            if key is None:
                key = ("oid", row["oid"])
            if key in seen_pr:
                continue
            seen_pr.add(key)
            out.append(row)
        return out

    rows: list[dict] = []
    for pr in filtered_prs:
        detail = gh_pr_view(pr["number"])
        rows.append(
            {
                "number": pr["number"],
                "title": pr["title"],
                "mergedAt": pr["mergedAt"],
                "filtered_commits": filter_commits(detail.get("commits")),
            }
        )

    groups: dict[str, list] = defaultdict(list)
    for item in rows:
        groups[item["title"]].append(item)

    def section_sort_key(items: list) -> str:
        return max(i["mergedAt"] for i in items)

    ordered_titles = sorted(groups.keys(), key=lambda t: section_sort_key(groups[t]), reverse=True)

    lines: list[str] = []
    lines.append(
        f"# Deploy PRs for {args.month_title} ({args.window_start} → {args.window_end})"
    )
    lines.append("")
    lines.append(
        "*Merged contributor PRs only: subjects come from this repo’s `scripts/generate_releases_deploy.py` "
        "(squash / merge-PR headlines only; no commit SHA; trailing `(#NNNN)` stripped from text). "
        "Each sub-bullet links `[#NNNN](url) - subject` when the PR number is known. "
        "Sub-commits are ordered oldest first within each deploy PR.*"
    )
    lines.append("")

    for title in ordered_titles:
        items = groups[title]
        items.sort(key=lambda x: x["mergedAt"], reverse=True)
        lines.append(f"## {title}")
        for it in items:
            lines.append(
                f"- https://github.com/{args.repo}/pull/{it['number']} - {it['title']}"
            )
            for c in it["filtered_commits"]:
                bullet = format_contributor_bullet(args.repo, c["prn"], c["display"])
                lines.append(f"  - {bullet}")
            if not it["filtered_commits"]:
                lines.append(
                    "  - *(no squash/merge-PR commits: e.g. Phrase-style “File … committed” only, "
                    "or spot-check on GitHub)*"
                )
        lines.append("")

    text = "\n".join(lines).rstrip() + "\n"
    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Wrote {out_path} ({len(text)} bytes)")


if __name__ == "__main__":
    main()
