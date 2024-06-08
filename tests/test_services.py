def test_service__class_no_arguments__no_method(container) -> None:
    """
    This test is to check the service with:
    - Class with no arguments.
    - No method.
    """
    dep = container.get("service__class_no_arguments__no_method")

    name = dep.method_with_no_arguments()

    assert isinstance(name, str)
    assert name == "Julián Álvarez"


def test_service__class_arguments__no_method(container) -> None:
    """
    This test is to check the service with:
    - Class with arguments.
    - No method.
    """
    dep = container.get("service__class_arguments__no_method")

    name = dep.method_with_no_arguments()

    assert isinstance(name, str)
    assert name == "Lionel Messi"


def test_service__no_class__method_no_arguments(container) -> None:
    """
    This test is to check the service with:
    - No class.
    - Method with no arguments.
    """
    name = container.get("service__no_class__method_no_arguments")

    assert isinstance(name, str)
    assert name == "Cuti Romero"


def test_service__no_class__method_arguments(container) -> None:
    """
    This test is to check the service with:
    - No class.
    - Method with arguments.
    """
    dep = container.get("service__no_class__method_arguments")

    assert isinstance(dep, str)
    assert dep == "sqlite:///:memory:"


def test_service__class_no_arguments__method_no_arguments(container) -> None:
    """
    This test is to check the service with:
    - Class with no arguments.
    - Method with no arguments.
    """
    dep = container.get("service__class_no_arguments__method_no_arguments")

    assert isinstance(dep, str)
    assert dep == "Julián Álvarez"


def test_service__class_arguments__method_no_arguments(container) -> None:
    """
    This test is to check the service with:
    - Class with arguments.
    - Method with no arguments.
    """
    dep = container.get("service__class_arguments__method_no_arguments")

    assert isinstance(dep, str)
    assert dep == "Angel Di Maria"


def test_service__class_no_arguments__method_arguments(container) -> None:
    """
    This test is to check the service with:
    - Class with no arguments.
    - Method with arguments.
    """
    dep = container.get("service__class_no_arguments__method_arguments")

    assert isinstance(dep, str)
    assert dep == "Enzo Fernandez"


def test_service__class_arguments__method_arguments(container) -> None:
    """
    This test is to check the service with:
    - Class with arguments.
    - Method with arguments.
    """
    dep = container.get("service__class_arguments__method_arguments")

    assert isinstance(dep, str)
    assert dep == "Lautaro Martinez"


def test_service__class_referenced_arguments__no_method(container) -> None:
    """
    This test is to check the service with:
    - Class with referenced arguments.
    - No method.
    """
    dep = container.get("service__class_referenced_arguments__no_method")

    session = dep.get_session()

    assert isinstance(session, str)
    assert session == "sqlite:///:memory:"


def test_service__class_tagged_arguments__no_method(container) -> None:
    """
    This test is to check the service with:
    - Class with tagged arguments.
    - No method.
    """
    dep = container.get("service__class_tagged_arguments__no_method")

    message = dep.say_hello()

    assert isinstance(message, str)
    assert message == "Hello, Diego Maradona, Cuti Romero"


def test_service__variable(container) -> None:
    """
    This test is to check the service with:
    - Variable.
    """
    dep = container.get("service__variable")

    message = dep

    assert isinstance(message, str)
    assert message == "Lionel Messi"
