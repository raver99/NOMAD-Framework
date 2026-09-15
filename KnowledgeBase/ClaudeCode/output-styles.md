# 🎚️ Output Styles – Controlling How Claude Responds, and What That Control Cannot Do

## Purpose of This Document

This document explains **output styles** in Claude Code — the mechanism that changes how the agent
writes back to you, without changing what it knows or how it works. It covers the five built-in
styles, how to select one, how to write a custom one, and how a style binds to a session. It then
covers the part nobody documents: a selected style **loses grip as a conversation gets longer**, this
is measurable, and the obvious fixes do not work. NOMAD treats AI-assisted development as a
first-class concern, and the volume of prose an agent returns is a direct cost on every session — so
the control is worth using, and its limit is worth knowing before you rely on it.

> **Pick a style when you keep re-prompting for the same voice every turn. Then expect it to fade
> after roughly eight exchanges, and start a fresh session rather than fighting it — the drift is a
> model behaviour, not a misconfiguration.**

This document covers the **mechanism and its limits**. The measurements and sources behind the limit
are in [Output style adherence over a conversation](../../docs/research/output-style-adherence-over-a-conversation.md).

---

## 1. What an Output Style Is

An output style **modifies the system prompt**. It sets role, tone and default response format. It
does not change which tools are available, what the agent knows about your project, or how it does
the work.

That is the line worth holding onto:

| Concern | Belongs in |
| :--- | :--- |
| How the agent *writes back to you* | Output style |
| What the agent knows about your project | `CLAUDE.md` |
| A procedure invoked on demand | A skill |
| A one-off addition for a single invocation | `--append-system-prompt` |
| A separately scoped helper task | A subagent |

Styles apply to the **main conversation only**. A subagent runs its own system prompt, so a style
does not reach it. A fork is the exception, because it inherits the parent's full system prompt.

---

## 2. The Five Built-In Styles

| Style | Behaviour |
| :--- | :--- |
| **Default** | The standard software-engineering system prompt. |
| **Concise** | Leads with the result, skips preamble and narration, keeps responses short by default. Requires v2.1.237+. |
| **Proactive** | Executes immediately, makes reasonable assumptions rather than pausing for routine decisions. Independent of permission mode. |
| **Explanatory** | Adds educational "Insights" between engineering steps. |
| **Learning** | Collaborative; adds `TODO(human)` markers asking you to write small pieces yourself. |

All five keep Claude Code's built-in software-engineering instructions. A **custom** style drops them
by default — see §5.

### 2.1 What Concise Actually Instructs

Concise is worth spelling out because its guard rails are the reason it is safe to use on real work.
It instructs the agent to lead with the result, cut narration, answer simple questions in 1–3
sentences, and state things plainly — **and** it explicitly carves out three exceptions:

- **Full detail on request.** Asking for an explanation gets a complete one. Concise never means
  withholding information you asked for.
- **Correctness over brevity.** Error reports, failing test output and security warnings keep their
  full content.
- **Destructive-action confirmations** keep their full content.

It also declares that where it conflicts with other communication guidance in the prompt, the style
wins.

> **Concise constrains the shape of the answer, not the thinking budget.** It does not cap the
> reasoning between tool calls, which is where compressing an agent measurably damages its work.

---

## 3. Selecting a Style

| Where | How |
| :--- | :--- |
| Terminal | `/config` → **Output style**. Saves to `.claude/settings.local.json`. |
| VS Code extension | `/` → **Output styles**. Same file. Requires v2.1.257+. |
| Any settings file | Set `"outputStyle": "Concise"` directly. |

```json
{
  "outputStyle": "Concise"
}
```

The standalone `/output-style` command was deprecated in v2.1.73 and removed in v2.1.91.

> ⚠️ **A global setting reaches every session on the machine, including unattended ones.** If you run
> scheduled agents or automation under the same account, a global `Concise` applies to the reports
> they write — and a report nobody can ask a follow-up question about is exactly where brevity costs
> most. Scope the style to the interactive work.

---

## 4. How a Style Binds — and Why That Depends on Your Host

The documentation states that output style is part of the system prompt, which Claude Code reads once
at session start, so changes take effect after `/clear` or a new session.

**That describes the interactive REPL**, which holds one long-lived process. It is not universally
true, and the difference matters if you are building on the Agent SDK:

| Host | Process model | Consequence |
| :--- | :--- | :--- |
| Interactive CLI | One process holds the session | Style is fixed at session start; `/clear` to change it |
| Agent SDK caller that spawns per turn and resumes by session id | Every turn is a fresh process | Every turn *is* a session start — the style can be changed mid-conversation, **and must be re-sent every turn or it silently reverts** |

The second row is the trap. A style that is not re-passed on a resumed turn reverts to whatever the
project's own settings say, with no error and no visible signal. If you build a per-session style
control, the queue or background path — where no client is present to re-send anything — is where
this goes unnoticed.

> **If you host Claude Code, record the style the session *reports* installed, not just the one you
> asked for.** They are two different facts. When a user says "it stopped working", only the reported
> value distinguishes a plumbing bug from §6.

Changing style mid-session invalidates the cached prompt prefix once. The cost scales with
conversation length and does not repeat.

---

## 5. Custom Styles

A custom style is a Markdown file: frontmatter, then instructions appended to the system prompt.

| Location | Scope |
| :--- | :--- |
| `~/.claude/output-styles/` | All your projects |
| `.claude/output-styles/` | This project |
| Managed settings directory | Organisation |

| Frontmatter | Purpose | Default |
| :--- | :--- | :--- |
| `name` | Style name, if not the filename | Filename |
| `description` | Shown in the `/config` picker | None |
| `keep-coding-instructions` | Keep the built-in software-engineering instructions | `false` |
| `force-for-plugin` | Plugin styles only: apply automatically when the plugin is enabled | `false` |

> ❌ **The `keep-coding-instructions` default is the one that bites.** It is `false`, so a custom
> style silently drops Claude Code's guidance on scoping changes, writing comments and verifying
> work. If you are changing *how the agent talks* while it still writes code, you must set it to
> `true`. All five built-ins have it on.

---

## 6. The Limitation: Style Adherence Fades Over a Conversation

This is the part that is not in the documentation, and it is the reason to read this page.

### 6.1 What Was Measured

With Concise selected and verifiably installed on **every** turn, the same five questions were asked
in a fresh session and again deep inside a 12-turn conversation:

| | Cold session | Deep in a conversation |
| :--- | ---: | ---: |
| Mean answer length | 272 words | 414 words |
| | | **+52%** |

Five out of five questions came back longer at depth. Meanwhile the style itself never lapsed — 40
consecutive runs reported `Concise` installed, including turn 11.

**So the style is being delivered, and the agent gets more verbose anyway.**

### 6.2 It Is the Turns, Not the Context Size

Seeding a *fresh* session with 60 KB of pasted material and asking on turn 2 did **not** reproduce
the effect — on-topic material +16%, unrelated material −0%, both inside measurement noise. Ten
exchanges do it; one large message does not.

This matches the published mechanism: attention on the system prompt stays stable *within* an
utterance and drops at each **new user turn**. A long conversation and a long prompt are not the same
stressor.

### 6.3 This Is a Named, Reproduced Effect

Three independent research groups have measured versions of it:

| Effect | Finding |
| :--- | :--- |
| **Instruction drift** | Significant drift within **eight rounds** of conversation; mechanism identified as attention decay over exchanges. |
| **Answer bloat** | Multi-turn answers run **20–300% longer** than single-turn equivalents; even *correct* solutions come back **27% longer**. |
| **Complexity inflation** | Iterative pressure "reliably increases structural complexity" while reducing adherence to original constraints. |

And it is **not forgetting**: models asked to restate a constraint do so accurately *while violating
it*, at rates from 8% to 99% depending on the model.

### 6.4 Why Reminding It Again Does Not Work

The instinctive fix is to re-state the instruction each turn. **Claude Code already does this** — the
documentation confirms it reminds Claude of the selected style during the conversation, and the
reminder text is present in the binary. Drift is measured anyway.

The mitigations the literature validates are either the same idea (system-prompt repetition), or
require access an ordinary user does not have (reweighting attention internally; filtering the
assistant's own prior turns out of the history). Layering a second reminder into your own prompt is
re-implementing something with demonstrated insufficiency.

### 6.5 What To Actually Do

| Situation | Do this |
| :--- | :--- |
| Answers have got long and waffly | **Start a fresh session.** This is the effective lever, and it costs nothing. |
| A long thread you cannot abandon | State the constraint in *this turn's message* — the last position in the input carries the most weight |
| You need brevity to hold reliably | Keep the task short. Brevity survives a 3-turn conversation; it does not survive a 20-turn one |
| Unattended or scheduled work | Do not apply a brevity style at all — see the warning in §3 |
| A user reports "the style stopped working" | Check the *reported* installed style first (§4). If it says the style is on, this section is your answer |

> **Verbosity is not only cosmetic.** Longer assistant responses correlate with **10–50% worse task
> performance** across most tasks measured, and bloated solutions are described as qualitatively
> worse. A conversation that has got wordy has probably also got less reliable — which is a second,
> better reason to start fresh.

---

## 7. A Note on Measuring This Yourself

If you go to check any of this on your own setup, one number matters more than the rest: **identical
inputs vary by ±20–30%.** Three runs of one unchanged question returned 440, 395 and 314 words.

Two conclusions during the work behind this document were drawn from single measurements, and
replication overturned both. Use a paired design — the same question in both arms — and at least five
pairs. Below about a 30% difference, a single run tells you nothing.

---

## Related

- [Output style adherence over a conversation](../../docs/research/output-style-adherence-over-a-conversation.md) — the measurements, sources and raw extracts behind §6
- [Claude Code Skills](claude-code-skills.md) — for procedures and reference material, which is a different job from tone
