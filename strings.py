#  String s are collection of characters (in python this is unicode character)
# unicode means 16 bit 

s = "Hello world!"
print(s[-3])

# Slicing 
"""
print(s[0:8:3]) # print the characters using in the negative direction 
print(s[::1]) # print the string 
print(s[::-1])  # reverse the string

print(s[-6:-1])
print(s[-1:-7:-1])"""


# editing and deleting in a string 
# You can not change the string it means that the strings in python are immutable

# deletion using "del"

# del s[-1:-5:2]    because deletion means the change in string but not allowed
# print(s)

# Operators in string 
"""1. Airthmatic operator
2. Relational operator
3. logical operator
4. loops on String 
5. Membership operator"""

# print("Hello" + " How are you ")
# print("*"*10)

# print("Delhi"=="delhi")

"lmumbai" > "pune"  # --> false because it use lexiographically

# Logical operator 

"hello " and "World"   # --> "World" true for "Filled string " and false for " "

# Lopps in string  also membership 

# for i in "Hello":
#      print(i)

# for i in "Delhi":
#      print("Agra")


# String functions 
# Common Function works on every data type 
# len 
# max
# min 
# sorted

"""str = "Hello Python"
print(len(str))
print(max(str))  # max value character on the basis of ASCII 
print(min(str))
print(sorted(str)) # in ascending order of ASCII list
"""

# Capitalize/ Title/ Upper / Lower /Swapcase
"""str = "Hello Python"
print(str.capitalize()) # First word capital
print(str.title())  # The first character of world will capitalize
print(str.upper())
print(str.lower())
print(str.swapcase()) # Just apposite to uppercase """


# Count/ Find /Index

"""str = "My name is Devesh Kumar"

print(str.count("D")) # count the character 
print(str.index("D"))  
print(str.find("D"))  # Index and find are same but it does not throw error but index """

# endswith/startwith

# name = "Devesh Kumar"

# print(name.startswith("D"))

# fromate 

# name = "Devesh Kumar"
# gender = "Male"
# print('Hi I am {} and I am {}'.format(name,gender))

# isalnum/ isalpha /isdigit/ isidentifier


# split/ Join  
# split convert your string in a list word by word
# Join helps in joining the two strings 


"""intro = "Hello I am Devesh Kumar Jha"

store = intro.split()
print(store)
print(intro.split("Devesh"))

# join 

print(" ".join(store))
print("-".join(store))
print("_".join(store))

# output
# Hello I am Devesh Kumar Jha
# Hello-I-am-Devesh-Kumar-Jha
# Hello_I_am_Devesh_Kumar_Jha"""


# Replace 

# intro = "Hi am Devesh Kumar"
# print(intro.replace("Devesh","Devendra"))

# Strip 

intro = "    Devesh is a Developer and             "
print(intro.strip())

# Check for the pallidrome string 

# s = input("Enter the string you want to check: ")

# flag = True 

# for i in range(0,len(s)//2):
#      if s[i] != s[len(s)-i-1]:
#           flag = False
#           print("Not Pallidrome!")
#           break
# if flag:
#      print('Pallidrome')

#  Countin the word
# count = 0      
# for i in s:
#      count +=1
# print(count)


#  Write a programm to convert all the word title without using title 

# str = input("Enter the string: ")
# L = []
# for i in str.split():
#     L.append(i[0].upper() + i[1:].lower())

# print(" ".join(L))


#  Convert a number into a string without using type conversion








