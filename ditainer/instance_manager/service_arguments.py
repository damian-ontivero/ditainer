from .service_argument import ServiceArgument


class ServiceArguments:
    def __init__(self, value: list[ServiceArgument]) -> None:
        self._value = value

    @property
    def value(self) -> list[ServiceArgument]:
        return self._value

    @classmethod
    def from_primitives(cls, arguments: list) -> "ServiceArguments":
        args = []
        for argument in arguments:
            if isinstance(argument, str) and argument.startswith("!"):
                args.append(ServiceArgument.from_primitives(*argument.split(" ")))
            else:
                args.append(ServiceArgument.from_primitives("", argument))
        return cls(args)
