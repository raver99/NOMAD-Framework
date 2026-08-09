---
status: planned
type: feature
priority: high
epic: EP-Implementation
updated: 2026-08-09
---

# WI-2 — App version management guide

## Summary

The README's Implementation index already promises "App Version management — Updating users to
newest app version", with no guide behind it. Write that guide: how an app detects it is
outdated and how it gets the user onto a current build without stranding anyone.

Migrated from `TASKS.md` T-002.

## Plan

A single document at `KnowledgeBase/Implementation/app-version-management.md`, sitting beside
the error logging guide from [[WI-1]] in the same new Implementation category.

The core recommendation is that the minimum supported version lives server-side, not baked
into the build — a client cannot be told it is too old by a rule shipped inside itself. From
there the guide covers the decisions a team has to make:

- Version and build numbering, and what each store actually enforces
- The three escalating responses: passive nudge, recommended update, forced update — and the
  bar for using the last one, since a forced update is an outage for anyone who declines
- Where the version check happens and how it fails safe when the check is unreachable
- Store deep links for sending a user to the right place to update
- How this interacts with staged/phased rollout, where "newest" differs per user

Platform agnostic per the content guidelines — the guide names the mechanism, and SDK wiring
belongs in NOMAD.Maui. Cross-reference the publishing checklist, since phased rollout is
configured at submission time.

## Tasks

- [ ] Draft `KnowledgeBase/Implementation/app-version-management.md`
- [ ] Cover numbering, server-driven minimum version, and the fail-safe path when the check is unreachable
- [ ] Set out the three update responses with the bar for forcing one
- [ ] Cover the staged-rollout interaction and store deep links
- [ ] Cross-reference the app store publishing checklist
- [ ] Fill in the README Implementation index row, replacing the "Coming soon" placeholder
