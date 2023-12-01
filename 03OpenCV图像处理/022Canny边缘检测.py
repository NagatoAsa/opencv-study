import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
# Canny边缘检测
# Canny边缘检测算法是一种非常流行的边缘检测算法，被认为是最优的边缘检测算法
# 原理
# Canny边缘检测算法是由四步构成，分别为：
# 第一步：噪声去除
# 由于边缘检测很容易受到噪声的影响，所以首先使用5*5高斯滤波器去除噪声
# 第二步：计算图像梯度
# 对平滑后的图像使用Sobel算子计算水平方向和竖直方向的一阶导数
# 根据得到的这两幅梯度的（Gx和Gy）找到边界的梯度和方向，公式如下：
# Edge_Gardient(G) = sqrt(Gx^2+Gy^2)
# Angle(θ)=1/tan(Gy/Gx)
# 如果某个像素点是边缘，则其梯度方向总是与边缘垂直。梯度方向被归为四类：垂直、水平和两个对角线方向
# 第三步：非极大值抑制
# 在获得梯度的方向和大小后，对整幅图像进行扫描，去除那些非边界上的点。对每一个像素进行检查，看这个点的梯度是不是周围具有相同梯度方向的点中最大的
# A点位于图像的边缘，在其梯度变化方向，选择像素点B和C，用来检验A点的梯度是否为极大值，若为极大值，则进行保留，否则A点被抑制，最终结果是具有”细边“的二进制图像
# 第四步：滞后阈值
# 现在要确定真正的边界，我们设置两个阈值：minVal和maxVal
# 当图像的弧度梯度高于maxVal被认为是真的边界，低于minVal的边界会被抛弃
# 如果介于两者，就要看这个点是否与某个被确定为真正的边界点相连，如果是就认为它也是边界点，如果不是就抛弃
# 故选择合适的maxVal和minVal非常重要
# canny = cv.Canny(image, threshould1, threshould2)
# 参数
#   1.image：灰度图
#   2.threshold1：minVal，较小的阈值将间断的边缘连接起来
#   3.threshold2：maxVal，较大的阈值检测图像中明显的边缘

img = cv.imread("horse.jpg", 0)
plt.imshow(img, cmap=plt.cm.gray)
plt.show()
res = cv.Canny(img, 0, 100)
plt.imshow(res, cmap=plt.cm.gray)
plt.show()
