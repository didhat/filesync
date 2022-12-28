import abc


class AbstractRequestMaker(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    async def post(self, url: str, headers: dict, body):
        pass

    @abc.abstractmethod
    async def get(self, url: str, headers: dict):
        pass

    @abc.abstractmethod
    async def put(self, url: str, headers: dict):
        pass

    @abc.abstractmethod
    async def patch(self, url: str, headers: dict):
        pass

    @abc.abstractmethod
    async def delete(self, url: str, headers: dict):
        pass
