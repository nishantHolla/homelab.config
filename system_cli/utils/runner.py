import utils

import subprocess


def run(
    author: str, command: list[str] | str, critical=False, capture=False, silent=False
) -> tuple[str, int, str]:

    if not silent:
        command_str = " ".join(command) if type(command) is list else command
        utils.io.info(author, f"Running {command_str}")

    result = subprocess.run(
        command, capture_output=capture, text=True, check=True, shell=True
    )

    if result.returncode and critical:
        append = f": {result.stderr}" if capture else ""
        utils.io.error(author, f"Command failed{append}")
        exit(1)

    return result.stdout, result.returncode, result.stderr
