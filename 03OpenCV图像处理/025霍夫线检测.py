import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
# 霍夫线检测
# cv.HoughLines(img, rho, theta, threshould)
# 参数
#   1.img：检测的图像，要求是二值化的图像，所以在调用霍夫变换之前首先要进行二值化，或者进行Canny边缘检测
#   2.rho、theta：ρ和θ的精确度
#   3.threshold：阈值，只有累加器中的值高于该阈值时才被认为是直线

img = cv.imread("rili.jpg", 0)
img2 = cv.imread("rili.jpg")
plt.imshow(img, cmap=plt.cm.gray)
plt.show()
edges = cv.Canny(img, 50, 150)
plt.imshow(edges, cmap=plt.cm.gray)
plt.show()
lines = cv.HoughLines(edges, 0.8, np.pi / 180, 150)
for line in lines:
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = rho * a
    y0 = rho * b
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * a)
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * a)
    cv.line(img2, (x1, y1), (x2, y2), (0, 255, 0))
plt.imshow(img2[..., ::-1])
plt.show()
