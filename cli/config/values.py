import os
from pathlib import Path


## Paths

HOMELAB_CLI_DIR = Path(__file__).parent.parent
HOMELAB_DIR = HOMELAB_CLI_DIR.parent

NIXOS_DIR = HOMELAB_DIR / "nixos"
NIXOS_TEMPLATE_DIR = NIXOS_DIR / "template"
NIXOS_FLAKE_FILE = NIXOS_DIR / "flake.nix"

SERVICE_DIR = HOMELAB_DIR / "service"
SECRET_DIR = HOMELAB_DIR / "secrets"

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

SERVICE_TYPER_HELP_STR = "Control services of the homelab"
SERVICE_TYPER_HELP = {
    "up": "Start a service",
    "down": "Stop a service",
    "list": "List all the services and their status",
    "logs": "Attach current shell to service logs",
}
