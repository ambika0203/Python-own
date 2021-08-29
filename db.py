# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 11:42:25 2019

@author: VAIO
"""
import MySQLdb
 
db = MySQLdb.connect(host="localhost",  # your host 
                     user="root",       # username
                     passwd="",     # password
                     db="fdp")   # name of the database
 
# Create a Cursor object to execute queries.
cur = db.cursor()
 
# Select data from table using SQL query.
cur.execute("SELECT * FROM sample")
 
# print the first and second columns      
for row in cur.fetchall() :
    print (row[0], " ", row[1])