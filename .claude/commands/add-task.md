You are adding a task to the NOMAD project task list in `TASKS.md` at the project root. Tasks track what is still to do in this project — mostly knowledge base topics to write, but also structural or tooling work.

The task to add is: $ARGUMENTS

If no task was provided, ask the user what the task is and stop.

---

## Step 1: Read the Task List

Read `TASKS.md`. If it does not exist, create it with this skeleton first:

```markdown
# 📋 NOMAD Task Tracking

Open tasks and ideas for the NOMAD project. Managed with the `/add-task`, `/list-tasks`, `/complete-task`, and `/remove-task` commands, but can also be edited by hand.

## Open

## Done

*(nothing completed yet)*
```

---

## Step 2: Prepare the Task

1. **ID**: Assign the next free ID. IDs are sequential in the form `T-NNN` (zero-padded, e.g., `T-004`). Scan both the **Open** and **Done** sections for the highest existing ID and increment it — never reuse an ID.
2. **Title**: Write a concise, action-oriented task title (start with a verb: "Write…", "Add…", "Evaluate…", "Restructure…"). Keep any useful detail from the user's input, but trim filler.
3. **Category**: Categorize using the README index categories (**Process**, **Implementation**, **Testing**, **DevOps**, **Claude Code**) or **Project** for meta/structural work. Use judgment; ask only if genuinely ambiguous.
4. **Duplicate check**: Look through the **Open** list for an existing task covering the same topic — if one exists, tell the user and ask whether to merge or add anyway instead of silently creating a duplicate.

---

## Step 3: Add the Task

Append the task to the end of the **Open** section in this exact format:

```markdown
- [ ] **T-NNN** <Task title> *(<Category> — added <YYYY-MM-DD>)*
```

---

## Step 4: Report

Confirm briefly: the new task's ID, title, and category. Do not commit to git — the user commits manually.
