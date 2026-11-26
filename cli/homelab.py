#!/usr/bin/env python

import typer
from config import values as v
from commands import service, rpios

app = typer.Typer(help=v.HOMELAB_TYPER_HELP_STR, rich_markup_mode=None)
app.add_typer(service.app, name="service")
app.add_typer(rpios.app, name="rpios")

if __name__ == "__main__":
    app()
