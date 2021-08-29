# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 22:35:30 2019

@author: VAIO
"""

import MySQLdb
 
db = MySQLdb.connect(host="localhost",  # your host 
                     user="root",       # username
                     passwd="")   # password
print(db)