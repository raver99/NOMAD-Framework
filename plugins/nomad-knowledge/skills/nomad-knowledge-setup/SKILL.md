---
name: nomad-knowledge-setup
description: Set up the knowledge base in this project — create KNOWLEDGE.md at the root and add the convention to CLAUDE.md. Run once per project.
disable-model-invocation: true
allowed-tools: Read, Write, Edit, Glob, Grep
metadata:
  version: 0.5.0
---

# Set Up the Knowledge Base

Installs two things: `KNOWLEDGE.md` at the project root, and a short section in `CLAUDE.md` stating
the convention. Both ship in this plugin, as `${CLAUDE_PLUGIN_ROOT}/assets/KNOWLEDGE.md` and
`${CLAUDE_PLUGIN_ROOT}/assets/CLAUDE-knowledge-section.md` (`../../assets/` relative to this file, if
it was copied out of its plugin). Copy them; do not retype them from memory, or the project gets a
paraphrase that drifts from what every other project has.

This runs once per project, so treat everything below as guarding against a second run.

## 1. Look before writing

A project may already keep a knowledge base without calling it that. Check for documents before
creating anything:

- `KNOWLEDGE.md` at the root, or a `knowledge/` directory
- A `docs/`, `wiki/` or similarly named directory holding topic documents
- An index in `README.md` — a table or list linking to documents

**If a knowledge base already exists, stop.** Report where it is and what conventions it appears to
follow. An existing base has readers and links into it; imposing a second layout splits the project
in two, and which one wins is not this skill's call. Offer instead to add the conventions header from
`assets/KNOWLEDGE.md` to whatever index the project already keeps, so `add-knowledge` reads declared
rules rather than inferring them.

## 2. The knowledge file

**If `KNOWLEDGE.md` already exists at the project root, stop.** Report what is there and change
nothing. Offer to show the differences against the seed instead.

Otherwise copy `assets/KNOWLEDGE.md` to the project root unchanged.

Then ask whether to delete the example index row. It is worth keeping for a few days in a project
whose first document has not been written yet, because it shows the row format in place — but it
points at nothing and the file says to delete it. The header carries the rules either way.

Ask one question before finishing: whether `knowledge/` is the right home for documents in this
project. Some projects have an established `docs/` tree that documents should join. If the answer is
a different directory, edit the header to say so — the header is the specification, so it has to
match reality rather than the seed.

## 3. The CLAUDE.md section

Read `CLAUDE.md` at the project root.

- **No `CLAUDE.md`** — create it containing the section from `assets/CLAUDE-knowledge-section.md`.
- **It exists with no knowledge base section** — append the section verbatim.
- **It already mentions a knowledge base** — stop and show what is there. Do not append a second copy
  and do not merge silently. Two statements of one convention is the drift this section exists to
  prevent, and which of them is right is the user's call.

The section states facts an agent cannot infer: where documents live, that every external claim
carries a reference, that values on someone else's release cycle are not recorded. It contains no
instruction to behave a certain way. **Do not add one** — capture is triggered by a research record
existing, which `nomad-researcher` already hands off, not by an agent watching every conversation for
things worth filing.

If the directory was changed in step 2, change it here too. One convention, stated twice, has to say
the same thing both times.

## 4. Report

What was created, what was skipped and why, and the skills now available: `nomad-researcher` to
produce a sourced record, `add-knowledge` to fold the durable parts of one into the base. Say that
the two are connected by the record file rather than by a direct reference, so either works alone.

The practice is described in
[Knowledge Management with AI](https://github.com/raver99/NOMAD-Framework/blob/main/KnowledgeBase/WorkingWithAI/knowledge-management-with-ai.md).

Do not commit; the user commits.
