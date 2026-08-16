---
name: nomad-backlog-capture
description: Add a piece of work or an idea to the project's BACKLOG.md, without duplicating something already captured or reviving something already dropped.
disable-model-invocation: true
arguments:
  - name: item
    description: The work or idea to capture, in whatever wording comes naturally
    required: false
allowed-tools: Read, Edit, Glob, Grep
metadata:
  version: 0.1.0
---

# Capture a Backlog Item

The item is: $ARGUMENTS

If nothing was given, ask what to capture and stop.

## The file states its own format

Read `BACKLOG.md` at the project root first. Its header defines the line format, the sections and the
rules — follow that rather than any backlog convention carried in from elsewhere. If the header and
this skill ever disagree, the file wins; it is what the project actually uses.

The convention is described in
[A Backlog in the Repository](https://github.com/rolandhuhn/NOMAD/blob/main/KnowledgeBase/WorkingWithAI/backlog-in-the-repository.md).

## What this skill adds

**Read the whole file before adding, including Ideas and Dropped.** This is the one step worth
naming, because it is the one a hurried capture skips. Something already captured should be pointed
out rather than duplicated. Something already dropped should be raised with the user rather than
quietly revived — the reason it was dropped is on the line, and it may still hold.

**Capture what was meant, not more.** A hedged "we should probably look at whether…" is an Idea. A
decision already taken is Now or Later. Promoting is the user's call, so where the wording is
genuinely ambiguous, put it in Ideas and say that is what you did.

**One line.** A detail file is earned by having real reasoning to hold, not by an item feeling
important. Capturing a single sentence does not earn one.

**Change nothing else.** Do not reorder, demote or tidy other items to make room. If Now is now too
long, say so and leave it — what to demote is a priority decision.

## Report

The ID, the section it went to, and anything decided on the user's behalf. Do not commit; the user
commits.
