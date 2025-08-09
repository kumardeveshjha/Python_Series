"""Q1 :- Print the given strings as per stated format.
Given strings:

"Data" "Science" "Mentorship" "Program" 
"By" "CampusX"
Output:

Data-Science-Mentorship-Program-started-By-CampusX"""

# solution
# print("Data","Science","Mentorship","Program",sep='-',end='-started-')
# print("By","CampusX",sep='-')
     
""" Q2:- Write a program that will convert celsius value to fahrenheit."""
 
#  Solution  
# celsius = float(input("Enter temperature in celsius: "))
# fahrenheit = (celsius * 9/5) + 32
# print('The Temperature in Fahrenheight is:',fahrenheit)



"""Q3:- Take 2 numbers as input from the user.Write a program to swap the numbers without using any special python syntax."""

# Solution 
# a = int(input("Enter the first Number: "))
# b = int(input("Enter the second Number: "))
# Swapping 
# a,b = b,a
# second Logic 
# a  = a+b 
# b = a-b
# a = a-b 
# print("After swapping the a is: ",a)
# print("After swapping the b is: ",b)




"""Q4:- Write a program to find the euclidean distance between two coordinates.Take both the coordinates from the user as input."""

# x1 = int(input("Enter the the first coordinate: "))
# y1 = int(input("Enter the the second coordinate: "))
# x2 = int(input("Enter the the third coordinate: "))
# y2 = int(input("Enter the the fourth coordinate: "))

# ecludinDist = int((x1-x2)**2 + (y1-y2)**2)**0.5

# print(int(ecludinDist))



"""Q5:- Write a program to find the simple interest when the value of principle,rate of interest and time period is provided by the user."""

# Solution 
# p = int(input("Enter the value of Principal: "))
# r = float(input("Enter the value of rate: "))
# t = int(input("Enter the value of time: "))

# SI = (p*r*t)/100

# print(int(SI))

"""Q6:- Write a program that will tell the number of dogs and chicken are there when the user will provide the value of total heads and legs.
For example: Input: heads -> 4 legs -> 12
Output: dogs -> 2 chicken -> 2 """

# d = 4l + 1h             
# c = 2l + 1h

# d +c = 6l + 2h 

# Number of dogs  d = 4 - c
# Number of chickens 

# h = int(input('Enter the number of heads: '))
# l = int(input('Enter the number of legs: '))




"""Q7:- Write a program to find the sum of squares of first n natural numbers where n will be provided by the user."""
# Solution 

# n = int(input('Enter the number : '))

# squaredSum = (n*(n+1)*(2*n+1))/6
# print(int(squaredSum))




"""Q8:- Given the first 2 terms of an Arithmetic Series.Find the Nth term of the series. Assume all inputs are provided by the user."""

# a = int(input('Enter the first term : '))
# b = int(input('Enter the second term : '))
# n = int(input('Enter the number of term : '))
# d = b-a 

# nTerm = a + (n-1)*d

# print(int(nTerm))





"""Q9:- Given 2 fractions, find the sum of those 2 fractions.Take the numerator and denominator values of the fractions from the user."""

# n1 = int(input('Enter the first numerator : '))
# n2 = int(input('Enter the second numerator : '))
# d1 = int(input('Enter the first denominator : '))
# d2 = int(input('Enter the second denominator : '))

# sum = (n1/d1)+(n2/d2)

# print(int(sum))



"""
Q10:- Given the height, width and breadth of a milk tank, you have to find out how many glasses of milk can be obtained? Assume all the inputs are provided by the user.
Input:
Dimensions of the milk tank
H = 20cm, L = 20cm, B = 20cm

Dimensions of the glass
h = 3cm, r = 1cm
"""

# Mix Tank Dimensions 

# H = int(input('Enter the Height of Tank: '))
# L = int(input('Enter the Length of Tank: '))
# B = int(input('Enter the Width of Tank: '))

# V = H*L*B

# # Dimensions of the glass 

# h = int(input('Enter the Height of Glass: '))
# l = int(input('Enter the Length of Glass: '))
# b = int(input('Enter the Width of Glass: '))

# v = l*b*H

# numberOfGlasses = int(V/v)

# print(numberOfGlasses)





