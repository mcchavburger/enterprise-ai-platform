"""Allow the EAP CLI to be run with python -m eap."""

from eap.cli.app import app

if __name__ == "__main__":
    app()