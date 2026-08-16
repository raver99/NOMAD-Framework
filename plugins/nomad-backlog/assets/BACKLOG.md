# Backlog

One line per item: `- [ ] **ID** Title`, plus an optional `` `#tag` `` and an optional link to a
detail file. IDs are assigned once and never reused, so gaps are meaningless. Status is which
section the line sits in and lives nowhere else — a detail file carries context and reasoning,
never metadata. Changing state means moving the line.

Closing dates go at the end of the line as `(YYYY-MM-DD)`. Tags travel with a line when it moves.
There are no sub-items: work that belongs inside another item goes in that item's detail file. To
link two items, name the other ID in the title.

Delete the example lines below. The rules above are what carries the format, not the examples.

## In progress

What is being worked on right now, so a new session can pick up where the last one stopped. Usually
one item, occasionally two. Empty is a normal state.

## Now

Ordered — the top line is the next thing. If this section does not fit on a screen, it is not a Now
list. Ordering only means something near the top; nobody sorts the eighth item against the ninth.

- [ ] **T-001** Example: replace this with real work `#example`

## Later

Real work, agreed it should happen, no claim about sequence. Moving a line from here to Now is the
act of prioritising it.

- [ ] **T-002** Example: an item that needs a body of its own → [detail](backlog/T-002.md)

## Ideas

Uncommitted. No obligation and no readiness bar — promoting one is a judgment call, not a checklist.

- [ ] **T-003** Example: a half-formed thought worth not losing

## Done

- [x] **T-000** Example: a finished item, dated when it finished (2026-08-16)

## Dropped

Kept, never pruned. A deleted decision gets re-proposed by the next agent that reads this file, and
then re-argued from scratch. The box stays unticked because the work was never done; the section
already says it is closed. One line of reason, then the date it was dropped.

- [ ] **T-004** Example: something decided against — Sentry already covers it (2026-08-16)
