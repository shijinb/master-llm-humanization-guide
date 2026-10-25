# 3. Formats and content types

The same facts need a different shape depending on where and how they are read.

## 3.1 Blog article

- Open with the problem, a result or a short story, never a definition.
- H2/H3 headings phrased as questions people actually ask.
- Paragraphs of 2–4 lines; at least one table or comparison if the topic allows it.
- FAQs only if they are real questions from customers, support tickets or search data, not invented ones.

## 3.2 Landing or product page

- Hero: the outcome, not the feature ("Close the month in two days", not "Automated reconciliation engine").
- Structure: problem → proof → offer. Proof (a number, a named customer with permission, a screenshot) belongs in the first screen.
- One primary call to action, worded as the action ("Import a sample file"), not "Learn more".
- No block longer than about 80 words without a visual break.

## 3.3 Variant pages (per city, industry, product line)

Templated pages fail when one could be swapped for another and still make sense. The test: *could this section appear on a different variant's page unchanged?* If yes, it is not specific enough.

- Each variant needs its own opening problem, examples and FAQs from real knowledge of that variant.
- Keep a **facts sheet** per variant ([template](../templates/facts-sheet.md)) and only write from it.
- Run a separate pass for non-visible details that templates copy silently: tracking parameters, IDs, canonical URLs, schema markup (see [Production lessons](09-production-lessons.md)).

## 3.4 Technical documentation

- Lead with what the reader is trying to do, then the minimum steps to do it.
- Every command, path, setting name and API field must be copied from the real system and tested, never written from memory or generated.
- State prerequisites and versions up front; state limitations and known issues honestly.
- Prefer one complete working example over three partial ones.
- Use the same term for the same thing throughout ("workspace" or "project", not both).

## 3.5 Resumes and LinkedIn profiles

AI assistance is legitimate here for structure, wording and trimming. Content is a different matter: **every claim must be true and attributable to the candidate.**

- Bullet pattern: action + scope + result. "Rebuilt the invoice import (Python, 40k rows/day), cutting failed imports from 3% to 0.2%."
- Numbers must be ones the candidate can explain in an interview. If a figure is an estimate, phrase it as one ("roughly", "about").
- Do not let a model add skills, tools, titles, employers or achievements that the candidate did not supply. Provide the facts; ask the model only to phrase them (see the [resume template](../templates/prompt-resume-bullets.md)).
- Tailoring to a job description means reordering and emphasising real experience, not inventing matching keywords.

## 3.6 Business email

- Subject line: the topic and the ask ("Invoice import: approve sample by Thu").
- First sentence: the point. Context after it.
- One request per email, with a date if there is one.
- Under ~200 words before the ask.

## 3.7 Marketing and social posts

- First line carries the post: a specific number, a short story or a clear opinion.
- One idea per line on LinkedIn; white space is formatting.
- At most three hashtags, at the end.
- Claims follow the same rules as everywhere else: no invented statistics, customer quotes or results.

## 3.8 Tone by audience

| Audience | Tone |
|---|---|
| Practitioners (engineers, recruiters, accountants) | Peer to peer. Skip the basics, use their terms, be exact about time and cost. |
| Executives | Business impact first. Assume they read the first paragraph and decide. A clear recommendation. |
| Enterprise buyers | Measured, data-backed. Acknowledge complexity, compliance and integration. |
| Job seekers or consumers | Warm, direct, honest. Second person. Don't oversell. |
| Regulators, legal, policy | Formal, precise, no contractions, every term defined once. |
