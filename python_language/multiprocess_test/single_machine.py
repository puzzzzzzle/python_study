import random
from multiprocessing import Pool, Manager
from time import sleep

from tqdm import tqdm


def worker(args) -> str:
    index , arg2,counter = args
    sleep(0.5)
    counter[f"{index}"] = 1
    return f"index: {index}; data: {str(arg2)}"

def master():
    with Manager() as manager, Pool(processes=32) as pool:
        counter = manager.dict()
        tasks = [(x, random.randbytes(16),counter) for x in range(100)]
        result = list(tqdm(pool.imap_unordered(worker, tasks)))
        for result in result:
            print(result)
        for key, value in counter.items():
            print(f"{key}: {value}")

if __name__ == '__main__':
    master()