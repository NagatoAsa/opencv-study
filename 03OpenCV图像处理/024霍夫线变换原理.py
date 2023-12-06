# 霍夫线变换
# 霍夫变换常用来提取图像中的直线和圆等几何形状

# 原理
# 在笛卡尔坐标系中，一条直线由两个点A(x1, y1)和B(x2, y2)确定
# 而这两个点确定的直线的斜率k与截距q可以在另一个坐标系确定另一个坐标点（以k为横坐标，q为y坐标）
# 变换后的空间我们叫做霍夫空间，即：笛卡尔坐标系中的一条直线，对应于霍夫空间中的一个点
# 反过来同样成立，即，霍夫空间中的一条线，对应于笛卡尔坐标系中一个点
# 两个在笛卡尔坐标系中的点，可以在霍夫空间中表示为两条直线，而这两条直线的交点，正是在笛卡尔坐标系中两个点确定的直线
# 假如若干点在笛卡尔坐标系中共线，那么这些点在霍夫空间中应当交于一点
# 而假如若干点确认了多条直线，那么在霍夫空间中也应该会有多个交点
# 而对于笛卡尔坐标系下没有斜率的直线，我们需要将笛卡尔坐标系转换为极坐标系
# 笛卡尔坐标系：y=ax+b 极坐标系：ρ=xcosθ+ysinθ
# 在极坐标系下，极坐标中的点对应霍夫空间中的线，这时的霍夫空间是(ρ,θ)的空间
# ρ是原点到直线的垂直距离，θ表示直线的垂线与横轴顺时针方向的夹角

# 实现流程
# 假设有一个大小为100*100的图片，使用霍夫变换检测图片中的直线，则步骤如下所示
# 直线都可以使用(ρ,θ)表示，首先创建一个2D数组，我们叫做累加器。初始化所有值为0，行表示ρ，列表是θ
# 该数组的大小决定了结果的准确性，若希望角度的精度为1度，那就需要180列。对于ρ，最大值为图片对角线的距离，如果希望精度达到像素级别，行数应该与图像的对角线的距离相等
# 去直线上的一个点(x,y)，将其带入直线在极坐标的公式中，然后遍历θ的取值：1、2、3...180，分别求出对应的染ρ值，如果这个数值在上述累加其中存在相应位置，则在该位置加上1
# 取直线上的第二个点，重复上述步骤，更新累加器中的值
# 对图像中的直线上的每个点都执行以上步骤，每次更新累加器中的值
# 搜索累加器中的最大值，并找到对应的(ρ,θ)，就可将图像中的直线表示出来
