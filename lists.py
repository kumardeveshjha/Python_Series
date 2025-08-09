# Arrays vs lists
# arrays are fixed in size
# List act like dynamic arrays 
# Arrays are homogenous You can only store single type data
# Speed of execution more and more memory 
# Lists are referential arrays 

# Lists are ordered
# Are changeble
# Mutable 
# Hetrogeneous 
# Nested 
# Items can be extracted



# Create a list 

# empty list 
# print([])

# 1-D list 
# l1 = [1,2,4,5,6]
# 2 -D list 
# l2 = [1,23,[2,3,4.5]]
# print(l2)

# 3 -D Lists 
# l3 = [1,[2,3,[4,5,6]]]
# print(l3)


# Accessing the items from list 

# accessList = [1,2,3,4,5]
# print(accessList[1:3])
# print(accessList[-4:])

# print(l3[1][2][0])

"""Adding Items to a list """
# Append 
# Extend
# Insert

# Append: When add a single item in the list 

# L = [1,2,3,4,5,6]
# L.append(True)
# print(L)

# Extend : When we want to add multiple items in the list 

# L.extend([7,8,9,10])
# print(L)

# L.append([11,22,33])
# print(L)

# L.extend("DEvesh")
# print(L)

# Insert : When I want to add item in the desired location in list 

# L.insert(2,200)
# print(L)
# L.insert(2,"Delhi")
# print(L)

"""Editing Items in List """

# L = [1,2,3,4,5,6]

# L[0] = 200
# L[-1:] = [200,300,400,500,600]
# print(L)

#del 

# del L
# del L[1]
# print(L)

#remove
# L.remove(6)
# L.remove(5)
# L.remove(3)
# print(L)

# pop : Bydefault delets the last item
# clear : Clear the list but don't delete the list 


"""Operations on Lists"""
# Arithmatic
# Membership 
# Loop

# Arithmatic Operator(+,*)

L1 = [1,2,3,4,5]
L2 = [5,6,7,[8,9]]
L3 = [[[1,2],[3,4]]]
# print(L1+ L2)
# print(L1*5)

#Membership operator  (in, not in )
# print(3 in L1)
# print(3 in L2)
# mulList = [[1,2,3],[4,5,6]]
# print(1 in mulList)

# loops 

# for i in L1:
#      print(i**2)
# for i in L2:
#      print(i)
# for i in L3:
#      print(i[0])


"""list functions"""

# Len/min/max/sorted ---> only for homogenous list
# L = [15,25,35,4,15]

# print(len(L1))
# print(min(L1))
# print(max(L1))
# print(sorted(L1,reverse=True))

# print(L.count(15))

# print(L.index(15))

# Reverse : Permanent Reverse the list 
# Sort : Permanent but sorted not permanent 

# Copy 

# 
# L = [1,2,34]
# print(L)
# print(id(L))
# L1 = L.copy()
# print(L1)
# print(id(L1))



"""  List Comprehension   """

# It provides a concise way of creating lists 
# More time- efficient and space efficient 
# Transforms iterative statement into a formula 

# Add 1 to 10 numbers in a list 

# Old method 
# L = []

# for i in range(1,11):
#      L.append(i)
# print(L)

# L = [i for i in range(1,11)]
# print(L)


# Vector multiplication 
# v = [2,3,4]
# s = -3
# x = []
# for  i in v:
#      x.append(i*s)
# print(x)

# mul_Vector = [s*i for i in v ]
# print(mul_Vector)


# Print all the number which are divisible by 5 from 1 to 50 

# div = [i for i in range(1,51) if i%5==0]

# languages = ["Python", "Java", "JavaScript","Kotlin","Papaya"]

# # Find the language starting with "P"

# desired = [lang for lang in languages if lang.startswith('P')]

# print(desired)

# fal1 = ["Apple", "Banana","Kiwi","Amrood"]
# fal2 = ["Apple", "Sev","Khumani","Aam"]

# desiredFruit = [fruit for fruit in fal2 if fruit in fal1 if fruit.startswith('A')]
# print(desiredFruit)


# Print a 3x3 matrix using list comprehension ----> Nested List Comprehension 

# print([[i*j for i in range(1,4)] for j in range(1,4)])

# Cartesian Product Using List comprehension 

# c1 = [1,2,3]
# c2 = [4,5,6]
# cartesianProduct = [(i,j) for i in c1 for j in c2]
# print(cartesianProduct)

# l = []
# for i in c1:
#      for j in c2:
#           l.append((i,j))
# print(l)

# List iterations 

# 1. ItemWise
 
# l = ["Devesh ", "Devendra", "Neelam","Abhi"]

# for i in l:
#      print(i)

# # 2. Indexwise

# for i in range(0,len(l)):
#      print(l[i])


# zip() function

Z1 = [1,2,3,4,5]
Z2 = [-1,-2,-3,-4,-5]

print(list(zip(L1,L2)))

#  We can store any object in list


# disadvantage of python lists

# 1. slow
# 2. riskey usage --> because lists are mutable 
# 3. eats up more memory
































