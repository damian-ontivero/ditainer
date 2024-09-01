class ClassWithFactoryWithNoArguments:
    def __init__(self, name: str) -> None:
        self._name = name

    @classmethod
    def create(cls) -> "ClassWithFactoryWithNoArguments":
        return cls(name="Angel Di Maria")

    def run(self) -> str:
        return self._name


class ClassWithFactoryWithArguments:
    def __init__(self, name: str) -> None:
        self._name = name

    @classmethod
    def create(cls, name: str) -> "ClassWithFactoryWithArguments":
        return cls(name=name)

    def run(self) -> str:
        return self._name
