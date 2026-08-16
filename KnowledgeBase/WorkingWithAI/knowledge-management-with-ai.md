# 📘 Knowledge Management with AI – Keeping What the Work Produces

## Purpose of This Document

Working with an AI assistant produces knowledge worth keeping — verified facts, findings from
official sources, decisions and the reasoning behind them. Most of it stays in the conversation and
is lost, and the next person researches it again. This document covers what to keep, where it goes,
how it stays checkable, and which parts of that a project should automate rather than remember.

The guidance is domain agnostic. It assumes a project with an assistant and somewhere to put
documents, not a codebase.

---

## 1. Knowledge management is two acts, not one

Finding and keeping are separate, and conflating them is why knowledge bases fill with unsourced
assertions or stay empty.

| | Research record | Knowledge base entry |
|---|---|---|
| Answers | What was found on a given day | What the project now holds to be true |
| Scope | Everything retrieved, including dead ends | The durable part only |
| Lifetime | Frozen; it is a dated observation | Maintained; it is corrected when it goes wrong |
| Shape | Sources, raw extracts, findings | The project's document conventions |
| Owner | Whoever asked the question | The project |

> **A record is evidence. An entry is a commitment.** Promoting one to the other is a decision
> someone makes, not a side effect of research finishing.

A project that can research but not capture loses the work. A project that can capture but not
research captures claims nobody can check. Both halves are needed, and they are usually built in
that order.

---

## 2. What belongs in the knowledge base

The test is a question about the future, not about the content:

> **Would someone redo this work because they could not find the answer?**

If yes, capture it. If the answer is recoverable from the artifacts themselves, do not — a second
copy goes stale while the original stays right.

| Knowledge | Belongs in |
|-----------|------------|
| A practice, convention or recommendation the project follows | Knowledge base |
| A verified external fact the project depends on (a limit, a format, a requirement) | Knowledge base, with its source |
| A value on someone else's release cycle (a version, a deadline, a price) | Nowhere — capture the pointer instead (§5) |
| Why a decision was made, what was rejected, what it cost | An article, or the decision record |
| Why a specific change was made | The commit message or pull request |
| What the system currently does | The code and its tests |
| What is planned or broken | The issue tracker or work items |
| What was found while investigating, including dead ends | The research record |

✅ **Capture the finding, not the search.** "Play Store requires a privacy policy URL for all apps
since 2023" is knowledge. "I searched three pages and found the console docs unhelpful" is not.

❌ **Do not capture what the artifact already states.** A document restating configuration that
lives in a config file becomes a second source of truth, and the two diverge silently.

---

## 3. Every claim shows where it came from

A claim without a source has to be taken on trust, and the next reader either trusts it wrongly or
researches it again. Both outcomes cost more than recording the source did.

### 3.1 Source tiers

Record the tier alongside every source. It costs a word and it makes a weak evidence base visible
at a glance.

| Tier | Is | Examples |
|------|----|----------|
| **Primary** | The thing itself | Specifications, vendor documentation, source repositories, official APIs, the artifact on disk |
| **Live state** | The thing right now | Status pages, health endpoints, current API responses |
| **Secondary** | Someone describing the thing | Blog posts, tutorials, aggregators, search-result summaries |

Five secondary sources agreeing is not corroboration when all five paraphrase the same primary
source. Trace claims back rather than counting them.

### 3.2 What a reference carries

A URL alone is not enough. A reference records **what was retrieved, when, and at what tier**, so a
future reader can tell a claim that is wrong from a claim that is merely old.

| # | Source | Tier | Retrieved |
|---|--------|------|-----------|
| 1 | [Vendor limit documentation](https://example.com) | primary | 2026-08-16 |

✅ **Date the evidence.** Where two sources conflict, the one carrying a verifiable later date
usually wins, and saying so is stronger than asserting a preference.

✅ **Mark judgement as judgement.** A recommendation that is the project's own opinion says so in
the sentence. It does not need a citation; it needs to not look like a sourced fact.

### 3.3 What this looks like when it is missing

Measured against this repository on 2026-08-16, before the convention was adopted: 7 external links
across 9 knowledge base documents, 6 documents with none at all, and 1 document carrying a
references section. `KnowledgeBase/Publishing/app-store-metadata-reference.md` discussed official
versus secondary sources, compliance deadlines and disputed community claims, and linked to none of
them. Re-checking its dated claims found two of the three already wrong.

That is the failure state. It is not visible from inside the documents, which read as confident —
which is exactly why the convention has to be structural rather than remembered.

---

## 4. When a finding is authoritative enough to capture

Capture is a judgement about evidence, not about usefulness. A useful claim from a weak source is
the most expensive thing a knowledge base can hold, because it is acted on.

✅ **Capture** when the claim traces to a primary source, or to live state that was checked, and the
retrieved date is recorded.

✅ **Capture with the weakness stated** when only a secondary source was reachable — say which
primary source was blocked and what that costs. A named gap is safe; a hidden one is not.

❌ **Do not capture** a claim whose only support is a search-result summary, an undated page, or an
assistant's own recall. Assistant recall in particular reads as authoritative and carries no source
at all.

❌ **Do not capture** a value that moves on someone else's schedule. Point at the live source
instead — §5.

---

## 5. Capture the shape, point at the schedule

The most common way a knowledge base becomes actively misleading is a copied value that has since
changed. It does not look stale. It looks like every other line in the document, and it is read with
the same confidence.

The distinction that matters is not stable versus volatile. It is **whether the value or the shape is
the knowledge**:

| | Shape | Schedule |
|---|---|---|
| Is | Which things exist, how they relate, what constrains what | The current number, version or date |
| Changes | When the domain is redesigned | On someone else's release cycle |
| Wrong how | Visibly — the structure no longer matches | Invisibly — the number still reads as fact |
| Capture | Yes, this is the knowledge | No, capture the pointer |

✅ **Record the gate, not the threshold.** "Publishing is blocked below a minimum platform version;
the current one is here" stays true for years. "The minimum is version 35" is wrong within months and
gives no hint that it has expired.

✅ **Keep values where the value is the point** — a field's character limit, an asset's pixel
dimensions, a protocol's field order. These move slowly and are the reason someone opens the
document. Give them a retrieved date (§3.2).

❌ **Do not mix the two in one section.** Once a section contains both, the durable parts inherit the
volatile parts' shelf life, and the whole section has to be re-verified or distrusted together.
Separate them physically so a reader can see which is which.

> **A section holding only pointers should say so.** State that it deliberately carries no numbers or
> dates, so a future editor does not helpfully fill them in.

Where per-release values genuinely need tracking, they belong in a checklist or a work item —
something with a lifecycle — rather than in a reference document that is read as standing truth.
[App Store Metadata Reference](../Publishing/app-store-metadata-reference.md) §4 is this pattern
applied.

---

## 6. Where a finding lands

Three destinations, in order of preference:

1. **An existing topic document.** Merge it in. One canonical source per topic is what makes a
   knowledge base usable; a second document on the same topic makes both untrustworthy.
2. **A new topic document**, when the subject is genuinely new and there is enough to say.
3. **The research record**, when the finding is durable but too small to carry a document.

> **The record is the holding area.** Findings that have no home wait there until a topic
> accumulates enough to be worth writing.

❌ **Do not create a general notes document** for findings that fit nowhere. It absorbs everything,
gets read by nobody, and removes the pressure that would otherwise produce a real topic document.

❌ **Do not create stub documents** to hold a single line. An index entry pointing at a stub costs a
reader a navigation for nothing.

---

## 7. Capture has to be triggered, not remembered

A capture step that only runs when someone invokes it will run rarely, and the knowledge base will
reflect what people remembered to file rather than what was learned.

The trigger fires **when a research record is completed**, and it is a proposal rather than an
automatic write:

1. Research completes and the record is written.
2. The assistant names which findings are durable, which are situational, and where the durable ones
   would land.
3. A person accepts, edits or declines.

> **Propose, do not file automatically.** Deciding what a project holds to be true is the one step
> worth a human sentence. Automatic capture fills a knowledge base with situational findings, and a
> knowledge base nobody trusts is worse than none.

Declining is a normal outcome. Most research is situational and correctly stays in the record.

---

## 8. Keeping entries true

Captured knowledge decays. External requirements change, vendors move documentation, and a claim
that was right stays in the document looking exactly as authoritative as it did on the day it was
verified.

| Signal | Action |
|--------|--------|
| A reference's retrieved date is old relative to how fast the subject moves | Re-verify before relying on it; update the date whether or not the content changed |
| A source URL no longer resolves | Find the current primary source; if there is none, mark the claim as unverifiable rather than deleting it silently |
| Two entries disagree | One of them is stale. Resolve to a single canonical entry rather than annotating both |
| The claim is now contradicted by live state | Live state wins over documentation. Record both and say which was observed |

✅ **Re-verification is cheap when references are complete and impossible when they are not.** This
is the practical return on §3, and it only arrives later.

---

## 9. The assets a project installs

The guidance above operates only if it is built into the steps people already run. A project should
be able to adopt it the way it adopts a linter configuration.

| Asset | Does |
|-------|------|
| A research skill | Sets depth, prefers primary sources, escalates past blocked pages, writes the layered record |
| A capture step | Takes a record, decides placement — including *nowhere* — writes the entry with its references, updates the index |
| Document conventions | A references table in the template, so an entry without sources looks wrong |
| A seeded index | An index file whose header states the conventions, installed once, so nothing has to be inferred |

> **An installable asset reads the project's conventions rather than carrying its own.** The capture
> step establishes where documents live, how they are grouped and named, and where the index is by
> looking at the base that already exists. Where the two disagree, the project wins — it is what
> people there actually read. An asset that hard-codes one project's layout only works in that
> project.

In this repository these are the `nomad-researcher` skill and the `/add-knowledge` command. They are
connected by the record file rather than by a direct reference: research writes a record to
`docs/research/`, and capture takes that path as its input. Either half works without the other
installed.

See [Claude Code Skills](../ClaudeCode/claude-code-skills.md) for how skills are organised and
scoped, and [Skill Authoring Rules](../ClaudeCode/skill-authoring-rules.md) for writing them.

---

## 10. Summary

1. **Finding and keeping are separate acts.** A record is dated evidence; an entry is a maintained
   commitment. Promotion between them is a decision.
2. **Capture what someone would otherwise redo**, and nothing that an artifact already states.
3. **Every claim shows a source with a tier and a retrieved date**, or says plainly that it is
   judgement.
4. **Authority decides capture, not usefulness.** A useful claim from a weak source is the most
   expensive thing to hold.
5. **Capture the shape, point at the schedule.** A copied version or deadline goes wrong invisibly,
   because it reads exactly like the durable lines around it.
6. **One canonical document per topic.** Findings with no home wait in the record rather than
   collecting in a notes document.
7. **Trigger capture when the record completes**, and propose rather than file automatically.
8. **Re-verify against the retrieved date.** Complete references make this cheap; missing ones make
   it impossible.
9. **Install the practice as assets**, because a convention that depends on memory is not a
   convention.

---

## References

| # | Source | Tier | Retrieved |
|---|--------|------|-----------|
| 1 | Repository audit of `KnowledgeBase/` — 7 external links across 9 documents, 6 with none, 1 with a references section | primary | 2026-08-16 |
| 2 | `plugins/nomad-knowledge/skills/nomad-researcher/SKILL.md` — source tiers, depth, the layered record | primary | 2026-08-16 |
| 3 | `plugins/nomad-knowledge/commands/add-knowledge.md` — placement rules and the document template | primary | 2026-08-16 |

The practices in §2, §4, §5, §6 and §7 are this project's own judgement rather than sourced claims. They
were derived from the failure state measured in [1] and have not been validated against other
projects.
