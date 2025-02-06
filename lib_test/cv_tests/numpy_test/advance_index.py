import numpy as np
import logging

logging.basicConfig(level=logging.DEBUG)
arr = np.arange(75).reshape(5, 5, 3)
logging.info(arr.shape)
logging.info(arr)
# 花式索引, 取 第一维为0和2的地方的所有数组(二维)
logging.info(arr[[0, 2]])
# 花式索引, 取 第一维为(0,0)和(2,1)的地方的所有数组(一维)
logging.info(arr[[0, 2],
[0, 1]])
arr[[0, 2], [0, 1]] = [[99, 99, 99],
                       [3, 4, 5, ]]
logging.info(arr[[0, 2],
[0, 1]])
# 整数索引, 取 (0,0,0) (2,1,1)处的值
logging.info(arr[[0, 2],
[0, 1],
[0, 2]])

# bool 索引中, 索引结束, 返回的一定是一维数组
# 布尔掩码（mask）的形状始终与原始数组（arr）的形状相同。这是因为布尔掩码是通过对原始数组的每个元素应用某种条件（例如，比较操作）来生成的。
# 布尔索引, 比较维度为0, 比较每个元素
mask = arr == 99
logging.info(mask.shape)
logging.info(mask)
logging.info(arr[mask])
arr[mask] = 0
logging.info(arr)

# 布尔索引, 比较维度为1, 取前两个维度为坐标, 第三个维度当做一个整体
mask = arr == (0, 0, 0)
logging.info(mask.shape)
logging.info(mask)
logging.info(arr[mask])
arr[mask] = (128, 129, 130)
logging.info(arr)
