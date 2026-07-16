# ADR 0002: Use Ruff for Python Code Quality

## Status

Accepted

## Context

The project requires consistent formatting, linting and import organisation.

Traditional Python projects commonly combine several tools, including Black, Flake8 and isort. Maintaining multiple overlapping tools adds configuration and dependency overhead.

## Decision

Ruff will be used as the primary Python linting and formatting tool.

Initial linting rules include:

- `E` — pycodestyle errors
- `F` — Pyflakes
- `I` — import sorting

The maximum line length is 100 characters.

## Consequences

### Positive

- Fast execution.
- One tool covers several code-quality responsibilities.
- Configuration is centralised in `pyproject.toml`.
- Simple to run locally and later within CI pipelines.

### Negative

- Some specialised checks may require additional tools later.
- Contributors unfamiliar with Ruff will need to learn its commands.
- Expanding the rule set may reveal existing violations that require remediation.