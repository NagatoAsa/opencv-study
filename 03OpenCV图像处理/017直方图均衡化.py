import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
# 直方图均衡化
# 对于一副图像，假设其亮度很高，则灰度值都会集中在一个较高的水平，所以应该把它的直方图做一个横向拉伸，就可以扩大图像像素值的分布范围，提高图像的对比度，这就是直方图均衡化要做的事情
# “直方图均衡化”是把原始图像的灰度直方图从比较集中的某个灰度区间变成在更广泛灰度范围内的分布
# 直方图均衡化是对图像进行非线性拉伸，重新分配图像像素值，使一定灰度范围内的像素数量大致相同
# 这种方法提高图像整体的对比度，特别是有用数据的像素值分布比较接近时，在X光图像中使用广泛，可以提高骨架结构的显示，另外在曝光过度或不足的图像中可以更好地突出细节
# cv.equalizeHist(img)
# 参数
#   1.img：灰度图

img = cv.imread("cat.jpeg", 0)
plt.imshow(img, cmap=plt.cm.gray)
plt.show()
dst = cv.equalizeHist(img)
plt.imshow(dst, cmap=plt.cm.gray)
plt.show()
hist1 = cv.calcHist([img], [0], None, [256], [0, 256])
hist2 = cv.calcHist([dst], [0], None, [256], [0, 256])
plt.plot(hist1)
plt.show()
plt.plot(hist2)
plt.show()
