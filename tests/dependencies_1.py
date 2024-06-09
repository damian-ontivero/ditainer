class ClassWithNoArguments:
    def __init__(self) -> None:
        pass

    def run(self) -> str:
        return "Lionel Messi"


class ClassWithArguments:
    def __init__(self, name: str) -> None:
        self._name = name

    def run(self) -> str:
        return self._name
