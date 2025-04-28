import sys
from multiprocessing import Process
from multiprocessing.managers import BaseManager
from queue import Queue
import random
import time
from threading import Thread

ADDR = ('localhost', 50000)
AUTH_KEY = b'abracadabra'


class MyManager(BaseManager):
    pass


def master():
    task_queue = Queue()
    result_queue = Queue()
    # 具名化共享对象, 两个queue必须先放在栈上, 再注册到manager
    MyManager.register('get_task_queue', callable=lambda: task_queue)
    MyManager.register('get_result_queue', callable=lambda: result_queue)
    m = MyManager(address=ADDR, authkey=AUTH_KEY)
    m.start()

    # 必须通过代理来访问共享对象, 否则数据同步会出错
    task_queue :Queue= m.get_task_queue()
    result_queue :Queue= m.get_result_queue()
    tasks = [(x, random.randbytes(16)) for x in range(100)]
    for task in tasks:
        task_queue.put(task)
    results = []
    while len(results) < len(tasks):
        try:
            result = result_queue.get(timeout=1)
            results.append(result)
            print(f"get result : {result}; {len(results)}/{len(tasks)}")
        except Exception as e:
            print(f"get result fail , continue {len(results)}/{len(tasks)}")
            continue

def client():
    MyManager.register('get_task_queue')
    MyManager.register('get_result_queue')

    m = None
    while True:
        try:
            m = MyManager(address=ADDR, authkey=AUTH_KEY)
            m.connect()
            print("connected")
            break
        except Exception as e:
            print(f"connect error")
            time.sleep(1)

    task_queue :Queue= m.get_task_queue()
    result_queue :Queue= m.get_result_queue()

    while not task_queue.empty():
        try:
            task = task_queue.get(timeout=1)
            print(f"get task : {task}")
            index, arg2 = task
            result = f"index: {index}; data: {str(arg2)}"
            result_queue.put(result)
        except Exception as e:
            print(f"get task error:{e}")
            continue

if __name__ == '__main__':
    # 使用两个进程，一个主进程，一个客户端进程
    master_thread = Thread(target=master)
    master_thread.start()

    client_process = Process(target=client)
    client_process.start()

    master_thread.join()
    client_process.join()
