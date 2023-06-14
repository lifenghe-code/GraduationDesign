# 毕业设计
## 悬臂式掘进机实时姿态智能最优控制方法  
### Part 1位姿补偿
首先根据悬臂式掘进机的拓扑结构模型，推导出各个空间姿态参数与各个结构回路之间的关系式 
悬臂式掘进机共有6个位姿参数：
$$
W=A,L,H,\alpha,\beta,\gamma
$$
***psoition.py***	记录了位姿参数与各个结构回路变化量之间的关系；

***pca.py***	利用主成分分析法（PCA）对位姿偏差数据进行降维，得到对位姿偏差影响最大的几个偏差分量，记录下这些偏差分量以及他们的编号

***communaldata.py***	作为公共数据文件，在各个程序之间共享数据；

***optimization.py***	记录各个位姿参数的目标函数；

***pso.py***	利用粒子群算法（PSO）进行寻优；

***mpso.py***	利用多目标粒子群算法（MPSO）进行寻优，将结果保存在CompensationStrategy文件夹中；

***selectbest.py***	从Pareto解集中选择最优的补偿策略，将结果保存在result文件夹中

```mermaid
graph LR;
data --- PriData:降维后的数据
PriData:降维后的数据---priDeviations.txt:位姿偏差分量
PriData:降维后的数据---priPostures.txt:偏差分量的编号
data --- RawData:原始数据
```

```mermaid
graph LR;
classDef class1 fill:#f96;
CompensationStrategy---strategy1:A,L,alpha偏差的补偿策略---pareto_fitness1
strategy1:A,L,alpha偏差的补偿策略---pareto_in1
CompensationStrategy---strategy2:H,beta,gamma的偏差补偿策略---pareto_fitness2
strategy2:H,beta,gamma的偏差补偿策略---pareto_in2
```

