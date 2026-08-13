---
status: planned
type: feature
priority: high
epic: EP-AICollaboration
updated: 2026-08-11
---

# WI-6 — Knowledge management with AI

## Summary

Working with an AI assistant produces knowledge worth keeping — research findings, verified
facts from official sources, decisions and their reasoning — but nothing currently makes that
knowledge land anywhere. It stays in the conversation and is lost. Establish knowledge
management as a NOMAD topic: a guide on how to work with a knowledge base alongside AI, plus
the reusable assets (skills, custom instructions) a project drops in to actually do it.

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
config. Where they live and how they get installed into a target project needs settling.

Two concrete gaps already found, which the work should close:

*Capture is never triggered.* `/add-knowledge` only runs when a person invokes it and hands it
source material. Nothing prompts capture at the moment research actually produces something
worth keeping, so the decision depends entirely on someone remembering to make it.

*Sources are never recorded.* The `/add-knowledge` document template has no references section,
and its research step tells the model to research and report findings without recording where
they came from. The knowledge base shows the result: three external links across nine
documents, and no references section anywhere.
`KnowledgeBase/Publishing/app-store-metadata-reference.md` discusses official versus secondary
sources, compliance deadlines and disputed community claims in its Caveats section, and links
to none of them — so every claim must be taken on trust or researched again from scratch.

## Tasks

- [ ] Write the knowledge management guide in the knowledge base
- [ ] Define what makes a source authoritative enough to capture, and what gets skipped
- [ ] Add a references convention to the `/add-knowledge` template and its research step
- [ ] Define the capture trigger: how a finding gets proposed for the knowledge base mid-research
- [ ] Decide whether capture is proposed to the user or automatic, and where findings land when no topic file fits
- [ ] Package the skills and custom instructions so another project can adopt them
- [ ] Back-fill sources into existing knowledge base documents, starting with the app store metadata reference
- [ ] Add the guide to the README index
