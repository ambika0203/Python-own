# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 22:18:48 2019

@author: Ambika
"""
#Pattern match checking
import re
pattern = '^a...s$'
test_string = 'abyss'
result = re.match(pattern, test_string)

if result:
  print("Search successful.")
else:
  print("Search unsuccessful.")