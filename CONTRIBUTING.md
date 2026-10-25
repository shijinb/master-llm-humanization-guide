# Contributing

Corrections, new examples, templates and rules are welcome.

## Content changes

- **Facts need sources.** Any claim about search engines, detectors, research or tools links to the primary source; update the review date in the README.
- **Examples are synthetic.** No real customer data, personal data or confidential material. Mark invented figures as illustrative.
- **No fabrication or detector-evasion content.** See [guide/08-ethics.md](guide/08-ethics.md).
- Run `prose-check` on your changes. The guide should follow its own advice; deliberate exceptions (such as quoted bad examples) are fine.

## Code changes (`prose_check/`)

```bash
python -m venv .venv && . .venv/bin/activate
pip install -e ".[dev]"
ruff format . && ruff check . && mypy && pytest
```

- New rules go in `prose_check/rules.py`, registered in `RULES`, with tests for what they flag **and** what they must not flag.
- Keep the package dependency-free.
- Changing a rule's output may break `tests/test_repository.py::test_readme_sample_output_is_real`; update the README sample from the tool's real output, never by hand.

## Versioning

Bump the version in `pyproject.toml` and `prose_check/__init__.py` and add a CHANGELOG entry, following the rules in the README.
