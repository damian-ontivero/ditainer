import enum


class ServiceArgumentType(enum.Enum):
    SIMPLE = ""
    REF = "!ref"
    TAGGED = "!tagged"


class ServiceArgument:
    def __init__(self, type_: ServiceArgumentType, value: str) -> None:
        self._type = type_
        self._value = value

    @property
    def value(self) -> str:
        return self._value

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, self.__class__):
            return NotImplemented

        return self._type == other._type and self._value == other._value

    def __ne__(self, other: object) -> bool:
        return not self.__eq__(other)

    def __hash__(self) -> int:
        return hash((self._type, self._value))

    def __repr__(self) -> str:
        return "{c}(type={type!r}, value={value!r})".format(
            c=self.__class__.__name__, type=self._type, value=self._value
        )

    @classmethod
    def from_primitives(cls, type_: str, value: str) -> "ServiceArgument":
        return cls(ServiceArgumentType(type_), value)

    def is_simple(self) -> bool:
        return self._type == ServiceArgumentType.SIMPLE

    def is_ref(self) -> bool:
        return self._type == ServiceArgumentType.REF

    def is_tagged(self) -> bool:
        return self._type == ServiceArgumentType.TAGGED


class ServiceArguments:
    def __init__(self, value: list[ServiceArgument]) -> None:
        self._value = value

    @property
    def value(self) -> list[ServiceArgument]:
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

    def __contains__(self, argument: str) -> bool:
        return argument in [arg.value for arg in self._value]

    @classmethod
    def from_list(cls, arguments: list) -> "ServiceArguments":
        args = []

        for argument in arguments:
            if isinstance(argument, str) and argument.startswith("!"):
                args.append(ServiceArgument.from_primitives(*argument.split(" ")))
            else:
                args.append(ServiceArgument.from_primitives("", argument))

        return cls(args)
