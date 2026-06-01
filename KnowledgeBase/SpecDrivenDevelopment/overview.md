# 📐 Spec-Driven Development – Framework Evaluation

## Purpose of This Document
This is the hub for NOMAD's evaluation of **spec-driven development (SDD)** frameworks — approaches where a structured, human-reviewed specification drives AI-assisted implementation rather than ad-hoc prompting. It defines what SDD is, the criteria NOMAD uses to judge a framework, and an index of the candidates under evaluation. Detailed per-framework analyses live in their own candidate-profile documents linked below.

> **Spec-driven development makes the *spec* the source of truth and the AI agent the implementer. The discipline lives in the artifacts and the workflow, not in any single prompt.**

---

## 1. What Spec-Driven Development Is

In an AI-assisted workflow, the quality of output is bounded by the quality of intent fed to the model. SDD formalizes that intent: instead of conversational, one-shot prompting, work flows through explicit artifacts — briefs, PRDs, architecture docs, epics, and stories — each reviewed by a human before the next phase begins.

The agent doesn't guess; it reads the spec, executes a defined step, and stops at controlled checkpoints. This is the same principle NOMAD applies to requirements (see [Requirements Best Practices](../Requirements/requirements-best-practices.md)), extended across the entire lifecycle from idea to retrospective.

✅ **Structured artifacts as the contract** between human intent and AI execution
✅ **Phased, reviewable progression** (analysis → planning → solutioning → implementation)
✅ **Human-in-the-loop at defined checkpoints**, not on every token
❌ **Ad-hoc prompting** with no durable artifact and no defined stopping points

---

## 2. Why It Matters for NOMAD

NOMAD's core principles are *don't reinvent the wheel*, *minimize setup/maintenance effort*, and *AI-assisted development at every stage*. A good SDD framework delivers all three at once: it packages a proven process, runs inside the tools the team already uses, and keeps the AI productive without losing human control.

The goal of this evaluation is to pick (or compose) an opinionated SDD approach NOMAD can recommend as a default for mobile and cross-platform projects.

---

## 3. Evaluation Criteria

Each candidate is assessed against the following:

| Criterion | What we look for |
| :--- | :--- |
| **Setup effort** | How quickly a team goes from zero to a working workflow |
| **Tool fit** | Works inside existing AI IDEs/agents (Claude Code, Cursor, etc.) without a bespoke runtime |
| **Lifecycle coverage** | Spans ideation → planning → architecture → implementation → review |
| **Customizability** | Team and personal overrides without forking |
| **Context discipline** | Keeps the AI's working context lean (avoids overflow/drift) |
| **Human-in-the-loop** | Clear, well-placed checkpoints and blocking mechanisms |
| **Graceful degradation** | Falls back sensibly when a tool or sub-agent is unavailable |
| **Maintainability** | Updates, versioning, and backward compatibility |

---

## 4. Candidates

| Framework | Summary | Status | Profile |
| :--- | :--- | :--- | :--- |
| **BMAD-METHOD** | npm-installable framework that turns an AI IDE into a structured agile team of specialist agents; every capability is a Markdown skill, no runtime engine. | ✅ Documented | [View](bmad-method.md) |
| *Others* | Additional SDD frameworks to evaluate and profile here as the comparison grows. | ⏳ Pending | — |

> **As candidates are profiled, this table becomes the comparison surface** — each row links to a full analysis, and §3's criteria become the columns for a side-by-side once enough candidates exist.

---

## 5. Summary

1. **SDD makes the spec the source of truth** and the AI the implementer — the discipline is in the artifacts and workflow.
2. **NOMAD evaluates SDD frameworks** against setup effort, tool fit, lifecycle coverage, customizability, context discipline, human-in-the-loop control, graceful degradation, and maintainability.
3. **BMAD-METHOD is the first documented candidate**; see its [profile](bmad-method.md) for a full architecture analysis.
4. **This hub is the canonical entry point** for the topic — add new candidates as profiles and link them from the table above rather than duplicating overview content.
</content>
