# 8. Ethics and limits

This guide is about making AI-assisted writing **useful and accurate for the reader**. Some requests that sound similar are out of scope, and it helps to say why.

## 8.1 Never fabricate

Do not use a model (or this guide) to produce:

- experience, credentials, employers, titles or achievements a person does not have (resumes, bios, author pages);
- testimonials, reviews, case studies or quotes that did not happen;
- statistics, studies or references that do not exist;
- a persona presented as a real, named human when there is none.

"Make it sound human" never means "make it sound like a person who was there". If nobody was there, say what the source is instead.

## 8.2 Honesty about authorship

Respect the rules of the context: academic integrity policies, journal and conference rules, client contracts, platform terms. Where AI assistance must be disclosed, disclose it. Polishing your own ideas and facts with a model is a different act from submitting a model's work as your own where that is prohibited.

## 8.3 AI detectors

Passing AI-detection tools is **not** a goal of this guide.

- Detectors are unreliable. OpenAI withdrew its own classifier in July 2023, citing its low rate of accuracy ([OpenAI](https://openai.com/index/new-ai-classifier-for-indicating-ai-written-text/)), and research has found that detectors disproportionately flag text by non-native English writers as AI-generated ([Liang et al., *Patterns*, 2023](https://doi.org/10.1016/j.patter.2023.100779)).
- Detector scores are not what search quality is judged on. Google's published position is that it rewards helpful, reliable content "however it is produced", while using automation mainly to manipulate rankings breaks its spam policies ([Google Search Central, Feb 2023](https://developers.google.com/search/blog/2023/02/google-search-and-ai-content); [spam policies](https://developers.google.com/search/docs/essentials/spam-policies)).
- Optimising for a detector pushes writing in random directions (odd word choices, artificial errors) that make it worse for readers.

If someone sends you a detector report, treat it only as a prompt to look for **real** problems a reader would notice. Is the sentence rhythm uniform? Is every card in a section built the same way? Is one claim repeated in four places? Does a byline promise a person the text never shows? If those are present, fix them because they hurt readers. If they are not, the score is noise. Also check what text the tool actually received: page scrapes often run navigation labels, buttons and headings into the body text.

## 8.4 Privacy and confidentiality

Do not paste personal data (customer records, candidate resumes, health or financial details) or confidential business information into a model unless your organisation's agreement with the provider allows it. Examples in this repository are synthetic.

## 8.5 Limits of this guide

- It is a set of editorial practices, not a guarantee of rankings, conversions or acceptance by any platform.
- It is written for English-language business and technical writing. Rhythm and phrase advice may not carry over to other languages.
- The sources cited here reflect what was published as of the review date in the [README](../README.md#sources-and-review-date). Check them again before relying on them.
