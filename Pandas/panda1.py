import pandas as pd
import numpy as np



# Pandas Series 
# A Pandas Series is a one-dimensional array-like object that can hold any data type.

# string 

country = ['India', 'USA', 'China', 'Japan', 'Germany']

print(pd.Series(country))


# Integer 

runs = [100, 200, 300, 400, 500]

print(pd.Series(runs,dtype='int32'))

#Cumstom Index 

marks = [68, 75, 80, 90, 95]
subject = ['Math', 'Science', 'English', 'History', 'Geography']

subject_marks = pd.Series(marks, index=subject)
print(subject_marks)




