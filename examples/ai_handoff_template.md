# AI Handoff Template

Use this template when passing work to an AI coding agent or from one AI-assisted step to another.

The goal is to make the next action clear, safe, and reviewable.

## Template

### Purpose

Describe the goal of the task.

Example:

- Create documentation for the approval workflow.
- Review backup verification rules.
- Prepare a safe proposal before modifying files.

### Target Files

List the files or folders the AI agent may inspect or change.

Allowed targets:

- 

Read-only targets:

- 

Do not touch:

- 

### Risks

List the risks the agent should consider before acting.

Possible risks:

- existing files may be overwritten
- backup may be missing
- approval may be required
- scope may be unclear
- generated output may be difficult to recreate
- user data may be sensitive

### Rules

List the rules the agent must follow.

Recommended rules:

- read before modifying
- explain planned changes before execution
- create or verify backups when required
- ask for approval before overwrite, delete, move, or rename
- do not change unrelated files
- do not change license, repository name, or public scope unless explicitly requested
- log completed actions

### Completion Conditions

Define what must be true when the task is complete.

Examples:

- target documentation file exists
- required sections are present
- no unrelated files were changed
- issue has a completion comment
- release notes mention the completed work

## Approval Block

Use this block when approval is required.

### Proposed Action

- 

### Affected Files

- 

### Backup Required

- yes / no

### Approval Status

- pending / approved / rejected / needs changes

### Approval Notes

- 

## Work Log Block

Use this block after the work is complete.

### Actions Completed

- 

### Files Created

- 

### Files Modified

- 

### Verification

- 

### Remaining Issues

- 

## Example Usage

### Purpose

Create a documentation file that explains backup verification.

### Target Files

Allowed targets:

- docs/backup_verification.md

Read-only targets:

- README.md
- docs/roadmap.md

Do not touch:

- LICENSE
- repository settings
- runtime scripts

### Risks

- The new document may imply automation that does not exist yet.
- The document must not change the project license or public scope.
- The workflow should remain beginner-friendly.

### Rules

- Create documentation only.
- Do not add runtime code.
- Explain hash verification as a concept only.
- Keep rollback steps human-approved.
- Log the completed file and verification result.

### Completion Conditions

- docs/backup_verification.md exists.
- Backup creation, timestamp check, hash check explanation, and rollback procedure are included.
- The related issue can be closed with a completion comment.

### Work Log

Actions completed:

- Created docs/backup_verification.md.
- Added backup creation check, timestamp check, hash explanation, and rollback procedure.

Files created:

- docs/backup_verification.md

Files modified:

- none

Verification:

- File exists on GitHub.
- Required sections are present.
- No runtime feature was added.
