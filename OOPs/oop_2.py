# Part 1 : Encapsulation 

# Write OOP classes to handle the following scenarios:
#   A user can create and view 2D coordinates
#   A user can find out the distance between 2 coordination
#   A user can find the distance of a coordinate from origin
#   A user can check if a point lies on a given line 
#   A user can find the distance between a given 2D point and a given line 
#   A user can check the line intercepts or not 
  
# class Point:
#      def __init__(self,x,y):
#           self.x_cord = x
#           self.y_cord = y
#      # User can create and view new cordinates 
#      def __str__(self):
#           return f"({self.x_cord},{self.y_cord})"
#      # Ecludian distance 
#      def ecludian_distance(self,other):
#           return ((self.x_cord-other.y_cord)**2 + (self.y_cord-other.y_cord)**2)**0.5
     
#      # distance from origin 
#      def orgin_distance(self):
#      # return (self.x_cord**2 + self.y_cord**2)**0.5
#           return self.ecludian_distance(Point(0,0))
     
     
     
          
             
# p1 = Point(0,1)
# p2 = Point(1,1)

# print(p1)            
# print(p2)            

# print(p1.ecludian_distance(p2))
# print(p1.orgin_distance())


# class Line:
     
#      def __init__(self,A,B,C):
#        self.A = A   
#        self.B = B   
#        self.C = C   
       
#      def __str__(self):
#           return f"{self.A}x+{self.B}y+{self.C} = 0"
     
#      def poinOnLine(line,point):
#           if line.A*point.x_cord + line.B*point.y_cord + line.C == 0:
#               return ("Pints Lies on the line")
#           else:
#                return ("points Does not lies on the the line")
               
#      def minimumDistance(line,point):
#          return abs(line.A*point.x_cord + line.B*point.y_cord + line.C)/(line.A**2 + line.B**2)**0.5
     
#      def intersectingLines(line1,line2):
#           if line1.A == line2.A & line1.B == line2.B & line1.C != line2.C:
#                return f'{line1} and {line2} are  parallel lines'
#           elif line1.A != line2.A & line1.B != line2.B & line1.C != line2.C:
#                return f'{line1} and {line2} are distinct lines'
          
#      def findSlope(line):
#           return f'the slope of {line} is {-line.B}/{line.A}'         
     
     

# line1 = Line(3,4,-8)
# line2 = Line(2,3,-5)
# line3 = Line(5,-1,-4)
# point = Point(0,2)
# print(line1)
# print(point)

# print(line1.poinOnLine(point))   # when you call as objectname.methodName() then your object automatically makes the first parameter
# print(line1.minimumDistance(point))

# print(line2.intersectingLines(line3))

# print(line1.findSlope())




# How object access the attributes 

# class Person:
#      def __init__(self,name,country):
#           self.name = name
#           self.country = country 
          
#      def greet(self):
#           if self.country =='Bharat':
#                print('Namaste',self.name)
#           else:
#                print('Hello',self.name)


# dev = Person('dev','Bharat')
# # dev.name = 'dev'
# # dev.country = 'Bharat'
# dev.greet()
          

# Reference Variable


# Lets take an example of this 
# p = Person()   # here person is the object created and the p is the refernce variable which holds the address of the that object 


# Pass by reference 

# class Contact:
#    def __init__(self,name,gender):
#         self.name = name 
#         self.gender = gender 
  

# outside of the class --> Function 

# def greet(Person):
#      print(id(p))
#      print(f'Hello my name is {Person.name} and my is the gender is {Person.gender}')
#      Person.name = "Devesh"
#      return Person    # If the type is immmutable than the address will change but python object are mutable  
# p = Contact('Dev','Male')
# print(id(p))
# p1 = greet(p)
# print(id(p1))





# Encapsulation

# instance variable 

# class Contact:
#      def __init__(self,name,country):   # here name and country are instance variables because they have different value
#           self.name = name
#           self.country = country
          
#      def greet(self):
#           return f"Hello {self.name} from {self.country}"


# p1 = Contact('Dev','India')
# print(p1.name)
# p2 = Contact('Deven','Australia')
# print(p2.name)


# # So basically the encapsulation is used when we want to secure the methods and attributes
# # of a class from being accessed directly from outside the class.


# # Example for encapsulation 
# class ATM:
  
#   #constructor (it is a special function)
#   def __init__(self):
    
#     self.__pin = ''
#     self.__balance = 0   
# #   self.menu()
  
#   def get_balance(self):
#        print(f'Your current balance is {self.__balance}')
       
#   def set_balance(self,new_balance):
#        if type(new_balance) == int:
#         self.__balance = new_balance
#        else:
#             return "Bohot maroonga sale sudhar ja"
      
  
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
#            self.withdrawal()
#       else:
#            print("Thank you for using our ATM service")
           
 
  
#   def create_pin(self):
#        user_pin = int(input("Please enter your pin: "))
#        self.__pin = user_pin
#        user_balance = int(input("Please enter your balance: "))
#        self.__balance = user_balance
#        print("Your pin is created successfully")
#        self.menu()
       
 
#   def change_pin(self):
#        old_pin =int(input("Please enter your pin: "))
#        if old_pin == self.__pin:
#             new_pin = int(input("Please enter your new pin: "))
#             self.__pin = new_pin
#             print("Your pin is changed successfully")
#        else:
#             print("Wrong Pin")
#        self.menu()
            
          
          
#   def check_balance(self):
#        user_pin = int(input("Please enter your pin: "))
#        if user_pin == self.__pin:
#             print(f'Your balance is: {self.__balance}')
            
#        else:
#             print("Wrong Pin! Please enter the correct pin")
#        self.menu()
  
#   def withdrawal(self):
#        user_pin = int(input("Please enter your pin: "))
#        if user_pin == self.__pin:
#             amount = int(input("Please enter the ammount to withdraw"))
#             if amount <= self.__balance:
#                  self.__balance -= amount
#                  print(f'Please collect your cash: {amount}')
#                  print(f'your remaining balance is: {self.__balance}')
#             else:
#                  print('Insufficient balance')
#        else:
#             print("Wrong pin! please enter the correct pin")
#        self.menu()
            
       
      
     
    
# obj = ATM()
# obj.menu()


# obj.create_pin()
# obj.balance = "hehhehe" it will change 
# obj.__balance = "Heheheh" // that it will not work 
# obj._ATM__balance = 'Hehehed'

# obj.get_balance()
# obj.set_balance(2000)

# obj.get_balance()
# obj.check_balance()



# obj.check_balance()

# class User:
#      def __init__(self,name,gender):
#           self.name = name
#           self.gender = gender
     
     
# u1 = User("Dev","Male")
# u2 = User("Deven","Male")
# u3 = User("Mina","female")


# # Storing in lists 
# L = [u1,u2,u3]
# for i in L:
#      print(i.name,i.gender)
     
# # Storing in dictionary 

# d = {"user1":u1, "user2":u2,"user3":u3}
# print(d)

# for i in d:
#      print(d[i].name)
     
# Storing in set // it will not store it because set does not store mutable objects 



### 'STATIC' Keyword

class ATM:
     
  __counter = 1    # here it is static variable
  
  #constructor (it is a special function)
  def __init__(self):
    print(id(self))
    self.cid = ATM.__counter
    ATM.__counter = ATM.__counter + 1
    self.pin = ''
    self.balance = 0
    print("I am called and executed")
#     self.menu()
  
  
  #utility functions that does not requires the methods 
  @staticmethod
  def get_counter():
       return ATM.__counter
  
  
  def menu(self):
      user_input =  input("""
             Hi, How can I help yo?
             
             1. Press 1 for create pin
             2. Press 2 for change pin
             3. Press 3 for check balance
             4. Press 4 for withdrawal
             5. Anything else to exit
             """)
      if user_input == '1':
           #create pin
           self.create_pin()
      elif user_input == '2':
           #change pin
           self.change_pin()
      elif user_input == '3':
           #user balance
           self.check_balance()
      elif user_input == '4':
           #withdrawal
           self.withdraw()
      else:
           print("Thank you for using our ATM service")
           exit()
 
  def create_pin(self):
       user_pin = int(input("Please enter your pin: "))
       self.pin = user_pin
       
       user_balance = int(input("Please enter your balance: "))
       self.balance = user_balance
      
       print("Your pin is created successfully")
       self.menu()
 
  def change_pin(self):
       old_pin =int(input("Please enter your pin: "))
       if old_pin == self.pin:
            new_pin = int(input("Please enter your new pin: "))
            self.pin = new_pin
            print("Your pin is changed successfully")
            self.menu()
       else:
            print("Wrong Pin")
            self.menu()
          
          
  def check_balance(self):
       user_pin = int(input("Please enter your pin: "))
       if user_pin == self.pin:
            print(f'Your balance is: {self.balance}')
            self.menu()
       else:
            print("Wrong Pin! Please enter the correct pin")
  
  def withdrawal(self):
       user_pin = int(input("Please enter your pin: "))
       if user_pin == self.pin:
            amount = int(input("Please enter the ammount to withdraw"))
            if amount <= self.balance:
                 self.balance -= amount
                 print(f'Please collect your cash: {amount}')
                 print(f'your remaining balance is: {self.balance}')
            else:
                 print('Insufficient Balance')
       else:
            print("Wrong pin! please enter the correct pin")
            self.menu()
       
      
     
    
obj = ATM()

C1 = ATM()
C2 = ATM()
C3 = ATM()

print(C1.cid)
print(C2.cid)
print(C3.cid)
print(ATM.counter)


