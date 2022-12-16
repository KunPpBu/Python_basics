# Sicience modules
import numpy as np
import pandas as pd

# polotting module
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Self define functions
from ML_basic_function import *


w = 0
x = np.array([[1], [3]])
x
y = np.array([[2], [5]])
y
w = w_cal(x[0], w, y[0], lr_gd, lr = 0.02, itera_times = 1)
w
w = w_cal(x[1], w, y[1], lr_gd, lr = 0.02, itera_times = 1)
w
w = 0
w_cal(x, w, y, lr_gd, lr = 0.02, itera_times = 2)

w = 0
epoch = 40

for j in range(epoch):
    for i in range(2):
        w = w_cal(x[i], w, y[i], lr_gd, lr = 0.02, itera_times = 1)

w

def sgd_cal(X, w, y, gd_cal, epoch, lr = 0.02):
    """
    随机梯度下降计算函数
    :param X: 训练数据特征
    :param w: 初始参数取值
    :param y: 训练数据标签
    :param gd_cal：梯度计算公式
    :param epoch: 遍历数据集次数
    :param lr: 学习率      
    :return w：最终参数计算结果       
    """
    m = X.shape[0]
    n = X.shape[1]
    for j in range(epoch):
        for i in range(m):
            w = w_cal(X[i].reshape(1, n), w, y[i].reshape(1, 1), gd_cal=gd_cal, lr=lr, itera_times = 1)
    return w
