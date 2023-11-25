import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# 图像的透射变换
# 透射变换是视角变换的结果，是利用投影中心、像点、目标点三点共线的条件，按照透视旋转定律使承影面绕透视轴旋转某一角度，破坏原有投影光线束，仍能保持承影面上投影的几何图形不变的变换
# 仿射变换保持了二维图形的“平直性”（直线经过变换之后依然是直线）和“平行性”（二维图形之间的相对位置关系保持不变，平行线依然是平行线，且直线上点的位置顺序不变）
# 获取变换矩阵
# cv.getPerspectiveTransform
# 该函数需要传入两个列表，每个列表四个坐标，两个列表分别对应变换前与变换后
# 应用变换
# cv.warpPerspective

img = cv.imread("kids.jpg")
plt.imshow(img[..., ::-1])
plt.show()
rows, cols = img.shape[:2]
print(rows, cols)
pst1 = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])
pst2 = np.float32([[100, 145], [300, 100], [80, 290], [310, 300]])
T = cv.getPerspectiveTransform(pst1, pst2)
res = cv.warpPerspective(img, T, (cols, rows))
plt.imshow(res[..., ::-1])
plt.show()
