# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 16:56:11 2019

@author: Ambika
"""
dict = { "country":["Brazil", "Russia", "India", "China", "South Africa"],
"capital":["Brasilia", "Moscow", "New Delhi", "Beijing", "Pretoria"],  "area":[8.516, 17.10, 3.286, 9.597, 1.221]
"population" :[200.4, 143.5, 1252, 1357, 52.98]}
import pandas as pd
brics = pd.DataFrame(dict)