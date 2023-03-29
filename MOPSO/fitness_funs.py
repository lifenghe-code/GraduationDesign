# encoding: utf-8
import numpy as np
import optimization


# 适应值函数：实际使用时请根据具体应用背景自定义
def fitness_(in_):
    fit_1 = optimization.positionDeviations(in_[0], in_[1], Delta_lh=0, Delta_lv=0)
    fit_2 = optimization.adjustTime(in_[0], in_[1], Delta_lh=0, Delta_lv=0)
    return [fit_1, fit_2]
