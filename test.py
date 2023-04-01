from math import sin, cos, tan, atan, acos, asin, sqrt
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import Axes3D

pi = 3.1415926
l1 = 1.5
l2 = 1.5
l3 = 2.6
l4 = 2.6
l5 = 1.5
l6 = 1.3


def cal_A(lh, lv):
    Lambda = 2 * atan((l5 - lh) * sin(pi / 6) / ((l2 - lh) * sin(pi / 6)) ** 2 + (l6 + lh) ** 2)
    Phi = acos((l6 + lv) ** 2 / 5) - acos(l6 ** 2 / 5)
    Numerator = (l5 + lh) * (l5 - lh) * cos(Lambda) * cos(Phi)
    Denominator = (l5 - lh) * sin(4 / pi + Lambda)
    A = (Numerator / Denominator) / 2 - 1.1
    return A


def cal_L(lh, lv):
    Lambda = 2 * atan((l5 - lh) * sin(pi / 6) / ((l2 - lh) * sin(pi / 6)) ** 2 + (l6 + lh) ** 2)
    Phi = acos((l6 + lv) ** 2 / 5) - acos(l6 ** 2 / 2)
    Numerator = cos(Phi)
    Denominator = 5 * sin(Phi) * (l6 + lv) * cos(Lambda) / ((l5 - lh) * sin(Lambda) + (l5 + lh) * sin(Lambda))
    L = (Numerator / Denominator) / 10+0.1
    return L


def cal_H(lsu, lsh):  # lsu, lsh的变化量必须相同
    H0 = 0.85
    H = (l1 + lsu) * sin(pi / 6) + (l2 + lsh) * sin(pi / 6) - H0 - 0.64
    return H


def cal_alpha(lh, lv):
    Lambda = 2 * atan((l5 - lh) * sin(pi / 6) / ((l2 - lh) * sin(pi / 6)) ** 2 + (l6 + lh) ** 2)
    Phi = acos((l6 + lv) ** 2 / 5) - acos(l6 ** 2 / 5)
    Numerator = (l5 + lh) * (l5 - lh) * cos(Lambda) * cos(Phi)
    Denominator = (l5 - lh) * sin(4 / pi + Lambda)
    alpha = ((Numerator / Denominator) / 3 - 0.75)*40
    return alpha


def cal_beta(lsu, lsh):
    delta = pi / 6
    a = (l2 - lsu) * cos(delta)
    Numerator = -4 * (l2 - lsu) * sin(delta) + sqrt((2 * (l2 - lsu) * sin(delta)) ** 2 - (l3 + lsh) ** 2 + (4 * a) ** 2)
    Denominator = ((((l2 - lsu) * sin(delta)) ** 2 - (l3 + lsh) ** 2) ** 2 + 2 * a) / 10
    beta = 80 * atan(Numerator / Denominator) - 32
    return beta


def cal_gamma(lsu, lsh):
    Numerator = -9 * (l1 - lsu) + sqrt((l1 - lsu) ** 2 + ((l1 - lsu) ** 2 - (l2 + lsh) ** 2) ** 2)
    Denominator = (((l2 - lsu) ** 2 + 4 + (l1 - lsu)) ** 2 - (l2 + lsh) ** 2)/10
    gamma = ((40 * atan(Numerator / Denominator))+44.8)*10
    return gamma


x1 = np.linspace(-0.05, 0.05, 100)
x2 = np.linspace(-0.05, 0.05, 100)
x1, x2 = np.meshgrid(x1, x2)  # 根据横纵坐标生成网格点
m, n = np.shape(x1)
y1, y2 = np.zeros((m, n)), np.zeros((m, n))
for i in range(m):
    for j in range(n):
        y1[i, j] = cal_gamma(x1[i, j], x2[i, j])
fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')
surf = ax1.plot_surface(x1, x2, y1, cmap=plt.cm.brg, alpha=0.6)
cb = fig.colorbar(surf, shrink=0.8, aspect=15)  # 设置颜色棒
plt.show()

"""
各个位姿参数的范围
lh,lv的范围 -0.5 -- 0.5
lsh,lsu的范围 -0.05 -- 0.05
A -0.15 -- 0.15
L -0.1 -- 0.075
H -0.04 -- 0.04
alpha -4 -- 4
beta -4 -- 4
gamma -3 -- 3
"""