from ditainer.instance_manager import InstanceManager, Service


class Container:
    """
    The container is responsible for registering services and managing their instances.
    """

    def __init__(self) -> None:
        self._services = set()
        self._instance_manager: InstanceManager = None

    @property
    def instance_manager(self) -> InstanceManager:
        if self._instance_manager is None:
            self._instance_manager = InstanceManager(self._services)
        return self._instance_manager

    def register_service(self, service: dict) -> None:
        service_ = Service.from_primitives(
            service.get("id"),
            service.get("module"),
            service.get("class"),
            service.get("factory"),
            service.get("arguments", []),
            service.get("tags", []),
        )
        self._services.add(service_)

    def find(self, id: str) -> object:
        return self.instance_manager.find(id)

    def find_tagged(self, tag: str) -> list:
        return self.instance_manager.find_tagged(tag)
