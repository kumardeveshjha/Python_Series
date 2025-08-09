
# aliasing It helps in # code/memory optimization and reusability
# b = 4
# a = b
# print(id(a,b))

# when you delete actually there is no deleting in memory it only delets the reference 

# what is garbage collection in python 


L = [1,2,3,4]
print(id(L))
L.append(5)
print(id(L))

T = (1,2,3)
print(id(T))
T = T + (4,)
print(id(T))


def func(data):
     data = data +(5,)

T1 = (1,2,3,4)
func(T1)
print(T1)

sset_1 = {"name": "Dev", "age": 25}
print(sset_1)
sset_1["name"] = "Devesh Kumar"
sset_1["gender"] = "Male"

print(sset_1)


# set follows the concept of hashing for storing data or indexing 

