from pathlib import Path

from .result import Result


def find_and_replace(file_path: Path | str, find: str, replace: str) -> Result:
    try:
        with open(file_path, "r") as file:
            data = file.read()

        data = data.replace(find, replace)

        with open(file_path, "w") as file:
            file.write(data)

        return Result(0, "Ok")

    except Exception as e:
        return Result(1, str(e))
