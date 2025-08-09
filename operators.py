# OPERATORS in Python
"""
1. Airthmatic Operator
2. Assignnent Operator
3. Comparision Opearator (Relational Operator)
4. Logical Opeartor
5. Identity Operator
6. Membership Operator"""


# 1. Airthamatic Opeartors

# These are basic mathematical operations taht we can operate on integers and float 

"""x = 20
y = 30
add = x+y
print(add)
print("sum = ",add)"""

#Difference 
"""diff = x-y
print("Difference is :", diff)"""

# Multiply 
"""mul = x*y
print("Multiplication is :",mul)"""

# Division 
"""div = int(x/y)
print("Division is : ",div)"""

# Exponent 

"""exp = x**2
print(exp)"""

# Modulus Operator   ----->> %
# It provides the reminder 

"""num1 = 40
num2 = 12

modul = num1%num2
print(modul)
print(10%3)"""


# Assignment Operators 
# =, +=, -=, *=, /=

"""a = 5 
print(a)

b = 10
b -= 3

print(b)
c = 10
c *= 5
print(c)

d = 10 
d /= 2

print(int(d))
e = 10
e %= 7
print("Modulus is :",e)"""


# Comparision operators 
# There output will be either true or false


"""a = 20
b = 30
print(a ==b )
print(a !=b )
print(a<b)
print(a<=b)
print(a>=b)
print(a===b)  # it will provide error"""

# Logical Operators
# And, OR , NOT

# a = 10

# print(a>2 and a<11)
# print(a>2 or a<10)
# print(a<2 or a>10)
# and 
# print(2 & 3)
# # or 
# print(2 | 3)
# # not 
# print(not 2)
# # XOR
# print(2 ^ 3)






# Identity Operators 
# is, is Not

"""x = 10
y = 10
print(x is y)
print(x is not y)

z = 15"""


# Membership Operators 
# in, not in
"""
a  = 5 
b =  3

mmyList = [1,2,3,4,5]

print(a in mmyList)
print(b not in mmyList)"""



# In and Not in opeerators


print('D' not in 'delhi')
print('d'  in 'delhi')

# ^^^^^^^^^^ Exercise ^^^^^^^^^^^^

# Program 1 : Find the sum of 3 digit number entered by the user

"""num = int(input("Enter the 3 digit number :"))

a = num%10
# let say number is 123
# 123%10 ---> 3
num = num//10

b = num%10

num = num//10

c = num%10

sum = a+b+c
print(sum)"""













