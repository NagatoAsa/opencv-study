import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# 图像金字塔
# 图像金字塔是图像多尺度表达的一种，最主要用于图像的分割，是一种以多分辨率来解释图像的有效但概念简单的结构
# 图像金字塔用于机器视觉和图像压缩，一幅图像的金字塔是一系列以金字塔形状排列的分辨率逐步降低，且来源于同一张原始图片的图像集合，直到达到某个终止条件才停止采样
# 金字塔的底部是待处理图像的高分辨率表示，而顶部是低分辨率的近似，层级越高，图像越小，分辨率越低
#　cv.pyrUp(img)  对图像进行上采样
#　cv.pyrDown(img)  对图像进行下采样

# 原图
img = cv.imread("kids.jpg")
plt.imshow(img[..., ::-1])
plt.show()

# 上采样
imgup = cv.pyrUp(img)
plt.imshow(imgup[..., ::-1])
plt.show()

# 下采样
imgdown = cv.pyrDown(img)
plt.imshow(imgdown[..., ::-1])
plt.show()
