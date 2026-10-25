# Prompt: new content

Copy, fill in every `{…}`, delete lines that don't apply. Facts must come from a source you have checked.

```text
ROLE AND READER
You are drafting a {blog article | landing page | help article} for {reader: role, company size, situation}.
They already know {what they know}. After reading they should be able to {decision or task}.

FACTS (use only these; do not add statistics, names, quotes, dates or experiences that are not listed)
- {fact} (source: {link or document}, checked {date})
- {measured result} (source: {…})
- {limitation or trade-off}
- {first-hand observation from {person}, used with permission}

TASK
Write about {length} words that {goal}. Main points, in order:
1. {point}
2. {point}
3. {point}

CONSTRAINTS
- Tone: {preset from guide/03-formats.md §3.8}.
- Open with {the problem | the result | a short story from the facts}. Do not open with a definition.
- Vary sentence length; keep paragraphs to 2–4 sentences.
- Do not use: delve, leverage, robust, seamless, furthermore, moreover, "in today's…", "in conclusion".
- Say each main point once. If it comes up again, add something new or refer back.
- If a fact you need is missing, write [NEEDS: what is missing] and continue.
- End with {a next step | a decision rule | an open question}.

OUTPUT
1. The draft in Markdown.
2. "Claims": a list of every factual claim in the draft and which FACTS line it came from.
3. "Gaps": every [NEEDS: …] you inserted.
```
