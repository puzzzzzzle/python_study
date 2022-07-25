import math
import random
import numpy as np
import cv2
import consts

logger = consts.get_logger(__name__)


def distance(p1, p2):
    return math.sqrt(((p2[0] - p1[0]) ** 2) + ((p2[1] - p1[1]) ** 2))


# 双线随机有问题, 不可用
#
# class ClusterSpaceRandom_ERROR:
#     """
#     带权重的空间随机分布算法
#     空间消耗: O(n)
#     时间消耗: o(n)
#     n:地形边长
#
#     需要实现 h函数, 用来返回每个点的权重
#     """
#
#     def __init__(self, width, height):
#         logger.info("start init random")
#         self.shape = (width, height)
#         width_weight = [0 for _ in range(width)]
#         height_weight = [0 for _ in range(height)]
#         i_max = i_min = 0
#         for i_column in range(width):
#             for i_row in range(height):
#                 i_h = self.h(i_row, i_column)
#                 width_weight[i_column] += i_h
#                 height_weight[i_row] += i_h
#                 i_max = max(i_max, i_h)
#                 i_min = min(i_min, i_h)
#         self.width_weight = width_weight
#         self.height_weight = height_weight
#         self.width_sum = sum(width_weight)
#         self.height_sum = sum(height_weight)
#         self.i_max = i_max
#         self.i_min = i_min
#         logger.info("end init random")
#         pass
#
#     def h(self, row: int, column: int):
#         """
#         返回高度(权重)信息
#         每次访问需要返回一致的数值
#         """
#         return 0
#
#     def rand(self):
#         return self.rand_one(self.height_weight, self.height_sum), self.rand_one(self.width_weight, self.width_sum)
#
#     @staticmethod
#     def rand_one(ls, wh):
#         rnd = random.randint(0, wh)
#         for i in range(len(ls)):
#             if rnd < ls[i]:
#                 return i
#             else:
#                 rnd -= ls[i]


class ClusterSpaceRandomLinearRand:
    """
    带权重的空间随机分布算法
    使用权重线单性随机实现
    """

    def __init__(self, width, height):
        self.shape = (width, height)
        i_max = i_min = 0
        arr = np.zeros((width, height), dtype=np.int32)
        weight_arr = np.zeros(width * height)
        weight_all = 0
        for i_column in range(width):
            logger.debug(f"build rand info ... {i_column}/{width}")
            for i_row in range(height):
                i_h = self.h(i_row, i_column)
                arr[i_row][i_column] = i_h
                i_max = max(i_max, i_h)
                i_min = min(i_min, i_h)
                weight_arr[i_row * width + i_column] = i_h
                weight_all += i_h
        self.i_max = i_max
        self.i_min = i_min
        self.weight_arr = weight_arr
        self.weight_all = weight_all

        logger.info("end init random")
        self.arr = arr
        pass

    def to_label(self, row, column):
        return row * self.shape[0] + column
        pass

    def from_label(self, label):
        row = int(label / self.shape[0])
        column = int(label % self.shape[0])
        return row, column
        pass

    def h(self, row: int, column: int):
        """
        返回高度(权重)信息
        每次访问需要返回一致的数值
        """
        return 0

    def rand(self):
        ret = -1
        rnd = random.randint(0, self.weight_all)
        for i in range(len(self.weight_arr)):
            if rnd < self.weight_arr[i]:
                ret = i
                break
            else:
                rnd -= self.weight_arr[i]
        assert ret != -1
        return self.from_label(ret)


class ClusterSpaceRandomNpRand:
    """
    带权重的空间随机分布算法
    使用numpy的单线性随机实现
    """

    def __init__(self, width, height):
        self.shape = (width, height)
        i_max = i_min = 0
        arr = np.zeros((width, height), dtype=np.int32)
        for i_column in range(width):
            logger.debug(f"build rand info ... {i_column}/{width}")
            for i_row in range(height):
                i_h = self.h(i_row, i_column)
                arr[i_row][i_column] = i_h
                i_max = max(i_max, i_h)
                i_min = min(i_min, i_h)
        self.i_max = i_max
        self.i_min = i_min
        logger.info("end init random")
        self.arr = arr
        pass

    def h(self, row: int, column: int):
        """
        返回高度(权重)信息
        每次访问需要返回一致的数值
        """
        return 0

    def rand(self):
        linear_idx = np.random.choice(self.arr.size, p=self.arr.ravel() / float(self.arr.sum()))
        return np.unravel_index(linear_idx, self.arr.shape)


# 上面两种方式原理一直, np的块一些, 先使用np的了
ClusterSpaceRandom = ClusterSpaceRandomNpRand


class CycleRandom(ClusterSpaceRandom):
    """
    简单的带几个中心点的随机分布测试
    圆形 阶梯分布策略
    """

    def __init__(self, width, height, r_min, r_max, cycle_num):
        centers = []
        for i in range(cycle_num):
            centers.append((random.randint(0, height), random.randint(0, width), random.randint(r_min, r_max)))

        self.centers = centers
        ClusterSpaceRandom.__init__(self, width, height)

    def h(self, row: int, column: int, ):
        # 比任何一个中心点都进就使用新的
        for item in self.centers:
            if distance((item[0], item[1]), (row, column)) < item[2]:
                return 100
        return 5


class CycleRayRandom(ClusterSpaceRandom):
    """
    简单的带几个中心点的随机分布测试
    圆形放射分布策略
    """

    def __init__(self, width, height, min_r, max_r, cycle_num, default_rand=5):
        centers = []
        for i in range(cycle_num):
            centers.append((random.randint(0, height), random.randint(0, width), random.randint(min_r, max_r)))

        self.centers = centers
        self.default_rand = default_rand
        ClusterSpaceRandom.__init__(self, width, height)

    def h(self, row: int, column: int, ):
        rnd = self.default_rand
        for item in self.centers:
            i_len = distance((item[0], item[1]), (row, column))
            if i_len < item[2]:
                i_len = max(i_len, 1)
                this_ret = 100 * (item[2] - i_len) / item[2]
                rnd = max(rnd, this_ret)
        return int(rnd)


def test_show(r: ClusterSpaceRandom, point_num):
    width = r.shape[0]
    height = r.shape[1]

    logger.info("start build img")

    # 初始化图像
    img = np.zeros((width, height, 3), np.uint8)
    # 初始化颜色
    img = np.where(img == (0, 0, 0), (255, 255, 255), (255, 255, 255)).astype(dtype=np.uint8)
    # 分配颜色
    color_min = np.array([30, 30, 30])
    color_max = np.array([255, 255, 255])
    color_diff = color_max - color_min
    for i_column in range(width):
        logger.debug(f"build show img ... {i_column}/{width}")
        for i_row in range(height):
            i_h = r.h(i_row, i_column)
            c = ((i_h - r.i_min) / r.i_max) * color_diff + color_min
            img[i_column][i_row] = c

    logger.info("end build img, start gen rand pos")
    # 随机生成一批点
    for i in range(point_num):
        if i % 100 == 0:
            logger.debug(f"gen pos ... {i}/{point_num}")
        pos = r.rand()
        # 画在图像上
        cv2.circle(img, pos, 3, (0, 0, 0), -1)

    cv2.imshow(f"{type(r)}", img)
    logger.info("end gen pos, show img")

    pass


if __name__ == '__main__':
    # test_show(CycleRayRandom(500, 500, 50, 150, 10), 1000)

    # 圆阶梯分布, 目前只有两阶, 有需要可以调
    # 宽, 长, 聚集带最小半径, 聚集带最大半径,  聚集带数量,
    # test_show(CycleRandom(500, 500, 50, 150, 10), 1000)

    # 圆形放射分布策略
    # 宽, 长, 聚集带最小半径, 聚集带最大半径, 聚集带数量, 每个点最小概率,  取样数量
    test_show(CycleRayRandom(500, 500, 100, 150, 20, 100), 400)

    cv2.waitKey()
    cv2.destroyAllWindows()
