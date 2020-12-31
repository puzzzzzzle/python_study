import time
import logging
import consts
import asyncio
import aiohttp
import random

logger = logging.getLogger(__name__)
info = logger.info


async def get(url):
    session = aiohttp.ClientSession()
    logger.debug(f"{url} before get")
    response = await session.get(url)
    logger.debug(f"{url} before text")
    result = await response.text()
    logger.debug(f"{url} before close")
    await session.close()
    logger.debug(f"{url} before result")
    return result


async def request():
    url = f'http://127.0.0.1:5000/name_{random.randint(0, 1000)}'
    info(f'Waiting for {url}', )
    result = await get(url)
    info(f'Get response from {url} Resul: {result}')


if __name__ == '__main__':
    start = time.time()
    tasks = [asyncio.ensure_future(request()) for _ in range(5)]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))

    end = time.time()
    info(f'Cost time: {end - start}')
