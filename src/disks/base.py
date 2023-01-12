import abc


class BaseDiskService(metaclass=abc.ABCMeta):

    # @abc.abstractmethod
    # async def get_file_from_path(self, path: str):
    #     raise NotImplementedError()

    @abc.abstractmethod
    async def download_file(self, path: str):
        raise NotImplementedError()

    @abc.abstractmethod
    async def upload_file(self, path: str, file: bytes) -> bytes:
        raise NotImplementedError()

    @abc.abstractmethod
    async def get_meta_info_about_disk(self):
        raise NotImplementedError()

    @abc.abstractmethod
    async def create_folder(self, path: str, name: str):
        raise NotImplementedError()
