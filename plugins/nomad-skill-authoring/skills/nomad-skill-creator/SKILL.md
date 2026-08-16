---
name: nomad-skill-creator
description: Use when creating a new skill, turning a repeated workflow into a skill, improving an existing skill, or drafting a SKILL.md. Also when a skill fails to trigger reliably, or when asked to add a skill to a plugin or marketplace.
metadata:
  version: 0.2.0
---

# Creating Skills

The rules this skill applies ship in this plugin, at
`${CLAUDE_PLUGIN_ROOT}/references/skill-authoring-rules.md` — or `../../references/` relative to this
file, if the skill was copied out of its plugin. Read it first; this file is the procedure, that
file is the reasoning.

Writing a skill is the easy part. Knowing whether it earns its place is the hard part, and most of
this procedure is about that.

## 1. Watch it fail first

Before writing any content, run the task **without** a skill and watch what actually goes wrong.
Capture what you saw.

This is the step people skip and the reason most skills contribute nothing. A skill written without
observing failure encodes what its author imagines the model gets wrong, which is frequently
something the model already handles. Observing first tells you what to write — and sometimes that
nothing needs writing at all, which is a good outcome and worth saying out loud.

If the baseline run produces a fine result, stop and say so.

## 2. Capture intent

If the conversation already contains the workflow being captured, mine it before asking anything:
the tools used, the sequence, the corrections the user made, the formats observed. Ask only what is
still missing.

Otherwise establish: what should this enable, when should it trigger, what does it output, and which
of the four skill types is it (rules §3) — the type decides what testing discriminates.

Look for prior art before drafting. Someone has likely solved this, and arriving with context
reduces what the user has to supply.

## 3. Draft the minimum

Write the smallest skill that addresses the failures observed in step 1. Nothing speculative.

Explain the reasoning behind each instruction rather than asserting it. A model given the reason can
handle a case the rule did not anticipate; a model given only a rule cannot. Reaching for a shouted
imperative is a signal that a reason has not been worked out yet.

The description is the routing mechanism and the body is not loaded until it fires, so all triggering
information belongs in the description — under 300 characters, keywords first, conditions rather than
procedure. Rules §5.

## 4. Test with and without

Write two or three realistic prompts — messy and specific, the kind of thing someone would actually
type. Show them to the user before running.

Run each prompt twice: once with the skill, once without, launched together so conditions match. The
without-skill arm is what turns an impression into evidence. Keep run artifacts in a sibling
`<skill-name>-workspace/` directory, never inside the skill.

Put the outputs in front of the user before offering your own verdict, so their reaction is theirs.

## 5. Commit the trigger evals

Write `evals/trigger_eval.json` — around twenty queries, roughly half of which should trigger.

The negatives carry the value, and only if they are near-misses: queries sharing vocabulary or
subject with the skill that nonetheless need something else. An obviously unrelated query tests
nothing and passes regardless of how bad the description is.

## 6. Improve

Generalise from the feedback rather than patching the specific cases — a skill that works only on its
own test prompts is worthless. Read the transcripts and not only the outputs: wasted effort is
visible in how the work was done, not in the result. If part of the skill is causing that waste,
remove it and measure the difference.

Repeat until the feedback is empty or progress stalls. Stalling is a legitimate reason to stop.

## 7. Validate before finishing

Run the `nomad-skill-validator` skill over the result and resolve what it finds.

## Does it need anything to exist in the target project?

If the skill only works once something is in place — a statement in `CLAUDE.md`, a config file, a
directory layout, an installed CLI, a credential — ship a one-time setup skill in the same plugin
rather than instructions someone follows by hand. Hand-followed setup gets paraphrased or skipped,
and the failure is silent: the skill looks installed and misbehaves later. Rules §10.1 covers what
that skill has to do — guard every step, copy shipped assets verbatim, verify rather than assume,
keep secrets out of the repository, and say what remains manual.

Ask first whether the need can be designed away. Setup that exists because an artifact cannot
describe itself is a design problem being automated instead of fixed, and a file that states its own
conventions also serves the people who install nothing.

## Placing the skill

- **General, reusable** → a plugin in a marketplace repository, one plugin per independently
  installable skill, with `metadata.version` mirroring the plugin version.
- **Project-specific** → `.claude/skills/` in that project, committed with it.
- **Project-specific behaviour layered on a general skill** → an extension skill that records
  `metadata.extends` and `metadata.built-against`, rather than editing the general skill or hiding
  the difference in a file it happens to look for. Rules §8.
