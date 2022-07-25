import logging
import numpy as np
import math
import cv2

import consts

logger = logging.getLogger(__name__)


def distance(p1, p2):
    return math.sqrt(((p2[0] - p1[0]) ** 2) + ((p2[1] - p1[1]) ** 2))


class TerrainSimple:
    def __init__(self, sed, width, height, dtype=np.int32):
        import random
        r = random.Random(sed)
        self.r = r
        self.shape = (width, height)
        self.dtype = dtype
        self.range_h = None
        self.height_arr = None

    def h(self, row, column):
        """
        需要覆写这个方法
        """
        return 0

    def arr_h(self, row, column):
        return self.arr()[row][column]

    def arr(self):
        if self.height_arr is None:
            logger.info("start build arr")
            width, height = self.shape
            min_h = max_h = 0
            arr = np.zeros((width, height), dtype=self.dtype)
            for i_column in range(width):
                logger.debug(f"build rand info ... {i_column}/{width}")
                for i_row in range(height):
                    i_h = self.h(i_row, i_column)
                    arr[i_row][i_column] = i_h
                    max_h = max(max_h, i_h)
                    min_h = min(min_h, i_h)
            self.height_arr = arr.astype(dtype=self.dtype)
            self.range_h = (min_h, max_h)
        return self.height_arr

    def color_default(self, height):
        min_h, max_h = self.range_h
        color_min = np.array([30, 30, 30])
        color_max = np.array([255, 255, 255])
        color_diff = color_max - color_min
        return ((height - min_h) / max_h) * color_diff + color_min

    def to_height_img(self, color):
        logger.info("start build img")
        width, height = self.shape
        # 初始化图像
        img = np.zeros((width, height, 3), np.uint8)
        # 分配颜色
        for i_column in range(width):
            logger.debug(f"build show img ... {i_column}/{width}")
            for i_row in range(height):
                i_h = self.arr_h(i_row, i_column)
                img[i_column][i_row] = color(i_h)
        return img.astype(dtype=np.uint8)

    pass


TerrainBase = TerrainSimple


class CycleTerrain(TerrainBase):
    def __init__(self, sed, width, height, r_min, r_max, cycle_num):
        super().__init__(sed, width, height, np.int32)
        centers = []
        for i in range(cycle_num):
            centers.append((self.r.randint(0, height), self.r.randint(0, width), self.r.randint(r_min, r_max)))
        self.centers = centers

        # 初始化地形高度
        self.arr()

    def h(self, row: int, column: int):
        # 比任何一个中心点都进就使用新的
        for item in self.centers:
            if distance((item[0], item[1]), (row, column)) < item[2]:
                return 100
        return 5


class CycleRayTerrain(TerrainBase):
    def __init__(self, sed, width, height, min_r, max_r, cycle_num, default_height=5):
        super().__init__(sed, width, height, np.int32)

        centers = []
        for i in range(cycle_num):
            centers.append((self.r.randint(0, height), self.r.randint(0, width), self.r.randint(min_r, max_r)))
        self.centers = centers
        self.default_height = default_height
        # 初始化地形高度
        self.arr()

    def h(self, row: int, column: int):
        rnd = self.default_height
        for item in self.centers:
            i_len = distance((item[0], item[1]), (row, column))
            if i_len < item[2]:
                i_len = max(i_len, 1)
                this_ret = 100 * (item[2] - i_len) / item[2]
                rnd = max(rnd, this_ret)
        return int(rnd)


def test_show(r: TerrainBase):
    # 初始化图像
    img = r.to_height_img(r.color_default)
    cv2.imshow(f"{type(r)}", img)
    logger.info("end gen pos, show img")

    pass


def main():
    test_show(CycleRayTerrain(42, 500, 500, 100, 150, 20))
    test_show(CycleTerrain(42, 500, 500, 50, 100, 5))

    cv2.waitKey()
    cv2.destroyAllWindows()
    pass


if __name__ == '__main__':
    main()
