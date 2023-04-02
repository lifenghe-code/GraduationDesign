# encoding: utf-8
import numpy as np
import optimization


# 适应值函数：实际使用时请根据具体应用背景自定义
def fitness_(in_):
    fit_0 = optimization.positionDeviations0(0, 0, in_[0], in_[1])
    fit_1 = optimization.positionDeviations1(0, 0, in_[0], in_[1])
    # fit_2= optimization.positionDeviations1(in_[0], in_[1], 0, 0)
    fit_3 = optimization.positionDeviations3(0, 0, in_[0], in_[1])
    # fit_4 = optimization.positionDeviations3(in_[0], in_[1], 0, 0)
    # fit_5 = optimization.positionDeviations4(in_[0], in_[1], 0, 0)
    return [fit_0, fit_1, fit_3]
