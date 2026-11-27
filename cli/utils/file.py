from pathlib import Path
import os
import shutil

from .result import Err, Ok, Result


def resolve_path(path: Path | str):
    return Path(os.path.expandvars(os.path.expanduser(path))).absolute()


def find_and_replace(
    file_path: Path | str, find_str: str, replace_str: str
) -> Result[None, str]:
    try:
        with open(file_path, "r") as file:
            data = file.read()

        data = data.replace(find_str, replace_str)

        with open(file_path, "w") as file:
            file.write(data)

        return Ok(None)
    except Exception as e:
        return Err(str(e))


def backup(file_path: Path | str) -> Result[Path, str]:
    file_path = Path(file_path)
    new_path = file_path.with_suffix(file_path.suffix + ".bak")

    if not new_path.exists():
        shutil.move(file_path, new_path)
        return Ok(new_path)

    counter = 1
    while True:
        new_path = file_path.with_suffix(file_path.suffix + f".bak{counter}")

        if not new_path.exists():
            shutil.move(file_path, new_path)
            return Ok(new_path)

        counter += 1
