# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Iterate over rows of cars
for lab, row in cars.iterrows():
    print(lab)
    print(row)
    
#Loop over a dataframe
    # Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Adapt for loop
for lab, row in cars.iterrows() :
    print(str(lab) + ": " + str(row["cars_per_cap"]))


# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'bonn', 
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'australia':'vienna' }
          
# Iterate over europe
for k, v in europe.items():
    print("the capital of " + str(k) + " is " + str(v))
# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
for a in areas:
    print(a)

#Loop over a list of lists

house = [["hallway", 11.25], 
         ["kitchen", 18.0], 
         ["living room", 20.0], 
         ["bedroom", 10.75], 
         ["bathroom", 9.50]]
         
# Build a for loop from scratch
for room, area in house :
    print("the " + str(room) + " is " + str(area) + " sqm")

#Loop over a numpy array
    
    # Import numpy as np
import numpy as np

# For loop over np_height
for x in np_height:
    print(str(x) + " inches")

# For loop over np_baseball
for x in np.nditer(np_baseball):
    print(x)

#add a column based on condition
    # Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Code for loop that adds COUNTRY column
for lab, row in cars.iterrows():
    cars.loc[lab, 'COUNTRY'] = row['country'].upper()
# Print cars
print(cars)

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Use .apply(str.upper)
cars['COUNTRY'] = cars['country'].apply(str.upper)
