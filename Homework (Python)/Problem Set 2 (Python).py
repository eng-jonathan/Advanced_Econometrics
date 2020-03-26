# -*- coding: utf-8 -*-
"""
Spyder Editor

Title: Econ 387 Homework 2
Author: Jonathan Eng
Date: Febuary 19, 2020
"""

import numpy as np
import scipy as sp

#1
def estimate_intercept_and_slope(x, y):
    mean_x = sp.mean(x)
    mean_y = sp.mean(y)
    sumnum = 0
    sumden = 0
    for i in range(0, len(x) - 1):
        sumnum = sumnum + (x[i] - mean_x) * (y[i] - mean_y)
        sumden = sumden + ((x[i] - mean_x) ** 2)
    slope = sumnum/sumden #b1
    intercept = mean_y - (slope * mean_x) #b0
    return (intercept, slope) #b0, b1

#2
np.random.seed(37)

#3
x = np.random.randn(1000)

#4
e = np.random.randn(1000)
y = 0.5 + (1.8 * x) + e

#5
print(estimate_intercept_and_slope(x, y))
b0, b1 = estimate_intercept_and_slope(x, y)

simple_linear_regression = b0 + (b1 * x) + e
print(y == simple_linear_regression)




#6
'''
The estimates I obtained for b0 and b1 are close to the true values of .5 and 1.8, with my b0 being ~0.484 and my b1 being ~1.796. The values are not exact because the formula only allows us to estimate the true values and will not be exact due to noise. 
'''

#7
e = np.random.randn(1000)
y = .5 + (1.8 * x) + e

b0_2, b1_2 = estimate_intercept_and_slope(x, y)

print(b0 == b0_2)
print(b1 == b1_2)

'''
The value of the estimates are similar, however not the same due to the change in the noise (e) in the equation.
'''
