
# Questions 
How indexing works in sets
Why dict key cant be mutable data types
Enumerate
destructor
dir/isinstance/issubclass
classmethod vs staticmethod
The diamond problem
What’s the meaning of single and double underscores in Python variable and method names
Magic Methods (repr vs str)
How can objects be stored in sets even though they are mutable
Because set only allows the hashable data types 
every class has a method __has__ if it return integer then it is hashable otherwise not 




# Answers 

classmethod
A class method is a method that is bound to the class and not the object of the class.
They have the access to the state of the class as it takes a class parameter that points to the class and not the object instance.
It can modify a class state that would apply across all the instances of the class. For example, it can modify a class variable that will be applicable to all the instances.
staticmethod
A static method does not receive an implicit first argument. A static method is also a method that is bound to the class and not the object of the class. This method can’t access or modify the class state. It is present in a class because it makes sense for the method to be present in class.

Class method vs Static Method
The difference between the Class method and the static method is:

A class method takes cls as the first parameter while a static method needs no specific parameters.
A class method can access or modify the class state while a static method can’t access or modify it.
In general, static methods know nothing about the class state. They are utility-type methods that take some parameters and work upon those parameters. On the other hand class methods must have class as a parameter.
We use @classmethod decorator in python to create a class method and we use @staticmethod decorator to create a static method in python.
When to use the class or static method?
We generally use the class method to create factory methods. Factory methods return class objects ( similar to a constructor ) for different use cases.
We generally use static methods to create utility functions.


# :::::::::::::::::::: Week 4 : Modules :::::::::::::::::::::::

1.  What do you mean by __name__ == '__main__'
Here we are using this because we wanted to block a piece of code in our module that we do not wanted to display to others when they import our module.

# "Smart way to hide the code from other programmer"


2. What is a module?
   Module is a python file or piece of code that can exist independently 
   When a file running itself then its name is __main__
   When we call this file in another module it shows the name of the module by which it was defined. 

3. If we want to give anyone to allow to use that code we make it in a function and put it in the :
 #  if __name__ == '__main__':


Importing a module in pytgon 

1. We can import as many module as we want 
2. We can rename the name of the module
3. We can also import a specific function from the module
4. We can also rename that fraction of the module 



# ::::::::::::::: Week 4 Packages in Python ::::::::::::::::::::::

1. What are packages in Python
   A package in python is a directory containing similar sub packages and modules.

   A particular directory is treated as package if it has __init__.py file in it.
   The __init__.py file may be empty or contain some initialization code related to the package
    


