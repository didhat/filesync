from typing import Any

import abc


class RequestResponse:

    def __init__(self, data: Any, status_code: int):
        self.data = data
        self.status_code = status_code


class AbstractRequestMaker(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    async def post(self, url: str, headers: dict, body):
        pass

    @abc.abstractmethod
    async def get(self, url: str, headers: dict = None, params: dict = None) -> RequestResponse:
        pass

    @abc.abstractmethod
    async def put(self, url: str, headers: dict = None, params: dict = None,
                  data: dict | bytes = None, response_type: str = "json") -> RequestResponse:
        pass

    @abc.abstractmethod
    async def patch(self, url: str, headers: dict):
        pass

    @abc.abstractmethod
    async def delete(self, url: str, headers: dict):
        pass

    @abc.abstractmethod
    async def get_file(self, url: str, headers: dict | None = None, params: dict | None = None) -> RequestResponse:
        pass
