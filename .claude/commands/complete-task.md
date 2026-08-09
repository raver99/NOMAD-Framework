You are marking a task as completed in the NOMAD project task list in `TASKS.md` at the project root.

The task to complete is: $ARGUMENTS

If no task was provided, ask the user which task to complete and stop.

---

## Step 1: Find the Task

Read `TASKS.md` and find the task in the **Open** section by ID (e.g., `T-002`), or by fuzzy-matching the description if no ID was given. If the match is ambiguous, list the candidates and ask. If no match is found, say so and show the open tasks.

---

## Step 2: Complete It

1. Move the line from **Open** to the end of the **Done** section.
2. Change `- [ ]` to `- [x]` and append the completion date, so the line reads:

   ```markdown
   - [x] **T-NNN** <Task title> *(<Category> — added <date>, completed <YYYY-MM-DD>)*
   ```

3. Remove the *(nothing completed yet)* placeholder from the **Done** section if it is still present.

---

## Step 3: Cross-Check the README

If the task was about writing a knowledge base document, check whether the README index has a matching entry — if the row still says *Coming soon* or is missing a link, point this out to the user. Do not silently edit the README; the `/add-knowledge` command owns that flow.

---

## Step 4: Report

Confirm briefly: the completed task's ID and title. Do not commit to git — the user commits manually.
