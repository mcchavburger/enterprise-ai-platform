# Contributing

Thank you for contributing to the Enterprise AI Platform.

This project uses a lightweight issue, branch and pull-request workflow.

## Local Setup

Clone the repository and create a Python virtual environment:

~~~bash
python -m venv .venv
source .venv/Scripts/activate
python -m pip install --upgrade pip
~~~

Install the project development dependencies as documented in `pyproject.toml`.

## Development Workflow

1. Select or create a GitHub issue.
2. Assign it to the appropriate milestone.
3. Create a branch from the latest `main`.
4. Implement and validate the change.
5. Commit using Conventional Commits.
6. Push the branch.
7. Open a pull request.
8. Link the pull request to the issue.
9. Merge once the acceptance criteria are satisfied.
10. Delete the merged branch.

Full guidance is available in:

~~~text
docs/development/workflow.md
~~~

## Branch Naming

Use:

~~~text
<type>/<short-description>
~~~

Examples:

~~~text
docs/add-contribution-templates
feat/add-version-command
fix/correct-version-output
test/add-cli-tests
~~~

## Commit Messages

Use Conventional Commits:

~~~text
<type>: <description>
~~~

Examples:

~~~text
docs: add contribution guidance
feat: add version command
fix: handle missing configuration
test: add CLI tests
~~~

## Validation

Run the relevant local checks before opening a pull request:

~~~bash
ruff check .
~~~

Additional test and build commands will be added as the platform evolves.

## Pull Requests

Pull requests should:

- contain one focused change
- have a clear summary
- explain how the change was validated
- link to the relevant issue
- target `main`

Use a closing keyword when the pull request should close an issue:

~~~text
Closes #123
~~~