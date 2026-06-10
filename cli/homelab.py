#!/usr/bin/env python

import typer
from config import usage

app = typer.Typer(help=usage.HOMELAB_USAGE)

if __name__ == "__main__":
    app()
