# What Skills Are For

We set out to build three skills for backlog management. Testing killed all three, and then two came
back for a reason that had nothing to do with why they were proposed. Both halves are worth writing
down: the first is the easiest mistake to make when adding capability to an AI-assisted project, and
the second exposed a gap in the rules we were using to judge it.

## The plan

A project needs somewhere to put work and somewhere to put ideas. The design settled quickly: one
Markdown file in the repository, an ID per item, status carried by which section a line sits in,
priority carried by position. The rules are in
[A Backlog That Lives in the Repository](../../KnowledgeBase/WorkingWithAI/backlog-in-the-repository.md).

The tooling seemed to follow. Three skills: `nomad-backlog-capture` for adding an item,
`nomad-backlog-status` for moving one between sections, `nomad-backlog-groom` for the periodic
review. Each had a plausible justification. Capture would carry the conventions — assign the next
free ID, check for duplicates, decide whether a hedged sentence is a task or an idea. Status would
enforce the small rules about dates and reasons. Groom would run the checklist nobody remembers.

Every one of those justifications was invented at a desk. Not one came from watching a model fail.

## The rule that stopped it

NOMAD's own [Skill Authoring Rules](../../KnowledgeBase/ClaudeCode/skill-authoring-rules.md) open
with a governing principle — *a test that cannot fail proves nothing* — and §2.1 states the practical
form: run the task without the skill first and write against the failures you observe. It calls
itself the highest-value rule in the document, on the grounds that most skills which fail to earn
their place instruct a model that was already behaving correctly.

Section 5.3 sharpens it into a prediction. A skill covering work the model can already do fails
twice: it will not reliably trigger, because the model only consults a skill for work it cannot
easily do alone, and it will not beat its baseline, because there was no gap to close.

So before writing anything, we ran the three operations with no skill available. Three agents, three
fresh contexts, one seeded backlog each — eight items in Now, an idea planted to duplicate what the
capture prompt would add, a deliberately ambiguous instruction in the status prompt. The requests
were the kind a person actually types, not clean specimens:

> *"ok so while we were doing the auth thing i realised we never handle the case where the refresh
> token expires while the app is backgrounded. also we should probably look at whether we even need
> our own session store. add these"*

## What happened

The capture run assigned `T-020` as the next free ID and noted it would not fill gaps, because the
file says IDs are never reused. It found the planted duplicate sitting in Ideas and refused to add a
second item for the same question. It put the new item in Now rather than Ideas, arguing that a
concrete unhandled case inside in-progress work is not a question to evaluate. It normalised a
rambled sentence into one line, tagged it consistently with its neighbours, and then observed
unprompted that Now had reached nine lines and it had demoted nothing to compensate.

That is the entire content of the skill we were going to write.

The status run drew an ambiguous instruction — "drop the analytics dashboard one" matched two items.
It reasoned that the other candidate *was* the Sentry item, so "Sentry covers it" could not refer to
itself, picked the right line, and then flagged its own inference as an inference and asked for a
second look.

The groom run was the one we expected to survive, and it was the most decisive result. It changed a
single line, then reported what it had deliberately not changed: two items in direct contradiction,
one committed and one an idea that would make the first unnecessary — which it declined to resolve,
because killing committed work in favour of an unvalidated idea is not an agent's call. It caught a
detail link pointing at a file that did not exist and left it rather than fabricating a stub. And it
noticed that Now was in exact ascending ID order, which means it had been appended to and never
prioritised, whatever the section header claimed.

That last observation was not on our checklist. The baseline found something the skill would have
missed.

## Why the file did the work

The seed backlog states its own format in its header: one line per item, IDs never reused, status is
the section and lives nowhere else. The agents read that and followed it.

This is the part worth generalising. **A well-designed artifact can carry the convention that would
otherwise have to be carried by a skill.** The knowledge has to live somewhere an agent will
encounter it, and a file the agent must open anyway is a better location than a skill it has to
decide to load. The file also serves people who install nothing, and it cannot fall out of sync with
itself.

Every gap the runs exposed was a gap in the file, not a missing skill. Whether tags survive an item
being dropped. Whether the Dropped section is ever pruned. Whether a checkbox stays ticked. Each was
fixed by editing the seed file, which improved the convention for every project that adopts it,
including those that install no tooling at all.

## What survived, and the rule that was missing

Two skills shipped: `/nomad-backlog-capture` and `/nomad-backlog-groom`, both marked
`disable-model-invocation: true`.

That looks like a reversal and is not one. The baseline test answers a specific question — *does this
close a gap in what the model can do?* — and for a skill the model chooses to load, that is the whole
question, because a skill covering easy work will not be loaded and would not help if it were. Set
`disable-model-invocation` and the routing decision disappears. The skill runs when a person types
its name, and the test stops being the only thing that matters.

What replaces it is a question the rules never asked: **does a person benefit from being able to name
this operation?**

Three things sit behind that, and none is visible to a baseline run. A named operation appears in
autocomplete, which is how someone finds out the project supports it — a convention living only in a
file is invisible until somebody opens the file. The list of skills teaches a new contributor what
this project expects to be done, which prose conveys only to whoever reads it. And a skill issues the
same request every session, where a person composing the prompt from memory issues a slightly
different one each time and gets slightly different work back.

That last point is where the baseline runs stop being an argument against and become an argument for.
They show the model performs well *given a good prompt*. A skill that supplies that prompt every time
is exactly the right shape for periodic work — nobody types "check for duplicates, contradictions,
stale ideas, broken detail links and whether Now is actually ordered" from memory.

None of this was in
[Skill Authoring Rules](../../KnowledgeBase/ClaudeCode/skill-authoring-rules.md). §5.2 already treated
`disable-model-invocation` skills as exempt from the description budget, but nothing said how to judge
whether one should exist, so §5.3 was being applied to skills it was never about. The rules now carry
§5.4 for the explicitly invoked case, along with its two consequences: trigger evals do not apply when
nothing routes, and names should take an action form, because the name is what gets typed rather than
a routing signal.

The exemption has a floor. A skill that fails the baseline test *and* the naming test is still
overhead — which is why nothing ships for marking an item done. "T-007 is done" is shorter than the
skill name would be.

## The limits

One round of three runs, on a small clean file with a worked example in every section. A file with
two hundred items, or one that has drifted for months, was not tested — and that is exactly where a
skill is most likely to start earning its place. The claim here is narrow: on a healthy file, the
model needs no skill.

The examples deserve their own caveat. The format was self-describing partly *because* every section
had a specimen in it, and the examples are the first thing a real project deletes. The seed file now
states its rules in prose for that reason, but the version that was tested is not the version that
shipped.

## The transferable part

The instinct that produced three skills was that a new capability needs new tooling. It is a strong
instinct and it is usually wrong in the same way: it encodes what the author imagines a model gets
wrong, and models are frequently better at the imagined weakness than at the thing nobody thought to
check.

Watching it fail first costs about ten minutes. In this case it emptied all three skills of the
content we had planned to put in them, produced a better file, and turned up a failure mode — the
append-only Now list — that no amount of desk design had surfaced. Two of the skills survived, but
they shipped nearly empty, doing a job nobody had articulated until the original one was taken away.
