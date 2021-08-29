# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 23:08:47 2019

@author: VAIO
"""

my_dict = {'name':'Jack', 'age': 26}

# update value
my_dict['age'] = 27

#Output: {'age': 27, 'name': 'Jack'}
print(my_dict)

# add item
my_dict['address'] = 'Downtown'  

# Output: {'address': 'Downtown', 'age': 27, 'name': 'Jack'}
print(my_dict)
print (len(my_dict))
dict2 = my_dict.copy() 
print ("New Dictionary : %s" % str(dict2))
print ("Value : %s" % dict2.keys())
print ("Value : %s" % dict2.values())
