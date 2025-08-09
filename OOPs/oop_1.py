# L = [1,2,3,4]
# print(type(L)) # <class 'list'>

# Class is a blueprint for creating objects
# Object is an instance of a class
# Class has two main componets 
# 1. Attributes (data members) or properties
# 2. Methods (functions)

# Syntax to create a object
# object_name = ClassName() # object_name is the instance of the class

# A small banking application -- like an ATM

# class ATM:
  
#   #constructor (it is a special function)
#   def __init__(self):
#     print(id(self))
#     self.pin = ''
#     self.balance = 0
#     print("I am called and executed")
#     self.menu()
  
#   def menu(self):
#       user_input =  input("""
#              Hi, How can I help yo?
             
#              1. Press 1 for create pin
#              2. Press 2 for change pin
#              3. Press 3 for check balance
#              4. Press 4 for withdrawal
#              5. Anything else to exit
#              """)
#       if user_input == '1':
#            #create pin
#            self.create_pin()
#       elif user_input == '2':
#            #change pin
#            self.change_pin()
#       elif user_input == '3':
#            #user balance
#            self.check_balance()
#       elif user_input == '4':
#            #withdrawal
#            self.withdraw()
#       else:
#            print("Thank you for using our ATM service")
#            exit()
 
#   def create_pin(self):
#        user_pin = int(input("Please enter your pin: "))
#        self.pin = user_pin
       
#        user_balance = int(input("Please enter your balance: "))
#        self.balance = user_balance
      
#        print("Your pin is created successfully")
#        self.menu()
 
#   def change_pin(self):
#        old_pin =int(input("Please enter your pin: "))
#        if old_pin == self.pin:
#             new_pin = int(input("Please enter your new pin: "))
#             self.pin = new_pin
#             print("Your pin is changed successfully")
#             self.menu()
#        else:
#             print("Wrong Pin")
#             self.menu()
          
          
#   def check_balance(self):
#        user_pin = int(input("Please enter your pin: "))
#        if user_pin == self.pin:
#             print(f'Your balance is: {self.balance}')
#             self.menu()
#        else:
#             print("Wrong Pin! Please enter the correct pin")
  
#   def withdrawal(self):
#        user_pin = int(input("Please enter your pin: "))
#        if user_pin == self.pin:
#             amount = int(input("Please enter the ammount to withdraw"))
#             if amount <= self.balance:
#                  self.balance -= amount
#                  print(f'Please collect your cash: {amount}')
#                  print(f'your remaining balance is: {self.balance}')
#             else:
#                  print('Insufficient Balance')
#        else:
#             print("Wrong pin! please enter the correct pin")
#             self.menu()
       
      
     
    
# obj = ATM()

# print(id(obj))


# print(id(1))
# obj2 = ATM()

# print(id(obj2))


# Personal datatype -> Fractions 

# class Fraction:
     
#      #parameterized constructor --> It requires parameters 
#      def __init__(self,x,y):
#           self.numerator = x
#           self.denominator = y 
#           self.compare = self.__compare__
     
#      def __str__(self):
#           return f'{self.numerator}/{self.denominator}'
     
#      def __add__(self,other):
#           new_num = self.numerator *other.denominator + other.numerator * self.denominator
#           new_den = self.denominator*other.denominator
#           return f'{new_num}/{new_den}'
     
#      def __sub__(self,other):
#           new_num = self.numerator*other.denominator - other.numerator*self.denominator
#           new_den = self.denominator*other.denominator
#           return(f'{new_num}/{new_den}')
     
#      def __mul__(self,other):
#           new_num = self.numerator * other.numerator
#           new_den = self.denominator * other.denominator
#           return f"{new_num}/{new_den}"
     
#      def __truediv__(self,other):
#           new_num = self.numerator * other.denominator
#           new_den = self.denominator * other.numerator
#           return f"{new_num}/{new_den}"
     
#      def __compare__(self,other):
#           if self.numerator * other.denominator > other.numerator * self.denominator:
#                return f"{self} is greater than {other}"
#           elif self.numerator * other.denominator < other.numerator * self.denominator:
#                return f"{self} is less than {other}"
#           else:
#                return f"{self} is equal to {other}"
          
        
     
# fr1 = Fraction(1,3)
# fr2 = Fraction(1,2)

# print(fr1+fr2)
# print(fr1-fr2)
# print(fr1*fr2)
# print(fr1/fr2)
# print(fr1.compare(fr2))


class User:
     def __init__(self):
          self.name = ''
          self.age = 0
          self.email = ''
         
          
     def set_name(self):
          user_name = input('Please Enter Your Name: ')
          self.name = user_name
     
     def set_age(self):
          user_age = int(input('Please enter your age: '))
          self.age = user_age
     def set_email(self):
          user_email = input("Please enter your email: ")
          self.email = user_email
     

     def display_user_info(self):
          print(f"Name: {self.name}")
          print(f"Age: {self.age}")
          print(f"Email: {self.email}")
          
     # instance of user1 
     

     
user1 = User()
user1.set_name() 
user1.set_age()  
user1.set_email() 
user1.display_user_info()








