# Tuples 

# Tuples is immutable 
# Both list and tuples have same functionality except mutability


# list = [1,1,2,3]
# print(list)

# tuple1 = (1,2,34)

# print(tuple1)


# creating a tuple 
# single item tuple can not make 
# t1 = (1)
# print(type("St"))

#Tuples are "Hetrogenous "

# t2 = (1,2,3,"Bolo","Jai","Mata","Di",2.5,True,[1,2,3])
# print(t2)


# Using type conversion 
t3 = tuple("Devesh") 
print(t3)


# Accessing Items 

# Indexing 
# slicing


# Indexing 
print(t3[-1])
print(t3[::-1])   # Reversing the string 

# Slicing 

print()

print(t3[0:4:2])


# Editing the tuple item 

tup = (1,2,3,4,5)

# tuple editing is not possible because it is immutable 

# tup[0] = 100

# print(tup)


# Deleting item 

# You can not delete an item but can delete whole tuple 

# del tup
# print(tup)

# Operations and functions in tuple 

# t1 = (1,2,3,4)
# t2 = (5,6,7,8)

# print(t1+t2)
# print(t1*2)

#Membership 

# print(1 in t1)
# print(7 not in t1)

# Tple function 
# sorted always returns a list of sorted elements 

# Read only functionality is provided by tuple 


# Tuple unpacking 

# a,b,c = (1,2,3)

# print(a,b,c)


# a,b,*others = (1,2,3,4,5,6)

# print(a,b)
# print(others)

#Zipping of Tuples 

# z1 = (1,2,3,4)
# z2 = (5,5,7,8)

# print(list(zip(z1,z2)))


# tuple comprehension 

# print([i*j for i in z1 for j in z2])


"""#Set """

# Set is unordered dataset 
# it is used to do mathematical set operations like uinon, intersection, symmetric difference
# Unordered 
# Mutable 
# No dupllicate 
# Can't contain mutable data types 


# creating a set 

# set1 = {}
# print(type(set1))

# s1 = set(set1)
# print(type(s1))

# s2 = {1,2,3,4,5}

# print(s2)

# s3 = {1,2,3,(2,3,4),"Devesh"}
# print(s3)

#Set does not allow duplicate values
# s4 = {1,1,2,2,3,3}
# print(s4)

# type conversion 

# s5 = set([1,2,3,4])
# print(s5)


# Accessing the element 

# s6 = {1,2,3,4}
# s6[0]

# Set items can not acceessed by indexing 

# Items can not be edited because it does not allows indexing 

# Adding Items 
# Add function can only add one item in the set 

# s6.add(5)
# print(s6)

# updating items in set 
# We can add multiple items in a set using update function 

# s6.update([6,7,8,9])

# print(s6)

# Deleting item in set 

s7  = {1,2,3,4,5}

# using delete 
# Delete can only delete the whole set but not the items 

# del s7
# print(s7)

# using discard 
# discard can delete any item 
# s7.discard(5)
# print(s7)

# remove 
# remove can delete any single element but if the item is not available it throws error 
# it helps in error handleing 
s7.remove(4)

print(s7)

# POP function 
# pop delets any item randomnly


# clear can clear the set or empty the set 



# Set operations 

# s1 = {1,2,3,4,5,6}
# s2 = {6,7,8,9,10}

# uinion 

# print(s1|s2)

# intersection 

# print(s1 & s2)

# Difference 

# print(s1-s2)

# print(s2-s1)

# Symmetric Difference 

# print(s1^s2)


# membership operation 

# print(1 in s1)

# for i in s1:
#      print(i)

# Set functions 
# len/ sum/min/max/sorted 

# s = {1,2,3,4,5,6,7}

# print(len(s))
# print(sum(s))
# print(max(s))
# print(min(s))



# union/ Update 


s1 = {10,20,30,40}
s2 = {100,200,300,400}

# s3 = s1.union(s2)
# s4 = s1.update(s2)
# print(s3)

# intersection / intersection_update

# Differencfe/difference_update

#Symmetric_difference / symmetric_diffrence_update
#isadjoint/ issubset/issupport

# print(s1.isdisjoint(s2))
# print(s1.issubset(s2))
# print(s1.issuperset(s2))

# Copy 

# s3 = s1.copy()
# print(s3)


# frozzenSet 
# frozenset is a immutable version of python set 

frozen1 = frozenset([1,2,3,4])
frozen2= frozenset([10,20,30])

print(frozen1|frozen2)

# frozen set is only used for read operations but not write operations 


# Dictonary in python 
# Dictonary in python is a collection of keys values, used to store data values like a map, which
# unilke other data types which hold only a single values as an elements 
#  Inother languages it is known as map associative arrays 

# Mutable 
# Indexing has no meaning
# Keys can't be duplicated 
# keys can't be mutable items 



# Create dictionaries 

d = {}  # 1-d dictionary

d1 = {'Name':'Devesh Kumar','age': 24, 'location':'agra'}

print(d1)


"""d2 = {
     'name': 'Devendra Kumar',
     'age':24,
     'college':'GL Bajaj',
'result':{
     'math':'Pass',
     'DSA':'Pass',
     'Communication':'Pass'
}
}

print(d2['result'])"""

# using dict keyword

d3 = dict(((1,1),(2,2),(3,3),(4,4)))
print(d3)

d4 = {'name':'Devesh','profesion':'entrepreneur'}

# List is not allowed as key

# d5 = {'name':'Devesh',(1,2,3):'1'}
# print(d5)

# d6 = {[1,2,3]:'2','name':'Devendra'}

# List or mutable data tpe can not be used as a key 
# print(d6)


# Accessing item from a dictionary
# WE can not use indexing
# using the keys to get the values from dict 


# print(d4["age"])

# adding key value pair in  a dictonary

# d4['education'] = "Bachelaors"

# print(d4)

# d4['education'] = 'Masters in every possible way'
# print(d4)

# deleting a key 

# del d4["profesion"]
# Here we have deleted the profession key from the d4 dictionary data 
# print(d4)


# Dictonary operations 
# Membership
# iterations 

user = {
     'name':'Devesh Kumar',
     'age':24,
     'profession':'Enrepreneur',
     'Expertize':['Fintech','Healthtech','AI']
}

print('name' in user)

# li = []
# for i in user:
     # print(f"{i}:{user[i]}")
     # li.append(i,user[i])
# print(li)


# Dictionary Function 

# len/ print / sort 

# print(len(user))
# print(sorted(user))  # it soreted the the 

#  Items/ keys /values

# print(user.items())
# print(user.keys())
# print(user.values())



# Dictionary comprehension 

# {key: value for vars in iterable}

# square = {i:i**2 for i in range(1,10)} 
# print(square)

distances = {"delhi":200,'mumbai':800,'hyderabad':1200}

# first aproach of solving the problem 
miles_distance = {key:value*0.62 for (key,value) in distances.items()}
print(miles_distance)

# Second Approach of solving the problem 
second_distance = {key:distances[f"{key}"]*0.62 for key in distances}
print(second_distance)


# Using zip 

"""days = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday']

temp = [72,50,34,46,49,50,35]

temp_data = {i:j for i in days for j in temp}

print(temp_data)

# using zip 

zipped_data  = {i:j for (i,j) in zip(days,temp)}
print(zipped_data)"""


# Using conditions 

product = {'phone':10,'laptop':0,'charger':15,'tablet':0}

display_products = {i:product[i] for i in product if product[i]>0 }
print(display_products)

# Nested comprehension 

# print the tables of number form 2 to 4

tables = {i:{j:i*j for j in range(1,11)} for i in range(2,5)}
print(tables)













