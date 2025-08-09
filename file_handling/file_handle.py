# # Case 1: If the file is not present 

# f = open("sample.txt",'w')
# f.write("Har har mahadev")
# f.write("\n Namah parvati pataye har har mahadev ")
# f.close()


# f = open("sample.txt",'w')
# f.write("Om namah shivay")  # it will oerride the above text 
# f.close()

# f = open('sample.txt','a')
# f.write("\nHello Dev")
# f.close()

# # When we wanted to add multiple line as input in a single time
# L = ["Hello Dev!\n","How are you\n","I am here to help you "]
# f = open('sample.txt','w')
# f.writelines(L)

# f = open('sample.txt','r')
# r = f.read()
# print(r)
# f.close()
# f = open('sample.txt','r')
# s = f.readlines()     // it willl provide the list of lines 

# print(s)
# while True:
     
#      data = f.readline()
     
#      if data == "":
#           break
#      else:
#           print(data,end='')
# f.close()


# Using with keyword 

# with open('sample.txt','w') as f:
#      f.write("\nHello I am from context manager")

# with open('sample.txt','r') as f:
#      print(f.read(),end='')

# with open('sample.txt','r') as f:
#      print(f.read(10),end='')
#      print(f.read(10),end='')
     
     
     
# big_L = ["Hello Dev" for i in range(1000)]
# # big_L = str(big_L)    // this is when we use read method 
# with open('sample.txt','w') as f:
#      f.writelines(big_L)

# with open('sample.txt','r') as f:
     
     # chunk_size = 100
     
     # while len(f.read(chunk_size)) > 0:
     #      print(f.read(chunk_size),end='')
     #      f.read(chunk_size)
     # while chunk_size > 0:
     #      print(f.read(chunk_size),end="")
     #      f.read(chunk_size)

# with open('sample.txt','r') as f:
#      print(f.read(10))
#      print(f.tell())
#      print(f.read(20))
#      print(f.seek(0))
#      print(f.tell())
#      print(f.read(300))
#      print(f.seek(301))
#      print(f.read(3))


#Seek during write 
# with open("sample.txt",'w') as f:
#      f.write('Hello')
#      f.seek(0)
#      f.write("Hello Devmanus")
     
# Problems in working with text files 

# with open("GTM.png",'r') as f:
#      f.read()  # we can't do it with images 

# working with binary files 
# with open("Dev.JPG",'rb') as f:
#     with open("Dev_copy.jpg",'wb') as wf:
#          wf.write(f.read())
          
# working with other data type 

# with open('sample.txt','w') as f:
#      f.write(5)                  # it will not work 
     

# with open('sample.txt','r') as f:
#      print(int(f.read()) + 5)

# working with other data types 

# d = {
#      "name":"Devesh Kumar",
#      "Age": 24,
#      'gender': "Male"
# }
 
# # with open('sample.txt','w') as f:
# #      f.write(str(d))

# # with open('sample.txt','r') as f:
# #      print(f.read())
# #      print(dict(f.read()))


# # Serialization and Deserialization 

# # This is done so we can handle the complex data type in files 

# # Serialization: Process of converting python data types to JSON format 
# # Deserialization : Process of converting JSON to python data type 

# # Serialization using JSON module 

# # list 

# import json
# # L = [1,2,3,4]

# # with open('demo.json','w') as f:
# #      json.dump(L,f)

# with open('demo.json','w') as f:
#      json.dump(d,f,indent=5)

# with open('demo.json','r') as f:
#     d = json.load(f)
#     print(d)
#     print(type(d))
    
    
# t = (1,2,3,4,5)

# with open('demo.json','w') as f:
#      json.dump(t,f)


# Serialization and deserialization for custom object 



# We can not serialize our personal methods 
class Person: 
     
     def __init__(self,fname,lname,age,gender):
          self.fname = fname
          self.lname = lname
          self.age = age
          self.gender = gender 
          
person = Person("Devesh","Kumar",24,"Male")


# formate to printed in 
# Devesh Kumar age -> 33 gender -> male 

# import json

# def show_method(person):
#      if isinstance(person,Person):
#           return f'{person.fname} age -> {person.age} gender -> {person.gender}'

# with open('demo.json','w') as f:
#      json.dump(person,f,default = show_method)

# with open('demo.json','r') as f:
#      print(json.load(f))
     


# Pickling 

# Pickling is a method in which we convert our objects or any code base into a pickle file and can be transferred  


# class Person:
#      def __init__(self,name,age):
#           self.name = name
#           self.age = age 
          
#      def display(self):
#           print(f'Hi my name {self.name} and i am {self.age} years old')
          
# person = Person('Devess',24)

# import pickle

# with open('person.pkl', 'wb') as f:
#      pickle.dump(person,f)

# with open('person.pkl', 'rb') as f:
#      print(pickle.load(f))

# person.display()


























