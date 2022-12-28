from aiohttp import ClientSession

from src.aioreq.base import AbstractRequestMaker


class RequestMaker(AbstractRequestMaker):

    def __init__(self, session: ClientSession):
        self._session = session

    async def post(self, url: str, headers: dict, body):
        async with self._session.post(url, json=body, headers=headers) as r:
            json_body = await r.json()
        return json_body

    async def get(self, url: str, headers: dict):
        async with self._session.get(url, headers=headers) as r:
            response = await r.json()
        return response

    async def put(self, url: str, headers: dict):
        pass

    async def patch(self, url: str, headers: dict):
        pass

    async def delete(self, url: str, headers: dict):
        pass
