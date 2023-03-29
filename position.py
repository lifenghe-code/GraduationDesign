# 记录位姿参数与各个液压回路之间的关系
import math

# 相关参数
pi = 3.14159
mu = 0.9  # 摩擦系数
# 长度 “_”代表论文中的‘
L1 = 3.627
L2 = 3.900
l1 = l2 = 1.487
l3 = l4 = 2.637
l5 = 1.662
l6 = 1.370
L1_ = 7.352
LG = 1.75
R = 0.844
H0 = 0.859  # 机身起始高度
B = 1.855
# 重量
M = 4500
m1 = 1600
m2 = 5700
g = 9.8
P1 = 13 * 10 ** 6  # 截割臂回转液压油缸压力
P2 = 18 * 10 ** 6  # 截割臂升降液压油缸压力
#######################################
delta = pi * 2 / 16
n = 1  # 截割臂摆速
S1 = 2  # 回转油缸横截面积
S2 = 2  # 升降油缸横截面积
S1_ = 1.8  # 回转油缸有效工作面积
S2_ = 1.8  # 升降油缸缸有效工作面积
u = 1  # 升降机构两接点之间的距离
w = 1  # 升降机构两接点之间的距离


#######################################

#########下面的函数，计算的结果都是位姿偏差####
def cal_alpha(Delta_lh=0, Delta_lv=0):
    ##################################
    Lx = 2
    theta = 20 * (pi / 180)
    h = 0.3
    a = 1
    h = 0.3
    ##################################
    C = math.acos((n ** 2 + R ** 2 - l5 ** 2) / (2 * n * R))
    q = (l5 + Delta_lh) * math.cos(theta) - h
    Delta_Lambda = 2 * math.atan(
        (-2 * Lx * (l5 - Delta_lh) * math.sin(delta) + math.sqrt((2 * Lx * (l5 - Delta_lh) * math.sin(delta)) ** 2 -
                                                                 (((l5 - Delta_lh) * math.sin(
                                                                     delta)) ** 2 + Lx ** 2 + a ** 2 - (
                                                                          l6 + Delta_lh) ** 2) ** 2 + (
                                                                         2 * q * Lx) ** 2))
        / ((((l2 - Delta_lh) * math.sin(delta)) ** 2 + Lx ** 2 + a ** 2 - (l6 + Delta_lh) ** 2) ** 2 + (2 * q * Lx)))

    Delta_Phi = math.acos((u ** 2 + w ** 2 - (l6 + Delta_lv) ** 2) / (2 * u * w)) - math.acos(
        (u ** 2 + w ** 2 - l6 ** 2) / (2 * u * w))
    Fx = (P1 * R * n * (S1 * (l5 - Delta_lh)) * math.sin(C + Delta_Lambda) + (l5 + Delta_lh) * S1_ * math.sin(
        C - Delta_Lambda)) / (L2 * (l5 + Delta_lh) * (l5 - Delta_lh) * math.cos(Delta_Lambda) * math.cos(Delta_Phi))
    alpha = 90 * mu * B * M * g / (pi * Fx * L1_)
    return alpha


def cal_beta(Delta_lsu=0, Delta_lsh=0):
    a = (l2 - Delta_lsu) * math.cos(delta) - L1_
    beta = 180 / pi * 2 * math.atan(-2 * L1 * (l2 - Delta_lsu) * math.sin(delta) + math.sqrt(
        ((2 * L1 * (l2 - Delta_lsu) * math.sin(delta)) ** 2 - ((((l2 - Delta_lsu) * math.sin(
            delta)) ** 2) + L1 ** 2 + a ** 2 - (l3 + Delta_lsh) ** 2) ** 2 + (2 * a * L1) ** 2)) / (
                                            (((l2 - Delta_lsu) * math.sin(
                                                delta)) ** 2 + L1 * L1 + a * a - ((l3 + Delta_lsh) ** 2)) ** 2 + (
                                                    2 * a * L1)))
    return beta + 180 - 26


def cal_gamma(Delta_lsu=0, Delta_lsh=0):  # 论文中的Delta_lsu_即对应Delta_lsh
    gamma = 2 * 180 / pi * math.atan((-2 * B * (l1 - Delta_lsu) + math.sqrt((2 * B * (l1 - Delta_lsu)) ** 2 + (
            (2 * (B ** 2) + (l1 - Delta_lsu)) ** 2 + (l1 - Delta_lsu - B) ** 2 - (l2 + Delta_lsh) ** 2)) ** 2 + (
                                              2 * (l2 + Delta_lsh - B) * B) ** 2) /
                                     (((l2 - Delta_lsu) ** 2 + B ** 2 + (l1 - Delta_lsu - B) ** 2 - (
                                             (l2 + Delta_lsh) ** 2)) ** 2 - 2 * (l1 - Delta_lsu - B) * B))
    return gamma - 180 + 20


def cal_A(Delta_lh=0, Delta_lv=0):
    ##################################
    Lx = 2
    theta = 20 * (pi / 180)
    C = math.acos((n ** 2 + R ** 2 - l5 ** 2) / (2 * n * R))  #
    h = 0.3
    a = 1
    ##################################
    q = (l5 + Delta_lh) * math.cos(theta) - h
    Delta_Lambda = 2 * math.atan(
        (-2 * Lx * (l5 - Delta_lh) * math.sin(delta) + math.sqrt((2 * Lx * (l5 - Delta_lh) * math.sin(delta)) ** 2 -
                                                                 (((l5 - Delta_lh) * math.sin(
                                                                     delta)) ** 2 + Lx ** 2 + a ** 2 - (
                                                                          l6 + Delta_lh) ** 2) ** 2 + (
                                                                         2 * q * Lx) ** 2))
        / ((((l2 - Delta_lh) * math.sin(delta)) ** 2 + Lx ** 2 + a ** 2 - (l6 + Delta_lh) ** 2) ** 2 + (2 * q * Lx)))
    Delta_Phi = math.acos((u ** 2 + w ** 2 - (l6 + Delta_lv) ** 2) / (2 * u * w)) - math.acos(
        (u ** 2 + w ** 2 - l6 ** 2) / (2 * u * w))
    Fx = (P1 * R * n * (S1 * (l5 - Delta_lh)) * math.sin(C + Delta_Lambda) + (l5 + Delta_lh) * S1_ * math.sin(
        C - Delta_Lambda)) / \
         (L2 * (l5 + Delta_lh) * (l5 - Delta_lh) * math.cos(Delta_Lambda) * math.cos(Delta_Phi))

    A = (mu * M * g * B) / (4 * Fx)
    return A


def cal_L(Delta_lh=0, Delta_lv=0):
    ##################################
    Lx = 2
    theta = 20 * (pi / 180)
    a = 1
    h = 0.2
    ##################################
    B_ = math.acos((u ** 2 + w ** 2 - l6 ** 2) / (2 * u * w))
    C = math.acos((n ** 2 + R ** 2 - l5 ** 2) / (2 * n * R))  #
    q = (l5 + Delta_lh) * math.cos(theta) - h
    Delta_Lambda = 2 * math.atan(
        (-2 * Lx * (l5 - Delta_lh) * math.sin(delta) + math.sqrt((2 * Lx * (l5 - Delta_lh) * math.sin(delta)) ** 2 -
                                                                 (((l5 - Delta_lh) * math.sin(
                                                                     delta)) ** 2 + Lx ** 2 + a ** 2 - (
                                                                          l6 + Delta_lh) ** 2) ** 2 + (
                                                                         2 * q * Lx) ** 2))
        / ((((l2 - Delta_lh) * math.sin(delta)) ** 2 + Lx ** 2 + a ** 2 - (l6 + Delta_lh) ** 2) ** 2 + (2 * q * Lx)))

    Delta_Phi = math.acos((u ** 2 + w ** 2 - (l6 + Delta_lv) ** 2) / (2 * u * w)) - math.acos(
        (u ** 2 + w ** 2 - l6 ** 2) / (2 * u * w))
    Fy = ((P1 * R * n * math.sin(Delta_Lambda) * (S1 * (l5 - Delta_lh)) * math.sin(C + Delta_Lambda) + (
            l5 + Delta_lh) * S1_ * math.sin(
        C - Delta_Lambda)) / (L2 * (l5 + Delta_lh) * (l5 - Delta_lh) * math.cos(Delta_Phi))) + (
                 2 * P2 * S2 * u * w * math.sin(Delta_Phi) * math.sin(B_ + Delta_Phi) /
                 (L2 * (l6 + Delta_lv) * math.cos(Delta_Lambda))) - (
                 (m1 + m2) * g * LG * math.sin(Delta_Phi) * math.cos(Delta_Phi) / L2)

    Fz = 2 * u * w * P2 * S2 * math.cos(Delta_Phi) * math.sin(B_ + Delta_Phi) / (
            L2 * (l6 + Delta_lv) * math.cos(Delta_Lambda)) - (
                 m1 + m2) * g * LG * math.cos(Delta_Phi) ** 2 / L2

    L = mu * L1 * (M * g + Fz * math.cos(Delta_Phi)) / (2 * Fy * math.sin(Delta_Phi)) / 100000
    return L


def cal_H(Delta_lsu=0, Delta_lsh=0):
    a = (l2 - Delta_lsu) * math.cos(delta) - L1_
    beta = 180 / pi * 2 * math.atan(-2 * L1 * (l2 - Delta_lsu) * math.sin(delta) + math.sqrt(
        ((2 * L1 * (l2 - Delta_lsu) * math.sin(delta)) ** 2 - ((((l2 - Delta_lsu) * math.sin(
            delta)) ** 2) + L1 ** 2 + a ** 2 - (l3 + Delta_lsh) ** 2) ** 2 + (2 * a * L1) ** 2)) / (
                                            (((l2 - Delta_lsu) * math.sin(
                                                delta)) ** 2 + L1 * L1 + a * a - ((l3 + Delta_lsh) ** 2)) ** 2 + (
                                                    2 * a * L1)))
    beta = beta + 180 - 26
    H = ((l2 + Delta_lsu) * math.sin(delta) + L1 * math.sin(beta) / 2 - H0) * 10
    return H
