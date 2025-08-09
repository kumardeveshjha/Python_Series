# Decorators 
# @staticmethod, @classmethod, @abstractmethod and @property are decorators 
# that are used to modify the behavior of methods in classes.

# def func():
#      print("Hello")
     
# a  = func
# a()

# Python are 1st class function

# def modify(func,num):
#   return func(num)

# def square(num):
#   return num**2

# modify(square,2)

# simple example

# def my_decorator(func):
#   def wrapper():
#     print('***********************')
#     func()
#     print('***********************')
#   return wrapper

# def hello():
#   print('hello')

# def display():
#   print('hello devesh')


# b = my_decorator(display)
# b()


# Shortcut method to use decorator 


def my_decorator(func):
  def wrapper():
    print('***********************')
    func()
    print('***********************')
  return wrapper

@my_decorator
def hello():
  print('hello')

hello()

# anything meaningful?

import time

def timer(func):
  def wrapper(*args):  
     # here we are using *args to allow any number of arguments
     # This will allow the function to accept any number of arguments
     # in this we can not get values unless we provide *args in the wrapper
    start = time.time()
    func(*args)
    print('time taken by',func.__name__,time.time()-start,'secs')
  return wrapper

@timer
def hello():
  print('hello wolrd')
  time.sleep(2)

@timer
def square(num):
  time.sleep(1)
  print(num**2)

@timer
def power(a,b):
  print(a**b)

hello()
square(2)
power(2,3)


