from ditainer.exception.service import ServiceClassError


class ServiceClass:
    def __init__(self, value: str) -> None:
        if value is None:
            raise ServiceClassError("The class value cannot be None")

        if not isinstance(value, str):
            raise ServiceClassError("The class value must be a string")

        self._value = value

    @property
    def value(self) -> str:
        return self._value

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, self.__class__):
            return NotImplemented

        return self._value == other._value

    def __ne__(self, other: object) -> bool:
        return not self.__eq__(other)

    def __hash__(self) -> int:
        return hash(self._value)

    def __repr__(self) -> str:
        return "{c}(value={value!r})".format(c=self.__class__.__name__, value=self._value)

    @classmethod
    def from_string(cls, value: str) -> "ServiceClass":
        return cls(value)
