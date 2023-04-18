#  建立悬臂式掘进机的优化模型
from position import *

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
#######################例子
A_ = -0.05
L_ = 0.03
alpha_ = 2
########################
H_ = 0
beta_ = 0
gamma_ = 0
A_ = -0.05
L_ = 0.03
alpha_ = 2
'''

compensationStrategy = {'A': ['Delta_lh', 'Delta_lv'], 'L': ['Delta_lh', 'Delta_lv'], 'H': ['Delta_lsh', 'Delta_lsu'],
                        'alpha': ['Delta_lh', 'Delta_lv'], 'beta': ['Delta_lsh', 'Delta_lsu'],
                        'gamma': ['Delta_lsh', 'Delta_lsu']}
positionType = ['A', 'L', 'H', 'alpha', 'beta', 'gamma']
structuralLoop = ['Delta_lsh', 'Delta_lsu', 'Delta_lh', 'Delta_lv']
# 液压缸的调节速度，以m/s为单位
adjustSpeed = {'Delta_lsh': 0.010, 'Delta_lsu': 0.011, 'Delta_lh': 0.09, 'Delta_lv': 0.020}


###################################
# 下面计算的各个参数，均是在PCA分析的基础上
#  调整量
def positionDeviations0(Delta_lsh=0, Delta_lsu=0, Delta_lh=0, Delta_lv=0, position_error=None):
    try:
        # alpha = cal_alpha(Delta_lh, Delta_lv)
        # beta = cal_beta(Delta_lsu, Delta_lsh)
        # gamma = cal_gamma(Delta_lsu, Delta_lsh)
        A = cal_A(Delta_lh, Delta_lv)
        # L = cal_L(Delta_lh, Delta_lv)
        # H = cal_H(Delta_lsu, Delta_lsh)
        # print(A, "........", L, "........", alpha)
        return abs(A - position_error[0])
    except:
        # print('该数据无效')
        return 1000


def positionDeviations1(Delta_lsh=0, Delta_lsu=0, Delta_lh=0, Delta_lv=0, position_error=None):
    try:
        L = cal_L(Delta_lh, Delta_lv)
        return abs(L - position_error[1])
    except:
        # print('该数据无效')
        return 1000


def positionDeviations2(Delta_lsh=0, Delta_lsu=0, Delta_lh=0, Delta_lv=0, position_error=None):
    try:
        H = cal_H(Delta_lsu, Delta_lsh)
        return abs(H - position_error[0])
    except:
        # print('该数据无效')
        return 1000


def positionDeviations3(Delta_lsh=0, Delta_lsu=0, Delta_lh=0, Delta_lv=0, position_error=None):
    try:
        alpha = cal_alpha(Delta_lh, Delta_lv)
        return abs(alpha - position_error[2])
    except:
        # print('该数据无效')
        return 1000


def positionDeviations4(Delta_lsh=0, Delta_lsu=0, Delta_lh=0, Delta_lv=0, position_error=None):
    try:

        beta = cal_beta(Delta_lsu, Delta_lsh)
        return abs(beta - position_error[1])
    except:
        # print('该数据无效')
        return 1000


def positionDeviations5(Delta_lsh=0, Delta_lsu=0, Delta_lh=0, Delta_lv=0, position_error=None):
    try:
        gamma = cal_gamma(Delta_lsu, Delta_lsh)
        return abs(gamma - position_error[2])
    except:
        # print('该数据无效')
        return 1000


#  调整时间，目前不用
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
            print(cal_L(i, 0.01))
        except:
            print(1)
