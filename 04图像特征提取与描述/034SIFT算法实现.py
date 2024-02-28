import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
# SIFT算法实现

# 1.实例化SIFT
# sift = cv.xfeatures2d.SIFT_create()

# 2.利用sift.detectAndCompute()检测关键点并计算
# kp, des = sift.detectAndCompute(gray, None)
# 参数
#   1.进行关键点检测的图像，注意是灰度图像
# 返回
#   1.kp：关键点信息，包括位置、尺度、方向信息
#   2.des：关键点描述符，每个关键点对应128个梯度信息的特征向量

# 3.将关键点检测结果绘制在图像上
# cv.drawKeypoints(image, keypoints, outputimage, color, flags)
# 参数
#   1.image：原始图像
#   2.keypoints：关键点信息，将其绘制在图像上
#   3.outputimage：输出图片，可以是原始图像
#   4.color：颜色设置，通过修改(b, g, r)的值，更改画笔颜色
#   5.flags：绘图功能的标识设置
#       1.cv2.DRAW_MATCHES_FLAGS_DEFAULT：创建输出图像矩阵，使用现存的输出图像绘制匹配对和特征点，对每一个关键点只绘制中间点
#       2.cv2.DRAW_MATCHES_FLAGS_DRAW_OVER_OUTIMG：不创建图像输出矩阵，而是在输出图像上绘制匹配对
#       3.cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS：对每一个特征点绘制带大小和方向的关键点图形
#       4.cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINT：单点的特征点不被绘制

# SURF算法的应用与上述流程一致

img = cv.imread('tv.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
sift = cv.xfeatures2d.SIFT_create()
kp1, des1 = sift.detectAndCompute(gray, None)
cv.drawKeypoints(img, kp1, img, flags=cv.DrawMatchesFlags_DRAW_RICH_KEYPOINTS)
plt.imshow(img[..., ::-1])
plt.show()
