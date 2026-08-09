You are removing a task from the NOMAD project task list in `TASKS.md` at the project root. Removal is for tasks that are no longer relevant — finished work belongs in `/complete-task` instead.

The task to remove is: $ARGUMENTS

If no task was provided, ask the user which task to remove and stop.

---

## Steps

1. Read `TASKS.md` and find the task by ID (e.g., `T-002`), or by fuzzy-matching the description if no ID was given. Search both **Open** and **Done** sections. If the match is ambiguous, list the candidates and ask. If no match is found, say so and show the open tasks.
2. Show the exact line to the user and ask for confirmation before deleting.
3. After confirmation, remove the line from `TASKS.md`. Never reuse the freed ID for future tasks.
4. Confirm briefly what was removed. Do not commit to git — the user commits manually.
