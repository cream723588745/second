import numpy as np
import matplotlib.pyplot as plt


# 定义 arcsinx 函数
def arccos(x):
    return np.arccos(x)


# 定义 x 值范围和步长
x = np.arange(-1, 1, 0.01)

# 计算对应的 y 值
y = arccos(x)

# 绘制图像
plt.plot(x, y)
plt.xlim(-1,1)  # 设置 x 轴范围
plt.ylim(0,np.pi)  # 设置 y 轴范围
plt.title('arcsinx Function')
plt.show()