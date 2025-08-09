# There are two types of errors
# 1. Syntax error : When there is mistake in the programm grammar
# 2. Exceptions : When there is mistake in the program logic / Execution Error 


# IndexError

# L = [1, 2, 3, 4, 5]
# print(L[5])

# TypeError
# The TypeError is thrown when an operation or function is applied to an object of an inappropriate type.
# 1 + 'a'

# ValueError
# The ValueError is thrown when a function's argument is of an inappropriate type.
# int('a')

# NameError
# The NameError is thrown when an object could not be found.
# print(k)

# AttributeError
# L = [1,2,3]
# L.upper()

# Stacktrace


# Why is it important to handle exceptions 
# When we have eror in our code python communicate us using exceptions/error 
# it is also used to secure the codebase

# using try except block 

with open('sample.txt','w') as f:
     f.write('Hi Dev')


# try:
#      with open('sample1.txt','r') as f:
#       print(f.read())
# except:
#      print('File not found, please check the file path or name')

# try:
#      f = open('sample1.txt','r')
#      print(f.read())
# except:
#      print('Some error occured')
     
# catching specific exception
# try:
#   m=5
#   f = open('sample.txt','r')
#   print(f.read())
#   print(m)
#   print(5/2)
#   L = [1,2,3]
#   L[100]
# except FileNotFoundError:     # this is specific exception handling
#   print('file not found')
# except NameError:
#   print('variable not defined')
# except ZeroDivisionError:
#   print("can't divide by 0")
# except Exception as e:            # this is generic exception handling
#   print(e.with_traceback)
  
  
# try:
#      f = open('sample.txt','r')
     
# except FileNotFoundError:
#      print('File not found')
# except Exception:
#      print('There might be some error')
# else:
#      print(f.read())     #when you are super sure that there is no error in the try block, you can use else block
  

# finally
# else
# try:
#   f = open('sample1.txt','r')
# except FileNotFoundError:
#   print('file nai mili')
# except Exception:
#   print('kuch to lafda hai')
# else:
#   print(f.read())
# finally:                       # it will always execute 
#   print('ye to print hoga hi')  
  
  # Finally is very much important because it ensures that the code inside it will always execute,
  # regardless of whether an exception occurred or not.
  # This is particularly useful for cleanup actions, such as closing files or releasing resources.
  
  # raise Exception
# In Python programming, exceptions are raised when errors occur at runtime. 
# We can also manually raise exceptions using the raise keyword.
# We can optionally pass values to the exception to clarify why that exception was raised
  
# class Bank:
#        def __init__(self,balance):
#           self.balance = balance
          
#        def withdraw(self,amount):
#             if amount < 0:
#                  raise Exception("Amount can not be negative")
#             if amount > self.balance:
#                  raise Exception("Bank mein rupees kam hai")
#             self.balance = self.balance - amount

# obj = Bank(10000)
# try:
#      obj.withdraw(500000)
# except Exception as e:
#      print(e)
# else:
#      print(obj.balance)
# finally:
#      print("Transaction Complete Please pull your card")
          
           
           
# Custom Exepition 

# class MyException(Exception):
#   def __init__(self,message):
#     print(message)
    
# class Bank:
#        def __init__(self,balance):
#           self.balance = balance
          
#        def withdraw(self,amount):
#             if amount < 0:
#                  raise MyException("Amount can not be negative")
#             if amount > self.balance:
#                  raise MyException("Bank mein rupees kam hai")
#             self.balance = self.balance - amount

# obj = Bank(10000)
# try:
#      obj.withdraw(500)
# except Exception as e:
#      print(e)
# else:
#      print(obj.balance)
# finally:
#      print("Transaction Complete Please pull your card")
  
  
### Custom Exception Hnadling 
# Custom Exception Handling Example        


class SecurityError(Exception):
  def __init__(self,message):
    print(message)
    
  def logout(self):
    print("Logged Out from all the devices")


class Google:
  def __init__(self,name,email,password,device):
    self.name = name
    self.email = email
    self.password = password
    self.device = device 
    
  def login(self,name,email,password,device):
    if device != self.device:
      raise SecurityError("Anauthorized device")
    if email == self.email and password == self.password:
      print("Login successful")
    else:
      raise("Bhoolaaaa.....")

access = Google('Dev','dev@email.com',12345,'Android')

try:
  access.login('Dev','dev@email.com',12345,'Mac')
except SecurityError as e:
  e.logout()
else:
  print('welcome to google')
finally:
  print("Database updated")


      
    
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  