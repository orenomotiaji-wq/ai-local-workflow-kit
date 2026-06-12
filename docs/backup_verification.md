# Backup Verification

This document describes how AI Local Workflow Kit thinks about backup verification before modifying important local files.

The goal is to make file changes recoverable. Before an AI-assisted workflow overwrites or changes important files, the user should be able to confirm that a backup exists and can be identified later.

## Overview

Backup verification has four parts:

1. Confirm that a backup was created
2. Confirm the backup timestamp
3. Optionally confirm file integrity with a hash
4. Keep a rollback path visible

This document is guidance only. It does not add automation or runtime behavior.

## 1. Backup Creation Check

Before modifying an existing file, confirm whether a backup is required.

A backup is usually required when:

- an existing file will be overwritten
- an important document will be modified
- generated assets will be replaced
- the change is hard to recreate manually
- the user may need to compare before and after states

A backup record should include:

- original file path
- backup file path
- time created
- reason for backup
- planned modification

## 2. Timestamp Check

A timestamp helps confirm that the backup was created for the current operation, not an older unrelated change.

A good timestamp check answers:

- Was the backup created before the modification?
- Is the backup recent enough for this task?
- Does the backup timestamp match the current workflow log?
- Can the user identify which backup belongs to which operation?

Recommended timestamp format:

`YYYY-MM-DD_HH-MM-SS`

Example backup filename:

`report.md.backup-2026-06-12_21-40-00`

## 3. Hash Check Explanation

A hash is a short fingerprint generated from file contents.

Hash checks can help confirm that:

- the backup content did not change after it was created
- two files are identical or different
- the user can verify backup integrity later

Common hash types include SHA-256 and SHA-1. SHA-256 is generally preferred for integrity checks.

This repository does not require a specific hash tool yet. At this stage, hash verification is documented as a recommended safety concept, not an implemented feature.

A hash record may include:

- original file hash before modification
- backup file hash
- modified file hash after execution
- timestamp of the hash check

## 4. Rollback Procedure

Rollback means returning to a known safe previous state.

A basic rollback procedure should include:

1. Stop further modifications.
2. Identify the affected file.
3. Identify the correct backup file.
4. Compare timestamps and, if available, hashes.
5. Restore the backup to the original location or copy it to a safe review location.
6. Log the rollback action.
7. Re-check the restored file.

Rollback should be explicit. AI agents should not silently restore or overwrite files unless the user approves the rollback action.

## Backup Verification Checklist

Use this checklist before modifying important files:

- [ ] Target file is identified
- [ ] Modification purpose is clear
- [ ] Backup requirement is decided
- [ ] Backup file path is recorded
- [ ] Backup timestamp is recorded
- [ ] Hash check is considered, if integrity matters
- [ ] Rollback path is known
- [ ] User approval is recorded before modification

## Example Backup Record

Task: Update project documentation.

Target file:

- docs/example.md

Backup required:

- yes, because the file already exists and will be overwritten

Backup file:

- backups/docs/example.md.backup-2026-06-12_21-40-00

Timestamp:

- 2026-06-12 21:40:00 JST

Hash check:

- optional for this documentation-only change

Rollback path:

- copy the backup file back to docs/example.md after user approval

Approval:

- approved before modification

## Logging Backup Status

After backup verification, the workflow log should state:

- whether backup was required
- whether backup was created
- backup location
- timestamp
- hash status, if used
- rollback note

Example log:

`Backup verified: docs/example.md backed up to backups/docs/example.md.backup-2026-06-12_21-40-00 before modification. Hash check not used. Rollback is available by restoring the backup file with user approval.`

## Current Status

Backup verification is currently documented as a workflow requirement.

Future work may add examples or scripts, but any automation should preserve the same safety expectations:

- show targets before action
- verify backup before modification
- require approval before overwrite or rollback
- log the result
