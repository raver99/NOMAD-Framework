---
name: nomad-skill-validator
description: Use when a SKILL.md has been written or changed, before publishing a skill, or when asked to review, check or validate a skill. Symptoms include a description over budget, dangling skill references, version drift, shouted rules, generic reference filenames.
metadata:
  version: 0.2.0
---

# Validating Skills

Review a skill against NOMAD's rules and report what is wrong. Report, do not rewrite — a reviewer
that edits starts fixing instead of reporting, and the finding is lost along with the chance to
decide whether the rule or the skill is wrong.

The canonical rules ship in this plugin, at
`${CLAUDE_PLUGIN_ROOT}/references/skill-authoring-rules.md` — or `../../references/` relative to this
file, if the skill was copied out of its plugin. Read it before judging anything, and cite the
section a finding comes from so the author can check the reasoning rather than take the verdict on
faith.

## Run the mechanical checks first

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/skills/nomad-skill-validator/scripts/check_skill.py" <skill-directory>
```

It exits non-zero when any check fails, so it works unattended in CI. It covers what is decidable by
reading files: the description ceiling and its shape, name form, version mirroring, extension pins,
body length, reference existence, depth and naming, dangling skill mentions, shouted rules, and
whether trigger evals were committed.

Run it before reading the skill yourself. Its findings tell you where to look, and re-deriving them
by eye wastes effort the script has already spent.

## Then judge what the script cannot see

The script checks form. These need reading, and they are where real problems live:

**Does the description route, or merely describe?** Accuracy is not the bar. Ask what a user would
actually type when they need this, and whether those words appear. A description can be true and
still never match anything. For a skill with `disable-model-invocation: true` the description is a
label read by a person in autocomplete, so ask instead whether it says what the skill does — and
whether naming the operation helps anyone at all (rules §5.4).

**Does it need something the package does not install?** If the skill only works once a `CLAUDE.md`
statement, a config file, a credential or a tool exists in the project, and nothing ships to put it
there, the setup gets followed by hand and eventually skipped — silently, because the skill looks
installed. Rules §10.1.

**Is the skill overfitted to its own examples?** Look for instructions that only make sense for one
project, one file layout, one naming convention. Authoring pressure produces this: you iterate on
two or three cases, so every fix is tempted to fit exactly those. Rules §2.3.

**Are the degrees of freedom right?** High freedom where several approaches work and context
decides; low freedom where the sequence is fragile and consistency matters. A rigid script for an
open-ended judgement is as wrong as vague prose for a migration.

**Does it explain why?** A skill that only states rules gets discarded the first time one is
inconvenient, because nobody can tell a legitimate exception from a violation.

**Would it beat a baseline?** The hardest and most valuable question. If the model would produce
much the same result without this skill, the skill earns nothing however well written it is. Say so
plainly — it is more useful than a list of style notes.

## Report

Group findings by severity, most severe first. For each: what is wrong, which rule section it comes
from, and what to change. Where a finding is a judgement rather than a mechanical failure, say which
it is — the author needs to know what is arguable.

Close with the baseline question, answered explicitly. A skill that passes every check and still
contributes nothing is the failure worth catching.

If nothing is wrong, say so without inventing findings to look thorough.
