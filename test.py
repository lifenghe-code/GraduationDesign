import numpy as np
# coding=utf-8
import matplotlib.pyplot as plt
import optimization
from position import *
from scipy import interpolate

pso_fitness = np.loadtxt('PSO//pso_fitness.txt', dtype='float32')
A = 0.3
L = 0.055
alpha = 8
maxmin = [A, L, alpha]
print([pso_fitness[0], pso_fitness[1], pso_fitness[2]],
      pso_fitness[0] / maxmin[0] + pso_fitness[1] / maxmin[1] + pso_fitness[2] / maxmin[2])
result = []
mpso_fitness = np.loadtxt('img_txt/pareto_fitness.txt', dtype='float32')
for i in mpso_fitness:
    result.append(i[0] / maxmin[0] + i[1] / maxmin[1] + i[2] / maxmin[2])
Index = np.argmin(result)
print(Index)
print([mpso_fitness[Index][0], mpso_fitness[Index][1], mpso_fitness[Index][2]],
      result[Index])
plt.figure(dpi=100)
x1 = [i + 1 for i in range(len(result))]
y1 = result
x2 = x1
y2 = [pso_fitness[0] / maxmin[0] + pso_fitness[1] / maxmin[1] + pso_fitness[2] / maxmin[2]] * len(x2)
'''
plt.plot(x1, y1, c='red')
plt.plot(x2, y2, c='blue')
plt.show()
'''
x = [i + 1 for i in range(10)]
pso = [0.689, 0.201, 0.652, 1.181, 1.027, 0.759, 1.505, 1.073, 0.227, 1.134]
mpso = [0.167, 0.112, 0.481, 0.276, 0.059, 0.220, 0.344, 0.063, 0.156, 0.392]
plt.xlabel('实验次数', fontproperties='SimHei')
plt.ylabel('评价指标', fontproperties='SimHei')
plt.plot(x, pso, c='orange', label='PSO')
plt.plot(x, mpso, c='blue', label='MPSO')
plt.rcParams['figure.figsize'] = (10 * 16 / 9, 10)
plt.subplots_adjust(left=0.06, right=0.94, top=0.92, bottom=0.08)
plt.legend(framealpha=0.7)
plt.grid()
#plt.show()
'''
lh = 2.844542326925336151e-01
lv = 4.517331000702760613e-01
'''

lh = 4.328603755840016443e-01
lv = -3.845092777437228437e-01
print(cal_A(lh, lv), cal_L(lh, lv), cal_alpha(lh, lv))
