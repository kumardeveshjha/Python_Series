def isEven(num):
     """
     This function returns if  a given number is even or not 
     input ; any valid integer 
     output : even number 
     
     """
     if num%2 ==0:
          return "Even"
     else: 
          return "Not even"
 
for i in range(1,11):
     x = isEven(i)
     print(x)

# As a senior programmar you are responsible for the all functions error
# When you making a function it is knowns as parameters 
# When we call the function is known as argument 

# Types of argument 

# 1. default arguments 

# Providing the default value to a parameters 
# it will help in managing errors 

# def power(a=1,b=1):
#      print(a**b)
# power(2)
# power(2,2)

# 2. Positional Argument 
# Focus on order when providing the arguments to parameters 

# 3. Keyword Argument 
# Keyword arguments supercede the positional arguments 
# Whenever we have lots of parameters we use keyword arguments

# power(b=2,a=3)  # output : 9


# "*arg" and "**kwargs"

# *arg is used when we don't know trhat how much arguments will be provided by the user

"""def add(*arg):
     total = 0
     
     for i in arg:
          total = total + i
     return total

print(add(1,2,3,4,5,56))"""


# "*kwargs" is used when we provide key - values pair

def display(**kwargs):
     
     for (key,value) in kwargs.items():
          print(f"{key}:{value}")
          
display(Bharat = "Delhi",Pakistan='Islamabad',Srilanka='Colombo')


"""
      Order of the arguments matter (normal -> *args -> **kwargs)
"""

# How functions executes in memory  

# What is difference between return and print in function 
# If you didn't use return keyword then it will by default return a 'none


l = [1,2,3]

print(l.append(4))  # it will return none

# Variable scope in python function 

 # Local Variable 
 # Global Variable 
 
 

# 1. When we want to access value form global variables 
 
# def g(y):
#       print(x)
#       print(x+1)
  
# x = 5 
# g(x)
# print(g(x))
# print(x)   

# 2. When we have both variables global and local with same name then they don't have any relation 
# They are independent 


# def g(y):
#       x =1 
#       x += 1
#       print(x)

# x = 5
# g(x)
# print(x) 

# 3. When we are accessing the global variable in the function 
# We can not change the global variable 
# we may have 'global' variable 

"""def h(y):
     x += 1
x = 5 
h(x)
print(x)"""


# def f(x):
#      x = x+1
#      print(' in f(x): x =',x)
#      return x

# x = 3
# z = f(x)
# print('in main program scope: z =', z)
# print('in main program scope: x =', x)


# Nested function 

# def f():
#      def g():
#           print('Inside function g')
#           f()
#      g()
#      print('inside function f')

# f()

# Mamximum recursion depth exceeded


# def g(x):
#      def h():
#           x ='abc'
#      x = x + 1
#      print(' in g(x): x =',x)
#      h()
#      return x

# x = 3
# z = g(x)


# def fun(x):
#      def g(x):
#           x = x + 1
#           print('in g(x): x = ',x)
#      x = x+1
#      print('in h(x): x = ',x)
#      g(x)
#      return x

# x =3 
# z = fun(x)


# In python functions are also called as first class citizen 
# function in python act as datatype 
def square(y):
     return y**2
# print(type(square))
# print(id(square))

# reassign 

x = square
print(x(3)) 

# deleting as function 

# del square
# print(square(2))
 
# storing a function 

l = [1,2,3,4,square]
print(l[-1](2))
 
 
#  returning a function 

def f():
     def x(a,b):
          return a+b
     return x
val = f()(3,4)
print(val)
          
          
def fun1():
     print('inside function 1')

def fun2(a):
     print('inside function2')
     return a()

fun2(fun1)

# Benefits of using a function 

# code Modularity 
# code readibility
# code reusability 


# Lambda Function 
# A lambda function is a small anonymous function 
# A Lambda function can take any number of arguments, but can only have one expression


a = lambda x: x**2

print(a(2))

a = lambda x,y: x+y
print(a(1,2))
 
#Diffrence between lambda and general function 
# No Name 
# Lambda has no return value 
# It is written in a single line 

# These are used with Higher order function 


# check_word = lambda str: 'a' in str 
 
# print(check_word("hELLP"))
 
a = lambda x: 'even' if x%2 ==0 else 'odd'
print(a(3))
 
 
# Higher Order Function 
# If a function returns Function
# If a function takes function as argument 


# def square(x):
#      return x**2

# def transform(f,L):
#      output = []
#      for i in L:
#           output.append(f(i))
#      print(output)

# L = [1,2,3,4,5]

# transform(square,L)
# Here we can use lambda function 

# transform(lambda x:x**2,L)

# ***Map
# 1. lmabda function and list 
# We can easily iterate on a list 

mappedList = list(map(lambda x:x**2,[1,2,3,4,5]))

print(mappedList) 

type_Number =  list(map(lambda x: 'even' if x%2== 0 else 'odd',[1,2,3,4,5]))
print(type_Number)


users = [
     {
          'name':"Devesh Kumar",
          'age': 24,
          'Profession': ['Entrepreneur','VC','Founder']
     },
     {
          'name':"Devendra Kumar",
          'age': 25,
          'Profession': ['Artist','Developer','Environmentlist']
     },
     {
          'name':"Neelam ",
          'age': 20,
          'Profession':['Data Scientist','Manager'] 
     },
     
]


userDetails = list(map(lambda x:x['name'],users))
print(userDetails)

# Filter 
# It requires two things 1. lambda function List 
# It only returns those values which are true but map logic applies to all elements 

L= [100,200,300,400,700,555,750]

filteredNumbers = list(filter(lambda num: num>500,L))
print(filteredNumbers)


# Fetch fruits starting with with 'a'

fruits  = ['apple','guava','cherry']
desiredFruits = list(filter(lambda fruit: fruit.startswith('a') ,fruits))
print(desiredFruits)

# Reduce 

# It is not default function 

import functools 

print(functools.reduce(lambda x,y:x+y,[1,2,3,4,5]))

print(functools.reduce(lambda x,y:x if x<y else y,[23,11,45,10,1]))

 




