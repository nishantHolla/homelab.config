from typing import List, Dict, Optional, TypedDict
import docker
from docker.models.containers import Container


class ComposeContainerInfo(TypedDict):
    name: str
    project: str
    service: str
    status: str


def get_compose_containers(
    project_name: Optional[str] = None, all_containers: bool = True
) -> List[ComposeContainerInfo]:
    client = docker.from_env()

    filters = {}
    if project_name:
        filters["label"] = f"com.docker.compose.project={project_name}"

    containers: List[Container] = client.containers.list(
        all=all_containers, filters=filters if filters else None
    )

    result: List[ComposeContainerInfo] = []

    for c in containers:
        labels = c.labels or {}

        # If no project filter, ensure it's a compose container
        if not project_name and "com.docker.compose.project" not in labels:
            continue

        if not c.name:
            continue

        result.append(
            {
                "name": c.name,
                "project": labels.get("com.docker.compose.project", ""),
                "service": labels.get("com.docker.compose.service", ""),
                "status": c.status,
            }
        )

    return result
