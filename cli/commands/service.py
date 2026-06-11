import os
from pathlib import Path
from typing import List

import typer
import utils
import yaml
from config import values as v
from utils import completion
from utils.result import Err, Ok, Result

app = typer.Typer(help=v.SERVICE_TYPER_HELP)


def _load_secrets(service_name: str) -> Result[dict[str, str], str]:
    if not v.SOPS_DIR:
        return Err("HOMELAB_SOPS_DIR env not set")

    service_secret = v.SECRET_DIR / f"{service_name}.yaml"
    if not service_secret.is_file():
        return Ok(os.environ.copy())

    env = os.environ.copy()
    env["SOPS_AGE_KEY_FILE"] = str(Path(v.SOPS_DIR) / "age" / "keys.txt")
    stdout = utils.runner.run(
        f"sops -d {service_secret}", capture=True, critical=True
    ).unwrap()  # Safe to unwrap because critical is True

    secrets = yaml.safe_load(stdout)
    env = os.environ.copy()
    for key, value in secrets.items():
        env[key] = value

    return Ok(env)


@app.command(help=v.SERVICE_TYPER_HELP["up"])
def up(
    service_name: str = typer.Argument("", shell_complete=completion.complete_services),
):
    if service_name == "":
        utils.io.error("Error: Service name not provided")
        exit(1)

    service_root = v.SERVICE_DIR / service_name

    if not service_root.is_dir():
        utils.io.error(f"Service {service_name} not found")
        exit(1)

    service_compose_file = service_root / "docker-compose.yml"

    if not service_compose_file.is_file():
        utils.io.error(
            f"Service compose file for {service_name} not found at {service_compose_file}"
        )
        exit(1)

    result = _load_secrets(service_name)
    match result:
        case Err(e):
            utils.io.error(f"Failed to load secrets. Error: {e}")
            exit(1)

    env = result.unwrap()
    utils.runner.run(
        f"docker compose -f {service_compose_file} up",
        capture=False,
        critical=True,
        env=env,
    )

    utils.io.info(f"Started service {service_name}")
    exit(0)


@app.command(help=v.SERVICE_TYPER_HELP["down"])
def down(
    service_name: str = typer.Argument("", shell_complete=completion.complete_services),
):
    if service_name == "":
        utils.io.error("Error: Service name not provided")
        exit(1)

    service_root = v.SERVICE_DIR / service_name

    if not service_root.is_dir():
        utils.io.error(f"Service {service_name} not found")
        exit(1)

    service_compose_file = service_root / "docker-compose.yml"

    if not service_compose_file.is_file():
        utils.io.error(f"Service compose file for {service_name} is not found")

    utils.runner.run(
        f"docker compose -f {service_compose_file} down", capture=False, critical=True
    )

    exit(0)


@app.command(name="list", help=v.SERVICE_TYPER_HELP["list"])
def list_services():
    services = utils.docker_handler.get_service_info()
    table: List[List[str]] = [["Servie", "Status"]]

    for service in services:
        row = [service["name"], service["status"]]
        table.append(row)

        for container in service["containers"]:
            row = [(" " * 4) + container["name"], container["status"]]
            table.append(row)

    utils.io.table(table)
