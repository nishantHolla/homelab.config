import logging
from getpass import getpass

logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] %(message)s",
)

_logger = logging.getLogger("homelab")


def get_confirmation(prompt: str) -> bool:
    while True:
        confirmation = get_input(f"{prompt} [y/n]").lower()

        if confirmation == "y":
            return True

        if confirmation == "n":
            return False


def get_input(prompt: str) -> str:
    return input(f"[INPT] {prompt}")


def get_password(prompt: str) -> str:
    return getpass(f"[INPT] {prompt}")


def debug(msg: str) -> None:
    _logger.debug(msg)


def info(msg: str) -> None:
    _logger.info(msg)


def warning(msg: str) -> None:
    _logger.warning(msg)


def error(msg: str) -> None:
    _logger.error(msg)
