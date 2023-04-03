import numpy as np

pso_fitness = np.loadtxt('PSO//pso_fitness.txt', dtype='float32')
A = 0.3
L = 0.055
alpha = 8
maxmin = [A, L, alpha]
print([pso_fitness[0] / maxmin[0], pso_fitness[1] / maxmin[1], pso_fitness[2] / maxmin[2]],
      pso_fitness[0] / maxmin[0] + pso_fitness[1] / maxmin[1] + pso_fitness[2] / maxmin[2])
result = []
mpso_fitness = np.loadtxt('img_txt/pareto_fitness.txt', dtype='float32')
for i in mpso_fitness:
    result.append(i[0] / maxmin[0] + i[1] / maxmin[1] + i[2] / maxmin[2])
Index = np.argmin(result)
print(mpso_fitness[Index], result[Index])
