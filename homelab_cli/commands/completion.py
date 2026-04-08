from typing import List
from config import values as v
import typer


def complete_services(incomplete: str) -> List[str]:
    services: List[str] = [item.name for item in v.SERVICE_DIR.iterdir()]
    return [s for s in services if s.startswith(incomplete)]
