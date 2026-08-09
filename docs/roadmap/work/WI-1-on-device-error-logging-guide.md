---
status: planned
type: feature
priority: high
epic: EP-Implementation
updated: 2026-08-09
---

# WI-1 — On-device error logging guide

## Summary

The knowledge base covers requirements, publishing and CI, but nothing yet on what an app
should do when it fails in a user's hands. Write the "On device error logging" guide — the
first entry in an Implementation category — so a team can pick a crash and error reporting
setup without re-running the evaluation themselves.

## Plan

A single document at `KnowledgeBase/Implementation/on-device-error-logging.md`, following the
shape the existing guides already use: a short problem statement, a recommendation, then the
detail behind it.

Keep it platform agnostic per the content guidelines — the guide names the criteria and the
recommended service, and leaves SDK wiring to the platform repos (NOMAD.Maui and friends).
Cover the decisions a team actually has to make: what to capture (unhandled crashes, handled
exceptions, breadcrumbs, user context), where it goes, how offline and delayed delivery are
handled, what personal data must not leave the device, and how release/version tagging ties a
report back to a build.

Give one opinionated recommendation with the trade-off stated rather than a comparison
matrix. Cross-reference the publishing checklist, since store review expects crash reporting
to already be in place, and the CI guide for symbol/mapping upload.

## Tasks

- [ ] Create the `KnowledgeBase/Implementation/` category directory
- [ ] Draft `on-device-error-logging.md`: problem statement, selection criteria, recommendation
- [ ] Cover capture scope, offline buffering, PII boundaries, and version/release tagging
- [ ] Cross-reference the app store publishing checklist and the CI pipeline guide
- [ ] Add the new category and document to the README index
- [ ] Close out T-001 in `TASKS.md`
