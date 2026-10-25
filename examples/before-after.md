# Before and after

Synthetic examples written for this repository. Companies, people and figures are invented for illustration and marked as such. In real use, every figure in an "after" must come from a checked source.

## 1. Blog opening

**Before**

> In today's fast-paced business landscape, invoice management plays a crucial role in the success of organizations. Invoices are documents that record transactions between buyers and sellers. In this article, we will delve into how automation can transform your accounts payable process.

**After** (figures from the writer's own measured pilot)

> Our accounts team used to spend the last three days of every month retyping supplier invoices. After we switched to CSV import, it took one afternoon, and the error rate on supplier totals fell from about 1 in 50 to 1 in 600. Here is what we changed, what went wrong in the first month, and when the import is not worth it.

**What changed:** the definition and the promise are cut; the opening carries a result with numbers, signals first-hand experience and tells the reader what follows, including the limitations.

## 2. Product claim

**Before**

> Our robust, cutting-edge platform seamlessly empowers teams to unlock unprecedented productivity.

**After**

> Imports of up to 50,000 rows finish in under two minutes on the standard plan (measured October 2026, median of 20 runs). Files with merged cells fail; export to plain CSV first.

**What changed:** five adjectives replaced by one measured claim with its conditions, plus a limitation the reader would otherwise discover the hard way.

## 3. Repeated blocks on a variant page

**Before** (every entry has the same shape)

> **Northgate** is located 12 km from the city centre and is home to many logistics companies, making it ideal for warehouse hiring.
> **Riverside** is located 8 km from the city centre and is home to many software companies, making it ideal for tech hiring.
> **Old Town** is located 3 km from the city centre and is home to many retail companies, making it ideal for retail hiring.

**After** (fictional city)

> **Northgate.** If you're hiring forklift drivers, start here: three of the region's largest distribution centres sit along the ring road, and shift workers mostly live within a 20-minute bus ride.
> Developers cluster in **Riverside**, but so do your competitors. Expect counter-offers.
> **Old Town** is retail, and seasonal: hiring for December starts in September.

**What changed:** each entry opens differently, varies in length, and says something that would only make sense for that area.

## 4. Resume bullet

**Facts supplied by the candidate:** rebuilt the nightly order export; Python; about 40,000 orders a day; failures went from roughly 3 a week to none in the following quarter.

**Before** (model output without a facts block)

> Spearheaded a transformative, AI-driven data pipeline initiative leveraging Python, Kafka and Spark, improving efficiency by 60%.

**After** (model output with the facts block and the resume template)

> Rebuilt the nightly order export in Python (about 40,000 orders/day); failed runs fell from roughly 3 a week to none over the next quarter.

**What changed:** the "before" invented Kafka, Spark, "AI-driven" and "60%". All of those would collapse in an interview. The "after" uses only what the candidate supplied.

## 5. Email

**Before**

> Subject: Following up!
>
> Hi Priya, I hope this email finds you well! I just wanted to circle back regarding the import project we discussed. As you know, there are various considerations to take into account. Please let me know your thoughts at your earliest convenience.

**After**

> Subject: Import pilot: approve the sample file by Thursday
>
> Hi Priya, could you approve the attached sample file by Thursday? If it looks right, we import the full supplier list on Monday. The only open question is the duplicate supplier codes on rows 14 and 92. Which one should we keep?

**What changed:** the ask, the deadline, the consequence and the one decision needed, in four sentences.
