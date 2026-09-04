import os
from pathlib import Path


## Paths

HOMELAB_CLI_DIR = Path(__file__).parent.parent
HOMELAB_DIR = HOMELAB_CLI_DIR.parent

NIXOS_DIR = HOMELAB_DIR / "nixos"
NIXOS_TEMPLATE_DIR = NIXOS_DIR / "template"
NIXOS_FLAKE_FILE = NIXOS_DIR / "flake.nix"

RPIOS_DIR = HOMELAB_DIR / "rpios"
RPIOS_PACKAGES_LIST = RPIOS_DIR / "packages.txt"
RPIOS_INSTALL_DIR = RPIOS_DIR / "install"

SERVICE_DIR = HOMELAB_DIR / "service"
CONFIG_DIR = HOMELAB_DIR / "config"
CONFIG_INDEX_FILE = CONFIG_DIR / "index.json"

SOPS_DIR = os.environ.get("HOMELAB_SOPS_DIR")

## Help

HOMELAB_TYPER_HELP_STR = "CLI for homelab"
HOMELAB_TYPER_HELP = {
    "nixos": "Control system-level configuration",
    "service": "Control services of the homelab",
}

NIXOS_TYPER_HELP_STR = "Control system-level configuration"
NIXOS_TYPER_HELP = {
    "setup": "Perform setup actions for the system",
    "switch": "Switch to new configuration by rebuilding using nixos",
}

RPIOS_TYPER_HELP_STR = "Control system-level configuration"
RPIOS_TYPER_HELP = {
    "setup": "Perform setup actions for the system",
    "link": "Setup symlinks for config",
    "unlink": "Teardown sysmlinks of config"
}

SERVICE_TYPER_HELP_STR = "Control services of the homelab"
SERVICE_TYPER_HELP = {
    "up": "Start a service",
    "down": "Stop a service",
    "list": "List all the services and their status",
    "logs": "Attach current shell to service logs",
}
