from ditainer.exception.service import ServiceError
from ditainer.service.service_arguments import ServiceArguments
from ditainer.service.service_class import ServiceClass
from ditainer.service.service_factory import ServiceFactory
from ditainer.service.service_id import ServiceId
from ditainer.service.service_module import ServiceModule
from ditainer.service.service_tags import ServiceTags


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
    def class_(self) -> ServiceClass:
        return self._class

    @property
    def factory(self) -> ServiceFactory | None:
        return self._factory

    @property
    def arguments(self) -> ServiceArguments | None:
        return self._arguments

    @property
    def tags(self) -> ServiceTags | None:
        return self._tags

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, self.__class__):
            return NotImplemented

        return self._id == other._id

    def __ne__(self, other: object) -> bool:
        return not self.__eq__(other)

    def __hash__(self) -> int:
        return hash(self._id)

    def __repr__(self) -> str:
        return (
            "{c}(id={id!r}, module={module!r}, class={class_!r}, "
            "factory={factory!r}, arguments={arguments!r}, tags={tags!r})"
        ).format(
            c=self.__class__.__name__,
            id=self._id,
            module=self._module,
            class_=self._class,
            factory=self._factory,
            arguments=self._arguments,
            tags=self._tags,
        )

    @classmethod
    def from_primitives(
        cls,
        id: str,
        module: str,
        class_: str,
        factory: str | None,
        arguments: list | None,
        tags: list | None,
    ) -> "Service":
        if id is None:
            raise ServiceError("The id value cannot be None")

        if module is None:
            raise ServiceError("The module value cannot be None")

        if class_ is None:
            raise ServiceError("The class value cannot be None")

        return cls(
            ServiceId.from_string(id),
            ServiceModule.from_string(module),
            ServiceClass.from_string(class_),
            ServiceFactory.from_string(factory) if factory else None,
            ServiceArguments.from_list(arguments) if arguments else None,
            ServiceTags.from_list(tags) if tags else None,
        )
