#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 05:04:23 2021
Pengantar Metode Numerik: Persamaan Non Linear
@author: fafa
"""

from numpy import linspace
import matplotlib.pyplot as plt

y = lambda x: x**2 - 6*x + 8

x = linspace(2.5,7,100)
y1 = y(x)

fig, ax = plt.subplots()
plt.plot(x,y1)
plt.grid(color='r', linestyle='-', linewidth=0.3, axis='y')
plt.xlabel('sb-x', loc='right')
plt.legend(['$f(x) = x^2 - 6x + 8$'])
fig.savefig('img001.svg', format='svg', dpi=1200)