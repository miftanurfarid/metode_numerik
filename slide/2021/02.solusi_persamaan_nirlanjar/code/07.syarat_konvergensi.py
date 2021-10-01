#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 03:12:37 2021

Syarat konvergensi dari x^3 - 3x + 1 dalam selang [1,2] dengan 

@author: fafa
"""
import numpy as np

f1 = lambda x: abs(x**2)
f2 = lambda x: abs( 2*x / (x**2 - 3)**3 )
f3 = lambda x: abs( (-3*x+2)/(x ** 3) )
f4 = lambda x: abs(np.sqrt(1/5*np.exp(x)))


for x in np.arange(1,2.1,0.1):
    print("x:{:.2f} \t |g'(x)| = {:.4f}".format(x,f4(x)))