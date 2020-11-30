import numpy as np
from matplotlib import pyplot as plt
from logging import *
import consts as co
import sys


def __khcall_test_plt():
    plt.figure("aha")
    plt.grid(True)
    x = np.linspace(0, 2 * np.pi, 50)
    plt.plot(x, np.sin(x))


def __khcall_test_arange():
    plt.figure()
    plt.grid(True)
    x = np.arange(0, 4 * np.pi, 0.1)
    y = np.sin(x)
    plt.plot(x, y, 'b-o', x, np.cos(x) + 1, 'r-^')


def __khcall_test_mat():
    plt.figure()
    plt.legend()
    plt.grid(True)
    x = np.arange(0, 10)  # error only np array support
    y = 2 * x
    plt.plot(x, y)
    plt.figure()


def __khcall_test_sac1():
    plt.figure()
    x = np.arange(0, 4 * np.pi, 0.1)
    y = np.sin(x)
    plt.plot(x, y, 'bo')


def __khcall_test_sac2():
    info(f"{sys._getframe().f_code.co_name}")
    plt.figure(f"{sys._getframe().f_code.co_name}")
    x = np.arange(0, 8 * np.pi, 0.1)
    y = np.sin(x)
    plt.scatter(x, y)


def __khcall_test_sac3():
    plt.figure()
    plt.title("rand scatter")
    import functools
    total = 200
    rand = functools.partial(np.random.randint, 0, size=total, dtype=np.int_)

    x = rand(200)
    y = rand(200)
    size = rand(40)
    color = rand(200)
    plt.scatter(x, y, size, color)
    # 显示颜色条
    plt.colorbar()


if __name__ == '__main__':
    co.auto_run(__name__, "__khcall")
    plt.show()
