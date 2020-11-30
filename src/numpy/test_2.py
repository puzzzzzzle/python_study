import numpy as np
from matplotlib import pyplot as plt
from logging import *
import consts as co
import sys
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

mpl.rcParams['legend.fontsize'] = 20  # mpl模块载入的时候加载配置信息存储在rcParams变量中，rc_params_from_file()函数从文件加载配置信息
font = {
    'color': 'b',
    'style': 'oblique',
    'size': 20,
    'weight': 'bold'
}


def __khcall_test_sac1():
    fig = plt.figure(figsize=(16, 12))  # 参数为图片大小
    ax = fig.gca(projection='3d')  # get current axes，且坐标轴是3d的
    p1 = np.array([[2, -1, 0, ],[-1, 2, -1],[0, -3, 4]])
    for p in p1:
        ax.scatter(p[0],p[1],p[2], alpha=0.6)


if __name__ == '__main__':
    co.auto_run(__name__, "__khcall")
    plt.show()
