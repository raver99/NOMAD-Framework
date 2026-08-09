---
status: planned
type: feature
priority: medium
epic: EP-Testing
updated: 2026-08-09
---

# WI-3 — First testing strategy topic

## Summary

"Testing mobile apps" is one of the four aspects the README claims NOMAD covers, and its index
table is the only one that is entirely empty. Write the entry topic that opens the category
and gives later testing documents a shared vocabulary to build on.

Migrated from `TASKS.md` T-003.

## Plan

The first decision this item has to make is *which* topic goes first, and the answer should be
the one everything else depends on: what to test at which level. Recommendation is a document
at `KnowledgeBase/Testing/what-to-test-where.md` covering the split between unit, integration,
UI automation and manual exploratory testing on mobile specifically.

Mobile is what makes this worth writing rather than linking to general testing advice — UI
automation is markedly more expensive and more brittle on device than on web, emulator time is
slow, and store review adds a feedback loop measured in days. That cost curve is what should
drive the recommended split, so the guide gives a concrete default allocation and the
reasoning behind it, rather than restating the test pyramid.

Keep it opinionated and platform agnostic: one recommended split with trade-offs stated, and
framework-specific runners left to NOMAD.Maui. Structure it so later topics — device
coverage, test data, CI integration — slot in beside it without restating this one.

## Tasks

- [ ] Confirm the entry topic before drafting: "what to test where" versus an alternative first topic
- [ ] Create the `KnowledgeBase/Testing/` category directory
- [ ] Draft the guide: the four levels, and what belongs at each on mobile
- [ ] Make the mobile-specific cost argument (device time, brittleness, store review latency) explicit
- [ ] Give one recommended default split with trade-offs stated
- [ ] Add the Testing category rows to the README index
