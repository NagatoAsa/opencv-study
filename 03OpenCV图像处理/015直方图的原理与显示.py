import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
# 直方图的原理与显示

# 灰度直方图
# 原理
# 图像直方图是用以表示数字图像中亮度分布的直方图，标绘了图像中每个亮度值的像素个数。
# 这种直方图中，横坐标左侧为较暗的区域，而右侧为较亮的区域。
# 因此一张较暗图片的直方图中数据多集中于左侧和中间部分，而整体明亮，只有少量阴影的图像则相反
# 灰度直方图是按照灰度图进行绘制的，而不是彩色图像
# 直方图的一些术语与细节：
# dims：需要统计的特征数目，在上例中，dims=1，因为仅仅统计了灰度值
# bins：每个特征空间子区段的数目，即组距
# range：要统计特征的取值范围，在上例中，range=[0， 255]
# 直方图的意义
# 直方图是图像中像素强度分布的图形表达式
# 它统计了每一个强度值所具有的像素个数
# 不同的图像的直方图可能是相同的

# 直方图的计算与绘制
# 我们使用OpenCV中的方法统计直方图，并使用matplotlib将其绘制出来
# cv.calcHist(image, channels, mask, histSize, ranges[, hist[, accumulate]])
# 参数
#   1.images：原图像，当传入函数时应该用中括号[]括起来，例如：[img]
#   2.channels：如果输入的图象是灰度图，它的值就是[0]，如果是彩色图像的话，传入的参数可以是[0]，[1]，[2]它们分别对应着通道B、G、R
#   3.mask：掩模图像。要统计整幅图像的直方图就把它设为None。但是如果你想统计图像的某一部分的直方图的话，你就需要制作一个掩模图像，并使用它。
#   4.histSize：分组数目。也应该用中括号括起来，如：[256]
#   5.ranges：像素值范围，通常为[0, 256]

img = cv.imread("cat.jpeg", 0)
plt.imshow(img, cmap=plt.cm.gray)
plt.show()
hist = cv.calcHist([img], [0], None, [256], [0, 256])
plt.figure(figsize=(10, 8), dpi=80)
plt.plot(hist)
plt.show()
