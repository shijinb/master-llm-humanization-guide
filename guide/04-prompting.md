# 4. Prompt design

A model writes generic text when it is given a generic request. Most of the quality of an AI-assisted draft is decided before the model writes a word, by what goes into the prompt.

## 4.1 The structure that works

Ready-to-use versions are in [`templates/`](../templates/).

```text
ROLE AND READER
You are writing for {reader}, who already knows {what they know} and needs to {decision or task}.

FACTS (use only these; do not add others)
- {fact, with source}
- {measured result, with date}
- {limitation or trade-off}

TASK
Write a {format} of about {length} that {goal}.

CONSTRAINTS
- Tone: {preset from guide/03-formats.md §3.8}
- Do not invent statistics, customers, quotes, dates or experiences. If a fact is missing, write [NEEDS: ...] instead.
- Avoid the phrases in guide/02-style.md §2.3.
- {format-specific rules}

OUTPUT
{exact shape: headings, word counts, a list of claims with their source}
```

## 4.2 Patterns

| Pattern | When | How |
|---|---|---|
| **Facts block** | Always | Put verified facts in the prompt and forbid others. This is the main defence against invented details. |
| **Missing-fact markers** | Always | Ask for `[NEEDS: …]` placeholders instead of guesses. They are easy to search for and impossible to publish by accident if your checklist blocks them. |
| **Claims list** | Anything published | Ask the model to append every factual claim with the fact it came from. Review that list, not just the prose. |
| **Outline first** | Long pieces | Approve an outline, then draft section by section. Easier to steer, fewer repeated points. |
| **Edit, don't rewrite** | Updating live content | Supply the current text and a list of what to change; require everything else to stay. See [prompt-update-content](../templates/prompt-update-content.md). |
| **Critique pass** | Final drafts | Run the [review checklist](../templates/review-checklist.md) as a separate prompt against the draft, then fix the findings yourself. |
| **Structured output** | Content going into a CMS or app | Ask for JSON matching a schema and validate it before use; reject rather than repair malformed output. |

## 4.3 What not to put in prompts

- **Instructions to fake experience** ("write as if you personally tested this"). Supply real experience in the facts block or leave it out.
- **Confidential data** you are not allowed to send to the model provider: customer personal data, unreleased financials, credentials.
- **"Make it undetectable"** or similar. It optimises for the wrong target and, in academic or contractual settings, can be dishonest. See [Ethics](08-ethics.md).

## 4.4 Versioning prompts

Treat prompts that are reused (by a team or in a pipeline) like code:

- Keep them in version control next to the facts sheets they use.
- Give each a version and a changelog line when it changes.
- Re-run a few [evaluation cases](../eval/) after changing a prompt, and compare scores before and after.
