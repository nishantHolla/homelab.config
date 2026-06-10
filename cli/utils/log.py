import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] %(message)s",
)

_logger = logging.getLogger("myapp")


def debug(msg: str) -> None:
    _logger.debug(msg)


def info(msg: str) -> None:
    _logger.info(msg)


def warning(msg: str) -> None:
    _logger.warning(msg)


def error(msg: str) -> None:
    _logger.error(msg)
