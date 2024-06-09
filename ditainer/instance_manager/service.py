from .service_arguments import ServiceArguments
from .service_class import ServiceClass
from .service_factory import ServiceFactory
from .service_id import ServiceId
from .service_module import ServiceModule
from .service_tags import ServiceTags


class Service:
    def __init__(
        self,
        id: ServiceId,
        module: ServiceModule,
        class_: ServiceClass,
        factory: ServiceFactory | None,
        arguments: ServiceArguments | None,
        tags: ServiceTags | None,
    ):
        if id is None:
            raise ServiceError("Id must be provided")
        if module is None:
            raise ServiceError("Module must be provided")
        if class_ is None:
            raise ServiceError("Class must be provided")
        self._id = id
        self._module = module
        self._class = class_
        self._factory = factory
        self._arguments = arguments
        self._tags = tags

    @property
    def id(self) -> ServiceId:
        return self._id

    @property
    def module(self) -> ServiceModule:
        return self._module

    @property
    def class_(self) -> ServiceClass | None:
        return self._class

    @property
    def factory(self) -> ServiceFactory | None:
        return self._factory

    @property
    def arguments(self) -> ServiceArguments | None:
        return self._arguments

    @property
    def tags(self) -> ServiceTags:
        return self._tags

    @classmethod
    def from_primitives(
        cls, id: str, module: str, class_: str, factory: str | None, arguments: list | None, tags: list | None
    ) -> "Service":
        return cls(
            ServiceId.from_string(id),
            ServiceModule.from_string(module),
            ServiceClass.from_string(class_),
            ServiceFactory.from_string(factory) if factory else None,
            ServiceArguments.from_list(arguments) if arguments else None,
            ServiceTags.from_list(tags) if tags else None,
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, self.__class__):
            return NotImplemented
        return (
            self._id == other._id
            and self._module == other._module
            and self._class == other._class
            and self._factory == other._factory
            and self._arguments == other._arguments
            and self._tags == other._tags
        )

    def __ne__(self, other: object) -> bool:
        return not self.__eq__(other)

    def __hash__(self) -> int:
        return hash((self._id, self._module, self._class, self._factory, self._arguments, self._tags))

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}(id={self._id}, module={self._module}, class={self._class}, "
            f"factory={self._factory}, arguments={self._arguments}, tags={self._tags})"
        )


class ServiceError(Exception):
    pass
