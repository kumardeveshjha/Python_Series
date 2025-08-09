# @Inheritance 
# @Polymorphism 
# @Abstraction 


# Class Relationship 
# 1. Aggregation 
# 2. Inheritance 


# class Customer:
#      def __init__(self,name,gender,address):
#           self.name = name
#           self.gender = gender
#           self.address = address
#      def display_address(self):
#           print(self.address.get_city(),self.address.pin,self.address.state,self.address.mobile)
          
#      def edit_profile(self,new_name,new_city,new_pin,new_state,new_mobile):
#           self.name = new_name
#           self.address.edit_address(new_city,new_pin,new_state,new_mobile)

# class Address:
     
#      def __init__(self,city,pin,state,mobile):
#           self.__city = city 
#           self.pin = pin 
#           self.state = state
#           self.mobile = mobile 
          
#      def get_city(self):
#           return self.__city
     
#      def edit_address(self,new_city,new_pin,new_state,new_mobile):
#           self.__city = new_city
#           self.pin = new_pin
#           self.state = new_state
#           self.mobile = new_mobile
          

# add1 = Address('Agra',28311,"UP",908841234)       
# customer = Customer("Dev","Male",add1)  

# customer.display_address()

# customer.edit_profile("Devesh","Mohali",12345,"Punjab",20000000)
# customer.display_address()

# Aggregation doesn't gaurantee that you can access the private data of that class 



# Inheretance : A child class owns the properties of the parent class : 


# class User:
#      def __init__(self):
#           self.name = "Devesh"
#      def login(self):
#           print("Login")
          
# class Student(User):
#      def enroll(self):
#           self.rollno = 24
     
#      def enroll(self):
#           print('Enrolled into the course')
          
# u = User()

# s = Student()
# print(s.name)



# What can be inherited 

# class Phone:
#      def __init__(self,price,brand,camera):
#           print("Inside the Phone class constructor")
#           self.price = price
#           self.brand = brand
#           self.camera = camera
     
#      def buy(self):
#           print("I am buying a phone")
          
     
     
# class Smartphone(Phone):
#      pass
     
# s = Smartphone(2000,"Apple",24)   # Here Smartphone class will inherit the properties of phone class
# s.buy() 


# class Phone:
#      def __init__(self,price,brand,camera):
#           print("Inside the Phone class constructor")
#           self.price = price
#           self.brand = brand
#           self.camera = camera
     
#      def buy(self):
#           print("I am buying a phone")
          
# class Smartphone(Phone):
#      def __init__(self,os,ram):
#           self.os  = os
#           self.ram = ram
#           print("Inside the Smartphone class")

# s1 = Smartphone("Android",8)          ## when child has it's own constructor than child will not access the parents class constructor


# Child class can not access the private methods of parent class

# class Phone:
#      def __init__(self,price,brand,camera):
#           print("Inside the Phone class constructor")
#           self.price = price
#           self.brand = brand
#           self.camera = camera
     
#      def buy(self):
#           print("I am buying a phone")
          
# class Smartphone(Phone):
#      def check_price(self):
#           print(self.price)
     

# S3 = Smartphone(40000,"Apple",24)

# S3.buy()


# class Parent:
     
#      def __init__(self,num):
#           self.num = num
          
#      def get_num(self):
#           return self.num

# class Child(Parent):
#      def show(self):
#           print("This is in the child class")


# son = Child(200)

# class A:
#      def __init__(self):
#           self.vari = 101
     
#      def display(self,var1):
#           print("Class A : ",self.vari)

# class B(A):
#      def display(self,veri):
#           print("Class B :", self._vari)

# obj = B()
# obj.display(200)      # output 101


# Method Overriding

# In this concept the method of the constructor will override the method of the any parent or child class



####***** Super Keyword 

# class Phone:
#      def __init__(self,price,brand,camera):
#           self.__price = price
#           self.brand = brand 
#           self.camera = camera 
          
     
#      def buy(self):
#           print("I am buying a new phone")          
# class Smartphone(Phone):
#      def buy(self):
#           print("Buying A new smartphone")
#           print("Using super keyword")
#           # syntax to call parent's buy method 
#           super().buy()
          
# s = Smartphone(40000,"Iphone 16",24)

# s.buy()


## Best example to use the super method 

# class Phone:
#       def __init__(self,price,brand,camera):
#           print("Inside the phone constructor")
#           self.__price = price
#           self.brand = brand 
#           self.camera = camera 
          
# class Smartphone(Phone):
#      def __init__(self,price,brand,camera,os,ram):
#           print("Inside the smartphone constructor")
#           super().__init__(price,brand,camera)
#           self.os = os
#           self.ram = ram
#           print("Inside the smartphone constructor")

# s = Smartphone(100000,"Iphone",48,"IOS16",16)

          
# Questions 1 

# class Parent:
     
#      def __init__(self,num):
#           self.__num = num
#      def get_num(self):
#           return self.__num


# class Child(Parent):
#      def __init__(self, num,val):
#           super().__init__(num)
#           self.__val = val

#      def get_val(self):
#           return self.__val

# son = Child(200,300)
# print(son.get_num())
# print(son.get_val())


#Question 2 
# class Parent:
     
#      def __init__(self):
#           self.num = 100
#      def get_num(self):
#           return self.num


# class Child(Parent):
#      def __init__(self):
#           super().__init__()
#           self.var = 200

#      def show(self):
#           print(self.num)
#           print(self.var)

# son = Child()
# son.show()


#Example 3 


# class Parent:
     
#      def __init__(self):
#           self.__num = 100
#      def show(self):
#           print("Parent",self.__num)


# class Child(Parent):
#      def __init__(self):
#           super().__init__()
#           self.__var = 20

#      def show(self):
#           print("Child",self.__var)

# Obj = Child()
# Obj.show()


##:::::::::::
# # Types of Inheritance 
# 1. Single Inheritance 
# 2. Multilevel Inheritance 
# 3. Hierachical 
# 4. Multiple Inheritance(Diamond Problem)
# 5. Hybrid Inheritance 


# 2. Mulltilevel 

# class Product:
#      def review(self):
#           print("Product customer review")
     
# class Phone(Product):
#      def __init__(self,price,brand,camera):
#           print("Inside the phone constructor")
#           self.__price = price
#           self.brand = brand 
#           self.camera = camera 
#      def buy(self):
#           print("Buying a Phone")

# class Smartphone(Phone):
#      pass

# S = Smartphone()




# 3. Hierarchical Inheritance 


# class Phone():
#      def __init__(self,price,brand,camera):
#           print("Inside the phone constructor")
#           self.__price = price
#           self.brand = brand 
#           self.camera = camera 
          
#      def buy(self):
#           print("Buying a phone")
          
# class Product():
#      def buy(self):
#           print("Product buy Method")

# class Smartphone(Phone, Product):
#      pass
     
     
# s = Smartphone(2000,"Aple",13)
# s.buy()                          # // Here the first class method will call this is known as Mthod Resolution order 


# class A:
#      def m1(self):
#           return 20
# class B:
#      def m1(self):
#           return 30
#      def m2(self):
#           return 40
# class C(B):
#      def m2(self):
#           return 20

# obj1 = A()
# obj2 = B()
# obj3 = C()

# print(obj1.m1() + obj3.m1() + obj3.m2())


# class A:
#      def m1(self):
#           return 20

# class B:
#      def m1(self):
#           val = super().m1() + 30
#           return val
# class C(B):
#      def m1(self):
#           val = self.m1()+20
#           return val

# obj = C()

# print(obj.m1())