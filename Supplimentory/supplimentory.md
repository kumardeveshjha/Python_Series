What is an Iteration 
Iteration is a general term for taking each item of something. one after another. Anytime you use a loop. explicit or implicit, to go over a group of items, that is iteration.

# What is a iterator 

A iterator is an object that allows the programmer to traverse through a sequence of data without having to store the entire data into memory.
Like it takes a sigle data at a single time and load it to the memory and perform any operation task and remove it from memory and continue this process. 
this helps in memory optimization.

use sys module 
sys.getsizeof(l)   to check the memory allocated or consumed by the iterator.


<!-- What can be iterable-->

Iterable is an object, which one can ietaret over
it generates an iterator when passed to iter() method

# every iterator is also and iterables 
# not all iterables are iterators 

trick : (agar loop chala sakte hai to iterable hai nahi to nahi)
(ek iterator should have two methods iter() and next())
-- every iterable has an iter function

How loop works?


How Iterator works 
There are two main function in the iterators 
1. iter  
2. next





#Gernerators  

-- Generators are the simple way to create the iterators. 
-- Because the iterator consumes less metory than loops
-- Here the unique thing is the 'Yield' over 'Return'

-- Here the function does not call direct untill the object is not created 

## Yield Vs Return in a gunction 
-- The main difference between a function and a generator is that the function returns a single value but the generator partially returns the value and also keep track of the previous execution 

## Why we use generators 
1. Ease of implementation 
2. It is used in Deeep Learning to store and train the data 
3. It is memory efficient.
4. Chaining the generator 
Bade data ke saath kam karne ke liye bahot avashayak hai .









