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


def test_service__find_tagged(container: Container) -> None:
    """
    This test is to check that the find_tagged method returns a list of instances with the given tag.
    """
    instances = container.find_tagged("name_to_say_hello")

    assert len(instances) == 1
    assert instances[0].run() == "Angel Di Maria"
