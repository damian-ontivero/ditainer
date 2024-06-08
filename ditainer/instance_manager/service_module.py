class ServiceModule:
    def __init__(self, path: str) -> None:
        if path is None:
            raise ServiceModuleError("Path must be provided")
        self._path = path

    @property
    def path(self) -> str:
        return self._path


class ServiceModuleError(Exception):
    pass
