import importlib

from .service import Service
from .service_arguments import ServiceArguments


class InstanceManager:
    def __init__(self, services: dict[str, Service]) -> None:
        self._services = services

    def get_instance(self, service_id: str) -> object:
        service = self._services.get(service_id)
        if service is None:
            raise ServiceNotFoundError(f"Service: {service_id!r} not found")
        return self._create_instance(service)

    def _create_instance(self, service: Service) -> object:
        instance = importlib.import_module(service.module.path)
        arguments = None
        if service.class_:
            instance = getattr(instance, service.class_.name)
            if service.class_.arguments:
                arguments = self._resolve_arguments(service.class_.arguments)
                instance = instance(*arguments)
            else:
                instance = instance()
        if service.method:
            instance = getattr(instance, service.method.name)
            if service.method.arguments:
                arguments = self._resolve_arguments(service.method.arguments)
                instance = instance(*arguments)
            else:
                instance = instance()
        if service.variable:
            instance = getattr(instance, service.variable.value)
        return instance

    def _resolve_arguments(self, arguments: ServiceArguments) -> list:
        resolved_arguments = []
        for argument in arguments.value:
            if argument.is_ref:
                resolved_arguments.append(self.get_instance(argument.value))
            elif argument.is_tagged:
                instances = []
                for service_id, service in self._services.items():
                    if argument.value in [tag.value for tag in service.tags]:
                        instances.append(self.get_instance(service_id))
                resolved_arguments.append(instances)
            else:
                resolved_arguments.append(argument.value)
        return resolved_arguments


class ServiceNotFoundError(Exception):
    pass
