import logging
from getpass import getpass
from typing import List

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


def table(rows: List[List[str]]) -> None:
    if not rows:
        return

    col_widths = [
        max(len(row[i]) for row in rows if i < len(row))
        for i in range(max(len(row) for row in rows))
    ]

    def format_row(row: List[str]) -> str:
        return " | ".join(
            row[i].ljust(col_widths[i]) if i < len(row) else " " * col_widths[i]
            for i in range(len(col_widths))
        )

    print(format_row(rows[0]))

    print("-+-".join("-" * w for w in col_widths))
    for row in rows[1:]:
        print(format_row(row))
