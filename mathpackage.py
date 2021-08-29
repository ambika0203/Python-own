# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 00:43:40 2019

@author: Ambika
"""
# Example of importing a Package
#Definition of radius
r = 0.43

# Import the math package
import math

# Calculate C
C = 2 * math.pi * r

# Calculate A
A = math.pi * (r**2)

# Build printout
print("Circumference: " + str(C))
print("Area: " + str(A))