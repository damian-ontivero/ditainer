import importlib

from typing import Any
from typing import Callable

from ditainer.exception.instance_manager import ServiceNotFoundError
from ditainer.service.service import Service
from ditainer.service.service_arguments import ServiceArguments


class LazyProxy:
    def __init__(self, resolver: Callable) -> None:
        self._resolver = resolver

    def __call__(self, *args, **kwargs):
        """
        Resolve the service instance when the lazy reference is called.
        """
        instance = self._resolver()

        return instance(*args, **kwargs)

    def __getattr__(self, item):
        """
        Resolve the service instance when an attribute or method is accessed.
        """
        instance = self._resolver()

        return getattr(instance, item)

    def __enter__(self):
        """
        Resolve the service instance when the lazy reference is used in a context manager.
        """
        instance = self._resolver()

        return instance.__enter__()

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Resolve the service instance when the lazy reference is used in a context manager.
        """
        instance = self._resolver()

        return instance.__exit__(exc_type, exc_val, exc_tb)

    async def __aenter__(self):
        """
        Resolve the service instance when the lazy reference is used in an async context manager.
        """
        instance = self._resolver()

        return await instance.__aenter__()

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """
        Resolve the service instance when the lazy reference is used in an async context manager.
        """
        instance = self._resolver()

        return await instance.__aexit__(exc_type, exc_val, exc_tb)


class InstanceManager:
    def __init__(self, services: set[Service]) -> None:
        self._services = services
        self._instances: dict[str, Any] = {}

    def _find(self, id: str) -> Any:
        if id in self._instances:
            return self._instances[id]

        service = next((s for s in self._services if s.id.value == id), None)

        if service is None:
            raise ServiceNotFoundError(f"No service found with id {id!r}")

        return self._create_instance(service)

    def _search_tagged(self, tag: str) -> list[Any]:
        tagged_services = [
            service for service in self._services if service.tags and tag in service.tags
        ]

        return [self._find(tagged_service.id.value) for tagged_service in tagged_services]

    def _create_lazy_reference(self, id: str) -> LazyProxy:
        return LazyProxy(lambda: self._find(id))

    def _resolve_arguments(self, arguments: ServiceArguments) -> list:
        resolved_arguments: list[Any] = []

        for argument in arguments.value:
            if argument.is_ref():
                # If the argument is a reference to another service, create a lazy reference to it.
                resolved_arguments.append(self._create_lazy_reference(argument.value))
            elif argument.is_tagged():
                resolved_arguments.append(self._search_tagged(argument.value))
            else:
                resolved_arguments.append(argument.value)

        return resolved_arguments

    def _create_instance(self, service: Service) -> Any:
        if service.id.value in self._instances:
            return self._instances[service.id.value]

        class_ = getattr(importlib.import_module(service.module.value), service.class_.value)
        arguments = self._resolve_arguments(service.arguments) if service.arguments else []

        if service.factory:
            factory = getattr(class_, service.factory.value)
            instance = factory(*arguments)
        else:
            instance = class_(*arguments)

        self._instances[service.id.value] = instance

        return instance

    def find(self, id: str) -> Any:
        return self._find(id)

    def search_tagged(self, tag: str) -> list[Any]:
        return self._search_tagged(tag)
