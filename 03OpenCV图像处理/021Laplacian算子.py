import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
# Laplacian算子
# Laplacian是利用二阶导数来检测边缘，因为图象是二维，我们需要在两个方向上求导，如下式所示：
# Δsrc = Δsrc^2/Δx^2+Δsrc^2/Δy^2
# 不连续函数的二阶导数是：
# f''(x)=f'(x+1)-f'(x)=f(x+1)+f(x-1)-2f(x)
# 使用的卷积核是：
# [[0, 1, 0], [1, -4, 1], [0, 1, 0]]
# laplacian = cv.Laplacian(src, ddepth, [, dst[, ksize[, scale[, delta[, borderType]]]]])
# 参数
#   1.src：需要处理的图像
#   2.ddpeh：图像的深度，-1表示采用的是原图像相同的深度，目标图像的深度必须大于等于原图像的深度
#   3.ksize：算子的大小，即卷积核的大小，必须为奇数,默认为3

img = cv.imread("horse.jpg", 0)
plt.imshow(img, cmap=plt.cm.gray)
plt.show()
res = cv.Laplacian(img, cv.CV_16S)
res = cv.convertScaleAbs(res)
plt.imshow(res, cmap=plt.cm.gray)
plt.show()
