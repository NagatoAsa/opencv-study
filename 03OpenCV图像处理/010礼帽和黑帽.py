import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
# 礼貌和黑帽

# 礼帽运算
# 为原图像与开运算的结果图之差，如下式计算
# dst = tophat(src, element) = src - open(src, element)
# 因为开运算带来的结果是放大了裂缝或者局部低亮度的区域，因此，从原图中减去开运算后的图，得到的效果图突出了比原图轮廓周围的区域更明亮的区域，且这一操作和选择的核的大小相关
# 礼帽运算用来分离比邻近点亮一些的斑块。当一幅图像具有大幅的背景的时候，而微小物品比较有规律的情况下，可以使用礼帽运算进行背景提取

# 黑帽运算
# 为闭运算的结果图与原图像之差，如下式计算
# dst = blackhat(scr, element) = close(src, element) - src
# 黑帽运算后的效果图突出了比原图轮廓周围区域更暗的区域，且这一操作与选择的和大小相关
# 黑帽运算用来分离比邻近点暗一些的斑块

# cv.morphologyEx(img, op, kernel)
# 参数
#   1.img：要处理的图像
#   2.op：处理方式
#       cv.MORPH_TOPHAT 礼帽运算
#       cv.MORPH_BLACKHAT 黑帽运算
#   3.kernel：核结构

img_open = cv.imread("letteropen.png")
plt.imshow(img_open[..., ::-1])
plt.show()
img_close = cv.imread("letterclose.png")
plt.imshow(img_close[..., ::-1])
plt.show()
kernel = np.ones((10, 10), np.uint8)
top = cv.morphologyEx(img_open, cv.MORPH_TOPHAT, kernel)
plt.imshow(top[..., ::-1])
plt.show()
black = cv.morphologyEx(img_close, cv.MORPH_BLACKHAT, kernel)
plt.imshow(black[..., ::-1])
plt.show()
