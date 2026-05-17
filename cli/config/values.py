from pathlib import Path

## Paths

HOMELAB_CLI_DIR = Path(__file__).parent.parent
HOMELAB_DIR = HOMELAB_CLI_DIR.parent

NIXOS_DIR = HOMELAB_DIR / "nixos"
NIXOS_TEMPLATE_DIR = NIXOS_DIR / "template"
NIXOS_FLAKE_FILE = NIXOS_DIR / "flake.nix"

SERVICE_DIR = HOMELAB_DIR / "service"
SECRET_DIR = HOMELAB_DIR / "secrets"
