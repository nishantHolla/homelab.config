import utils
from utils.result import Result
from config import usage as u
from config import values as v


def _check_service(service_name: str) -> Result:
    service_dir = v.SERVICE_DIR / service_name
    env_file = service_dir / ".env"
    compose_file = service_dir / "docker-compose.yml"

    if not service_dir.is_dir():
        return Result(1, f"Could not find service {service_name}")

    if not env_file.is_file():
        return Result(2, f"Could not find env file for service {service_name}")

    if not compose_file.is_file():
        return Result(3, f"Could not find compose file for service {service_name}")

    return Result(0, "Ok")


def _check_all_services() -> Result:
    for item in v.SERVICE_DIR.iterdir():
        result = _check_service(item.name)

        if result.code != 0:
            return result

    return Result(0, "Ok")


def check(args: list[str]) -> Result:
    if len(args) == 0:
        result = _check_all_services()
        message = "All services configured"

    else:
        service_name = args.pop(0)
        result = _check_service(service_name)
        message = f"{service_name} service configured correctly"

    if result.code == 0:
        utils.io.info("check", message)
    else:
        utils.io.error("check", result.message)

    return Result(0, "Ok")


def _up_service(service_name) -> Result:
    service_path = v.SERVICE_DIR / service_name
    utils.runner.run(
        "up", f"docker compose up -d {service_path}", capture=False, critical=True
    )

    return Result(0, "Ok")


def _up_all_services() -> Result:
    for item in v.SERVICE_DIR.iterdir():
        _up_service(item.name)
        utils.io.info("up", f"Composed up {item.name} service")

    return Result(0, "Ok")


def up(args: list[str]) -> Result:
    if len(args) == 0:
        result = _up_all_services()
        message = "All services composed up"

    else:
        service_name = args.pop(0)
        result = _up_service(service_name)
        message = f"Composed up {service_name}"

    if result.code == 0:
        utils.io.info("up", message)
    else:
        utils.io.info("up", result.message)

    return Result(0, "Ok")


def _down_service(service_name) -> Result:
    service_path = v.SERVICE_DIR / service_name
    utils.runner.run(
        "down", f"docker compose down -d {service_path}", capture=False, critical=True
    )

    return Result(0, "Ok")


def _down_all_services() -> Result:
    for item in v.SERVICE_DIR.iterdir():
        _down_service(item.name)
        utils.io.info("down", f"Composed down {item.name} service")

    return Result(0, "Ok")


def down(args: list[str]) -> Result:
    if len(args) == 0:
        result = _down_all_services()
        message = "All services composed down"

    else:
        service_name = args.pop(0)
        result = _down_service(service_name)
        message = f"Composed down {service_name}"

    if result.code == 0:
        utils.io.info("down", message)
    else:
        utils.io.info("down", result.message)

    return Result(0, "Ok")


def run(args: list[str]) -> int:
    if len(args) == 0:
        utils.io.info("service", u.SERVICE_USAGE)
        return 1

    sub_command = args.pop(0)

    if sub_command == "help":
        utils.io.info("service", u.SERVICE_USAGE)
        return 0

    elif sub_command == "check":
        result = check(args)

        if result.code != 0:
            utils.io.error("check", result.message)

        return result.code

    elif sub_command == "up":
        result = up(args)

        if result.code != 0:
            utils.io.error("up", result.message)

        return result.code

    elif sub_command == "down":
        result = down(args)

        if result.code != 0:
            utils.io.error("down", result.message)

        return result.code

    else:
        utils.io.error(
            "service",
            f"Unknown sub-command {sub_command}\n"
            "Run 'system service help' for list of all sub-commands",
        )
        return 1
