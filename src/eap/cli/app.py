"""Enterprise AI Platform command-line application."""

import typer

app = typer.Typer(
    name="eap",
    help="Enterprise AI Platform command-line interface.",
)


@app.callback()
def main() -> None:
    """Enterprise AI Platform command-line interface."""