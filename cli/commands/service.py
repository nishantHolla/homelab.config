import os
from pathlib import Path
from typing import List

import typer
import utils
import yaml
from config import values as v
from utils import completion
from utils.result import Err, Ok, Result

app = typer.Typer(help=v.SERVICE_TYPER_HELP_STR)

### Command Functions ###


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


def start_service(service_name: str, detach=False) -> Result[None, str]:
    if service_name == "":
        return Err("Service name not provided")

    service_root = v.SERVICE_DIR / service_name

    if not service_root.is_dir():
        return Err(f"Service {service_name} not found")

    service_compose_file = service_root / "docker-compose.yml"

    if not service_compose_file.is_file():
        return Err(
            f"Service compose file for {service_name} not found at {service_compose_file}"
        )

    result = _load_secrets(service_name)
    match result:
        case Err(e):
            return Err(f"Failed to load secrets. Error: {e}")

    env = result.unwrap()
    flags = ""
    if detach:
        flags += " -d"

    utils.runner.run(
        f"docker compose -f {service_compose_file} up {flags}",
        capture=False,
        critical=True,
        env=env,
    )

    utils.io.info(f"Started service {service_name}")
    return Ok(None)


def start_all_services() -> Result[None, str]:
    for service in utils.docker_handler.get_stopped_services():
        utils.io.info(f"Starting service {service}")
        result = start_service(service, detach=True)
        match result:
            case Err(e):
                return Err(e)

    return Ok(None)


def stop_service(service_name: str) -> Result[None, str]:
    if service_name == "":
        return Err("Service name is required")

    service_root = v.SERVICE_DIR / service_name

    if not service_root.is_dir():
        return Err(f"Service {service_name} not found")

    service_compose_file = service_root / "docker-compose.yml"

    if not service_compose_file.is_file():
        return Err(f"Service compose file for {service_name} is not found")

    utils.runner.run(
        f"docker compose -f {service_compose_file} down", capture=False, critical=True
    )

    return Ok(None)


def stop_all_services() -> Result[None, str]:
    for service in utils.docker_handler.get_stopped_services():
        utils.io.info(f"Stopping service {service}")
        result = stop_service(service)
        match result:
            case Err(e):
                return Err(e)

    return Ok(None)


def print_service_status() -> Result[None, str]:
    services = utils.docker_handler.get_service_info()
    table: List[List[str]] = [["Servie", "Status"]]

    for service in services:
        row = [service["name"], service["status"]]
        table.append(row)

        for container in service["containers"]:
            row = [(" " * 4) + container["name"], container["status"]]
            table.append(row)

        table.append(["", ""])

    utils.io.table(table)
    return Ok(None)


def attach_to_service_logs(service_name: str) -> Result[None, str]:
    if service_name == "":
        return Err("Service name not provided")

    service_root = v.SERVICE_DIR / service_name

    if not service_root.is_dir():
        return Err(f"Service {service_name} not found")

    service_compose_file = service_root / "docker-compose.yml"

    if not service_compose_file.is_file():
        return Err(
            f"Service compose file for {service_name} not found at {service_compose_file}"
        )

    utils.runner.run(
        f"docker compose -f {service_compose_file} logs -f",
        capture=False,
        critical=False,
    )

    return Ok(None)


### Sub Commands ###


@app.command(help=v.SERVICE_TYPER_HELP["up"])
def up(
    service_name: str = typer.Argument("", shell_complete=completion.complete_services),
):
    result = None

    if service_name == "":
        confirm = utils.io.get_confirmation("Do you want to start all services?")

        if not confirm:
            exit(0)
        else:
            result = start_all_services()

    else:
        result = start_service(service_name)

    match result:
        case Err(e):
            utils.io.error(e)
            exit(1)

    exit(0)


@app.command(help=v.SERVICE_TYPER_HELP["down"])
def down(
    service_name: str = typer.Argument("", shell_complete=completion.complete_services),
):
    result = None

    if service_name == "":
        confirm = utils.io.get_confirmation("Do you want to stop all services?")

        if not confirm:
            exit(0)
        else:
            result = stop_all_services()

    else:
        result = stop_service(service_name)

    match result:
        case Err(e):
            utils.io.error(e)
            exit(1)

    exit(0)


def down_all():
    for item in utils.docker_handler.get_running_services():
        stop_service(item)


@app.command(name="list", help=v.SERVICE_TYPER_HELP["list"])
def list_services():
    print_service_status()


@app.command(help=v.SERVICE_TYPER_HELP["logs"])
def logs(
    service_name: str = typer.Argument("", shell_complete=completion.complete_services),
):
    result = attach_to_service_logs(service_name)
    match result:
        case Err(e):
            utils.io.error(e)
            exit(1)

    exit(0)
