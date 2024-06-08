from .service_class import ServiceClass
from .service_id import ServiceId
from .service_method import ServiceMethod
from .service_module import ServiceModule
from .service_tag import ServiceTag
from .service_variable import ServiceVariable


class Service:
    def __init__(
        self,
        id: ServiceId,
        module: ServiceModule,
        class_: ServiceClass | None,
        method: ServiceMethod | None,
        variable: ServiceVariable | None,
        tags: list[ServiceTag],
    ):
        if id is None:
            raise ServiceError("Id must be provided")
        if module is None:
            raise ServiceError("Module must be provided")
        if class_ is None and method is None and variable is None:
            raise ServiceError("Class_, method, or variable must be provided")
        self._id = id
        self._module = module
        self._class = class_
        self._method = method
        self._variable = variable
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
    def method(self) -> ServiceMethod | None:
        return self._method

    @property
    def variable(self) -> ServiceVariable | None:
        return self._variable

    @property
    def tags(self) -> list[ServiceTag]:
        return self._tags

    @classmethod
    def from_primitives(
        cls, id: str, module: str, class_: dict | None, method: dict | None, variable: str | None, tags: list[str]
    ) -> "Service":
        return cls(
            ServiceId(id),
            ServiceModule(module),
            ServiceClass.from_primitives(class_) if class_ is not None else None,
            ServiceMethod.from_primitives(method) if method is not None else None,
            ServiceVariable(variable) if variable is not None else None,
            [ServiceTag(tag) for tag in tags],
        )

    def __str__(self) -> str:
        return (
            "{c}(id={id!r}, module={module!r}, class_={class_!r}, "
            "method={method!r}, variable={variable!r}, tags={tags!r})"
        ).format(
            c=self.__class__.__name__,
            id=self._id,
            module=self._module,
            class_=self._class,
            method=self._method,
            variable=self._variable,
            tags=self._tags,
        )

    def __repr__(self) -> str:
        return self.__str__()


class ServiceError(Exception):
    pass
