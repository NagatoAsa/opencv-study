import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
# 绘制直线
# cv.line(img, start, end, color, thickness)
# 参数
#   1.img：要绘制直线的图像
#   2.start、end：直线的起点和终点
#   3.color：线条的颜色
#   4.thickness：线条的宽度

# 绘制一个全黑的图像
img = np.zeros((512, 512, 3), np.uint8)
cv.line(img, (0, 0), (512, 512), (255, 0, 0), 5)

# 绘制圆形
# cv.circle(img, centerpoint, r, color, thickness)
# 参数
#   1.img：要绘制圆形的图像
#   2.centerpoint、r：圆心和半径
#   3.color：线条的颜色
#   4.thickness：线条宽度，-1时生成闭合图案并填充颜色

cv.circle(img, (256, 256), 60, (0, 0, 255), -1)

# 绘制矩形
# cv.rectangle(img, leftupper, rightdown, color, thickness)
# 参数
#   1.img：要绘制矩形的图像
#   2.leftupper、rightdown：矩形的左上角和右下角坐标
#   3.color：线条的颜色
#   4.thickness：线条宽度

cv.rectangle(img, (100, 100), (400, 400), (0, 255, 0), 5)

# 向图像中添加文字
# cv.putText(img, text, station, font, fontsize, color, thickness, cv.LINE_AA)
#   1.img：图像
#   2.text：要写入的文本数据
#   3.station：文本的放置位置
#   4.font：字体
#   5.fontsize：字体大小

cv.putText(img, "hello", (100, 150), cv.FONT_HERSHEY_COMPLEX, 5, (255, 255, 255), 3)

plt.imshow(img[..., ::-1])
plt.show()
