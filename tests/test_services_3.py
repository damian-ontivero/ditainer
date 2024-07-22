from ditainer.container import Container


def test_service__class_with_referenced_arguments(container: Container) -> None:
    """
    This test is to check the service with:
    - Class with referenced arguments.
    """
    dependency = container.find("ClassWithReferencedArguments")

    result = dependency.run()

    assert isinstance(result, str)
    assert result == "Angel Di Maria"


def test_service__class_with_tagged_arguments(container: Container) -> None:
    """
    This test is to check the service with:
    - Class with tagged arguments.
    """
    dependency = container.find("ClassWithTaggedArguments")

    result = dependency.run()

    assert isinstance(result, str)
    assert result == "Hello, Angel Di Maria"
