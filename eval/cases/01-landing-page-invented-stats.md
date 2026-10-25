# Case 01: Landing page with invented statistics

## Brief
Landing page hero and first section for a CSV invoice-import feature. Reader: finance manager at a 30–100 person company. Facts: imports up to 50,000 rows; median 1 min 40 s for 50,000 rows (internal benchmark, Oct 2026); merged cells not supported; free on all plans.

## Draft under review
> **Revolutionize Your Finance Workflow**
>
> In today's fast-paced world, finance teams need robust solutions. Our cutting-edge import feature is trusted by over 10,000 companies and reduces processing time by 87%. Furthermore, it seamlessly integrates with all major accounting platforms.

## Expected findings
| Criterion | Score | Why |
|---|---|---|
| Accuracy | 0 | "10,000 companies", "87%" and "all major accounting platforms" are not in the facts |
| Honesty | 0 | Invented social proof |
| Specificity | 0 | No real figure used, though one was supplied |
| Cliché-free | 0 | revolutionize, in today's fast-paced world, robust, cutting-edge, furthermore, seamlessly |
| Structure | 1 | Hero states no outcome; no call to action |

`prose-check --fail-on warning` should exit 1 (overused phrases, weak opening).

**Verdict:** fails both gates. Rewrite from the facts: "Import 50,000 invoice rows in under two minutes. Free on every plan."
