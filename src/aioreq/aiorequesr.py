from aiohttp import ClientSession

from src.aioreq.base import AbstractRequestMaker, RequestResponse


class RequestMaker(AbstractRequestMaker):

    def __init__(self):
        self._session = ClientSession()

    async def post(self, url: str, headers: dict, body):
        async with self._session.post(url, json=body, headers=headers) as r:
            json_body = await r.json()
        return json_body

    async def get(self, url: str, headers: dict | None = None, params: dict | None = None) -> RequestResponse:
        async with self._session.get(url, headers=headers, params=params) as r:
            data = await r.json()
            response = RequestResponse(data, r.status)
        return response

    async def get_file(self, url: str, headers: dict | None = None, params: dict | None = None) -> RequestResponse:
        async with self._session.get(url, headers=headers, params=params) as r:
            data = await r.read()
            response = RequestResponse(data, r.status)
        return response

    async def put(self, url: str, headers: dict = None, params: dict = None, data: dict | bytes = None,
                  response_type: str = "json"):
        async with self._session.put(url, headers=headers, params=params, data=data) as r:
            if response_type == "json":
                data = await r.json()
                response = RequestResponse(data, r.status)
            else:
                response = RequestResponse(None, r.status)
        return response

    async def patch(self, url: str, headers: dict):
        pass

    async def delete(self, url: str, headers: dict):
        pass

    async def close(self):
        await self._session.close()
