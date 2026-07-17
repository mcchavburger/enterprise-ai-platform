# ADR 0004: Adopt Typer

## Status

Accepted

## Context

The Enterprise AI Platform requires a command-line interface that will become the primary interface for interacting with the platform during its early development.

The chosen framework should support a growing hierarchy of commands while remaining maintainable, testable and easy to extend.

Several frameworks were evaluated, including Python's built-in `argparse`, Click and Typer.

The project also aims to adopt modern Python development practices, including the use of type hints.

## Decision

The Enterprise AI Platform will use **Typer** to implement the `eap` command-line interface.

Typer provides a modern, type-hint-driven interface while building upon the mature Click framework.

The CLI will remain a presentation layer only.

Business logic, configuration handling and platform functionality must remain independent from Typer so that they can later be reused by other interfaces, such as REST APIs, web applications or automation services.

## Consequences

### Positive

- Provides a modern, easy-to-maintain CLI framework.
- Encourages the use of Python type hints throughout the project.
- Supports nested command groups as the platform grows.
- Produces consistent help output and shell completion.
- Keeps presentation separate from reusable platform logic.
- Allows the CLI to evolve without tightly coupling the platform to the framework.

### Negative

- Introduces an additional third-party dependency.
- Future framework changes would require changes to the CLI layer.
- Contributors unfamiliar with Typer may require a short learning period.