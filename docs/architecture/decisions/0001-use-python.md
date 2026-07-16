# ADR 0001: Use Python for Platform Tooling

## Status

Accepted

## Context

The Enterprise AI Platform requires tooling for command-line interaction, environment validation, API integration, automation and platform operations.

Python is widely used across DevOps, cloud automation, platform engineering and AI infrastructure. It also provides mature libraries for REST APIs, cloud SDKs, testing and command-line applications.

## Decision

Python will be the primary language for platform tooling and automation developed within this repository.

The project initially requires Python 3.13 or later.

## Consequences

### Positive

- Strong ecosystem for automation, cloud and AI tooling.
- Supports type hints and structured application development.
- Integrates well with REST APIs and cloud SDKs.
- Enables development of CLI tools, services and validation utilities.
- Provides transferable skills outside the VMware ecosystem.

### Negative

- Contributors require a compatible Python installation.
- Dependency and virtual-environment management must be maintained.
- Some infrastructure components may still require other languages or configuration formats.