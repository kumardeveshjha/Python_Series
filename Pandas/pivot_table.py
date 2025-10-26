#%%

import numpy as np
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt



""" 6  """

##::::::::::::::::: Pivot table

# "The pivot table takes simple column-wise data as input, and groups the entries int a two-dimensional table that provides a multidimensional summarization of the data"

# It is a summarization function which gives the summary of high dimensional data 

df = sns.load_dataset('tips')
df.head()

# findin gthe average bill payments on the basis of the gender 
# df.groupby('sex')[['total_bill']].mean()

# usinb two attributes 

# print(df.groupby(['sex','smoker'])[['total_bill']].mean().unstack())

# the shortcut for the above code 

## using ivot table 

# df.pivot_table(index='sex',columns='smoker',values='total_bill')

# the default aggregate method is mean() 

# we can provide the aggregation method 

# print(df.pivot_table(index='sex',columns='smoker',values='total_bill',aggfunc='sum))


# All columns together --> when we don't specify any column (values) then it will show the all columns

# print(df.pivot_table(index='sex',columns='smoker')['size'])


## Multiindexing 

# df.pivot_table(index=['sex','smoker'],columns=['day','time'])

# Providing custom aggregate for individual columns 

# print(df.pivot_table(index=['sex','smoker'],columns=['day','time'],aggfunc={'size':'mean','tip':'max','total_bill':'sum'}))


### ::::::::;; margins 
# an extra row and column which sums the total 

# print(df.pivot_table(index='sex',columns='smoker',values='total_bill',aggfunc='sum',margins=True))


#%%

# plotting graph--> The pivot table 

df_1 = pd.read_csv('dataset_4/expense_data.csv')
# print(df_1.head())

# print(df_1['Category'].value_counts())


##:::::: Converting the string datetime(object) to datetime 

# df_1.info()  # here datetime is string we have to make it 

df_1['Date'] = pd.to_datetime(df_1['Date']) # now it is datetime 

# print(df_1.info()) 

# now extracting the month name from the date 
# and storing it as acolumn to our dataframe 

df_1['Month'] = df_1['Date'].dt.month_name()


#%%
# plotting the graph 
print('Hello')

# df_1.pivot_table(index='Month',columns='Category',values='INR',aggfunc='sum',fill_value=0).plot()
# df_1.pivot_table(index='Month',columns='Income/Expense',values='INR',aggfunc='sum',fill_value=0).plot()
# df_1.pivot_table(index='Month',columns='Account',values='INR',aggfunc='sum',fill_value=0).plot()


# print(plt.show())




















# %%
