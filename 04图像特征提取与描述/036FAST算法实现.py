import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
# FAST算法实现

# 1.实例化fast
# fast = cv.FastFeatureDetector(threshold, nonmaxSupression)
# 参数
#   1.threshold：阈值t，有默认值10
#   2.nonmaxSuppression：是否进行非极大值抑制，默认值为True
# 返回
#   fast：创建的FastFeatureSuppression对象

# 2.利用fast.detect检测关键点，没有对应的关键点描述
# kp = fast.detect(img, None)
# 参数
#   1.img：进行关键点检测的图像，可以是彩色图像
# 返回
#   kp：关键点信息，包括位置，尺度，方向信息

# 3.将关键点检测结果绘制在图像上，与在SIFT中是一样的
# cv.drawKeypoints(image, keypoints, outputimage, color, flags)

img = cv.imread('tv.jpg')
fast = cv.FastFeatureDetector_create(threshold=30)
keypoints = fast.detect(img, None)
img2 = cv.drawKeypoints(img, keypoints, None, color=(0, 0, 255))
plt.imshow(img2[..., ::-1])
plt.show()

fast.setNonmaxSuppression(0)
keypoints = fast.detect(img, None)
img3 = cv.drawKeypoints(img, keypoints, None, color=(0, 0, 255))
plt.imshow(img3[..., ::-1])
plt.show()
