# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 12:49:20 2019

@author: Ambika
"""
#Array creation - to print entire 2D array
from array import * 
T = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]] 
for r in T: 
    for c in r:
        print(c,end = " ")
    print() 
# insert element in the array
from array import *
T = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]

T.insert(2, [0,5,11,13,6])

for r in T:
    for c in r:
        print(c,end = " ")
    print()
    
#update values in 2D array
from array import *

T = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]

T[2] = [11,9]
T[0][3] = 7
for r in T:
    for c in r:
        print(c,end = " ")
    print()
    
#deleting values from the 2D array
from array import *
T = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]

del T[3]
for r in T:
    for c in r:
        print(c,end = " ")
    print()