---
status: planned
type: feature
priority: high
epic: EP-AICollaboration
updated: 2026-08-16
---

# WI-7 — Working with AI agents

## Summary

Working with an AI agent well is a skill with its own practices, and they are not specific to
software. Structuring knowledge so an agent can use it, running research that produces
trustworthy answers, communicating so intent survives, validating output instead of trusting
it — these apply to a legal review, a business plan or a research project as much as to a
mobile app. Capture them as a NOMAD area in their own right.

This is the umbrella. [WI-5](WI-5-general-ai-behavior.md) (conversational behavior) and
[WI-6](WI-6-knowledge-management-with-ai.md) (knowledge management) are already branched out of
it and stay separate items.

## Plan

The output is the usual NOMAD pair: opinionated written guidance, plus the skills and custom
instructions that make the guidance operate in a real project without anyone remembering it.
The distinguishing constraint is that this content is **domain agnostic** — it must not assume
a codebase, a repository or a technical user.

### Candidate topics

The initial set, to be refined before anything is written:

- **Structuring knowledge for agents** — how knowledge is organised so an agent finds and reuses
  it rather than re-deriving it. Overlaps [WI-6](WI-6-knowledge-management-with-ai.md); the split
  between them needs settling.
- **How to research** — what a good research request looks like, how deep to go, source quality
  and how to judge it, when to stop, and how findings get recorded so the work is not repeated.
- **Communicating efficiently** — stating intent and constraints, giving the right context
  without flooding it, pacing a conversation, recognising when the agent has misread the task.
  Overlaps [WI-5](WI-5-general-ai-behavior.md).
- **Cross-checking and validation** — using a second agent to review, refute or independently
  redo work rather than accepting the first answer. When the cost is worth it, and what a
  reviewing agent must not be told in order to stay independent.
- **Scoping and decomposition** — sizing a task so an agent can finish it, and splitting what it
  cannot.
- **Deciding what to delegate** — which work an agent should do, which it should assist with,
  and which stays human.
- **Verification and trust** — how a claim gets checked, what evidence an agent should be
  required to produce, and how confident output is calibrated against actual reliability.
- **Tracking work** — *delivered 2026-08-16.* Where a project keeps work and ideas so an agent can
  read them without an external tracker. Guide at
  `KnowledgeBase/WorkingWithAI/backlog-in-the-repository.md`, assets in the `nomad-backlog` plugin.

### Open questions

- **Project scope.** NOMAD presents itself as a mobile application development framework, and
  the README already notes that some practices extend to software development generally. This
  area goes further — to non-technical projects. Either the README's framing is widened, or
  this becomes an explicitly general-purpose section within a mobile-focused framework.
- ~~**Where domain-agnostic content lives.**~~ **Settled 2026-08-16:**
  `KnowledgeBase/WorkingWithAI/`, README category "Working with AI". The premise behind this
  question was wrong — `KnowledgeBase/` is not organised around mobile delivery. Of its documents,
  only the two under `Publishing/` are mobile-specific; `Requirements/`, `SpecDrivenDevelopment/`
  and `ClaudeCode/` are already general. Adding a domain-agnostic area was not a departure needing
  the README reframed first. The earlier `AICollaboration/` directory was consolidated into
  `WorkingWithAI/`; the `EP-AICollaboration` epic slug is unchanged, as it is a tracking identifier
  rather than a path.
- **A research skill.** Discussed as a likely first concrete asset in this area; not yet
  scoped, and gets its own work item once it is.

## Tasks

- [ ] Settle the project scope question and update the README framing accordingly
- [ ] Refine the candidate topic list and fix the boundaries against WI-5 and WI-6
- [x] Decide where domain-agnostic content lives and add the README category
- [ ] Write the topics, starting with research and with cross-checking/validation
- [ ] Package the accompanying skills and custom instructions for adoption by other projects —
      done for tracking work (`nomad-backlog` plugin, 0.1.0); open for the remaining topics
- [ ] Scope the research skill as its own work item
