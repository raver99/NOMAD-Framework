---
name: nomad-researcher
description: Use when researching a topic, evaluating tools or approaches, checking how something actually works, or verifying a claim before relying on it. Also when a decision needs authoritative backing, or when web results look thin, paraphrased or blocked.
metadata:
  version: 0.5.0
---

# Researcher

Research output becomes the foundation other work is built on, so a weak finding is expensive far
downstream. The job is not to produce an answer quickly — it is to produce an answer whose basis
someone else can check.

## 1. The bias to correct for

**What is reachable is a biased sample, and the bias runs against authority.** Many high-value
sources block automated fetching, while a great deal of accessible content is paraphrase, summary
and search-engine filler. Availability and quality are not merely uncorrelated here; in places they
run opposite.

The failure that matters is not the blocked page. It is quietly substituting an accessible secondary
source that paraphrases the blocked primary one, producing a citation that looks solid and is
second-hand.

> Treat a blocked source as **something to retrieve another way**, not as a reason to lower the
> standard of evidence.

## 2. Source tiers

Record the tier of every source. It costs a word and it makes a weak evidence base visible.

| Tier | Is | Examples |
|------|----|----------|
| **Primary** | The thing itself | Specifications, vendor documentation, source repositories, the installed artifact on disk, official APIs |
| **Live state** | The thing right now | Status pages, health endpoints, the running service, current API responses |
| **Secondary** | Someone describing the thing | Blog posts, tutorials, aggregators, search-result summaries, news coverage |

Live state deserves its own line because documentation answers "what was published" while a status
page answers "what is true today", and those diverge — a service can be documented as ended and be
demonstrably running.

Five secondary sources agreeing is not corroboration when all five paraphrase the same primary
source. Trace claims back rather than counting them.

## 3. Match the depth to the decision

Depth is set by what the answer will be used for, not by how large the topic is. A question that
looks broad can need one source; a one-line claim can need three if a release depends on it.

| Depth | Use when | Work |
|-------|----------|------|
| **Check** | A single claim needs confirming before it is relied on | One primary source, dated. Answer inline; no record file. |
| **Standard** | Choosing between known options, or producing something to be captured | A primary source per claim, tiers recorded, full layered record (§5). |
| **Deep** | The decision is expensive to reverse, or sources conflict | Standard, plus tracing secondary claims back to the primary, checking documentation against artifacts, and first-principles reasoning where sources are absent. |

State the depth at the start, so the requester can correct it before the work is done rather than
after. Escalate mid-way when the evidence justifies it — a check that turns up two sources
disagreeing has become a standard, and saying so is better than answering thinly at the depth
originally agreed. Escalation is a finding in itself; record what forced it.

Do not deepen by default. Depth spent on a reversible choice is not free — it delays the answer and
buries the part that mattered.

## 4. Procedure

**Go for primary sources.** Identify who actually owns the answer — the vendor, the spec author, the
maintainer — and go there. Search results are a way to locate primary sources, not a source in
themselves.

**Read the artifact, not the description of it.** Fetch raw files rather than repository landing
pages, which return navigation rather than content. Where the subject is installed locally, read what
is on disk; it is the ground truth and it cannot be out of date relative to itself.

**Escalate when blocked.** On a 403 or a blocked response for a public page, retrieve it through a
browser session (Chrome MCP) rather than accepting a weaker substitute. If that also fails, the
source is unretrieved — record it as such (§6).

**Check claims against practice.** The highest-value findings come from comparing what documentation
*states* against what artifacts *contain*. Documented guidance and actual behaviour diverge often,
and nobody writes that divergence down. Where a claim is checkable, check it and report the count.

**Date the evidence.** Capture when a page was last updated — publication metadata, a changelog entry,
a commit date — alongside what it says. It converts "this looks stale" into a demonstrable claim, and
it separates a page that is wrong from a page that is merely old. Where two sources conflict, the one
carrying a verifiable later date usually wins, and saying so is stronger than asserting a preference.

**Reason from first principles where sources are absent or conflict.** State plainly when a
conclusion is derived rather than sourced, so it is weighted accordingly.

## 5. The record is layered

Keep evidence and interpretation physically apart, so a claim can be re-checked when its source
moves and so a reader can filter to whichever layer they need.

```markdown
# <the question, as asked>
**Depth:** standard — escalated from check, sources [2] and [4] disagreed on the limit.

## Sources
| # | Source | Tier | Retrieved | How |
|---|--------|------|-----------|-----|
| 1 | https://... | primary | 2026-08-13 | direct fetch |
| 2 | https://... | primary | 2026-08-13 | browser session after 403 |

## Raw extracts
### [1] <what this is>
> Verbatim or near-verbatim. Unedited, uninterpreted.

## Findings
1. **<Finding>** — what it means and why it matters here. Sources: [1], [2].
```

Interpretation lives only in Findings. If a sentence in Raw extracts contains a judgement, it is in
the wrong layer.

### Where the record goes

Persistence belongs to whoever owns the conversation, not to a delegated worker.

- **Working in the main conversation** — write the record to a file in the requesting project,
  `docs/research/` by default, named for the question.
- **Running as a subagent** — return the complete record as text and leave persistence to the
  caller. Some harnesses refuse subagent file writes outright, with wording along the lines of
  *"subagents should return findings as text"*.

If a write is refused or unavailable, return the full record inline and say plainly that it was not
persisted, so the caller can save it. Losing the record to a silent refusal is the one outcome this
skill cannot afford — research that stays in the conversation is research that will be redone.

## 6. Record what could not be reached

List sources that were identified as relevant and not retrieved, with the reason: blocked, paywalled,
requires an account, no longer published. An unreported gap reads as ground that was covered.

Say what the gap costs. "The vendor's own limit could not be retrieved, so the figure below comes
from a secondary source" tells a reader exactly how much weight to place on it.

## 7. Hand off to capture

Research worth doing is worth keeping. Once the record exists, offer to fold the durable parts into
the project's knowledge base, carrying the sources and their tiers across.

Which step does that depends on the project. Where a capture step is installed — `/add-knowledge`,
which ships alongside this skill — name it and hand the record path to it. Where none is, say so and
leave the record as the place the knowledge currently lives, so nobody assumes it was filed.

The two are separate acts on purpose: the record is what was found on a given day, the knowledge base
entry is what the project now holds to be true. Findings that are situational stay in the record.
