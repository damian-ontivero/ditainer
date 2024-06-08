class ServiceTag:
    def __init__(self, value: str) -> None:
        if value is None:
            raise ServiceTagError("Tag must be provided")
        self._value = value

    @property
    def value(self) -> str:
        return self._value


class ServiceTagError(Exception):
    pass
