import typer
from fastmcp import FastMCP
from typing_extensions import Annotated
from typing import Optional

from . import __version__

mcp = FastMCP("My MCP Server")


def version_callback(value: bool):
    if value:
        print(f"Mock MCP Server Version: {__version__}")
        raise typer.Exit()


def app(
    host: Annotated[str, typer.Option(help="Host to bind to")] = "localhost",
    port: Annotated[int, typer.Option(help="Port to bind to")] = 8000,
    _version: Annotated[
        Optional[bool],
        typer.Option("--version", callback=version_callback, help="Show version and exit"),
    ] = None,
):
    """Mock MCP Server for testing."""
    mcp.run()


@mcp.tool
def greet(name: str) -> str:
    return f"Hello, {name}!"


@mcp.resource("resource://greeting")
def get_greeting() -> str:
    """Provides a simple greeting message."""
    return "Hello from FastMCP Resources!"


@mcp.prompt
def ask_about_topic(topic: str) -> str:
    """Generates a user message asking for an explanation of a topic."""
    return f"Can you please explain the concept of '{topic}'?"


def main():
    typer.run(app)


if __name__ == "__main__":
    main()
