import yaml

from ditainer.loader.loader import Loader

yaml.add_constructor("!ref", lambda loader, node: "!ref " + loader.construct_scalar(node))
yaml.add_constructor("!tagged", lambda loader, node: "!tagged " + loader.construct_scalar(node))


class YAMLLoader(Loader):
    def load(self, file_path: str) -> None:
        self._file_path = file_path
        try:
            with open(self._file_path, "r") as file:
                data: dict = yaml.load(file, Loader=yaml.FullLoader)
        except FileNotFoundError:
            raise YAMLLoaderError(f"File: {self._file_path!r} not found")
        if "imports" in data:
            self._process_imports(data["imports"])
        if "services" in data:
            self._process_services(data["services"])


class YAMLLoaderError(Exception):
    pass
