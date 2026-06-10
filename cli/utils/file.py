from pathlib import Path

from .result import Err, Ok, Result


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
