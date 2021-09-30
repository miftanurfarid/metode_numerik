#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 08:28:52 2021

@author: fafa
"""
import numpy as np

a = 0
b = 1
eps = 0.00001

f = lambda x: np.exp(x) - 5*x**2

for i in range(0,51,1):
    
    if  abs(a - b) < eps:
        break
    
    c = (a + b) / 2
    
    if f(a)*f(c) < 0:
        b = c
    else:
        a = c
        
    print("Iterasi: {:02d}, akar: {:.6f}, lebar: {:.6f}".format(i,c,abs(a - b)))
    