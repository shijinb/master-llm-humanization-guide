# 5. Accuracy, citations and human review

Fluent text is not evidence of correct text. Models generate plausible statistics, quotes, references and product details with the same confidence as real ones. This section is the safeguard.

## 5.1 Prevent invented content

1. **Ground the draft.** Put the facts in the prompt ([§4.2](04-prompting.md#42-patterns)) and forbid others.
2. **Ask for gaps, not guesses.** `[NEEDS: source for churn figure]` beats a made-up "37%".
3. **Get a claims list.** Every number, name, date, quote and comparison, with its source.
4. **Search the draft for `[NEEDS:`** before publishing. Any left means the piece is not finished.

## 5.2 Verify what remains

For every item on the claims list:

| Claim type | Check |
|---|---|
| Statistic | Open the original source (not a blog quoting it). Check the number, the date, the population and the definition. |
| Quote | Confirm the person said it, in those words, and agreed to be quoted. |
| Customer or partner name | Confirm permission to name them. |
| Product capability | Confirm it in the product, or with the team that owns it. Not from old marketing copy. |
| Price, limit, version | Check the current official page; note the date checked. |
| Law, regulation, medical, financial | Have a qualified person review it. A model's summary is not legal or medical advice. |
| Link | Open it. Models produce URLs that look right and do not exist. |

## 5.3 Citations

- Cite the primary source: the study, the official documentation, the dataset. Not a secondary article.
- Include enough to find it again: title, publisher or author, date, and a link.
- Record when you checked time-sensitive facts ("pricing as of 2026-10-25").
- Never ask a model to "add citations" to a finished draft. That is how fabricated references appear. Add sources you have read.

## 5.4 Source of truth

Before editing existing content, confirm **where the live version is**: the rendered page, the CMS record, the template. A database export or an old draft can differ from what readers see. Rewriting a stale copy produces a well-written, wrong page.

When content moves between systems (draft → CMS, template → export), **compare section by section** against the live source. Smooth reading does not mean nothing is missing.

## 5.5 Human review

Every published piece gets a named human reviewer who:

1. reads it start to finish against the brief;
2. checks the claims list against sources ([§5.2](#52-verify-what-remains));
3. runs the [review checklist](../templates/review-checklist.md);
4. signs off, with their name and the date, in the content's history or ticket.

The reviewer is accountable for the piece. AI assistance does not change that.

## 5.6 Disclosure

Follow the rules of the place you publish: some journals, schools, clients and platforms require AI assistance to be disclosed. Where nothing is required, ask whether a reasonable reader would feel misled to learn how the piece was made. If yes, disclose.
