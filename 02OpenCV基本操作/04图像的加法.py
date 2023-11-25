import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# 图像的加法
# 可以使用OpenCV的cv.add()把两幅图像相加，或者简单地通过numpy操作添加两个图像，如res = img1 + img2。两个图像应该具有相同的大小和类型，或者第二个图像可以是标量值
# 注：OpenCV加法和Numpy加法之间存在差异OpenCV的加法是饱和操作，而Numpy添加是模运算
# numpy对8位整数进行计算：250 + 10 = 260 => 4
# OpenCV对8位整数进行计算：250 + 10 = 260 => 255
# 这种差别在对两幅图像进行加法时会更加明显，OpenCV的结果会更好一些，所以尽量使用OpenCV中的函数

rain = cv.imread("rain.jpg")
plt.imshow(rain[:, :, ::-1])
plt.show()
view = cv.imread("view.jpg")
plt.imshow(view[:, :, ::-1])
plt.show()
img1 = cv.add(rain, view)
plt.imshow(img1[:, :, ::-1])
plt.show()
img2 = rain + view
plt.imshow(img2[:, :, ::-1])
plt.show()
