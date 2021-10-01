#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 03:39:55 2021

@author: fafa
"""
import numpy as np

x = 1
eps = 0.000001

x_new1 = lambda x: np.sqrt(2*x+3)
x_new2 = lambda x: 3/(x-2)
x_new3 = lambda x: (x**2 - 3)/2
x_new4 = lambda x: np.sqrt(1/5*np.exp(x))

for i in range(1,101,1):
    xr = x_new4(x)
    
    print("iterasi:{:02d}, xr:{:.6f}, xr-x:{:.6f}".format(i,xr,abs(xr-x)))
    
    if abs(xr-x) < eps:
        break
    
    x = xr