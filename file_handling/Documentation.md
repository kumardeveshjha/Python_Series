# Theory

Types of data used in I/O:
1. Text: 12345 as a sequence of Unicode char
2. Binary : 1234 as a sequence of bytes of it's binary equivalance 

Hence there are 2 file types :
1. Text file: All program files are text files 
2. Binary Files: Images,music,video,exe files

# How fil I/0 is done:

Open a file 
Read/Write data
Close the file 


Open a file using Open method 

store it into a reference variable object 

-- Problem with the write function is that when we reopen it and try to write something it will start from the beginning / or replace the context of existing file with new content 

-- Here we will use append method 

-- when we wanted to add multiple lines in a file we use "writelines"

# Read the file 
f.read() method is used to read the file 
-- Readline and readlines are the method to read the file 
-- readlines gives the lost of the lines from the file 

# Always use close function after completing the task to manage the memory 



# Now using context Manager(with)

-- It is good to close the file after usage as it will free up the resources 
-- If we don't then garbage collector will
# Using with 'context manager'
-- With keyword closes the file as soon as the usage is over 
-- Here is buffer memory works and it track all the records 

# Seek and Tell 
-- Seek: It can take you anywhere in the file 
-- Tell : It tells the current position in the file 

# Problem with working with text files 
-- Can't work with binary files 
-- Not good for other data types like int/float/list/tuple
1.
-- we must copy the image file and make it text file 
2.
-- For this purpose we uses a dummy copy file and store it in the directory 

 # Serialization and Deserialization 

 Serialization: Process of converting python data types to JSON format 
 Deserialization : Process of converting JSON to python data type 

# In serialization 

we create a any_name.json file and open it in write mode to write content

json.dump(data_type,f):

when we read it we use 

json.load(file name )


# Pickling ---- Important for data scientist 

Pickiling is a process whereby a Python object hierarchy is converted into a byte stream, and unpickling is the inverse operation, whereby a byte stream (from a binary file or bytes like object) is converted back into an object hierarchy.


-- You can convert into bytes, binary file that can be transfered. 
-- That can be reused in the same formate and can be use for working 

Pickle lets the user to store data in binary format. JSON lets the user store data in a human-readable text format.









