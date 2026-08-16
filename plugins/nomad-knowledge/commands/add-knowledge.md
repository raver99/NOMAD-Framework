You are adding knowledge to the NOMAD knowledge base. NOMAD is a documentation project (not code) containing best practices and solutions for modern mobile application development.

Your input is: $ARGUMENTS

---

## Step 1: Determine Input Type

Determine whether the input above is:
- **A file path** (e.g., starts with `/`, `./`, `~`, or looks like a path ending in a file extension) — if so, read the file and use its contents as the source material.
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
   - **Claude Code** — Claude Code specific tools and extensions
   - A new top-level category may be created if none of the above fit. Use judgment.

3. **Directory**: Check the existing directories under `KnowledgeBase/` to see if an appropriate one already exists. Directory names use **PascalCase** (e.g., `Requirements`, `ClaudeCode`, `Solutions`).

4. **File**: Determine the target filename using **lowercase-with-hyphens** (e.g., `error-logging-strategy.md`). Check if a file on this topic already exists — if so, the content should be merged into the existing file rather than creating a duplicate. Remember: **one canonical source of truth per topic**.

Briefly tell the user:
- Where the content will be placed (directory + filename)
- Whether this is a new file or an update to an existing one
- Which README index category it falls under

---

## Step 3: Research and Validate

Before writing anything, assess the quality and completeness of the source material. Ask the user how they want to proceed by presenting these options:

1. **Add as-is** — Trust the input, format it to NOMAD conventions, and add it directly. Best when the source material is already well-researched and complete.
2. **Research & enhance** — Research the topic to fill gaps, add missing best practices, verify accuracy, and enrich the content with additional insights. The original input serves as the foundation.
3. **Deep research** — Thoroughly research the topic from scratch using the input as a starting point. Validate all claims, compare with current industry best practices, identify outdated information, and produce a comprehensive document.

If the user chooses option 2 or 3, perform the research using web searches and present your findings before writing:
- **Validated**: What from the input checks out
- **Gaps found**: Missing topics, best practices, or considerations
- **Outdated or inaccurate**: Anything that needs correction
- **Suggested additions**: New sections or content to include

Wait for user confirmation on the research findings before proceeding to write.

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
- Keep content **practical over theoretical**, **opinionated** (make clear recommendations), and **platform agnostic**
- Consider **AI-assisted development** as a first-class concern where relevant
- **Cross-reference** related NOMAD documents rather than duplicating their content (e.g., "See [Requirements Best Practices](../Requirements/requirements-best-practices.md)")

### For EXISTING files:
- Read the existing file first
- Merge the new content into the appropriate section(s)
- Maintain the existing structure and numbering
- Do not duplicate information already present
- Add cross-references if the new content relates to other documents

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
- **Research applied**: what was validated, enhanced, or added (if research was performed)
- **Brief content summary**: 2-3 sentence overview of what the document covers
