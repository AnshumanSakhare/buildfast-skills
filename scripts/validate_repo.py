#!/usr/bin/env python3
"""Validate the portable structure and public documentation of BuildFast Skills."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
SKILL_NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*-skill$")
MARKDOWN_LINK = re.compile(r"!?(?:\[[^\]]*\])\(([^)]+)\)")
LEGACY_TEXT = (
    "buildfastwithai/agent-skills",
    "app-builder-skills/",
    "html-game-generator-skill",
    "32 skills",
    "six categories",
)


def frontmatter(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError("must start with YAML frontmatter")
    parts = text.split("---", 2)
    if len(parts) != 3:
        raise ValueError("frontmatter is not closed")
    return parts[1]


def field(block: str, key: str) -> str | None:
    match = re.search(rf"(?m)^{re.escape(key)}:\s*(.+)$", block)
    return match.group(1).strip().strip("'\"") if match else None


def local_link_target(markdown: Path, raw_target: str) -> Path | None:
    target = raw_target.strip().strip("<>")
    if not target or target.startswith(("#", "http://", "https://", "mailto:")):
        return None
    target = unquote(target.split("#", 1)[0].split("?", 1)[0])
    return (markdown.parent / target).resolve()


def main() -> int:
    errors: list[str] = []
    skill_dirs = sorted(
        path for path in ROOT.iterdir() if path.is_dir() and path.name.endswith("-skill")
    )

    if not skill_dirs:
        errors.append("no root-level *-skill directories found")

    for skill_dir in skill_dirs:
        skill_file = skill_dir / "SKILL.md"
        readme = skill_dir / "README.md"

        if not SKILL_NAME.fullmatch(skill_dir.name):
            errors.append(f"{skill_dir.name}: invalid folder name")
        if not skill_file.is_file():
            errors.append(f"{skill_dir.name}: missing SKILL.md")
            continue
        if not readme.is_file():
            errors.append(f"{skill_dir.name}: missing README.md")

        try:
            metadata = frontmatter(skill_file)
        except ValueError as exc:
            errors.append(f"{skill_file.relative_to(ROOT)}: {exc}")
            continue

        name = field(metadata, "name")
        description = field(metadata, "description")
        if name != skill_dir.name:
            errors.append(
                f"{skill_file.relative_to(ROOT)}: name {name!r} must match folder"
            )
        if not description:
            errors.append(f"{skill_file.relative_to(ROOT)}: missing description")

        if readme.is_file():
            readme_text = readme.read_text(encoding="utf-8")
            expected = f"--skill {skill_dir.name}"
            if expected not in readme_text:
                errors.append(f"{readme.relative_to(ROOT)}: missing {expected!r}")

        agent_yaml = skill_dir / "agents" / "openai.yaml"
        if agent_yaml.is_file():
            agent_text = agent_yaml.read_text(encoding="utf-8")
            expected_token = "$" + skill_dir.name
            if expected_token not in agent_text:
                errors.append(
                    f"{agent_yaml.relative_to(ROOT)}: default prompt must name "
                    f"{expected_token}"
                )

    markdown_files = sorted(ROOT.rglob("*.md"))
    for markdown in markdown_files:
        text = markdown.read_text(encoding="utf-8")
        relative = markdown.relative_to(ROOT)
        lowered = text.lower()
        for old in LEGACY_TEXT:
            if old.lower() in lowered:
                errors.append(f"{relative}: contains stale text {old!r}")

        for raw_target in MARKDOWN_LINK.findall(text):
            target = local_link_target(markdown, raw_target)
            if target is not None and not target.exists():
                errors.append(f"{relative}: broken link {raw_target!r}")

    if errors:
        print(f"Validation failed with {len(errors)} issue(s):")
        for error in errors:
            print(f"  - {error}")
        return 1

    print(
        f"Validated {len(skill_dirs)} skills and "
        f"{len(markdown_files)} Markdown files."
    )
    print("Frontmatter, install commands, agent metadata, links, and identity: OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
