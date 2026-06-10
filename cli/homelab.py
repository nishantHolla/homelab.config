#!/usr/bin/env python

import typer
from config import usage
from commands import nixos

app = typer.Typer(help=usage.HOMELAB_USAGE)
app.add_typer(nixos.app, name="nixos")

if __name__ == "__main__":
    app()
