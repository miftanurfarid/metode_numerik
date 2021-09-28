#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 04:14:47 2021

@author: fafa
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,5,0.1)
y = lambda x: np.power((x - 3),2)

plt.plot(x,y(x))