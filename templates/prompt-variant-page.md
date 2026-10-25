# Prompt: variant page (per city, industry or product line)

One prompt per variant, each with its own facts sheet. The goal is a page that would make no sense on any other variant.

```text
VARIANT: {name}
FACTS SHEET (use only this; see templates/facts-sheet.md)
"""
{paste the filled facts sheet for this variant}
"""

SHARED PRODUCT FACTS (true for all variants)
- {fact}
- {fact}

TASK
Write the {variant} page with these sections: {list}.

RULES
- The opening problem must come from this variant's facts sheet, not the shared facts.
- Each section must include at least one detail from the facts sheet. Any section that would read the same on another variant's page should be rewritten or cut.
- Vary the shape of repeated blocks (cards, FAQs): different openings and lengths.
- Use human-scale details ("a 40-minute drive from the centre"), not lookup-table details (coordinates, postcode lists).
- FAQs: only questions listed in the facts sheet.
- Do not invent clients, numbers or quotes. Write [NEEDS: …] for gaps.

OUTPUT
1. The page in Markdown.
2. "Variant-specific details used": a list, by section.
3. "Swap test": for each section, one line on why it would not fit another variant.
```

After drafting, run a separate check of tracking parameters, canonical URL and structured data for this variant (guide/09-production-lessons.md §9.2).
