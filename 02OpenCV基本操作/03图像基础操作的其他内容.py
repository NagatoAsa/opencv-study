import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# 获取并修改图像中的像素点
# 我们可以通过行和列的坐标值获取该像素点的像素值，对于BGR图像，它返回一个蓝、绿、红值的数组。
# 对于灰度图像，进返回相应的强度值，使用相同的方法对像素值进行修改。

img = np.zeros((256, 256, 3), np.uint8)
plt.imshow(img[..., ::-1])
plt.show()
print(img[100, 100])
print(img[100, 100, 0])
img[100, 100] = [0, 0, 255]
plt.imshow(img[..., ::-1])
plt.show()
print(img[100, 100])

# 获取图像的属性
#   img.shape形状
#   img.size图像大小
#   img.dtype数据类型

print(img.shape)
print(img.dtype)
print(img.size)

# 图像通道的拆分与合并
# 有些时候需要在B、G、R通道图像上单独工作，这种情况下，需要将BGR图像分割为单个通道。
# 或在其他情况下，可能需要将这些单独的通道合并到BGR图像
# 通道拆分
# b, g, r = cv.split(img)
# 通道合并
# img = cv.merge((b, g, r))

dili = cv.imread("dili.jpg")
plt.imshow(dili[..., ::-1])
plt.show()
b, g, r = cv.split(dili)
plt.imshow(b, cmap=plt.cm.gray)
plt.show()
img2 = cv.merge((b, g, r))
plt.imshow(img2[..., ::-1])
plt.show()

# 色彩空间的改变
# OpenCV中有150多种颜色空间转换方法，最广泛使用的转换方法有两种：BGR与Gray互转和BGR与HSV互转
# cv.cvtColor(input_image, flag)
# 参数
#   1.input_image：进行颜色空间转换的图像
#   2.flag：转换类型
#       cv.COLOR_BGR2GRAY：BGR转Gray
#       cv.COLOR_BGR2HSV：BGR转HSV

gray = cv.cvtColor(dili, cv.COLOR_BGR2GRAY)
plt.imshow(gray, cmap=plt.cm.gray)
plt.show()
hsv = cv.cvtColor(dili, cv.COLOR_BGR2HSV)
plt.imshow(hsv)
plt.show()
