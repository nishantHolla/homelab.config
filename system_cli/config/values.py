from pathlib import Path

## Paths

SYSTEM_CLI_DIR = Path(__file__).parent.parent
SYSTEM_DIR = SYSTEM_CLI_DIR.parent

NIXOS_DIR = SYSTEM_DIR / "nixos"
NIXOS_TEMPLATE_DIR = NIXOS_DIR / "template"
NIXOS_FLAKE_FILE = NIXOS_DIR / "flake.nix"

SERVICE_DIR = SYSTEM_DIR / "service"
