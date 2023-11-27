import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
# 腐蚀与膨胀
# 腐蚀与膨胀是最基本的形态学操作，腐蚀与膨胀是相对于白色部分（高亮部分）而言的
# 膨胀就是使图像中高亮部分扩张，效果图拥有比原图更大的高亮区域
# 腐蚀是原图中的高亮部分被蚕食，效果图中拥有比原图更小的高亮区域
# 膨胀是求局部最大值的操作，腐蚀是求局部最小值的操作

# 腐蚀
# 具体操作是：用一个结构元素（图像）扫描图像中的每一个像素，用结构元素中的每一个像素与其覆盖做“与”操作，结构元素的中的及其对应覆盖的原图的像素都为1，则该像素为1，否则为0
# 腐蚀的作用是消除物体边界点，使目标缩小，可以消除小于结构元素的噪声点
# cv.erode(img, kernel, iterations)
# 参数
#   1.img：要处理的图像
#   2.核结构（即结构元素）
#   3.iteration：腐蚀的次数，默认是1

# 膨胀
# 具体操作是：用一个结构元素（图像）扫描图像中的每一个像素，用结构元素中的每一个像素与其覆盖做“或”操作，只有结构元素中像素及其覆盖的对应的像素都为0才会将该像素置为0，否则为1
# 作用是将与物体接触的所有背景点合并到物体中，使目标增大，可填补目标中的孔洞
# cv.dilate(img, kernel, iteration)
# 参数
#   1.img：要处理的图像
#   2.kernel：核结构（即结构元素）
#   3.iteration：腐蚀的次数

img = cv.imread("letter.png")
plt.imshow(img[..., ::-1])
plt.show()
kernel = np.ones((5, 5), np.uint8)
img2 = cv.erode(img, kernel)
plt.imshow(img2[..., ::-1])
plt.show()
img3 = cv.dilate(img, kernel)
plt.imshow(img3[..., ::-1])
plt.show()
