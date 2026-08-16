---
status: in-progress
type: feature
priority: high
epic: EP-AICollaboration
updated: 2026-08-16
---

# WI-6 — Knowledge management with AI

## Summary

Working with an AI assistant produces knowledge worth keeping — research findings, verified
facts from official sources, decisions and their reasoning — but nothing currently makes that
knowledge land anywhere. It stays in the conversation and is lost. Establish knowledge
management as a NOMAD topic: a guide on how to work with a knowledge base alongside AI, plus
the reusable assets (skills, custom instructions) a project drops in to actually do it.

Knowledge management is the whole; **finding** and **keeping** are its two halves. Research
produces a record on a given day; capture turns the durable parts of that record into what the
project holds to be true. The halves ship together, because a project that can research but not
capture loses the work, and a project that can capture but not research captures unsourced
claims.

Branched out of WI-5, which covers conversational behavior rather than knowledge handling. Sits
under [WI-7](WI-7-working-with-ai-agents.md), the general AI collaboration area.

## Plan

Two deliverables, and they are different in kind.

**The guide** — a knowledge base document on knowledge management with AI. What belongs in a
knowledge base versus what belongs in code, commit messages or issue trackers. How knowledge is
structured so an assistant can find and reuse it. When a finding is authoritative enough to
capture. How captured knowledge stays traceable and gets re-verified when the upstream source
moves. This is the NOMAD-style opinionated guidance a team reads once.

**The assets** — the skills and custom instructions that make the guidance operate without
anyone remembering it. A project should be able to adopt them the way it adopts a linter
config.

## Decided so far

**The researcher exists and owns the finding half.** `nomad-researcher` is written and committed.
It carries the source-tier convention this item asked for — primary, live state, secondary,
recorded per source — plus a record layered into sources, raw extracts and findings, escalation
past a blocked page rather than substitution of a weaker one, and an explicit list of what could
not be reached. The convention now exists in the skill rather than in `/add-knowledge` or the
knowledge base, so the guide should cite it rather than restate it.

**`/add-knowledge` belongs in the package.** It is the keeping half, and it is NOMAD-specific in
its filing rules — `KnowledgeBase/` directories, the README index, one canonical source per topic.
The researcher is self-contained enough to ship alone, and shipping it alone was considered; it
loses the capture step that makes research worth doing, so the two are packaged as one
knowledge-management set.

**The record file is the interface between them.** `/add-knowledge` Step 1 already accepts a file
path as its input, and the researcher already writes a record to `docs/research/`. Neither needs a
hard reference to the other — the file connects them. The researcher's §6 handoff should name a
capture step conditionally, so it degrades cleanly where none is installed.

**`/add-knowledge` Step 3 is superseded.** It runs its own research, offering depth options and
reporting findings as validated / gaps / outdated / suggested additions, with no sources recorded.
That is the gap this item diagnosed, and the researcher now does the same job properly. Step 3
should take a record or invoke the researcher instead of researching on its own.

## Open questions

**How deep to go.** The researcher gives every request the same treatment; it has no notion of
scope or depth. `/add-knowledge` Step 3 had a crude version of this in its three depth options.
Overlaps the "How to research" topic in [WI-7](WI-7-working-with-ai-agents.md) and the split needs
settling — the depth heuristic is general guidance, the researcher is the asset that applies it.

**When capture fires.** `/add-knowledge` only runs when a person invokes it and hands it source
material. Nothing prompts capture at the moment research produces something worth keeping, so the
decision depends on someone remembering to make it. Whether capture is proposed or automatic, and
where a finding lands when no topic file fits, is still open.

**Sources in the knowledge base itself.** The document template has no references section, and the
result shows: three external links across nine documents, and no references section anywhere.
`KnowledgeBase/Publishing/app-store-metadata-reference.md` discusses official versus secondary
sources, compliance deadlines and disputed community claims in its Caveats section, and links to
none of them — so every claim must be taken on trust or researched again from scratch.

## Tasks

- [x] Establish the source-tier convention (delivered in `nomad-researcher`)
- [x] Strip the research step from `/add-knowledge` and have it consume a record instead
- [x] Make the researcher's capture handoff conditional so it works where no capture step exists
- [x] Add a references convention to the `/add-knowledge` document template
- [x] Define the capture trigger, and where findings land when no topic file fits (guide §6, §7)
- [x] Settle the depth heuristic with [WI-7](WI-7-working-with-ai-agents.md) (`nomad-researcher` §3)
- [x] Write the knowledge management guide in the knowledge base
- [x] Define what makes a source authoritative enough to capture, and what gets skipped (guide §4, §5)
- [x] Package the knowledge-management set so another project can adopt it (`nomad-knowledge` plugin)
- [x] Back-fill sources into the app store metadata reference
- [x] Add the guide to the README index
- [x] Establish the shape-versus-schedule rule and apply it to the app store metadata reference
- [ ] Back-fill the remaining unsourced claims in the app store metadata reference — Apple text-field
      limits, app preview video specs, and Google title and full-description limits
- [ ] Back-fill sources into the other seven knowledge base documents
- [ ] Confirm plugin installation end to end from a second project
