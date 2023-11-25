import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# 图像旋转
# 思路：将所有的像素点进行移动
# 公式：x'=rcos(α-θ)；y'=rcos(α-θ)  （r为旋转矩阵的对角线长，θ为旋转角，α为旋转角与旋转矩阵对角线与x轴的夹角之和）
# 获取旋转矩阵
# cv2.getRotationMatrix2D(center, angle, scale)
# 参数：
#   1.angle：旋转中心
#   2.angle:旋转角度
#   3.scale：缩放比例
# 该函数能够返回旋转矩阵
# 图像的平移与旋转本质上是图像矩阵的线性变换
# 最后是调用cv.warpAffine完成图像的旋转
img = cv.imread("kids.jpg")
plt.imshow(img[:, :, ::-1])
plt.show()
rows, cols = img.shape[:2]
print(rows, cols)
M = cv.getRotationMatrix2D((cols/2, rows/2), 45, 1)
res = cv.warpAffine(img, M, (cols, rows))
plt.imshow(res[:, :, ::-1])
plt.show()
M = cv.getRotationMatrix2D((cols/2, rows/2), 45, 0.5)
res = cv.warpAffine(img, M, (cols, rows))
plt.imshow(res[:, :, ::-1])
plt.show()
