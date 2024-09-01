import os

import pytest

from ditainer.container import Container
from ditainer.loader.yaml_loader import YAMLLoader


@pytest.fixture(scope="session", autouse=True)
def container() -> Container:
    container = Container()
    loader = YAMLLoader(container)

    loader.load(os.path.join(os.path.dirname(__file__), "imports.yaml"))

    return container
