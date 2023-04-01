#  建立悬臂式掘进机的优化模型
import numpy as np
from position import *
import sys

pi = 3.14159
compensationStrategy = {'A': ['Delta_lh', 'Delta_lv'], 'L': ['Delta_lh', 'Delta_lv'], 'H': ['Delta_lsh', 'Delta_lsu'],
                        'alpha': ['Delta_lh', 'Delta_lv'], 'beta': ['Delta_lsh', 'Delta_lsu'],
                        'gamma': ['Delta_lsh', 'Delta_lsu']}
positionType = ['A', 'L', 'H', 'alpha', 'beta', 'gamma']
structuralLoop = ['Delta_lsh', 'Delta_lsu', 'Delta_lh', 'Delta_lv']
# 液压缸的调节速度，以m/s为单位
adjustSpeed = {'Delta_lsh': 0.0010, 'Delta_lsu': 0.0011, 'Delta_lh': 0.009, 'Delta_lv': 0.0020}


###################################
# 下面计算的各个参数，均是在PCA分析的基础上
#  调整量
def positionDeviations(Delta_lsh=0, Delta_lsu=0, Delta_lh=0, Delta_lv=0):
    try:
        alpha = cal_alpha(Delta_lh, Delta_lv)
        beta = cal_beta(Delta_lsu, Delta_lsh)
        gamma = cal_gamma(Delta_lsu, Delta_lsh)
        A = cal_A(Delta_lh, Delta_lv)
        L = cal_L(Delta_lh, Delta_lv)
        H = cal_H(Delta_lsu, Delta_lsh)
        print(alpha, "........", A, "........", L)
        return abs(alpha - 0.7) #+ abs(A - 0.002167) * 10000 + abs(L + 0.004667) * 10000
        # print(abs(alpha + 2.167) + abs(beta) + abs(gamma) + abs(A - 2.167) + abs(L + 4.667) + abs(H))
        # return abs(alpha + 2.167) + abs(beta) + abs(gamma) + abs(A - 2.167) + abs(L + 4.667) + abs(H)
    except:
        print('该数据无效')
        return 300


#  调整时间
def adjustTime(Delta_lsh=0, Delta_lsu=0, Delta_lh=0, Delta_lv=0):
    Time = 0
    Time += abs(Delta_lsh) / adjustSpeed['Delta_lsh']
    Time += abs(Delta_lsu) / adjustSpeed['Delta_lsu']
    Time += abs(Delta_lh) / adjustSpeed['Delta_lh']
    Time += abs(Delta_lv) / adjustSpeed['Delta_lv']
    return Time


###################################
if __name__ == '__main__':
    for i in np.arange(-0.5, 0.5, 0.001):
        try:
            print(cal_alpha(i, 0.01))
        except:
            print(100000)
