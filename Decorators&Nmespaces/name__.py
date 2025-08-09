# It is the pythons core phylosophy 

# LEGB (L-> E-> G-> B)

#Local and Global 

# Global 
# a = 2 

# def temp():
#      #Local Scope
#      b = 3
#      print(a)
     
# temp()
# print(a)

# example 

# a = 2 

# def temp():
#      #Local Scope
#      a = 3
#      b = 3
#      print(a)
     
# temp()
# print(a)

# You can only read the global variable not write it or change its value in the local space 
# a = 2

# def temp():
#   # local var
#   a += 1
#   print(a)

# temp()
# print(a)


# But python gives you flexibility using global keyword
# But you should not do it because it is not 
# a = 2

# def temp():
#   # local var
#   global a
#   a += 1
#   print(a)

# temp()
# print(a)

# local and global -> global created inside local
# def temp():
#   # local var
#   global a
#   a = 1
#   print(a)

# temp()
# print(a)


# local and global -> function parameter is local
# def temp(z):
#   # local var
#   print(z)

# a = 5
# temp(5)
# print(a)
# print(z)

# Built-in Scope 

# import builtins

# print(dir(builtins))

# Enclosing scope
# def outer():

#   def inner():
#        print(a)
#   inner()
#   print('outer function')


# outer()
# print('main program')
     
     
# nonlocal keyword
# def outer():
#   a = 1
#   def inner():
#     nonlocal a
#     a += 1
#     print('inner',a)
#   inner()
#   print('outer',a)


# outer()
# print('main program')
           

