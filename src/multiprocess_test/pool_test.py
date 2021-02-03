from multiprocessing import Process, Pool, Queue, Pipe, Manager, Barrier
from consts import get_logger

logger = get_logger(__name__)


def f(name, q, v):
    logger.info(f"start f {name}")
    count = 0
    """
    比起while True, v.value 在访问非常频繁的情况下, 慢两个数量级, 估计内部有很多锁与同步...
    """
    while v.value > 0:
        count += 1
        if count % 100000 == 0:
            val = f"name:{name}  at {count}"
            logger.info(f"put {val}")
            q.put(val)
            v.value -= 1
    logger.info(f"end f {name}")


def c(q, v):
    logger.info(f"start c")
    while v.value > 0 or len(q) > 0:
        item = q.get()
        logger.info(f"get {item}")
    logger.info(f"end c")


if __name__ == '__main__':
    p = Pool(4)
    m = Manager()
    q = m.Queue()
    v = m.Value('i', 10)

    tasks = [(f"name_{x}", q, v) for x in range(6)]
    p.apply_async(c, (q, v))
    p.starmap(f, tasks)

    p.close()
    p.join()
