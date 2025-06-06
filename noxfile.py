"""Nox configuration for running tests across multiple Python versions."""

import nox
from nox import Session

nox.options.default_venv_backend = "uv"


@nox.session(python=["3.10", "3.11", "3.12", "3.13"])
def tests(session: Session) -> None:
    """Run tests with pytest."""
    session.install("pytest", "jsonschema", ".")
    session.run("pytest")
