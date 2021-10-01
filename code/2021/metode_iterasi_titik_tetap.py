#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 09:18:48 2021

@author: fafa
"""
import numpy as np

# contoh 2
#x = 4

# contoh 3
#x = 1.3 # bentuk 2, x = 1.1 atau 1.2
        # bentuk 3, x = 1.3 atau 1.4 atau 1.5

x = 1
eps = 0.00001

# contoh 2
#g1 = lambda x: np.sqrt(2*x + 3) # prosedur 1
#g2 = lambda x: 3 / (x-2) # prosedur 2
#g3 = lambda x: (x**2 - 3)/2 # prosedur 3

# contoh 3
g2 = lambda x: -1 / (x**2 - 3)
g3 = lambda x: 3/x - 1/x**2
g4 = lambda x: np.sqrt(1/5*np.exp(x))

for i in range(1,101,1):
    x_new = g4(x)
    
    if abs(x_new - x) < eps:
        break
    
    print("iterasi:{} \t x_new:{:.6f}, x_new-x:{:.6f}".format(i,x_new,abs(x_new - x)))
    
    x = x_new