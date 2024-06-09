class ServiceArgumentType:
    SIMPLE = ""
    REFERENCE = "!ref"
    TAGGED = "!tagged"

    def __init__(self, value: str) -> None:
        if value is None:
            raise ServiceArgumentTypeError("Type must be provided")
        if not isinstance(value, str):
            raise ServiceArgumentTypeError("Type must be a string")
        if value not in [self.SIMPLE, self.REFERENCE, self.TAGGED]:
            raise ServiceArgumentTypeError(f"Invalid service argument type: {value}")
        self._value = value

    @property
    def value(self) -> str:
        return self._value

    @classmethod
    def from_string(cls, value: str) -> "ServiceArgumentType":
        return cls(value)

    def is_simple(self) -> bool:
        return self._value == self.SIMPLE

    def is_ref(self) -> bool:
        return self._value == self.REFERENCE

    def is_tagged(self) -> bool:
        return self._value == self.TAGGED

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self._value == other._value

    def __ne__(self, other: object) -> bool:
        return not self.__eq__(other)

    def __hash__(self) -> int:
        return hash(self._value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(value={self._value})"


class ServiceArgumentTypeError(Exception):
    pass
