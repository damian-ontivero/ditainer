from ditainer.container import Container


def test_service__class_with_factory_with_no_arguments(container: Container) -> None:
    """
    This test is to check the service with:
    - Class with factory with no arguments.
    """
    dependency = container.find("ClassWithFactoryWithNoArguments")

    result = dependency.run()

    assert isinstance(result, str)
    assert result == "Angel Di Maria"


def test_service__class_with_factory_with_empty_arguments(container: Container) -> None:
    """
    This test is to check the service with:
    - Class with factory with empty arguments.
    """
    dependency = container.find("ClassWithFactoryWithEmptyArguments")

    result = dependency.run()

    assert isinstance(result, str)
    assert result == "Angel Di Maria"


def test_service__class_with_factory_with_arguments(container: Container) -> None:
    """
    This test is to check the service with:
    - Class with factory with arguments.
    """
    dependency = container.find("ClassWithFactoryWithArguments")

    result = dependency.run()

    assert isinstance(result, str)
    assert result == "Angel Di Maria"
