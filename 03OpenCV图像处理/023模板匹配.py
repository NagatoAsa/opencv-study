import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
# 模板匹配
# 原理
# 所谓模板匹配，就是在给定的图片中查找和模板最相似的区域
# 该算法的输入包括模板和图片，整个任务的思路就是按照滑窗的思路不断移动模板图片，计算与图像中相对应区域的匹配度，最终将匹配度最高的区域选择为最终的结果
# 实现流程
# 准备两幅图像
#   原图像：在这幅图中，找到与模板匹配的区域
#   模板：与原图像进行比对的图像块
# 滑动模板图像和原图像进行比对
# 将模板快每次移动一个像素（从左往右、从上到下），在每一个位置，都计算与模板图像的相似程度
# 对于每一个位置将计算的相似结果保存在结果矩阵R中
# 如果输入图像大小W*H且模板大小w*h则输出矩阵R大小为(W-w+1, H-h+1)
# 获得上述图像后，查找最大值的位置，那么该位置对应的区域就被认为是最匹配的
# 对应的区域就是以该点为顶点，长宽和模板图像一样大小的矩阵
# res = cv.matchTemplate(img, template, method)
# 参数
#   1.img：要进行模板匹配的图像
#   2.template：模板
#   3.method：实现模板匹配的算法，主要有：
#       平方差匹配（CV_TM_SQDIFF）：利用模板与图像之间的平方差进行匹配，最好的匹配是0，匹配越差，匹配的值越大
#       相关匹配（CV_TM_CCORR）：利用模板与图像间的乘法进行匹配，数值越大表示匹配程度越高，越小表示匹配效果相差
#       利用相关系数匹配（CV_TM_CCOEFF）：利用模板与图像间的相关系数匹配，1表示完美的匹配，-1表示最差的匹配
# 完成匹配后，使用cv.minMaxLoc()方法查找最大值所在的位置即可
# 如果使用平方差作为比较方法，则最小值位置是最佳匹配位置
# 拓展：模板匹配不适用于尺度变换，视角变换后的图像，这时我们就要使用关键点匹配算法，
# 比较经典的关键点检测算法包括SIFT和SURF等
# 主要的思路是首先通过关键点检测算法获取模板和测试图片中的关键点，然后使用关键点匹配算法处理即可
# 这些关键点可以很好的处理尺度变化、势角变换、光照变化等，就有很好的不变性

img = cv.imread("wulin.jpeg")
plt.imshow(img[..., ::-1])
plt.show()
template = cv.imread("bai.jpeg")
plt.imshow(template[..., ::-1])
plt.show()
res = cv.matchTemplate(img, template, cv.TM_CCORR)
plt.imshow(res, cmap=plt.cm.gray)
plt.show()
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
top_left = max_loc
h, w = template.shape[:2]
bottom_right = (top_left[0]+w, top_left[1]+h)
cv.rectangle(img, top_left, bottom_right, (0, 255, 0), 2)
plt.imshow(img[..., ::-1])
plt.show()
