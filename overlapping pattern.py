# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 10:50:32 2019

@author: Ambika
"""

import re 
s = "123456789123456789"
matches = re.finditer(r'(?=(\d{10}))',s)
results = [int(match.group(1)) for match in matches]
print(results)

