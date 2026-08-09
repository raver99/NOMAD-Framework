---
status: planned
type: feature
priority: medium
epic: EP-ClaudeCode
updated: 2026-08-09
---

# WI-4 — Project health command

## Summary

NOMAD documents best practices but has no way to tell whether a given project actually follows
them. Build a Claude Code command that checks a project against NOMAD guidance and reports
what is missing — starting with branching strategy.

Migrated from `TASKS.md` T-004.

## Plan

A command in `.claude/commands/`, shaped as one check to begin with rather than a framework
for checks that do not exist yet. It reads the target repository, compares what it finds
against the documented practice, and reports violations with the guide to read.

There is a dependency to settle first: **NOMAD has no branching strategy document.** The
knowledge base covers requirements, CI pipelines, publishing and Claude Code, but nothing
states the recommended branching model — so there is currently no canonical rule for the
command to check against. Either that guide gets written first, or this item is rescoped to a
check whose practice is already documented.

Report, do not enforce, in the first version. A command that rewrites a repository to match a
convention is a much larger commitment than one that names the gap, and the reporting version
is what establishes whether the checks are right. Design the check contract — what a check
reads, what it reports — so later checks for error logging, CI structure and store metadata
plug in without reworking the command.

## Tasks

- [ ] Settle the dependency: write the branching strategy guide, or rescope to an already-documented practice
- [ ] Define the check contract: inputs, findings, and how a finding cites its guide
- [ ] Implement the command with a single check end to end
- [ ] Report-only output; no automatic rewriting of the target repository
- [ ] Verify against a real repository with a known violation
- [ ] Add the command to the README Claude Code index
