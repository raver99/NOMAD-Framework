You are adding knowledge to the NOMAD knowledge base. NOMAD is a documentation project (not code) containing best practices and solutions for modern mobile application development.

Your input is: $ARGUMENTS

---

## Step 1: Determine Input Type

Determine whether the input above is:
- **A file path** (e.g., starts with `/`, `./`, `~`, or looks like a path ending in a file extension) — if so, read the file and use its contents as the source material. A research record under `docs/research/` is the expected case.
- **Inline text** — if so, use the text directly as the source material.

If a file path is provided but the file does not exist or cannot be read, stop and tell the user.

---

## Step 2: Analyze Content and Determine Placement

Analyze the source material and determine:

1. **Topic**: What specific topic does this content address?
2. **Category**: Which top-level NOMAD framework category does it belong to? The current categories in the README index are:
   - **Process** — development process practices (requirements, planning, workflow)
   - **Implementation** — common mobile feature implementations (error logging, version management, etc.)
   - **Testing** — testing strategies for mobile apps
   - **Working with AI** — working with AI agents, domain agnostic (knowledge management, research, validation, tracking work)
   - **Claude Code** — Claude Code specific tools and extensions
   - A new top-level category may be created if none of the above fit. Use judgment.

3. **Directory**: Check the existing directories under `KnowledgeBase/` to see if an appropriate one already exists. Directory names use **PascalCase** (e.g., `Requirements`, `ClaudeCode`, `Solutions`).

4. **File**: Determine the target filename using **lowercase-with-hyphens** (e.g., `error-logging-strategy.md`). Check if a file on this topic already exists — if so, the content should be merged into the existing file rather than creating a duplicate. Remember: **one canonical source of truth per topic**.

Briefly tell the user:
- Where the content will be placed (directory + filename)
- Whether this is a new file or an update to an existing one
- Which README index category it falls under

---

## Step 3: Check the Evidence

Knowledge that cannot be re-checked is taken on trust, and the next reader researches it again from scratch. Establish where the claims come from before writing anything.

**If the input is a research record** — a document with Sources, Raw extracts and Findings, as produced by the `nomad-researcher` skill — the evidence is already assembled. Carry its Sources table into the References section of the target document (Step 4), keep the tiers, and continue.

**If the input carries no sources**, identify which claims are external fact rather than the project's own judgement, tell the user which of them are unsupported, and offer two ways forward:

1. **Add as-is** — the material is already trusted, or its claims are judgement and are recorded as such.
2. **Research first** — run the `nomad-researcher` skill over the open claims and return here with its record.

Do not research inline. Findings produced without a recorded source reproduce the problem this step exists to catch.

---

## Step 4: Create or Update the Knowledge Base File

### For NEW files, follow this structure:

```
# <emoji> <Topic Title> – <Descriptive Subtitle>

## Purpose of This Document
<2-4 sentences explaining what this document covers and who it helps. Mention relevance to mobile development, AI-assisted workflows, or cross-platform concerns where applicable.>

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
- Keep content **practical over theoretical**, **opinionated** (make clear recommendations), and **platform agnostic**
- Consider **AI-assisted development** as a first-class concern where relevant
- **Cross-reference** related NOMAD documents rather than duplicating their content (e.g., "See [Requirements Best Practices](../Requirements/requirements-best-practices.md)")

### For EXISTING files:
- Read the existing file first
- Merge the new content into the appropriate section(s)
- Maintain the existing structure and numbering
- Do not duplicate information already present
- Add cross-references if the new content relates to other documents
- Merge new sources into the References table and renumber only if needed; where a new source supersedes an existing one on the same claim, replace it and keep the later retrieved date

---

## Step 5: Update the README Index

Open `README.md` and add the new topic to the appropriate table in the Framework Index section (between the `# Framework` heading and the `# Licence` heading).

The index uses tables per category with this format:

```
### <Category Name>

| Topic | Description | Guide |
|-------|-------------|-------|
| <Topic name> | <Short description> | [View](<relative path to file>) |
```

- Add a new row to the matching category table
- If a new category is needed, add a new `### <Category>` heading with a fresh table following the same format
- Keep descriptions concise (one short sentence)

---

## Step 6: Present Results

Summarize what was done:
- **File created/updated**: full path
- **Category**: where it was placed and why
- **README updated**: what was added to the index
- **Evidence**: how many references the document now carries, their tiers, and any claim left unsourced
- **Record**: the research record this came from, if there was one
- **Brief content summary**: 2-3 sentence overview of what the document covers
