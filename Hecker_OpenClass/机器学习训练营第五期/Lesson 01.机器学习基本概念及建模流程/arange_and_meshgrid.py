#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 10:59:10 2022

@author: amanda
"""
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = np.arange(-1,3,0.05)
y = np.arange(-1,3,0.05)
w, b = np.meshgrid(x, y)
SSE = (2 - w - b) ** 2 + (4 - 3 * w - b) ** 2

ax = plt.axes(projection='3d')

ax.plot_surface(w, b, SSE, cmap='rainbow')
ax.contour(w, b, SSE, zdir='z', offset=0, cmap="rainbow")  #生成z方向投影，投到x-y平面
plt.xlabel('w')
plt.ylabel('b')
plt.show()

x = np.arange(-10,10,0.1)
y = x ** 2
plt.plot(x, y, '-')
plt.show()

# example of meshgrid: Return coordinate matrices from coordinate vectors.

m = np.arange(1,5)
#n = np.arange(5,8)
n = np.array(range(5,8))
n[::-1]
mm,nn = np.meshgrid(m,n[::-1])
print(mm,nn)


