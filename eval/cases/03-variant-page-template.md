# Case 03: Variant pages that pass the style check but fail the swap test

## Brief
Two city pages for a hiring service, each with a "Why hire here" section. Facts sheets list different industries, commute patterns and salary bands for each city.

## Draft under review (identical apart from the city name)
> **Why hire in Eastport?** Eastport has a large and growing talent pool across many industries. Employers here benefit from competitive salaries and a strong local economy. Our platform helps you find the right candidates quickly.
>
> **Why hire in Westvale?** Westvale has a large and growing talent pool across many industries. Employers here benefit from competitive salaries and a strong local economy. Our platform helps you find the right candidates quickly.

## Expected findings
| Criterion | Score | Why |
|---|---|---|
| Information gain | 0 | Nothing from either facts sheet is used |
| Specificity | 0 | "large", "many", "competitive", "strong": no figures |
| Audience fit | 0 | Tells local employers nothing they don't know |
| Accuracy | 1 | Nothing false, but nothing checkable either |

**Swap test:** fails completely; each section fits the other page unchanged.

**Note:** `prose-check` finds little here (one vague quantity). This case shows why automated checks are not enough.
