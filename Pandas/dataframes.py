import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

student_data = [
     [100,70,10],
     [120,100,24],
     [80,60,4]
]



print(pd.DataFrame(student_data,columns=['iq','marks','Packages']))


# Plotting Graph 
# plotted_data = pd.DataFrame(student_data,columns=['iq','marks','Packages'])

# plotted_data.plot(kind='bar')
# plt.show()


## --> Creating a DataFrame from Dictiomnary 

my_data = {
     'iq':[100,120,80,90,0,0],
     'Marks':[90,100,80,70,0,0],
     'Packages':[12,18,10,4,0,0]
}

my_data = pd.DataFrame(my_data)
print(my_data)

## --> Real world Data Set. 

##  using read_csv

ipl = pd.read_csv('dataset/ipl-matches.csv')
movies = pd.read_csv('dataset/bollywood.csv')

# print(movies)

## Some important DataFrame Attributes and Methods

## 1. Shape 

# print(movies.shape)

## dtype 

# print(movies.dtypes)

## index

# print(movies.index)

## Column 

# print(movies.columns)

## Values 

# print(ipl.values)

##-->> Functions of DataFrame 

# Head and Tail 

# print(movies.head(1))
# print(movies.tail(1))

# Sample()

# print(ipl.sample())

# info() : High level info of the data it tell the info 

# print(ipl.info())

# dwscribe() : To give mathematical summary when we have numerical columns 

# print(movies.describe())
print(ipl.describe())

## isnull()

print(ipl.isnull().sum())

## duplicate()

print(ipl.duplicated().sum())
print(my_data.duplicated().sum())

 






