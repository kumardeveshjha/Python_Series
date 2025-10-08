
# %%
import pandas as pd 
import numpy as np 



## Vectorized string Operations 

##--> 

a = np.array([1,2,3,4])
a*4

# problem with vectorized operations in vanilla python 

s = ['cat','mat',None,'rat']  # it will be slow if the data is too much and also it doesn't work with None


# [i.startswith('c') for i in s]    # AttributeError: 'NoneType' object has no attribute 


# panda --> Numpy --> c  (This gives it the speed)


# How to solve this with pandas 

s = pd.Series(s)

# here 'str' is string accessor
s.str.startswith('c')


#%%

df = pd.read_csv('dataset_4/titanic.csv')

df['Name']

# common Functions 

# lower/upper/capitalize/title 

# df['Name'].str.upper()
# df['Name'].str.lower()
# df['Name'].str.capitalize()


# print(df['Name'][df['Name'].str.len() == 82])

# Strip  --. important in NLP related tasks 

# '           dev        '.strip()

## Split --> get
# split() -- > It splits the string and gives the list 
# df['Name'].str.split(',')

# But we can get using the it spreads the split

df['lastname'] =  df['Name'].str.split(',').str.get(0)
# df.head()

df[['title','f_name']] = df['Name'].str.split(',').str.get(1).str.strip().str.split(' ',n=1,expand=True)
df['title'].value_counts()

##:::: Replace --->  Stops the duplicate of the data 

df['title'] = df['title'].str.replace('Ms.','Miss.')
df['title'] = df['title'].str.replace('Mlle.','Miss.')
df['title'].value_counts()


#%%
## Filtering:::::::: 

# startswith / endswith

df[df['f_name'].str.startswith('A')]
df[df['f_name'].str.endswith('A')]


# isdigit/isalpha 

df[df['f_name'].str.isdigit()]



## Applying RegEx ::::::::::::

# Contains For searching any string based name 
df[df['f_name'].str.contains('john',case=False)]

# find the lastname with start and end char vowel 

df[df['lastname'].str.contains('^[aeiouAEIOU].+[aeiouAEIOU]$')]


# Slicing in the dataframe strings 
df['Name'].str[::2]



# %%
