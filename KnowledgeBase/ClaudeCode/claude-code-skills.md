# 🔧 Claude Code Skills – Creating, Organizing, and Scaling a Skill Library

## Purpose of This Document
This document explains how to build, organize, and scale **skills** in Claude Code — the reusable Markdown units that extend what the AI agent can do. It covers the skill structure and full frontmatter, how the discovery and description-budget mechanism works, and how to keep auto-activation reliable as your skill library grows. Because NOMAD treats AI-assisted development as a first-class concern, skills are the primary mechanism for encoding repeatable mobile workflows (build/release recipes, requirements consumption, review checklists) so they execute consistently across projects and platforms.

> **A skill turns a repeated instruction into a callable capability. Use one when you keep pasting the same procedure into chat, or when a section of `CLAUDE.md` has grown into a workflow rather than a fact.**

This document covers the **mechanism** — how skills are structured, discovered and scaled. The
**rules NOMAD authors by**, and the testing practice behind them, are in
[Skill Authoring Rules](skill-authoring-rules.md), which the `nomad-skill-creator` and
`nomad-skill-validator` skills both read.

---

## 1. What Skills Are

A skill is a directory containing a `SKILL.md` file with YAML frontmatter plus Markdown instructions. Claude either loads the skill **automatically** when your request matches its description, or you invoke it **directly** with `/skill-name`.

Skills follow the open **[Agent Skills standard](https://agentskills.io)**, which works across multiple AI tools; Claude Code extends it with invocation control, subagent execution, and dynamic context injection.

### 1.1 Why Skills Instead of CLAUDE.md

`CLAUDE.md` content loads **every session** whether you need it or not. A skill's *body* loads **only when invoked**, so long reference material, workflows, and checklists cost almost nothing until you actually use them. Only the short skill *description* is always in context.

> **Rule of thumb:** facts that should always apply → `CLAUDE.md`. Procedures, checklists, and reference material invoked on demand → a skill.

### 1.2 Commands Are Now Skills

Custom slash commands have been merged into skills. A file at `.claude/commands/deploy.md` and a skill at `.claude/skills/deploy/SKILL.md` both create `/deploy` and behave the same way. Existing `.claude/commands/` files keep working; skills simply add optional features (a directory for supporting files, frontmatter for invocation control, and automatic loading). If a command and a skill share a name, the skill wins.

---

## 2. Where Skills Live

Where you store a skill determines who can use it.

| Scope      | Path                                          | Applies to                     |
| :--------- | :-------------------------------------------- | :----------------------------- |
| Enterprise | Managed settings                              | All users in your organization |
| Personal   | `~/.claude/skills/<skill-name>/SKILL.md`      | All your projects              |
| Project    | `.claude/skills/<skill-name>/SKILL.md`        | This project only              |
| Plugin     | `<plugin>/skills/<skill-name>/SKILL.md`       | Where the plugin is enabled    |

When names conflict across levels, **enterprise overrides personal, and personal overrides project**. Plugin skills use a `plugin-name:skill-name` namespace, so they cannot collide with the other levels.

✅ **`~/.claude/skills/`** → genuinely universal tools (git workflows, commit formatting, review style).
✅ **`.claude/skills/` (committed)** → project- or platform-specific patterns (architecture conventions, deploy targets, domain knowledge).
❌ **Don't put project-specific skills in `~/.claude/skills/`** — every project you open then pays the discovery cost for skills it will never use.

### 2.1 Discovery Details

- **Parent + nested discovery:** project skills load from `.claude/skills/` in your starting directory and every parent up to the repo root. When you touch files in a subdirectory (e.g. `packages/frontend/`), skills in that subdirectory's `.claude/skills/` are also discovered — useful for **monorepos**.
- **Additional directories:** `.claude/skills/` inside an `--add-dir` / `/add-dir` directory is loaded automatically (an exception to the usual "file access only" rule). The `permissions.additionalDirectories` *setting* does not load skills.
- **Live change detection:** adding, editing, or removing a `SKILL.md` under a watched directory takes effect **within the current session**. Creating a brand-new top-level skills directory requires a restart so it can be watched.

---

## 3. Skill Structure

```
my-skill/
├── SKILL.md           # Required — frontmatter + instructions (the entrypoint)
├── reference.md       # Optional — detailed docs loaded only when needed
├── examples/
│   └── sample.md      # Optional — example output showing expected format
└── scripts/
    └── helper.py      # Optional — script Claude executes (not loaded into context)
```

Only `SKILL.md` is required. Reference the other files *from* `SKILL.md` so Claude knows what each contains and when to load it.

> **Keep `SKILL.md` under ~500 lines.** Push large reference docs, API specs, and example collections into supporting files so they load on demand instead of every run. Once a skill loads, its body stays in context across turns — every line is a recurring token cost.

---

## 4. Frontmatter Reference

Frontmatter sits between `---` markers at the top of `SKILL.md`. **All fields are optional; only `description` is recommended** so Claude knows when to use the skill.

```yaml
---
name: my-skill                     # Display label (defaults to directory name)
description: What it does AND when to use it
when_to_use: Extra trigger phrases / example requests
disable-model-invocation: true     # Manual-only: only you can invoke it
user-invocable: false              # Hidden from / menu: only Claude can invoke it
allowed-tools: Read Grep Bash      # PRE-APPROVE these tools (does NOT restrict)
context: fork                      # Run in an isolated subagent context
agent: Explore                     # Which subagent type when context: fork
model: inherit                     # Model override while the skill is active
paths: "src/**/*.ts"               # Auto-load only when working on matching files
---

Your skill instructions here…
```

### 4.1 Key Fields

| Field                      | What it does |
| :------------------------- | :----------- |
| `description`              | The trigger text Claude matches against your prompt. Combined `description` + `when_to_use` is **capped at 1,536 characters** in the listing — put the key use case first. |
| `when_to_use`              | Extra trigger context appended to `description`; counts toward the 1,536-char cap. |
| `disable-model-invocation` | `true` → only **you** can invoke (via `/name`). Removes the description from context entirely. Use for side-effecting workflows (`/commit`, `/deploy`). |
| `user-invocable`           | `false` → only **Claude** can invoke; hidden from the `/` menu. Use for background knowledge that isn't a meaningful user command. |
| `allowed-tools`            | **Pre-approves** the listed tools (no permission prompt) while active. **It does not restrict** the available toolset. |
| `disallowed-tools`         | Removes tools from the pool while active — this is how you actually *restrict* (e.g. block `AskUserQuestion` in an autonomous loop). |
| `context` / `agent`        | `context: fork` runs the skill as an isolated subagent; `agent` picks the subagent type (`Explore`, `Plan`, `general-purpose`, or a custom one). |
| `model` / `effort`         | Override the model / effort level for the duration of the skill's turn. |
| `paths`                    | Glob patterns; Claude auto-loads the skill only when working with matching files. |
| `argument-hint` / `arguments` | Autocomplete hint, and named positional arguments for `$name` substitution. |

> **The single most common mistake:** treating `allowed-tools` as a sandbox. It is an *allow-list for skipping prompts*, not a restriction. To deny tools, use `disallowed-tools` or deny rules in `/permissions`.

### 4.2 Who Can Invoke — at a Glance

| Frontmatter                      | You invoke | Claude invokes | Description in context? |
| :------------------------------- | :--------- | :------------- | :---------------------- |
| (default)                        | ✅          | ✅              | Yes                     |
| `disable-model-invocation: true` | ✅          | ❌              | No (frees budget)       |
| `user-invocable: false`          | ❌          | ✅              | Yes                     |

---

## 5. How Discovery and the Description Budget Work

At session start, Claude loads every skill **description** (not the body) into context so it knows what's available. Bodies load only on invocation. This two-phase design lets you install many skills with minimal upfront cost.

Discovery is **language-model-based**: Claude matches your request against descriptions through normal reasoning — there are no embeddings or classifiers. **Description quality is therefore everything.**

### 5.1 The Budget

- The total space for all descriptions scales at roughly **1% of the model's context window** (~2,000 tokens on a 200K model).
- Each individual entry (`description` + `when_to_use`) is capped at **1,536 characters** by Claude Code (`maxSkillDescriptionChars`). Note this is a *different limit from a different layer* than the portable Agent Skills spec, which caps `description` at **1,024** — a skill within Claude Code's cap can still fail spec validation.

When the budget overflows, **all skill *names* are always kept**, but descriptions for the skills you invoke **least** are dropped first — so the skills you actually use keep their full text. A truncated description can strip the very keywords Claude needs to match your request.

> **Practical ceiling:** with 200–400-char descriptions, trimming typically begins around **15–25 skills**. With tight 100–150-char descriptions, 50+ fit comfortably.

### 5.2 Diagnosing and Raising the Budget

- Run **`/doctor`** to see whether the budget is overflowing and which skills are affected. (`/context` also shows a `Skills:` usage line.)
- Raise it via the **`skillListingBudgetFraction`** setting (e.g. `0.02` = 2%) or the **`SLASH_COMMAND_TOOL_CHAR_BUDGET`** environment variable (a fixed character count):

```bash
SLASH_COMMAND_TOOL_CHAR_BUDGET=20000 claude
```

- The 1,536-char per-entry cap is itself configurable via **`maxSkillDescriptionChars`**.
- To free budget without deleting skills, set low-priority entries to `"name-only"` in `skillOverrides` (see §7.2).

---

## 6. Keeping Auto-Activation Sharp at Scale

### 6.1 Front-Load Trigger Keywords

Descriptions are trimmed from the end when over budget, and the model only matches what it can see. Put the use case and the words a user would naturally say **in the first sentence**.

```yaml
# ❌ Critical trigger buried at the end
description: >
  Comprehensive guidance on deployment workflows, environment
  configuration, rollback procedures, and production safety checks.
  Use when deploying to production.

# ✅ Trigger keywords first
description: >
  Deploy to production. Use when running deployments, releases,
  or pushing to staging/prod environments.
```

### 6.2 Be Specific and Directive (Community Pattern)

Official guidance: make descriptions **specific** and include keywords users would naturally say. Beyond that, a widely used community pattern pairs a **positive directive** with a **negative constraint** to push reliability higher:

```yaml
# Vague
description: Use when reviewing pull requests or checking code quality.

# Specific + directive
description: >
  ALWAYS invoke when reviewing PRs, diffs, or code quality.
  Do not attempt code review directly — use this skill first.
```

> The positive directive alone still lets Claude bypass the skill for tasks it deems "simple"; the negative constraint is what closes that gap. This is an empirical heuristic, not documented behavior — measure it on your own skills.

If a skill triggers **too often**, do the inverse: make the description narrower, or add `disable-model-invocation: true` to make it manual-only.

### 6.3 Take Manual-Only Skills Out of the Budget

Skills you always trigger yourself — deploys, migrations, DB operations — don't need to participate in auto-discovery. `disable-model-invocation: true` removes them from the description budget entirely while still letting you run `/skill-name`.

### 6.4 Keep Descriptions Lean

NOMAD's ceiling is **300 characters** for model-invocable skills — enough to enumerate trigger cases explicitly (Claude tends to *under*-trigger), while still fitting roughly 25 skills before trimming. It is a ceiling, not a target. See [Skill Authoring Rules §5](skill-authoring-rules.md) for the reasoning and the exemption for `disable-model-invocation` skills. A description is for **routing**, not documentation — the full instructions live in the body. Quick audit for bloat:

```bash
find ~/.claude/skills .claude/skills -name "SKILL.md" -exec sh -c \
  'echo "$(wc -c < "$1") chars: $1"' _ {} \; | sort -rn | head -20
```

### 6.5 Reference Critical Skills in CLAUDE.md

For workflow-critical skills, name them in `CLAUDE.md` as routing hints so Claude reaches for them even if auto-discovery falters:

```markdown
# Workflows
- For all PR reviews, use `/code-review`
- For production deployments, use `/deploy`
- For database migrations, use `/db-migrate`
```

> **Direct `/skill-name` invocation bypasses description matching entirely** — it works even for skills dropped from the listing due to budget limits.

---

## 7. Controlling and Overriding Skill Access

### 7.1 Restrict What Claude Can Invoke

Use permission rules (`/permissions`) to gate the `Skill` tool:

```text
Skill                 # Deny rule: disables ALL skills
Skill(commit)         # Allow only this exact skill
Skill(review-pr *)    # Allow with any arguments (prefix match)
Skill(deploy *)       # Deny a specific skill
```

### 7.2 Override Visibility from Settings (`skillOverrides`)

When you can't (or don't want to) edit a skill's frontmatter — e.g. a shared repo skill or an MCP-provided one — control visibility from `.claude/settings.local.json`. The `/skills` menu writes it for you (Space to cycle, Enter to save).

| Value                   | Listed to Claude     | In `/` menu |
| :---------------------- | :------------------- | :---------- |
| `"on"` (default)        | Name + description   | Yes         |
| `"name-only"`           | Name only            | Yes         |
| `"user-invocable-only"` | Hidden               | Yes         |
| `"off"`                 | Hidden               | Hidden      |

---

## 8. Skill Content Lifecycle

Once invoked, a skill's rendered content enters the conversation as a **single message** and stays for the rest of the session. Claude does **not** re-read the file on later turns — write standing instructions, not one-time steps.

### 8.1 After Auto-Compaction

When a long session is summarized to free context, Claude Code re-attaches the **most recent invocation** of each skill, keeping its first **5,000 tokens**. Re-attached skills share a combined **25,000-token** budget, filled from the most recently invoked skill backward — so older skills can be dropped entirely if you invoked many in one session.

> **If a skill seems to stop influencing behavior, the content is usually still present** and the model is simply choosing other approaches. Strengthen the description and instructions, enforce behavior with [hooks](https://code.claude.com/docs/en/hooks), or re-invoke the skill with `/skill-name` to restore its full content after compaction.

---

## 9. Advanced Patterns

### 9.1 Dynamic Context Injection

The `` !`<command>` `` syntax runs a shell command **before** the skill reaches Claude; the output replaces the placeholder. Claude receives real data, never the command itself.

```yaml
---
name: summarize-changes
description: Summarize uncommitted changes and flag risks. Use when asked what changed or for a commit message.
---

## Current changes
!`git diff HEAD`

## Instructions
Summarize the changes above in 2–3 bullets, then list risks (missing error handling, hardcoded values, tests to update).
```

The `!` form is only recognized at the start of a line or after whitespace. For multi-line commands use a fenced `` ```! `` block. Disable globally with `"disableSkillShellExecution": true` in settings (most useful in managed settings).

### 9.2 Arguments and Substitutions

| Variable               | Expands to |
| :--------------------- | :--------- |
| `$ARGUMENTS`           | All arguments as typed |
| `$ARGUMENTS[N]` / `$N` | The Nth argument (0-based) |
| `$name`                | A named argument declared in the `arguments` frontmatter list |
| `${CLAUDE_SKILL_DIR}`  | Directory containing the skill — use to reference bundled scripts |
| `${CLAUDE_SESSION_ID}` | Current session ID (logging, session-specific files) |
| `${CLAUDE_EFFORT}`     | Active effort level (`low`…`max`) |

```yaml
---
name: migrate-component
description: Migrate a component from one framework to another
---

Migrate the $0 component from $1 to $2. Preserve all behavior and tests.
```

`/migrate-component SearchBar React Vue` → `$0`=SearchBar, `$1`=React, `$2`=Vue.

### 9.3 Run a Skill in a Subagent (`context: fork`)

`context: fork` runs the skill in an isolated context with no access to your conversation history; the skill body becomes the subagent's prompt. Pair it with `agent:` to choose the execution environment.

```yaml
---
name: pr-summary
description: Summarize changes in a pull request
context: fork
agent: Explore
allowed-tools: Bash(gh *)
---

## Pull request context
- PR diff: !`gh pr diff`
- Changed files: !`gh pr diff --name-only`

## Your task
Summarize this pull request…
```

> `context: fork` only makes sense for skills with an explicit **task**. A pure-guidelines skill ("use these conventions") gives the subagent no actionable prompt and returns nothing useful.

### 9.4 Bundled Skills

Claude Code ships prompt-based bundled skills you invoke like any other — e.g. `/code-review`, `/run`, `/verify`, `/loop`, `/claude-api`. Unlike fixed built-in commands, these instruct Claude and let it orchestrate the work with its tools.

---

## 10. Skills in an AI-Assisted Mobile Workflow

Skills are how NOMAD's principle of *not reinventing the wheel* shows up inside the agent. Encode the repeatable, cross-platform parts of mobile delivery once:

- **Release & build recipes** → a project skill (`.claude/skills/`) capturing the exact install/build/launch/deploy steps, so every agent in the repo follows the recorded recipe instead of rediscovering it. Cross-reference [CI/CD Pipeline Strategies](../DevOps/pipeline-structuring-strategies.md).
- **Requirements consumption** → a skill that loads your feature-based requirements format and acceptance-criteria checklist on demand. See [Requirements Best Practices](../Requirements/requirements-best-practices.md).
- **Review & quality gates** → a manual-only (`disable-model-invocation: true`) skill that runs your review checklist before a PR.
- **Side-effecting operations** (store submission, signing, migrations) → always `disable-model-invocation: true`, with `allowed-tools` pre-approving only the specific commands they need.

> **Commit project skills to version control.** A skill checked into `.claude/skills/` is shared context for the whole team and every agent that opens the repo — the same "one canonical source of truth" principle NOMAD applies to documentation.

---

## 11. Quick Reference — Troubleshooting

| Symptom | Likely cause | Fix |
| :--- | :--- | :--- |
| Skill never auto-activates | Vague description / buried keywords | Make it specific; move trigger keywords to the first sentence; try the directive + constraint pattern (§6.2) |
| Skill activates on wrong requests | Description too broad | Narrow it, or set `disable-model-invocation: true` for manual-only |
| Descriptions cut short at startup | Over budget | Run `/doctor`; trim descriptions, raise `skillListingBudgetFraction`/`SLASH_COMMAND_TOOL_CHAR_BUDGET`, or set low-priority skills to `"name-only"` |
| Skill stops influencing mid-session | Dropped/aged out during compaction | Re-invoke with `/skill-name`; strengthen instructions or enforce via hooks |
| Skill can still call a tool you wanted blocked | `allowed-tools` only *pre-approves* | Use `disallowed-tools` or a deny rule in `/permissions` |
| Changes to `SKILL.md` not taking effect | New top-level skills dir created mid-session | Restart Claude Code so the directory is watched |

---

## 12. Summary

1. **Skills load on demand; `CLAUDE.md` loads always.** Move procedures and reference material into skills; keep only standing facts in `CLAUDE.md`.
2. **Description quality is everything** — discovery is pure language matching. Front-load keywords, state triggering conditions rather than workflow steps, and keep entries within NOMAD's 300-char ceiling ([rules §5](skill-authoring-rules.md)).
3. **Mind the ~1% listing budget.** Around 15–25 skills it starts trimming least-used descriptions; diagnose with `/doctor`, raise it with `skillListingBudgetFraction`/`SLASH_COMMAND_TOOL_CHAR_BUDGET`, and pull manual-only skills out with `disable-model-invocation: true`.
4. **`allowed-tools` pre-approves, it does not restrict** — use `disallowed-tools` or deny rules to actually limit tool access.
5. **Scope deliberately:** universal tools in `~/.claude/skills/`, project/platform patterns committed to `.claude/skills/`.
6. **Use the advanced features** — dynamic context injection (`` !`cmd` ``), arguments/substitutions, and `context: fork` subagents — to make skills do real work, not just hold guidelines.
7. **Direct `/skill-name` invocation always works**, bypassing the matcher and budget — name critical skills in `CLAUDE.md` as a safety net.
</content>
</invoke>
