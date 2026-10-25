import json

import pytest

from prose_check.cli import main, summary
from prose_check.rules import Options, run
from prose_check.text import paragraphs, sentences


def rules_hit(text: str, **options: int) -> list[str]:
    return [finding.rule for finding in run(paragraphs(text), Options(**options))]


# --- Parsing ---------------------------------------------------------------------------------------


def test_skips_code_blocks_comments_and_front_matter() -> None:
    text = "---\ntitle: x\n---\n\nReal text.\n\n```\nleverage robust synergy\n```\n\n<!-- leverage -->\n"
    assert [p.text for p in paragraphs(text)] == ["Real text."]


def test_headings_and_list_items_are_separate_paragraphs() -> None:
    kinds = [p.kind for p in paragraphs("# Title\nIntro line.\n\n- one\n- two\n")]
    assert kinds == ["heading", "prose", "list", "list"]


def test_bold_only_line_is_a_heading() -> None:
    assert [p.kind for p in paragraphs("**Big Promise**\n\nIn today's world we sell.")] == ["heading", "prose"]


def test_inline_markdown_is_removed() -> None:
    (para,) = paragraphs("See [the docs](https://example.com) and `config.yaml` for **details**.")
    assert para.text == "See the docs and code for details."


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("One. Two words. Three more words.", 3),
        ("Use tools, e.g. a linter. Then ship.", 2),
        ("Revenue grew 3.5 percent. Costs fell.", 2),
        ("J. Smith wrote it. Done.", 2),
        ('He said "stop." Then left.', 2),
    ],
)
def test_sentence_splitting(text: str, expected: int) -> None:
    (para,) = paragraphs(text)
    assert len(sentences(para)) == expected


# --- Rules -----------------------------------------------------------------------------------------


def test_overused_phrases_match_word_forms_and_ignore_substrings() -> None:
    hits = run(paragraphs("We leveraged it. Utilization rose. Then we delved deeper."), Options())
    words = {f.message.split('"')[1].lower() for f in hits if f.rule == "overused-phrase"}
    assert words == {"leveraged", "utilization", "delved"}


def test_overused_phrase_is_not_flagged_inside_other_words() -> None:
    assert "overused-phrase" not in rules_hit("The leverage-free design.")  # hyphenated compound
    assert "overused-phrase" not in rules_hit("Pivotally placed.")  # 'pivotal' has no wildcard


def test_vague_quantities_are_info() -> None:
    findings = run(paragraphs("Costs fell significantly across various teams."), Options())
    assert {(f.rule, f.severity) for f in findings} == {("vague-quantity", "info")}


def test_weak_opening_and_definition_opening() -> None:
    assert "weak-opening" in rules_hit("In this article we explain caching.")
    assert "weak-opening" in rules_hit("Caching is a technique that stores data.")
    assert "weak-opening" not in rules_hit("Our cache hit rate fell to 61% last week.")


def test_long_sentence_threshold() -> None:
    long = " ".join(["word"] * 36) + "."
    assert "long-sentence" in rules_hit(long)
    assert "long-sentence" not in rules_hit(long, long_sentence=40)


def test_uniform_rhythm_flags_monotone_runs_only() -> None:
    monotone = " ".join(["This sentence has exactly seven words in it."] * 5)
    varied = (
        "Short one. This sentence is quite a lot longer than the first one was, by design. "
        "Medium length here, more or less. Tiny. And then another long sentence that keeps going for a while longer."
    )
    assert "uniform-rhythm" in rules_hit(monotone)
    assert "uniform-rhythm" not in rules_hit(varied)


def test_long_paragraph() -> None:
    assert "long-paragraph" in rules_hit(" ".join(["Word."] * 130))


def test_repeated_figures_flag_units_and_money_but_not_years_or_small_numbers() -> None:
    text = (
        "Shortlists took 22 hours.\n\nIn 2024 we hired 4 people.\n\n"
        "The Pune office also took 22 hours.\n\nIn 2024 sales grew; 4 teams joined."
    )
    findings = [f for f in run(paragraphs(text), Options()) if f.rule == "repeated-figure"]
    assert len(findings) == 1 and '"22 hours"' in findings[0].message


def test_repeated_figure_in_one_paragraph_is_not_flagged() -> None:
    assert "repeated-figure" not in rules_hit("We saved $1,200 in March and $1,200 in April.")


def test_clean_text_has_no_warnings() -> None:
    text = (
        "Our invoice export failed for 38 customers on Monday. The cause was a timezone bug: invoices dated "
        "after 23:00 UTC landed in the next month's file.\n\nWe fixed the date conversion and re-sent the files by noon."
    )
    assert [f for f in run(paragraphs(text), Options()) if f.severity == "warning"] == []


# --- CLI -------------------------------------------------------------------------------------------


def test_cli_json_output_and_exit_codes(tmp_path, capsys) -> None:  # type: ignore[no-untyped-def]
    draft = tmp_path / "draft.md"
    draft.write_text("We leverage data. Revenue grew significantly.", encoding="utf-8")

    assert main([str(draft), "--format", "json"]) == 0
    report = json.loads(capsys.readouterr().out)
    assert report[0]["summary"]["sentences"] == 2
    assert {f["rule"] for f in report[0]["findings"]} == {"overused-phrase", "vague-quantity"}

    assert main([str(draft), "--fail-on", "warning"]) == 1
    assert main([str(draft), "--rules", "vague-quantity", "--fail-on", "warning"]) == 0
    assert main([str(draft), "--rules", "vague-quantity", "--fail-on", "info"]) == 1


def test_cli_rejects_unknown_rule(tmp_path) -> None:  # type: ignore[no-untyped-def]
    draft = tmp_path / "d.md"
    draft.write_text("x", encoding="utf-8")
    with pytest.raises(SystemExit):
        main([str(draft), "--rules", "nope"])


def test_summary_counts() -> None:
    assert summary("One two three. Four five.") == {
        "words": 5,
        "sentences": 2,
        "mean_sentence_words": 2.5,
        "shortest_sentence_words": 2,
        "longest_sentence_words": 3,
    }
