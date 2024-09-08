from ditainer.container import Container


def test_service__circular_dependency(container: Container) -> None:
    """
    This test is to check that the container can handle circular dependencies.
    """
    service = container.find("ServiceA")
    service.run()
