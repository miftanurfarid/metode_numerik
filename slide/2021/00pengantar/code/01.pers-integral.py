#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 06:22:11 2021
Pengantar Metode Numerik: Persamaan Integral
@author: fafa
"""

from numpy import linspace
import matplotlib.pyplot as plt

x = linspace(-2,2,100)

y = lambda x: 4 - x**2

fx = y(x)

plt.plot(x,fx)
plt.grid(axis = 'both')
plt.legend(['$f(x) = 4 - x^2$'])
plt.xlabel('x')
plt.savefig('img003.svg', format='svg', dpi=1200)