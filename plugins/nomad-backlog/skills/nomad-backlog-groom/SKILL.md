---
name: nomad-backlog-groom
description: Review the project's BACKLOG.md for drift — duplicates, contradictions, stale ideas, broken detail links, and a Now list that has stopped being ordered.
disable-model-invocation: true
allowed-tools: Read, Edit, Glob, Grep, Bash
metadata:
  version: 0.2.0
---

# Groom the Backlog

Read `BACKLOG.md` at the project root, plus any detail files it links to. The file's header states
its own format and section rules; follow those. The convention is described in
[A Backlog in the Repository](https://github.com/raver99/NOMAD-Framework/blob/main/KnowledgeBase/WorkingWithAI/backlog-in-the-repository.md).

## Report before you edit

Grooming is a reporting job before it is an editing job. Fix what is unambiguous, propose the rest.
Anything turning on the user's priorities — what matters most, whether committed work should give
way to a newer idea — is theirs to decide, and guessing silently does more damage than leaving it.

### Fix directly

- Lines that do not match the format the file's own header states
- Broken detail links, and detail files that nothing links to
- Items finished or abandoned in fact but still in an open section, where the evidence is in the
  repository rather than in your memory of a conversation

### Report, do not fix

- **Items that duplicate or contradict each other.** Name both IDs. A committed item alongside an
  idea that would make it unnecessary is the common case, and resolving it is a decision, not a
  cleanup.
- **Ideas stale enough to be worth dropping.** `git log` dates every line, so this is checkable
  rather than a feeling. Propose dropping; do not drop.
- **A Now list longer than a screen.** Also one in ascending ID order, which means it has been
  appended to and never prioritised, whatever the section header claims.
- **Items whose title no longer describes what the work has become.**

## Report

Three things: what you changed, what needs the user's call, and what you deliberately left alone.
The third is not filler — an unexplained omission reads as an oversight. Do not commit; the user
commits.
