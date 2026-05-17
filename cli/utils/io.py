from getpass import getpass
from typing import List


def info(author: str, *args, **kwargs) -> None:
    print(f"[INFO] {author}:", *args, **kwargs)


def error(author: str, *args, **kwargs) -> None:
    print(f"[ERRR] {author}:", *args, **kwargs)


def warn(author: str, *args, **kwargs) -> None:
    print(f"[WARN] {author}:", *args, **kwargs)


def get_input(author: str, prompt: str) -> str:
    return input(f"[INPT] {author}: {prompt}")


def get_password(author: str, prompt: str) -> str:
    return getpass(f"[INPT] {author}: {prompt}")


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
