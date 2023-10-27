# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 14:22:20 2023

@author: s_herwegh22
"""

import matplotlib.pyplot as plt

s_n = []

r= 0.5
a= 1
n= 10
x=0

for k in range(1, n+1):
    x += (a*r)**(k-1)
    s_n.append(x)
    
plt.plot(s_n)
    