"""Overused words and stock phrases, with a plainer alternative.

None of these are wrong in themselves. They are flagged because drafts (human or model-written) lean on
them in place of saying something specific. Keep one when it is the most precise word available.
"""

# phrase -> suggestion. Matched case-insensitively on word boundaries; "*" is a wildcard for word endings.
OVERUSED: dict[str, str] = {
    "delve*": "look at / examine, or cut",
    "tapestry": "say what the parts are",
    "testament to": "shows",
    "underscore*": "show / stress",
    "pivotal": "important, or say why it matters",
    "robust": "say what it withstands",
    "holistic": "say what is included",
    "seamless*": "say what no longer breaks",
    "leverag*": "use",
    "utiliz*": "use",
    "facilitat*": "help / make possible",
    "synerg*": "say what each side contributes",
    "game-changer": "say what changed, with a number",
    "revolutioni*": "say what is different",
    "transformative": "say what changes",
    "cutting-edge": "say what is new",
    "state-of-the-art": "say what is new",
    "embark*": "start",
    "elevate*": "improve, and by how much",
    "unlock*": "enable / allow",
    "empower*": "let / help",
    "landscape": "market / field, or cut",
    "realm": "area, or cut",
    "navigate the": "deal with / work through",
    "bustling": "a specific detail instead",
    "vibrant": "a specific detail instead",
    "thriving": "a number instead",
    "in today's fast-paced world": "cut; start with the point",
    "in today's digital age": "cut; start with the point",
    "in the ever-evolving": "cut",
    "it's important to note that": "cut; state the point",
    "it is important to note that": "cut; state the point",
    "it's worth noting that": "cut; state the point",
    "it goes without saying": "cut",
    "needless to say": "cut",
    "at the end of the day": "cut",
    "in conclusion": "end on a next step or open question",
    "in summary": "end on a next step or open question",
    "furthermore": "and / also, or start a new paragraph",
    "moreover": "and / also, or start a new paragraph",
    "additionally": "also, or cut",
    "a wide range of": "name two or three",
    "plays a crucial role": "say what it does",
    "plays a vital role": "say what it does",
}

# Vague quantities: flagged as a hint to use a number where one is known.
VAGUE: dict[str, str] = {
    "significant*": "how much?",
    "numerous": "how many?",
    "a number of": "how many?",
    "various": "which ones?",
    "very": "a stronger word or a number",
    "extremely": "a number",
    "incredibly": "a number",
}

# Openers that delay the point.
WEAK_OPENERS: tuple[str, ...] = (
    "in today's",
    "in this article",
    "in this blog",
    "have you ever wondered",
    "imagine a world",
    "when it comes to",
    "as we all know",
)
