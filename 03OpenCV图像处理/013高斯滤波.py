import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
# 高斯滤波
# 进行高斯滤波需要设置一个权重矩阵，该矩阵会对图像进行扫描，矩阵中心的像素会被置会以权重矩阵覆盖的区域的二维高斯函数（以矩阵中心为均值）作为权重赋予每一个被权重矩阵覆盖的每一个像素的加权平均数（最后权重矩阵的结果会进行归一化以使概率总和为1）
# cv.GaussianBlur(src, ksize, sigmaX, sigmaY, borderType)
# 参数
#   1.src：输入图像
#   2.ksize：高斯卷积核的大小，注意：卷积核的宽度和高度都应为奇数，且可以不同
#   3.sigmaX：水平方向的标准差
#   4.sigmaY：垂直方向的标准差，默认为0，表示与sigmaX相同
#   5.borderType：填充边界类型

img = cv.imread("dogGauss.jpeg")
plt.imshow(img[..., ::-1])
plt.show()
img2 = cv.GaussianBlur(img, (3, 3), 1)
plt.imshow(img2[..., ::-1])
plt.show()
