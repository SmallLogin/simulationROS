from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig)


# 数据录入
X = np.linspace(-1, 1, 200)
Y = np.linspace(-1, 1, 200)
X, Y = np.meshgrid(X, Y)
print("网格化后的X=",X)
print("X维度信息",X.shape)
print("网格化后的Y=",Y)
print("Y维度信息", Y.shape)

# Z = np.array(
#     [
#     [1.85,	2.47,	3.64	,5.26,	7.03,	14.32],
#     [3.09,	4.13,	6.19	,7.81,	11.81,	24.04],
#     [4.67,	6.24,	9.24,	11.95	,17.99,	36.64],
#     [6.59	,8.84	,13.03,	16.73,	24.98,	51.87],
#     [8.98	,11.82,	17.41	,22.39	,33.79	,68.52],
#     [11.47	,15.47	,22.51	,28.71,	43.33	,88.21],
#     [14.34,	19.38,	28.09,	36.19	,54.22,	112.77],
#     [17.95,	23.76	,34.76	,44.23,	66.29	,136.09]
# ]
# )
# Z=np.loadtxt('1.txt')
Z=np.loadtxt('2.txt')
print(Z)
print("维度调整前的Z轴数据维度",Z.shape)
Z = Z.T
print("维度调整后的Z轴数据维度",Z.shape)

# 绘制三维曲面图
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')
#设置三个坐标轴信息
ax.set_xlabel('distance-x', color='b')
ax.set_ylabel('distance-y', color='g')
ax.set_zlabel('v2', color='r')

plt.draw()
plt.savefig('3D-v2.jpg')
plt.show()

