import typer
import json

import utils
from config import values as v
from utils.result import Err, Ok, Result

app = typer.Typer(help=v.RPIOS_TYPER_HELP_STR)

### Command Functions ###


def _unlink_config() -> Result[None, str]:
    if not v.CONFIG_INDEX_FILE.is_file():
        return Err(f"Index file for config not found at  {v.CONFIG_INDEX_FILE}")

    with open(v.CONFIG_INDEX_FILE, "r") as file:
        index = json.load(file)

    for value in index.values():
        DEST = utils.file.resolve_path(value)

        if not DEST.is_symlink():
            utils.io.warning(f"Destination {DEST} does not exists. Skipping")
        else:
            utils.io.info(f"Unlinking {DEST}")

    return Ok(None)


def _link_config(force=False) -> Result[None, str]:
    if not v.CONFIG_INDEX_FILE.is_file():
        return Err(f"Index file for config not found at  {v.CONFIG_INDEX_FILE}")

    with open(v.CONFIG_INDEX_FILE, "r") as file:
        index = json.load(file)

    for key, value in index.items():
        DEST = utils.file.resolve_path(value)
        SRC = utils.file.resolve_path(v.CONFIG_DIR / key)

        if DEST.exists():
            if force:
                result = utils.file.backup(DEST)
                match result:
                    case Ok(p):
                        utils.io.warning(f"{DEST} already exists. Moving it to {p}")
                    case Err(e):
                        utils.io.error(f"Failed to setup up symlink for {DEST}. {e}")
                        continue
            else:
                utils.io.warning(f"{DEST} already exists. Skipping linking")
                continue

        DEST.symlink_to(SRC)
        utils.io.info(f"Linking {DEST} to {SRC}")

    return Ok(None)


def setup_rpios() -> Result:
    utils.io.info("Installing base packages")
    packages = set()
    repos = set()

    with open(v.RPIOS_PACKAGES_LIST, "r") as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip()
        if line.startswith("#"):
            continue

        words = line.split(" ")
        if len(words) == 2:
            repos.add(words[0])
            packages.add(words[1])
        elif len(words) == 1:
            packages.add(words[0])
        else:
            return Err(f"Invalid packages.txt: {line}")

    package_str = " ".join(list(packages))
    utils.runner.run("sudo apt update", critical=True, capture=False)
    utils.runner.run(f"sudo apt install {package_str}", critical=True, capture=False)

    utils.io.info("Running all install scripts")
    for file in v.RPIOS_INSTALL_DIR.iterdir():
        if file.is_file() and file.suffix == ".sh":
            utils.runner.run(f"{file}", critical=True, capture=False)

    utils.io.info("Changing shell of user")
    utils.runner.run("chsh -s $(which zsh)", capture=False, critical=True)

    utils.io.info("Setting up config links")
    _link_config(force=True)

    return Ok(None)


### Sub Commands ###


@app.command(help=v.RPIOS_TYPER_HELP["setup"])
def setup():
    result = setup_rpios()
    match result:
        case Err(e):
            utils.io.error(e)
            exit(1)

    exit(0)


@app.command(help=v.RPIOS_TYPER_HELP["link"])
def link():
    result = _link_config()
    match result:
        case Err(e):
            utils.io.error(e)
            exit(1)

    exit(0)


@app.command(help=v.RPIOS_TYPER_HELP["unlink"])
def unlink():
    result = _unlink_config()
    match result:
        case Err(e):
            utils.io.error(e)
            exit(1)

    exit(0)
