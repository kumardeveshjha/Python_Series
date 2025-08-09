def mul(a,b):
     if b ==1 :
          return a
     else:
          return a + mul(a,b-1)
     
print(mul(5,3))     


def factorial(n):
     if n ==1:
          return 1
     else:
          return n *factorial(n-1)
     
print(factorial(5))


pallildrome = "madam"

def is_palildrome(str):
     if len(str) == 1 or len(str) == 0:
          return True
     else :
          if str[0] == str[-1]:
               return is_palildrome((str[1:-1]))
          else:
               return False
print(is_palildrome(pallildrome))


# Rabbit problem gave birth to the fibanacci series 

# It has time complexity 2^n which is the worst time complexity and space complexity is 0(n)
# In fibonacci series next number is formed using the sum of last two numbers 

import time
def fb(m):
     if m == 0 or m== 1:
          return 1
     else:
          return fb(m-1) + fb(m-2) 

time_start = time.time()
print(fb(6))
print(time.time() - time_start)



# To minimize the time complexity we can use memoization(Which is also known as dynamic programming
# We use space time trade off to reduce the time complexity 
def fb_memo(m,d):
     if m in d:
          return d[m]
     else:
          d[m] = fb_memo(m-1,d) + fb_memo(m-2,d)
          return d[m]
d = {0:1,1:1}
print("using memoization")
print(fb_memo(6,d))


# Power set 
def power_set(s):
     #base condition
     if len(s) == 0:
          return [[]]
     else:
          subset = power_set(s[1:])
          return subset + [[s[0]] + i for i in subset] 
s =[1,2,3]
print(power_set(s))