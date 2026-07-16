# Development Workflow

## Purpose

This document defines the lightweight development workflow used for the Enterprise AI Platform.

The goal is to maintain clear history, consistent delivery and good engineering practices without introducing unnecessary process overhead.

## Workflow

Each change should follow this lifecycle:

1. Select or create a GitHub issue.
2. Assign the issue to the appropriate milestone.
3. Create a branch from the latest version of `main`.
4. Implement and validate the change.
5. Commit the change using Conventional Commits.
6. Push the branch to GitHub.
7. Open a pull request into `main`.
8. Link the pull request to the relevant issue.
9. Merge the pull request when the acceptance criteria are satisfied.
10. Delete the merged local and remote branches.

## Starting Work

Always begin from an up-to-date `main` branch:

~~~bash
git switch main
git pull
~~~

Create a new branch for the issue:

~~~bash
git switch -c <type>/<short-description>
~~~

Examples:

~~~text
docs/document-development-workflow
feat/add-version-command
fix/correct-version-output
test/add-cli-tests
refactor/simplify-cli-structure
~~~

## Branch Naming

Branches should use the following format:

~~~text
<type>/<short-description>
~~~

Recommended branch types:

- `docs` — documentation changes
- `feat` — new functionality
- `fix` — defect corrections
- `test` — test-related changes
- `refactor` — internal restructuring without changing behaviour
- `chore` — maintenance and configuration
- `ci` — continuous integration changes

Branch names should:

- use lowercase
- use hyphens between words
- be concise
- describe the intended change

## Commit Messages

Commits should follow the Conventional Commits format:

~~~text
<type>: <description>
~~~

Examples:

~~~text
docs: document development workflow
feat: add version command
fix: handle missing configuration
test: add CLI version tests
refactor: separate CLI and platform logic
chore: update Ruff configuration
ci: add Python validation workflow
~~~

Commit messages should be concise, written in the imperative mood and describe one logical change.

## Validation

Before committing, run the relevant local checks.

For the current Python project:

~~~bash
ruff check .
~~~

Additional test and build commands will be added as the platform evolves.

## Pull Requests

Each pull request should:

- have a clear title
- summarise the change
- explain how it was validated
- reference the relevant issue
- contain only related changes
- target the `main` branch

Use a closing keyword in the pull-request description when the merge should close the issue automatically:

~~~text
Closes #5
~~~

Other supported keywords include:

~~~text
Fixes #5
Resolves #5
~~~

## Merge Strategy

Use squash merging unless there is a specific reason to preserve the individual commits.

The final squash commit should follow the Conventional Commits format.

## After Merge

Update the local repository:

~~~bash
git switch main
git pull
~~~

Delete the merged local branch:

~~~bash
git branch -d <branch-name>
~~~

If GitHub did not automatically delete the remote branch:

~~~bash
git push origin --delete <branch-name>
~~~

## Principles

- Keep the process lightweight.
- Prefer small, focused issues and pull requests.
- Keep `main` in a usable state.
- Document significant architectural decisions through ADRs.
- Let engineering practices support learning rather than obstruct it.