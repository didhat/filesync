import asyncio

import aiohttp

from src.aioreq.base import AbstractRequestMaker
from src.disks.base import BaseDiskService
from src.aioreq.aiorequesr import RequestMaker
from src.disks.yandex.headers import get_header_for_request


class YandexDiskService(BaseDiskService):
    disk_url = "https://cloud-api.yandex.net/v1/disk"

    def __init__(self, token: str, req_maker: AbstractRequestMaker):
        self._token = token
        self._req_maker = req_maker
        self._headers = get_header_for_request(token)

    async def get_file_from_path(self, path: str):
        pass

    async def download_file(self, name: str, ile: bytes):
        pass

    async def upload_file(self, path: str) -> bytes:
        pass

    async def get_meta_info_about_disk(self):
        url = f"{self.disk_url}"
        data = await self._req_maker.get(url, self._headers)
        return data


async def main():
    token = ""
    async with aiohttp.ClientSession() as s:
        req_maker = RequestMaker(s)
        serv = YandexDiskService(token, req_maker)
        res = await serv.get_meta_info_about_disk()
        print(res)


if __name__ == "__main__":
    asyncio.run(main())
