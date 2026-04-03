#!/usr/bin/env python3
"""
Evaluate Cursor Bugbot review comments on auto-translation PRs using Claude.

Fetches Bugbot's inline review comments, sends them to Claude for evaluation,
applies valid fixes, updates glossaries when systemic issues are found,
and posts a summary comment on the PR.

Usage:
    PR_NUMBER=123 python scripts/review_bugbot.py
"""

import json
import os
import re
import subprocess
import sys
from pathlib import Path

REPO = os.environ.get("GITHUB_REPOSITORY", "braze-inc/braze-docs")
PR_NUMBER = os.environ.get("PR_NUMBER", "")
REVIEW_MODEL = os.environ.get("REVIEW_MODEL", "claude-sonnet-4-20250514")
REPO_ROOT = Path(os.environ.get("GITHUB_WORKSPACE", Path.cwd()))
GLOSSARY_DIR = REPO_ROOT / "scripts" / "glossaries"
SCRIPTS_DIR = REPO_ROOT / "scripts"

LANGUAGES = {
    "de":    {"glossary": "de",    "name": "German"},
    "es":    {"glossary": "es",    "name": "Spanish"},
    "fr_fr": {"glossary": "fr",    "name": "French"},
    "ja":    {"glossary": "ja",    "name": "Japanese"},
    "ko":    {"glossary": "ko",    "name": "Korean"},
    "pt_br": {"glossary": "pt-br", "name": "Portuguese (Brazil)"},
}

SUMMARY_FILE = REPO_ROOT / "bugbot_review_summary.md"


def _get_client():
    try:
        from anthropic import Anthropic
    except ImportError:
        print("ERROR: pip install anthropic")
        sys.exit(1)
    return Anthropic()


# ── GitHub API helpers ───────────────────────────────────────────────────────

def fetch_bugbot_comments():
    """Fetch inline review comments left by Cursor Bugbot on the PR."""
    result = subprocess.run(
        ["gh", "api", "--paginate",
         f"repos/{REPO}/pulls/{PR_NUMBER}/comments"],
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        print(f"Error fetching comments: {result.stderr}")
        return []

    all_comments = json.loads(result.stdout)
    bugbot_logins = {"cursor[bot]"}
    return [
        c for c in all_comments
        if c.get("user", {}).get("login", "") in bugbot_logins
    ]


# ── File / language helpers ──────────────────────────────────────────────────

def detect_language(file_path):
    """Return (lang_dir, glossary_code, display_name) from a _lang/ path."""
    m = re.match(r"_lang/([^/]+)/", file_path)
    if not m:
        return None, None, None
    lang_dir = m.group(1)
    info = LANGUAGES.get(lang_dir)
    if info:
        return lang_dir, info["glossary"], info["name"]
    return lang_dir, None, None


def english_source_path(file_path):
    """Derive the English source path for a _lang/ translated file."""
    m = re.match(r"_lang/[^/]+/(.*)", file_path)
    if not m:
        return None
    relative = m.group(1)
    for prefix in ["_docs/", "_includes/", ""]:
        candidate = REPO_ROOT / (prefix + relative)
        if candidate.exists():
            return candidate
    return None


def load_glossary(glossary_code):
    if not glossary_code:
        return {}
    path = GLOSSARY_DIR / f"{glossary_code}.json"
    return json.loads(path.read_text("utf-8")) if path.exists() else {}


def load_translation_rules():
    path = SCRIPTS_DIR / "translation_prompt.md"
    return path.read_text("utf-8") if path.exists() else ""


def read_window(file_path, center_line=None, half_window=25):
    """Read a window of content from a file, centered on a line."""
    p = REPO_ROOT / file_path
    if not p.exists():
        return ""
    lines = p.read_text("utf-8").splitlines()
    if center_line is None or center_line < 1:
        return "\n".join(lines[:80])
    start = max(0, center_line - half_window - 1)
    end = min(len(lines), center_line + half_window)
    numbered = [f"{i+1:4d}| {l}" for i, l in enumerate(lines[start:end], start=start)]
    return "\n".join(numbered)


# ── Claude evaluation ────────────────────────────────────────────────────────

SYSTEM_PROMPT = """\
You are a translation quality reviewer for Braze documentation. You evaluate
review comments from Cursor Bugbot on machine-translated documentation and
decide which fixes to apply.

## Decision criteria

Apply a fix when:
- Product names are incorrectly cased (Canvas, Campaign, Braze, etc. must be capitalized)
- SDK/platform names are incorrectly cased (Cordova, Roku, etc.)
- Grammar errors (gender agreement, verb conjugation, etc.)
- Genuine typos or formatting inconsistencies in the translation

Dismiss a comment when:
- It suggests translating a term that should stay in English per our glossary
  (e.g., Braze product names, technical terms)
- It conflicts with the translation rules (e.g., keeping English product names)
- The current text is actually correct

## Response format

Respond with ONLY a JSON array (no markdown fences, no extra text). One object
per comment:

[
  {
    "comment_id": 123456,
    "valid": true,
    "reason": "brief explanation",
    "fix": {
      "file": "_lang/fr_fr/path/to/file.md",
      "old_string": "exact substring to replace",
      "new_string": "replacement"
    },
    "glossary_update": {
      "glossary_code": "fr",
      "old_key": "canvas",
      "new_key": "Canvas",
      "value": "Canvas"
    }
  }
]

- Set "fix" to null if no file change needed.
- Set "glossary_update" to null if no glossary change needed.
- "old_key" in glossary_update is the existing key to remove (null if adding new).
- "new_key" is the key to add/update.
- The "old_string" MUST be an exact substring of the current file content.
"""


def build_user_prompt(comments, rules_excerpt):
    """Build the user prompt with all comments and their context."""
    sections = [f"## Translation rules (excerpt)\n\n{rules_excerpt}\n"]

    for i, ctx in enumerate(comments, 1):
        s = f"### Comment {i} (ID: {ctx['id']})\n"
        s += f"**File:** `{ctx['file']}`\n"
        s += f"**Language:** {ctx['language']}\n"
        s += f"**Bugbot says:**\n{ctx['body']}\n\n"
        s += f"**Diff context:**\n```\n{ctx['diff_hunk']}\n```\n\n"
        s += f"**File context (around line {ctx['line']}):**\n```\n{ctx['file_context']}\n```\n\n"

        if ctx.get("english_excerpt"):
            s += f"**English source excerpt:**\n```\n{ctx['english_excerpt']}\n```\n\n"

        if ctx.get("glossary"):
            relevant = {k: v for k, v in ctx["glossary"].items()
                        if any(k.lower() in ctx["body"].lower()
                               or v.lower() in ctx["body"].lower()
                               for _ in [None])}
            if not relevant:
                relevant = dict(list(ctx["glossary"].items())[:20])
            s += f"**Glossary ({ctx['glossary_code']}):**\n```json\n{json.dumps(relevant, ensure_ascii=False, indent=2)}\n```\n"

        sections.append(s)

    return "\n---\n".join(sections)


def evaluate_comments(client, comment_contexts):
    """Send all comments to Claude and parse the evaluation."""
    rules = load_translation_rules()
    rules_excerpt = rules[:5000]

    user_prompt = build_user_prompt(comment_contexts, rules_excerpt)

    response = client.messages.create(
        model=REVIEW_MODEL,
        max_tokens=4096,
        temperature=0,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": user_prompt}],
    )

    text = response.content[0].text.strip()
    if text.startswith("```"):
        text = re.sub(r"```(?:json)?\n?", "", text).rstrip("`").strip()

    try:
        return json.loads(text)
    except json.JSONDecodeError as e:
        print(f"ERROR: Failed to parse Claude response as JSON: {e}")
        print(f"Raw response:\n{text[:2000]}")
        return []


# ── Apply fixes ──────────────────────────────────────────────────────────────

def apply_fix(fix):
    """Apply a single text replacement. Returns True on success."""
    if not isinstance(fix, dict):
        print(f"  WARN: malformed fix (not a dict): {type(fix).__name__}")
        return False
    for key in ("file", "old_string", "new_string"):
        if not isinstance(fix.get(key), str) or not fix[key]:
            print(f"  WARN: malformed fix — missing or empty '{key}'")
            return False

    path = REPO_ROOT / fix["file"]
    if not path.exists():
        return False
    content = path.read_text("utf-8")
    if fix["old_string"] not in content:
        return False
    content = content.replace(fix["old_string"], fix["new_string"], 1)
    path.write_text(content, "utf-8")
    return True


def apply_glossary_update(update):
    """Apply a glossary key/value update. Returns True on success."""
    if not isinstance(update, dict):
        return False
    code = update.get("glossary_code")
    new_key = update.get("new_key")
    if not isinstance(code, str) or not code:
        return False
    if not isinstance(new_key, str) or not new_key:
        return False
    if "value" not in update:
        return False

    path = GLOSSARY_DIR / f"{code}.json"
    if not path.exists():
        return False

    glossary = json.loads(path.read_text("utf-8"))

    old_key = update.get("old_key")
    if isinstance(old_key, str) and old_key in glossary:
        glossary.pop(old_key)

    glossary[new_key] = update["value"]

    path.write_text(
        json.dumps(glossary, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return True


# ── Summary ──────────────────────────────────────────────────────────────────

def generate_summary(results, applied, dismissed, glossary_updates):
    lines = ["## Bugbot review — automated evaluation\n"]
    lines.append(
        f"**Evaluated by:** Claude | "
        f"**Comments:** {len(results)} | "
        f"**Applied:** {len(applied)} | "
        f"**Dismissed:** {len(dismissed)} | "
        f"**Glossary updates:** {len(glossary_updates)}\n"
    )

    if applied:
        lines.append("### Applied fixes\n")
        lines.append("| File | Change | Reason |")
        lines.append("|------|--------|--------|")
        for r in applied:
            fix = r.get("fix") or {}
            f = f"`{fix.get('file', '?')}`"
            old = (fix.get("old_string") or "")[:50].replace("|", "\\|")
            new = (fix.get("new_string") or "")[:50].replace("|", "\\|")
            reason = (r.get("reason") or "").replace("|", "\\|")
            lines.append(f"| {f} | `{old}` → `{new}` | {reason} |")
        lines.append("")

    if dismissed:
        lines.append("### Dismissed\n")
        lines.append("| Comment | Reason |")
        lines.append("|---------|--------|")
        for r in dismissed:
            body = (r.get("_bugbot_body") or "")[:80].replace("|", "\\|")
            reason = (r.get("reason") or "").replace("|", "\\|")
            lines.append(f"| {body}… | {reason} |")
        lines.append("")

    if glossary_updates:
        lines.append("### Glossary updates applied\n")
        for u in glossary_updates:
            old = u.get("old_key") or "(new)"
            lines.append(
                f"- `{u['glossary_code']}.json`: "
                f"`{old}` → `{u['new_key']}` = `{u['value']}`"
            )
        lines.append("")

    if not applied and not dismissed:
        lines.append("Bugbot found no inline issues. PR is ready for human review.\n")

    return "\n".join(lines)


# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    if not PR_NUMBER:
        print("ERROR: PR_NUMBER environment variable is required")
        sys.exit(1)

    print(f"Fetching Bugbot comments for PR #{PR_NUMBER}...")
    raw_comments = fetch_bugbot_comments()
    print(f"Found {len(raw_comments)} Bugbot inline comment(s)")

    if not raw_comments:
        summary = generate_summary([], [], [], [])
        SUMMARY_FILE.write_text(summary, encoding="utf-8")
        _set_output("fixes_applied", "0")
        return

    comment_contexts = []
    for c in raw_comments:
        file_path = c.get("path", "")
        line = c.get("original_line") or c.get("line")
        _, glossary_code, display_name = detect_language(file_path)

        ctx = {
            "id": c["id"],
            "file": file_path,
            "line": line,
            "body": c.get("body", ""),
            "diff_hunk": c.get("diff_hunk", ""),
            "language": display_name or "Unknown",
            "glossary_code": glossary_code,
            "file_context": read_window(file_path, line),
        }

        src = english_source_path(file_path)
        if src:
            ctx["english_excerpt"] = src.read_text("utf-8")[:3000]

        if glossary_code:
            ctx["glossary"] = load_glossary(glossary_code)

        comment_contexts.append(ctx)

    print("Evaluating comments with Claude...")
    client = _get_client()
    results = evaluate_comments(client, comment_contexts)

    if not isinstance(results, list):
        print(f"ERROR: Claude returned {type(results).__name__} instead of list — skipping")
        results = []
    results = [r for r in results if isinstance(r, dict)]

    comment_body_map = {c["id"]: c.get("body", "") for c in raw_comments}

    applied = []
    dismissed = []
    glossary_updates = []

    for r in results:
        r["_bugbot_body"] = comment_body_map.get(r.get("comment_id"), "")

        if r.get("valid") and r.get("fix"):
            if apply_fix(r["fix"]):
                applied.append(r)
                print(f"  Applied: {r['fix']['file']} — {r.get('reason', '')}")
            else:
                r["reason"] = f"Fix could not be applied: {r.get('reason', '')}"
                dismissed.append(r)
                print(f"  Failed:  {r['fix']['file']} — {r['reason']}")
        else:
            dismissed.append(r)
            print(f"  Dismissed: {r.get('reason', 'no reason')}")

        if r.get("glossary_update"):
            if apply_glossary_update(r["glossary_update"]):
                glossary_updates.append(r["glossary_update"])
                print(f"  Glossary: {r['glossary_update']['glossary_code']}.json updated")

    summary = generate_summary(results, applied, dismissed, glossary_updates)
    SUMMARY_FILE.write_text(summary, encoding="utf-8")

    total_changes = len(applied) + len(glossary_updates)
    _set_output("fixes_applied", str(total_changes))

    print(f"\nDone: {len(applied)} fix(es), {len(dismissed)} dismissed, "
          f"{len(glossary_updates)} glossary update(s)")


def _set_output(key, value):
    """Set a GitHub Actions output variable."""
    out = os.environ.get("GITHUB_OUTPUT")
    if out:
        with open(out, "a") as f:
            f.write(f"{key}={value}\n")


if __name__ == "__main__":
    main()
