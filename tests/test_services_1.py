def test_service__class_with_no_arguments(container) -> None:
    """
    This test is to check the service with:
    - Class with no arguments.
    """
    dependency = container.get("ClassWithNoArguments")

    result = dependency.run()

    assert isinstance(result, str)
    assert result == "Lionel Messi"


def test_service__class_with_empty_arguments(container) -> None:
    """
    This test is to check the service with:
    - Class with empty arguments.
    """
    dependency = container.get("ClassWithNoArguments")

    result = dependency.run()

    assert isinstance(result, str)
    assert result == "Lionel Messi"


def test_service__class_with_arguments(container) -> None:
    """
    This test is to check the service with:
    - Class with arguments.
    """
    dependency = container.get("ClassWithArguments")

    result = dependency.run()

    assert isinstance(result, str)
    assert result == "Lionel Messi"
