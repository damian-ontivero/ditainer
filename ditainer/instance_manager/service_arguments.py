from ditainer.instance_manager.service_argument import ServiceArgument


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
