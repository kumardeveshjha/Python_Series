import numpy as np

# creating a numpyarray uisng function np.array()
# install numpy array 

#Vector 
# a = np.array([1,2,3])
# print(type(a))

#Matrix
# make two list for 2-d numpy array 
# b = np.array([[1,2,3],[4,5,6]])
# print(b)

#Tensor 

# c = np.array([[[[1,2,3],[4,5,6],[7,8,9]]]])
# print(c)
# print(type(c))


#dtype  --> Parameter 
# float, boolean, int
# a1 = np.array([1,2,3],dtype= bool)
# print(a1)

#np.arange 
# it works as a range 

# a2 = np.arange(1,11)
# print(a2)

#With reshape 
# reshape(n1,n2) n1*n2 = n 
# a3 = np.arange(1,11).reshape(5,2) 
# print(a3)


# a31 = np.arange(24).reshape(2,2,2,3)
# print(a31)
# np.ones and np.zeros

# a4 = np.ones([3,4])
# print(a4)

# a5 = np.zeros((3,4))
# print(a5)


#np.random random class and erandom method 
# a6 = np.random.random((2,5))
# a6 = np.round(a6*100)
# print(a6)

#mp.linesopce  --> linear space : it generates points at equal distance 

# print(np.linspace(-10,10,10))

# np.identity 
# print(np.identity(3)) 

# b1 = np.arange(128).reshape(4,2,4,4)
# print(b1)

# Number of dimensions 
# print(b1.ndim)

# Tell the shape of the array 
# print(b1.shape)

# Tell the number of the 
# print(b1.size)

#Itemsize
# b2 = np.arange(18).reshape(2,3,3)
# print(b2)

#dtype 

# print(b2.dtype)

#Changing Datatype 

#astype
# print(b2.astype(np.int32))


#Array operations 

# b3 = np.arange(12).reshape(3,4)
# b4 = np.arange(12,24).reshape(3,4)
# print(b4)
# print(b4.shape)
# print(b4.ndim)
# print(b4.size)

#Mathematical operations : These performs at every element of the arrayu
# print(b3)
# print(b3+3)
# print(b3-3)
# print(b3*3)
# print(b3/3)


#Relational operator 
# print(b3>10)
# print(b4>10)
# print(b4<10)


#Vector operations 

# print(b3+b4)


# b5 = np.array([1,2,3,4,5,6,7,8]).reshape(2,2,2)
# print(b5[1][1][0])

# b5[1][1][0] = 2

# print(b5[1][1][0])



#Array Function 

# af1 = np.random.random((3,3))
# af1 = np.round(af1*100)
# print(af1)

# max ,min, sum, product 
# 0-> Column and 1 -> row
# print(np.max(af1))
# print(np.min(af1))
# print(np.prod(af1))
# print(np.sum(af1))

# when I want to find the specific min/max from a row or column

# print(np.max(af1,axis=0))


# mean/ median / var /std

# print(np.mean(af1,axis=1))
# print(np.median(af1))
# print(np.var(af1))

# trignometric 
#we will barely use it 

# dot product 

# af2 = np.arange(12).reshape(4,3)
# af3 = np.arange(12,24).reshape(3,4)
# af4 = np.random.random((3,4))*100
# print(af2)
# print(af3)
# print(np.dot(af2,af3))

#log and exponent 

# print(np.exp(af3))
# print(np.log(af3))

# round / floor / ciel 


#Indexing and Slicing 

# a1 = np.arange(10)
# a2 = np.arange(12).reshape(3,4)
# a3 = np.arange(24).reshape(2,4,3)

# name = "devesh Kumar Jha "
# print(a3)
# print(a3[1,1,1],a3[0,2,1])  # array[shape,]


#Slicing   slicing(first,n-1)

# When we want to get multiple Ite,s then we use slicing

# a4 = np.array([0,1,2,3,4,5,6,7,8,9])
# print(a4[1:])   

# a5 = np.arange(12).reshape(3,4)

# print(a5)
# print(a5.ndim)
# print(a5[0,:])
# print(a5[:,1])
# print(a5[1:,1:3])
# print(a5[::2,0::3])
# print(a5[::2,1::2])
# print(a5[1,::3])
# print(a5[0:2,1:])
# print(a5[0:2,1::2])

# a6 = np.arange(27).reshape(3,3,3)
# print(a6)
# print(a6[::2])
# print(a6[0][1])
# print(a6[1][:,1])
# print(a6[::2,0,0::2])


#::::::::::::::::::::::-- Iterations on arrays--:::::::::::::

# a7 = np.arange(10)

# for i in a7:
#      print(i)


# a8 = np.arange(27).reshape(3,3,3)
# print(a8)
# for i in a8:    #This will give me the arrays of 2-D
#      print(i)

# for i in np.nditer(a8):   # This converts the nth dimension array in the single dimensio
#      print(i)
     
# :::::::::::::::-----Reshape-----::::::::::::
#Reshape()

# Transpose()

# a9 = np.arange(6).reshape(2,3)
# print(a9)
# print(np.transpose(a9))  
# a9.T
# print(a9)

#Ravel convert any order array into 1-D array 
# print(a9.ravel())


#:::::::::::::::---Stacking----::::::::::::::::
#Adding two numpy Arrays 
# Here we have two types of stacking 
#----------------1. Horizontal Stacking--------
a10 = np.arange(12).reshape(3,4)
a11 = np.arange(12,24).reshape(3,4)

print(np.hstack((a10,a11)))

#----------------2. Vertical Stacking-------

print(np.vstack((a10,a11)))

# Use: when we have multiple data sources and when we have same type of data we can use stacking 


# :::::::::::::::------Splitting ---------:::::::::::::
# Just opposite to the stacking 
# X- split 

print(np.hsplit(a10,4))












