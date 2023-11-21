# -*- coding: utf-8 -*-
# @Time    : 2023/10/9 20:55
# @Author  : colagold
# @FileName: embedding_visual.py
import numpy as np
import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE

# 生成示例数据
np.random.seed(42)
data = np.random.randn(100, 5)

# 创建一个TSNE对象
tsne = TSNE(n_components=3)

# 计算嵌入
embedded_data = tsne.fit_transform(data)

# 可视化嵌入
plt.scatter(embedded_data[:, 0], embedded_data[:, 1])
plt.title('t-SNE Visualization')


# 创建一个3D绘图窗口
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 可视化嵌入
ax.scatter(embedded_data[:, 0], embedded_data[:, 1], embedded_data[:, 2])
ax.set_title('t-SNE 3D Visualization')
plt.show()
