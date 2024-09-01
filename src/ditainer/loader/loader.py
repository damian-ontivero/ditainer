import abc
import os

from ditainer.container import Container
from ditainer.exception.loader import LoaderError


class Loader(metaclass=abc.ABCMeta):
    """
    Abstract base class for all loaders.

    A Loader is responsible for loading a file and parsing its content to register services in a container.
    """

    def __init__(self, container: Container) -> None:
        self._file_path: str

        if not isinstance(container, Container):
            raise LoaderError("The container must be an instance of Container.")

        self._container = container

    @abc.abstractmethod
    def load(self, file_path: str) -> None:
        """
        Load the data from the file and process it.
        """
        raise NotImplementedError

    def _process_imports(self, imports: list[dict]) -> None:
        """
        Process the imports defined in the file.

        The imports file contains a list of files to import.
        The files are imported in the order they are defined.
        """
        for import_ in imports:
            working_dir = self._file_path

            self.load(os.path.join(os.path.dirname(self._file_path), import_["resource"]))

            self._file_path = working_dir

    def _process_services(self, services: list[dict]) -> None:
        """
        Process the services defined in the file and register them in the container.
        """
        for service in services:
            self._container.register_service(service)
