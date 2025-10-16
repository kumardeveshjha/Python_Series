#%%

import numpy as np 
import pandas as pd 

# Time stamp Object 

# This is a particular moments in time 

## ::: Creating a timestamp object 

t_s = pd.Timestamp('2025/10/07')

type(t_s)

# Variations 

pd.Timestamp('2025-10-07')
pd.Timestamp('2025,10,07')


# only Year 

pd.Timestamp('2024')

# Using Text 
pd.Timestamp('7th november 2025')

# providing time 

pd.Timestamp('7th october 2025 1:55 pm')

# using datetime.datetime object (python)

import datetime as dt
dt.datetime(2025,10,7,1,58,00)

# now converting the datetime in timestamp 

x = pd.Timestamp(dt.datetime(2025,10,7,1,58,00))
x 

# %% 
# Fetching the 



##:: Why to use pandas timestamp when we have dattime in python which works as timestamp 

# syntax wise datetime is convinient 
# but the performance takes a hit while working with huge data. List vs Numpy array 
# The weakness of the python's datetime format inspired the Numpy team to add a set of native time series data type to Numpy
# The datetime64 dtype encode dates as 64-bit integers, and thus allows arrays of dates to be represented very compactly 

#%%

date = np.array('2025-10-07',dtype=np.datetime64)
date

# making 12 additional dates using the existing date 
date + np.arange(12)

# Text Area 



#


#%%

## Datetime Index Object : A collection of pandas timestamps objects 


# from strings (Creating datetime Index)

pd.DatetimeIndex(['2025/7/20','2025/11/10','2025/12/17'])

# using python datetime object 

pd.DatetimeIndex([dt.datetime(2025,7,10),dt.datetime(2025,11,10),dt.datetime(2025,12,17)])

# using pd.timestamps 

timed_index = pd.DatetimeIndex([pd.Timestamp(2025,10,7),pd.Timestamp(2025,11,10),pd.Timestamp(2025,12,17)])

# using datetimeindex as series index 

pd.Series([1,2,3],index=timed_index)


#%%
# Date_range Function 

# my_index = pd.date_range(start='2025/10/7',end='2025/11/10',freq='D')
# pd.Series([ i for i in range(35)],index=my_index)


# Some flexibility usng the frequency parameter 

pd.date_range(start='2025/10/7',end='2025/11/10',freq='3D')

# Set frequencies for multiple purpose 
# 3D --> After 3 days 
# B --> Only business days means mon - fri 
# Days --> only single days like 'W-sun' means only sundays 
# Hourly timestamp --> freq="H"

# Month start 
pd.date_range(start='2025/10/7',end='2025/11/10',freq='MS')

# Month end 
pd.date_range(start='2025/10/7',end='2025/11/10',freq='ME')

# A --> Year End 
pd.date_range(start='2025/10/7',end='2030/11/10',freq='A')

# using periods (number of results) ::--> makes periods of the equally according to the given periods value

pd.date_range(start='2025/10/7',periods=25,freq='me') 


##:::: To datetime 

# converts an existing object to pandas timestamps/datetimeindex object 

# simple series 


# %%
# s = pd.Series(['2025/10/7','2025/10/10','2025/10/12'])
# s.str.split('/').str.get(0)  --> This becomes hectic to handle 

#  now convert to datetime 

# pd.to_datetime(s).dt.year

#with errors 

s1 = pd.Series(['2025/10/7','2025/10/10','2025/105/12'])

pd.to_datetime(s1,errors='coerce').dt.month_name()


df = pd.read_csv('dataset_4/expense_data.csv')

df.info()

df['Date'] = pd.to_datetime(df['Date'])

df.info()


# now using dt accessor 

df['Date'].dt.month


# Plot the graph

#%%
import matplotlib.pyplot as plt 
plt.plot(df['Date'],df['INR'])
plt.show()


df['Day'] = df['Date'].dt.day_name()
df

# plt.plot(df['Day'],df['INR'])  THIS IS WFONG APPROACH 

# Now come to the exact approach 

# The day wise expenses 
df.groupby('Day')['INR'].mean().plot(kind='bar')

# On the basis of the month 

# df['Month'] = df['Date'].dt.month_name()

# noe using groupby 

# df.groupby('Month')['INR'].sum().plot(kind='bar')

# Month end 






# %%
