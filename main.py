# encoding: utf-8
import matplotlib.pyplot as plt
from MOPSO.Mopso import *


def main():
    w = 0.8  # 惯性因子
    c1 = 0.1  # 局部速度因子
    c2 = 0.1  # 全局速度因子
    particals = 200  # 粒子群的数量
    cycle_ = 30  # 迭代次数
    mesh_div = 10  # 网格等分数量
    thresh = 300  # 外部存档阀值
    min_ = np.array([-0.5, -0.5])  # 粒子坐标的最小值
    max_ = np.array([0.5, 0.5])  # 粒子坐标的最大值
    mopso_ = Mopso(particals, w, c1, c2, max_, min_, thresh, mesh_div)  # 粒子群实例化
    pareto_in, pareto_fitness = mopso_.done(cycle_)  # 经过cycle_轮迭代后，pareto边界粒子
    np.savetxt("./img_txt/pareto_in.txt", pareto_in)  # 保存pareto边界粒子的坐标
    np.savetxt("./img_txt/pareto_fitness.txt", pareto_fitness)  # 打印pareto边界粒子的适应值
    print("\n", "pareto边界的坐标保存于：/img_txt/pareto_in.txt")
    print("pareto边界的适应值保存于：/img_txt/pareto_fitness.txt")
    print("\n,迭代结束,over")
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlabel('fitness_y1')
    ax.set_ylabel('fitness_y2')
    ax.set_zlabel('fitness_y3')
    ax.scatter(pareto_fitness[:, 0], pareto_fitness[:, 1], pareto_fitness[:, 2], cmap='viridis', alpha=0.2)
    plt.show()
    '''
    for i in range(len(pareto_in)):
        y = [optimization.positionDeviations(0, 0, pareto_in[i, 0], pareto_in[i, 1]),
             optimization.positionDeviations3(0, 0, pareto_in[i, 0], pareto_in[i, 1]),
             optimization.positionDeviations4(0, 0, pareto_in[i, 0], pareto_in[i, 1])]
        print(y)
    '''

if __name__ == "__main__":
    main()
