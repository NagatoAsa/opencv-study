# OpenCV基本操作
# 图像的IO操作

# ·读取图像
# ·cv.imread
# ·参数
#   1.要读取的图像
#   2.读取方式的标志
#       cv.IMREAD * COLOR：以彩色方式加载图像，任何图像的透明度都将被忽略（默认参数）
#       cv.IMREAD * GRAYSCALE：以灰度模式加载图像
#       cv.IMREAD_UNCHANGED：包括alpha通道加载图像模式
#   可以使用1、0、-1分别代表上面三种标志

import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
img = cv.imread("dili.jpg")
img2 = cv.imread("dili.jpg", 0)
# 若加载路径有错误，不会报错，会返回一个None值

# ·显示图像
# ·cv.imshow()
# ·参数
#   1.显示图像的窗口名称，以字符串类型表示
#   2.要加载的图像
# 注意：在调用显示图像的函数后，要调用cv.waitKey()
# 给图像绘制留下时间，否则窗口会出现无响应情况，并且图像无法显示出来（参数中填入等待时间，0为永远）
# 另外也可以使用matplotlib对图像进行显示
#   plt.imshow(img[:, :, ::-1])
# 这里对图像进行索引切片的目的是为了将颜色通道进行反转（opencv使用的是BGR通道，而matplotlib使用的是RGB通道）

# 显示全彩图片
cv.imshow("dili", img)
cv.waitKey(0)
cv.destroyAllWindows()
# 使用matplotlib进行显示
plt.imshow(img[:, :, ::-1])
plt.show()
# 显示灰度图片
plt.imshow(img2, cmap=plt.cm.gray)
plt.show()

# ·保存图像
# ·cv.imwrite()
# ·参数
#   1.文件名、文件路径
#   2.要保存的图像

cv.imwrite("dilireba.png", img2)
