from typing import Any

from ditainer.instance_manager import InstanceManager
from ditainer.service.service import Service


class Container:
    """
    The container is responsible for registering services and managing their instances.
    """

    def __init__(self) -> None:
        self._services: set[Service] = set()
        self._instance_manager: InstanceManager | None = None

    @property
    def instance_manager(self) -> InstanceManager:
        if self._instance_manager is None:
            self._instance_manager = InstanceManager(self._services)

        return self._instance_manager

    def register_service(self, service: dict) -> None:
        service_ = Service.from_primitives(
            service["id"],
            service["module"],
            service["class"],
            service.get("factory"),
            service.get("arguments"),
            service.get("tags"),
        )

        self._services.add(service_)

    def find(self, id: str) -> Any:
        return self.instance_manager.find(id)

    def find_tagged(self, tag: str) -> list[Any]:
        return self.instance_manager.search_tagged(tag)
