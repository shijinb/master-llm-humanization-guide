# 9. Lessons from production

What went wrong when AI-assisted content moved from drafts into a live site with many templated pages. None of these were about prose quality, and none would be caught by reading for tone.

## 9.1 Missing sections, not bad sentences, were the biggest defect

Copies of pages kept in a database (for previews and related content) had silently drifted from the live templates: whole cards and sidebar blocks were missing. Every copy read smoothly. Only a section-by-section comparison against the live page found the gaps.

**Practice:** whenever content exists in two places that should match, diff them section by section against the live version.

## 9.2 Tracking parameters are the detail templates forget

Two different buttons on the same page carried the same campaign tracking code, because a template was copied and only the visible text was localised.

**Practice:** when producing variants from a template, run one pass that checks *only* non-visible values: tracking parameters, IDs, canonical URLs, structured data. Do it separately from the writing review.

## 9.3 Duplicated specifics are a fact-check category of their own

Two supposedly different locations shared identical coordinates, and two case studies quoted the same result. Field-by-field template filling leaves one field unswapped.

**Practice:** scan for the same specific number attached to different entities. `prose-check`'s `repeated-figure` rule flags candidates.

## 9.4 Match records on two identifiers before writing to a live system

Some pages had a stale numeric ID in the source material. Writing back by that ID alone would have overwritten the wrong record.

**Practice:** when syncing content into a CMS or database, match on two independent identifiers (for example slug *and* ID), so a mismatch updates nothing instead of the wrong thing.

## 9.5 Report unrelated problems; don't fix them on the way past

Content work regularly uncovers unrelated bugs. Fixing them inside the content change made it hard to review and surprised the people who owned those parts.

**Practice:** note the problem, where it is and why it matters, and hand it to the owner. Keep the change you were asked to make focused.

## 9.6 The "swap test" works

The rule that each variant page's sections must fail to make sense on another variant ([§3.3](03-formats.md#33-variant-pages-per-city-industry-product-line)) consistently produced pages with distinct opening problems, examples and FAQs. It is a practical, checkable bar.

## 9.7 Two minutes on the source of truth saves the whole review

The file that looked authoritative (an export) was stale; the one that looked like "just a template" was what visitors saw. Confirm which version is live before writing anything.
