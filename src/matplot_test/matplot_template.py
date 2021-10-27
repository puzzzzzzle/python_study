import time
import numpy as np
import cv2

import matplotlib.pyplot as plt


def draw_lines():
    fig, ax = plt.subplots()  # type:plt.Figure,plt.Axes
    ax.axis("equal")
    ax.set_title(f"test {time.asctime()}")
    x = [4, 9, 8, 7, 3]
    y = [4, 1, 4, 4, 3]
    ax.plot(x, y, "-")
    ax.plot(x, y, "o")


draw_lines()


def draw_math():
    fig, ax = plt.subplots()  # type:plt.Figure,plt.Axes
    ax.set_title(f"draw_math {time.asctime()}")
    x = np.arange(-100, 100) # step 默认为1
    y = x**3
    ax.plot(x, y, "o")


draw_math()
plt.show()
