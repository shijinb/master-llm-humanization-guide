# 7. Evaluation

A shared rubric turns "this reads better" into something two reviewers can agree on, and lets you compare prompt versions or models on the same brief.

## 7.1 Rubric

Score each criterion 0, 1 or 2. The machine-readable version is [`eval/rubric.json`](../eval/rubric.json).

| # | Criterion | 0 | 1 | 2 |
|---|---|---|---|---|
| 1 | **Accuracy** | Any unsupported or false claim | All claims supported, but sources not recorded | Every claim traceable to a recorded source |
| 2 | **Information gain** | Restates common knowledge | Some sections add something new | Every major section adds a number, example, trade-off or first-hand point |
| 3 | **Audience fit** | Wrong level or tone for the reader | Mostly right, some lapses | Right assumed knowledge and tone throughout |
| 4 | **Specificity** | Mostly adjectives and vague quantities | Mixed | Claims carried by numbers, names and examples |
| 5 | **Structure and format** | Wrong shape for the channel | Right shape, weak opening or ending | Opens with the point, ends with an action, scannable |
| 6 | **Readability** | Monotone or hard to follow | Readable, some long or uniform stretches | Varied rhythm, plain words, reads well aloud |
| 7 | **Cliché-free** | Several overused phrases or filler transitions | One or two | None (or each one deliberate) |
| 8 | **Honesty** | Fabricated experience, testimonial or result | Overstated claims | Claims match the evidence; limitations stated |

**Publish threshold:** total ≥ 13 of 16, and **Accuracy = 2 and Honesty = 2**. Those two are gates, not points: a piece scoring 2 everywhere else still fails if either is below 2.

## 7.2 Test cases

[`eval/cases/`](../eval/cases/) holds briefs with a deliberately weak draft and the problems a reviewer should find. Use them to:

- calibrate new reviewers (score independently, then compare);
- compare prompts or models: same brief, score each output with the rubric;
- regression-test a prompt change: re-run the cases, check no score drops.

## 7.3 What automated checks can and cannot tell you

`prose-check` measures surface patterns: phrases, sentence lengths, paragraph size, repeated figures. It is useful for criteria 6 and 7 and as a nudge for 4. It **cannot** judge accuracy, honesty, audience fit or information gain; those need a person who knows the subject and has the sources open. Don't publish on a clean run alone.

Commercial "AI detector" scores are not a quality measure either; see [Ethics §8.3](08-ethics.md#83-ai-detectors).
