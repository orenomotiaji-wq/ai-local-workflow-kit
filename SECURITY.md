# Security Policy

AI Local Workflow Kit is focused on safer local-first AI-assisted workflows. Security reports are welcome, especially when they relate to file safety, backups, approval flows, logging, or unsafe automation patterns.

## Reporting a Security Issue

If you find a security issue, please do not open a public issue with sensitive details.

Instead, report the issue privately to the project maintainer through an appropriate private channel for the repository owner. If a private channel is not available, open a minimal public issue that says a security report is needed, without including exploit details, private data, credentials, or sensitive file paths.

A helpful report should include:

- a short summary of the concern
- affected files or workflow areas, if known
- steps to reproduce, when safe to share privately
- potential impact
- suggested mitigation, if available

## Vulnerability Response Policy

The maintainer will review security reports with priority based on risk and impact.

The expected response process is:

1. Confirm whether the report affects this repository.
2. Assess severity and affected scope.
3. Prepare a fix, documentation update, or mitigation guidance.
4. Avoid exposing sensitive details before users have a reasonable chance to respond.
5. Document the resolved behavior when appropriate.

Because this is an early public OSS project, response time may vary. Reports involving destructive operations, unsafe overwrite behavior, missing approval steps, backup failures, or sensitive local-file handling should be treated as higher priority.

## Supported Scope

This policy covers:

- repository documentation
- workflow templates
- backup, approval, logging, and handoff guidance
- example scripts or local workflow helpers included in this repository
- safety assumptions documented for AI-assisted local operations

This policy does not cover:

- third-party AI tools not maintained in this repository
- user-created workflows outside this repository
- unrelated infrastructure or accounts
- issues caused by disabling documented safety checks

## Safety Principles

Security fixes should preserve the project principles:

- read before modify
- backup before change
- human approval before overwrite
- log every action
- avoid destructive operations by default
