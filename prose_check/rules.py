"""Editorial checks. Each rule takes the parsed document and yields findings.

These are prompts for a human editor, not verdicts: every finding names a pattern worth a second look.
"""

from __future__ import annotations

import re
import statistics
from collections import defaultdict
from collections.abc import Callable, Iterator
from dataclasses import dataclass

from prose_check.phrases import OVERUSED, VAGUE, WEAK_OPENERS
from prose_check.text import Paragraph, Sentence, sentences, word_count


@dataclass(frozen=True)
class Finding:
    rule: str
    severity: str  # "warning" | "info"
    line: int
    message: str
    excerpt: str = ""

    def as_dict(self) -> dict[str, object]:
        return {"rule": self.rule, "severity": self.severity, "line": self.line, "message": self.message, "excerpt": self.excerpt}


@dataclass(frozen=True)
class Options:
    long_sentence: int = 35  # words
    uniform_min_sentences: int = 5  # consecutive sentences needed before rhythm is judged
    uniform_max_spread: int = 8  # max - min word count within such a run
    max_paragraph_words: int = 120


Rule = Callable[[list[Paragraph], Options], Iterator[Finding]]


def _pattern(phrase: str) -> re.Pattern[str]:
    body = re.escape(phrase).replace(r"\*", r"\w*").replace(r"\ ", r"\s+")
    return re.compile(rf"(?<![\w-]){body}(?![\w-])", re.IGNORECASE)


_OVERUSED = [(phrase, _pattern(phrase), hint) for phrase, hint in OVERUSED.items()]
_VAGUE = [(phrase, _pattern(phrase), hint) for phrase, hint in VAGUE.items()]


def _excerpt(text: str, start: int, end: int, width: int = 30) -> str:
    left = max(0, start - width)
    right = min(len(text), end + width)
    return ("…" if left else "") + text[left:right] + ("…" if right < len(text) else "")


def overused_phrases(doc: list[Paragraph], options: Options) -> Iterator[Finding]:
    for paragraph in doc:
        for _phrase, pattern, hint in _OVERUSED:
            for match in pattern.finditer(paragraph.text):
                yield Finding(
                    "overused-phrase",
                    "warning",
                    paragraph.line,
                    f'"{match.group(0)}": {hint}',
                    _excerpt(paragraph.text, match.start(), match.end()),
                )


def vague_quantities(doc: list[Paragraph], options: Options) -> Iterator[Finding]:
    for paragraph in doc:
        if paragraph.kind == "heading":
            continue
        for _phrase, pattern, hint in _VAGUE:
            for match in pattern.finditer(paragraph.text):
                yield Finding(
                    "vague-quantity",
                    "info",
                    paragraph.line,
                    f'"{match.group(0)}": {hint}',
                    _excerpt(paragraph.text, match.start(), match.end()),
                )


def weak_opening(doc: list[Paragraph], options: Options) -> Iterator[Finding]:
    first = next((p for p in doc if p.kind == "prose"), None)
    if first is None:
        return
    lowered = first.text.lower()
    for opener in WEAK_OPENERS:
        if lowered.startswith(opener):
            yield Finding("weak-opening", "warning", first.line, f'Opens with "{opener}…": start with the point', first.text[:80])
    if re.match(r"^[A-Z][\w\s-]{0,40}\s(is|are)\s(a|an|the)\s", first.text):
        yield Finding("weak-opening", "info", first.line, "Opens with a definition: readers usually know it already", first.text[:80])


def long_sentences(doc: list[Paragraph], options: Options) -> Iterator[Finding]:
    for paragraph in doc:
        if paragraph.kind not in ("prose", "quote"):
            continue
        for sentence in sentences(paragraph):
            if sentence.words > options.long_sentence:
                yield Finding(
                    "long-sentence",
                    "info",
                    sentence.line,
                    f"{sentence.words} words: consider splitting",
                    sentence.text[:80] + ("…" if len(sentence.text) > 80 else ""),
                )


def uniform_rhythm(doc: list[Paragraph], options: Options) -> Iterator[Finding]:
    """Runs of prose sentences whose lengths sit in a narrow band read as monotonous when spoken aloud."""
    run: list[Sentence] = []

    def check() -> Iterator[Finding]:
        if len(run) >= options.uniform_min_sentences:
            lengths = [s.words for s in run]
            if max(lengths) - min(lengths) <= options.uniform_max_spread:
                yield Finding(
                    "uniform-rhythm",
                    "info",
                    run[0].line,
                    f"{len(run)} sentences in a row between {min(lengths)} and {max(lengths)} words "
                    f"(mean {statistics.mean(lengths):.0f}): vary the length where the content allows",
                )

    for paragraph in doc:
        if paragraph.kind != "prose":
            yield from check()
            run = []
            continue
        for sentence in sentences(paragraph):
            if run and abs(sentence.words - statistics.mean(s.words for s in run)) > options.uniform_max_spread:
                yield from check()
                run = []
            run.append(sentence)
    yield from check()


def long_paragraphs(doc: list[Paragraph], options: Options) -> Iterator[Finding]:
    for paragraph in doc:
        if paragraph.kind == "prose" and (count := word_count(paragraph.text)) > options.max_paragraph_words:
            yield Finding("long-paragraph", "info", paragraph.line, f"{count} words in one paragraph: hard to read on a phone")


_FIGURE = re.compile(r"(?<![\w.])(?:[$€£₹]\s?)?\d+(?:[,.]\d+)*\s?(?:%|percent|[kKmM]\b|lakhs?|crores?|hours?|days?|weeks?|minutes?)?")


def repeated_figures(doc: list[Paragraph], options: Options) -> Iterator[Finding]:
    """The same specific figure in several paragraphs is often a copy-paste slip in templated content.

    Small integers and years are ignored; percentages, money and numbers with units are checked.
    """
    seen: dict[str, list[int]] = defaultdict(list)
    for paragraph in doc:
        if paragraph.kind == "heading":
            continue
        for match in _FIGURE.finditer(paragraph.text):
            figure = match.group(0).strip()
            digits = re.sub(r"\D", "", figure)
            has_unit = bool(re.search(r"[%$€£₹a-zA-Z]", figure))
            is_year = re.fullmatch(r"(19|20)\d{2}", figure) is not None
            if is_year or (not has_unit and len(digits) < 3):
                continue
            if paragraph.line not in seen[figure.lower()]:
                seen[figure.lower()].append(paragraph.line)

    for figure, lines in seen.items():
        if len(lines) >= 2:
            yield Finding(
                "repeated-figure",
                "info",
                lines[1],
                f'"{figure}" appears in {len(lines)} paragraphs (lines {", ".join(map(str, lines))}): '
                "confirm each one is meant to be the same value",
            )


RULES: dict[str, Rule] = {
    "overused-phrase": overused_phrases,
    "vague-quantity": vague_quantities,
    "weak-opening": weak_opening,
    "long-sentence": long_sentences,
    "uniform-rhythm": uniform_rhythm,
    "long-paragraph": long_paragraphs,
    "repeated-figure": repeated_figures,
}


def run(doc: list[Paragraph], options: Options | None = None, only: set[str] | None = None) -> list[Finding]:
    options = options or Options()
    findings = [finding for name, rule in RULES.items() if only is None or name in only for finding in rule(doc, options)]
    return sorted(findings, key=lambda f: (f.line, f.rule))
