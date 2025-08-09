# Why we need generator

# # using Loop
# L = [x for x in range(10000)]

# # for i in L:
# #      print(i**2)

# # now using iterator

# import sys
# print(sys.getsizeof(L))

# x = range(10000)

# print(sys.getsizeof(x))
# for i in x:
#      print(i**2)


# Python Generator 

# def gen_demo():
     
#      yield 'FIRST Statement'
#      yield 'Second Statement'
#      yield 'ThirdStatement'
     
# gen = gen_demo()
# #printing the statement using next function 
# print(next(gen))


# def square(num):
#      for i in range(1,num):
#           yield i**2
  
# gen_square = square(10)        
# print(next(gen_square))
# print(next(gen_square))
# print(next(gen_square))
# print(next(gen_square))
# print(next(gen_square))

# for i in gen_square:
#      print(i)


#Range Function 

# def mera_range(start,end):
     
#      for i in range(start,end):
#           yield i
# rang = mera_range(15,30)
# for i in rang:
#      print(i)

# # List Comprehension 

# L = [i**2 for i in range(1,101)]

# for i in L:
#      print(i)
     
# without using a function and list comprehension 

# gen = (i**2 for i in range(1,101))
# for i in gen:
#      print(i)

## Important for deep learning 
# It is used in Deep learning to train and store the data 