# encoding: utf-8
import numpy as np
import optimization


# 适应值函数：实际使用时请根据具体应用背景自定义
def fitness_(in_):
    fit_1 = optimization.positionDeviations(0, 0, in_[0], in_[1])
    fit_2 = optimization.adjustTime(0, 0, in_[0], in_[1])
    fit_3 = optimization.positionDeviations3(0, 0, in_[0], in_[1])
    fit_4 = optimization.positionDeviations4(0, 0, in_[0], in_[1])
    return [fit_1,  fit_3, fit_4]
