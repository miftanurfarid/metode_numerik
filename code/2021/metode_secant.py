#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 06:08:11 2021

@author: fafa
"""
import numpy as np

x0 = 0.5
x1 = 1
eps = 0.00001
f = lambda x: np.exp(x) - 5*x**2

for i in range(1,101,1):
    x2 = x1 - f(x1)*(x1-x0)/(f(x1)-f(x0))
    
    if abs(x2-x1) < eps:
        break
    
    print("iterasi:{:02d}, akar:{:.6f}, lebar:{:.6f}".format(i,x2,abs(x2-x1)))
    
    x0 = x1
    x1 = x2