from __future__ import annotations

from pydantic import BaseModel, Field

from squadron_sdk import Squadron

app = Squadron()
app.greeting = ""


@app.configure
def setup(settings: dict[str, str]) -> None:
    app.greeting = settings.get("greeting", "")


@app.tool
def ping() -> str:
    """Returns 'pong' when called."""
    return "pong"


@app.tool
def pong() -> str:
    """Returns 'ping' when called."""
    return "ping"


@app.tool
def echo(
    message: str = Field(..., description="The message to echo back"),
    all_caps: bool = False,
) -> str:
    """Echoes back the message provided, optionally capitalized."""
    out = message.upper() if all_caps else message
    return f"{app.greeting}{out}"


class AddResult(BaseModel):
    sum: int
    even: bool


@app.tool
def add(a: int, b: int) -> AddResult:
    """Add two integers and report whether the sum is even."""
    s = a + b
    return AddResult(sum=s, even=s % 2 == 0)


def main() -> None:
    app.serve()
