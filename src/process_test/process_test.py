import os
import multiprocessing
import time

def worker(index):
    print(f'worker {index} started : pid {os.getpid()} , ppid {os.getppid()}')
    time.sleep(1)
    print(f'worker {index} end')


def process_run(index):
    worker(index)
    if index < 5:
        process = multiprocessing.Process(target=process_run, args=[index + 1])

        """
        普通的子进程, 主进程退出后, 子进程不会退出, 可以创建多级子进程

        如果标记为守护进程, 主进程退出后, 子进程会随之结束, 但不能创建多级子进程
        """

        # process.daemon = True
        process.start()
        process.join()
    print(f'process {index} end : pid {os.getpid()} , ppid {os.getppid()}')


if __name__ == '__main__':
    # 启动新进程, 子进程也要启动QApplication, 不能用线程, 每个进程中有个单例
    process_run(0)
