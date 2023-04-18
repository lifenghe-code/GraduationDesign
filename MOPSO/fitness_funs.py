# encoding: utf-8
# 适应值函数：实际使用时请根据具体应用背景自定义
import numpy as np
import optimization


# 这代码写的真是毫无逻辑，硅基生物看了都得吐
def fitness_(in_, position_error, key):
    if key == 0:
        fit_0 = optimization.positionDeviations0(0, 0, in_[0], in_[1], position_error)
        fit_1 = optimization.positionDeviations1(0, 0, in_[0], in_[1], position_error)
        fit_3 = optimization.positionDeviations3(0, 0, in_[0], in_[1], position_error)
        tmp1 = [fit_0, fit_1, fit_3]
        tmp2 = list()
        for i in range(len(position_error)):
            if position_error[i] == 0:
                pass
            else:
                tmp2.append(tmp1[i])
        return tmp2
    elif key == 1:
        fit_2 = optimization.positionDeviations2(in_[0], in_[1], 0, 0, position_error)
        fit_4 = optimization.positionDeviations4(in_[0], in_[1], 0, 0, position_error)
        fit_5 = optimization.positionDeviations5(in_[0], in_[1], 0, 0, position_error)
        tmp1 = [fit_2, fit_4, fit_5]
        tmp2 = list()
        for i in range(len(position_error)):
            if position_error[i] == 0:
                pass
            else:
                tmp2.append(tmp1[i])
        return tmp2
    else:
        print("KEY ERROR!")
