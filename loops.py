# loops


# while Loop
"""a = int(input("Enter a number: "))

i = 1 
while i<11:
   
     print(f"{a}*{i} = {a*i}")
     i += 1"""

# else with while loop

"""x = 1
while x<5:
     print(x)
     x += 1
else:
     print("Out of the loop")"""


# Randim integer from 1 to hundred

"""import random 
jackpot = random.randint(1,100)
guess= int(input("Enter your gues: "))"""


"""if guess<jackpot:
     print("Jackpot is greater than guess")
else: 
     print("The guessed number is less than jackpot")"""
"""counter = 1 
while guess != jackpot:
     if guess<jackpot:
          print("Jackpot is greater than guess")
     else:
          print("Jackpot is less than guess")
     
     guess = int(input("Enter your guess: "))

     counter += 1

else: 
     print("You have guessed the jackpot number")
     print(f"Number of attempts: {counter}")"""
     

# for loop

# for i in range(1,11,3):   # range(initiate,limit,skip or jump)
#      print(i)


# For loop with else

"""current_population = 10000

for i in range(10,0,-1):
     print(f"Population in the year {i} is {int(current_population)}")
     current_population = current_population /1.1
     print("Population is ",int(current_population))


print("Population is ",current_population) """ 

"""for i in range(1,11):
     print(f"Population in the year {i} is {int(current_population)}")
     current_population -= current_population/1.1

print("Population is ",current_population) """   


# Sequence sum 
# 1 + 1/2! + 1/3! + 1/4! + 1/5! + 1/6! + 1/7! + 1/8! + 1/9! + 1/10! code for this series
"""import math
n = int(input("Enter the number: "))
sum = 0
for i in range(1,n+1):
     sum += i/(math.factorial(i))
     
print(sum)"""

# Nested Loops

# for i in range(1,6):
#      for j in range(1,i+1):
#           print("*",end=" ")
#      print(" "*i,end="\n")
     # 
# row = int(input("Enter number of rows: "))

# for i in range(1,row+1):
#      for j in range(1,i+1):
#           print("*",end=" ")
#      print()


# for i in range(1,row+1):
#      for j in range(1,i+1):
#           print(j,end=" ")
#      print()

# for  i in range(1,row+1):
#      for j in range(1,i+1):
#           print(j, end=" ")
#      for k in range(i-1,0,-1):
#           print(k,end=" ")
#      print()

# output of the above code 
# 1
# 12
# 123
# 12321
# 1234321
           

# Loop Control  
# Break 
# continue
# pass

# 1. Break 
for i in range(1,5):
     if i == 3:
          break
     print(i)

# Example : Find the prime number from a given data range 

"""lower = int(input("Enter lower range: "))
upper = int(input("Enter the upper range: "))


for i in range(lower,upper+1):
     for j in range(2,i):
          if i%j == 0:
               break
     else:
          print(i)"""

# 2. Continue 

# for i in range(1,10):
#      if i ==5 :
#           continue
#      print(i)

# 3 Pass To avoid error 

for  i in range(1,10):
     pass







     

     
          