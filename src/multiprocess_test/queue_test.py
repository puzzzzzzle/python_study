from multiprocessing import Process, Pool, Queue, Pipe, Manager

from consts import get_logger

logger = get_logger(__name__)

q = Queue()


class MyProcess(Process):
    def __init__(self, name, q):
        super().__init__()
        self.name = name
        """
        spawn
        The parent process starts a fresh python interpreter process. The child process will only inherit those resources necessary to run the process objects run() method. In particular, unnecessary file descriptors and handles from the parent process will not be inherited. Starting a process using this method is rather slow compared to using fork or forkserver.
        
        Available on Unix and Windows. The default on Windows.
        
        fork
        The parent process uses os.fork() to fork the Python interpreter. The child process, when it begins, is effectively identical to the parent process. All resources of the parent are inherited by the child process. Note that safely forking a multithreaded process is problematic.
        
        Available on Unix only. The default on Unix.
        
        forkserver
        When the program starts and selects the forkserver start method, a server process is started. From then on, whenever a new process is needed, the parent process connects to the server and requests that it fork a new process. The fork server process is single threaded so it is safe for it to use os.fork(). No unnecessary resources are inherited.
        
        Available on Unix platforms which support passing file descriptors over Unix pipes.
        关键点:
        Process对象是一个完全独立的对象, 也就是说, 全局空间中的q并不共享, 在新的process中, 全局空间的q对象也是新的
        但是我们需要q对象使用同一个
        按照官方doc, process会继承自己所需要的所有资源, 也就是说, 如果通过init传进来支持多进程的对象, 会使用同一个
        这样就实现了进程间通信
        """
        self.q = q

    def run(self) -> None:
        count = 0
        while True:
            count += 1
            if count % 10000000 == 0:
                val = f"name:{self.name}  at {count}"
                logger.info(f"put {val}")
                self.q.put(val)


if __name__ == '__main__':

    process_list = []
    for i in range(4):
        p = MyProcess(f"process_{i}", q)
        p.start()
        process_list.append(p)
    while True:
        item = q.get()
        logger.info(f"get {item}")
    for i in process_list:
        p.join()
