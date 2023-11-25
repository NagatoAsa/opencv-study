import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# 图像的仿射变换
# 图像的仿射变换相当于将二维平面上的每个坐标点与一个2*3的矩阵相乘
# 需要注意的是，在填写坐标的时候要记得图像的原点在左上角
# 在OpenCV中，仿射变换的矩阵是一个2*3的矩阵
# cv.getAffineTransform
# 该函数需要传入两个列表，分别保存三个坐标，这两个列表中的坐标分别是发生仿射变化前与仿射变化后的点的坐标，会创建一个2*3的变换矩阵
img = cv.imread("kids.jpg")
plt.imshow(img[..., ::-1])
plt.show()
rows, cols = img.shape[:2]
pos1 = np.float32([[50, 50], [200, 50], [50, 200]])
pos2 = np.float32([[100, 100], [200, 50], [100, 250]])
M = cv.getAffineTransform(pos1, pos2)
res = cv.warpAffine(img, M, (cols, rows))
plt.imshow(res[..., ::-1])
plt.show()
