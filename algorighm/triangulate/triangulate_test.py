import random

from triangulate import triangulate, Point


def draw_img(shape, points, triangles):
    import numpy as np
    import cv2

    img = np.empty((shape[0] + 30, shape[1] + 30, 3))
    img[:] = (255, 255, 255)
    for p in points:
        cv2.circle(img, p.int_2d(), 3, (0, 0, 0), -1)
    # cv2.imshow("", img)
    print(len(triangles))
    for t in triangles:
        cv2.line(img, points[t.p1].int_2d(), points[t.p2].int_2d(), (0, 0, 0), 2)
        cv2.line(img, points[t.p1].int_2d(), points[t.p3].int_2d(), (0, 0, 0), 2)
        cv2.line(img, points[t.p3].int_2d(), points[t.p2].int_2d(), (0, 0, 0), 2)
    cv2.imshow("", img)

    cv2.waitKey()
    cv2.destroyAllWindows()


def main():
    nv = 20
    shape = [400, 400]
    # make points
    points = []
    for i in range(nv + 3):
        points.append(Point(random.randint(0, shape[0]), random.randint(0, shape[1])))
    # sort
    points = sorted(points, key=lambda x: x.x)
    triangles = triangulate(points)
    # triangles = []

    # 画图
    draw_img(shape, points, triangles)

    pass


if __name__ == '__main__':
    main()
    pass
