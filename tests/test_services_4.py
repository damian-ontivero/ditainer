from ditainer.container import Container


def test_service__find_tagged(container: Container) -> None:
    """
    Test that the find_tagged method returns a list of instances with the given tag.
    """
    instances = container.find_tagged("name_to_say_hello")

    assert len(instances) == 1
    assert instances[0].run() == "Angel Di Maria"
