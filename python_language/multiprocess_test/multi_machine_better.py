import sys
from multiprocessing import Process
from multiprocessing.managers import BaseManager
from queue import Queue
import random
import time
from threading import Thread
from tqdm import tqdm

ADDR = ('localhost', 50000)
AUTH_KEY = b'abracadabra'

# 再复杂的可以考虑ray等框架
class QueueManager(BaseManager):
    def get_task_queue(self) -> Queue: ...

    def get_result_queue(self) -> Queue: ...

    @staticmethod
    def create_queue_manager(address, authkey):
        task_queue = Queue()
        result_queue = Queue()

        # 每次都创建一次类, 多次调用类和对象都不同
        class MyManager(QueueManager): pass

        MyManager.register('get_task_queue', callable=lambda: task_queue)
        MyManager.register('get_result_queue', callable=lambda: result_queue)
        return MyManager(address=address, authkey=authkey)


def master():
    tasks = [(x, random.randbytes(16)) for x in range(100)]
    with QueueManager.create_queue_manager(address=ADDR, authkey=AUTH_KEY) as m, tqdm(total=len(tasks), desc="Processing",
                                                                         file=sys.stdout) as pbar:
        # 必须通过代理来访问共享对象, 否则数据同步会出错
        task_queue_proxy = m.get_task_queue()
        result_queue_proxy = m.get_result_queue()
        for task in tasks:
            task_queue_proxy.put(task)
        results = []
        while len(results) < len(tasks):
            try:
                result = result_queue_proxy.get(timeout=1)
                results.append(result)
                pbar.update(1)
                # print(f"get result : {result}; {len(results)}/{len(tasks)}")
            except Exception as e:
                # print(f"get result fail , continue {len(results)}/{len(tasks)}")
                continue


def client():
    # 连接服务器
    m = None
    while True:
        try:
            m = QueueManager.create_queue_manager(address=ADDR, authkey=AUTH_KEY)
            m.connect()
            print("connected")
            break
        except Exception as e:
            print(f"connect error")
            time.sleep(1)

    task_queue_proxy = m.get_task_queue()
    result_queue_proxy = m.get_result_queue()

    while not task_queue_proxy.empty():
        try:
            task = task_queue_proxy.get(timeout=1)
            index, arg2 = task
            time.sleep(0.5)
            result = f"index: {index}; data: {str(arg2)}"
            result_queue_proxy.put(result)
        except Exception as e:
            print(f"get task error:{e}")
            continue


if __name__ == '__main__':
    # 使用两个进程，一个主进程，一个客户端进程
    processes = []
    master_process = Process(target=master)
    master_process.start()
    processes.append(master_process)

    for _ in range(3):
        client_process = Process(target=client)
        client_process.start()
        processes.append(client_process)

    for p in processes:
        p.join()
