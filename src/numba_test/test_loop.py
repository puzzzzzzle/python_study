import numpy as np
import numba
from numba import jit
import time
import logging

import consts

logger = logging.getLogger(__name__)


def time_me(fn):
    def _wrapper(*args, **kwargs):
        start = time.process_time()
        ret = fn(*args, **kwargs)
        logger.info(f"{fn.__name__} costs {time.process_time() - start}")
        return ret

    return _wrapper


@time_me
def loop_local(arr):
    ret = 0
    for i in arr:
        ret += i
    return ret


@time_me
@numba.jit(nopython=True, )
def loop_ba(arr):
    ret = 0
    for i in arr:
        ret += i
    return ret


if __name__ == '__main__':
    logger.info("start")
    arr = np.arange(10000000)
    logger.info(loop_local(arr))
    logger.info(loop_ba(arr))
