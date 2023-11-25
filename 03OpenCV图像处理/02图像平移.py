import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# 图像平移
# 图像平移将图像按照指定的方向和距离，移动到相应的位置
# cv.warpAffine(img, M, dsize)
# 参数
#   1.img：输入图像
#   2.M：2*3移动矩阵
#       对于(x, y)处的像素点，要把它移动到(x + tx, y + ty)处时，M矩阵应如下设置：
#           M = [[1, 0, tx], [0, 1, ty]]
#           注意：将M设置为np.float32类型的Numpy数组
#   3.dsize：输出图像的大小
#       注：输出图像的大小，应该是(宽度, 高度)的形式，记住width=列数，height=行数

kids = cv.imread("kids.jpg")
plt.imshow(kids[..., ::-1])
plt.show()
rows, cols = kids.shape[:2]
print(rows)
print(cols)
M = np.float32([[1, 0, 50], [0, 1, 100]])
res = cv.warpAffine(kids, M, (cols, rows))
plt.imshow(res[..., ::-1])
plt.show()
res = cv.warpAffine(kids, M, (cols*2, rows*2))
plt.imshow(res[..., ::-1])
plt.show()
