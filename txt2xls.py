# 利用Mpso算法得到的结果
# 将最终生成的result中的各个txt文件合并，并生成xls文件，以便于后续使用
import numpy as np
import pandas as pd
import xlwt

fileNum = 100  # 文件数量
filepath1 = 'E:\\GraduationDesign\\result\\strategy1\\pareto_fitness'
filepath2 = 'E:\\GraduationDesign\\result\\strategy2\\pareto_fitness'
filepath3 = 'E:\\GraduationDesign\\result\\strategy1\\pareto_in'
filepath4 = 'E:\\GraduationDesign\\result\\strategy2\\pareto_in'
filepath5 = 'E:\\GraduationDesign\\data\\PriData\\priDeviations.txt'
filepath6 = 'E:\\GraduationDesign\\data\\PriData\\priPostures.txt'
inputs = []
for i in range(fileNum):
    c = []
    a = np.loadtxt(filepath3 + '\\pareto_in%d.txt' % i)
    b = np.loadtxt(filepath4 + '\\pareto_in%d.txt' % i)
    if a.size == 0:
        c.append(0)
        c.append(0)
    else:
        for j in a:
            c.append(j)
    if b.size == 0:
        c.append(0)
        c.append(0)
    else:
        for j in b:
            c.append(j)
    inputs.append(c)
# 将c中的内容写入xls文件中
book = xlwt.Workbook(encoding='utf-8', style_compression=0)
sheet = book.add_sheet('补偿略略', cell_overwrite_ok=True)
col = ('lh', 'lv', 'lsh', 'lsu')
for i in range(0, 4):
    sheet.write(0, i, col[i])
for i in range(0, fileNum):
    data = inputs[i]
    for j in range(0, 4):
        sheet.write(i + 1, j, data[j])
savepath = './inputs_mpso.xls'
book.save(savepath)

fitness = []
for i in range(fileNum):
    c = []
    a = np.loadtxt(filepath1 + '\\pareto_fitness%d.txt' % i)
    b = np.loadtxt(filepath2 + '\\pareto_fitness%d.txt' % i)
    if a.size == 0:
        c.append(None)
    else:
        for j in a:
            c.append(j)
    if b.size == 0:
        c.append(None)
    else:
        for j in b:
            c.append(j)
    inputs.append(c)
# 将c中的内容写入xls文件中
book = xlwt.Workbook(encoding='utf-8', style_compression=0)
sheet = book.add_sheet('适应度', cell_overwrite_ok=True)
for i in range(0, fileNum):
    data = inputs[i]
    for j in range(0, 4):
        sheet.write(i + 1, j, data[j])
savepath = './inputs_mpso.xls'
book.save(savepath)