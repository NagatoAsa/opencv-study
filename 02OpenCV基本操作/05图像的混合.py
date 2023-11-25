import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# 图像的混合
# 图像的混合也是一种加法，但是不同的两幅图像的权重不同，可以显示出混合或者透明的感觉
# 思路：res = (1 - α)img1 + αimg2（α为权重）
# cv.addWeighted(img1, α, img2, β, γ)
# 要将两张图混合在一起，第一张图的权重为0.7，第二张图的权重为0.3。函数cv.addWeighted()可以按下面的公式对图片进行混合操作
# dist = α·img1 + β·img2 + γ （这里γ取零）

img1 = cv.imread("rain.jpg")
img2 = cv.imread("view.jpg")
plt.imshow(img1[:, :, ::-1])
plt.show()
plt.imshow(img2[:, :, ::-1])
plt.show()
img3 = cv.addWeighted(img2, 0.7, img1, 0.3, 0)
plt.imshow(img3[:, :, ::-1])
plt.show()
img3 = cv.addWeighted(img2, 0.3, img1, 0.7, 0)
plt.imshow(img3[:, :, ::-1])
plt.show()
