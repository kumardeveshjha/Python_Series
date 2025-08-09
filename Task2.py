# Problem 1: Write a program that will give you in hand monthly salary after deduction on CTC - HRA(10%), DA(5%), PF(3%) and taxes deduction as below:
# Salary(Lakhs) : Tax(%)

# Below 5 : 0%
# 5-10 : 10%
# 10-20 : 20%
# aboove 20 : 30%

# CTC =int(input('Enter the in-hand Salary(in LPA): '))
# salary = 0
# if CTC <=500000:     # deduction = ctc - ctc*(10+5+3)%  ==> ctc(1-0.18)
#      salary == CTC*82

# elif 5< CTC <= 1000000:    #deduction = ctc - ctc*(10+5+3+10)%  ==> ctc(1-0.28)  
#      salary = float(CTC*0.72)
     
# elif 10 < CTC <=2000000:     #deduction = ctc - ctc*(10+5+3+20)%  ==> ctc(1-0.38) 
#      salary = float(CTC*0.62)
     
# else:                     #deduction = ctc - ctc*(10+5+3+30)%  ==> ctc(1-0.28) 
#      salary = float(CTC*0.52)  
        

# print('In hand salry after deduction is: ',round(salary/12,2))

"""Problem 2: Write a program that take a user input of three angles and will find out whether it can form a triangle or not.
Hint - Sum of all angles is 180 and all angles are positive"""

# a = int(input("Enter the first angle: "))
# b = int(input("Enter the first angle: "))
# c = int(input("Enter the first angle: "))

# if a+b+c == 180 and a>0 and b>0 and c>0:
#      print("This is a triagle")
# else:
#      print("This is not a triangle")

     
     
"""Problem 3: Write a program that will take user input of cost price and selling price and determines whether its a loss or a profit."""

# CP = int(input("Enter the cost Price: "))
# SP = int(input("Enter the selling Price: "))
# if SP > CP:
#      print("Profit of:", SP - CP)
# elif SP < CP:
#      print("Loss of:", CP - SP)
# else:
#      print("No Profit No Loss")


"""Problem 4: Write a menu-driven program -
3.cm to ft
1.km to miles
2.USD to INR
exit
Hint

1 cm = 0.032ft
1km = 0.62
1 USD = 80 INR"""

# option = int(input("""
#                    Hello, Select the option for the functionality
#                    1. CM to ft
#                    2. KM to Miles
#                    3. USD to INR
#                    """))


# if option == 1:
#      cm = int(input("Enter the cm value"))
#      print("The converted value is: ",0.032*cm)
# elif option == 2:
#      KM = int(input("Enter the KM value: "))
#      print('The converted value of KM',0.62*KM)
# else:
#      USD = int(input('Enter the USD value: '))
#      print('Coverte value of USD: ',86*USD)

"""Problem 5 - Exercise 12: Display Fibonacci series up to 10 terms.
Note: The Fibonacci Sequence is a series of numbers.
The next number is found by adding up the two numbers before it. 
The first two numbers are 0 and 1. 
For example, 0, 1, 1, 2, 3, 5, 8, 13, 21. The next number in this series above is 13+21 = 34"""

# n = int(input("Enter the number of turns: "))

# fibonacci = 0
# for i in range(1,n):
#      print(fibonacci)
#      fibonacci = fibonacci + i 
#      print(fibonacci,end=",")
     
     


"""Problem 6 - Find the factorial of a given number.
Write a program to use the loop to find the factorial of a given number.

The factorial (symbol: !) means to multiply all whole numbers from the chosen number down to 1.

For example: calculate the factorial of 5"""
     
# n = int(input("Enter the number for factorial: "))

# fact =1
# if n>0:
#      for i in range(1,n+1):
#           fact = fact*i
# else: 
#      print("Factorial is: 1")
# print(fact)
          
"""Reverse a given integer number.
Example:
Input:76542
Output:24567
"""

# n = int(input("Enter the number to be reversed: "))

# rev = 0

# while n>0:
#      last = n%10
#      rev = rev*10 + last 
#      n = n//10
# print(rev)

# for i in range(len(n)):
#      last = n%10
#      rev = rev*10 + last
#      n = n//10
# print(rev)


"""
Problem 8: Take a user input as integer N. 
   Find out the sum from 1 to N. If any number if divisible by 5, then skip that number. 
   And if the sum is greater than 300, don't need to calculate the sum further more. 
   Print the final result. And don't use for loop to solve this problem.
Example 1:
Input:30
Output:276
"""

# n = int(input('Enter the number: '))
# sum = 0 
# for i in range(1, n + 1):
#      if i % 5 == 0:
#           continue
#      sum += i
#      if sum > 300:
#           sum -= i
#           break

     
# print(sum)

"""Problem 9: Write a program that keeps on accepting a number from the user until the user enters Zero.
Display the sum and average of all the numbers.
"""

# sum = 0
# count = 0
# while True:
#      n = int(input('Enter the number: '))
#      print('The number is:',n)
#      if n==0:
#           break 
#      sum = sum + n
     
#      count += 1
# print('The sum is',sum)
# print('The average is',sum/count)
     

"""
   Problem 9: Write a program which will find all such numbers which are:
   divisible by 7 but are not a multiple of 5,between 2000 and 3200 (both included). 
   The numbers obtained should be printed in a comma-separated sequence on a single line.
"""

# for i in range(1200,3201):
#      if i%7 == 0 and i%5 !=0:
#           print(i,end=",")

# L = []
# for i in range(2000,3201):
#      if i%7 ==0 and i%5 != 0:
#           L.append(i)
# print(L)

"""
     Problem 10: Write a program, which will find all such numbers between 1000 and 3000 (both included) 
     such that each digit of the number is an even number.
     The numbers obtained should be printed in a space-separated sequence on a single line.
"""

# L= []

# for i in range(100,3001):
#      if i%2 ==0:
#           L.append(str(i))
# print(','.join(L))

"""
Problem 11: A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps.
The trace of robot movement is shown as the following:

UP 5
DOWN 3
LEFT 3
RIGHT 2
!
The numbers after the direction are steps.

! means robot stop there.

Please write a program to compute the distance from current position after a sequence of movement and original point.
If the distance is a float, then just print the nearest integer.
Example:
Input:
UP 5
DOWN 3
LEFT 3
RIGHT 2
!
Output:2
     """
     
     

# pos = [0,0]
# while True:
#        move = input('Enter the steps and move: ')
#        direction = move.split()[0]
#        steps = int(move.split()[1])
#        if direction == '!':
#             break
#        if direction == 'UP':
#             pos[1] +=steps
#        elif direction == 'DOWN':
#            pos[1] -= steps
#        elif direction == 'RIGHT':
#            pos[0] += steps
#        elif direction == 'LEFT':
#            pos[0] -= steps
#        else:
#           pass
       
# print('The position and distance from the original point is:',pos,int((pos[0]**2 + pos[1]**2)**0.5))
    


# n = int()

     


"""Problem 12:Write a program to print whether a given number is a prime number or not
"""

n = int(input("Enter the number: "))

flag = True
for i in range(2,n):
   if n%i == 0:
      flag = False
      break
   if flag == True:
      print("Prime Number")
   else:
      print("Not Prime")
      

"""Problem 13:Print all the Armstrong numbers in a given range.
Range will be provided by the user
Armstrong number is a number that is equal to the sum of cubes of its digits. For example 0, 1, 153, 370, 371 and 407 are the Armstrong numbers.
"""

"""Problem 14:Calculate the angle between the hour hand and minute hand.
Note: There can be two angles between hands; we need to print a minimum of two. Also, we need to print the floor of the final result angle. For example, if the final angle is 10.61, we need to print 10.

Input:
H = 9 , M = 0
Output:
90
Explanation:
The minimum angle between hour and minute hand when the time is 9 is 90 degress.
   """



     



