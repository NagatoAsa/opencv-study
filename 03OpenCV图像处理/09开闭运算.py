import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
# 开闭运算
# 开运算和闭运算是将腐蚀和膨胀按照一定的次序进行处理。但这两者并不是可逆的，即先开后闭并不能得到原来的图像

# 开运算
# 开运算是先腐蚀后膨胀，其作用是：分离物体，消除小区域。
# 特点：消除噪点，去除小的干扰块，而不影响原来的图像

# 闭运算
# 闭运算与开运算相反，是先先膨胀后腐蚀，作用是消除或闭合物体的孔洞
# 特点：可以填充闭合区域

# cv.morphologyEx(img, op, kernel)
# 参数
#   1.img：要处理的图像
#   2.op：处理方式：若进行开运算，则设为cv.MORPH_OPEN，若进行闭运算，则设为cv.MORPH_CLOSE
#   3.kernel：核结构

img_open = cv.imread("letteropen.png")
plt.imshow(img_open[..., ::-1])
plt.show()
img_close = cv.imread("letterclose.png")
plt.imshow(img_close[..., ::-1])
plt.show()
kernel = np.ones((10, 10), np.uint8)
cvopen = cv.morphologyEx(img_open, cv.MORPH_OPEN, kernel)
plt.imshow(cvopen[..., ::-1])
plt.show()
cvclose = cv.morphologyEx(img_close, cv.MORPH_CLOSE, kernel)
plt.imshow(cvclose[..., ::-1])
plt.show()
