Fold a finding into this project's knowledge base, as a new document or a merge into an existing one.

Your input is: $ARGUMENTS

---

## Step 0: The Knowledge Base States Its Own Conventions

Every project files knowledge differently. Establish this project's conventions before writing
anything, and follow them rather than any convention carried in from elsewhere. Where this command
and the project disagree, the project wins — it is what people there actually read.

**Read the index header first.** `KNOWLEDGE.md` at the project root, or whatever file indexes the
documents, states where documents go, how they are named, what shape they take and what a reference
carries. Where a header exists, it is the specification and nothing below applies. A header states
its rules whether the index holds fifty documents or none, so an empty base is not a problem to solve.

**Where no header exists, infer from what is there** — and say that you are inferring:

| What | How to find it |
|------|----------------|
| **Root** | The directory holding the documents — `KnowledgeBase/`, `docs/`, `wiki/` or the repository root. Whichever already has topic documents in it. |
| **Grouping** | Whether documents sit in per-topic subdirectories or flat, and how those are named (PascalCase, kebab-case, none). |
| **Filenames** | The style already in use, taken from sibling files rather than assumed. |
| **Index** | The file listing the documents — a README section, a `SUMMARY.md`, an index page — and the exact row format it uses. There may be none. |

State what you found in one line before proceeding, so a wrong reading is cheap to correct:
*"Filing into `KnowledgeBase/<PascalCase>/kebab-case.md`, indexed in README.md under a per-category
table — inferred, this project has no conventions header."*

**Where nothing exists at all**, stop and point at `nomad-knowledge-setup`, which installs a seeded
`KNOWLEDGE.md` whose header carries the conventions. Do not invent a layout — a layout invented in
one conversation is a layout no other project shares.

---

## Step 1: Determine Input Type

Determine whether the input above is:
- **A file path** (e.g., starts with `/`, `./`, `~`, or looks like a path ending in a file extension) — if so, read the file and use its contents as the source material. A research record under `docs/research/` is the expected case.
- **Inline text** — if so, use the text directly as the source material.

If a file path is provided but the file does not exist or cannot be read, stop and tell the user.

---

## Step 2: Decide Where It Lands — Including Nowhere

Not everything worth finding is worth filing. Work through the destinations in order and stop at the
first that fits:

1. **An existing document on this topic.** Merge into it. One canonical source per topic is what makes
   a knowledge base usable; a second document on the same subject makes both untrustworthy. Check for
   one before concluding the topic is new.
2. **A new document**, when the subject is genuinely new *and* there is enough to say to fill one.
3. **Nowhere — it stays in the research record.** The finding is durable but too small to carry a
   document, and no existing document is the right home. Say so and stop. The record is the holding
   area until a topic accumulates enough to be worth writing.

❌ **Do not create a stub document** to hold a single line. An index entry pointing at three sentences
costs a reader a navigation for nothing.

❌ **Do not create a general notes or miscellaneous document** for findings that fit nowhere. It
absorbs everything, is read by nobody, and removes the pressure that would otherwise produce a real
topic document.

Where a document is warranted, determine the topic, the grouping it belongs under, and the filename —
all in the conventions established in Step 0. Then tell the user, briefly:

- Where the content will be placed, or that it is staying in the record and why
- Whether this is a new document or a merge
- Which index section it falls under, if the project keeps an index

---

## Step 3: Check the Evidence

Knowledge that cannot be re-checked is taken on trust, and the next reader researches it again from scratch. Establish where the claims come from before writing anything.

**If the input is a research record** — a document with Sources, Raw extracts and Findings, as produced by the `nomad-researcher` skill — the evidence is already assembled. Carry its Sources table into the References section of the target document (Step 4), keep the tiers, and continue.

**If the input carries no sources**, identify which claims are external fact rather than the project's own judgement, tell the user which of them are unsupported, and offer two ways forward:

1. **Add as-is** — the material is already trusted, or its claims are judgement and are recorded as such.
2. **Research first** — run the `nomad-researcher` skill over the open claims and return here with its record.

Do not research inline. Findings produced without a recorded source reproduce the problem this step exists to catch.

---

## Step 4: Create or Update the Document

Match the structure of the documents already in the base. Where the base is empty or inconsistent, the
following is a reasonable default:

```
# <emoji> <Topic Title> – <Descriptive Subtitle>

## Purpose of This Document
<2-4 sentences explaining what this document covers and who it helps.>

---

## 1. <First Major Section>

### 1.1 <Subsection>
<Content>

> **Key insight or principle as a blockquote callout.**

---

## 2. <Second Major Section>

<Use comparison tables where contrasting options:>

| Option A | Option B |
|----------|----------|
| Pro/con  | Pro/con  |

<Use rule statements for prescriptive guidance:>
✅ **Recommended practice**
❌ **Anti-pattern to avoid**

---

... (continue numbered sections as needed)

---

## <N>. Summary

1. **Key takeaway one**
2. **Key takeaway two**
3. ...

---

## References

| # | Source | Tier | Retrieved |
|---|--------|------|-----------|
| 1 | [<Title>](https://...) | primary | YYYY-MM-DD |
| 2 | [<Title>](https://...) | secondary | YYYY-MM-DD |
```

### Formatting rules:
- Choose a single relevant emoji for the main heading (📘 for guides, 🔧 for tools, 🧪 for testing, 🚀 for implementation, 📋 for process)
- Use `---` horizontal rules between major sections
- Use `>` blockquote callouts for key principles or important insights
- Use ✅/❌ for clear do/don't recommendations
- Use comparison tables when evaluating options or contrasting approaches
- Number all top-level sections (`## 1.`, `## 2.`, etc.)
- Number subsections hierarchically (`### 1.1`, `### 1.2`, etc.)
- End with a summary section containing numbered key takeaways
- Every external claim carries a numbered reference into the References table; claims that are the project's own judgement say so in the sentence rather than citing nothing
- Reference tiers are the ones `nomad-researcher` defines: **primary** (the thing itself), **live state** (the thing right now), **secondary** (someone describing it)
- Retrieved dates come from the research record, not from the day the document is written
- Keep content **practical over theoretical** and **opinionated** — make clear recommendations
- **Cross-reference** related documents rather than duplicating their content

### For EXISTING files:
- Read the existing file first
- Merge the new content into the appropriate section(s)
- Maintain the existing structure and numbering
- Do not duplicate information already present
- Add cross-references if the new content relates to other documents
- Merge new sources into the References table and renumber only if needed; where a new source supersedes an existing one on the same claim, replace it and keep the later retrieved date

---

## Step 5: Update the Index

If the project keeps an index (Step 0), add the document to it in the row format already in use. Match
the existing rows rather than introducing a format.

- Add a row to the matching section
- If a new section is needed, follow the shape of the existing ones
- Keep descriptions to one short sentence

If the project keeps no index, skip this step and say so — do not create one unasked.

---

## Step 6: Present Results

Summarize what was done:
- **File created/updated**: full path — or that the finding stayed in the record, and why
- **Placement**: where it went and on what grounds
- **Index updated**: what was added, or that the project keeps no index
- **Evidence**: how many references the document now carries, their tiers, and any claim left unsourced
- **Record**: the research record this came from, if there was one
- **Brief content summary**: 2-3 sentence overview of what the document covers
