import aiohttp
from app.config.settings import settings
import asyncio


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get(url=settings.request_url) as response:
            print(await response.json())


if __name__ == "__main__":
    asyncio.run(main())