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

    async def download_file(self, path: str) -> bytes:
        url = f"{self.disk_url}/resources/download"
        response = await self._req_maker.get(url, self._headers, params={"path": path})
        if not response.status_code == 200:
            raise

        download_href = response.data.get("href")
        if not download_href:
            raise

        file = await self._req_maker.get_file(download_href)
        return file.data

    async def upload_file(self, path: str, file: bytes) -> None:
        download_href = await self._get_upload_href_for_file(path)
        response = await self._req_maker.put(url=download_href, data=file, response_type="")

        if response.status_code != 201 and response.status_code != 202:
            raise
        return

    async def get_meta_info_about_path(self, path: str):
        url = f"{self.disk_url}/resources"
        response = await self._req_maker.get(url, self._headers, params={"path": path})
        return response.data

    async def get_meta_info_about_disk(self):
        url = f"{self.disk_url}"
        response = await self._req_maker.get(url, self._headers)

        return response.data

    async def create_folder(self, path: str, name: str):
        url = f"{self.disk_url}/resources"
        data = {"path": f"{path}/{name}"}
        response = await self._req_maker.put(url, self._headers, data)

        return response.data

    async def _get_upload_href_for_file(self, path: str, overwrite: bool = False) -> str:
        url = f"{self.disk_url}/resources/upload"
        params = {"path": path}

        response = await self._req_maker.get(url, params=params, headers=self._headers)
        download_href = response.data.get("href")
        print(response.data)
        if not download_href:
            raise
        return download_href


async def main():
    token = ""
    req_maker = RequestMaker()
    serv = YandexDiskService(token, req_maker)
    with open("img.png", mode="rb") as f:
        res = await serv.upload_file("test_upload6.png", f.read())

    await req_maker.close()


if __name__ == "__main__":
    asyncio.run(main())
