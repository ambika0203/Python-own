# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 23:22:45 2019

@author: VAIO
"""

my_set = {1, 2, 3}
print(my_set)

# set of mixed datatypes
my_set = {1,2,3,4,3,2}
print(my_set)
my_set = {1,3}
print(my_set)


my_set.add(2)
print(my_set)

# add multiple elements
# Output: {1, 2, 3, 4}
my_set.update([2,3,4])
print(my_set)

# add list and set
# Output: {1, 2, 3, 4, 5, 6, 8}
my_set.update([4,5], {1,6,8})
print(my_set)
my_set.discard(4)
print(my_set)
my_set.remove(4)