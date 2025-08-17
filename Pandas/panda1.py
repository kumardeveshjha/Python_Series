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

# Cumstom Index 

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

# marks_series = pd.Series(marks,name = "Devesh Ke marks",dtype="int32")
# print(marks_series)


# Series Attributes 

# 1. size
# print(marks_series.size)

# 2. dtype
# print(marks_series.dtype)

# 3. name 
# print(marks_series.name)

# 4. is_unique
# print(marks_series.is_unique)
# 5. index
# print(marks_series.index)
# 6. values

# print(marks_series.values)



# Series using read_csv  --> Real World Dataset for csv files

my_subs = pd.read_csv("dataset/subs.csv").squeeze()

# print(my_subs.values)

kohli_runs = pd.read_csv('dataset/kohli_ipl.csv',index_col='match_no').squeeze()

# print(kohli_runs)

movies = pd.read_csv('dataset/bollywood.csv',index_col='movie').squeeze()

# print(movies)

# Series important methods 

# 1. Head and tail  top 5 amd last 5 rows

# print(movies.head())
# print(movies.head(10))  # we can also specify the number of rows and columns 
# print(movies.tail(10))

# 2. sample()  gives randomly any rows : used when data is biased
 
# print(my_subs.sample())
# print(movies.sample(10))

# 3. value_counts :-> To count the frequency of any data in decending order

# print(movies.value_counts())

# sort_values :-> It sorts the values 

# print(kohli_runs.sort_values(ascending=False).head(1).values[0])  #method chainoing 

# print(movies.sort_index()) # it is used to sort the index 
# print(movies.sort_index(inplace=True))  # it makes it permanent store


# Series Maths Methods 

# Count  :-> It count the total number of values in the data 

# print(kohli_runs.count())

# Sum() , Product()  :-> These sums up and multiply the values in the data the values 

# print(my_subs.sum())

# Mean, mediam, mode, std, var 

# print(kohli_runs.mean())
# print(kohli_runs.mode())
# print(kohli_runs.std())
# print(kohli_runs.var())

# Min/ Max 

# print(kohli_runs.min())

# descibe :-> It provides all the details 

# print(kohli_runs.describe())


## ----> Series Indexing 

# x = pd.Series([10,11,23,46,67,34])
# print(x[2])

# Negative indexing : only for the string values 
# print(x[-1])

# Slicing 

# print(kohli_runs[1:10])

# Negative slicing 

# print(kohli_runs[-19: ])

# print(kohli_runs[: : 3])

# fancy Indexing 

# print(kohli_runs[[1,2,3,4]])

# label indexing 

# print(movies)

# print(movies['Hum Tumhare Hain Sanam'])
# print(movies[['Why Cheat India','The Accidental Prime Minister (film)','Awara Paagal Deewana']])

# Editing the series 


# Using indexing 

# marks['Math']= 100

# print(marks)

# What if any index does not exists 

# marks['yoga'] = 100

# print(marks)

# slicing 

# runs = pd.Series([10,20,30,54,72,100,101,103])

# runs[0:3] = [80,85,90]

# print(runs)

## label indexing 

# runs[[1,2,3]] = [100,105,95]

# print(runs.describe())



# Series with Python functionalities 













