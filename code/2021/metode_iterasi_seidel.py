#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 06:32:19 2021

@author: fafa
"""
import numpy as np

x0 = 1.5
y0 = 3.5
eps = 0.000001

# ini divergen
#g1 = lambda x,y: (10 - x**2)/y
#g2 = lambda x,y: 57 - 3*x*y**2

# ini konvergen
g1 = lambda x,y: np.sqrt(10-x*y)
g2 = lambda x,y: np.sqrt((57-y)/(3*x))

for i in range(1,101,1):
    x1 = g1(x0,y0)
    y1 = g2(x1,y0)
    
    if abs(x1-x0) < eps and abs(y1-y0) < eps:
        break
    
    print("iterasi:{:02d}, x:{:.6f}, y:{:.6f}, abs(x1-x0):{:.6f}, abs(y1-y0):{:.6f}".format(i,x1,y1,abs(x1-x0),abs(y1-y0)))
    
    x0 = x1
    y0 = y1