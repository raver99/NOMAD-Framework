---
name: nomad-technical-writer
description: Use when writing or revising a knowledge base guide, an article, release notes, a README or any prose in this project. Also when asked to explain the reasoning behind a decision, or when existing text reads as padded, generic or hedged.
metadata:
  version: 0.1.0
---

# Writing Technical Docs

NOMAD publishes two kinds of prose and they have different jobs. Establish which one is being written
before starting, because the failure mode is writing one in the shape of the other.

| | Knowledge base guide | Article |
|---|---|---|
| Answers | What and how | Why |
| Read | By lookup, repeatedly | Once, start to finish |
| Shape | Numbered sections, tables, rules | Narrative, argued |
| Holds | The decision | The reasoning behind it, what was rejected, what it cost |

They cross-reference rather than repeat. One canonical source per topic: if the rule is in the guide,
the article links to it instead of restating it, and the article is where the evidence and the
discarded alternatives live.

## Write from evidence

Every claim either shows its source or is marked as judgement. A guide that asserts a limit without
saying where it came from cannot be re-checked when the upstream source moves, and the next reader
has to redo the research.

Prefer the concrete over the abstract. "Of the 25 skills in the official marketplace, one carries
evals" is worth more than "evals are uncommon in practice", because a reader can verify it and it
survives being wrong in a visible way.

## Cut the padding

The default register of AI-written prose is fluent, balanced and empty. It reads well and says
little. Specific habits to strip:

- **Throat-clearing.** Openings that restate the question or announce what the document will do.
  Start with the content.
- **Both-sidesing.** Laying out options without recommending one. NOMAD is opinionated; a comparison
  that ends without a call has not finished.
- **Hedging.** "It may be worth considering that..." either it is worth doing or it is not. Say
  which, and say what would change the answer.
- **Summary that repeats.** A closing section is for the takeaways a reader needs to leave with, not
  a recap of what they just read.
- **Adjective inflation.** "Powerful", "seamless", "robust", "comprehensive" carry no information.
  Delete them; if a claim remains, it was doing the work.
- **Symmetry for its own sake.** Three bullets because three looks tidy, when there were two real
  points.

## Structure carries the meaning

Headers, tables and lists are how a reader navigates without reading everything. Use a table when
contrasting options, a list when order matters, prose when the reasoning has to be followed. Do not
use a table to hold sentences that are not comparable.

Numbered sections in knowledge base guides, so they can be cited precisely from skills and other
documents.

## Say what is not known

State assumptions, unresolved questions and the limits of what was checked. A document that quietly
covers gaps is more expensive than one that names them, because the reader discovers the gap after
relying on it.

## House conventions

Knowledge base guides follow the structure in `.claude/commands/add-knowledge.md`: purpose statement,
numbered sections, comparison tables where options are contrasted, and a summary of takeaways.

Cross-reference related NOMAD documents by relative path rather than duplicating their content.
Content stays platform agnostic — platform specifics belong in the implementation repositories.
