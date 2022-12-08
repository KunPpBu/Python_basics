# Sicience modules
import numpy as np
import pandas as pd

# polotting module
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Self define functions
from ML_basic_function import *

# 3D plot for SSE loss
x = np.arange(-1,3,0.05)
y = np.arange(-1,3,0.05)
w, b = np.meshgrid(x, y)
SSE = (2 - w - b) ** 2 + (4 - 3 * w - b) ** 2

ax = plt.axes(projection='3d')

ax.plot_surface(w, b, SSE, cmap='rainbow')
ax.contour(w, b, SSE, zdir='z', offset=0, cmap="rainbow")  #generate mapping on z-axis，projected to the hyperplane on x-y
plt.xlabel('w')
plt.ylabel('b')
plt.show()

