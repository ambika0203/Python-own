# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 10:10:54 2019

@author: Ambika
"""

Most list methods will change the list they're called on. Examples are:

append(), that adds an element to the list it is called on,
remove(), that removes the first element of a list that matches the input, and
reverse(), that reverses the order of the elements in the list it is called on.
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Print out the index of the element 20.0
print(areas.index(20))

# Print out how often 14.5 appears in areas
print(areas.count(14.5))
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50,18.0]

# Use append twice to add poolhouse and garage size
areas.append(24.5)
areas.append(15.45)

# Print out areas
print(areas)

# Reverse the orders of the elements in areas
areas.reverse()

# Print out areas
print(areas)

List Sorting
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Paste together first and second: full
full = first + second

# Sort full in descending order: full_sorted
full_sorted = sorted(full, reverse=True)
areas.remove(18.0)
areas