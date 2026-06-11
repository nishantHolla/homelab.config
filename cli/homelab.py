#!/usr/bin/env python

import typer
from config import values as v
from commands import nixos, service

app = typer.Typer(help=v.HOMELAB_TYPER_HELP)
app.add_typer(nixos.app, name="nixos")
app.add_typer(service.app, name="service")

if __name__ == "__main__":
    app()
