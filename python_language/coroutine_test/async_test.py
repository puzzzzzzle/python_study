import asyncio
import consts

log = consts.get_logger(__name__)


# generator
def generator_test1(end):
    a = 0
    while a < end:
        yield a
        a += 1
    return 42


t1 = generator_test1(3)
print(type(t1))
print([x for x in t1])


# async_generator

async def async_generator1(end):
    a = 0
    while a < end:
        await asyncio.sleep(0.1)
        inp = yield a
        print(f"inp : {inp}")
        a += 1


print(async_generator1(3))


async def async_runner():
    ret = []
    async for num in async_generator1(3):
        ret.append(num)
    print(ret)


asyncio.run(async_runner())


# coroutine
async def coro_test2(end):
    a = 0
    while a < end:
        await asyncio.sleep(0.1)
        a += 1


c2 = coro_test2(3)
print(type(c2))
asyncio.run(c2)

# error :
# def coro_test3(end):
#     a = 0
#     while a < end:
#         await asyncio.sleep(0.5)
