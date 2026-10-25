# 2. Style

Rules for sentences, words and structure. They make text easier to read aloud, quicker to scan and harder to mistake for filler. [`prose-check`](../README.md#prose-check) automates the mechanical parts.

## 2.1 Vary sentence length

Text where every sentence is 15–20 words long reads like a drone. Mix them. A short sentence lands a point. A longer one can carry an idea through a condition and a consequence before it stops, which gives the short ones something to contrast with. Then a medium one consolidates.

Check by reading aloud: if you run out of breath, split the sentence; if every sentence has the same beat, merge two or cut one down.

Rhythm applies to structure too. If a page has eight cards, FAQs or case studies and every one follows the same shape (name, number, claim, takeaway), the reader predicts the fourth before reading it. Vary the openings and the lengths: lead one with a number, another with a short verdict, let one run to four sentences and another stop at one.

## 2.2 Prefer plain words

| Instead of | Use |
|---|---|
| utilize, leverage (verb) | use |
| facilitate | help, make possible |
| commence | start |
| in order to | to |
| a wide range of | name two or three |
| at this point in time | now |

The [plainlanguage.gov guidelines](https://www.plainlanguage.gov/guidelines/) and the [Google developer documentation style guide](https://developers.google.com/style) cover this in depth.

## 2.3 Overused words and stock phrases

These are flagged because drafts lean on them instead of saying something specific. None is wrong in itself; keep one when it is genuinely the most precise word. The full list with suggested replacements is in [`prose_check/phrases.py`](../prose_check/phrases.py).

- **Words:** delve, tapestry, testament, underscore, pivotal, robust, holistic, seamless, leverage, synergy, transformative, game-changer, cutting-edge, elevate, unlock, empower, landscape (as metaphor), realm
- **Place clichés:** bustling, vibrant, thriving. Each one stands in for a detail the writer did not supply.
- **Transitions:** furthermore, moreover, additionally, "it's important to note that", "it goes without saying", "needless to say"
- **Openers:** "In today's fast-paced world", "In this article we will", "Have you ever wondered", "When it comes to"
- **Closers:** "In conclusion", "In summary", then a repeat of the introduction

## 2.4 Openings and endings

- **Open with the point**: a problem, a result, a number or a short story. Not a definition (the reader searched for the term, so they know roughly what it is) and not a promise of what the article will do.
- **Cut the warm-up.** Drafts, especially model drafts, spend the first paragraph clearing their throat. Delete it and see if the second paragraph is a better start. It usually is.
- **End with something the reader can do**: a next step, a decision rule, or an honest open question. Don't summarise what they just read.

## 2.5 Paragraphs and scanning

- Two to four sentences per paragraph for anything read on a phone.
- Headings that read as the question the reader would type ("How long does a CSV import take?") rather than labels ("Performance").
- Numbered lists only when order matters; bullets otherwise.
- A table when comparing more than two things on more than two attributes.

## 2.6 Voice

- Contractions and second person ("you'll", "your team") suit most business and product writing. Formal documents (policies, contracts, regulatory text) are the exception.
- A named author byline promises a person. If the page carries one, the text should contain at least an occasional first-hand observation that only that person could make, and that observation must be real.
- One clear point of view beats a balanced list of everything. Where you are unsure, say so and say why.
