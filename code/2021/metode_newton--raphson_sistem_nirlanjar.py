#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 06:59:32 2021

@author: fafa
"""

x0 = 1.5
y0 = 3.5
eps = 0.000001

u = lambda x,y: x**2 + x*y - 10
v = lambda x,y: y + 3*x*y**2 - 57

dudx = lambda x,y: 2*x + y
dudy = lambda x,y: x
dvdx = lambda x,y: 3*y**2
dvdy = lambda x,y: 1 + 6*x*y

for i in range(1,101,1):
    detJac = dudx(x0,y0)*dvdy(x0,y0) - dudy(x0,y0)*dvdx(x0,y0)
    
    x1 = x0 - (u(x0,y0)*dvdy(x0,y0) + v(x0,y0)*dudy(x0,y0)) / detJac
    
    y1 = y0 + (u(x0,y0)*dvdx(x0,y0) - v(x0,y0)*dudx(x0,y0)) / detJac
    
    print("iterasi:{:02d}, x:{:.6f}, y:{:.6f}, abs(x1-x0):{:.6f}, abs(y1-y0):{:.6f}".format(i,x1,y1,abs(x1-x0),abs(y1-y0)))
    
    if abs(x1-x0) < eps and abs(y1-y0) < eps:
        break
    
    x0 = x1
    y0 = y1