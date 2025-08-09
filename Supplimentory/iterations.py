num = [1,2,3]

# for i in num:
#      print(i)


# step 1: it fetches the iterator using iter()
# iter_num = iter(num)

# # Step2: it call the next function using the iter()

# next(iter_num)
# next(iter_num)
# next(iter_num)


# def my_lop(iterable):
#      iterable = iter(iterable)
#      while True:
#           try:
#                print(next(iterable))
#           except StopIteration:
#                break

# a = [1,2,3,4,5]
# print('Tuple')
# b = (1,2,3,4,5)
# print('set')
# c = {1,2,3,4,5}
# d = {'name':'devesh','age':24,'city':'koibhi ho'}

# print(list)              
# # my_lop(a)
# print('tuple')
# # my_lop(b)
# print('set')
# # my_lop(c)

# print('dict')
# my_lop(d)

# When you aplly iter on iterable then you get an iterator 
# but you again apply iter on the iterator then you get the same iterator 

# What is the benifit of learning 
# When you wanted to make a your own program and wanted to use ierable 
  


# lets create our own range function 

class My_Range:
     def __init__(self,start,end):
          self.start = start 
          self.end = end 
          
     def __iter__(self):
          return My_Range_Iterator(self)

class My_Range_Iterator:
     def __init__(self,iterable_obj):
          self.iterable = iterable_obj
     def __iter__(self):
          return self
     def __next__(self):
          if self.start >= self.end:
               raise StopIteration
          
               
