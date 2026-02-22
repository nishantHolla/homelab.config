from pathlib import Path

def find_and_replace(file_path: Path | str, find: str, replace: str) -> int:
    try:
        with open(file_path, "r") as file:
            data = file.read()

        data = data.replace(find, replace)

        with open(file_path, "w") as file:
            file.write(data)

        return 0

    except Exception as e:
        return 1
