import pandas as pd
import numpy as np



# Pandas Series 
# A Pandas Series is a one-dimensional array-like object that can hold any data type.

# string 

# country = ['India', 'USA', 'China', 'Japan', 'Germany']

# print(pd.Series(country))


# Integer 

# runs = [100, 200, 300, 400, 500]

# print(pd.Series(runs,dtype='int32'))

#Cumstom Index 

# marks = [68, 75, 80, 90, 95]
# subject = ['Math', 'Science', 'English', 'History', 'Geography']

# subject_marks = pd.Series(marks, index=subject)
# print(subject_marks)


# Using Dictionary 

marks = {
     'Math': 80,
     'English':90,
     'Hindi':95,
     'Physics':98,
     'Python': 100
}

marks_series = pd.Series(marks,name = "Devesh Ke marks",dtype="int32")
print(marks_series)


# Series Attributes 

# 1. size
print(marks_series.size)

# 2. dtype
print(marks_series.dtype)

# 3. name 
print(marks_series.name)

# 4. is_unique
print(marks_series.is_unique)
# 5. index
print(marks_series.index)
# 6. values

print(marks_series.values)



# Series using read_csv  --> Real World Dataset for csv files

my_subs = pd.read_csv("dataset/subs.csv")

print(my_subs)

pd.read_csv('/dataset/kohli_ipl.csv')