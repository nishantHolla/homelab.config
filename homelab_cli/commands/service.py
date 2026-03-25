import os
from pathlib import Path
import yaml

import utils
from config import usage as u
from config import values as v
from utils.result import Result


def _load_secrets(service_name: str) -> tuple[Result, dict[str, str]]:
    SOPS_DIR = os.environ.get("HOMELAB_SOPS_DIR", None)
    if not SOPS_DIR:
        return (Result(1, "HOMELAB_SOPS_DIR env not set"), {})

    service_secret = v.SECRET_DIR / f"{service_name}.yaml"
    if not service_secret.is_file():
        return (
            Result(2, f"No secrets to load for service {service_name}"),
            os.environ.copy(),
        )

    env = os.environ.copy()
    env["SOPS_AGE_KEY_FILE"] = str(Path(SOPS_DIR) / "age" / "keys.txt")
    stdout, rc, stderr = utils.runner.run(
        "load_secrets",
        f"sops -d {service_secret}",
        capture=True,
        critical=False,
    )

    if rc != 0:
        return (
            Result(
                3,
                f"sops decryption for service {service_name} failed: {stderr}",
            ),
            {},
        )

    secrets = yaml.safe_load(stdout)
    env = os.environ.copy()
    for key, value in secrets.items():
        env[key] = value

    return (Result(0, "Ok"), env)


def up(args: list[str]) -> Result:
    if len(args) == 0:
        return Result(1, "Not enough args")

    service_name = args.pop(0)
    service_root = v.SERVICE_DIR / service_name

    if not service_root.is_dir():
        return Result(2, f"Service {service_name} not found")

    service_compose_file = service_root / "docker-compose.yml"

    if not service_compose_file.is_file():
        return Result(3, f"Service compose file for {service_name} not found")

    result, env = _load_secrets(service_name)
    if result.code not in [0, 2]:
        return Result(4, result.message)

    _, rc, stderr = utils.runner.run(
        "up",
        f"docker compose -f {service_compose_file} up -d",
        capture=False,
        critical=True,
        env=env,
    )
    if rc != 0:
        return Result(5, f"Failed to start service {service_name}: {stderr}")

    utils.io.info("up", f"Started service {service_name}")
    return Result(0, "Ok")


def up_all() -> Result:
    for item in v.SERVICE_DIR.iterdir():
        if not item.is_dir():
            continue

        result = up([str(item)])
        if result.code != 0:
            return result

    return Result(0, "Ok")


def down(args: list[str]) -> Result:
    if len(args) == 0:
        return Result(1, "Not enough args")

    service_name = args.pop(0)
    service_root = v.SERVICE_DIR / service_name

    if not service_root.is_dir():
        return Result(2, f"Service {service_name} not found")

    service_compose_file = service_root / "docker-compose.yml"

    if not service_compose_file.is_file():
        return Result(3, f"Service compose file for {service_name} not found")

    _, rc, stderr = utils.runner.run(
        "down",
        f"docker compose -f {service_compose_file} down",
        capture=False,
        critical=True,
    )
    if rc != 0:
        return Result(5, f"Failed to shutdown service {service_name}: {stderr}")

    utils.io.info("down", f"Shutdown service {service_name}")
    return Result(0, "Ok")


def down_all() -> Result:
    for item in v.SERVICE_DIR.iterdir():
        if not item.is_dir():
            continue

        result = down([str(item)])
        if result.code != 0:
            return result

    return Result(0, "Ok")


def run(args: list[str]) -> int:
    if len(args) == 0:
        utils.io.info("service", u.SERVICE_USAGE)
        return 1

    sub_command = args.pop(0)

    if sub_command == "help":
        utils.io.info("service", u.SERVICE_USAGE)
        return 0

    elif sub_command == "up":
        result = up_all() if len(args) == 0 else up(args)

        if result.code != 0:
            utils.io.error("up", result.message)

        return result.code

    elif sub_command == "down":
        result = down_all() if len(args) == 0 else down(args)

        if result.code != 0:
            utils.io.error("down", result.message)

        return result.code

    else:
        utils.io.error(
            "service",
            f"Unknown sub-command {sub_command}\n"
            "Run 'homelab service help' for list of all sub-commands",
        )
        return 1
