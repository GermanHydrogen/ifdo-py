import nox
from nox_poetry import session

nox.options.default_venv_backend = "uv"

@session(python=["3.10", "3.11", "3.12", "3.13"])
def tests(session):
    session.install("pytest", "jsonschema", ".")
    session.run("pytest")
