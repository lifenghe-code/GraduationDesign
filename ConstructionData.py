# 由于论文作者不方便提供具体的数据和模型，因此在本文件中合理的构造一些悬臂式掘进机的位姿偏差数据

import numpy as np

# 位姿偏差数据
A = np.random.randint(low=-20, high=20, size=(1, 6))
L = np.random.randint(low=-20, high=20, size=(1, 6))
H = np.random.randint(low=-20, high=20, size=(1, 6))
alpha = np.random.randint(low=-5, high=5, size=(1, 6))
beta = np.random.randint(low=-5, high=5, size=(1, 6))
gamma = np.random.randint(low=-5, high=5, size=(1, 6))
data = np.vstack((A, L, H, alpha, beta, gamma))
data = data.T  # 将数据的每一列作为一个维度，即每一列为一个类型的偏差
np.savetxt('data.txt', data)
