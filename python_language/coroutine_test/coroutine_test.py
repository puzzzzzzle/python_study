import consts

log = consts.get_logger(__name__)
import asyncio


async def say_defer(time, what):
    await asyncio.sleep(time)
    log.info(f"say {what} after {time}")
    return f"said {what}"


# 正常执行协程
asyncio.run(say_defer(1, "hahah"))  # 1s 后输出

log.info("next")


def test_func():
    return "nothing"


# 普通函数无法作为函数执行
# 只能用于执行可等待对象
# 协程, 任务 和 Future
try:
    asyncio.run(test_func())
except ValueError as e:
    log.info(f"{e} happeneds")  # a coroutine was expected, got 'nothing' happeneds

# async 函数返回的是一个协程对象
task_say = say_defer(1, "task_say")
log.info(f"""type of say_defer(1,"task_say") {type(task_say)}""")  # type of say_defer(1,"task_say") <class 'coroutine'>
# 并没有执行中
log.info(task_say.cr_running)
# 执行它
asyncio.run(task_say)


log.info("next")
