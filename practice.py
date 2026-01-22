# Mkainhg a infinite array generator in numpy array 
# import numpy as np

# def infinite_array(rows=3,cols=3):
     
#      n = 0
#      while True:
          
#           arr = np.arange(n,n + rows*cols).reshape(rows,cols)
#           yield arr
#           n += rows*cols
         

# infi_array = infinite_array()

# for i,array in enumerate(infi_array):
#      if isinstance(array,np.ndarray):
#           print(np.vstack(array))
#      else:
#           print("Not a numpy array")
#      if i == 100:
#           break
     
     
# eng_std = int(input())
# eng_roll = [list(map(int,input().split()))]

# fre_std = int(input())
# fre_roll = [list(map(int,input().split()))]

# eng_set = set(eng_roll)
# fre_set = set(fre_roll)

# print(eng_set,fre_set)

eng = int(input())
eng_list = list(map(int,input().split()))
fre = int(input())
fre_list = list(map(int,input().split()))

if len(eng_list) == eng and len(fre_list) == fre:
    eng_set = set(eng_list)
    fre_set = set(fre_list)
    
    print(eng_set.difference(fre_set))
    
else:
     print("The set has ot elements to be deleted")