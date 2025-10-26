#%%
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt



""" 2 """

student_data = [
     [100,70,10],
     [120,100,24],
     [80,60,4]
]


# %%
# print(pd.DataFrame(student_data,columns=['iq','marks','Packages']))


# Plotting Graph 
# plotted_data = pd.DataFrame(student_data,columns=['iq','marks','Packages'])

# plotted_data.plot(kind='pie',subplots=True)
# plt.show()


## --> Creating a DataFrame from Dictiomnary 

my_data = {
     'iq':[100,120,80,90,0,0],
     'Marks':[90,100,80,70,0,0],
     'Packages':[12,18,10,4,0,0]
}

# %%
my_data = pd.DataFrame(my_data)
# print(my_data)

## --> Real world Data Set. 

##  using read_csv

ipl = pd.read_csv('dataset/ipl-matches.csv')
movies = pd.read_csv('dataset/movies.csv')

# print(movies)

## Some important DataFrame Attributes and Methods

## 1. Shape 

# print(movies.shape)

## dtype 

# print(movies.dtypes)

## index

# print(movies.index)

## Column 

# print(movies.columns)

## Values 

# print(ipl.values)

##-->> Functions of DataFrame 

# Head and Tail 

# print(movies.head(1))
# print(movies.tail(1))

# Sample()

# print(ipl.sample())

# info() : High level info of the data it tell the info 

#%%
# print(ipl.info())

# dwscribe() : To give mathematical summary when we have numerical columns 

# print(movies.describe())
# print(ipl.describe())

## isnull()

# print(ipl.isnull().sum())

## duplicated()

# print(ipl.duplicated().sum())
# print(my_data.duplicated().sum())


## Rename() -->  It changes the name of the column 

# my_data.rename(columns={'Marks':'percent','Packages':'lpa'},inplace=True)

# print(my_data)



## Mathematical Functions 

# Sum : This applies to all the columns and each series of the column

# print(movies.sum()) 

# print(my_data.sum())

# ## Now usning : Axis argument 

# %%
# print(my_data.sum(axis=1))
# print(my_data.mean(axis=1))
# print(my_data.min(axis=1))
# print(my_data.max(axis=1))

#%% 

# To print any specific column
# print(movies[['movie']])

## now fetch multiple column 
# print(movies[["movies","year_of_release"]])


#### How to fetch rows 
#%%
my_data_2 = {
     'name': ["Dev","Devesh","Devendra","Neelam","Abhishek","Rishabh"],    
     'iq':[100,120,80,90,0,0],
     'Marks':[90,100,80,70,0,0],
     'Packages':[12,18,10,4,0,0]
}

student = pd.DataFrame(my_data_2)

print(student)

# iloc - searches using index positions returns a series
# loc - Searches using index labels basically the names 

## Single row 
# movies.iloc[0]

## multiple row 
# movies.iloc[0:5]

# fancy indexing 

# movies.iloc[[0,4,5]]


##--> loc --> Fetches the data using the index label

#%%
# print(student)
# student.loc['']
# print(student.loc[['Dev','Devesh']])



my_students  = {
     'names':["Astha","Neelam","Prachi","Neha","Raj"],
     'iq':[110,100,80,120,120],
     'marks':[85,85,70,95,95],
     'rank':[3,4,5,2,1]
}

my_students_data = pd.DataFrame(my_students,index=my_students['names'])

my_students_data
# my_students_data.iloc[0]
# my_students_data.loc['Neelam']

##-->> Both Rows and Column selection 

# student.iloc[0:2,0: ]



### ----->>************** Filtering the data **************************************


# using the ipl data 

# ipl.head(2)

# We will find the winner the final 

# mask = ipl['MatchNumber'] == 'Final'
# new_data = ipl[mask]
# new_data[["Season","WinningTeam","Team1","Team2"]]

#%%

# ipl[ipl['MatchNumber']=='Final'][["Season","WinningTeam"]].head(5)
 
# ipl[ipl['SuperOver']== "Y"][["Team1","Team2"]].shape[0]  # here shape gives the number of the ipl matches 

# ipl[ipl['City']== 'Kolkata'].shape

 
# ipl[(ipl['WinningTeam'] == 'Chennai Super Kings') & (ipl['City']== "Kolkata") & (ipl["MatchNumber"] == "Final")]


## Humein dekhana hai ki jitane teams ne toss jeeta unhone match jeeta.


# (ipl[ipl['TossWinner'] == ipl['WinningTeam']].shape[0]/ipl.shape[0])*100


# movies[(movies['imdb_rating'] > 8) & (movies["imdb_votes"] > 10000)].shape

# movies[movies['genres'].str.split('|').apply(lambda x: 'Action' in x)]

# spec_1 = movies['genres'].str.contains('Action')
# spec_2 = movies['imdb_rating'] > 7.5

# movies[spec_1 &  spec_2]
     

##--->> Adding a new column 

# movies['Country'] = "Bharat"

# movies

# Now to show the lead actor 

# actor = movies['actors'].str.split('|')

 


# Pandas Function 

# ipl.info()










 









# %%
