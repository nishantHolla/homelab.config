import utils

import subprocess
import os

def run(author: str, command: list[str] | str, critical=False, capture=False, silent=False) \
    -> tuple[str, int, str] | None:

    if not silent:
        command_str = " ".join(command) if type(command) is list else command
        utils.io.info(author, f"Running {command_str}")


    if capture:
        result = subprocess.run(command, capture_output=True, text=True, check=True, shell=True)

        if result.returncode and critical:
            utils.io.error(author, f"Command failed: {result.stderr}")
            exit(1)

        return result.stdout, result.returncode, result.stderr

    else:
        returncode = os.system(command)

        if returncode and critical:
            utils.io.error(author, f"Command failed")
            exit(1)

        return returncode

