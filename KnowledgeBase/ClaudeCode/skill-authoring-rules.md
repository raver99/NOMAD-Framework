# 📏 Skill Authoring Rules – The Canonical NOMAD Rule Set

## Purpose of This Document

This is the single source of truth for how skills are written, tested and reviewed in NOMAD. The
`nomad-skill-creator` and `nomad-skill-validator` skills both read this file rather than carrying their own
copies, so a rule changed here changes both.

Every rule states **why** it exists. A rule without its reason gets discarded the first time it is
inconvenient, and nobody can tell whether an exception is legitimate.

For how skills are discovered, organised and scaled as a library, see
[Claude Code Skills](claude-code-skills.md).

---

## 1. The Governing Principle

> **A test that cannot fail proves nothing.**

Every testing rule below is this principle in a different costume:

| Mechanism | What it stops you believing |
|-----------|-----------------------------|
| Baseline run (without the skill) | That the skill caused the result, when the model would have done it anyway |
| No-guidance control in wording tests | That a phrasing helped, when it made no difference |
| Non-discriminating assertion check | That an eval measures your skill, when it measures the model |
| Near-miss negative trigger queries | That a description is precise, when it was never tested against anything close |

Skills are easy to write and easy to fool yourself about. The rules exist because plausible-looking
skills that contribute nothing are the normal outcome, not the rare one.

---

## 2. Authoring Workflow

### 2.1 Watch It Fail First

Before writing any skill content, run the task **without** the skill and observe what actually goes
wrong. Write the skill against those observed failures.

> **If you did not watch it fail, the skill encodes what you *imagine* the model gets wrong.**

This is the highest-value rule in the document. Most skills that fail to earn their place instruct a
model that was already behaving correctly. Observing the failure first also tells you whether the
skill is needed at all — if nothing goes wrong, stop.

This applies to edits as well as new skills. Observing a failure is cheap; it is committing an
assertion that costs, and those are separate decisions (§6).

### 2.2 The Loop

1. **Capture intent** — what should this enable, when should it trigger, what is the output?
   If the conversation already contains the workflow, mine it: the tools used, the sequence, the
   corrections made, the formats observed.
2. **Research first** — look for prior art before writing. Someone has probably solved this, and
   arriving with context reduces what the human has to supply.
3. **Observe the baseline** (§2.1).
4. **Draft** the minimal skill addressing the observed failures.
5. **Test** with 2–3 realistic prompts, run with and without the skill in the same batch.
6. **Review** the outputs as a human before the model offers its verdict.
7. **Improve and repeat** until the feedback is empty or progress stalls.

### 2.3 Improving

- **Generalise from feedback.** You iterate on two or three cases, so every fix is tempted to fit
  exactly those. A skill that only works on its own test cases is worthless.
- **Deletion is an experiment.** Read the transcripts, not just the outputs. If the skill makes the
  model waste effort, remove that part and measure. Skills only ever get added to unless removal is
  made deliberate.
- **Rigidity is a symptom.** Reaching for a shouted rule usually means patching a behaviour you have
  not understood. Reframe and explain the reason instead.
- **Repeated work becomes a script.** If every test run reinvents the same helper, bundle it once.

---

## 3. Skill Types

The type determines what testing discriminates. Classify before testing.

| Type | Is | Test by |
|------|----|---------|
| **Discipline** | A rule to hold under pressure | Pressure scenarios and academic questions |
| **Technique** | A how-to | Application, plus edge cases |
| **Pattern** | A mental model | Recognition, plus counter-examples |
| **Reference** | Documentation | Retrieval, plus correct application |

A rule-shaped skill fails differently from a reference-shaped one — a discipline skill that is
merely *understood* has still failed if it is abandoned under pressure.

---

## 4. Frontmatter

✅ **Allowed keys:** `name`, `description`, `license`, `allowed-tools`, `metadata`, `compatibility`,
plus the Claude Code additions `arguments`, `disable-model-invocation` and `context`.

❌ **Never a top-level `version:`.** It fails spec validation. Version belongs under `metadata`.

```yaml
---
name: nomad-skill-validator
description: Use when ...
metadata:
  version: 1.2.0
---
```

| Field | Rule | Why |
|-------|------|-----|
| `name` | Kebab-case, ≤64 chars; gerund form preferred | See §4.1 |
| `description` | ≤300 chars, see §5 | Shares a budget with every other skill |
| `metadata.version` | Mirrors the containing plugin's version | Plugin manifests do not travel when a skill is copied out |
| `allowed-tools` | Scope it on any side-effecting skill | Blast radius. Signing, submission and migrations should not inherit everything |

> **On `allowed-tools`:** some community guidance says to omit it entirely and let skills inherit all
> capabilities. NOMAD rejects that. Scoping is the cheapest control available for skills that can
> destroy something.

### 4.1 Naming

NOMAD uses **`nomad-` prefix plus a noun phrase naming the role**: `nomad-skill-validator`,
`nomad-skill-creator`, `nomad-technical-writer`. Two reasons, and neither is style:

- **Collision.** Anthropic ships an official `skill-creator` in the marketplace this machine already
  has configured. An unprefixed `skill-creator` would collide the moment that plugin is installed.
  The prefix also matches the existing NOMAD.Maui skills (`nomad-maui-doctor`, `nomad-add-tool`).
- **Names survive trimming.** When the description budget overflows, descriptions are dropped but
  **names are always kept** — so the name is the fallback routing signal exactly when routing has
  already degraded. It has to carry meaning alone.

The official guidance instead suggests **gerund form** (`processing-pdfs`, `writing-documentation`)
on the grounds that it names the activity. It says "consider" rather than requiring it, and
explicitly allows noun phrases (`pdf-processing`) and action-oriented forms (`process-pdfs`).
Anthropic's own shipped skills almost entirely use noun phrases — of roughly 25 in the official
marketplace, exactly one is a gerund — so the recommendation is weaker in practice than on paper.
Either convention is defensible; the validator does not fail a name for its form.

❌ What is genuinely wrong: vague names (`helper`, `utils`, `tools`), names too generic to
distinguish (`documents`, `data`), and **inconsistency within a library** — which matters more than
which convention you picked.

---

## 5. Descriptions

The description is the entire routing mechanism. It is loaded at startup; the body is not.

### 5.1 Triggers Only, Never Workflow

✅ `Use when a SKILL.md was written or changed, or when asked to review a skill.`
❌ `Use when reviewing skills - runs the checker script then reports findings by severity.`

> **Procedure placed in a description is procedure the model may execute without ever opening the
> skill.** A documented case: a description reading *"dispatches subagent per task with code review"*
> caused agents to follow the description and skip the two-stage review defined in the body.

State symptoms, contexts and error messages. Start with "Use when".

This applies to descriptions that route. For a skill with `disable-model-invocation: true` the
description is a label in autocomplete rather than a trigger, so it should say what the skill does;
"Use when" is not required and the validator does not ask for it (§5.4).

### 5.2 The 300-Character Ceiling

Descriptions share a budget of roughly 1% of the context window. At 300 characters, about 25
model-invocable skills fit before trimming begins — and trimming drops the descriptions of the skills
you use least, stripping the keywords that would have matched.

- It is a **ceiling, not a target**. A target invites padding.
- Trigger keywords go **first**; a truncated description keeps its opening.
- Skills with `disable-model-invocation: true` are **exempt** — they leave the budget entirely, so
  their length is a documentation question rather than a routing one.

Claude tends to *under*-trigger skills, so enumerate trigger cases explicitly rather than implying
them. The ceiling is what stops that turning into padding.

### 5.3 Triggering Is Not Pure Matching

Claude only consults a skill for work it cannot easily do alone. A skill covering easy work will not
reliably trigger *and* will not beat its baseline — it fails twice. That is a reason not to write it.

### 5.4 Explicitly Invoked Skills Are Judged Differently

`disable-model-invocation: true` removes a skill from routing altogether. The model never loads it on
its own; it runs when a person types its name. That changes what the skill has to prove.

§5.3 rejects skills over easy work on two grounds: they will not trigger, and they will not beat
their baseline. The first ground disappears when there is no triggering decision to get wrong. The
second stops being the only measure, because an explicitly invoked skill carries value the baseline
test does not measure:

- **Discoverability.** A convention recorded in a file is invisible until someone opens the file. A
  skill appears in autocomplete, so what a project supports can be found by typing `/`.
- **Teaching.** The list of skills tells a new contributor what this project expects to be done, and
  in what way. A guide conveys that only to whoever reads it.
- **Consistency and speed.** Typing `/nomad-backlog-groom` is faster than composing the paragraph it
  stands for, and it issues the same request every time instead of a differently-worded one each
  session.

> **The bar for an explicitly invoked skill is whether a person benefits from being able to name the
> operation** — not whether it beats a baseline.

A skill that passes that test and fails the baseline test is legitimate. One that fails both is not:
if an operation is faster to describe than to invoke, naming it is overhead. "Mark T-007 done" needs
no skill.

Two consequences follow:

- **Trigger evals do not apply** (§6). There is nothing to route, and an eval measuring a description
  that is never matched cannot fail.
- **Action-form names are preferred** over the noun-phrase convention of §4.1, because here the name
  is the thing being typed rather than a routing signal.

---

## 6. Evaluations

**Trigger evals — always committed, except where nothing routes.** `evals/trigger_eval.json`, 20
queries, roughly half `should_trigger: true`. Skills with `disable-model-invocation: true` are exempt
(§5.4).

- Realistic and messy: real paths, names, backstory, lowercase, typos, mixed lengths.
- Negatives must be **near-misses**. An obviously unrelated query tests nothing.
- Clean specimens like `Extract text from PDF` discriminate nothing — any description passes them.

**Output evals — kept while authoring, committed selectively.** They need input files, assertions, a
grader and baseline runs to mean anything. Commit them where output is objectively verifiable; do not
force them where the output is judged by eye.

**Run artifacts never live inside the skill.** They go in a sibling `<skill-name>-workspace/`.
`evals/` ships with the skill; the workspace does not.

---

## 7. Structure

```
skill-name/
├── SKILL.md              # under 500 lines
├── evals/
│   └── trigger_eval.json
├── references/           # loaded on demand
├── scripts/              # executed, not loaded
└── assets/               # used in output
```

- **References one level deep from SKILL.md.** Nested references get partially read — the model
  previews rather than reads, and takes away incomplete information.
- **Intention-revealing filenames.** `aws-deployment-patterns.md`, never `reference.md`. Claude
  decides what to open from the filename alone; a generic name carries no signal.
- **Tables of contents** in reference files over ~100 lines, so a partial read still reveals scope.
- **Forward slashes** in all paths.

---

## 8. Generality

Write the skill as general as the task allows. Specific cases become extensions, not narrower skills.

- **Variants of the same problem** → `references/<variant>.md`, selected by the skill body.
- **Project-specific behaviour** → a **project extension skill** in that project's `.claude/skills/`
  that names the general skill and adds local deltas. It survives reinstalling the general skill,
  is version-controlled with the project, and states its dependency openly — where a `references/`
  file inside the general skill is overwritten on update, and a look-for-this-file convention fails
  silently.
- The extension is the **entry point**, not a second trigger, so the two do not compete for routing.

❌ Over-general is also failure. A skill that restates good practice earns nothing. Set the altitude
by how fragile the task is: high freedom where many approaches work, low freedom where the sequence
is fragile and consistency matters.

---

## 9. Parameters

| Situation | Shape |
|-----------|-------|
| The argument names *what to work on* | One skill, input argument |
| The branch is discoverable from state | One skill, branch internally — no flag |
| Different trigger phrasings or moments | Separate skills |
| Different risk profile | Separate skills — `allowed-tools` cannot be scoped per branch |
| Shared workflow, different variants | One skill + `references/<variant>.md` |

❌ **Mode arguments are usually a smell.** One description must then cover several jobs against the
300-character ceiling, so each is described vaguely and all of them route worse.

---

## 10. Versioning and Distribution

- **Marketplace** = repository. **Plugin** = unit of install *and* version. **Skill** = unit of function.
- One plugin per independently installable skill. Bundling several into one plugin makes installs
  all-or-nothing and forces version bumps on skills that did not change.
- `metadata.version` mirrors the plugin version, so the number survives a skill being copied out.
- Propagation is **pull-based**: each project updates when it chooses, so an improvement cannot
  silently change behaviour across several projects mid-flight.
- A project extension records `metadata.extends` and `metadata.built-against`. This is a pin
  *record*, not a resolver — nothing enforces it, but it makes drift detectable.

> **Cross-skill references have no platform support.** There is no `requires:`, no version constraint
> and no resolution. Of the 25 skills in Anthropic's official marketplace, exactly one references
> another skill — and that reference is dangling. Verifying them is the review gate's job because
> nothing else does it.

---

## 11. The Validation Checklist

Mechanical, enforced by `nomad-skill-validator`:

1. Description ≤300 chars for model-invocable skills
2. Description states triggers, not workflow steps
3. Every skill named by a skill exists
4. `metadata.version` matches the containing plugin
5. `built-against` pin still matches the installed target
6. No all-caps ALWAYS/NEVER/MUST (a yellow flag, not an error)
7. Body under 500 lines
8. No generic reference filenames
9. References one level deep

Judgement, requiring a model:

- Is the description a good trigger, or merely accurate? For an explicitly invoked skill (§5.4),
  does a person benefit from being able to name this operation?
- Is the skill overfitted to its own test cases?
- Are the degrees of freedom right for how fragile the task is?
- Does the skill explain *why*, or only *what*?

---

## 12. Summary

1. **Watch it fail before writing.** Otherwise the skill encodes imagined problems.
2. **A test that cannot fail proves nothing** — baselines, controls and near-miss negatives all exist
   to make failure possible.
3. **The description routes; the body instructs.** Triggers only, ≤300 characters, keywords first.
4. **Classify the skill type** — it decides what testing discriminates.
5. **Commit trigger evals always; commit output evals only where output is verifiable.**
6. **General by default**, with variants in references and project specifics in extension skills.
7. **Version the plugin, mirror it in `metadata`** so the number survives a copy.
8. **Explain why.** A shouted rule is a symptom of a reason you have not worked out yet.

---

## References

- Skill authoring best practices — https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices
- Anthropic Agent Skills repository — https://github.com/anthropics/skills
- Anthropic `skill-creator` — `~/.claude/plugins/marketplaces/claude-plugins-official/plugins/skill-creator/`
- `obra/superpowers` `writing-skills` — https://github.com/obra/superpowers
- `metaskills/skill-builder` — https://github.com/metaskills/skill-builder
