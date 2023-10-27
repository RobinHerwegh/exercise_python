# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 12:23:11 2023

@author: s_herwegh22
"""
def steigung_funktion(x):
    x1 = x[0]
    y1 = x[1]
    x2 = x[2]
    y2 = x[3]

    delta_x = (x2-x1)
    delta_y = (y2-y1)

    if delta_x == 0:
        print("Die Steigung ist nicht definiert")
        
    else:
        steigung = delta_y/delta_x
        print(steigung)

steigung_funktion([1,1,5,4])
