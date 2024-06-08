from .service_arguments import ServiceArguments


class ServiceClass:
    def __init__(self, name: str, arguments: ServiceArguments):
        self._name = name
        self._arguments = arguments

    @property
    def name(self) -> str:
        return self._name

    @property
    def arguments(self) -> ServiceArguments:
        return self._arguments

    @classmethod
    def from_primitives(cls, method: dict) -> "ServiceClass":
        return cls(method.get("name"), ServiceArguments.from_primitives(method.get("arguments", [])))
