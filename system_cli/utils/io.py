import getpass


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
