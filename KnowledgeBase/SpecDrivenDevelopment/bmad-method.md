# 📐 BMAD-METHOD – Spec-Driven Development Candidate Profile

## Purpose of This Document
This is a candidate profile for **BMAD-METHOD**, evaluated as a [spec-driven development framework](overview.md) for NOMAD. It documents the framework's architecture, core concepts, and workflow patterns from a study of the [BMAD-METHOD repository](https://github.com/bmad-code-org/BMAD-METHOD). The intent is to capture *why and how it works* so its best patterns can inform NOMAD's recommended approach — whether or not BMAD is adopted wholesale.

> **The key insight: every capability is a plain Markdown file with structured instructions for the LLM. There is no runtime engine — the LLM *is* the engine, and the Markdown files are its program.**

> **Naming note:** BMAD's "skills" are framework-internal Markdown units and are distinct from [Claude Code Skills](../ClaudeCode/claude-code-skills.md). The concepts rhyme but the mechanisms differ.

---

## 1. What BMAD-METHOD Is

An **npm-installable AI development framework** (`npx bmad-method install`) that installs a `_bmad/` directory into a project. It turns an AI IDE (Claude Code, Cursor, etc.) into a structured agile team of specialist agents that guide development through the full software lifecycle — from brainstorming and product requirements all the way to code review and retrospectives.

---

## 2. Repository Structure

```
src/
  bmm-skills/           ← lifecycle-phase skills
    1-analysis/
    2-plan-workflows/
    3-solutioning/
    4-implementation/
    module-help.csv     ← phase/sequencing catalog
    module.yaml         ← module config + agent roster
  core-skills/          ← cross-cutting skills (help, spec, brainstorm, etc.)
  scripts/
    resolve_customization.py   ← three-layer TOML merge
    resolve_config.py
bmad-modules.yaml       ← official module registry
```

Each skill is a directory:

```
bmad-agent-dev/
  SKILL.md              ← LLM instructions
  customize.toml        ← configurable defaults
  steps/                ← optional: one file per workflow step
    step-01-gather-context.md
    step-02-review.md
    ...
```

---

## 3. Core Concept: The Skill

A **skill** is the fundamental unit. Every capability — whether an agent persona or a multi-step workflow — is packaged as a skill directory containing `SKILL.md` and `customize.toml`.

### 3.1 SKILL.md

Two parts:

1. **YAML frontmatter** — metadata used by the skill catalog:
   ```yaml
   ---
   name: bmad-agent-dev
   description: 'Senior software engineer for story execution. Use when the user asks to talk to Amelia.'
   ---
   ```
2. **Body** — instructions for the LLM, in natural language with optional XML-like structure (see §5).

### 3.2 customize.toml

Defines the skill's configurable surface. Two namespaces — `[agent]` for persona skills, `[workflow]` for workflow skills — share the same fields:

```toml
[agent]   # or [workflow]

icon = "💻"

activation_steps_prepend = []   # run before standard activation
activation_steps_append = []    # run after greeting, before menu

persistent_facts = [
  "file:{project-root}/**/project-context.md",  # loaded as LLM context
  "Our org uses AWS only — do not propose GCP.", # literal fact
]

role = "Implement approved stories with test-first discipline."
identity = "Disciplined in Kent Beck's TDD."
communication_style = "Ultra-succinct. Speaks in file paths and AC IDs."

principles = [
  "No task complete without passing tests.",
  "Red, green, refactor — in that order.",
]

on_complete = ""   # terminal instruction when workflow finishes

[[agent.menu]]     # or [[workflow.menu]]
code = "DS"
description = "Write the next story's tests and code"
skill = "bmad-dev-story"
```

---

## 4. Three-Layer Customization

Every skill's `customize.toml` is the base layer. Two override layers sit above it:

```
{skill-root}/customize.toml                    ← shipped defaults (DO NOT EDIT)
{project-root}/_bmad/custom/{name}.toml         ← team overrides (committed to repo)
{project-root}/_bmad/custom/{name}.user.toml    ← personal overrides (gitignored)
```

A Python script (`_bmad/scripts/resolve_customization.py`) merges the layers at runtime and outputs JSON. The LLM calls it on activation:

```
python3 {project-root}/_bmad/scripts/resolve_customization.py --skill {skill-root} --key agent
```

### 4.1 Merge Rules (purely structural, no field-name special-casing)

| Type | Rule |
| :--- | :--- |
| Scalars (string, int, bool, float) | Override wins |
| Tables | Deep merge (recursive) |
| Arrays-of-tables where every item has `code` **OR** every item has `id` | Keyed merge: matching keys replace, new keys append |
| All other arrays | Append (base items first, then override items) |

> **There is no removal mechanism.** Overrides cannot delete base items. To suppress a default, fork the skill or override the item by code with a no-op.

### 4.2 Fallback When the Script Fails

If the Python script is unavailable, the `SKILL.md` instructs the LLM to read the three TOML files itself and apply the same merge rules manually. There is no hard dependency on the toolchain.

---

## 5. Agent Skills

Agent skills adopt a named persona for the session. All agent `SKILL.md` files follow the same eight-step activation protocol:

1. **Resolve agent block** — run the Python resolver for the `[agent]` key
2. **Execute prepend steps** — run `{agent.activation_steps_prepend}` in order
3. **Adopt persona** — take on the name, role, identity, communication style, and principles
4. **Load persistent facts** — treat each entry as foundational context; `file:`-prefixed entries are loaded from disk (glob supported)
5. **Load config** — read `_bmad/bmm/config.yaml` for `user_name`, `communication_language`, `document_output_language`, artifact paths
6. **Greet the user** — by name, in `{communication_language}`, prefixed with `{agent.icon}`
7. **Execute append steps** — run `{agent.activation_steps_append}` in order
8. **Dispatch or present menu** — if intent is clear from the initial message, dispatch directly; otherwise render the menu as a numbered table and wait

Once active, the agent icon prefix (`💻`, `📋`, `🏗️`, etc.) is used on every response so the user can see which persona is speaking.

### 5.1 The Agent Roster (bmm module)

| Code | Name | Title | Icon |
| :--- | :--- | :--- | :--- |
| bmad-agent-analyst | Mary | Business Analyst | 📊 |
| bmad-agent-tech-writer | Paige | Technical Writer | 📚 |
| bmad-agent-pm | John | Product Manager | 📋 |
| bmad-agent-ux-designer | Sally | UX Designer | 🎨 |
| bmad-agent-architect | Winston | System Architect | 🏗️ |
| bmad-agent-dev | Amelia | Senior Software Engineer | 💻 |

---

## 6. Workflow Skills

Workflow skills execute a structured, multi-step process. They do not adopt a persona — the LLM acts as a facilitator. Workflow `SKILL.md` files begin with the same boot protocol as agents (steps 1–6), but instead of presenting a menu they immediately start executing workflow steps.

### 6.1 Workflow Style A — Inline XML DSL

The entire workflow lives in one `SKILL.md`, inside a `<workflow>` block. Used by shorter, linear workflows like `bmad-dev-story`.

```xml
<workflow>
  <critical>Execute ALL steps in exact order; do NOT skip steps</critical>

  <step n="1" goal="Find next ready story" tag="sprint-status">
    <check if="{{sprint_status}} file exists">
      <action>Load the FULL file: {{sprint_status}}</action>
      <action>Find first story with status "ready-for-dev"</action>

      <check if="no ready-for-dev story found">
        <output>No ready-for-dev stories found. What would you like to do?</output>
        <ask>Choose option [1], [2], or [3]:</ask>

        <check if="user chooses '1'">
          <action>HALT - Run create-story</action>
        </check>
      </check>
    </check>

    <anchor id="task_check" />
    <action if="story file inaccessible">HALT: "Cannot develop story without access"</action>
  </step>

  <step n="5" goal="Implement task (red-green-refactor)">
    <action>Write FAILING tests first for the task functionality</action>
    <action>Implement MINIMAL code to make tests pass</action>
    <action>Improve code structure while keeping tests green</action>
    <action if="3 consecutive failures">HALT and request guidance</action>
  </step>

  <step n="8" goal="Validate and mark task complete">
    <action>Verify ALL tests ACTUALLY EXIST and PASS 100%</action>
    <action if="more tasks remain">
      <goto step="5">Next task</goto>
    </action>
    <action if="no tasks remain">
      <goto step="9">Completion</goto>
    </action>
  </step>
</workflow>
```

**XML tags used:**

| Tag | Purpose |
| :--- | :--- |
| `<step n="N" goal="…" tag="…">` | Numbered step with optional tag for filtering |
| `<check if="…">` | Conditional branch |
| `<action>` | Imperative instruction |
| `<action if="…">` | Conditional imperative |
| `<critical>` | Rule that must never be violated |
| `<output>` | Text to emit to the user |
| `<ask>` | Halt and prompt for user input |
| `<anchor id="…">` | Jump target |
| `<goto step="N">` | Jump to step N |
| `<goto anchor="id">` | Jump to named anchor |

`<goto>` + `<anchor>` implement loops. The dev-story workflow loops from step 8 back to step 5 for each task until all tasks are complete.

### 6.2 Workflow Style B — Step-File Architecture

The workflow is split across multiple Markdown files, one per step. The main `SKILL.md` only boots and kicks off step 1. Used by longer, more complex workflows like `bmad-code-review`, `bmad-create-architecture`, `bmad-quick-dev`.

```
SKILL.md                             ← boot + "read ./steps/step-01.md"
steps/
  step-01-gather-context.md
  step-02-review.md
  step-03-triage.md
  step-04-present.md
```

Each step file ends with a `## NEXT` section:

```markdown
## NEXT
Read fully and follow `./step-02-review.md`
```

The `SKILL.md` documents the rationale explicitly:

> **Just-In-Time Loading**: Only load the current step file.
> **NEVER** load multiple step files simultaneously.

**Why:** complex workflows would overflow the LLM context if loaded all at once. Loading one step file at a time keeps the active context lean.

Each step file has YAML frontmatter declaring its runtime state variables:

```yaml
---
diff_output: ''       # set at runtime
spec_file: ''         # set at runtime (path or empty)
review_mode: ''       # set at runtime: "full" or "no-spec"
story_key: ''         # set at runtime when discovered
---
```

This is **documentation-as-contract** — it tells the LLM exactly what variables to track in memory for this step.

---

## 7. Key Workflow Patterns

### 7.1 HALT vs CHECKPOINT

Two distinct stop mechanisms:

| | HALT | CHECKPOINT |
| :--- | :--- | :--- |
| When | Something is blocking or ambiguous | Natural pause between phases |
| Tone | Error / cannot proceed | Summary + confirmation |
| Resume | User must resolve the blocking issue | User just confirms to continue |
| Example | "3 consecutive test failures" | "Here are the diff stats. Proceed?" |

Checkpoint example from `step-01-gather-context.md`:

```markdown
### CHECKPOINT
Present a summary: diff stats (files changed, lines added/removed), review_mode,
and loaded spec/context docs (if any). HALT and wait for user confirmation to proceed.
```

### 7.2 Tiered Auto-Discovery

Before asking the user anything, step-1 files use a waterfall of inference tiers:

```
Tier 1 — Was it passed explicitly as an argument?     → use it directly
Tier 2 — Is it clear from recent conversation?        → use it
Tier 3 — Can we infer from sprint status/artifacts?   → suggest and confirm
Tier 4 — Can we infer from current git state?         → confirm with user
Tier 5 — Ask directly
```

> **Rule: never ask a question you could answer yourself.** The cascade short-circuits as soon as any tier resolves.

### 7.3 EARLY EXIT Routing

In step-file workflows, `EARLY EXIT` is a `goto` for step files. Used when artifact state determines which phase to resume at:

```markdown
If spec status is "draft":          → EARLY EXIT to step-02-plan.md
If spec status is "ready-for-dev":  → EARLY EXIT to step-03-implement.md
If spec status is "in-review":      → EARLY EXIT to step-04-review.md
```

The LLM checks the artifact's `status` frontmatter and jumps directly to the appropriate phase, skipping phases that are already complete.

### 7.4 Parallel Sub-agents

Complex workflows (like code review) spawn parallel sub-agents for independent tasks:

```markdown
Launch parallel subagents without conversation context:
- Blind Hunter — diff only. Invoked via bmad-review-adversarial-general skill.
- Edge Case Hunter — diff + project read access. Invoked via bmad-review-edge-case-hunter skill.
- Acceptance Auditor — diff + spec + context docs.

If subagents are not available:
  Generate prompt files in {implementation_artifacts} — one per role.
  HALT. Ask user to run each in a separate session and paste back findings.
```

> **Graceful degradation:** if the runtime doesn't support sub-agents, the workflow falls back to human-relayed prompts.

### 7.5 The `on_complete` Hook

Every workflow `customize.toml` has an `on_complete` scalar. If non-empty, the last step executes it as a terminal instruction:

```toml
on_complete = "Run the sprint status check and present the updated board."
```

This is how teams wire workflows together — e.g. the PRD workflow can `on_complete` into suggesting architecture next.

---

## 8. The Lifecycle Phases

Skills are organized into four phases, tracked in `module-help.csv`:

| Phase | Skills (examples) |
| :--- | :--- |
| 1 — Analysis | Brainstorm, Market Research, Domain Research, Product Brief, PRFAQ |
| 2 — Planning | PRD (required), UX Design |
| 3 — Solutioning | Architecture (required), Create Epics & Stories (required), Implementation Readiness Check |
| 4 — Implementation | Sprint Planning (required) → Create Story → Dev Story → Code Review → Retrospective |

`required=true` in the CSV means the skill must complete before the user can meaningfully proceed to later phases. Optional skills are recommended but not gating.

---

## 9. The CSV Skill Catalog

`module-help.csv` is the single navigation map. The `bmad-help` skill reads it to orient users.

```
module,skill,display-name,menu-code,description,action,args,phase,
preceded-by,followed-by,required,output-location,outputs
```

Example rows:

```
BMad Method,bmad-prd,Create/Edit/Review PRD,PRD,...,2-planning,bmad-product-brief,,true,planning_artifacts,prd
BMad Method,bmad-dev-story,Dev Story,DS,...,4-implementation,bmad-create-story:validate,,true,,
BMad Method,bmad-code-review,Code Review,CR,...,4-implementation,bmad-dev-story,,false,,
```

- `preceded-by` / `followed-by` — soft sequencing hints (not hard gates unless `required=true`)
- `action` — for skills with multiple entry points (e.g. `create`, `validate`, `update`)
- `output-location` — where the skill writes artifacts (resolves against config paths)
- `_meta` rows carry a URL to the module's documentation (e.g. `llms.txt`) that `bmad-help` fetches

---

## 10. Project Config

Installed at `{project-root}/_bmad/bmm/config.yaml`. Read by every skill on activation.

```yaml
user_name: Roland
project_name: MyProject
communication_language: English
document_output_language: English
user_skill_level: expert          # beginner | intermediate | expert
planning_artifacts: docs/planning-artifacts
implementation_artifacts: docs/implementation-artifacts
project_knowledge: docs
```

`user_skill_level` affects how agents explain concepts in chat — it does not change code or artifact output.

---

## 11. The `project-context.md` Pattern

Every agent and workflow has this in `persistent_facts`:

```toml
persistent_facts = [
  "file:{project-root}/**/project-context.md",
]
```

This file is a lean, LLM-optimized summary of the project — architecture, conventions, key decisions. It is automatically loaded as foundational context by every skill. The `bmad-generate-project-context` skill produces it by scanning the codebase.

> **It is the primary mechanism for giving every agent consistent project knowledge without duplicating information everywhere** — the same single-source-of-truth principle NOMAD applies to its own documentation.

---

## 12. The Module System

BMAD is extensible via modules. Each module:

- Has a `module.yaml` defining its config variables, agent roster, and directory structure
- Registers in `bmad-modules.yaml` with an npm package name, GitHub URL, and module code
- Installs its skills under `_bmad/{module-code}/`

Official modules:

| Code | Name | Purpose |
| :--- | :--- | :--- |
| bmm | BMad Method | Core agile lifecycle (34+ workflows) |
| bmb | BMad Builder | Build custom agents and workflows |
| tea | Test Architect | Risk-based test strategy and automation |
| gds | Game Dev Studio | Game development workflows |
| cis | Creative Intelligence Suite | Brainstorming, design thinking |

---

## 13. Skill Deprecation / Forwarding Pattern

When a skill is consolidated into another, the old skill becomes a thin shim:

```markdown
# DEPRECATED — forwards to bmad-prd (create intent)

## On Activation
1. Resolve legacy customization
2. Emit a deprecation notice in {communication_language}
3. Invoke bmad-prd with create intent and forward pre-resolved customization
   bmad-prd takes the workflow from here. Do not execute further steps.
```

This preserves backward compatibility for teams with `_bmad/custom/old-name.toml` override files, while directing new work to the consolidated skill.

---

## 14. Path Resolution Conventions

Every `SKILL.md` documents these conventions at the top:

```markdown
## Conventions
- Bare paths (e.g. `steps/step-01.md`) resolve from the skill root
- {skill-root}   = this skill's installed directory (where customize.toml lives)
- {project-root} = the working directory (where _bmad/ lives)
- {skill-name}   = basename of the skill directory
```

Template variables use `{single_braces}` for config/context values and `{{double_braces}}` for runtime variables set during execution.

---

## 15. Summary: Why It Works

The entire system is instructions to an LLM in Markdown, structured to enforce procedural discipline:

1. **One step at a time** — prevents context overflow and LLM drift
2. **Explicit state variables in frontmatter** — the LLM knows exactly what to track
3. **HALT for blockers, CHECKPOINT for milestones** — humans stay in the loop at the right moments
4. **Tiered auto-discovery** — minimizes unnecessary questions
5. **Three-layer TOML customization** — shipped defaults, team overrides, personal overrides; no fork needed for most customizations
6. **Graceful degradation** — every step has a fallback when tools or sub-agents are unavailable
7. **`on_complete` hooks** — workflows chain declaratively without hardcoded coupling
8. **CSV catalog** — a single navigation map decoupled from the skills themselves
9. **`project-context.md`** — one file gives every agent consistent project knowledge

> **Relevance to NOMAD:** BMAD demonstrates that a disciplined, fully-Markdown spec-driven process can run inside existing AI IDEs with no custom runtime — directly serving NOMAD's principles of *not reinventing the wheel* and *AI-assisted development at every stage*. See the [evaluation hub](overview.md) for how it stacks up against other candidates.
</content>
