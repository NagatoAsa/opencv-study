import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
# Harris检测演示
# dst = cv.cornerHarris(src, blockSize, ksize, k)
# 参数
#   1.src：数据类型为float32的输入图像
#   2.ksize：角点检测中要考虑的领域大小
#   3.ksize：sobel求导使用的核大小
#   4.k：角点检测方程中的自由参数，取值参数为[0.04, 0.06]

img = cv.imread('chessboard.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray = np.float32(gray)
dst = cv.cornerHarris(gray, 2, 3, 0.04)
img[dst > 0.01*dst.max()] = [0, 0, 255]
plt.figure(figsize=(10,10))
plt.imshow(img[..., ::-1])
plt.show()
