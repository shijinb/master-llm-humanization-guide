"""Keeps the documentation honest: links resolve, the rubric is consistent, and the eval cases'
statements about prose-check are true."""

import json
import re
from pathlib import Path

import pytest

from prose_check.rules import Options, run
from prose_check.text import paragraphs

ROOT = Path(__file__).resolve().parent.parent
MARKDOWN = sorted(p for p in ROOT.rglob("*.md") if ".venv" not in p.parts and ".pytest_cache" not in p.parts)
LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")


def quoted_draft(case: str) -> str:
    """The '## Draft under review' block of an eval case, without the '> ' quote markers."""
    text = (ROOT / "eval" / "cases" / case).read_text(encoding="utf-8")
    block = text.split("## Draft under review", 1)[1].split("\n## ", 1)[0]
    return "\n".join(line[2:] if line.startswith("> ") else line.lstrip(">") for line in block.splitlines())


def anchors(path: Path) -> set[str]:
    """GitHub-style heading anchors."""
    result = set()
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("#"):
            title = line.lstrip("#").strip().lower()
            result.add(re.sub(r"\s", "-", re.sub(r"[^\w\s-]", "", title)))
    return result


@pytest.mark.parametrize("path", MARKDOWN, ids=lambda p: str(p.relative_to(ROOT)))
def test_relative_links_resolve(path: Path) -> None:
    text = re.sub(r"```.*?```", "", path.read_text(encoding="utf-8"), flags=re.S)
    for target in LINK.findall(text):
        if target.startswith(("http://", "https://", "mailto:")):
            continue
        file_part, _, anchor = target.partition("#")
        destination = (path.parent / file_part).resolve() if file_part else path
        assert destination.exists(), f"{path.name}: broken link {target}"
        if anchor and destination.suffix == ".md":
            assert anchor in anchors(destination), f"{path.name}: missing anchor {target}"


def test_rubric_is_consistent() -> None:
    rubric = json.loads((ROOT / "eval" / "rubric.json").read_text(encoding="utf-8"))
    ids = [c["id"] for c in rubric["criteria"]]
    assert len(ids) == len(set(ids)) == 8
    assert all(len(c["levels"]) == len(rubric["scale"]) for c in rubric["criteria"])
    maximum = len(ids) * max(rubric["scale"])
    assert rubric["publish_threshold"]["minimum_total"] <= maximum
    assert set(rubric["publish_threshold"]["gates"]) <= set(ids)


def test_rubric_table_in_guide_matches_json() -> None:
    rubric = json.loads((ROOT / "eval" / "rubric.json").read_text(encoding="utf-8"))
    guide = (ROOT / "guide" / "07-evaluation.md").read_text(encoding="utf-8")
    for criterion in rubric["criteria"]:
        assert f"**{criterion['name']}**" in guide
    assert f"≥ {rubric['publish_threshold']['minimum_total']} of {len(rubric['criteria']) * 2}" in guide


def test_case_01_draft_fails_prose_check() -> None:
    findings = run(paragraphs(quoted_draft("01-landing-page-invented-stats.md")), Options())
    rules = {f.rule for f in findings if f.severity == "warning"}
    assert {"overused-phrase", "weak-opening"} <= rules


def test_case_03_shows_prose_check_misses_template_content() -> None:
    findings = run(paragraphs(quoted_draft("03-variant-page-template.md")), Options())
    assert not [f for f in findings if f.severity == "warning"]


def test_before_after_examples_improve() -> None:
    text = (ROOT / "examples" / "before-after.md").read_text(encoding="utf-8")
    sections = re.split(r"\*\*(Before|After)[^*]*\*\*", text)
    befores = [sections[i + 1] for i in range(1, len(sections) - 1, 2) if sections[i] == "Before"]
    afters = [sections[i + 1] for i in range(1, len(sections) - 1, 2) if sections[i] == "After"]

    def warnings(block: str) -> int:
        quoted = "\n".join(line[2:] for line in block.splitlines() if line.startswith("> "))
        return sum(1 for f in run(paragraphs(quoted), Options()) if f.severity == "warning")

    assert len(befores) == len(afters) == 5
    assert sum(map(warnings, befores)) > 0
    assert sum(map(warnings, afters)) == 0


def test_readme_sample_output_is_real(capsys, monkeypatch) -> None:  # type: ignore[no-untyped-def]
    import io

    from prose_check.cli import main

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    expected = readme.split("```text\n-: ", 1)[1].split("```", 1)[0]
    examples = (ROOT / "examples" / "before-after.md").read_text(encoding="utf-8")
    first_before = examples.split("**Before**", 1)[1].split("**After**", 1)[0]
    draft = "\n".join(line[2:] for line in first_before.splitlines() if line.startswith("> "))

    monkeypatch.setattr("sys.stdin", io.StringIO(draft + "\n"))
    main(["-"])
    assert capsys.readouterr().out.strip() == ("-: " + expected).strip()
