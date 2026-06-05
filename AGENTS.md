# AGENTS.md

## Safety rules for AI agents

AI agents working in this repository must follow these rules.

## Allowed without confirmation

- Read files
- Analyze files
- Create reports
- Create logs
- Create backups
- Suggest changes
- Create new files inside reports, logs, examples, or drafts folders

## Requires confirmation

- Editing existing source files
- Overwriting files
- Renaming files
- Moving files
- Installing dependencies

## Prohibited unless explicitly approved

- Deleting files
- Mass replacement across many files
- Sending files to external services
- Reading secret files
- Accessing credentials
- Modifying files outside the project directory

## Required workflow

Before editing:

1. Inspect the target file
2. Explain the planned change
3. Create a backup
4. Apply the minimum required change
5. Save a work log
6. Report what changed

## Completion checklist

- Backup created
- Work log saved
- No unrelated files changed
- No secrets included
- User can understand what happened
