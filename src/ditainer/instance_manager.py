import importlib

from ditainer.exception.instance_manager import ServiceNotFoundError
from ditainer.service.service import Service
from ditainer.service.service_arguments import ServiceArguments


class InstanceManager:
    def __init__(self, services: set[Service]) -> None:
        self._services = services

    def _resolve_arguments(self, arguments: ServiceArguments) -> list:
        resolved_arguments = []

        for argument in arguments.value:
            if argument.is_ref():
                resolved_arguments.append(self.find(argument.value))
            elif argument.is_tagged():
                instances = []

                for service in self._services:
                    if service.tags and argument.value in service.tags:
                        instances.append(self.find(service.id.value))

                resolved_arguments.append(instances)
            else:
                resolved_arguments.append(argument.value)

        return resolved_arguments

    def _create_instance(self, service: Service) -> object:
        class_ = getattr(importlib.import_module(service.module.value), service.class_.value)
        arguments = self._resolve_arguments(service.arguments) if service.arguments else []

        if service.factory:
            factory = getattr(class_, service.factory.value)

            return factory(*arguments)

        return class_(*arguments)

    def find(self, id: str) -> object:
        for service in self._services:
            if service.id.value == id:
                return self._create_instance(service)

        raise ServiceNotFoundError(f"The service with id {id!r} was not found")

    def find_tagged(self, tag: str) -> list:
        instances = []

        for service in self._services:
            if service.tags and tag in service.tags:
                instances.append(self._create_instance(service))

        return instances
