from ditainer.exception.service import ServiceTagError
from ditainer.exception.service import ServiceTagsError


class ServiceTag:
    def __init__(self, value: str) -> None:
        if value is None:
            raise ServiceTagError("The tag value cannot be None")

        if not isinstance(value, str):
            raise ServiceTagError("The tag value must be a string")

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
    def from_string(cls, value: str) -> "ServiceTag":
        return cls(value)


class ServiceTags:
    def __init__(self, value: list[ServiceTag]) -> None:
        if not isinstance(value, list):
            raise ServiceTagsError("Tags must be a list")

        self._value = value

    @property
    def value(self) -> list[ServiceTag]:
        return self._value

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, self.__class__):
            return NotImplemented

        return self._value == other._value

    def __ne__(self, other: object) -> bool:
        return not self.__eq__(other)

    def __hash__(self) -> int:
        return hash(tuple(self._value))

    def __repr__(self) -> str:
        return "{c}(value={value!r})".format(c=self.__class__.__name__, value=self._value)

    def __contains__(self, tag: str) -> bool:
        return tag in [tag.value for tag in self._value]

    @classmethod
    def from_list(cls, tags: list[str]) -> "ServiceTags":
        return cls([ServiceTag.from_string(tag) for tag in tags])
