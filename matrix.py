# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 15:25:22 2019

@author: Ambika
"""
#Matrix
from numpy import * 
a = array([0,1,2, 3, 4, 5, 6, 7])
m=reshape(a,(4,2))
m


        
        
        
from numpy import * 
a = array(['Mon',18,20,22,17],['Tue',11,18,21,18],
            ['Wed',15,21,20,19],['Thu',11,20,22,21],
		   ['Fri',18,17,23,22],['Sat',12,22,20,18],
		   ['Sun',13,15,19,16],['Sun',13,15,19,16])
    
m = reshape(a,(8,5))# reshape method from numpy
print(m)
#Accessing the Matrix values
from numpy import * 
m = array([['Mon',18,20,22,17],['Tue',11,18,21,18],
		   ['Wed',15,21,20,19],['Thu',11,20,22,21],
		   ['Fri',18,17,23,22],['Sat',12,22,20,18],
		   ['Sun',13,15,19,16]])
    
# Print data for Wednesday
print(m[2])

# Print data for friday evening
print(m[4][3])

#adding a row
from numpy import * 
m = array([['Mon',18,20,22,17],['Tue',11,18,21,18],
		   ['Wed',15,21,20,19],['Thu',11,20,22,21],
		   ['Fri',18,17,23,22],['Sat',12,22,20,18],
		   ['Sun',13,15,19,16]])
    
m_r = append(m,[['Avg',12,15,13,11]],0)

print(m_r)

#Adding a column
from numpy import * 
m = array([['Mon',18,20,22,17],['Tue',11,18,21,18],
		   ['Wed',15,21,20,19],['Thu',11,20,22,21],
		   ['Fri',18,17,23,22],['Sat',12,22,20,18],
		   ['Sun',13,15,19,16]])
    
m_c = insert(m,[5],[[1],[2],[3],[4],[5],[6],[7]],1)

print(m_c)
#Delete a row from a matrix
from numpy import * 
m = array([['Mon',18,20,22,17],['Tue',11,18,21,18],
		   ['Wed',15,21,20,19],['Thu',11,20,22,21],
		   ['Fri',18,17,23,22],['Sat',12,22,20,18],
		   ['Sun',13,15,19,16]])
    
m = delete(m,[2],0)

print(m)
#Delete a column from a matrix
from numpy import * 
m = array([['Mon',18,20,22,17],['Tue',11,18,21,18],
		   ['Wed',15,21,20,19],['Thu',11,20,22,21],
		   ['Fri',18,17,23,22],['Sat',12,22,20,18],
		   ['Sun',13,15,19,16]])
    
m = delete(m,s_[2],1)

print(m)
#Update a row
from numpy import * 
m = array([['Mon',18,20,22,17],['Tue',11,18,21,18],
		   ['Wed',15,21,20,19],['Thu',11,20,22,21],
		   ['Fri',18,17,23,22],['Sat',12,22,20,18],
		   ['Sun',13,15,19,16]])
    
m[3] = ['Thu',0,0,0,0]

print(m)