import importlib

from .service import Service
from .service_arguments import ServiceArguments


class InstanceManager:
    def __init__(self, services: set[Service]) -> None:
        self._services = services

    def get_instance(self, service_id: str) -> object:
        for service in self._services:
            if service.id.value == service_id:
                return self._create_instance(service)
        raise ServiceNotFoundError(f"Service: {service_id!r} not found")

    def _create_instance(self, service: Service) -> object:
        if service.factory is not None:
            return self._create_instance_from_factory(service)
        return self._create_instance_from_class(service)

    def _create_instance_from_factory(self, service: Service) -> object:
        class_ = getattr(importlib.import_module(service.module.value), service.class_.value)
        factory = getattr(class_, service.factory.value)
        if service.arguments:
            arguments = self._resolve_arguments(service.arguments)
            return factory(*arguments)
        return factory()

    def _create_instance_from_class(self, service: Service) -> object:
        class_ = getattr(importlib.import_module(service.module.value), service.class_.value)
        if service.arguments:
            arguments = self._resolve_arguments(service.arguments)
            return class_(*arguments)
        return class_()

    def _resolve_arguments(self, arguments: ServiceArguments) -> list:
        resolved_arguments = []
        for argument in arguments.value:
            if argument.is_ref():
                resolved_arguments.append(self.get_instance(argument.value))
            elif argument.is_tagged():
                instances = []
                for service in self._services:
                    if service.tags and argument.value in service.tags:
                        instances.append(self.get_instance(service.id.value))
                resolved_arguments.append(instances)
            else:
                resolved_arguments.append(argument.value)
        return resolved_arguments


class ServiceNotFoundError(Exception):
    pass
