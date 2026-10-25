# Prompt: update existing content

For changing a live page without losing what is already right. Paste the **current live text**, not an old draft (see guide/05-accuracy.md §5.4).

```text
CURRENT TEXT (live as of {date}, from {URL or CMS record ID + slug})
"""
{paste}
"""

CHANGES
- Add: {new fact, with source}
- Update: {old statement} → {new statement} (source: {…})
- Remove: {what and why}

RULES
- Change only what is listed under CHANGES, plus sentences that become wrong because of them.
- Keep every other sentence, heading, link, number and name exactly as it is.
- Do not add facts that are not in CHANGES. Write [NEEDS: …] if something is missing.
- Keep the existing structure and heading order unless a change requires otherwise.

OUTPUT
1. The full updated text.
2. "Diff": each changed sentence, before → after.
3. "Unrelated issues noticed": problems you saw but did not change (broken link, outdated figure, duplicate tracking code).
```
