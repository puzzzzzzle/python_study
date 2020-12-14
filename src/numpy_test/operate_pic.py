import numpy as np
import consts
from logging import *
import math
import cv2
from pathlib import Path

base_matrix = np.arange(64).reshape([8, 8])
pic_name = str(Path(consts.projectDir) / "data/ignore_file/test1.png")
base_matrix = cv2.imread(pic_name)


def correct_pos(shape, pos):
    return 0 <= pos[0] < shape[0] and 0 <= pos[1] < shape[1]


def process_matrix(trans_matrix):
    info(f"\n{trans_matrix}\n")
    shape = base_matrix.shape
    translate_target = np.zeros(base_matrix.shape, dtype=base_matrix.dtype)
    for row in range(shape[0]):
        for column in range(shape[1]):
            src_pos = np.dot(trans_matrix, np.array([row, column, 1])).astype(np.int)
            if correct_pos(shape, src_pos):
                translate_target[row, column] = base_matrix[src_pos[0], src_pos[1]]
    cv2.imshow("pic", translate_target)
    cv2.waitKey()
    return translate_target


# 平移
scale_vec = [-20, -30]
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
