import consts
import asyncio
import time
import logging

logger = logging.getLogger(__name__)
debug = logger.debug


async def say_after(delay, before, after):
    debug(before)
    await asyncio.sleep(delay)
    debug(after)


async def single():
    debug(f"started at {time.strftime('%X')}")

    await say_after(1, 'sb1', 'sf1')
    await say_after(2, 'sb2', 'sf2')

    debug(f"finished at {time.strftime('%X')}")


async def same_time():
    task1 = asyncio.create_task(
        say_after(1, 'tb1', 'tf1'))

    task2 = asyncio.create_task(
        say_after(1, 'tb1', 'tf1'))

    debug(f"started at {time.strftime('%X')}")

    await task1
    await task2

    debug(f"finished at {time.strftime('%X')}")


if __name__ == '__main__':
    co_obj = same_time()
    debug(f"{co_obj}  {str(co_obj)}")
    asyncio.run(co_obj)
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(co_obj)