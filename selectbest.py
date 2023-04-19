import numpy as np
# coding=utf-8
import matplotlib.pyplot as plt
from position import *
from commomdata import *

'''
A -0.15 -- 0.15
L -0.02 -- 0.035
H -0.04 -- 0.04
alpha -4 -- 4
beta -4 -- 4
gamma -3 -- 3
'''
# 在帕累托解中，寻找最优
maxmin = [0.3, 0.055, 0.08, 8, 8, 6]
a = [0, 1, 3]
b = [2, 4, 5]


def selectbest():
    for i in range(len(priPostures)):
        # for i in range(1, 2):
        scores = list()
        tmp1 = list()  # A，L，alpha
        tmp2 = list()  # H，beta，gamma
        # print(priPostures[i])
        for j in priPostures[i]:
            if j in a:
                tmp1.append(j)
            elif j in b:
                tmp2.append(j)
        m = np.loadtxt('CompensationStrategy/strategy1/pareto_fitness/pareto_fitness%d.txt' % i, dtype='float32')
        n = np.loadtxt('CompensationStrategy/strategy2/pareto_fitness/pareto_fitness%d.txt' % i, dtype='float32')
        if m.size == 0:
            np.savetxt("./result/strategy1/pareto_fitness/pareto_fitness%d.txt" % i, [])
            np.savetxt("./result/strategy1/pareto_in/pareto_in%d.txt" % i, [])
        elif m.size == 1:
            m = m / maxmin[tmp1[0]]
            np.savetxt("./result/strategy1/pareto_fitness/pareto_fitness%d.txt" % i, [m])
            v = np.loadtxt('CompensationStrategy/strategy1/pareto_in/pareto_in%d.txt' % i)
            v = v.reshape(1, -1)
            np.savetxt("./result/strategy1/pareto_in/pareto_in%d.txt" % i, v)
        else:
            for it1 in m:
                score = []
                for it2 in range(len(it1)):
                    score.append(it1[it2] / maxmin[tmp1[it2]])
                scores.append(sum(score))
            Index = np.argmin(scores)
            # print(min(scores), Index)
            tmp = m[Index]
            tmp = np.array(tmp)
            tmp = tmp.reshape(1, -1)
            np.savetxt("./result/strategy1/pareto_fitness/pareto_fitness%d.txt" % i, tmp)
            v = np.loadtxt('CompensationStrategy/strategy1/pareto_in/pareto_in%d.txt' % i)
            v = v[Index]
            v = np.array(v)
            v = v.reshape(1, -1)
            np.savetxt("./result/strategy1/pareto_in/pareto_in%d.txt" % i, v)
        ##########################分---割---线##############################
        if n.size == 0:
            np.savetxt("./result/strategy2/pareto_fitness/pareto_fitness%d.txt" % i, [])
            np.savetxt("./result/strategy2/pareto_in/pareto_in%d.txt" % i, [])
        elif n.size == 1:
            n = n / maxmin[tmp2[0]]
            np.savetxt("./result/strategy2/pareto_fitness/pareto_fitness%d.txt" % i, [n])
            v = np.loadtxt('CompensationStrategy/strategy2/pareto_in/pareto_in%d.txt' % i)
            v = v.reshape(1, -1)
            np.savetxt("./result/strategy2/pareto_in/pareto_in%d.txt" % i, v)
        else:
            for it1 in range(len(n)):
                score = []
                for it2 in range(len(n[it1])):
                    score.append((n[it1][it2] / maxmin[tmp2[it2]]))
                scores.append(sum(score))
            Index = np.argmin(scores)
            tmp = n[Index]
            tmp = np.array(tmp)
            tmp = tmp.reshape(1, -1)
            np.savetxt("./result/strategy2/pareto_fitness/pareto_fitness%d.txt" % i, tmp)
            v = np.loadtxt('CompensationStrategy/strategy2/pareto_in/pareto_in%d.txt' % i)
            v = v[Index]
            v = np.array(v)
            v = v.reshape(1, -1)
            np.savetxt("./result/strategy2/pareto_in/pareto_in%d.txt" % i, v)


if __name__ == '__main__':
    selectbest()
