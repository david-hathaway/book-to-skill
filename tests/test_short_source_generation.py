"""Regression coverage for short-source generation guidance."""

from pathlib import Path


SKILL_PATH = Path(__file__).resolve().parent.parent / "SKILL.md"


def test_generator_has_a_compact_short_source_path() -> None:
    skill = SKILL_PATH.read_text(encoding="utf-8")

    assert "## Step 3.5 — Select output shape" in skill
    assert "SOURCE_SHAPE=short" in skill
    assert "sources/source-01-<slug>.md" in skill
    assert 'SOURCE_SHAPE=short: mkdir -p "$SKILLS_HOME/<skill_name>/sources"' in skill
    assert "Do not invent chapters" in skill
    assert "and `cheatsheet.md` for short-source output" in skill
    assert "Do not add empty supporting files during a fold-in" in skill
    assert "either a `chapters/` or `sources/` sub-folder" in skill


def test_master_skill_template_can_index_short_sources() -> None:
    skill = SKILL_PATH.read_text(encoding="utf-8")

    assert "## Source Index" in skill
    assert "[source-01](sources/source-01-<slug>.md)" in skill
    assert "**Sources**: <N>" in skill
    assert "use this complete standalone template instead" in skill
    assert "argument-hint: [topic, source number, or source title]" in skill
