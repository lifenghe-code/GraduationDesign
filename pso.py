# -*- coding: utf-8 -*-

import optimization
import random
import numpy as np
import matplotlib.pyplot as plt
import pylab as mpl
from commomdata import *
import pandas as pd
import xlwt
from position import *

mpl.rcParams['font.sans-serif'] = ['SimHei']


class PSO:
    def __init__(self, dimension, time, size, low, up, v_low, v_high, position_error):
        # 初始化
        self.dimension = dimension  # 变量个数
        self.time = time  # 迭代的代数
        self.size = size  # 种群大小
        self.bound = []  # 变量的约束范围
        self.bound.append(low)
        self.bound.append(up)
        self.v_low = v_low
        self.v_high = v_high
        self.x = np.zeros((self.size, self.dimension))  # 所有粒子的位置
        self.v = np.zeros((self.size, self.dimension))  # 所有粒子的速度
        self.p_best = np.zeros((self.size, self.dimension))  # 每个粒子最优的位置
        self.g_best = np.zeros((1, self.dimension))[0]  # 全局最优的位置
        self.error = position_error
        # 初始化第0代初始全局最优解
        temp = -1000000
        for i in range(self.size):
            for j in range(self.dimension):
                self.x[i][j] = random.uniform(self.bound[0][j], self.bound[1][j])
                self.v[i][j] = random.uniform(self.v_low, self.v_high)
            self.p_best[i] = self.x[i]  # 储存最优的个体
            fit = self.fitness(self.p_best[i])
            # 做出修改
            if fit < temp:
                self.g_best = self.p_best[i]
                temp = fit

    def fitness(self, x):
        """
        个体适应值计算
        """
        x1 = x[0]
        x2 = x[1]
        y = optimization.positionDeviations0(0, 0, x1, x2, self.error) + \
            optimization.positionDeviations1(0, 0, x1, x2, self.error) + \
            optimization.positionDeviations3(0, 0, x1, x2, self.error)
        # print(y)
        return y

    def update(self, size):
        c1 = 2.0  # 学习因子
        c2 = 2.0
        w = 0.8  # 自身权重因子
        for i in range(size):
            # 更新速度(核心公式)
            self.v[i] = w * self.v[i] + c1 * random.uniform(0, 1) * (
                    self.p_best[i] - self.x[i]) + c2 * random.uniform(0, 1) * (self.g_best - self.x[i])
            # 速度限制
            for j in range(self.dimension):
                if self.v[i][j] < self.v_low:
                    self.v[i][j] = self.v_low
                if self.v[i][j] > self.v_high:
                    self.v[i][j] = self.v_high

            # 更新位置
            self.x[i] = self.x[i] + self.v[i]
            # 位置限制
            for j in range(self.dimension):
                if self.x[i][j] < self.bound[0][j]:
                    self.x[i][j] = self.bound[0][j]
                if self.x[i][j] > self.bound[1][j]:
                    self.x[i][j] = self.bound[1][j]
            # 更新p_best和g_best
            if self.fitness(self.x[i]) < self.fitness(self.p_best[i]):
                self.p_best[i] = self.x[i]
            if self.fitness(self.x[i]) < self.fitness(self.g_best):
                self.g_best = self.x[i]

    def pso(self):
        best = []
        self.final_best = np.array([1, 2, 3, 4, 5])
        for gen in range(self.time):
            self.update(self.size)
            if self.fitness(self.g_best) < self.fitness(self.final_best):
                self.final_best = self.g_best.copy()
            # print('当前最佳位置：{}'.format(self.final_best))
            temp = self.fitness(self.final_best)
            # print('当前的最佳适应度：{}'.format(temp))
            best.append(temp)
        '''
        t = [i for i in range(self.time)]
        plt.figure()
        plt.plot(t, best, color='red', marker='.', ms=15)
        plt.rcParams['axes.unicode_minus'] = False
        plt.margins(0)
        plt.xlabel(u"迭代次数")  # X轴标签
        plt.ylabel(u"适应度")  # Y轴标签
        plt.title(u"迭代过程")  # 标题
        plt.savefig('PSO//pso.png')
        '''


maxmin = [0.3, 0.055, 0.08, 8, 8, 6]


def main(k):
    eva = 0
    priPosture = priPostures[k]
    priDeviation = priDeviations[k]
    posTodev = dict(zip(priPosture, priDeviation))
    position_error = [0] * 6
    for i in range(6):
        if i in priPosture:
            position_error[i] = posTodev[i]
    a = [position_error[0], position_error[1], position_error[3]]
    b = [position_error[2], position_error[4], position_error[5]]
    time = 30
    size = 200
    dimension = 2
    v_low = -0.05
    v_high = 0.05
    low = [-0.5, -0.5]
    up = [0.5, 0.5]
    pso1 = PSO(dimension, time, size, low, up, v_low, v_high, a)
    pso1.pso()
    y = [cal_A(pso1.g_best[0], pso1.g_best[1]),
         cal_L(pso1.g_best[0], pso1.g_best[1]),
         cal_alpha(pso1.g_best[0], pso1.g_best[1])]
    aa = [0, 1, 3]
    for l in range(len(a)):
        if a[l] != 0:
            eva += abs(y[l]-a[l]) / maxmin[aa[l]]
    # print('============')
    # print(pso1.g_best)
    v_low = -0.005
    v_high = 0.005
    low = [-0.05, -0.05]
    up = [0.05, 0.05]
    # np.savetxt('PSO//pso_fitness.txt', [y])  # 写入文件
    pso2 = PSO(dimension, time, size, low, up, v_low, v_high, b)
    pso2.pso()
    y = [cal_H(pso2.g_best[0], pso2.g_best[1]),
         cal_beta(pso2.g_best[0], pso2.g_best[1]),
         cal_gamma(pso2.g_best[0], pso2.g_best[1])]
    bb = [2, 4, 5]
    for l in range(len(b)):
        if b[l] != 0:
            eva += abs(y[l] - b[l]) / maxmin[bb[l]]
    return pso1.g_best, pso2.g_best, eva


tmp = []
evas = []
for i in range(100):
    r1, r2, eva = main(i)
    evas.append(eva)
    r1 = list(r1)
    r2 = list(r2)
    r1.extend(r2)
    tmp.append(r1)
fileNum = 100
book = xlwt.Workbook(encoding='utf-8', style_compression=0)
sheet = book.add_sheet('补偿略略', cell_overwrite_ok=True)
col = ('lh', 'lv', 'lsh', 'lsu')
for i in range(0, 4):
    sheet.write(0, i, col[i])
for i in range(0, fileNum):
    data = tmp[i]
    for j in range(0, 4):
        sheet.write(i + 1, j, data[j])
savepath = './inputs_pso.xls'
book.save(savepath)
np.savetxt('evaluating_indicator_pso.txt', evas)