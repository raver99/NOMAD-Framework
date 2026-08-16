# 📋 A Backlog That Lives in the Repository – Tracking Work Without an External Tool

## Purpose of This Document

Projects outlive their first idea. Work arrives faster than it gets done, and the ideas worth
keeping tend to arrive when there is no bandwidth to act on them. This document defines how a
project tracks that work: one Markdown file in the repository, readable by a person and usable by an
AI agent without a plugin, an account or an export step. It covers the file, what belongs in each
section, the rules that keep it honest, and the two skills worth installing.

It is deliberately small. A project needs somewhere to put work and somewhere to put ideas; almost
everything a tracker adds beyond that is overhead a small project pays and never recovers.

---

## 1. Why the backlog belongs in the repository

An agent acts on what it can reach. A backlog held in an external tracker sits behind an API, a
login and a rate limit, so an agent either cannot read it or reads a stale copy someone remembered
to sync. A file in the repository is available to every agent with read access to the project, at
the moment it is needed, in its current state.

The file also inherits everything the repository already provides. It is versioned, so the history
of a decision is recoverable. It diffs in review, so a change to priorities is visible alongside the
change to the code. It branches, so work-in-progress planning does not disturb the main line. And it
survives the project changing tools, because there is nothing to migrate.

> **The backlog is context, not administration.** Anything an agent must be told before it can work
> is better stored where the agent already looks.

---

## 2. The file

A single `BACKLOG.md` at the project root, with a header that states its own format. Detail files,
where an item earns one, live in `backlog/` beside it.

The header matters more than it appears to. It is what lets an agent — or a new contributor — open
the file cold and follow the convention without being briefed, and it is what stops each agent
inventing a different format. The seed file in the `nomad-backlog` plugin carries the rules as prose
rather than relying on the example lines, because the examples are the first thing a real project
deletes.

---

## 3. The sections

Status is the section a line sits in. There are six.

| Section | Holds | Ordered |
|---------|-------|---------|
| **In progress** | What is being worked on right now. Usually one item, sometimes two, often none. | — |
| **Now** | Work intended next. | Yes — the top line is the next thing |
| **Later** | Work agreed on, with no claim about sequence. | No |
| **Ideas** | Uncommitted thoughts. No obligation attached. | No |
| **Done** | Finished work, with the date it finished. | No |
| **Dropped** | Decided against, with the reason. | No |

**In progress earns its place through agents rather than people.** A person knows what they were
doing. An agent starting a fresh session does not, and the single most useful thing to hand it is
what was in flight when the last session ended. The section only works if it is kept current; a
stale in-progress marker is worse than an empty section, because it is confidently wrong.

**Ideas has no readiness bar.** Promoting an idea to Now or Later is a judgment call and nothing
more. A gate here would be the first piece of process that exists for its own sake, and the cost of
a slightly under-formed item in Now is lower than the cost of ideas nobody bothers to capture.

---

## 4. One line per item

```markdown
- [ ] **T-012** Handle refresh-token expiry while the app is backgrounded `#auth`
- [ ] **T-008** Export user data as JSON for GDPR requests `#compliance` → [detail](backlog/T-008.md)
- [x] **T-003** Login screen redesign `#ui` (2026-08-04)
```

An ID, a title, an optional tag, and a link to a detail file when one exists. Closing dates go at the
end in `(YYYY-MM-DD)`.

IDs are assigned once and never reused, which makes them safe to cite in a commit message, a branch
name or a conversation. Gaps in the sequence carry no meaning — a dropped idea leaves one behind and
nothing should try to fill it.

Tags are free-form and travel with a line when it moves. No taxonomy is prescribed, because this
convention is used by projects that are not software and by projects small enough that a taxonomy
would be the largest thing in the file.

---

## 5. Status lives in exactly one place

The section holds the status. A detail file holds context and reasoning and carries no metadata —
no frontmatter, no status field, no priority.

Any field stored in two places eventually disagrees, and there are only two remedies. A sync ritual
depends on someone remembering, which is the failure mode being designed out. Generating one from
the other adds a build step to a Markdown file, and having an agent regenerate an index is both slow
and lossy. One location removes the problem rather than managing it.

The cost is real and small: open a detail file on its own and its state is not visible. In practice
detail files are reached through the backlog, so the state is already known.

✅ Change an item's state by moving its line.
❌ Record state anywhere other than the line's position.

---

## 6. Priority is position

Now is ordered and the top line is the next thing. There is no priority field.

Priority labels let everything be important. A field with three values reliably ends in a backlog of
fourteen high-priority items and no answer to what to do next, because marking something high costs
nothing and requires no comparison. Ordering forces the comparison, which is the part that produces
the decision.

Two honesty constraints keep this from becoming a fiction:

- **Ordering only means something near the top.** Nobody sorts the eighth item against the ninth,
  and a convention that claims otherwise trains people to ignore it.
- **Now is short.** If it does not fit on a screen it is not a Now list, and the surplus belongs in
  Later.

The act of prioritising is moving a line from Later into Now. It is visible in a diff and it is a
decision someone made, which a label change never quite is.

> A Now list in ascending ID order has been appended to and never prioritised. It is the most
> reliable sign the convention has stopped being used, and it is worth checking for.

---

## 7. When an item earns a detail file

Most items never do. An item gets `backlog/T-NNN.md` when there is reasoning to hold — a plan, a
rejected approach, constraints discovered along the way, open questions. The test is whether
something would be lost if it stayed unwritten, not whether the item feels significant.

There are no sub-items. Work that belongs inside another item goes in that item's detail file, where
it can be described properly, rather than becoming a second line that competes with its parent for
position and status.

To link two items, name the other ID in the title. That covers dependency, conflict and supersession
without a field for each.

---

## 8. What the file does not record

| Not recorded | Because |
|--------------|---------|
| The date an item was added | `git log` and `git blame` already date every line, and a typed date can be wrong |
| Epics, parents, dependencies | The point where this becomes a tracker. A sentence naming the other ID does the same work |
| Assignees | A project small enough for this convention does not need them; one large enough has a tracker |
| Estimates | They would be guesses recorded as data |

---

## 9. Dropped items are kept

Deleting a rejected item is the intuitive move and it is wrong. An agent has no memory of the
rejection, so the idea gets proposed again, evaluated again, and argued down again. One line —
*"T-014 Custom analytics dashboard — Sentry already covers it (2026-08-16)"* — ends that loop
permanently for every future session.

The section is never pruned. Its growth is the point. Boxes stay unticked, because the work was
never done and the section already says it is closed.

This is one of two places where the convention is shaped by agents rather than people, the other
being In progress (§3). A human-only backlog would not need either.

---

## 10. The skills

Three skills ship in the `nomad-backlog` plugin. All set `disable-model-invocation: true`, so an
agent never loads them on its own — they run when a person types their name.

| Skill | Use |
|-------|-----|
| `/nomad-backlog-setup` | Install the convention: seed file at the project root, section in `CLAUDE.md`. Run once |
| `/nomad-backlog-capture <thought>` | Add work or an idea. Reads the whole file first, so an existing item is pointed out rather than duplicated and a dropped one is raised rather than revived |
| `/nomad-backlog-groom` | Review the file. Fixes format drift and broken links; reports duplicates, contradictions, stale ideas and a Now list that has stopped being ordered |

Capture and groom exist for the person, not the model. Tested against the bare file with no skill
available, a model already assigns IDs correctly, catches duplicates and resolves ambiguous
instructions — so neither beats its baseline, and on the usual test neither would be written. The
value is elsewhere: an operation with a name appears in autocomplete, which is how someone discovers
the project supports it at all, and a named skill issues the same request every session instead of a
differently-worded one. A convention that exists only in a file is invisible until someone opens the
file.

Setup is the exception, and it earns its place the ordinary way. It has failure modes — overwriting
a backlog that already holds work, or adding the `CLAUDE.md` section twice so the project carries two
statements of one convention — and it runs once per project, which is precisely when nobody
remembers the steps.

That is a specific exemption rather than a loophole. It applies because these skills are never routed
by the model, which is what [Skill Authoring Rules](../ClaudeCode/skill-authoring-rules.md) §5.4
covers; §5.3 still governs anything a model can choose to load.

**There is no skill for marking an item done.** "T-007 is done" is already shorter than any skill
name for it, and a well-formed file gives an agent everything it needs to make the change correctly.
Naming an operation that is faster to describe than to invoke is overhead.

The runs behind all of this are written up in
[What Skills Are For](../../docs/articles/what-skills-are-for.md).

---

## 11. Adopting it

Install the plugin and run `/nomad-backlog-setup`. It copies the seed `BACKLOG.md` to the project
root and adds a short section to `CLAUDE.md`. It refuses to overwrite an existing backlog, and
refuses to add the section a second time — a project with two statements of one convention has the
drift this design exists to prevent.

By hand instead: copy the seed file to the project root, delete the example lines, and paste the
`CLAUDE.md` section from the plugin's `assets/CLAUDE-backlog-section.md`.

That section records facts — where the file is, that status is the line's position, that IDs are
never reused. It contains no instruction to behave a certain way, and adding one is a mistake worth
naming: an agent told to watch for things worth capturing interrupts constantly, gets tuned out, and
taxes every conversation in the project whether or not it touches the backlog.

Nothing else is required. A project that installs no skills still has a working backlog.

---

## 12. Limits of this guidance

- **Tested on a healthy file.** The baseline runs behind §10 used a small, clean backlog with a
  worked example in each section. A file with two hundred items, or one that has drifted for months,
  was not tested, and it is where a skill is most likely to start earning its place on capability
  rather than on discoverability.
- **Not yet dogfooded.** NOMAD tracks its own work with Mission Control work items and does not use
  this convention, so nothing here has been proven over a long project. The parts most exposed are
  the ones only use can settle: whether grooming is worth running, and whether Now and Later stay
  distinct in practice.
- **No external sources.** The design rests on this project's own testing and judgment rather than
  published research on backlog structure.

---

## 13. Summary

1. **The backlog is a file in the repository**, because an agent acts on what it can reach.
2. **One line per item**, with an ID that is never reused.
3. **The section is the status**, and it is the only place status lives.
4. **Priority is position in Now**, and Now is short.
5. **A detail file is earned**, not issued with every item.
6. **Dropped items stay**, or the next agent re-proposes them.
7. **Three explicitly invoked skills** — setup, capture, groom. Capture and groom are there to be
   discoverable rather than to instruct the model. Marking work done needs neither.

---

## References

This guide records the project's own design decisions and its own testing. Its factual basis is
three baseline runs performed on 2026-08-16, in which an agent was given a seeded backlog and an
unstructured request, with no command and no skill available; the runs and their results are
described in [What Skills Are For](../../docs/articles/what-skills-are-for.md).

No external sources were consulted. Claims about how backlogs degrade — priority-label inflation,
append-only Now lists, re-proposed rejected ideas — are this project's judgment from practice and
are not sourced.
