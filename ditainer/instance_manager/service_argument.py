from .service_argument_type import ServiceArgumentType


class ServiceArgument:
    def __init__(self, type_: ServiceArgumentType, value: str) -> None:
        self._type = type_
        self._value = value

    @property
    def value(self) -> str:
        return self._value

    @classmethod
    def from_primitives(cls, type_: str, value: str) -> "ServiceArgument":
        return cls(ServiceArgumentType(type_), value)

    def is_simple(self) -> bool:
        return self._type.is_simple()

    def is_ref(self) -> bool:
        return self._type.is_ref()

    def is_tagged(self) -> bool:
        return self._type.is_tagged()

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self._type == other._type and self._value == other._value

    def __ne__(self, other: object) -> bool:
        return not self.__eq__(other)

    def __hash__(self) -> int:
        return hash((self._type, self._value))

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(type={self._type}, value={self._value})"
