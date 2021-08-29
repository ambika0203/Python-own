# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 16:28:25 2019

@author: Ambika
"""
#set creation
Days=set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])
Months={"Jan","Feb","Mar"}
Dates={21,22,17}
print(Days)
print(Months)
print(Dates)

#Accessing the values
Days=set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])
 
for d in Days:
	print(d)
#Adding an item
    Days=set(["Mon","Tue","Wed","Thu","Fri","Sat"])
 
Days.add("Sun")
print(Days)

#Removing an item
Days=set(["Mon","Tue","Wed","Thu","Fri","Sat"])
 
Days.discard("Sun")
print(Days)

#Union
DaysA = set(["Mon","Tue","Wed"])
DaysB = set(["Wed","Thu","Fri","Sat","Sun"])
AllDays = DaysA|DaysB
print(AllDays)

#Intersection
DaysA = set(["Mon","Tue","Wed"])
DaysB = set(["Wed","Thu","Fri","Sat","Sun"])
AllDays = DaysA & DaysB
print(AllDays)

#Difference
DaysA = set(["Mon","Tue","Wed"])
DaysB = set(["Wed","Thu","Fri","Sat","Sun"])
AllDays = DaysA - DaysB
print(AllDays)

#Compare
DaysA = set(["Mon","Tue","Wed"])
DaysB = set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])
SubsetRes = DaysA <= DaysB
SupersetRes = DaysB >= DaysA
print(SubsetRes)
print(SupersetRes)