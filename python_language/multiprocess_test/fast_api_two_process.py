import uuid
import asyncio
from rich.console import Console

from fastapi import FastAPI
from multiprocessing import Process, Manager
import uvicorn

app = FastAPI()

console = Console()
manager = Manager()
task_queue = manager.Queue()
result_dict = manager.dict()
# 用于存放 asyncio.Future，key为task_id
future_dict = {}


@app.get("/process")
async def process(data: int):
    task_id = str(uuid.uuid4())
    loop = asyncio.get_event_loop()

    console.print(f"start process: {task_id} data: {data}")
    fut = loop.create_future()
    future_dict[task_id] = fut

    # 放入任务队列
    task_queue.put((task_id, data))

    # 等待结果
    result = await fut
    console.print(f"get result: {result}")
    return {"result": result}


### worker
def worker(task_queue, result_dict):
    console = Console()
    while True:
        try:
            task_id, data = task_queue.get(timeout=10)
        except Exception as e:
            continue
        console.print(f"process: {task_id} data: {data}")
        # 这里做耗时处理
        result = data * 2  # 举例
        result_dict[task_id] = result


def start_worker():
    # 启动工作进程
    p = Process(target=worker, args=(task_queue, result_dict))
    p.start()
    return p

async def result_listener():
    """在A进程中运行，监听B进程处理结果，唤醒协程"""
    while True:
        try:
            task_id, result = result_dict.popitem()
        except KeyError:
            await asyncio.sleep(0.1)
            continue
        try:
            fut = future_dict.pop(task_id, None)
            if fut:
                # 需要在主线程事件循环中设置结果
                loop = asyncio.get_event_loop()
                if not loop.is_closed():
                    loop.call_soon_threadsafe(fut.set_result, result)
        except Exception as e:
            console.print_exception()
            continue

async def result_listener_wrapper():
    """包装器函数用于启动监听任务"""
    await result_listener()

# 启动结果监听协程
@app.on_event("startup")
async def startup_event():
    # 在事件循环启动后创建任务
    asyncio.create_task(result_listener())


def start_server():
    # 启动工作进程
    start_worker()
    # 启动FastAPI
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    # 启动A进程
    start_server()
