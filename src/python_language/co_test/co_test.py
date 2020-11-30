import src
import asyncio
import time
from logging import *


async def say_after(delay, what):
    await asyncio.sleep(delay)
    debug(what)


async def single():
    debug(f"started at {time.strftime('%X')}")

    await say_after(1, 'hello')
    await say_after(2, 'world')

    debug(f"finished at {time.strftime('%X')}")


async def same_time():
    task1 = asyncio.create_task(
        say_after(1, 'hello'))

    task2 = asyncio.create_task(
        say_after(1, 'world'))

    debug(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    await task1
    await task2

    debug(f"finished at {time.strftime('%X')}")


if __name__ == '__main__':
    co_obj = same_time()
    debug(f"{co_obj}  {str(co_obj)}")
    asyncio.run(co_obj)
