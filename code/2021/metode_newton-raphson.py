#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 10:16:54 2021

@author: fafa
"""

import numpy as np

x = 4
eps = 0.00001

#x_New = lambda x: x - (np.exp(x) - 5*x**2)/(np.exp(x) - 10*x)
x_New = lambda x: 6-x

for i in range(1,101,1):
    x_new = x_New(x)
        
    if abs(x_new - x) < eps:
        break
    
    print("iterasi:{} \t x_new:{:.6f}, x_new-x:{:.6f}".format(i,x_new,abs(x_new - x)))
    
    x = x_new