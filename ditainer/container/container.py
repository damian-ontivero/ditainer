from ditainer.instance_manager import InstanceManager, Service


class Container:
    """
    The container is responsible for registering services and managing their instances.
    """

    def __init__(self) -> None:
        self._services: dict[str, Service] = {}
        self._instance_manager: InstanceManager = None

    @property
    def instance_manager(self) -> InstanceManager:
        if self._instance_manager is None:
            self._instance_manager = InstanceManager(self._services)
        return self._instance_manager

    def register_service(self, service_id: str, service: dict[str, dict | str]) -> None:
        service_ = Service.from_primitives(
            service_id,
            service.get("module"),
            service.get("class"),
            service.get("method"),
            service.get("variable"),
            service.get("tags", []),
        )
        self._services[service_.id.value] = service_

    def get(self, service_id: str) -> object:
        return self.instance_manager.get_instance(service_id)
