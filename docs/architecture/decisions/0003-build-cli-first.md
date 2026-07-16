# ADR 0003: Build a Command-line Interface First

## Status

Accepted

## Context

The platform will eventually require several interaction methods, potentially including a REST API, developer portal and GitOps-based request workflow.

A command-line interface provides a small and testable starting point for establishing the project's package structure, configuration, diagnostics and operational workflows.

## Decision

The first user-facing component will be an `eap` command-line interface.

The initial commands will be:

- `eap version`
- `eap info`
- `eap doctor`

Business and platform logic must remain separate from CLI presentation so that it can later be reused by APIs or other interfaces.

## Consequences

### Positive

- Provides an early working product.
- Establishes reusable application structure.
- Encourages separation between presentation and platform logic.
- Can support local development, troubleshooting and automation.
- Creates functionality that can later be exposed through other interfaces.

### Negative

- A CLI is not sufficient as the platform's eventual self-service interface.
- Command compatibility must be considered as the project evolves.
- Additional interfaces will require separate design decisions later.