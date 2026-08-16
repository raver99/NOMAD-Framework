---
name: nomad-backlog-setup
description: Set up the NOMAD backlog in this project — create BACKLOG.md at the root and add the convention to CLAUDE.md. Run once per project.
disable-model-invocation: true
allowed-tools: Read, Write, Edit, Glob
metadata:
  version: 0.2.0
---

# Set Up the Backlog

Installs two things: `BACKLOG.md` at the project root, and a short section in `CLAUDE.md` stating
the convention. Both come from this plugin's `assets/` directory — `../../assets/BACKLOG.md` and
`../../assets/CLAUDE-backlog-section.md` relative to this file. Copy them; do not retype them from
memory, or the project gets a paraphrase that drifts from what every other project has.

This runs once per project, so treat everything below as guarding against a second run.

## 1. The backlog file

**If `BACKLOG.md` already exists at the project root, stop.** Report what is there and change
nothing. A project that already has a backlog either ran this before or keeps one by hand, and
overwriting it destroys work that exists nowhere else. Offer to show the differences against the
seed instead.

Otherwise copy `assets/BACKLOG.md` to the project root unchanged.

Then ask whether to delete the example lines. They are worth keeping for a few days in a project
whose first items have not been written yet, because they show the format in place — but they are
not real work and the file says to delete them. The header carries the rules either way.

## 2. The CLAUDE.md section

Read `CLAUDE.md` at the project root.

- **No `CLAUDE.md`** — create it containing the section from
  `assets/CLAUDE-backlog-section.md`.
- **It exists with no backlog section** — append the section verbatim.
- **It already mentions the backlog** — stop and show what is there. Do not append a second copy
  and do not merge silently. Two statements of one convention is the drift this section exists to
  prevent, and which of them is right is the user's call.

The section states facts an agent cannot infer: where the file is, that status lives in the line's
position, that IDs are never reused. It contains no instruction to behave a certain way. **Do not
add one** — an agent told to watch for things worth capturing interrupts constantly, gets tuned out,
and taxes every conversation in the project whether or not it touches the backlog. If the user asks
for proactive capture, tell them that was considered and rejected, and point at
[the guide](https://github.com/rolandhuhn/NOMAD/blob/main/KnowledgeBase/WorkingWithAI/backlog-in-the-repository.md).

## 3. Report

What was created, what was skipped and why, and the two skills now available:
`/nomad-backlog-capture` to add work or an idea, `/nomad-backlog-groom` to review what has drifted.
Marking something done needs no skill — say so, since it is the obvious next question.

Do not commit; the user commits.
