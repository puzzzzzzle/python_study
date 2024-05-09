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

def time_call(fn,*args, **kwargs):
    start = time.time()
    ret = fn(*args, **kwargs)
    logger.info(f"{fn.__name__} costs {time.time() - start}")
    return ret


def loop_local(arr):
    ret = 0
    for i in arr:
        arr += i
    return ret


@numba.jit(nopython=True, )
def loop_ba(arr):
    ret = 0
    for i in arr:
        arr += i
    return ret


if __name__ == '__main__':
    logger.info("start")
    arr = np.arange(100000)
    time_call(loop_local,arr)
    time_call(loop_local,arr)
    # 第一次要编译
    time_call(loop_ba,arr)
    # 第二次使用编译缓存
    time_call(loop_ba,arr)
    code = loop_ba.inspect_llvm()
    import pprint
    # pprint.pprint(code)
    with open("test.ir","wt") as f:
        for k, v in code.items():
            f.write(v)

