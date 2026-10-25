# Master Guide to Humanizing LLM-Assisted Writing

A practical guide, prompt templates, an evaluation rubric and a small linter for AI-assisted writing. The aim: drafts that are **accurate, specific and useful to the person reading them**, from blog posts and product pages to technical docs, resumes and business email.

[![CI](https://github.com/shijinb/master-llm-humanization-guide/actions/workflows/ci.yml/badge.svg)](https://github.com/shijinb/master-llm-humanization-guide/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/python-3.10%2B-3776ab)
![Docs: CC BY 4.0](https://img.shields.io/badge/docs-CC%20BY%204.0-lightgrey)
![Code: MIT](https://img.shields.io/badge/code-MIT-green)

**Try it in a minute:**

```bash
pip install git+https://github.com/shijinb/master-llm-humanization-guide.git
prose-check your-draft.md
```

## Contents

- [Why this exists](#why-this-exists)
- [The guide](#the-guide)
- [Templates](#templates)
- [Evaluation](#evaluation)
- [prose-check](#prose-check)
- [What this is not](#what-this-is-not)
- [Sources and review date](#sources-and-review-date)
- [Versioning](#versioning)
- [Licence](#licence)

## Why this exists

Language models produce fluent drafts quickly. The problems show up afterwards. The same three claims repeat in every section, adjectives stand where numbers should be, and openings define the obvious. Worst of all are confident statistics, quotes and experiences that nobody can trace. This repository collects the practices that fixed those problems in a production content pipeline, written up so a team can apply them consistently.

The approach in one line: **give the model verified facts, ask it to mark gaps instead of filling them, then edit and review like a human editor would.**

## The guide

| # | Chapter | Covers |
|---|---|---|
| 1 | [Principles](guide/01-principles.md) | Reader and intent, information gain, specificity, building on claims, accuracy |
| 2 | [Style](guide/02-style.md) | Sentence rhythm, plain words, overused phrases, openings and endings, voice |
| 3 | [Formats and content types](guide/03-formats.md) | Blog, landing page, variant pages, technical docs, resumes, email, social; tone by audience |
| 4 | [Prompt design](guide/04-prompting.md) | Prompt structure, facts blocks, missing-fact markers, claims lists, prompt versioning |
| 5 | [Accuracy and review](guide/05-accuracy.md) | Preventing invented content, verification, citations, source of truth, human sign-off |
| 6 | [The editing pass](guide/06-editing.md) | An eight-step human edit, and targeted fixes |
| 7 | [Evaluation](guide/07-evaluation.md) | Scoring rubric, publish threshold, test cases |
| 8 | [Ethics and limits](guide/08-ethics.md) | No fabrication, authorship honesty, why AI detectors are not a goal, privacy |
| 9 | [Production lessons](guide/09-production-lessons.md) | What broke when templated content went live, and the checks that caught it |

## Templates

Copy, fill in, use. Each template forbids invented facts and asks for a claims list.

| Template | For |
|---|---|
| [prompt-new-content](templates/prompt-new-content.md) | Articles, landing pages, help pages |
| [prompt-update-content](templates/prompt-update-content.md) | Changing live content without losing what was right |
| [prompt-variant-page](templates/prompt-variant-page.md) | Per-city / per-industry pages that pass the swap test |
| [prompt-technical-doc](templates/prompt-technical-doc.md) | How-tos and references built from verified commands |
| [prompt-resume-bullets](templates/prompt-resume-bullets.md) | Resume bullets from the candidate's own facts only |
| [prompt-email](templates/prompt-email.md) | One-ask business email |
| [facts-sheet](templates/facts-sheet.md) | The single source drafts may draw from |
| [review-checklist](templates/review-checklist.md) | Pre-publish checks, including the accuracy and honesty gates |

[Before-and-after examples](examples/before-after.md) show each template's effect on synthetic content.

## Evaluation

[`eval/rubric.json`](eval/rubric.json) scores eight criteria from 0 to 2. A piece publishes at **13 of 16 or more, with accuracy and honesty both at 2**. [`eval/cases/`](eval/cases/) has four briefs, each with a flawed draft and the findings a reviewer should reach. Use them to calibrate reviewers and to compare prompts or models.

## prose-check

A dependency-free command-line linter for the mechanical part of the edit. It reads Markdown or plain text, skips code blocks, and reports:

| Rule | Severity | Flags |
|---|---|---|
| `overused-phrase` | warning | Stock words and phrases (list in [`prose_check/phrases.py`](prose_check/phrases.py)), with a plainer alternative |
| `weak-opening` | warning / info | Openers such as "In today's…", "In this article…", or a definition |
| `vague-quantity` | info | "significantly", "numerous", "various": prompts for a number |
| `long-sentence` | info | Sentences over 35 words (configurable) |
| `uniform-rhythm` | info | Five or more sentences in a row within an 8-word band |
| `long-paragraph` | info | Paragraphs over 120 words |
| `repeated-figure` | info | The same figure (percentage, money, number with unit) in several paragraphs, a common copy-paste slip |

```bash
pip install -e ".[dev]"                     # from a clone
prose-check draft.md                         # readable report
prose-check --format json docs/*.md          # for scripts
prose-check --fail-on warning draft.md       # exit 1 on warnings (CI gate)
prose-check --rules overused-phrase,weak-opening draft.md
cat draft.txt | prose-check -
```

Real output for the first "before" opening in the [examples](examples/before-after.md):

```text
-: 41 words, 3 sentences, sentence length 10–16 (mean 13.7)
  -:1: warning [overused-phrase] "delve": look at / examine, or cut
      …ers. In this article, we will delve into how automation can trans…
  -:1: warning [overused-phrase] "landscape": market / field, or cut
      …n today's fast-paced business landscape, invoice management plays a c…
  -:1: warning [overused-phrase] "plays a crucial role": say what it does
      …landscape, invoice management plays a crucial role in the success of organizatio…
  -:1: warning [weak-opening] Opens with "in today's…": start with the point
      In today's fast-paced business landscape, invoice management plays a crucial rol
  4 warning(s), 0 info
```

Findings are prompts for an editor, not verdicts. The tool cannot judge accuracy, honesty, audience fit or whether a section says anything new. [Case 03](eval/cases/03-variant-page-template.md) is a draft it passes that a reviewer must fail.

**Tests:** `pytest` covers the rules, parsing and CLI. It also checks that every link in these docs resolves, that the rubric is consistent, and that both the eval cases and the sample output above describe what the tool really does. `ruff` and `mypy --strict` run in CI.

## What this is not

- **Not a way to evade AI detectors.** Detectors are unreliable and are not a quality measure; see [Ethics §8.3](guide/08-ethics.md#83-ai-detectors).
- **Not a way to invent experience.** Nothing here helps fabricate credentials, testimonials, reviews or results, and the templates are written to stop models from doing it.
- **Not an SEO guarantee.** Better content can help; nothing guarantees rankings or rich results.

## Sources and review date

Reviewed **2026-10-25**.

- Google Search Central, [Google Search's guidance about AI-generated content](https://developers.google.com/search/blog/2023/02/google-search-and-ai-content) (Feb 2023)
- Google Search Central, [Creating helpful, reliable, people-first content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content)
- Google Search Central, [Spam policies](https://developers.google.com/search/docs/essentials/spam-policies)
- OpenAI, [New AI classifier for indicating AI-written text](https://openai.com/index/new-ai-classifier-for-indicating-ai-written-text/) (withdrawal note, July 2023)
- Liang, Yuksekgonul, Mao, Wu, Zou, [GPT detectors are biased against non-native English writers](https://doi.org/10.1016/j.patter.2023.100779), *Patterns* 4(7), 2023
- [plainlanguage.gov guidelines](https://www.plainlanguage.gov/guidelines/); [Google developer documentation style guide](https://developers.google.com/style)

## Versioning

The guide, templates and rubric are versioned together using [semantic versioning](https://semver.org/): **major** for changes to the rubric's criteria or threshold, **minor** for new chapters, templates or rules, **patch** for wording and fixes. See [CHANGELOG.md](CHANGELOG.md). Teams adopting the templates should pin a version and re-run the eval cases when upgrading.

## Licence

- Guide, templates, examples and eval cases: [CC BY 4.0](LICENSE-docs). Reuse and adapt with attribution.
- `prose_check` code and tests: [MIT](LICENSE).

Contributions: see [CONTRIBUTING.md](CONTRIBUTING.md).
