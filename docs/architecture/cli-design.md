# Initial CLI Design

## Purpose

The `eap` command-line interface provides a consistent way to interact with and diagnose the Enterprise AI Platform.

The initial release establishes the CLI structure. Future releases will add commands for platform deployment, validation, configuration and operations.

## Commands

### `eap version`

Displays the application name and installed version.

Example output:

~~~text
Enterprise AI Platform
Version 0.1.0
~~~

### `eap info`

Displays basic information about the project and its current development status.

Example output:

~~~text
Enterprise AI Platform
Status: Under active development
Purpose: Self-service enterprise AI platform
~~~

### `eap doctor`

Checks whether the local development environment satisfies the platform prerequisites.

Initial checks:

- Python version
- Python executable
- Virtual environment
- Operating system
- Git availability and version

Example output:

~~~text
Python version: 3.13.7
Python executable: C:\enterprise-ai-platform\.venv\Scripts\python.exe
Virtual environment: Active
Operating system: Windows
Git: Available
~~~

Future checks will include:

- Docker
- Kubernetes
- Terraform
- Argo CD
- GPU availability

## Proposed Package Structure

~~~text
src/
└── eap/
    ├── __init__.py
    ├── cli.py
    ├── doctor.py
    └── version.py

tests/
├── test_cli.py
└── test_doctor.py
~~~

## Design Principles

- Commands should produce clear, concise output.
- Diagnostic checks should return actionable results.
- Platform-specific logic should remain separate from CLI presentation.
- Commands should be testable without invoking external infrastructure.
- New checks should be easy to add as the platform evolves.