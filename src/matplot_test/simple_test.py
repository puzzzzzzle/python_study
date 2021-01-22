from matplotlib import pyplot as plt
import numpy as np


def fig():
    fig = plt.figure()


# fig()


def one_ax():
    fig, ax = plt.subplots()
    x = np.linspace(0, 2, 100)
    ax.plot(x, x ** 3)


one_ax()

plt.show()
