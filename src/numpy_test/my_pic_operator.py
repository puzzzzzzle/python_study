import cv2
import math
import numpy as np
from pathlib import Path
from matplotlib import pyplot as plt
import functools
import logging

try:
    import consts

    data_dir = consts.projectDir
except ImportError:
    data_dir = "./"

logger = logging.getLogger(__name__)


def _print_transform(func):
    @functools.wraps(func)
    def print_transform(self, *args, **kwargs):
        logger.info(f"start call !{func.__name__}! transform is \n{self.transform}")
        ret = func(self, *args, **kwargs)
        logger.info(f"end call !{func.__name__}! transform is \n{self.transform}")
        return ret

    return print_transform


class PicOperator(object):
    def __init__(self):
        # self.src_img = src_img
        self.transform = np.identity(3)

    @staticmethod
    def __prepare_dest(src_img, shape):
        return np.zeros(shape, dtype=src_img.dtype)

    @staticmethod
    def correct_pos(pos, src_img):
        row, column = src_img.shape[:2]
        return 0 <= pos[0] < row and 0 <= pos[1] < column

    @_print_transform
    def process_inv_manul(self, src_img):
        ret = self.__prepare_dest(src_img, src_img.shape[:2])
        row, column = ret.shape[:2]
        for c_row in range(row):
            for c_column in range(column):
                src_pos = np.round(self.transform @ np.array([c_row, c_column, 1])).astype(np.int)
                if self.correct_pos(src_pos, src_img):
                    ret[c_row, c_column] = src_img[src_pos[0], src_pos[1]]
        return ret

    @_print_transform
    def process_by_cv(self, src_img):
        temp_transform = self.transform[0:2, :].astype(np.float)
        out_size = list(np.array(src_img.shape[:2]) * 2)
        out_size.reverse()
        ret = cv2.warpAffine(src_img, temp_transform, tuple(out_size))
        return ret


    @_print_transform
    def move(self, vec):
        """
        平移, 右下方向为负, 左上方向为正
        :param vec:
        :return:
        """
        assert len(vec) == 2
        temp_ident = np.array([
            [1, 0, vec[0]],
            [0, 1, vec[1]],
            [0, 0, 1]
        ])
        self.transform = self.transform @ temp_ident
        return self

    @_print_transform
    def zoom(self, vec):
        """
        缩放,
        :param vec: >1 放大 <1 缩小到原来的1/vec
        :return:
        """
        assert len(vec) == 2
        temp_ident = np.array([
            [vec[0], 0, 0],
            [0, vec[1], 0],
            [0, 0, 1]
        ])
        self.transform = self.transform @ temp_ident
        return self

    @_print_transform
    def rotate(self, rotate_angle, center=None):
        """
        旋转
        :param center: 旋转中心
        :param rotate_angle: 顺时针角度 为正, 默认(0,0)点(右上角)
        :return:
        """
        rotate_center = np.identity(3)
        if center is not None:
            rotate_center = np.array([
                [1, 0, center[0]],
                [0, 1, center[1]],
                [0, 0, 1]
            ])

        rotate_angle = math.radians(rotate_angle)
        temp_ident = np.array([
            [math.cos(rotate_angle), -math.sin(rotate_angle), 0],
            [math.sin(rotate_angle), math.cos(rotate_angle), 0],
            [0, 0, 1]
        ])
        self.transform = rotate_center @ self.transform @ temp_ident @ np.linalg.inv(rotate_center)
        return self


if __name__ == '__main__':
    pic_path = Path(data_dir) / "data/ignore_file/test1.png"
    assert pic_path.exists()
    src = cv2.imread(str(pic_path), cv2.IMREAD_COLOR)
    oper = PicOperator()
    plt.figure()
    plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))
    # img.vertically()  # 镜像
    oper.rotate(-45, np.array(src.shape[:2]) / 2)  # 旋转
    oper.move([-50, -50])  # 平移
    oper.zoom([2, 2])  # 缩放
    plt.figure()
    plt.imshow(cv2.cvtColor(oper.process_by_cv(src), cv2.COLOR_BGR2RGB))
    plt.show()
