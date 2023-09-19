#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 14:46:47 2023

@author: fafa
"""
from matplotlib import pylab


t = [0, 20, 40, 60, 80, 100]
T = [26.0, 48.6, 61.6, 71.2, 74.8, 75.2]

pylab.plot(t, T, '-o')
pylab.xlabel('time (sec.)')
pylab.ylabel('temperature (deg. C)')
pylab.grid()