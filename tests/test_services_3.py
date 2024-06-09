def test_service__class_with_referenced_arguments(container) -> None:
    """
    This test is to check the service with:
    - Class with referenced arguments.
    """
    dependency = container.get("ClassWithReferencedArguments")

    result = dependency.run()

    assert isinstance(result, str)
    assert result == "Angel Di Maria"


def test_service__class_with_tagged_arguments(container) -> None:
    """
    This test is to check the service with:
    - Class with tagged arguments.
    """
    dependency = container.get("ClassWithTaggedArguments")

    result = dependency.run()

    assert isinstance(result, str)
    assert result == "Hello, Angel Di Maria"
