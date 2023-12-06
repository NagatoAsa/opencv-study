import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
# Sobel检测算子
# Sobel边缘检测算法比较简单，实际应用中比Canny边缘检测效率要高，但是边缘不如Canny检测的准确
# 但是很多实际应用的场合，Sobel边缘检测却是首选
# Sobel算子是高斯平滑与微分操作的结合体，所以其坑噪声能力很强，用途较多
# 尤其是效率要求较高，而对细纹理不太关心的时候
# 原理
# 对于不连续的函数，一阶导数可以写作：f'(x)=f(x)-f(x-1)
# 或：f'(x)=f(x+1)-f(x)
# 所以有：f'(x)=[f(x+1)-f(x-1)]/2
# 上式的意义：某个像素的导数等于这个像素的后一个像素值减去这个像素前一个像素值的差除以二(在两个方向上求导)
# 实际处理上：
# 水平变化：将图像I与奇数大小的模板进行卷积，结果为Gx。比如，当模板大小为3是，Gx为：
# Gx=[[-1, 0, +1], [-2, 0, +2], [-1, 0, +1]]*I
# 垂直变化：将图像I与奇数大小的模板进行卷积，结果为Gy。比如，当模板大小为3时，Gy为：
# Gy=[[-1, -2, -1], [0, 0, 0], [+1, +2, +1]]*I
# 在图像的每一点，结合以上两个结果求出：
# G=sqrt(Gx**2+Gy**2)
# 统计极大值所在的位置，就是图像的边缘
# 注意：当内核大小为3时，以上Sobel内核可能产生比较明显的误差，为解决这一问题，我们使用Scharr函数，但该函数仅作用于大小为3的内核
# 该函数的运算与Sobel函数一样快，但结果却更加精确，其计算方法为：
# Gx=[[-3, 0, +3], [-10, 0, +10], [-3, 0, +3]]*I
# Gy=[[-3, -10, -3], [0, 0, 0], [+3, +10, +3]]*I
# Sobel_x_or_y = cv.Sobel(src, ddepth, dx, dy, dst, ksize, scale, delta, borderType)
# 参数
#   1.src：传入的图像
#   2.ddepth：图像的深度
#   3.dx和dy：指求导的阶数，0表示这个方向上没有求导，取值为0、1
#   4.ksize：是Sobel算子的大小，必须为奇数，默认为3 注：如果ksize=-1，就演变成为3*3的Scharr算子
#   5.scale：缩放导数的比例常数，默认情况为没有伸缩系数
#   6.borderType：图像边界的模式，默认为cv.BORDER_DEFAULT
# Sobel函数求完导数后会有负值，还会有大于255的值
# 而原图像是uint8，所以Sobel建立的图像位数不够，会有截断
# 因此要使用16位有符号的数据类型，即cv.CV_16S
# 处理完图像后，再使用cv.convertScaleAbs()函数将其转回原来的uint8格式，否则图像无法显示
# Sobel算子是在两个方向计算的，最后还需要cv.addWeighted()函数将其组合起来

img = cv.imread("horse.jpg", 0)
plt.imshow(img, cmap=plt.cm.gray)
plt.show()
# Sobel算子
x = cv.Sobel(img, cv.CV_16S, 1, 0)
y = cv.Sobel(img, cv.CV_16S, 0, 1)
absx = cv.convertScaleAbs(x)
absy = cv.convertScaleAbs(y)
res = cv.addWeighted(absx, 0.5, absy, 0.5, 0)
plt.imshow(res, cmap=plt.cm.gray)
plt.show()
# Scharr算子
x = cv.Sobel(img, cv.CV_16S, 1, 0, ksize=-1)
y = cv.Sobel(img, cv.CV_16S, 0, 1, ksize=-1)
absx = cv.convertScaleAbs(x)
absy = cv.convertScaleAbs(y)
res = cv.addWeighted(absx, 0.5, absy, 0.5, 0)
plt.imshow(res, cmap=plt.cm.gray)
plt.show()
