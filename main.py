# encoding: utf-8
import matplotlib.pyplot as plt
from MOPSO.Mopso import *
from commomdata import *

'''
计算A、L、alpha偏差，补偿lh、lv
计算H、beta、gamma偏差，补偿lsh、lsu
'''


def main(k: int):
    priPosture = priPostures[k]
    priDeviation = priDeviations[k]
    posTodev = dict(zip(priPosture, priDeviation))
    position_error = [0] * 6
    for i in range(6):
        if i in priPosture:
            position_error[i] = posTodev[i]
    w = 0.8  # 惯性因子
    c1 = 0.1  # 局部速度因子
    c2 = 0.1  # 全局速度因子
    particals = 200  # 粒子群的数量
    cycle_ = 20  # 迭代次数
    mesh_div = 10  # 网格等分数量
    thresh = 300  # 外部存档阀值
    min_0 = np.array([-0.5, -0.5])  # 粒子坐标的最小值
    max_0 = np.array([0.5, 0.5])  # 粒子坐标的最大值
    min_1 = np.array([-0.05, -0.05])  # 粒子坐标的最小值
    max_1 = np.array([0.05, 0.05])  # 粒子坐标的最大值
    a = [position_error[0], position_error[1], position_error[3]]
    b = [position_error[2], position_error[4], position_error[5]]
    print(a, b)
    mopso_0 = Mopso(particals, w, c1, c2, max_0, min_0, thresh, mesh_div, a, 0)  # 粒子群实例化
    # mopso_0，寻找A，L，alpha的补偿
    # mopso_1，寻找H，beta，gamma的补偿
    pareto_in, pareto_fitness = mopso_0.done(cycle_)  # 经过cycle_轮迭代后，pareto边界粒子
    np.savetxt("./CompensationStrategy/strategy1/pareto_in/pareto_in%d.txt" % k, pareto_in)  # 保存pareto边界粒子的坐标
    np.savetxt("./CompensationStrategy/strategy1/pareto_fitness/pareto_fitness%d.txt" % k,
               pareto_fitness)  # 打印pareto边界粒子的适应值
    # print("\n", "pareto边界的坐标保存于：/img_txt/pareto_in/pareto_in.txt")
    # print("pareto边界的适应值保存于：/img_txt/pareto_fitness/pareto_fitness.txt")
    # print("\n,迭代结束,over")
    mopso_1 = Mopso(particals, w, c1, c2, max_1, min_1, thresh, mesh_div, b, 1)  # 粒子群实例化
    pareto_in, pareto_fitness = mopso_1.done(cycle_)  # 经过cycle_轮迭代后，pareto边界粒子
    np.savetxt("./CompensationStrategy/strategy2/pareto_in/pareto_in%d.txt" % k, pareto_in)  # 保存pareto边界粒子的坐标
    np.savetxt("./CompensationStrategy/strategy2/pareto_fitness/pareto_fitness%d.txt" % k,
               pareto_fitness)  # 打印pareto边界粒子的适应值
    # print("\n", "pareto边界的坐标保存于：/img_txt/pareto_in/pareto_in.txt")
    # print("pareto边界的适应值保存于：/img_txt/pareto_fitness/pareto_fitness.txt")
    # print("\n,迭代结束,over")
    '''
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlabel('fitness_y1')
    ax.set_ylabel('fitness_y2')
    ax.set_zlabel('fitness_y3')
    ax.scatter(pareto_fitness[:, 0], pareto_fitness[:, 1], pareto_fitness[:, 2], cmap='viridis', alpha=0.2)
    # plt.show()
    for i in range(len(pareto_in)):
        y = [optimization.positionDeviations(0, 0, pareto_in[i, 0], pareto_in[i, 1]),
             optimization.positionDeviations3(0, 0, pareto_in[i, 0], pareto_in[i, 1]),
             optimization.positionDeviations4(0, 0, pareto_in[i, 0], pareto_in[i, 1])]
        print(y)
    '''


if __name__ == "__main__":
    l = len(priPostures)
    for m in range(l):
        main(m)
