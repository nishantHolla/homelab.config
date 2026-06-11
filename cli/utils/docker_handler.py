from typing import List, TypedDict
from collections import defaultdict
import docker
from docker.models.containers import Container
from config import values as v


class Container(TypedDict):
    name: str
    status: str


class Service(TypedDict):
    name: str
    containers: List[Container]
    status: str


def get_all_services() -> List[str]:
    return [s.name for s in v.SERVICE_DIR.iterdir() if s.is_dir()]


def get_running_services() -> List[str]:
    client = docker.from_env()
    all = set(get_all_services())
    projects: List[str] = []

    for c in client.containers.list(filters={"label": "com.docker.compose.project"}):
        project = c.labels["com.docker.compose.project"]
        projects.append(project)

    running = set(projects).intersection(all)
    return list(running)


def get_service_info() -> List[Service]:
    client = docker.from_env()
    projects = defaultdict(list)
    result: List[Service] = []

    for c in client.containers.list(filters={"label": "com.docker.compose.project"}):
        project = c.labels["com.docker.compose.project"]
        projects[project].append(c)

    for project, containers in projects.items():
        container_list: List[Container] = [
            {"name": str(c.name), "status": str(c.status)} for c in containers
        ]
        service: Service = {
            "name": project,
            "containers": container_list,
            "status": "running",
        }
        result.append(service)

    all_services = get_all_services()
    running_services = set(projects.keys())

    for service_name in all_services:
        if service_name not in running_services:
            result.append({"name": service_name, "containers": [], "status": "stopped"})

    return result


def get_stopped_services() -> List[str]:
    all = set(get_all_services())
    running = set(get_running_services())
    stopped = all - running

    return list(stopped)
