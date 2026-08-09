You are listing the NOMAD project task list from `TASKS.md` at the project root.

Optional filter: $ARGUMENTS

---

## Steps

1. Read `TASKS.md`. If it does not exist or the **Open** section is empty, tell the user there are no open tasks and suggest `/add-task`.
2. Show the **Open** tasks as they appear in the file. If a filter was given (e.g., a category like `Testing` or a keyword), show only matching tasks and say which filter was applied.
3. If the input is `done` or `all`, also show the **Done** section. Otherwise leave completed tasks out.
4. End with a one-line count summary (e.g., "5 open, 3 done").

Do not modify the file.
