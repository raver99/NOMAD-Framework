---
status: planned
type: feature
priority: medium
epic: EP-AICollaboration
updated: 2026-08-16
---

# WI-8 — Skill authoring practice

## Summary

Establish how skills get written and reviewed, so quality is enforced rather than hoped for.
The starting assumption is *not* that NOMAD builds its own skill creator — prior art already
exists and is strong. Research it first, understand it, then take the good parts and improve or
customize where NOMAD actually adds something.

## Approach

Research before building, per principle 1 in the README. That means: find what already exists,
understand *why* it works before judging it, compare the options against each other, then decide
what to adopt as-is, what to adapt and what genuinely has to be written from scratch.

### Prior art already found

**Anthropic's `skill-creator`** — an official plugin in the `claude-plugins-official`
marketplace, already present locally but not installed. A 485-line `SKILL.md` with grader,
comparator and analyzer subagents plus Python scripts. Its loop is evaluation-driven rather
than template-driven: interview, draft, run test prompts through subagents both with and
without the skill, grade against assertions, review the outputs in an HTML viewer, rewrite,
repeat. It also optimizes the `description` field against a train/test split of trigger queries.

**Anthropic's `plugin-dev`** — a separate plugin carrying a `skill-development` skill and a
`skill-reviewer` agent that audits an existing skill against best practices.
`skill-creator/scripts/quick_validate.py` mechanically checks frontmatter limits.

**Official documentation** — the skill authoring best practices page covers progressive
disclosure, degrees of freedom, description writing, evaluation-driven development and a set of
anti-patterns. See references.

### Where the gap looks like it is

Creation is well covered; **enforcement and review are the weaker half**. `quick_validate.py`
checks syntax and length limits, not quality. `skill-reviewer` is advisory and lives in a
different plugin from the creator, so nothing wires review into the authoring flow. Anthropic's
own documentation states that no special skill is needed to get Claude to write a skill — which
argues against NOMAD writing another creator, and for a review gate carrying the official best
practices plus NOMAD's own conventions.

This is a hypothesis from a first pass, not a conclusion. It gets confirmed or dropped after the
community comparison.

## Decisions so far

**Description budget: 300 characters.** A middle path between two defensible positions that
conflict. `skill-creator` says descriptions should be "pushy" — enumerate trigger cases
explicitly, because Claude tends to *under*trigger skills — and its own example runs to roughly
300 characters. `KnowledgeBase/ClaudeCode/claude-code-skills.md` §6.4 says aim for 100–200,
because descriptions share a budget of roughly 1% of the context window and bloat causes *other*
skills' descriptions to be dropped. The first optimises one skill, the second optimises the
library.

At 300 characters, roughly 25 model-invocable skills fit before trimming begins — consistent
with the 15–25 the knowledge base already states for the 200–400 band.

Applied as a **ceiling for model-invocable skills, not a target**: trigger keywords first, "when
to use" enumerated rather than implied. Skills carrying `disable-model-invocation: true` are
exempt — they leave the description budget entirely, so their length is a documentation question
rather than a routing one. A target invites padding; a ceiling does not.

This was settled by argument, but it is measurable rather than a matter of taste:
`skill-creator`'s `scripts/run_loop.py` scores a description against labelled trigger queries on
a held-out split, so whether 300 characters actually routes better than 150 for a given skill is
an experiment someone can run.

**Test cases stay open.** `skill-creator` splits skills into objectively verifiable (worth test
cases) and subjective (usually not). NOMAD skills are expected to produce both kinds, so the
split is a hint the authoring flow may offer, not a gate.

**Evals ship with the skill, split by type.** Evaluation-driven authoring is endorsed by the
official documentation ("build evaluations first"; the authoring checklist asks for at least
three). Shipping the evals is not established practice, though — of the 25 skills in the
official marketplace, exactly one carries an `evals/` directory, and what it holds is a trigger
eval rather than output evals. So:

- **Trigger evals — commit them** for every model-invocable skill. A JSON list of realistic
  queries labelled `should_trigger`, cheap to write, mechanically runnable, and the only way to
  verify that a description actually routes. This is what protects the 300-character decision
  above, and it is the one kind Anthropic does ship.
- **Output evals — keep while authoring, commit selectively.** They need input files,
  assertions, a grader and baseline runs to mean anything, and the platform documentation is
  explicit that no built-in runner exists for the documented eval format. Worth committing
  where output is objectively verifiable; not worth forcing where output is judged by eye.

**Interactive when it earns it.** `skill-creator` assumes a human available to interview. NOMAD
skills should ask when the answer changes the outcome, and proceed otherwise.

**To reconcile:** the knowledge base cites a 1,536-character per-entry cap
(`maxSkillDescriptionChars`, a Claude Code setting) while the platform spec states 1,024. These
are limits from different layers and the knowledge base does not currently distinguish them.

## Design decisions

- **Learning from real usage.** *Settled in shape, not in detail.* `skill-creator` already
  promotes repeated work into bundled scripts, but only from test runs inside an authoring
  session — learning from production runs over time is the gap. The design is **two stages**:
  skills self-report findings as they run, and a separate reviewer skill curates across runs and
  proposes changes. The split is forced rather than cosmetic — whether a lesson generalises
  cannot be judged from one run, so the filter only works with cross-run evidence, and the
  running skill is both the only witness and the worst judge of its own findings.
  - Findings land **outside** the skill, per project, append-only. An installed skill is often
    read-only; `skill-creator` hits this itself and copies to `/tmp` before editing.
  - The self-report instruction is stated **once, globally** — not duplicated into every skill,
    which would be a maintenance burden, a per-run token tax and a dilution of each skill's own
    instructions.
  - Report only **surprises**: friction, repeated work, a wrong assumption in the skill, an
    invented workaround. Not successful completions.
  - The reviewer **proposes**, it does not edit. Proposals go through the stage-5 baseline as
    v2-against-v1, so a learned change is verified rather than assumed.
  - Only **general** lessons feed back into the skill. Project-specific findings belong to that
    project's knowledge ([WI-6](WI-6-knowledge-management-with-ai.md)); narrower cases belong in
    an extension. Unfiltered feedback is a specificity pump — it drags a general skill toward
    whichever project used it most.
  - The findings log is knowledge capture and the reviewer is curation over it, which is
    structurally the same problem as WI-6; the two may share machinery.
- **Generality by default.** *Settled.* Skills are written as general as the task allows;
  specific cases become extensions rather than narrowing the skill. `skill-creator` names
  overfitting as the central authoring risk and explains the mechanism that causes it — you
  iterate on two or three test cases, so every fix is tempted to fit exactly those. Its tell is
  reaching for rigid rules to force a stubborn case through; the response is to reframe rather
  than constrain.
  - The extension mechanism is **progressive disclosure by domain**, not a second skill:
    `SKILL.md` carries the workflow and the selection logic, `references/<variant>.md` carries
    each specific case and loads only when relevant. No context cost until used.
  - Project-only specifics stay in the project, as a **project extension skill** in the
    project's own `.claude/skills/` that names the general skill it builds on and adds the local
    deltas. It survives reinstalling the general skill, is version-controlled with the project,
    and states its dependency in the open — where a `references/` file inside the general skill
    gets overwritten on update, and a look-for-this-file convention fails silently.
  - The extension is the **entry point**, not a second trigger: it carries the project-specific
    description and pulls in the general skill's workflow, so the two do not compete for routing.
  - Cross-skill references have **no support in the platform**. There is no `requires:`, no
    version constraint and no resolution; `compatibility` is freeform prose and is used by none
    of the 25 skills in the official marketplace. Of those 25, exactly one references another
    skill — and that reference is dangling, naming a skill that does not exist. So "every skill
    named by a skill actually exists" is a check the review gate has to perform itself. It is
    mechanically verifiable, and it would have caught Anthropic's own broken link.
  - Counter-pressure: over-general is also failure. A skill that restates good practice earns
    nothing and will not beat baseline. Altitude is set by **how fragile the task is** — high
    freedom where many approaches are valid, low freedom where the sequence is fragile and
    consistency matters.
- **Where best practices live.** *Settled by building the validator.* The rules go in a shared
  reference document that both the creator and the review gate read. If they lived inside either
  one, the other would need its own copy and the two would drift.
- **Parameterised skills versus separate skills.** *Settled.* What matters is what the argument
  does, not whether there is one.
  - **Input arguments** — naming the thing to operate on — are always fine. `/add-knowledge`
    already does this with `$ARGUMENTS`.
  - **Mode arguments** that switch which workflow runs are usually a smell. One description must
    then cover several jobs against a 300-character ceiling, so each is described vaguely and all
    of them route worse. `allowed-tools` is per skill rather than per branch, so a read-only mode
    and a destructive one share the union of permissions. Trigger evals have to disambiguate
    between modes rather than just decide whether to fire.
  - **Prefer branching on discovered state.** `/add-knowledge` already checks whether a file on
    the topic exists and merges rather than creating. The user should not have to know whether
    they are adding or enhancing — one trigger, one description, no flag. Splitting it into
    add/enhance would share a trigger, tools and workflow, so it stays one skill.
  - Separate skills when trigger phrasings differ, or when the risk profile differs and the tool
    grant should differ with it. One skill plus `references/<variant>.md` when the workflow is
    shared and only the variant changes.
- **Versioning and propagation.** *Settled.* Version at the **plugin** layer, which is where
  NOMAD.Maui already does it. Marketplace is the repository, plugin is the unit of install and
  of version, skill is the unit of function. Claude Code already records `version`,
  `installedAt`, `lastUpdated` and `gitCommitSha` per install, so provenance exists without
  anything new being built.
  - Skills also carry `metadata.version`, mirroring the version of the plugin that contains
    them. A top-level `version:` is not an option — `quick_validate.py` allows only `name`,
    `description`, `license`, `allowed-tools`, `metadata` and `compatibility`, and hard-fails on
    any other key; `metadata` is the one slot it does not inspect. (`plugin-dev`'s
    `skill-reviewer` still lists `version` as an optional top-level field. The two Anthropic
    artifacts contradict each other, and the validator is what runs.)
  - The reason to duplicate the number: plugin version does not travel. Skills get copied into
    `.claude/skills/` or vendored into other repositories, and the manifest is left behind while
    the SKILL.md goes with them. The version is also visible where the reader is — Claude reads
    SKILL.md, not `marketplace.json`. It does not prevent a copied-out skill from becoming a
    silent fork, but it is how anyone finds out they are sitting on a stale one.
  - The cost is two numbers that can drift, which the review gate closes by asserting
    `metadata.version` equals the containing plugin's version. Same move as the dangling
    reference and the built-against pin: the platform guarantees nothing, so the gate does.
  - Keep it in `metadata` frontmatter rather than body prose. Only `name` and `description` are
    preloaded for routing, so `metadata` costs nothing at discovery, while body text is paid on
    every invocation.
  - **Split the plugin.** NOMAD.Maui currently ships one plugin holding two skills, so a fix to
    one forces a version bump of the other and installs are all-or-nothing. Selective install
    across projects means more plugins in the same marketplace, not more skills per plugin.
    Cheap to restructure now, awkward later.
  - Propagation stays **pull-based** — each project updates when it chooses, so an improvement
    cannot silently change behaviour across several projects at once. The cost is that nothing
    tells a project it is behind.
  - A project extension skill records what it was built against in the one slot available
    (`metadata.extends`, `metadata.built-against`). This is a pin *record*, not a resolver —
    nothing enforces it — but it makes drift detectable by the review gate. Same shape as the
    dangling-reference check: the platform offers no guarantee, so the gate supplies it.

## Adopted from the community

Two community skill creators were compared against the official one:
[`metaskills/skill-builder`](https://github.com/metaskills/skill-builder), which is
conventions-focused and mostly restates official guidance, and
[`obra/superpowers`](https://github.com/obra/superpowers), whose `writing-skills` skill applies
test-driven development to skill authoring and is where most of the value is. Five ideas taken,
each with the reason it is worth having — the rule alone does not survive contact with someone
who does not know why it exists.

**Baseline first, as requirements-gathering rather than measurement.** `superpowers` runs
pressure scenarios *without* the skill before writing anything, then writes the minimal skill
addressing the specific violations observed: *"If you didn't watch an agent fail without the
skill, you don't know if the skill teaches the right thing."* NOMAD already had the baseline
from `skill-creator`, but only as an after-the-fact comparison that answers "did this help?".
Running it first answers a different and better question — "what should this say?" A skill
written without watching failure encodes what its author *imagines* the model gets wrong, which
is why so many skills earn nothing: they instruct a model that already behaves correctly.

**A description states triggering conditions, never workflow steps.** `superpowers` requires
descriptions to begin "Use when…" and to carry symptoms and error messages rather than
procedure, with evidence for the rule: a description reading *"Use when executing plans -
dispatches subagent per task with code review"* caused agents to **follow the description as if
it were the procedure and skip the two-stage review in the body**. That is the failure mode
worth guarding — the description is loaded at routing time and the body is not, so any procedure
placed in the description is a procedure the model may execute without ever opening the skill.
Mechanically checkable, so it becomes a validator check.

**Four skill types, each tested differently** — discipline (rules), technique (how-to), pattern
(mental models), reference (documentation). This replaces `skill-creator`'s binary split of
objectively verifiable against subjective, which NOMAD had left deliberately open because both
kinds were expected. The finer taxonomy resolves it: the question is not whether a skill *can*
be tested but which kind of test discriminates for that type, and a rule-shaped skill fails in a
way a reference-shaped skill does not.

**A no-guidance control, and repeated samples.** `superpowers` verifies wording against five or
more fresh samples per variant including a control with no guidance at all, and insists on
manual review because *"automated scoring misses subtle failures."* Same principle as the
baseline, the non-discriminating assertion and the near-miss negative: **a test that cannot fail
proves nothing.** Model output is stochastic, so a single sample is an anecdote, and without the
control there is no way to tell an improvement from the model's default behaviour.

**Intention-revealing reference filenames.** `skill-builder` requires
`./aws-deployment-patterns.md` over `reference.md`. Cheap, and it matters more than it looks:
Claude navigates a skill directory as a filesystem and decides what to open from the filename
alone, so a generic name carries no signal about whether it is worth reading. Checkable as a
denylist of generic names.

**Rejected — `skill-builder`'s claim that `allowed-tools` should never appear**, on the grounds
that skills inherit all CLI capabilities. It contradicts `KnowledgeBase/ClaudeCode/claude-code-skills.md`
§10, which uses `allowed-tools` to scope exactly the side-effecting skills where blast radius
matters — signing, store submission, migrations — and `allowed-tools` is in the official allowed
property set. **No position taken** on its preference for Node over Python in bundled scripts;
Anthropic's own scripts are Python and nothing here turns on it.

**Reconciling the Iron Law.** `superpowers` states "NO SKILL WITHOUT A FAILING TEST FIRST",
including for edits. Taken as: *always* observe the failure before writing, for every skill —
that is the RED step and it costs little. What is *kept* as a committed eval still follows the
earlier decision and the taxonomy: trigger evals always, output evals where the output is
verifiable. Observing failure and committing an assertion are different acts, and only the
second one is expensive.

## The validator

The first thing to build, and the one piece with no prior art. Six checks nothing else performs:

1. The 300-character ceiling for model-invocable skills
2. Every skill named by a skill actually exists
3. `metadata.version` matches the containing plugin
4. An extension's `built-against` pin still matches what is installed
5. All-caps ALWAYS/NEVER and rigid structures — `skill-creator` treats these as a **yellow
   flag**, since reaching for a shouted rule usually means patching a symptom instead of
   explaining the reason. A grep that points a human at the passages worth rereading.
6. No workflow steps in the description, and no generic reference filenames

Split by determinism. The mechanical checks — those six, plus body under 500 lines and
references one level deep — are string and file operations, so they belong in a script that
runs free of a model and works in CI. The judgement calls — is the description a good trigger,
is the skill overfitted to its examples, are the degrees of freedom right for how fragile the
task is — need a model, so a skill runs the script and reasons about what the script cannot see.

Reuse `quick_validate.py` for spec-level checks rather than reimplementing them, but **not its
allowed-key list**: it validates the portable Agent Skills spec, while Claude Code adds fields on
top. `arguments`, `disable-model-invocation` and `context` are all absent from its allowed set
and would hard-fail legitimate skills.

Keep the reviewer read-only, following `plugin-dev`'s `skill-reviewer` (`Read`, `Grep`, `Glob`).
A reviewer that can edit starts fixing instead of reporting, and the signal is lost — the same
reason the learning reviewer proposes rather than edits.

A validator's output is objectively verifiable, which makes it the case where committed output
evals earn their cost.

## Exercised on a real skill, 2026-08-16

The baseline-first loop was run for the first time, on three proposed backlog skills
(`nomad-backlog-capture`, `-status`, `-groom`). Three fresh agents, one seeded `BACKLOG.md` each,
no skill available. The model assigned IDs correctly, caught a planted duplicate, resolved an
ambiguous drop instruction with sound reasoning, and — grooming — reported a contradiction between
two items, a broken detail link and a Now list in ID order, then declined to resolve what needed the
user's priorities. All three skills failed their baseline. The practice works, and it is cheap:
about ten minutes.

Three things came out of it that change this work item:

- **A well-designed artifact can carry what a skill would have carried.** The seed backlog states
  its own format in its header, and the agents followed it. Every gap the runs exposed was a gap in
  the file, not a missing skill. Worth adding to the rules as a question to ask before writing a
  skill at all — is there a file that could hold this instead?
- **The rules had no bar for explicitly invoked skills.** §5.3 rejects skills over easy work on two
  grounds, one of which (won't trigger) does not apply when `disable-model-invocation: true`. Two of
  the three skills shipped on discoverability, teaching and consistent phrasing instead. Added as
  §5.4, with trigger evals waived and action-form names preferred.
- **The validator carried the same gap.** It already exempted `disable-model-invocation` skills from
  the description ceiling and from evals, but still required "Use when" — which degrades a label
  that is read by a person in autocomplete rather than matched by a model. Fixed.

Write-up: `docs/articles/what-skills-are-for.md`.

Still untested: the loop on a skill that *passes* its baseline. Every arm here failed, so the
"did this help?" half of the comparison was never exercised.

## Tasks

- [x] Build the validator: mechanical script plus the judgement-level skill over it
- [x] Write the shared best-practices reference the creator and the validator both read
- [x] Walk through `skill-creator` stage by stage and record what each stage is actually for
- [x] Capture the writing-style observations — they turned out to be general craft rather than
      personal taste, so they went into `nomad-technical-writer` itself. No extension skill: the
      audience question is asked per document rather than recorded in a profile
- [x] Run the baseline-first loop on a real skill, so the practice is exercised rather than described
- [ ] Split the NOMAD.Maui plugin so skills become independently installable
- [x] Research community skill-creation skills and compare them against the official one
- [x] Synthesize: what to adopt as-is, what to adapt, what NOMAD adds that nothing else does
- [ ] Confirm or drop the review-gate hypothesis based on that comparison
- [ ] Fold the findings into `KnowledgeBase/ClaudeCode/claude-code-skills.md`, which currently
      does not mention `skill-creator` at all
- [ ] Build whatever the synthesis says is missing

## References

- Skill authoring best practices — https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices
- Public Agent Skills repository — https://github.com/anthropics/skills
- Creating custom skills — https://support.claude.com/en/articles/12512198-creating-custom-skills
- Local: `~/.claude/plugins/marketplaces/claude-plugins-official/plugins/skill-creator/`
- Local: `~/.claude/plugins/marketplaces/claude-plugins-official/plugins/plugin-dev/`
