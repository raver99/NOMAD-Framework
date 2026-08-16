# 📏 Skill Authoring Rules

The canonical rule set for writing, testing and reviewing skills in NOMAD: the governing principle
that a test which cannot fail proves nothing, the authoring workflow, skill types, frontmatter and
naming, the description budget and what triggers a skill, evaluations, directory structure,
generality and extensions, parameters, distribution and setup, and the validation checklist.

> **The rules live in the plugin, not in this directory:**
> [`plugins/nomad-skill-authoring/references/skill-authoring-rules.md`](../../plugins/nomad-skill-authoring/references/skill-authoring-rules.md)

`nomad-skill-creator` and `nomad-skill-validator` are both procedures over that document and read it
at runtime rather than carrying their own copies, so a rule changed once changes both. It ships
inside the plugin so the skills keep working when installed in a project that has no copy of this
repository. A skill whose rules live outside its own package looks installed and quietly runs on
whatever the model happens to remember — the failure this page exists to prevent is the one it would
otherwise cause.

This page is a stable address rather than a second copy. Links here continue to resolve if the rule
set moves again.

For how skills are discovered, organised and scaled as a library, see
[Claude Code Skills](claude-code-skills.md).
