#  此文件作为公用数据集，用来读取PriData供各个函数使用
import numpy as np

# priPostures = np.loadtxt('./data/PriData/priPostures.txt')
# priDeviations = np.loadtxt('./data/PriData/priDeviations.txt')
# print(priPostures)
priPostures = []
priDeviations = []
with open('./data/PriData/priPostures.txt', encoding='utf-8') as f:
    for line in f:
        tmp1 = line[1:(len(line) - 2)].split(' ')
        tmp2 = [int(i) for i in tmp1]
        # print(tmp2)
        priPostures.append(tmp2)
with open('./data/PriData/priDeviations.txt', encoding='utf-8') as f:
    for line in f:
        tmp1 = line[1:(len(line) - 2)].split(',')
        # print(tmp1)
        tmp2 = [float(i) for i in tmp1]
        # print(tmp2)
        priDeviations.append(tmp2)
