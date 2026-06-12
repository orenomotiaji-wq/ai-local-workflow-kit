# Contributing to AI Local Workflow Kit

Thank you for your interest in improving AI Local Workflow Kit.

This project focuses on safe, local-first AI-assisted workflows. Contributions should improve clarity, reliability, safety, documentation, or maintainability without adding unnecessary complexity.

## Issue Rules

Before opening an issue, please check whether a similar issue already exists.

Use issues for:

- bugs or unclear behavior
- documentation improvements
- roadmap or enhancement proposals
- safety, backup, approval, or logging workflow gaps

A good issue should include:

- the goal or problem
- expected behavior
- current behavior, if relevant
- affected files or documentation sections, if known
- risks or safety concerns
- completion conditions

Please avoid broad, unrelated requests in a single issue. Smaller issues are easier to review and maintain.

## Pull Request Rules

Pull requests should be small, focused, and easy to review.

Before opening a pull request:

- explain the purpose clearly
- describe the files changed
- mention any safety or compatibility impact
- confirm that no unrelated functionality was added
- confirm that existing project philosophy was preserved

Pull requests should not include:

- unrelated feature additions
- license changes
- repository renames
- public scope changes
- destructive automation without clear approval and rollback guidance

## Documentation Update Rules

Documentation changes are welcome when they improve understanding, safety, or maintainability.

When updating documentation:

- preserve the local-first and safety-first philosophy
- keep language practical and beginner-friendly
- explain risks, approval points, backups, and logs when relevant
- avoid replacing existing intent unless the change is explicitly discussed
- prefer examples that are safe and easy to verify

## Commit Rules

Use clear, focused commit messages.

Recommended examples:

- Add issue templates
- Document contribution rules
- Improve security reporting policy
- Update roadmap documentation

Each commit should represent one understandable change. Avoid mixing documentation, workflow policy, and unrelated implementation changes in the same commit.

## Safety Expectations

This project treats destructive file operations, overwrites, automation, and external integrations as sensitive areas.

Changes that affect safety workflows should clearly describe:

- the operation being performed
- the affected files or data
- whether a dry run is available
- how backups are created or verified
- how users approve or reject the action
- how logs are saved
- how the user can recover
