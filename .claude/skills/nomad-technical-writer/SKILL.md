---
name: nomad-technical-writer
description: Use when writing or revising a knowledge base guide, an article, release notes, a README or any prose in this project. Also when asked to explain the reasoning behind a decision, or when existing text reads as padded, generic or hedged.
metadata:
  version: 0.2.0
---

# Technical Writer

## 1. Establish the audience before writing

Level cannot be inferred from the topic. Get three answers first:

1. **Who reads this?** Their role, and what they already work with daily.
2. **What should they be able to do afterwards?** The document succeeds or fails at this.
3. **What can be assumed known?** Name the concepts that get used without explanation.

Ask the user. This is the case where a question earns its cost — the answer changes the whole
document, and guessing wrong is expensive to undo.

Ask once, up front, and offer a proposed answer for each so the reply is a correction rather than an
essay. If the request already implies the answers, state the reading you are working from and carry
on rather than stopping for confirmation.

> **Why this comes first:** a document pitched at the wrong level cannot be repaired sentence by
> sentence. Each patch fixes a local symptom and exposes another, because the problem is altitude,
> not wording. Getting this wrong is the single largest source of rework.

The output of this step is a decision about what gets explained and what gets used bare. Write it
down before drafting, so the choice is deliberate rather than drifting paragraph by paragraph.

## 2. Know which of the two documents you are writing

| | Knowledge base guide | Article |
|---|---|---|
| Answers | What and how | Why |
| Read | By lookup, repeatedly | Once, start to finish |
| Shape | Numbered sections, tables, rules | Narrative, argued |
| Holds | The decision | The reasoning, what was rejected, what it cost |

They cross-reference rather than repeat. One canonical source per topic: if the rule is in the
guide, the article links to it instead of restating it.

## 3. State what is, not what it isn't

Do not write the decision *against* a discarded alternative. A guide that says "we structure by
feature, not by screen" makes the reader construct screen-based structure and then throw it away —
work they did not ask for, defending a choice they had not challenged.

> **The test:** "not Y" is earned only when **Y is what the reader would otherwise believe or do**.
> It is not earned when Y is merely what the author considered and discarded.

This happens because deliberation leaks into the artifact. Alternatives that cost effort to
evaluate feel informative, so they surface in the prose — but effort spent by the writer is not
value delivered to the reader. The reader was never in that conversation.

When a contrast is genuinely earned, give it its own sentence with the reason attached. Jammed in
mid-sentence as an aside, it reads as a tic even when the content is right.

✅ `Requirements are organised by feature.`
✅ `Requirements are organised by feature. Screen-based structures are common in older specs, and
they fragment a single behaviour across every screen it touches.`
❌ `Requirements are organised by feature, not by screen.`

Rejected alternatives are the *subject* of an article and noise in a guide. If the discarded option
deserves discussion, it belongs in the article, at length and in the open.

## 4. Tone

The register of good trade writing: plain declarative sentences addressing a competent peer.
Neither formal nor chatty.

Strip on sight:

- **Throat-clearing** — openings that restate the question or announce what the document will do.
- **Both-sidesing** — options laid out without a recommendation. A comparison that ends without a
  call has not finished.
- **Hedging** — "it may be worth considering that". Say whether it is worth doing, and what would
  change the answer.
- **Recap summaries** — a closing section carries the takeaways a reader needs to leave with, not a
  replay of what they just read.
- **Adjective inflation** — powerful, seamless, robust, comprehensive. Delete them; if a claim
  survives, it was doing the work.
- **Symmetry for its own sake** — three bullets because three looks tidy, when there were two real
  points.
- **Enthusiasm about the subject**, exclamation marks, jokes, and "let's dive in".

## 5. Write from evidence

Every claim either shows its source or is marked as judgement. A guide that asserts a limit without
saying where it came from cannot be re-checked when the source moves, and the next reader redoes the
research.

Prefer the concrete: "of the 25 skills in the official marketplace, one carries evals" beats "evals
are uncommon in practice". A reader can verify the first, and it fails visibly if it is wrong.

## 6. Structure carries the meaning

Headers, tables and lists are how a reader navigates without reading everything. A table when
contrasting comparable things, a list when order matters, prose when reasoning has to be followed.
Do not use a table to hold sentences that are not comparable.

Number the sections in knowledge base guides so they can be cited precisely from skills and other
documents.

## 7. Name the gaps

State assumptions, open questions and the limits of what was checked. A document that quietly papers
over a gap costs more than one that names it, because the reader finds out after relying on it.

## House conventions

Knowledge base guides follow the structure in `.claude/commands/add-knowledge.md`: purpose
statement, numbered sections, comparison tables where options are contrasted, and a summary of
takeaways.

Cross-reference related NOMAD documents by relative path rather than duplicating their content.
Content stays platform agnostic — platform specifics belong in the implementation repositories.
