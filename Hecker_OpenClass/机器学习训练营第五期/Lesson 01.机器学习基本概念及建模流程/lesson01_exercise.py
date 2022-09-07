#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 10:14:37 2022

@author: amanda
"""

import os
#import sys
# directory of script file
#print(os.path.abspath(os.path.dirname(sys.argv[0])))
# change current working directory
#os.chdir(os.path.abspath(os.path.dirname(sys.argv[0])))
# get current working directory
#print(os.getcwd())


#set working directory
os.chdir('/Users/amanda/Documents/Kun_Bu/Python_basics/Hecker_OpenClass/机器学习训练营第五期/Lesson 01.机器学习基本概念及建模流程')
print(os.getcwd())

# 导入相关包
import numpy as np
import pandas as pd


iris_df = pd.read_csv("iris.csv")
print(iris_df)

ab_df = pd.read_csv("abalone.txt", sep='\t', header=None)
print(ab_df)

ab_df.columns

ab_df.columns = ['Gender', 'Length', 
                 'Diameter', 'Height', 
                 'Whole weight', 'Shucked weight', 
                 'Viscera weight', 'Shell weight',
                 'Rings']
print(ab_df)

ab_df.to_csv('abalone.csv', index=False)

