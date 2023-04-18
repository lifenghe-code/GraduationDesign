# 由于论文作者不方便提供具体的数据和模型，因此在本文件中合理的构造一些悬臂式掘进机的位姿偏差数据
import numpy as np

'''
各个位姿参数的范围
lh,lv的范围 -0.5 -- 0.5
lsh,lsu的范围 -0.05 -- 0.05
A -0.15 -- 0.15
L -0.02 -- 0.035
H -0.04 -- 0.04
alpha -4 -- 4
beta -4 -- 4
gamma -3 -- 3
'''
# 位姿偏差数据
data = []
for i in range(100):
    A = np.random.uniform(low=-0.15, high=0.15, size=(1, 6))
    L = np.random.uniform(low=-0.02, high=0.035, size=(1, 6))
    H = np.random.uniform(low=-0.04, high=0.04, size=(1, 6))
    alpha = np.random.uniform(low=-4, high=4, size=(1, 6))
    beta = np.random.uniform(low=-4, high=4, size=(1, 6))
    gamma = np.random.uniform(low=-3, high=3, size=(1, 6))
    data = np.vstack((A, L, H, alpha, beta, gamma))
    np.savetxt('data/RawData/data%d.txt' % i, data.T)
