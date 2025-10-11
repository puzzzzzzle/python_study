import copy
import sys
import sysconfig
import time

import tqdm
from concurrent.futures import ThreadPoolExecutor

print('python version is: ', sys.version)

gil_status = sysconfig.get_config_var("Py_GIL_DISABLED")
print(gil_status)
assert gil_status == 1


def fib(n):
    a, b = 1, 1
    for i in range(n - 1):
        a, b = b, a + b
    return a


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

r = (1000_000_000_000_000_000, 1000_000_000_000_000_010)


total = []
start_time = time.time()
print(f"start multi thread {r[1] - r[0]}")
with ThreadPoolExecutor(max_workers=r[1] - r[0]) as executor:
    # for ret in executor.map(fib, range(*r)): # right
    for ret in executor.map(is_prime, range(*r)): # wrong, 竞争变量i, 导致只有单线程在跑
        total.append(ret)
print(f"multi thread time use {time.time() - start_time}")
print(total)

total = []
start_time = time.time()
for i in tqdm.tqdm(range(*r),total=r[1]-r[0]):
    total.append(is_prime(i))
print(f"single thread time use {time.time() - start_time}")
print(total)
