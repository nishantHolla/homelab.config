import subprocess
from typing import List, Tuple

import utils

from .result import Err, Ok, Result


def run(
    command: List[str] | str,
    critical=False,
    capture=False,
    silent=False,
    env=None,
) -> Result[str, Tuple[int, str]]:
    if not silent:
        command_str = " ".join(command) if type(command) is list else command
        utils.io.info(f"Running command {command_str}")

    result = subprocess.run(
        command, capture_output=capture, text=True, check=False, shell=True, env=env
    )

    if result.returncode:
        if critical:
            error = f": {result.stderr}" if result.stderr else ""
            utils.io.error(f"Command failed{error}")
            exit(1)
        else:
            return Err((result.returncode, result.stderr))

    return Ok(result.stdout)
