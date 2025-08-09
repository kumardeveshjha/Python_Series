print("Hello Python")

# print function


#Data types in python 2
#3. Integers   
#4. Floats
#3. Strings
#4. Booleans
#5. Lists
#6. Tuples
#7. Sets
#8. Dictionaries

#Variables and constants  
"""superhero  = "Batman"
#variables should be in lowercase and use underscore to separate words
marvelHero = "Ironman"
marvelHero = "Spiderman"
print(superhero, marvelHero,marvelHero)"""


"""hero01,hero02,hero03,hero04= "Dev","devesh","devansh","devendra"
print(hero01)
print(hero02)
print(hero03)
print(hero04)

# or 
print(hero01,hero02,hero03,hero04,sep="\n") 
print("Hello","world")
"""
#or 
# assigning multivariable same data 

"""x = y = z = 10
print(x)
print(y)
print(z)
print(x,y,z)


## Input function 

number_1 = int(input("Enter the first number: "))
number_2 = int(input("Enter the second number: "))

#use int() to convert the input string to integer
# the default data type of input is string
sum = number_1 + number_2
print(sum)
print(number_1 + number_2) """

# changing the data type in python
# what is type casting  how many types of type casting there? give with examples?
# type casting is a process of converting one data type to another data type.   
# there are 7 types of type casting in python
# 3. Implicit type casting
# 4. Explicit type casting
# 3. User defined type casting
# 4. Dynamic type casting
# 5. Static type casting
# 6. Downcasting
# 7. Upcasting

# float(), int(), str(), bool(), list(), tuple(), set(), dict()

"""num = 5.10
print(int(num))
float(num)
print(num)"""

""" basic data type """

"""#1. Integers
a = 10
print(a)"""

# type() function is used to check the data type of a variable
# type(a)

"""swapping of the two given number """
"""x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y:"))

temp = x 
x = y
y = temp"""


"""# Ecludian distance between two points
print("After swapping the numbers : ", x, y)

x1 = int(input("Enter the value of x1: "))
y1 = int(input("Enter the value of y1: "))
x2 = int(input("Enter the value of x2: ")2
y2 = int(input("Enter the value of y2: "))3
eclu_dist = int(((x2-x1)**4 + (y2-y1)**2)**0.5)

print(eclu_dist)"""



# Just for checking and reviewing the skill
# n = int(input("Enter a Number"))
# c = 0 
# while n>0:
#     n = n//10 
#     c = c+1
    
# print("Number of digits in the given number is: ", c)



# for i in range(5):
#     print("X"*5)
 


# for i in range(6):
#     print(" "*(6-i), end="")
#     print("X"*i)
#     #expalin this code 
#     # print(" "*(6-i), end="")  # this line is used to print the space before the X
#     # print("X"*i) # this line is used to print the X in the given range






# for  i in range(5,0,-1):
#     print(" "*(5-i), end="")
#     print("X"*(2*i-1))
    # what's the logic behind this code 
     # print(" "*(5-i), end="") # this line is used to print the space before the X
     # print("X"*(2*i-1)) # this line is used to print the X in the given range
     # 2*i-1 is used to print the odd number of X in the given range


  # special Data types in python
  # complex numbers
# c = 1+3j
# print(c)
# print(type(c))     


# string 


# print("Hello World"*10, end="/n")
# print("'Machine Learning'")


# my_string = "Hello World"
# for i in my_string:
#     print(i)
# print(my_string[8])

# slicing of the string
# my_string2 = "Hello world Again"
# print(my_string2[0:len(my_string2):3])


# string concatenation

# string1 = "Machine Learning"
# string2 = "is awesome"

# there are two types of objects in python 

# 1. Mutable 
# 2. Immutable

# Immutable Objects:

# 1. int
# 2. float
# 3. string
# 4. bool 
# 5. tuple

# Mutable Objects:
# 1. List 
# 2. set
# 3. Dictionary

# List 
#  It should be included into square Brackets
# It allows duplicate values 
"""m_list = [1,2,3,4,5]
print(m_list)
sum = 0 
for i in m_list:
    square = i**2
    sum += square
print(f"The square of {i} is {square} and the sum of quare is {sum}")
    
my_list1 = ["Name", "Surname","Surname","Verb"]
my_list2 = ["Devesh", "Kumar","Jha","Is"]
print(my_list1)

mapped_dict = {my_list1[i]: my_list2[i] for i in range(len(my_list1))}
print(mapped_dict)"""
    

#  List can have multiple data type

mul_list = ["dev", "has",10,"Name"]

# print(mul_list)
# for i in mul_list:
#      print(i, sep=" ")   # here sep to print in the new line

# Append in a list 
"""mul_list.append("Devesh is a Genius")
print(mul_list)
for i in mul_list:
     print(i,end=" ")    # end prints every value in a sigle line 


print("Length of the list is:", len([1,1,2,2,3,4,5,6]))
"""
# initiating a empty list

# list1 = []

"""print(list1)
list1.append(1)
list1.append(2)
list1.append(3)
list1.append(4)
print(list1)"""

# Deleting any element from a list
# del list1[2]
# print(list1)

# Join two lists 

"""joining_list1 = [1,2,3,4,5]
joining_list2 = [6,7,8,9,10]

joined_list = joining_list1+joining_list2

print(joined_list)
"""

# Tuple 
# They are immutable : You can not change it
# thse allows multiple data type 

"""tuple_1 = (2,3,45,6)
print(tuple_1)
print(type(tuple_1))

# Having multiple data type

tuple_2 = (1,2,3,"I am Learning Mchine Learning","For My project")
print(tuple_2)"""

# Converting a list into a tuple

"""my_list = [10,20,30]
print(my_list)

converted_list = tuple(my_list)
print(converted_list)
print(type(converted_list))
print()"""

# we can not change the elements of a tuple like adding element and deleting
# using length property 

"""my_tuple = ("Hello","Devesh","I am ","Measuring the","Length")
print(len(my_tuple))"""


# Set 
# Are also mutable data type 
# Using {}
# Set does not support indexing

"""
set_1 = {1,2,34,24}
print(set_1)
"""
#print(set_1[1])  # It will provide error

# converting list to a set

"""set_list = [10,30,50,70,10]
x = set(set_list)
print(x)
"""

# Dictionaries 
# It has key value pair 

"""myDictionary = {"name":"Devesh Kumar","Age":23,"Location":"Agra"}
print(myDictionary)
print(myDictionary["Location"])
myDictionary.push("Language")= "Hindi"
print(myDictionary)"""



# Literals 
# literals are data that is given in a variable or constant\
# literals are the values provided to the variables or constants

# Intergare
a = 0b1010
print(a)

# Float 

b = 1.5e10
print(b)

#complex
x = 1+3j
print(x.imag,x.real)

x = 2.6e10
print(x)

# string 

# name = "Devesh Kumar "
# age =  "234"
# char = "D"
# print([name,age,char])

# multistring = """Hello Devesh Kumar Jha. You are really a genius and you can solve any problem """

# unicode  = u"\u00dcnic\u00f6de"
# print(unicode)
# print(multistring)


# booleans
# python treats booleans as number 

# a = True + 1 
# print(a)

#  None
# in python we can not declare variables so we use none as literal for that void variables.

k = None
a = 10 
b = 20 
k = 10
print(a+b,10)

