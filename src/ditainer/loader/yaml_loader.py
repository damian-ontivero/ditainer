import yaml

from ditainer.exception.loader import YAMLLoaderError
from ditainer.loader.loader import Loader


def ref_constructor(loader: yaml.FullLoader, node) -> str:
    return f"!ref {loader.construct_scalar(node)}"


def tagged_constructor(loader: yaml.FullLoader, node) -> str:
    return f"!tagged {loader.construct_scalar(node)}"


yaml.add_constructor("!ref", ref_constructor, Loader=yaml.FullLoader)
yaml.add_constructor("!tagged", tagged_constructor, Loader=yaml.FullLoader)


class YAMLLoader(Loader):
    def load(self, file_path: str) -> None:
        self._file_path = file_path

        try:
            with open(self._file_path, "r") as file:
                data: dict = yaml.load(file, Loader=yaml.FullLoader)
        except FileNotFoundError:
            raise YAMLLoaderError(f"The file {self._file_path!r} was not found")

        if "imports" in data:
            self._process_imports(data["imports"])

        if "services" in data:
            self._process_services(data["services"])
