from multiprocessing import Process, Pool, Queue, Pipe, Manager
import multiprocessing
from consts import get_logger

logger = get_logger(__name__)


def f(name, q):
    count = 0
    while True:
        count += 1
        if count % 10000000 == 0:
            val = f"name:{name}  at {count}"
            logger.info(f"put {val}")
            q.put(val)


if __name__ == '__main__':
    p = Pool(3)
    m = Manager()
    q = m.Queue()
    tasks = [(f"name_{x}", q) for x in range(6)]
    p.starmap(f, tasks)
    while True:
        item = q.get()
        logger.info(f"get {item}")
