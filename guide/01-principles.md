# 1. Principles

Five ideas carry most of the weight. Everything else in this guide applies them to a specific situation.

## 1.1 Write for one reader with one job

Before drafting, answer three questions in a sentence each:

| Question | Weak answer | Useful answer |
|---|---|---|
| Who is reading? | "Businesses" | "An operations manager at a 40-person logistics firm who was asked to cut invoice errors" |
| What do they already know? | — | "They know their billing software; they don't know how our import works" |
| What should they be able to do afterwards? | "Understand our product" | "Decide whether the CSV import fits their month-end process, and try it on one file" |

A model given the useful answers writes a different, better draft than one given the weak answers. So does a person.

## 1.2 Every section must earn its place

Ask of each section: *could the reader get this from the first page of search results?* If yes, cut it or go further. A section earns its place when it contains at least one of:

- a number the reader could not easily find (a measured result, a threshold, a cost);
- first-hand experience: what happened when this was actually done;
- a trade-off or limitation, stated plainly;
- a worked example with real detail (size, timeline, outcome);
- a correction to common advice, with the reason.

This is often called **information gain**. It is the single best predictor of whether a piece is worth reading, and it is the part a model cannot invent: it has to come from the writer's own knowledge or from verified sources.

## 1.3 Specific beats impressive

Replace adjectives with the thing that justifies them.

| Instead of | Write |
|---|---|
| "a significantly faster process" | "month-end close dropped from 6 days to 2" |
| "trusted by many customers" | "used by 140 clinics in three states" (if true and countable) |
| "robust security" | "data is encrypted at rest with AES-256; access requires SSO" |

There are two kinds of specific detail. **Human-scale detail** is what a practitioner would say aloud: "about a 40-minute drive", "roughly 200 people". **Lookup-table detail** reads like a database export: coordinates, postcodes in a list, figures to four decimal places. Use the first by default; use the second only when the reader needs it, and sparingly.

## 1.4 Build on a claim instead of repeating it

Pages often state the same three benefits in the hero, a feature list, a sidebar and the closing section. Each repetition in slightly different words teaches nothing and signals a template. After the first mention, either refer back briefly or add something new: a number, a condition, an exception.

## 1.5 Accuracy is not negotiable

A fluent paragraph with one invented statistic is worse than a plain paragraph with none. Language models produce confident text regardless of whether it is true. Every factual claim needs a source the writer has checked (see [Accuracy and review](05-accuracy.md)), and anything that presents itself as experience must be experience someone actually had (see [Ethics](08-ethics.md)).
