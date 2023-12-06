import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
# 霍夫圆检测
# 原理：
# 圆的方程：(x-a)^2+(y-b)^2=r
# 霍夫圆检测就是在a、b、r三个参数组成的三维空间累加器上进行圆形绘制
# 此时效率会很低，所以OpenCV中使用霍夫梯度法进行圆形的检测
# 霍夫梯度法将霍夫圆检测分为两个阶段，第一行阶段检测圆心，第二阶段利用圆心推导出圆半径
# 圆心检测的原理：圆心是圆周法线的交汇处，设置一个阈值，在某点的相交的直线的条数大于这个阈值就认为该交汇点为圆心
# 圆半径确定原理：圆心到圆周上的半径是相同的，设置一个阈值，只要相同距离的数量大于该阈值，就认为该距离是该圆心的半径
# 原则上霍夫变换可以检测任何形状，但复杂的形状需要的参数就越多，霍夫空间的维数就多
# 因此在程序实现上所需的内存空间以及运行效率上都不利于把标准霍夫变换应用于实际复杂图形中
# 霍夫梯度法是霍夫变换的改进，它的目的是减小霍夫空间的维度，提高效率
# circles = cv.HoughCircles(image, method, dp, minDist, paraml1100, param2=100, minRadius=0, maxRadius)
# 参数
#   1.image：输入图像，应输入灰度图像
#   2.method：使用霍夫变换圆检测的算法，参数是CV_HOUGH_GRADIENT
#   3.dp：霍夫空间的分辨率，dp=1时表示霍夫空间与输入空间的大小一致，dp=2时霍夫空间是输入图像空间的一半，以此类推
#   4.minDist：圆心之间的最小距离，如果检测到的两个圆心之间小于该值，则认为他们是同一个圆
#   5.param1：边缘检测时使用Canny算子的高阈值，低阈值是高阈值的一半
#   6.param2：检测圆心和确定半径时所共有的阈值
#   7.minRadius和maxRadius：检测到的圆半径的最大值和最小值
# 返回：circles：输出圆向量，包括三个浮点型的元素——圆心横坐标、圆心纵坐标和圆半径
# 由于霍夫圆检测对噪声比较敏感，所以先对图像进行中值滤波
star = cv.imread("star.jpeg")
gray_img = cv.cvtColor(star, cv.COLOR_BGR2GRAY)
img = cv.medianBlur(gray_img, 7)
plt.imshow(img, cmap=plt.cm.gray)
plt.show()
circles = cv.HoughCircles(img, cv.HOUGH_GRADIENT, 1, 200, param1=100, param2=50, minRadius=0, maxRadius=100)
for i in circles[0, :]:
    cv.circle(star, (int(i[0]), int(i[1])), int(i[2]), (0, 255, 0), 2)
    cv.circle(star, (int(i[0]), int(i[1])), 2, (0, 255, 0), -1)
plt.imshow(star[..., ::-1])
plt.show()
