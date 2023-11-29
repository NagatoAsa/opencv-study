import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
# 掩膜的应用
# 掩膜就是用选定的图像、图形或物体，对要处理的图像进行遮挡，来控制图像处理的区域
# 在数字图像处理中，我们通常使用二维矩阵数组进行掩膜。掩膜是由0和1组成的一个二进制图像，利用该掩膜图像对要处理的图像进行掩膜
# 其中1值的区域被处理，0值区域被屏蔽，不会处理
# 掩膜的主要用途是：
#   提取感兴趣区域：用预先制作的感兴趣区掩膜与待处理图像进行“与操作”，得到感兴趣区的图像，感兴趣区内的图像值保持不变，而区外图像值为0
#   屏蔽作用：用掩膜对图像上某些区域做屏蔽，使其不参加处理或不参加处理参数的计算，或仅对屏蔽区做处理或统计
#   结构特征提取：用相似性变量或图像匹配方法检测和提取图像中与掩膜相似的结构特征
#   特殊形状图像制作
# 掩膜在遥感影像的处理中使用较多，当提取道路或者河流，或者房屋时，通过一个掩膜矩阵来对图像进行像素过滤，然后将我们需要的地物或者标志突出显示出来

img = cv.imread("cat.jpeg", 0)
plt.imshow(img, cmap=plt.cm.gray)
plt.show()

# 创建掩模图像
mask = np.zeros(img.shape[:2], np.uint8)
mask[400: 650, 200: 500] = 1
plt.imshow(mask, cmap=plt.cm.gray)
plt.show()

# 将掩模图像与原图像进行“与”运算
mask_img = cv.bitwise_and(img, img, mask=mask)
plt.imshow(mask_img, cmap=plt.cm.gray)
plt.show()

# 利用掩模图像处理后的图像统计直方图
mask_hist = cv.calcHist([img], [0], mask, [256], [0, 256])
plt.plot(mask_hist)
plt.show()
