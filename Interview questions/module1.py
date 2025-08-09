# What do you mean by __name__ == '__main'





# What is a module?
# Any file with an extention of .py is called a module in python.
# Whenever we execute a program it's module name is __main__ and this name is stored in __name__ variableInterview questions


# def hello():
#      print("Hello")

# hello()
# print(__name__)


# def square(num):
#      print(num**2)
     
# def add(num):
#      num += 2
#      print(num)
     
     

#Here we are using this because we wwnate d to block a code taht we do not wanted to display to others
# if __name__ == '__main__':
#      # for i in range(1,11):
#      #     square(i)
#      add(12)



def hello(name):
     print(f'Hello {name}')
