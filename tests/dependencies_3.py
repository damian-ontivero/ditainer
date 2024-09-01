from tests.dependencies_2 import ClassWithFactoryWithArguments
from tests.dependencies_2 import ClassWithFactoryWithNoArguments


class ClassWithReferencedArguments:
    def __init__(self, dependency: ClassWithFactoryWithNoArguments):
        self.dependency = dependency

    def run(self) -> str:
        return self.dependency.run()


class ClassWithTaggedArguments:
    def __init__(self, dependencies: list[ClassWithFactoryWithArguments]):
        self.dependencies = dependencies

    def run(self) -> str:
        names = [dependency.run() for dependency in self.dependencies]

        return f"Hello, {', '.join(names)}"
