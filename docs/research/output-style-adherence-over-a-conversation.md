# Does an output style keep working as a conversation gets longer?

**Depth:** deep — the answer decides whether a per-chat response-style control is worth shipping in a
tool, and whether a user complaint ("it reverts after a few turns") points at a bug to fix or a model
behaviour to live with. Escalated from *standard*: the first two conclusions drawn here were drawn at
n=1 and both were wrong, which is itself the most transferable finding.

**Date:** 2026-09-08. Measurements run against Claude Code 2.1.251 via the Agent SDK, model Opus,
inside one repository.

The durable half of this record is captured as guidance in
[Output Styles](../../KnowledgeBase/ClaudeCode/output-styles.md). This file is the evidence layer:
what was retrieved, what was measured, and what would overturn it.

---

## Sources

| # | Source | Tier | Retrieved | How |
|---|--------|------|-----------|-----|
| 1 | https://code.claude.com/docs/en/output-styles | primary | 2026-09-08 | direct fetch (after 301 from `docs.claude.com`) |
| 2 | https://arxiv.org/pdf/2402.10962 — *Measuring and Controlling Instruction (In)Stability in Language Model Dialogs*, COLM 2024 | primary | 2026-09-08 | PDF downloaded, text extracted locally |
| 3 | https://arxiv.org/pdf/2505.06120 — *LLMs Get Lost In Multi-Turn Conversation*, Laban et al. | primary | 2026-09-08 | PDF downloaded, text extracted locally |
| 4 | https://arxiv.org/pdf/2602.24287 — *Do LLMs Benefit From Their Own Words?*, COLM 2026 | primary | 2026-09-08 | PDF downloaded, text extracted locally |
| 5 | https://arxiv.org/pdf/2604.28031 — *Models Recall What They Violate: Constraint Adherence in Multi-Turn LLM Ideation* | primary | 2026-09-08 | PDF downloaded, text extracted locally |
| 6 | Own measurement — 40 instrumented runs, one repository, Opus | live state | 2026-09-08 | see §Own measurements |
| 7 | `strings` over the installed `claude` binary, 2.1.251 | primary | 2026-09-06 | local artifact on disk |

### Not retrieved

| Source | Why | What it costs |
|---|---|---|
| OpenReview discussion for [4] | Login/verification wall on `openreview.net` | Nothing — the arXiv PDF of the same paper was retrieved, so the primary content is covered. Only the reviewer discussion is missing. |
| Anthropic engineering commentary on why output styles drift | None located; searches returned only secondary blog restatements | No vendor statement on *intent* or roadmap. §Findings 6 rests on documented behaviour plus own measurement, not on a vendor position. |

A note on one near-miss: a search-result summary attributed to Anthropic the framing that the
per-turn style reminder is a "quick band-aid while they work on a longer-term fix." Fetching the
cited article showed **it contains no such claim** and cites no source for it. It is not used here.

---

## Raw extracts

### [1] Claude Code documentation — how output styles are applied

> Output styles change how Claude responds, not what Claude knows. They modify the system prompt to
> set role, tone, and output format.

> **Concise**: Claude leads with the result, skips preamble and narration, and keeps responses short
> by default, while doing the engineering work as thoroughly as in the Default style. When you ask
> for an explanation or more detail, Claude answers in full. Claude always keeps the complete content
> of error reports, security warnings, and confirmations for destructive actions. Requires Claude
> Code v2.1.237 or later.

> Output style is part of the system prompt, which Claude Code reads once at session start. Changes
> take effect after `/clear` or a new session.

> * Claude Code adds the output style's custom instructions to the system prompt.
> * When you select a style other than Default, Claude Code also reminds Claude of the style during
>   the conversation.
> * Custom output styles leave out Claude Code's built-in software engineering instructions, such as
>   how to scope changes, write comments, and verify work, unless `keep-coding-instructions` is set
>   to `true`.

> Output styles apply to the main conversation only: a subagent runs its own system prompt, so styles
> don't change how subagents respond. A fork is the exception, because it inherits the parent's full
> system prompt.

### [7] The Concise style text, extracted from the 2.1.251 binary

> You are an interactive CLI tool that helps users with software engineering tasks. Keep your
> responses short and direct while doing the work just as thoroughly.
>
> **# Concise Style Active**
>
> 1. **Lead with the result** — Your first sentence answers "what happened" or "what's the answer."
>    No preamble ("Let me...", "Now I'll...") and no closing recap of what you already said.
> 2. **Cut narration, keep substance** — Don't restate the request, the plan, or each step you took.
>    Report outcomes, decisions, and anything the user must act on.
> 3. **Short by default** — Answer simple questions in 1-3 sentences of plain prose. Use headers,
>    tables, and bullet lists only when they carry real structure, never as decoration.
> 4. **State things plainly** — Skip hedging boilerplate. Mention a caveat only when it changes what
>    the user should do next.
> 5. **Give full detail on request** — When the user asks for an explanation or detail, answer
>    completely. Conciseness never means withholding requested information.
> 6. **Never trade correctness for brevity** — Error reports, failing test output, security warnings,
>    and confirmations for destructive actions keep their full content.
>
> Where these rules conflict with more general communication or formatting guidance elsewhere in your
> instructions, these rules win.

A per-turn reminder is injected alongside it:

> Be concise: lead with the result, skip preamble and narration, keep only what the user needs.

### [2] Instruction drift and attention decay (COLM 2024) — abstract

> System-prompting is a standard tool for customizing language-model chatbots, enabling them to
> follow a specific instruction. An implicit assumption in the use of system prompts is that they
> will be stable, so the chatbot will continue to generate text according to the stipulated
> instructions for the duration of a conversation. We propose a quantitative benchmark to test this
> assumption, evaluating instruction stability via self-chats between two instructed chatbots.
> Testing popular models like LLaMA2-chat-70B and GPT-3.5, we reveal a significant instruction drift
> within eight rounds of conversations. An empirical and theoretical analysis of this phenomenon
> suggests the transformer attention mechanism plays a role, due to attention decay over long
> exchanges. To combat attention decay and instruction drift, we propose a lightweight method called
> split-softmax, which compares favorably against two strong baselines.

### [2] The mechanism, stated by the authors

> A natural guess is that instruction drift relates to the transformer attention mechanism. When a
> chatbot generates a new token, it takes into account all previous tokens in the dialog but with
> varying weights. One might speculate that the longer the dialog, the less weight is placed on the
> initial tokens that make up the prompt. We measure this effect precisely and find that there is
> indeed a strong attention decay effect. Intuitively, it seems plausible that the prompt's efficacy
> will decrease as attention to initial tokens wanes. We back up this intuition mathematically by
> showing that, in an idealized model, the space of possible outputs from a language model will
> steadily enlarge over time.

### [3] The "lost in conversation" result

> achieved an average performance of 65%–a 25-point drop from single-turn performances of 90% when
> they receive the entire instruction at the beginning of the conversation. Notably, we observe this
> drop in performance even in two-turn conversations, and across all LLMs we test, from small
> open-weights (LLama3.1-8B-Instruct) to state-of-the-art (Gemini 2.5 Pro).

> We investigate several explanations for this effect and show that the LLMs tend to (1) generate
> overly verbose responses, leading them to (2) propose final solutions prematurely in conversation,
> (3) make incorrect assumptions about underspecified details, and (4) rely too heavily on previous
> (incorrect) answer attempts.

### [3] The answer bloat effect

> Across the four tasks, we find that answer lengths in the FULL and CONCAT settings tend to be
> similar, typically within 2-10% of each other. On three of the analyzed tasks (Code, Database,
> Summary), the first answer attempt in the SHARDED setting has a similar length to FULL and CONCAT
> counterparts, yet for each subsequent answer attempt, we observe an increase in average answer
> length. The effect is such that the final answer attempts in SHARDED conversations (right portion
> of the four plots) tend to be 20-300% longer than the solutions generated in the FULL and CONCAT
> settings. We name this observation the answer bloat effect: as a multi-turn conversation
> progresses, the LLM generates incorrect answer attempts, making assumptions about portions of the
> instruction that remain unspecified. As the user reveals additional information in succeeding
> turns, the LLM does not successfully invalidate its prior assumptions and overly relies on its
> previous attempts.

> For Code task, correct programs obtained from SHARDED setting are on average 850 characters long,
> which is 27% more characters than the correct solutions generated in the FULL setting (668
> characters on average). For Database, correct SQL queries in the SHARDED setting are on average
> 129 characters, 14% more characters than those from the FULL setting (113 characters). In summary,
> LLMs are less likely to reach a correct solution in multi-turn settings (lower P), and when they
> do, the final solutions they reach are longer (bloated), hinting that the solutions are
> qualitatively worse.

### [3] Verbosity is not free

> On five of the six tasks, performance is 10-50% higher in simulated conversations with shortest
> response length, compared to conversations with longest response length. As assistant responses
> get longer (left to right in the Table), [...] response length from the assistant is detrimental.

### [4] Context pollution (COLM 2026) — abstract

> In multi-turn conversations, large language models typically condition on the full conversation
> history: both past user prompts and assistant responses. We revisit this design choice by comparing
> full-context prompting to four alternative, substantially-reduced context configurations. Analyzing
> in-the-wild multi-turn conversations across three open reasoning and one state-of-the-art model, we
> find that response quality is largely preserved under aggressive context filtering: replacing all
> prior assistant turns with one-sentence summaries or keeping only the most recent user–assistant
> exchange often matches storing full context in performance while using roughly 8× less context. To
> understand this result, we observe that a substantial fraction of user turns (36.4%) in multi-turn
> conversations are self-contained and that many follow-up turns can be addressed by seeing only the
> immediately preceding user–assistant exchange. Furthermore, we find that when models condition on
> their own past responses, this can lead to context pollution, a phenomenon in which reasoning
> errors, hallucinations, or stylistic artifacts propagate across turns. Motivated by these findings,
> we design a context-filtering approach that selectively omits the assistant-side history. Taken
> together, these findings suggest moving away from storing full dialogue transcripts and instead
> retaining only what is relevant.

### [5] Recall without adherence — abstract

> When researchers iteratively refine ideas with large language models, do the models preserve
> fidelity to the original objective? We introduce DRIFTBENCH, a benchmark for evaluating constraint
> adherence in multi-turn LLM-assisted scientific ideation. Across 2,146 scored benchmark runs
> spanning seven models from five providers (including two open-weight), four interaction conditions,
> and 38 research briefs from 24 scientific domains, we find that iterative pressure reliably
> increases structural complexity and often reduces adherence to original constraints. A restatement
> probe reveals a dissociation between declarative recall and behavioral adherence, as models
> accurately restate constraints they simultaneously violate. The knows-but-violates (KBV) rate,
> measuring constraint non-compliance despite preserved recall, ranges from 8% to 99% across models.
> Structured checkpointing partially reduces KBV rates but does not close the dissociation, and
> complexity inflation persists.

### [5] What the authors say this rules out

> We report a finding that challenges the assumption that multi-turn degradation is driven by
> forgetting or context loss. Under iterative pressure to improve a research proposal, multiple
> models achieve near-perfect accuracy when asked to restate the original constraints, yet violate
> them in their actual proposals. KBV rates vary widely, from 8% (GPT-5.4) to 99% (Sonnet 4.6), with
> four of seven models exceeding 50%.

---

## Own measurements [6]

One repository, Claude Code 2.1.251 via the Agent SDK, model Opus, Concise selected and re-sent on
every turn. Answer length is measured in whitespace-delimited words of the final assistant message,
excluding tool calls and thinking.

### A. Was the style actually installed?

Each run recorded the `output_style` field from its own session-init message, which is what the
session reports it is running, as distinct from what the caller asked for.

| Runs | Asked for | Reported installed |
|---|---|---|
| 40 | `Concise` | `Concise` — 40/40, including turn 11 of a 12-turn session |

### B. Same question, cold session vs deep in a session (paired)

Five questions, each asked once in a fresh session and once inside the same 12-turn conversation.

| Question | Cold (words) | Deep (words) | Change |
|---|---|---|---|
| What does the ChatDrainer do, and why does it exist? | 440 | 583 | +32% |
| What does pins.ts store, and why a separate file? | 327 | 483 | +48% |
| What is the purpose of the workflows folder? | 153 | 188 | +23% |
| What has to happen before a UI change counts as done? | 218 | 391 | +79% |
| Universal vs Process layers? | 221 | 425 | +92% |
| **Mean** | **272** | **414** | **+52%** |

5/5 in the same direction; under a null of no effect that is p ≈ 0.03 by sign test.

### C. Is it context size, or is it turns?

A fresh session was seeded with a single ~60 KB paste, then asked the control question on turn 2.
Three replicates per arm; the deep arm is the turn-11 measurement from B.

| Arm | Runs (words) | Mean | vs cold |
|---|---|---|---|
| Cold — turn 1, no context | 440, 395, 314 | 383 | — |
| Turn 2 after a 60 KB **on-topic** paste | 593, 348, 388 | 443 | +16% |
| Turn 2 after a 60 KB **unrelated** paste | 367, 451, 326 | 381 | −0% |
| Turn 11 of a real 12-turn conversation | 583 | 583 | +52% |

### D. The noise floor

Three runs of one identical question under identical conditions: **440, 395, 314 words** — a spread
of roughly ±20–30% around the mean.

---

## Findings

1. **Delivery is not the failure mode, and it is cheaply verifiable.** 40/40 runs reported `Concise`
   installed, including deep in a long conversation. Where a host spawns a process per turn, the
   style must be re-sent every turn or it silently reverts — but once it is, it stays. A host should
   record the *reported* style separately from the *requested* one; the two differing is the only
   signal that distinguishes a plumbing bug from a model behaviour. Sources: [1], [6].

2. **Answers do get longer deep in a conversation, by roughly half.** +52% mean across five paired
   questions, 5/5 in the same direction, with the style verifiably installed in both arms. Sources:
   [6].

3. **The effect is driven by turns, not by context volume.** Stuffing a fresh session with 60 KB and
   asking on turn 2 did not reproduce it, whether the material was on-topic (+16%) or unrelated
   (−0%) — both inside the noise floor. This is consistent with [2]'s mechanism, in which attention
   to the system prompt decays across *exchanges*: a single large user message is not the same
   stressor as ten turns. Sources: [2], [6].

4. **Independent literature brackets the size of the effect and names it three ways.** Instruction
   stability degrades measurably within eight rounds [2]; answer bloat runs 20–300% longer in
   multi-turn than single-turn, and 27% longer even when the answer is *correct* [3]; iterative
   pressure "reliably increases structural complexity" [5]. The own measurement of +52% sits inside
   this range. Sources: [2], [3], [5].

5. **This is not forgetting.** Models restate constraints accurately while violating them, at
   knows-but-violates rates from 8% to 99% depending on model [5]. Re-supplying the instruction
   therefore addresses a cause that is not the cause. Sources: [5].

6. **The obvious mitigation is already applied and is not sufficient.** Claude Code already re-states
   the selected style during the conversation [1], and the reminder text is present in the binary
   [7]. Drift is measured anyway [6]. A host layering a second reminder on top would be
   re-implementing a mitigation with demonstrated insufficiency. The mitigations the literature
   actually validates are either the same idea (system-prompt repetition, [2]) or require access a
   host does not have (split-softmax reweights attention internally, [2]; assistant-side history
   filtering, [4]). Sources: [1], [2], [4], [6], [7].

7. **Verbosity is not merely cosmetic.** Longer assistant responses correlate with 10–50% *worse*
   task performance across five of six tasks [3], and bloated solutions are described as
   "qualitatively worse". So drift in a style like Concise is a weak proxy for something that also
   costs correctness — which raises the value of noticing it, and lowers the case for tolerating it
   indefinitely. Sources: [3].

8. **Methodological, and the most transferable finding here: do not act on a single measurement of a
   generative system.** Identical inputs varied ±20–30% [6D]. Two confident conclusions were reached
   during this work at n=1 and both were overturned by replication — the first attributed the growth
   to prompt breadth, the second to on-topic context volume. A paired design (same question in both
   arms) plus n≥5 is what rescued a real signal from this noise; anything smaller than about 30% at
   n=1 is unmeasurable. Sources: [6].

---

## What would move these conclusions

- **Finding 3 rests on n=3 per arm.** The paste arms are inside the noise floor, so they establish
  "no large effect", not "no effect". A dose-response series (2, 5, 10, 20 turns at fixed context
  size) would separate turn count from conversation length properly.
- **One repository, one model, one style.** Whether the +52% holds on other models, or for styles
  other than Concise, is untested here.
- **Word count is a crude proxy for a style violation.** A longer answer carrying more substance is
  not necessarily disobeying "short by default" — rule 5 of the style text explicitly permits full
  detail on request [7]. No judge-based adherence scoring was run.
