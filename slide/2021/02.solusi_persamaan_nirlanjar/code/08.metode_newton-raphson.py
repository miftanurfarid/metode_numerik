#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 08:24:40 2021

@author: fafa
"""
import numpy as np

x = 1
eps = 0.000001

x_new = lambda x: x - (np.exp(x) - 5*x**2)/(np.exp(x) - 10*x)

for i in range(1,101,1):
    xr = x_new(x)
    
    print("iterasi:{:02d}, xr:{:.6f}, xr-x:{:.6f}".format(i,xr,abs(xr-x)))
    
    if abs(xr-x) < eps:
        break
    
    x = xr