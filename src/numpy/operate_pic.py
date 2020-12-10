import numpy as np
import consts
from logging import *
import math

base_matrix = np.arange(64).reshape([8, 8])


def correct_pos(shape, pos):
    return 0 <= pos[0] < shape[0] and 0 <= pos[1] < shape[1]


def process_matrix(trans_matrix):
    info(f"\n{trans_matrix}\n")
    shape = base_matrix.shape
    translate_target = np.zeros(base_matrix.shape)
    for row in range(shape[0]):
        for column in range(shape[1]):
            src_pos = np.dot(trans_matrix, np.array([row, column, 1]).T).astype(np.int)
            if correct_pos(shape, src_pos):
                translate_target[row, column] = base_matrix[src_pos[0], src_pos[1]]
    info(f"\n{translate_target}\n")
    return translate_target


# 输入矩阵
info(f"\n{base_matrix}\n")

# 平移
scale_vec = [-2, -3]
translate_matrix = np.identity(3)
translate_matrix[0:2, 2] = scale_vec
process_matrix(translate_matrix)

# 旋转
rotate_angle = math.pi / 4
rotate_matrix = np.identity(3)
rotate_matrix[0:2, 0:2] = np.array(
    [[math.cos(rotate_angle), -math.sin(rotate_angle)], [math.sin(rotate_angle), math.cos(rotate_angle)]])
process_matrix(rotate_matrix)

# 缩放
scale_vec = [0.5, 0.5]
scale_matrix = np.identity(3)
scale_matrix[0, 0] = scale_vec[0]
scale_matrix[1, 1] = scale_vec[1]
process_matrix(scale_matrix)

# 错切
