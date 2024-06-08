class ClassWithNoArguments:
    def __init__(self) -> None:
        pass

    def method_with_arguments(self, name: str) -> str:
        return name

    def method_with_no_arguments(self) -> str:
        return "Julián Álvarez"


class ClassWithArguments:
    def __init__(self, name: str) -> None:
        self._name = name

    def method_with_arguments(self, name: str) -> str:
        return name

    def method_with_no_arguments(self) -> str:
        return self._name


class Repository:
    def __init__(self, session: str) -> None:
        self._session = session

    def get_session(self) -> str:
        return self._session


class ClassToSayHello:
    def __init__(self, names: list[str]) -> None:
        self._names = names

    def say_hello(self) -> str:
        return f"Hello, {', '.join(self._names)}"


def method_with_arguments(name: str) -> str:
    return name


def method_with_no_arguments() -> str:
    return "Cuti Romero"


def create_session(uri: str) -> str:
    return uri


best_player = "Lionel Messi"
