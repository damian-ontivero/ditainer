from .service_argument_type import ServiceArgumentType


class ServiceArgument:
    def __init__(self, type_: ServiceArgumentType, value: str) -> None:
        self._type = type_
        self._value = value

    @property
    def value(self) -> str:
        return self._value

    @property
    def is_simple(self) -> bool:
        return self._type.is_simple

    @property
    def is_ref(self) -> bool:
        return self._type.is_ref

    @property
    def is_tagged(self) -> bool:
        return self._type.is_tagged

    @classmethod
    def from_primitives(cls, type_: str, value: str) -> "ServiceArgument":
        return cls(ServiceArgumentType(type_), value)
