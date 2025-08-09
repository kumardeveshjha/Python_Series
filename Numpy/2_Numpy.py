# Numpy Array vs Python Lists

# Speed 

# a = [i for i in range(10000000)]
# b = [i for i in range(10000000,20000000)]

# c = []

# import time 

# start = time.time()
# for i in range(len(a)):
#      c.append(a[i]+b[i])

# print(time.time()-start)

# Numpy 
import numpy as np

# a = np.arange(10000000)
# b = np.arange(10000000,20000000)

# start = time.time()
# c = a+b

# print((time.time()-start))

# 2. in Terms of memory 

# import sys 

# a = [i for i in range(10000000)]
# print(sys.getsizeof(a))

# b = np.arange(10000000,dtype=np.int32)

# print(sys.getsizeof(b))


# :::::::::::::::Advanced Indexing::::::::::::::::
# a = np.arange(24).reshape(6,4)

# print(a)


#Fancy Indexing 
# When we desires column or row means smartly handling the selected row or column
# print(a[:,[0,2,3]])
# print(a[[0,1],:])

# Boolean Indexing 
# when we want to extract the data using the logic and data analysis 
# Best method for data filteration when we have given conditions 

# a1 = np.random.randint(1,100,24).reshape(6,4)

# print(a1)

# When the number is greater than 50 

# print(a1>50)
# print(a1[a1>50])

# Find out even numbers 

# print(a1[a1%2==0])

# numbers those are greater than 50 and also even 
# Whenever we are working with the boolean values we use the bitwise operators 
#here we will use "&" in place of "and"
# print(a1[(a1>50)&(a1%2==0)])
# print(a1[a1%7==0])


# Broadcasting 

#Example 1 
# a2 = np.arange(12).reshape(4,3)
# a3 = np.arange(3)

# print(a2)
# print(a3)

# print(a3+a2)


# Example 2 
# a4 = np.arange(12).reshape(3,4)
# a5 = np.arange(3)

# print(a4)
# print(a5)
# print( a4 + a5)   # there will be an error 

# Example 3 
# a = np.arange(3).reshape(1,3)
# b = np.arange(3).reshape(3,1)

# print(a)
# print(b)
# print(a+b)

#Example 4 
# a = np.array([1])
# b = np.arange(4).reshape(2,2)

# print(a)
# print(b)
# print(a+b)

# a = np.arange(12).reshape(3,4)
# b = np.arange(12).reshape(4,3)

# print(a)
# print(b)
# print(a+b)

#Example 

# a = np.arange(16).reshape(4,4)
# b = np.arange(4).reshape(2,2)

# print(a)
# print(b)
# print(a+b)

# Example 
# a = np.arange(6).reshape(1,6)
# b = np.arange(6).reshape(3,2)

# print(a)
# print(b)
# print(a+b)

"""Working with the mathematical functions"""
 
 
#1. Sigmoid 
 
# def sigmoid(array):
#      return 1/(1+np.exp(-(array)))

# a = np.arange(100)
# print(sigmoid(a))

# Mean squared error : Loss Function 

# actual = np.random.randint(1,50,25)
# predicted = np.random.randint(1,50,25)


# def mse(actual,predicted):
#      return np.mean((actual- predicted)**2)

# print(mse(actual,predicted))

# binary cross entropy  --> Homework 

#Working with missing values -> np.nan

# a = np.array([1,2,3,4,5,6,np.nan,7,8])

# print(a)
# # To find the missing values 
# print(np.isnan(a))

# # Now we will remove missing values
# print(a[~np.isnan(a)])



#Plotting Graphs 

#Plotting a 2D graph 
# x = y 

import matplotlib.pyplot as plt
# x = np.linspace(-100,100,100)
# y = x
# print(y)

# plt.plot(x,y)
# plt.show()

# y = x**2

# plt.plot(x,y)
# plt.show()

# x  = np.linspace(-10,10,10)

# y = np.sin(x)

# plt.plot(x,y)
# plt.show()

# x = np.linspace(-10,10,10)

# y = np.log(x)

# plt.plot(x,y)
# plt.show()



