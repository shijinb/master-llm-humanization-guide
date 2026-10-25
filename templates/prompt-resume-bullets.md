# Prompt: resume and profile bullets

The model rewords; the candidate supplies every fact. Nothing gets added.

```text
ROLE
{title} at {company type}, {dates}. Target role: {target}.

FACTS (from the candidate; true and explainable in an interview)
- {what I did} | scope: {team size, volume, systems} | result: {measured or estimated result}
- {…}
- Tools actually used: {list}

TASK
Write {n} resume bullets for this role.

RULES
- Pattern: action verb + what + scope + result.
- Use only the FACTS. Do not add tools, skills, titles, numbers, employers or achievements.
- If a result is an estimate in the facts, keep it hedged ("about", "roughly").
- If a bullet has no result, leave it without one. Do not invent one.
- No "responsible for", "helped with", "various", "leveraged", "spearheaded".
- Under 25 words per bullet.

OUTPUT
The bullets, then for each one the FACTS line it is based on.
```
