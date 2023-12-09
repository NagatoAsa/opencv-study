import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
# Shi-Tomasi角点检测
# Shi-Tomasi算法是对Harris角点检测算法的改进，一般会比Harris算法得到更好的角点
# Harris算法的角点响应函数是将矩阵M的行列式与M的迹相减，利用差值判断是否为角点
# 后来Shi和Tomasi提出改进的方法是，若矩阵M的两个特征值中较小的一个大于阈值，则认为它是角点，即：
# R=min(λ1， λ2)
# 由于较小的那个特征值已经大于阈值，另一个特征值必定大于特征值
# 所以，只有λ1和λ2大于阈值时，才会被认为是角点
# 实现
# corners = cv2.goodFeaturesToTrack(image, maxcorners, qualityLevel, minDistance)
# 参数
#   1.image：输入灰度图像
#   2.maxCorners：获取角点数的数目
#   3.qualityLevel：该参数指出最低可接受的角点质量水平，在0-1之间
#   4.minDistance：角点之间最小的欧氏距离，避免得到相邻特征点
# 返回
# corners：搜索到的角点，在这里所有的低于质量水平的角点被排除掉
# 然后把合格的角点按质量排序，然后将质量较好的交点附近（小于最小欧氏距离）的角点删掉
# 最后找到maxCorners个角点返回
img = cv.imread('tv.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
corners = cv.goodFeaturesToTrack(gray, 1000, 0.01, 10)
print(corners)
for corner in corners:
    x, y = corner.ravel()
    cv.circle(img, (int(x), int(y)), 2, (0, 0, 255), -1)
plt.imshow(img[..., ::-1])
plt.show()
