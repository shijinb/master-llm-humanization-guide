"""Turns Markdown or plain text into paragraphs and sentences for the rules to inspect."""

from __future__ import annotations

import re
from dataclasses import dataclass

# Abbreviations whose trailing period does not end a sentence.
_ABBREVIATIONS = set(
    "e.g i.e etc vs mr mrs ms dr prof inc ltd co no fig approx jan feb mar apr jun jul aug sep sept oct nov dec st jr sr".split()
)

_FENCE = re.compile(r"^(```|~~~)")
_SENTENCE_END = re.compile(r"([.!?]+[\"')\]]*)\s+(?=[\"'(\[]?[A-Z0-9])")
_WORD = re.compile(r"[A-Za-z0-9][A-Za-z0-9'’-]*")
_INLINE_CODE = re.compile(r"`[^`]*`")
_LINK = re.compile(r"!?\[([^\]]*)\]\([^)]*\)")
_URL = re.compile(r"https?://\S+")


@dataclass(frozen=True)
class Paragraph:
    line: int  # 1-based line number where the paragraph starts
    text: str
    kind: str  # "prose", "heading", "list", "quote", "table"


@dataclass(frozen=True)
class Sentence:
    line: int
    text: str

    @property
    def words(self) -> int:
        return len(_WORD.findall(self.text))


def _clean_inline(text: str) -> str:
    text = _INLINE_CODE.sub("code", text)
    text = _LINK.sub(r"\1", text)
    text = _URL.sub("link", text)
    text = re.sub(r"[*_]{1,3}([^*_]+)[*_]{1,3}", r"\1", text)
    return re.sub(r"\s+", " ", text).strip()


def _kind(line: str) -> str:
    stripped = line.lstrip()
    if stripped.startswith("#") or re.fullmatch(r"(\*\*|__)[^*_]+(\*\*|__)", stripped.strip()):
        return "heading"  # a line that is entirely bold works as a heading
    if stripped.startswith(">"):
        return "quote"
    if stripped.startswith("|"):
        return "table"
    if re.match(r"([-*+]|\d+[.)])\s", stripped):
        return "list"
    return "prose"


def paragraphs(source: str) -> list[Paragraph]:
    """Splits text into paragraphs, skipping fenced code blocks, HTML comments and front matter."""
    lines = source.splitlines()
    result: list[Paragraph] = []
    buffer: list[str] = []
    start = 0
    kind = "prose"
    in_fence = False
    in_comment = False

    def flush() -> None:
        nonlocal buffer
        if buffer:
            text = _clean_inline(" ".join(part.lstrip("#>-*+ ").strip() for part in buffer))
            if text:
                result.append(Paragraph(start, text, kind))
        buffer = []

    index = 0
    if lines and lines[0].strip() == "---":  # YAML front matter
        index = next((i + 1 for i in range(1, len(lines)) if lines[i].strip() == "---"), 0)

    for number, line in enumerate(lines[index:], start=index + 1):
        if _FENCE.match(line.strip()):
            flush()
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if "<!--" in line:
            in_comment = "-->" not in line
            continue
        if in_comment:
            in_comment = "-->" not in line
            continue

        line_kind = _kind(line)
        if not line.strip():
            flush()
            continue
        # Headings and list items are paragraphs of their own.
        if line_kind in ("heading", "list") or (buffer and line_kind != kind):
            flush()
        if not buffer:
            start, kind = number, line_kind
        buffer.append(line)
        if line_kind == "heading":
            flush()

    flush()
    return result


def sentences(paragraph: Paragraph) -> list[Sentence]:
    parts: list[str] = []
    position = 0
    for match in _SENTENCE_END.finditer(paragraph.text):
        candidate = paragraph.text[position : match.end(1)]
        last_word = candidate.rstrip(".!?\"')]").rsplit(" ", 1)[-1].lower()
        if last_word in _ABBREVIATIONS or re.fullmatch(r"[a-z]", last_word):
            continue  # "e.g." or an initial such as "J."
        parts.append(candidate)
        position = match.end()
    parts.append(paragraph.text[position:])
    return [Sentence(paragraph.line, part.strip()) for part in parts if part.strip()]


def word_count(text: str) -> int:
    return len(_WORD.findall(text))
