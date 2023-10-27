# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 13:20:49 2023

@author: s_herwegh22
"""


quad_zahl= []

for k in range(1,11):
    if k % 2 == 0:
        quad_zahl.append(k)
    else:
        quad_zahl.append(k**2)

print(quad_zahl)