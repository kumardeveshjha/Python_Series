# Polymorphism : Multiple forms and phases

# 1. Method Overriding : If we have both parent and child method same then the child method will be called 
# 2. Method Overloading : In a single theree are multiple functions/methods but there outputs are different based on the inputs 
# 3. Operator Overloading 



# Mthod Overloading :
# A scenario in which you have two methods of same name in a single class but the behavior and outputs are different
# It helps in code optimization and reusability 
# In Python it does not works 

# class Shape:
#      def area(self,radius):
#           return 3.14*radius*radius
     
#      def area(self,l,b):
#           return l*b

# s = Shape()

# s.area(3)
# s.area(2,3)


# Making it method overriding in python 

# class Shape:
#      def area(self,a,b=0):
#           if b ==0:
#                return 3.14*a*a
#           else: 
#               return a*b
          

# s = Shape()

# print(s.area(3))
# print(s.area(2,3))


# Abstraction : It means  hidden 

# An abstraction class is something in which there should be atleast on abstract method 
# it is used to ensure security 

from abc import ABC,abstractmethod
class BankAPP(ABC):
     
     def database(self):
          print("Connected to database")

     @abstractmethod
     def security(self):
          pass

class MobileApp(BankAPP):
     def mobile_login(self):
          print("Login into the mobile app")
     
     def security(self):
          print("Mobile Security feature")

mob = MobileApp()
mob.mobile_login()


          



 



