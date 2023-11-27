import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
# 中值滤波
# 中值滤波是一种典型的非线性滤波技术，基本思想使用像素点邻域灰度值的中值代替该像素点的灰度值
# 中值滤波对椒盐噪声来说尤其有用，因为它不依赖于邻域内那些与典型值差别很大的值
# cv.medianBlur(src, ksize)
# 参数
#   1.src：输入图像
#   2.ksize：卷积核的大小

img = cv.imread("dogsp.jpeg")
plt.imshow(img[..., ::-1])
plt.show()
img2 = cv.medianBlur(img, 3)
plt.imshow(img2[..., ::-1])
plt.show()
