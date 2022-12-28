import abc


class BaseDiskService(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    async def get_file_from_path(self, path: str):
        raise NotImplementedError()

    @abc.abstractmethod
    async def download_file(self, name: str, ile: bytes):
        raise NotImplementedError()

    @abc.abstractmethod
    async def upload_file(self, path: str) -> bytes:
        raise NotImplementedError()

    @abc.abstractmethod
    async def get_meta_info_about_disk(self):
        raise NotImplementedError()

