import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

# 图像平滑
# 图像平滑从信号处理的角度看就是去除其中的高频信息，保留低频信息。因此我们可以对图像实施低通滤波。低通滤波可以去除图像中的噪声，对图像进行平滑。
# 根据滤波器的不同可分为均值滤波、高斯滤波、中值滤波、双边滤波

# 均值滤波
# 采用均值滤波模板对图像噪声进行滤除，需要设置一个卷积核（边长为奇数的方阵），该卷积核会覆盖于原图像的每一个像素点上，而卷积核中心覆盖的像素值会被置为卷积核覆盖的所有像素的像素值的均值
# 均值滤波的优点是算法简单，计算速度较快，缺点是在去噪的同时去除了很多细节部分，将图像变得模糊（类似于马赛克）
# cv.blur(src, ksize, anchor, borderType)
# 参数
#   1.src：输入图像
#   2.ksize：卷积核的大小
#   3.anchor：默认值为(-1, -1)，表示核中心
#   4.borderType：边界类型（由于边界区域无法被卷积核处理，故需要指定对边界的处理方式）

img = cv.imread("dogsp.jpeg")
plt.imshow(img[..., ::-1])
plt.show()
img2 = cv.blur(img, (5, 5))
plt.imshow(img2[..., ::-1])
plt.show()
