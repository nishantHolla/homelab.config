import re
import socket
from pathlib import Path

import typer
import utils
from config import values as v
from utils.result import Err, Ok, Result

app = typer.Typer(help=v.NIXOS_TYPER_HELP)

### Command Functions ###


def setup_nixos() -> Result[None, str]:
    if not Path("/etc/NIXOS").exists():
        confirm = utils.io.get_confirmation(
            "Detected that this is not an installation environment. Do you still want to run the 'setup' command?"
        )

        if not confirm:
            return Ok(None)

    HOSTNAME = utils.io.get_input("Enter hostname: ")
    USERNAME = utils.io.get_input("Enter username: ")
    ROOT_PATH = Path(utils.io.get_input("Enter root path: "))

    if not ROOT_PATH.is_dir():
        return Err(f"Root path {ROOT_PATH} not found")

    ROOT_CONFIG_DIR = ROOT_PATH / "etc" / "nixos"
    ROOT_HARDWARE_FILE = ROOT_CONFIG_DIR / "hardware-configuration.nix"

    HOST_CONFIG_DIR = v.NIXOS_DIR / HOSTNAME
    HOST_CONFIG_FILE = HOST_CONFIG_DIR / "config.nix"
    HOST_PACKAGE_FILE = HOST_CONFIG_DIR / "package.nix"
    HOST_HARDWARE_FILE = HOST_CONFIG_DIR / "hardware.nix"

    utils.io.info(f"Checking if root config exists at {ROOT_CONFIG_DIR}")
    if not ROOT_CONFIG_DIR.is_dir() or not ROOT_HARDWARE_FILE.is_file():
        utils.io.info(f"Root config not found. Making root config at {ROOT_CONFIG_DIR}")
        utils.runner.run(
            f"nixos-generate-config --root {ROOT_PATH}", capture=True, critical=True
        )

    utils.io.info(f"Checking if host config exists at {HOST_CONFIG_DIR}")
    if not HOST_CONFIG_DIR.is_dir():
        utils.io.info(f"Host config not found. Making host config at {HOST_CONFIG_DIR}")
        utils.runner.run(
            f"cp -r {v.NIXOS_TEMPLATE_DIR} {HOST_CONFIG_DIR}",
            capture=True,
            critical=True,
        )

        utils.io.info("Updating hardware file for host")
        utils.runner.run(
            f"cp -f {ROOT_HARDWARE_FILE} {HOST_HARDWARE_FILE}",
            capture=True,
            critical=True,
        )

        utils.io.info("Updating config file for host")

        machine_id = utils.runner.run(
            "head -c 8 /etc/machine-id", capture=True, critical=True
        ).unwrap()  # Safe to unwrap because critical is True

        result = utils.file.find_and_replace(
            HOST_CONFIG_FILE, "$TEMPLATE_NETWORK_HOST_ID", machine_id
        )

        match result:
            case Err(e):
                return Err(f"Failed to update config file. Error: {e}")

        result = utils.file.find_and_replace(
            HOST_CONFIG_FILE, "$TEMPLATE_HOSTNAME", HOSTNAME
        )

        match result:
            case Err(e):
                return Err(f"Failed to update config file. Error: {e}")

        result = utils.file.find_and_replace(
            HOST_CONFIG_FILE, "$TEMPLATE_USERNAME", USERNAME
        )

        match result:
            case Err(e):
                return Err(f"Failed to update config file. Error: {e}")

    utils.io.info(f"Checking if flake file has {HOSTNAME}")
    try:
        with open(v.NIXOS_FLAKE_FILE, "r") as file:
            flake = file.read()

    except Exception as e:
        return Err(f"Failed to read flake file. Error: {e}")

    check = rf"(nixosConfigurations\.{HOSTNAME}\s*=\s*nixpkgs\.lib\.nixosSystem\s*)"
    if not re.search(check, flake, re.DOTALL):
        utils.io.info("Updating falke file")

        pattern = r"(nixosConfigurations\.template\s*=\s*nixpkgs\.lib\.nixosSystem\s*\{\s*##\s*--START--.*?\};)\s*##\s*--END--"
        match = re.search(pattern, flake, re.DOTALL)

        if match:
            extracted_block = match.group(1)
            block = extracted_block.replace("template", HOSTNAME)

        else:
            return Err("Failed to find template block")

        flake = flake[: match.end()] + "\n\n    " + block + flake[match.end() :]
        try:
            with open(v.NIXOS_FLAKE_FILE, "w") as file:
                file.write(flake)

        except Exception as e:
            return Err(f"Failed to write flake file. Error: {e}")

    utils.io.info("Adding new config to git")
    utils.runner.run(f"git add {v.NIXOS_DIR}", capture=True, critical=True)

    utils.io.info("Installing system")
    utils.runner.run(
        f"nixos-install --flake {v.NIXOS_DIR}#{HOSTNAME}", capture=False, critical=True
    )

    if USERNAME != "":
        utils.io.info(f"Setting password for {USERNAME}")
        utils.runner.run(
            f"nixos-enter --root {ROOT_PATH} -c 'passwd {USERNAME}'",
            capture=False,
            critical=True,
        )

    return Ok(None)


def switch_nixos() -> Result[None, str]:
    HOSTNAME = socket.gethostname()
    if not HOSTNAME:
        return Err("Failed to get hostname")

    utils.io.info("Switching nixos config")
    utils.runner.run(
        f"sudo nixos-rebuild switch --flake {v.NIXOS_DIR}#{HOSTNAME}",
        capture=False,
        critical=True,
    )

    return Ok(None)


### Sub Commands ###


@app.command(help=v.NIXOS_TYPER_HELP["setup"])
def setup():
    result = setup_nixos()
    match result:
        case Err(e):
            utils.io.error(e)
            exit(1)

    exit(0)


@app.command(help=v.NIXOS_TYPER_HELP["switch"])
def switch():
    result = switch_nixos()
    match result:
        case Err(e):
            utils.io.error(e)
            exit(1)

    exit(0)
