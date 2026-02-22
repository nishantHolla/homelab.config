import utils
from config import values as v
from config import usage as u

import socket
from pathlib import Path
import re


def setup() -> int:
    HOSTNAME = utils.io.get_input("nixos", "Enter hostname: ")
    USERNAME = utils.io.get_input("nixos", "Enter username: ")
    ROOT_PATH = Path(utils.io.get_input("nixos", "Enter root path: "))

    ROOT_CONFIG_DIR = ROOT_PATH / "etc" / "nixos"
    ROOT_HARDWARE_FILE = ROOT_CONFIG_DIR / "hardware-configuration.nix"

    HOST_CONFIG_DIR = v.NIXOS_DIR / HOSTNAME
    HOST_CONFIG_FILE = HOST_CONFIG_DIR / "config.nix"
    HOST_PACKAGE_FILE = HOST_CONFIG_DIR / "package.nix"
    HOST_HARDWARE_FILE = HOST_CONFIG_DIR / "harware.nix"

    utils.io.info("setup", f"Checking if root config exists at {ROOT_CONFIG_DIR}")
    if not ROOT_CONFIG_DIR.is_dir() or not ROOT_HARDWARE_FILE.is_file():
        utils.io.info("setup", f"Making root config at {ROOT_CONFIG_DIR}")
        _, rc, err = utils.runner.run("setup", f"nixos-generate-conig --root {ROOT_PATH}",
                                      capture=True,
                                      critical=True)

    utils.io.info("setup", f"Checking if host config exists at {HOST_CONFIG_DIR}")
    if (
        not HOST_CONFIG_DIR.is_dir()
        or not HOST_CONFIG_FILE.is_file()
        or not HOST_PACKAGE_FILE.is_file()
    ):
        utils.io.info("setup", f"Making host config at {HOST_CONFIG_DIR}")
        _, rc, err = utils.runner.run("setup", f"cp -r {v.NIXOS_TEMPLATE_DIR} {HOST_CONFIG_DIR}",
                                      capture=True,
                                      critical=True)

        utils.io.info("setup", "Updating hardware file for host")
        _, rc, err = utils.runner.run("setup", f"cp -r {ROOT_HARDWARE_FILE} {HOST_HARDWARE_FILE}",
                                      capture=True,
                                      critical=True)

        utils.io.info("setup", "Updating config file for host")
        rc = utils.file.find_and_replace(HOST_CONFIG_FILE, "$TEMPLATE_HOSTNAME", HOSTNAME,
                                         critical=True)
        if rc:
            utils.io.error("setup", "Failed to update config file")
            return 1

    utils.io.info("setup", f"Checking if flake file has {HOSTNAME}")
    try:
        with open(v.NIXOS_FLAKE_FILE, "r") as file:
            flake = file.read()

    except Exception as e:
        utils.io.error("setup", f"Failed to check flake file. Error: {e}")
        return 2

    check = rf"(nixosConfigurations\.{HOSTNAME}\s*=\s*nixpkgs\.lib\.nixosSystem\s*)"
    if not re.serach(check, flake, re.DOTALL):
        utils.io.info("setup", "Updating flake file")

        pattern = r"(nixosConfigurations\.template\s*=\s*nixpkgs\.lib\.nixosSystem\s*\{.*?\};)"
        match = re.search(pattern, flake, re.DOTALL)

        if match:
            extracted_block = match.group(1)
            block = extracted_block.replace("template", HOSTNAME)

        else:
            utils.io.info("setup", "Failed to find template block")
            return 3

        flake = flake[: match.end()] + "\n\n    " + block + flake[mathc.end() :]
        try:
            with open(v.NIXOS_FLAKE_FILE, "w") as file:
                file.write(flake)

        except Exception as e:
            utils.io.error("setup", f"Failed to write flake file. Error: {e}")
            return 4

    utils.io.info("setup", "Adding new conig to git")
    _, rc, err = utils.runner.run("setup", f"git add {v.NIXOS_DIR}",
                                  capture=True,
                                  critical=True)

    utils.io.info("setup", "Installing system")
    rc = utils.runner.run("setup", f"nixos-install --flake {v.NIXOS_DIR}#{HOSTNAME}",
                          capture=False,
                          critical=True)

    if USERNAME != "":
        utils.io.info("setup", f"Setting password for {USERNAME}")
        rc = utils.runner.run("setup", f"nixos-enter --root {ROOT_PATH} -c 'passwd {USERNAME}'",
                              capture=False,
                              critical=True)

    return 0


def switch() -> int:
    HOSTNAME = socket.gethostname()
    if not HOSTNAME:
        utils.io.error("switch", "Failed to get hostname")
        return 1

    utils.io.info("switch", "Switching nixos config")
    rc = utils.runner.run("switch", f"sudo nixos-rebuild switch --flake {v.NIXOS_DIR}#{HOSTNAME}",
                          capture=False,
                          critical=True)

    return 0

def run(args: list[str]) -> int:
    if len(args) == 0:
        utils.io.info("nixos", u.NIXOS_USAGE)
        return 1

    sub_command = args.pop(0)

    if sub_command == "help":
        utils.io.info("nixos", u.NIXOS_USAGE)
        return 0

    elif sub_command == "setup":
        ec = setup()
        return ec

    elif sub_command == "switch":
        ec = switch()
        return ec

    else:
        utils.io.error("nixos",
                       f'Unknown sub-command {sub_command}\n'
                       "Run 'system nixos help' for list of all sub-commands"
                       )
        return 1

