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
