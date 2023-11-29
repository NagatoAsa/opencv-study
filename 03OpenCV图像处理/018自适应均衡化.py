import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
# 自适应均衡化
# 前文提到的直方图均衡，考虑的是图像的全局对比度，在完成均衡化后，图片的对比度被改变，但同时有一部分太暗而丢失了信息，效果并不好
# 为了解决这个问题，需要使用自适应的直方图均衡化
# 此时，整幅图像会被分为很多小块，这些小块被称为“tiles”（在OpenCV中的“tiles”的大小默认是8*8），然后再对每一个小块分别进行直方图均衡化
# 所以在每一个的区域中，直方图会集中在某一个小的区域中
# 如果有噪声的话，噪声会被放大
# 为了避免这种情况的出现，要使用对比度限制
# 对于每一个小块来说，如果直方图中的组距超过对比度上线的话，就把其中的像素点均匀分散到其他组距中，然后再进行直方图均衡化
# cv.creatCLAHE(clipLimit, tileGridSize)
# 参数
#   1.clipLimit：对比度限制，默认为40
#   2.tileGridSize：分块的大小，默认为8*8

img = cv.imread("cat.jpeg", 0)
plt.imshow(img, cmap=plt.cm.gray)
plt.show()
# 实例化一个CLAHE对象
cl = cv.createCLAHE(2.0, (8, 8))
# 将该对象应用到图像
clahe = cl.apply(img)
plt.imshow(clahe, cmap=plt.cm.gray)
plt.show()
hist1 = cv.calcHist([img], [0], None, [256], [0, 256])
hist2 = cv.calcHist([clahe], [0], None, [256], [0, 256])
plt.plot(hist1)
plt.show()
plt.plot(hist2)
plt.show()
