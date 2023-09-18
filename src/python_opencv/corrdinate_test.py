import cv2
import numpy as np

# shape : row(行) column(列) color
# shape : row : y方向 高度, column: x轴方向, 宽度, color: 颜色宽度
mat = np.empty((200, 400, 3))
mat[:, :] = (255, 255, 255)

# 假设左上为原点, y轴向下
# 访问一个坐标点(x:10,y:190), 应该使用(190,10)的方式
# cv使用 (行, 列) 的方式访问数组, 本质上是行列式
# 使用行列式格式, 第一个数字是行, 第二个数字是列
mat[190:192, 10:12] = (0, 0, 0)

# !!!!!!!  cv2 使用和numpy相反的访问方式 !!!!!!!!
# cv2 使用左上为原点的方式理解图形, y轴向下
# np的 坐标点(100,300) 对应cv2 的(300, 100)
cv2.circle(mat, (20, 190), 3, (0, 0, 0), -1)

cv2.imshow("2", mat)

cv2.imwrite("test.png",mat)

temp = cv2.imread("test.png")
cv2.imshow("temp", temp)

# 标准第一象限坐标系 与 np 坐标系 转换
def pos_quartile_np(pos, shape, is_quartile_pos):
    """
    :param is_quartile_pos: pos 是第一象限点吗
    """
    if is_quartile_pos:
        return shape[0] - pos[1] - 1, pos[0]
    else:
        return pos[1], shape[0] - pos[0] - 1


# 标准第一象限坐标系 与 cv2 坐标系 转换
def pos_quartile_cv(pos, shape):
    return pos[0], shape[0] - pos[1] - 1


p1 = (20, 100)  # 第一象限坐标点
# np格式的不可以来回转
# assert p1 == pos_quartile_2_np(pos_quartile_2_np(p1, mat.shape), mat.shape)
assert p1 == pos_quartile_np(pos_quartile_np(p1, mat.shape, True), mat.shape, False)

# cv格式的可以来回转
assert p1 == pos_quartile_cv(pos_quartile_cv(p1, mat.shape), mat.shape)

# mat[:, :] = (255, 255, 255)
# 使用cv画
cv2.circle(mat, pos_quartile_cv(p1, mat.shape), 5, (0, 0, 0), -1)
# 使用np画(np的向上+10 吧, 不然重叠了)
p1 = (p1[0], p1[1] + 10)
np_p1 = pos_quartile_np(p1, mat.shape, True)
mat[np_p1[0] - 5:np_p1[0] + 5:, np_p1[1] - 5:np_p1[1] + 5] = (0, 0, 0)

cv2.imshow("trans", mat)

cv2.waitKey()
cv2.destroyAllWindows()
