# Roadmap

This roadmap describes the direction of AI Local Workflow Kit as an OSS project.

The project is not focused on adding large features quickly. It is focused on making local-first AI workflows safer, clearer, easier to review, and easier to continue over time.

## Roadmap Principles

The roadmap follows these principles:

- safety before automation
- documentation before complexity
- small reusable patterns before large platforms
- human approval before file modification
- backup and logging before risky operations
- practical validation through real projects

## Short-Term Milestones

Short-term work focuses on making the foundation easier to use and verify.

### Milestone 1: Approval Workflows

Goal: document and standardize how users approve AI-proposed changes before files are modified.

Expected outcomes:

- clear approval checklist
- proposed-change review format
- approval and rejection recording guidance
- examples that separate analysis from execution

Completion signal:

- users can understand when approval is required and what they are approving

### Milestone 2: Backup Verification

Goal: define how backups should be checked before important modifications.

Expected outcomes:

- backup existence checks
- backup timestamp expectations
- simple backup status reporting
- recovery guidance for failed or unsafe changes

Completion signal:

- risky workflows clearly state whether backup verification is required and how to confirm it

### Milestone 3: AI Handoff Templates

Goal: provide reusable templates for passing work between humans and AI agents.

Expected outcomes:

- task purpose template
- target file and folder template
- constraints and safety rules template
- risk and unknowns section
- completion condition section

Completion signal:

- a new AI-assisted task can start with enough context to avoid unsafe assumptions

## Mid-Term Milestones

Mid-term work focuses on turning the safety foundation into a reusable local workflow engine.

### Milestone 4: Local-First AI Workflow Engine

Goal: define a repeatable workflow structure for local AI operations.

Expected outcomes:

- staged workflow model
- read, analyze, propose, approve, execute, log sequence
- reusable folder and report conventions
- safer defaults for local file operations

Completion signal:

- multiple projects can reuse the same workflow pattern without rewriting safety rules each time

### Milestone 5: Multi-Agent Coordination

Goal: document and test how multiple AI agents or AI-assisted steps can hand work to each other safely.

Expected outcomes:

- handoff rules between agents
- status and ownership tracking
- conflict and overwrite prevention guidance
- logs that explain which agent or step did what

Completion signal:

- multi-step AI workflows remain understandable and recoverable

## Long-Term Milestone

Long-term work focuses on a safe operating layer for local AI systems.

### Milestone 6: Safe AI Operating Layer for Local AI Systems

Goal: provide a practical safety layer for local AI workflows that can be reused across projects.

Expected outcomes:

- consistent approval model
- backup and recovery expectations
- log and report conventions
- handoff templates
- safe defaults for local file workflows
- guidance for external communication and automation boundaries

Completion signal:

- local AI systems can operate with clear human oversight, visible logs, and recoverable file workflows

## Current Priorities

Current priorities are:

1. document architecture and validation projects
2. close documentation roadmap issues with concrete docs
3. improve approval, backup, and handoff examples
4. keep the project small, understandable, and safe

## Out of Scope for Now

The following are intentionally out of scope for the current stage:

- automatic destructive operations
- external API integrations without explicit design review
- background agents that modify files without approval
- complex infrastructure before the workflow model is proven
- license or public-scope changes

## Review Cadence

The roadmap should be reviewed when:

- a roadmap issue is completed
- a new validation project exposes a repeated safety need
- documentation becomes unclear or outdated
- a release changes how users understand the project direction
