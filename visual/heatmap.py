# -*- coding: utf-8 -*-
# @Time    : 2023/10/25 10:48
# @Author  : colagold
# @FileName: heatmap.py
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# 生成示例数据
# 生成示例数据
# 生成示例数据
from sklearn.metrics.pairwise import cosine_similarity

vector1 = np.random.rand(50)
vector2 = np.random.rand(50)
vector3 = np.random.rand(50)
vector4 = np.random.rand(50)


#计算相关性矩阵
data = [vector1, vector2, vector3, vector4]
cosine_similarity_matrix = cosine_similarity(np.array(data), np.array(data))


# 使用Seaborn绘制热力图
sns.heatmap(cosine_similarity_matrix, cmap="YlGnBu", xticklabels=["Vector 1", "Vector 2", "Vector 3", "Vector 4"], yticklabels=["Vector 1", "Vector 2", "Vector 3", "Vector 4"])
plt.title("Correlation Heatmap")
plt.show()

