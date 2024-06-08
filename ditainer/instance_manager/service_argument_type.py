class ServiceArgumentType:
    SIMPLE = ""
    REFERENCE = "!ref"
    TAGGED = "!tagged"

    def __init__(self, value: str) -> None:
        if value not in [self.SIMPLE, self.REFERENCE, self.TAGGED]:
            raise ServiceArgumentTypeError(f"Invalid service argument type: {value}")
        self._value = value

    @property
    def is_simple(self) -> bool:
        return self._value == self.SIMPLE

    @property
    def is_ref(self) -> bool:
        return self._value == self.REFERENCE

    @property
    def is_tagged(self) -> bool:
        return self._value == self.TAGGED


class ServiceArgumentTypeError(Exception):
    pass
