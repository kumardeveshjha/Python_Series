# Creating a multiindexing series 
# 1. A series is a 1-d array with index
# 2. A dataframe is a 2-d array with index and columns
# 3. A multiindexing series is a series with multiple index levels
# 4. A multiindexing dataframe is a dataframe with multiple index levels

#%%
import pandas as pd
import numpy as np

# creating a multiindexing series using custom logic

index_val = [('cse',2018),('cse',2019),('cse',2020),('ece',2018),('ece',2019),('ece',2020)]
a = pd.Series([101,102,103,201,202,203],index=index_val)

# a

# but this is not a multiindexing series and can be more difficult to handle


#Solution create a multiindex object and then use it to create a multiindexing series(hierarchical indexing)

# There are two ways to create a multiindex object
# 1. pd.MultiIndex.from_tuples() :it takes a list of tuples as input
# 2. pd.MultiIndex.from_product() : it takes a list of lists as input

multi_index = pd.MultiIndex.from_tuples(index_val)
multi_index
print(pd.MultiIndex.from_tuples([('cse',2018),('cse',2019),('cse',2020),('ece',2018),('ece',2019),('ece',2020)],names=['branch','year']))
multi_index.levels[0]  # decouples the multi_index into levels

#%%

#multi index from product 

multi_2 = pd.MultiIndex.from_product([['cse','ece'],[2018,2019,2020,2021]])

multi_2

# Creating a series with multiIndex object 
multi_series = pd.Series([1,2,3,4,5,6,7,8],index=multi_2)


# print(multi_series)

#Fetching data from multiindexing series
# print(multi_series['cse'])  # accessing all the years of cse
# multi_series['cse']

# Can we convert multiindex series to dataframe
# Yes using unstack() method

multi_df = multi_series.unstack()  # converts multiindex series to dataframe
# print(multi_series)  

# now convert it back to a series using stack() 

# multi_df.stack()


# Why we need the multiindexing objects
# It helps in showing higher dimensional data into 1-d(series) or 2d(dataframe) data


#%%

# Multi_Index DataFrame

branch_df = pd.DataFrame([
     [1,2],
     [3,4],
     [5,6],
     [7,8],
     [9,10],
     [11,12],
     [13,14],
     [15,16]
],index=multi_2,columns=['average_package','num_of_students'])

# print(branch_df)  # accessing all the years of cse for average package
# print(branch_df['average_package'])  # accessing all the year for average package

# using this we can create dataframe using columns and rows both 

branch_df2 = pd.DataFrame([
     [1,2,0,0],
     [5,6,0,0],
     [7,8,0,0],
     [9,10,0,0],
     
],index=[2020,2021,2022,2023],columns=pd.MultiIndex.from_product([['delhi','mumbai'],['average_package','num_of_students']]))

# in this we have the 3d indexing using index and 2d using the columns 
print(branch_df2['delhi'])  # accessing all the years of mumbai for average package
# print(branch_df2['delhi']['average_package'])  # accessing all the years of mumbai for average package
# print(branch_df2.loc[2020])  # accessing all the years of mumbai for average package


# %%

# now we will create both rows and columns multiindex 
branch_df3 = pd.DataFrame([
     [1,2,0,0],
     [3,4,0,0],
     [5,6,0,0],
     [7,8,0,0],
     [9,10,0,0],
     [11,12,0,0],
     [13,14,0,0],
     [15,16,0,0]
],index=pd.MultiIndex.from_product([['cse','ece'],[2020,2021,2022,2023]]),columns=pd.MultiIndex.from_product([['delhi','mumbai'],['average_package','num_of_students']]))


print(branch_df3)

# Stacking and Unstcking

# Stacking and stacking are the poereful techniques used in multiindex objects to make the data more operationsl means 
# converting the high dimensional data into 2d, 3d or even 3d series or dataframe to perform operations 

#%%
# print(branch_df,branch_df2,branch_df3)
# print(branch_df)

##::::::::: Unstack     Rows ---> Column (The best way to perform operations on the data is using the columns)

# print(branch_df.unstack()) # it will stack the columns to rows
# print(branch_df.unstack().unstack()) # it will stack the columns to rows


##::::::::::: Stack  columns to ----> Rows (level - 1 will of column will convert to the level -1 of series )


# print(branch_df2)
# print(branch_df2.stack()['delhi'])

print(branch_df3)
print(branch_df3.unstack().unstack())


#%%
# Working with multiindex dataframe 
# Multiindex dataframe is a dataframe on which you can do all operations as you do on dataframe 

# 1. head() and tail()

# branch_df3.head()

# 2. shape()

# branch_df3.shape

# info 

# branch_df3.info()

# duplicated 

# branch_df3.duplicated()

# branch_df3.isnull()


#%%
## :::::::::::; extracting rows 


print(branch_df3)

### using loc

# single row 
# print(branch_df3.loc[('cse',2020)])

# multiple row 
# print(branch_df3.loc[('cse',2020):('ece',2020):2])

### Using iloc 
# print(branch_df3.iloc[0:5:2])


#%%

###  :::::::::::; Extracting Columns 

print(branch_df3)

# Info of a single column 


# print(branch_df3['delhi']['average_package'])

# info of the multiple columns 

print(branch_df3.iloc[:,1:3])

# when we want to slice in both rows and columns 

print(branch_df3.iloc[0:5:4,1:3])

#using fency indexing
print(branch_df3.iloc[[0,4],[1,2]])


#%%
## Sorting index 

print(branch_df3)

# sort index

# print(branch_df3.sort_index(ascending=False))

# when want to sort rows and columns separately 

# print(branch_df3.sort_index(ascending=[True,False]))

# only at the one level sorting 

print(branch_df3.sort_index(level=1,ascending=[False]))


###:::::::::::::; Transpose and swaplevel 

#%%
## Transpose  :::::::: Converts the rows into column 


print(branch_df3)

# print(branch_df3.transpose())

## Swaplevel :::::: Swapes the levels of the index and columns (levels)

print(branch_df3.swaplevel())  # Swaping the index level 

print(branch_df3.swaplevel(axis=1))


## Long Vs Wide Data 

# Wide format:: is where we have a single row for every data point with multiple columns to hold the values of various attributes. 
# It is wide form of row in which there are multiple columns 

# Long Format:: is where, for each data point we have as many roes as the number of attributes and each row contains values of a particularattribut for a given data points 
# It is a wide form of rows and columns  



##::::::::: Melt --> wide to long dataformat

# simple example of the melt function 


#%%
# print(pd.DataFrame({'cse':[100]}))
# print(pd.DataFrame({'cse':[100]}).melt())

# melt --> multiple branch 
# print(pd.DataFrame({'cse':[120],'ece':[100],'IT':[120],'Mech':[80]}))
# print(pd.DataFrame({'cse':[120],'ece':[100],'IT':[120],'Mech':[80]}).melt())


# melt --> complex data beranch with year 


complex_melt = pd.DataFrame({
              'branches':['cse','ece','IT','mech'],
              '2020':[100,120,100,80],
              '2021':[120,110,130,70],
              '2022':[140,105,140,60],
              '2023':[160,100,150,50]
              }
             )

# print(complex_melt.melt(id_vars=['branches'],var_name='year',value_name='students'))


# Time series databases 

covid_death = pd.read_csv('dataset_3/time_series_covid19_deaths_global.csv')

confirm_covid = pd.read_csv('dataset_3/time_series_covid19_confirmed_global.csv')


# print(covidz_death.head())
# print(covid_death)


# Niw making the data melt 
# converting the long formate data

death = covid_death.melt(id_vars=['Province/State','Country/Region','Lat','Long'],var_name='date',value_name='no_of_deaths')

confirm = confirm_covid.melt(id_vars=['Province/State','Country/Region','Lat','Long'],var_name='date',value_name='num_of_cases')

final_data = confirm.merge(death,on=['Province/State','Country/Region','Lat','Long','date'])[['Province/State','Country/Region','date','num_of_cases','no_of_deaths']]

print(final_data)



















# %%
