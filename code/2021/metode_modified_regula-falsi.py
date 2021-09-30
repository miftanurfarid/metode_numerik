#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 09:13:16 2021

@author: fafa
"""
import numpy as np

a = 0
b = 1
eps = 0.00001
mu = 0.000001

f = lambda x: np.exp(x) - 5*x**2
mandek = 0

for i in range(0,101,1):

    if mandek == 0:
        c = b - f(b)*(b-a)/(f(b)-f(a))
    else:
        c = b - f(b)/2*(b-a)/(f(b)/2-f(a))
    
    if  abs(a - b) < eps or abs(f(c)) < mu:
        break
    
    if f(a)*f(c) < 0:
        b = c
        mandek = 0
    else:
        a = c
        mandek = 1
        
    print("Iterasi: {:02d}, akar: {:.6f}, lebar: {:.6f}".format(i,c,abs(a - b)))
