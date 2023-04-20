import numpy as np
def DataReduction(filename):
    data = np.loadtxt(filename)
    data = np.array(data, 'float32')
    data = np.round(data, 3)
    # 去中心化
    # data矩阵每一列代表同一类型的偏差，每一列代表六个偏差分量
    mean = np.mean(data, axis=0)  # 沿轴0调用mean函数
    data = np.subtract(data, mean)  # 按列相减
    # 标准化
    for i in range(6):
        data[:, i] = data[:, i] / (np.std(data[:, i]))
    # 计算协方差矩阵
    cov = np.dot(data.T, data) / 5
    # 计算特征值和特征向量
    w, v = np.linalg.eig(cov)  # w是特征值，v是特征向量
    w = np.around(w, 4)  # 保留四位小数
    v = np.around(v, 4)  # 保留四位小数，v的列代表特征向量
    # 特征值对应的特征向量按列记
    # print(v)
    sum_lambda = np.sum(w)  # 特征值的和
    f = np.divide(w, sum_lambda)
    # print(f)
    Index = np.argsort(-f)  # 降序输出索引
    # print(Index)
    a = 0
    num = 0  # 需要的主成分个数
    for i in range(len(Index)):
        a += f[Index[i]]
        num += 1
        if a > 0.8:
            break
        else:
            pass
    # print(v)
    priIndex = Index[0:num]  # 记录需要的主成分
    featureVectors = []  # 记录需要的主成分的特征向量
    for i in priIndex:
        featureVectors.append(v[:, i])
    # print(featureVectors)
    # 找出占比最高的几个偏差分量
    weight = []
    for i in range(6):
        tmp = 0
        for j in range(num):
            tmp += abs(featureVectors[j][i]) * f[priIndex[j]]
        weight.append(tmp)
    weight = np.array(weight, 'float32')
    weight = np.around(weight, 4)  # 保留4位小数
    priPosture = np.argsort(-weight)[0:num]  # 主要的位姿
    priDeviation = [mean[i] for i in priPosture]  # 位姿偏差数据
    return priPosture, priDeviation


if __name__ == "__main__":
    priPostures = []
    priDeviations = []
    filename = '.\data\RawData\data%d.txt'
    for k in range(100):
        priPostures.append(DataReduction(filename % k)[0])
        priDeviations.append(DataReduction(filename % k)[1])
    #priPostures = np.array(priPostures)
    #priDeviations = np.array(priDeviations)
    np.savetxt('./data/PriData/priPostures.txt', priPostures, fmt='%s')
    np.savetxt('./data/PriData/priDeviations.txt', priDeviations, fmt='%s')
