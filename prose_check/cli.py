"""prose-check: editorial checks for drafts (Markdown or plain text).

Usage:
    prose-check draft.md
    prose-check --format json --fail-on warning docs/*.md
    cat draft.txt | prose-check -
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path
from typing import TypedDict

from prose_check import __version__
from prose_check.rules import RULES, Finding, Options, run
from prose_check.text import paragraphs, sentences, word_count


class Summary(TypedDict):
    words: int
    sentences: int
    mean_sentence_words: float
    shortest_sentence_words: int
    longest_sentence_words: int


class FileReport(TypedDict):
    file: str
    summary: Summary
    findings: list[dict[str, object]]


def summary(source: str) -> Summary:
    doc = paragraphs(source)
    lengths = [s.words for p in doc if p.kind == "prose" for s in sentences(p)]
    return {
        "words": sum(word_count(p.text) for p in doc),
        "sentences": len(lengths),
        "mean_sentence_words": round(sum(lengths) / len(lengths), 1) if lengths else 0,
        "shortest_sentence_words": min(lengths, default=0),
        "longest_sentence_words": max(lengths, default=0),
    }


def check(source: str, options: Options, only: set[str] | None = None) -> list[Finding]:
    return run(paragraphs(source), options, only)


def _print_text(report: list[FileReport]) -> None:
    for entry in report:
        stats = entry["summary"]
        print(
            f"{entry['file']}: {stats['words']} words, {stats['sentences']} sentences, "
            f"sentence length {stats['shortest_sentence_words']}–{stats['longest_sentence_words']} "
            f"(mean {stats['mean_sentence_words']})"
        )
        for finding in entry["findings"]:
            print(f"  {entry['file']}:{finding['line']}: {finding['severity']} [{finding['rule']}] {finding['message']}")
            if finding["excerpt"]:
                print(f"      {finding['excerpt']}")
        counts = Counter(finding["severity"] for finding in entry["findings"])
        print(f"  {counts['warning']} warning(s), {counts['info']} info\n")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="prose-check",
        description="Editorial checks for drafts. Findings are prompts for an editor, not verdicts.",
    )
    parser.add_argument("files", nargs="+", help="Markdown or text files; '-' reads standard input")
    parser.add_argument("--format", choices=["text", "json"], default="text")
    parser.add_argument("--rules", help=f"Comma-separated subset of: {', '.join(RULES)}")
    parser.add_argument(
        "--fail-on",
        choices=["warning", "info", "never"],
        default="never",
        help="Exit 1 if a finding of this severity (or higher) is present",
    )
    parser.add_argument(
        "--long-sentence",
        type=int,
        default=Options.long_sentence,
        help="Words above which a sentence is flagged (default %(default)s)",
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    args = parser.parse_args(argv)

    only = set(args.rules.split(",")) if args.rules else None
    if only and (unknown := only - set(RULES)):
        parser.error(f"unknown rule(s): {', '.join(sorted(unknown))}")
    options = Options(long_sentence=args.long_sentence)

    report: list[FileReport] = []
    for name in args.files:
        source = sys.stdin.read() if name == "-" else Path(name).read_text(encoding="utf-8")
        findings = check(source, options, only)
        report.append({"file": name, "summary": summary(source), "findings": [f.as_dict() for f in findings]})

    if args.format == "json":
        print(json.dumps(report, indent=2, ensure_ascii=False))
    else:
        _print_text(report)

    severities = {finding["severity"] for entry in report for finding in entry["findings"]}
    if args.fail_on == "warning" and "warning" in severities:
        return 1
    if args.fail_on == "info" and severities:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
