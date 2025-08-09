# Depending on the users input we have many branching 
# Branching means we ahve many options 
# to handle the we need to use if else statement

# Login program and indentation 

# email--> dev123@gmail.com
# password --> 1234

"""email = input("Enter the email ID: ")
password = input("Enter the password: ")"""

"""if email == 'dev123@gmail.com' and password == '1234':
    print("Login successful")
else :
    print("The user is not registerec.")"""

# using elif statement 

"""if email == 'dev123@gmail.com' and password == '1234':
    print("Login successful")
elif email == 'dev123@gmail.com' and password != '1234':
    print('Incorrect password')
    password = input("Enter password again:")
    if password == '1234':
        print('Welcome to the home page')
    else:
        print("Please try again") 
else: 
    print("Please enter the correct credentials.")"""

    
# Min of three numbers 

"""a = int(input("Enter the first number :"))
b = int(input("Enter the second number:"))
c = int(input("Enter the third number:"))"""

"""if a<b and a<c :
    print(f"{a} is the smallest number.")
elif b<c:
    print(f"{b} is the smallest number")
else : 
    print(f"{c} is the smallest number")"""



# for the greatest number
"""if a+b<=c and a>0 and b>0 and c>0 :
     print(f"{c} is the greatest number")
elif a+c<=b : 
     print(f"{b} is the greatest number")
else:
     print(f"{a} is the greatest number")"""

# menu driven calculator 

"""fnum = int(input("Enter the first number: "))
snum = int(input("Enter the second number: "))

op = input('Enter the operation: ')

if op == '+':
     print("Sum is:",fnum+snum)
elif op == '-':
     print("Substraction is: ",fnum+snum)
elif op == '*':
     print("Multiply is: ",fnum*snum)
elif op == '/':
     if snum == 0:
          print("Please enter the valid second number")
     else:
          print("Division is :",fnum/snum)
else: 
     print("The calculator can not calculate your problem ")"""

# Menu driven prgramm

option = int(input("""
Hi, How can I help you.
1. Enter 1 for Pin Change.
2. Enter 2 for Balance Enquiry.
3. Press 3 for withdrawal.
4. Enter 4 for Exit.
Enter your choice: """))

if option == 1:
     oldPin = int(input("Enter the old pin: "))
     if oldPin != '123':
          newPin = int(input("Enetr the new pin: "))
     print(f"your new pin is {newPin}")
elif option == 2:
     print("Seriously we don't know the balance of your account.")
elif option == 3:
     print("Mere kya baap ka bank hai jo tujhe rupees doo.")
else: 
     print("Bhad mein ja")


   







 





