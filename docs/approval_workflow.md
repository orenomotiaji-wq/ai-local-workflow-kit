# Approval Workflow

This document defines the approval workflow used by AI Local Workflow Kit before modifying existing files.

The goal is simple: AI can read, analyze, and propose, but important file changes should happen only after a human understands and approves the action.

## Overview

The approval workflow has six stages:

1. Proposal
2. Review
3. Approval
4. Execution
5. Log saving
6. Follow-up

This workflow is intended for local-first AI work where files may contain important user data, project notes, generated assets, or business documents.

## 1. Proposal

Before modifying files, the AI agent should prepare a proposal.

The proposal should include:

- purpose of the change
- target files or folders
- expected result
- files that may be overwritten or created
- backup requirement
- risks and assumptions
- completion condition

The proposal should be specific enough that a user can decide whether the change is safe.

## 2. Review

The user or maintainer reviews the proposal before execution.

Review should check:

- whether the target files are correct
- whether the change matches the requested goal
- whether backups are required
- whether the operation could overwrite, delete, move, rename, or expose data
- whether the result can be verified after execution

If the proposal is unclear, the workflow should stop and request clarification.

## 3. Approval

The user explicitly approves, rejects, or delays the proposed action.

Approval should be recorded in plain language.

Recommended approval states:

- Approved: the proposed action may run
- Rejected: the proposed action must not run
- Needs changes: the proposal must be revised
- Deferred: the action is postponed

Approval should not be assumed from silence.

## 4. Execution

Execution should follow the approved proposal only.

During execution:

- do not expand scope without approval
- do not modify unrelated files
- do not perform destructive operations unless explicitly approved
- create or verify backups when required
- stop if the actual target differs from the proposal

If unexpected files, conflicts, or risks appear, the workflow should pause and return to review.

## 5. Log Saving

After execution, save or provide a log of what happened.

The log should include:

- action summary
- files read
- files created or modified
- backup status
- approval decision
- errors or warnings
- verification result
- remaining issues

Logs help users recover context and continue work later.

## 6. Follow-Up

After the action is complete, identify any remaining tasks.

Follow-up notes may include:

- files that still need review
- tests or checks not performed
- manual confirmation needed
- related issues to update or close

## Approval Example

### Proposal

Purpose: Update documentation for the approval workflow.

Target files:

- docs/approval_workflow.md

Planned action:

- create a new documentation file
- describe proposal, review, approval, execution, and logging steps

Risk:

- low, because this creates documentation and does not modify existing runtime code

Backup requirement:

- not required for a new documentation file

Completion condition:

- documentation exists in docs/approval_workflow.md
- related issue can be closed after verification

### User Decision

Approved.

Reason: The change is documentation-only, scoped to one new file, and does not affect runtime behavior.

### Execution Log

Action completed.

Files created:

- docs/approval_workflow.md

Files modified:

- none

Verification:

- file exists
- approval workflow sections are present
- no runtime code changed

## When Approval Is Required

Approval is required before:

- overwriting existing files
- deleting files
- moving or renaming files
- changing repository settings
- changing license or public scope
- running external communication or automation
- modifying generated assets that cannot be easily recreated

## When Approval May Be Lightweight

Approval may be lightweight for:

- creating a new documentation file
- adding an example template
- updating non-sensitive notes
- improving wording without changing project direction

Even lightweight approval should still be visible and recorded when part of an issue workflow.
