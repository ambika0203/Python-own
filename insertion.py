# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 14:33:35 2019

@author: VAIO
"""

import MySQLdb

mydb = MySQLdb.connect(
  host="localhost",
  user="root",
  passwd="",
  database="bca"
)

mycursor = mydb.cursor()

sql = "INSERT INTO login (username,password) VALUES (%s, %s)"
val = ("mca", "123")

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
