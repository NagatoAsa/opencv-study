import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# 图像缩放
# 缩放是对图像的大小进行调整，即使图像放大或缩小
# cv.resize(src, dsize, fx=0, fy=0, interpolation=cv2.INTER_LINER)
# 参数
#   1.src：输入图像
#   2.dsize：绝对尺寸，直接指定调整后图像的大小
#   3.fx、fy：相对尺寸，将dsize设置为None，然后将fx和fy设置为比例因子即可
#   4.interpolation：插值方法
#       cv.INTER_LINER双线性插值法
#       cv.INTER_NEAREST最近邻插值
#       cv.INTER_AREA像素区域重采样（默认）
#       cv.INTER_CUBIC双三次插值

kids = cv.imread("kids.jpg")
plt.imshow(kids[..., ::-1])
plt.show()

# 绝对尺寸
rows, cols = kids.shape[:2]
print(rows)
print(cols)
res = cv.resize(kids, (2*cols, 2*rows))
plt.imshow(res[..., ::-1])
plt.show()
print(res.shape)

# 相对尺寸
res1 = cv.resize(kids, None, fx=0.5, fy=0.5)
plt.imshow(res1[..., ::-1])
plt.show()
print(res1.shape)
