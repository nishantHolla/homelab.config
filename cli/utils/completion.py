from typing import List

from config import values as v


def complete_services(ctx, param, incomplete: str) -> List[str]:
    services: List[str] = [item.name for item in v.SERVICE_DIR.iterdir()]
    matching_services = [s for s in services if s.startswith(incomplete)]

    if len(matching_services) > 0:
        return matching_services
    else:
        return [incomplete]
