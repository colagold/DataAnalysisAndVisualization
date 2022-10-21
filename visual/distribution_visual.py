import numpy as np
import matplotlib.pyplot as plt

x=np.random.normal(1.75, 1, 1000000) # 均值1.75 标准差 1 数据量1000000
plt.figure(figsize=(20, 10), dpi=100)
# 2）绘制直方图
plt.hist(x, 100) # x是其高度，在(0-100)范围内显示
plt.show()
