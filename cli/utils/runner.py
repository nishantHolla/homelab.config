import utils
import subprocess
from typing import List, Tuple
from .result import Result, Ok, Err


def run(
    command: List[str],
    critical=False,
    capture=False,
    silent=False,
    env=None,
) -> Result[str, Tuple[int, str]]:
    if not silent:
        command_str = " ".join(command) if type(command) is list else command
        utils.log.info(f"Running command {command_str}")

    result = subprocess.run(
        command, capture_output=capture, text=True, check=False, shell=True, env=env
    )

    if result.returncode:
        if critical:
            error = f": {result.stderr}" if result.stderr else ""
            utils.log.error(f"Command failed{error}")
            exit(1)
        else:
            return Err((result.returncode, result.stderr))

    return Ok(result.stdout)
