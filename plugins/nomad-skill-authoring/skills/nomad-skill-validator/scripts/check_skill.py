#!/usr/bin/env python3
"""Mechanical checks from ../../references/skill-authoring-rules.md §11."""

import json
import re
import sys
from pathlib import Path

DESCRIPTION_CEILING = 300
BODY_LINE_LIMIT = 500
GENERIC_REFERENCE_NAMES = {
    "reference.md", "doc.md", "docs.md", "notes.md", "info.md",
    "misc.md", "other.md", "details.md", "data.md", "file.md",
}
WORKFLOW_MARKERS = [
    r"\bthen\b", r"\bdispatch(?:es|ing)?\b", r"\brun(?:s|ning)\s+the\b",
    r"\bstep\s*\d", r"\bfirst\b.*\bthen\b", r"->", r"→",
]
SHOUTED_RULES = re.compile(r"\b(ALWAYS|NEVER|MUST NOT|MUST)\b")
MARKDOWN_LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
SKILL_MENTION = re.compile(
    r"`([a-z][a-z0-9]*(?:-[a-z0-9]+)+)`\s+skill\b|"
    r"\b([a-z][a-z0-9]*(?:-[a-z0-9]+)+)\s+skill\b"
)


class Report:
    def __init__(self):
        self.findings = []

    def error(self, check, message):
        self.findings.append(("error", check, message))

    def warn(self, check, message):
        self.findings.append(("warn", check, message))

    @property
    def errors(self):
        return [f for f in self.findings if f[0] == "error"]


def split_frontmatter(text):
    if not text.startswith("---"):
        return None, text
    end = text.find("\n---", 3)
    if end == -1:
        return None, text
    return text[3:end].strip("\n"), text[end + 4:]


def parse_frontmatter(raw):
    fields, nested, current = {}, {}, None
    for line in raw.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.startswith((" ", "\t")):
            if current and ":" in line:
                key, _, value = line.strip().partition(":")
                nested.setdefault(current, {})[key.strip()] = value.strip().strip("\"'")
            continue
        key, _, value = line.partition(":")
        key, value = key.strip(), value.strip().strip("\"'")
        if value:
            fields[key] = value
        else:
            current = key
            fields[key] = None
    fields.update(nested)
    return fields


def is_truthy(value):
    return str(value).strip().lower() in {"true", "yes", "1"}


def find_plugin_version(skill_dir):
    for parent in skill_dir.parents:
        manifest = parent / ".claude-plugin" / "marketplace.json"
        if manifest.exists():
            try:
                data = json.loads(manifest.read_text())
            except json.JSONDecodeError:
                return None
            for plugin in data.get("plugins", []):
                source = plugin.get("source", "")
                if Path(source).name in {p.name for p in skill_dir.parents}:
                    return plugin.get("version")
            plugins = data.get("plugins", [])
            if len(plugins) == 1:
                return plugins[0].get("version")
    return None


def known_skill_names(skill_dir):
    names = set()
    roots = [p for p in skill_dir.parents if p.name in {"skills", ".claude"}]
    roots.append(Path.home() / ".claude" / "skills")
    for root in roots:
        if root.exists():
            for found in root.rglob("SKILL.md"):
                names.add(found.parent.name)
    return names


def check_description(fields, report):
    description = fields.get("description")
    if not description:
        report.error("frontmatter", "Missing description")
        return
    exempt = is_truthy(fields.get("disable-model-invocation", "false"))
    if not exempt and len(description) > DESCRIPTION_CEILING:
        report.error(
            "description-budget",
            f"{len(description)} chars exceeds the {DESCRIPTION_CEILING} ceiling "
            "(§5.2). Exempt only with disable-model-invocation: true",
        )
    if not exempt and not description.lower().startswith("use when"):
        report.warn("description-triggers", 'Should start with "Use when" (§5.1)')
    for marker in WORKFLOW_MARKERS:
        if re.search(marker, description, re.I):
            report.error(
                "description-triggers",
                "Reads like workflow, not triggering conditions (§5.1). Procedure in a "
                "description can be executed without the body ever being opened",
            )
            break


def check_name(fields, skill_dir, report):
    name = fields.get("name")
    if not name:
        report.error("frontmatter", "Missing name")
        return
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
        report.error("name", f"'{name}' is not lowercase kebab-case")
    if len(name) > 64:
        report.error("name", f"'{name}' exceeds 64 characters")
    if name != skill_dir.name:
        report.warn("name", f"Frontmatter name '{name}' differs from directory '{skill_dir.name}'")


def check_version(fields, skill_dir, report):
    metadata = fields.get("metadata")
    declared = metadata.get("version") if isinstance(metadata, dict) else None
    if "version" in fields and not isinstance(fields.get("version"), type(None)):
        report.error("frontmatter", "Top-level 'version:' fails spec validation; use metadata.version (§4)")
    plugin_version = find_plugin_version(skill_dir)
    if plugin_version and not declared:
        report.error("version-mirror", f"Plugin is {plugin_version} but metadata.version is absent (§10)")
    elif plugin_version and declared != plugin_version:
        report.error("version-mirror", f"metadata.version {declared} does not match plugin {plugin_version}")

    if isinstance(metadata, dict) and metadata.get("extends"):
        target = metadata["extends"]
        if target not in known_skill_names(skill_dir):
            report.error("extends", f"Extends '{target}', which was not found")
        elif not metadata.get("built-against"):
            report.warn("extends", f"Extends '{target}' without a built-against pin (§10)")


def check_body(body, report):
    lines = body.splitlines()
    if len(lines) > BODY_LINE_LIMIT:
        report.error("body-length", f"{len(lines)} lines exceeds {BODY_LINE_LIMIT} (§7)")
    for number, line in enumerate(lines, 1):
        match = SHOUTED_RULES.search(line)
        if match:
            report.warn(
                "shouted-rule",
                f"line {number}: '{match.group(0)}' — usually a symptom of an unexplained "
                "reason rather than a rule worth shouting (§2.3)",
            )


def check_references(skill_dir, body, report):
    for target in MARKDOWN_LINK.findall(body):
        if target.startswith(("http://", "https://", "#")):
            continue
        if "\\" in target:
            report.error("paths", f"'{target}' uses backslashes; use forward slashes (§7)")
        path = (skill_dir / target).resolve()
        if not path.exists():
            report.error("references", f"'{target}' does not exist")
            continue
        if path.name.lower() in GENERIC_REFERENCE_NAMES:
            report.error("reference-naming", f"'{path.name}' is generic; name it for its content (§7)")
        if path.suffix == ".md":
            for nested in MARKDOWN_LINK.findall(path.read_text(encoding="utf-8", errors="replace")):
                if not nested.startswith(("http://", "https://", "#")) and nested.endswith(".md"):
                    report.warn(
                        "reference-depth",
                        f"'{target}' links onward to '{nested}'; keep references one level "
                        "deep or they get partially read (§7)",
                    )
                    break


def check_skill_mentions(skill_dir, body, report):
    known = known_skill_names(skill_dir)
    if not known:
        return
    mentioned_names = {
        group.lower() for match in SKILL_MENTION.findall(body) for group in match if group
    }
    for mentioned in mentioned_names:
        if mentioned not in known:
            report.warn("dangling-skill", f"Names '{mentioned}' skill, which was not found (§10)")


def check_evals(skill_dir, fields, report):
    if is_truthy(fields.get("disable-model-invocation", "false")):
        return
    if not (skill_dir / "evals" / "trigger_eval.json").exists():
        report.warn("evals", "No evals/trigger_eval.json; trigger evals are always committed (§6)")


def validate(skill_dir):
    report = Report()
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        report.error("structure", f"No SKILL.md in {skill_dir}")
        return report

    text = skill_md.read_text(encoding="utf-8")
    raw, body = split_frontmatter(text)
    if raw is None:
        report.error("frontmatter", "No YAML frontmatter")
        return report

    fields = parse_frontmatter(raw)
    check_name(fields, skill_dir, report)
    check_description(fields, report)
    check_version(fields, skill_dir, report)
    check_body(body, report)
    check_references(skill_dir, body, report)
    check_skill_mentions(skill_dir, body, report)
    check_evals(skill_dir, fields, report)
    return report


def main():
    if len(sys.argv) < 2:
        print("Usage: check_skill.py <skill-directory> [...]")
        return 2

    failed = False
    for argument in sys.argv[1:]:
        skill_dir = Path(argument).resolve()
        report = validate(skill_dir)
        print(f"\n{skill_dir.name}")
        if not report.findings:
            print("  ok")
            continue
        for severity, check, message in report.findings:
            marker = "FAIL" if severity == "error" else "warn"
            print(f"  [{marker}] {check}: {message}")
        if report.errors:
            failed = True

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
