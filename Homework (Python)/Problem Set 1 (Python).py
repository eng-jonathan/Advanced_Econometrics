# -*- coding: utf-8 -*-
"""
Spyder Editor

Title: Econ 387 Homework 1
Author: Jonathan Eng
Date: Febuary 10, 2020
"""

import numpy as np

#1
np.random.seed(37)
tmp = np.random.randn(21,21)
print (tmp)
print(tmp.shape)
print(np.size(tmp))

#2
np.fill_diagonal(tmp,1)
print(tmp);

#3
print(np.linalg.cond(tmp))

#4
print(np.linalg.inv(tmp))

#5
print(np.trace(tmp))

#6
tmp=np.sort(tmp,0)
print(tmp)

#7
tmp = np.delete(tmp,len(tmp)-1,0)
tmp = np.delete(tmp,len(tmp[0])-1,1)
print(tmp)

#8
tmp1 = np.reshape(tmp, (40,10)) 
print(tmp1)

#9
tmp2 = np.tile(tmp1, 4)
print(tmp2)

#10
print(np.linalg.cond(tmp2))

#11
print(np.shape(tmp2))
print(np.linalg.inv(tmp2)) #singular matrix error

#12
for i in range(len(tmp2)):
    for j in range(len(tmp2[0])):
        if(tmp2[i][j]<=0):
            tmp2[i][j]=.5
print(tmp2)

#13
tmp2[0][0] =-tmp2[0][0]
print(tmp2)

#14
tmp3 = np.log(tmp2)
print(tmp3)

#15
print(np.argwhere(np.isnan(tmp3)))
